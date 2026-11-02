#!/usr/bin/env python3
"""Validate six anonymous CSV inputs and regenerate one traceability report."""
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent.parent
NAMES = ('statement_anonym', 'codebook', 'questionnaire_items', 'correlations', 'patterns', 'links')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(name):
    with (PACKAGE / 'data' / (name + '.csv')).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def index(rows, key):
    require(len({r[key] for r in rows}) == len(rows), 'Duplicate ' + key)
    return {r[key]: r for r in rows}


def anchor(value):
    return re.sub(r'[^a-z0-9_-]', '-', value.lower())


def main():
    tables = {name: load(name) for name in NAMES}
    statements = index(tables['statement_anonym'], 'statement_id')
    codes = index(tables['codebook'], 'code')
    items = index(tables['questionnaire_items'], 'item_id')
    correlations = index(tables['correlations'], 'correlation_id')
    patterns = index(tables['patterns'], 'pattern_id')
    require((len(statements), len(codes), len(items), len(correlations), len(patterns)) == (63, 9, 22, 66, 10), 'Unexpected paper scope')
    require(all(list(r) == ['statement_id', 'direction'] for r in statements.values()), 'Unexpected anonymous statement schema')
    require(Counter(r['direction'] for r in statements.values()) == {'decrease': 33, 'increase': 30}, 'Question-context counts differ')
    for sid, r in statements.items():
        require(re.fullmatch(r'(DEC|INC)-\d{2}', sid) is not None, 'Invalid statement ID')
        require(r['direction'] == ('decrease' if sid.startswith('DEC') else 'increase'), 'Statement direction differs')

    metadata = {}
    alias_lookup = {}
    paper_items = defaultdict(set)
    for key, r in correlations.items():
        require(r['focal_variable'] in ('AI1', 'TD1', 'TD2') and r['item_id'] in items, 'Unresolved correlation variable')
        require(key == 'C-' + r['focal_variable'] + '-' + r['item_id'], 'Correlation key differs')
        require(-1 <= float(r['rho']) <= 1 and 0 <= float(r['p_value']) <= 1 and r['n'] == '70', 'Invalid numerical result')
        paper_id = r['manuscript_item_id']
        require(items[r['item_id']]['manuscript_item_id'] == paper_id, 'Manuscript item ID differs')
        require(r['item_id'] == {'EN2': 'EN2.c', 'PC3': 'PC3.a'}.get(paper_id, paper_id), 'Component ID differs')
        paper_items[paper_id].add(r['focal_variable'])
        require(r['qualitative_mapping_target'] in ('true', 'false'), 'Invalid mapping-target flag')
        if r['qualitative_mapping_target'] == 'true':
            metadata[key] = {'kind': 'correlation', 'label': r['mapping_label'], **r}
            values = re.search(r'ρ=([-\d.]+), p=([\d.]+), n=(\d+)', r['mapping_label'])
            require(values and (values[1], values[2], values[3]) == (r['rho'], r['p_value'], r['n']), 'Mapping label differs from numerical fields')
        else:
            require(not any(r[k] for k in ('mapping_label', 'archived_target_ids')), 'Unmapped result contains mapping metadata')
    require(set(items) == {r['item_id'] for r in correlations.values()}, 'Questionnaire and correlation scopes differ')
    require(len(paper_items) == 22 and all(v == {'AI1', 'TD1', 'TD2'} for v in paper_items.values()), 'Incomplete paper correlations')
    require(len(metadata) == 14, 'Unexpected qualitative correlation scope')
    for key, r in patterns.items():
        metadata[key] = {'kind': 'pattern', 'label': r['description'], **r}
    for key, r in metadata.items():
        aliases = r['archived_target_ids'].split('; ')
        for old in aliases:
            require(old and old not in alias_lookup, 'Invalid archived alias')
            alias_lookup[old] = key
    require(len(alias_lookup) == 24, 'Archived target count differs')

    by_statement = defaultdict(list)
    by_target = defaultdict(list)
    edge_keys = set()
    require(list(tables['links'][0]) == ['statement_id', 'target_type', 'target_id'], 'Unexpected link schema')
    catalogs = {'theme': codes, 'questionnaire_item': items,
                'correlation': {k: r for k, r in metadata.items() if r['kind'] == 'correlation'}, 'pattern': patterns}
    for r in tables['links']:
        sid, kind, target = r['statement_id'], r['target_type'], r['target_id']
        require(sid in statements and kind in catalogs and target in catalogs[kind], 'Unresolved link')
        require((sid, kind, target) not in edge_keys, 'Duplicate link')
        edge_keys.add((sid, kind, target))
        by_statement[sid].append(r)
        by_target[kind, target].append(r)
    counts_by_type = Counter(r['target_type'] for r in tables['links'])
    require(counts_by_type['theme'] == 224 and counts_by_type['questionnaire_item'] == 96 and counts_by_type['correlation'] + counts_by_type['pattern'] == 146 and len(edge_keys) == 466, 'Mapping counts differ')

    code_coverage = []
    for code, r in codes.items():
        coverage = Counter(statements[e['statement_id']]['direction'] for e in by_target['theme', code])
        require(all(coverage[d] == int(r[d + '_count']) for d in ('decrease', 'increase')), 'Content-code coverage differs')
        code_coverage.append({'code': code, **dict(coverage), 'matches_recorded_counts': True})
    item_coverage = []
    for item, r in items.items():
        coverage = Counter(statements[e['statement_id']]['direction'] for e in by_target['questionnaire_item', item])
        require(all(coverage[d] == int(r['archived_reported_' + d]) for d in ('decrease', 'increase')), 'Questionnaire coverage differs')
        item_coverage.append({'item_id': item, 'increase': coverage['increase'], 'decrease': coverage['decrease'], 'matches_archived_counts': True})
    for name in NAMES:
        text = (PACKAGE / 'data' / (name + '.csv')).read_text()
        require(re.search(r'(?:/Users/|/home/|file://|https?://|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,})', text) is None, 'Private path or contact remains')

    counts = {'statements': 63, 'coded_statements': sum(any(e['target_type'] == 'theme' for e in by_statement[s]) for s in statements),
              'content_codes': 9, 'questionnaire_items': 22, 'correlations': 66,
              'mapped_correlation_targets': 14, 'patterns': 10, 'theme_links': counts_by_type['theme'],
              'questionnaire_item_links': counts_by_type['questionnaire_item'],
              'correlation_pattern_links': counts_by_type['correlation'] + counts_by_type['pattern'],
              'total_links': len(edge_keys), 'archived_target_identifiers': len(alias_lookup)}
    lines = ['# Anonymous coding traceability', '', 'Statement IDs appear once; the reverse indexes link back to them.',
             'Recorded content assignments and mapping targets are preserved. Statement inputs contain only IDs and question context; statement text and interpretive notes are not included.', '', '## Coverage', '',
             '| Measure | Count |', '| --- | ---: |']
    lines += [f'| {k.replace("_", " ")} | {v} |' for k, v in counts.items()]
    lines += ['', 'All code and selected-item counts match their recorded coverage. Zero-link targets and unassigned statements remain included.', '',
              '## Content codebook', '']
    def statement_refs(edges):
        return ', '.join(f"[{e['statement_id']}](#{anchor(e['statement_id'])})" for e in edges) or 'None assigned.'
    for code, r in codes.items():
        lines += ['### ' + code, '', r['definition'], '', f"Decrease: {r['decrease_count']}; increase: {r['increase_count']}.", '',
                  statement_refs(by_target['theme', code]), '']

    lines += ['## Questionnaire items reported in the paper', '']
    for item, r in items.items():
        lines += [f'<a id="item-{anchor(item)}"></a>', '### ' + r['manuscript_item_id'] + ' — ' + r['label'], '',
                  'Internal ID: ' + item + '; area: ' + r['area'] + '.', '', 'Question: ' + r['question_wording'], '',
                  f"Recorded coverage: {r['archived_reported_decrease']} decrease and {r['archived_reported_increase']} increase statements.", '']
        lines += ['Linked statements: ' + statement_refs(by_target['questionnaire_item', item]), '']

    lines += ['## Reported correlations', '', 'AI1: AI use; TD1: perceived increase; TD2: perceived decrease. All numerical values reproduce the paper table.',
              'A reported p-value of 0.000 is rounded, not exactly zero.', '',
              '| Correlation ID | Focal measure | Paper item | rho | p | n | Qualitative mapping |', '| --- | --- | --- | ---: | ---: | ---: | --- |']
    for key, r in correlations.items():
        lines += [f"| <a id=\"{anchor(key)}\"></a>{key} | {r['focal_variable']} | {r['manuscript_item_id']} | {r['rho']} | {r['p_value']} | {r['n']} | {r['qualitative_mapping_target']} |"]
    lines += ['', '## Correlation and pattern evidence', '']
    for key, r in metadata.items():
        lines += [f'<a id="evidence-{anchor(key)}"></a>', '### ' + key, '', r['label'], '']
        if r['kind'] == 'pattern':
            lines += ['Stable manuscript reference: `' + r['manuscript_label'] + '`.', '']
        lines += ['Archived IDs: ' + r['archived_target_ids'] + '.', '']
        lines += ['Linked statements: ' + statement_refs(by_target[r['kind'], key]), '']

    lines += ['## Statement traceability', '', 'Each entry records an anonymous statement ID, question context, and retained connections.', '']
    for sid, r in statements.items():
        code_edges = [e for e in by_statement[sid] if e['target_type'] == 'theme']
        lines += [f'<a id="{anchor(sid)}"></a>', '### ' + sid, '',
                  'Question context: ' + r['direction'] + '.', '', 'Content codes: ' + ('; '.join(e['target_id'] for e in code_edges) or 'No assignment') + '.', '',
                  'Connections:', '']
        edges = [e for e in by_statement[sid] if e['target_type'] != 'theme']
        for e in edges:
            target = e['target_id']
            if e['target_type'] == 'questionnaire_item':
                label = items[target]['manuscript_item_id'] + ' — ' + items[target]['label']
                target_anchor = 'item-' + anchor(target)
            else:
                label = target
                target_anchor = 'evidence-' + anchor(target)
            lines += [f"- [{label}](#{target_anchor})"]
        if not edges:
            lines += ['No questionnaire or result connection is retained in the selected paper scope.']
        lines += ['']
    (PACKAGE / 'TRACEABILITY.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    checksums = {}
    for path in sorted(PACKAGE.rglob('*')):
        if path.is_file() and path.name != 'validation.json' and not {'.git', '__pycache__'}.intersection(path.relative_to(PACKAGE).parts):
            checksums[path.relative_to(PACKAGE).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    validation = {'schema_version': 8, 'status': 'passed', 'counts': counts,
                  'code_coverage_checks': code_coverage, 'item_coverage_checks': item_coverage, 'file_checksums': checksums}
    (PACKAGE / 'validation.json').write_text(json.dumps(validation, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'passed', **counts}, indent=2))


if __name__ == '__main__':
    main()
