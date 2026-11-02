# Anonymous coding traceability

Statement IDs appear once; the reverse indexes link back to them.
Recorded content assignments and mapping targets are preserved. Statement inputs contain only IDs and question context; statement text and interpretive notes are not included.

## Coverage

| Measure | Count |
| --- | ---: |
| statements | 63 |
| coded statements | 60 |
| content codes | 9 |
| questionnaire items | 22 |
| correlations | 66 |
| mapped correlation targets | 14 |
| patterns | 10 |
| theme links | 224 |
| questionnaire item links | 96 |
| correlation pattern links | 146 |
| total links | 466 |
| archived target identifiers | 24 |

All code and selected-item counts match their recorded coverage. Zero-link targets and unassigned statements remain included.

## Content codebook

### type of debt

Identifies a debt type or a concrete debt-related quality problem, such as code debt, architectural debt, duplication, dead code or obsolete code. A reference to code or tests alone is insufficient to infer a debt type.

Decrease: 9; increase: 10.

[DEC-01](#dec-01), [DEC-09](#dec-09), [DEC-12](#dec-12), [DEC-15](#dec-15), [DEC-17](#dec-17), [DEC-25](#dec-25), [DEC-30](#dec-30), [DEC-31](#dec-31), [DEC-32](#dec-32), [INC-03](#inc-03), [INC-05](#inc-05), [INC-08](#inc-08), [INC-10](#inc-10), [INC-12](#inc-12), [INC-13](#inc-13), [INC-19](#inc-19), [INC-20](#inc-20), [INC-22](#inc-22), [INC-30](#inc-30)

### tool

Names a product, platform or model/tool class, or explicitly identifies agentic/autonomous assistance. A generic reference to AI alone is insufficient; activities such as code review or assistant-driven coding are coded as process unless a tool is also identified.

Decrease: 10; increase: 4.

[DEC-03](#dec-03), [DEC-08](#dec-08), [DEC-09](#dec-09), [DEC-13](#dec-13), [DEC-18](#dec-18), [DEC-19](#dec-19), [DEC-24](#dec-24), [DEC-25](#dec-25), [DEC-27](#dec-27), [DEC-29](#dec-29), [INC-10](#inc-10), [INC-12](#inc-12), [INC-17](#inc-17), [INC-28](#inc-28)

### process

Describes a development or maintenance activity or workflow, including generation, review, verification, refactoring, testing, prompting, investigation, reuse or integration.

Decrease: 28; increase: 21.

[DEC-01](#dec-01), [DEC-02](#dec-02), [DEC-03](#dec-03), [DEC-04](#dec-04), [DEC-05](#dec-05), [DEC-06](#dec-06), [DEC-07](#dec-07), [DEC-08](#dec-08), [DEC-09](#dec-09), [DEC-11](#dec-11), [DEC-14](#dec-14), [DEC-15](#dec-15), [DEC-16](#dec-16), [DEC-17](#dec-17), [DEC-18](#dec-18), [DEC-19](#dec-19), [DEC-20](#dec-20), [DEC-22](#dec-22), [DEC-23](#dec-23), [DEC-24](#dec-24), [DEC-25](#dec-25), [DEC-26](#dec-26), [DEC-27](#dec-27), [DEC-29](#dec-29), [DEC-30](#dec-30), [DEC-31](#dec-31), [DEC-32](#dec-32), [DEC-33](#dec-33), [INC-02](#inc-02), [INC-03](#inc-03), [INC-05](#inc-05), [INC-06](#inc-06), [INC-07](#inc-07), [INC-08](#inc-08), [INC-09](#inc-09), [INC-10](#inc-10), [INC-11](#inc-11), [INC-12](#inc-12), [INC-13](#inc-13), [INC-14](#inc-14), [INC-16](#inc-16), [INC-19](#inc-19), [INC-20](#inc-20), [INC-21](#inc-21), [INC-22](#inc-22), [INC-23](#inc-23), [INC-24](#inc-24), [INC-25](#inc-25), [INC-29](#inc-29)

### benefit

Describes a reported or anticipated useful effect, such as ease, speed, improved code, assistance, TD reduction or prevention. A reported absence of AI-related TD increase is also a favorable outcome; it does not imply repayment of existing debt.

Decrease: 23; increase: 8.

[DEC-01](#dec-01), [DEC-04](#dec-04), [DEC-05](#dec-05), [DEC-06](#dec-06), [DEC-08](#dec-08), [DEC-09](#dec-09), [DEC-10](#dec-10), [DEC-11](#dec-11), [DEC-12](#dec-12), [DEC-15](#dec-15), [DEC-16](#dec-16), [DEC-17](#dec-17), [DEC-18](#dec-18), [DEC-19](#dec-19), [DEC-20](#dec-20), [DEC-21](#dec-21), [DEC-22](#dec-22), [DEC-25](#dec-25), [DEC-29](#dec-29), [DEC-30](#dec-30), [DEC-31](#dec-31), [DEC-32](#dec-32), [DEC-33](#dec-33), [INC-01](#inc-01), [INC-02](#inc-02), [INC-04](#inc-04), [INC-19](#inc-19), [INC-21](#inc-21), [INC-23](#inc-23), [INC-24](#inc-24), [INC-26](#inc-26)

### limitation

Describes a constraint, failure, risk, negative effect, capability gap or explicit uncertainty about a claim. Conditions that restrict usefulness can receive this tag alongside benefit.

Decrease: 13; increase: 21.

[DEC-05](#dec-05), [DEC-12](#dec-12), [DEC-15](#dec-15), [DEC-17](#dec-17), [DEC-19](#dec-19), [DEC-20](#dec-20), [DEC-21](#dec-21), [DEC-23](#dec-23), [DEC-24](#dec-24), [DEC-25](#dec-25), [DEC-26](#dec-26), [DEC-29](#dec-29), [DEC-32](#dec-32), [INC-02](#inc-02), [INC-03](#inc-03), [INC-04](#inc-04), [INC-05](#inc-05), [INC-06](#inc-06), [INC-08](#inc-08), [INC-09](#inc-09), [INC-10](#inc-10), [INC-11](#inc-11), [INC-12](#inc-12), [INC-13](#inc-13), [INC-14](#inc-14), [INC-16](#inc-16), [INC-17](#inc-17), [INC-19](#inc-19), [INC-20](#inc-20), [INC-22](#inc-22), [INC-23](#inc-23), [INC-25](#inc-25), [INC-29](#inc-29), [INC-30](#inc-30)

### example

Provides a concrete artefact, prompt, workflow configuration or situation illustrating a claim. A tool name or a generic activity alone is insufficient.

Decrease: 7; increase: 7.

[DEC-01](#dec-01), [DEC-04](#dec-04), [DEC-06](#dec-06), [DEC-19](#dec-19), [DEC-22](#dec-22), [DEC-27](#dec-27), [DEC-30](#dec-30), [INC-03](#inc-03), [INC-05](#inc-05), [INC-08](#inc-08), [INC-12](#inc-12), [INC-19](#inc-19), [INC-20](#inc-20), [INC-23](#inc-23)

### specification

Identifies rules, standards, requirements, prompts, instructions, codebase context or configuration that guide AI behavior or provide criteria for its output.

Decrease: 7; increase: 8.

[DEC-05](#dec-05), [DEC-06](#dec-06), [DEC-17](#dec-17), [DEC-19](#dec-19), [DEC-20](#dec-20), [DEC-27](#dec-27), [DEC-31](#dec-31), [INC-03](#inc-03), [INC-10](#inc-10), [INC-12](#inc-12), [INC-13](#inc-13), [INC-17](#inc-17), [INC-19](#inc-19), [INC-23](#inc-23), [INC-30](#inc-30)

### scope

States boundaries or extent, such as task size or complexity, code versus architecture, new versus legacy work, user expertise, or the stated extent of use or impact. Generic task mentions and hedging alone are insufficient.

Decrease: 16; increase: 14.

[DEC-04](#dec-04), [DEC-05](#dec-05), [DEC-07](#dec-07), [DEC-08](#dec-08), [DEC-11](#dec-11), [DEC-15](#dec-15), [DEC-16](#dec-16), [DEC-17](#dec-17), [DEC-18](#dec-18), [DEC-19](#dec-19), [DEC-21](#dec-21), [DEC-22](#dec-22), [DEC-23](#dec-23), [DEC-25](#dec-25), [DEC-29](#dec-29), [DEC-33](#dec-33), [INC-01](#inc-01), [INC-03](#inc-03), [INC-10](#inc-10), [INC-14](#inc-14), [INC-15](#inc-15), [INC-16](#inc-16), [INC-17](#inc-17), [INC-19](#inc-19), [INC-21](#inc-21), [INC-23](#inc-23), [INC-24](#inc-24), [INC-25](#inc-25), [INC-26](#inc-26), [INC-28](#inc-28)

### decision

Addresses task selection, output acceptance or rejection, assessment of alternatives, priorities, or responsibility for human/AI judgment. Merely naming a task does not establish a decision.

Decrease: 5; increase: 13.

[DEC-04](#dec-04), [DEC-14](#dec-14), [DEC-18](#dec-18), [DEC-20](#dec-20), [DEC-26](#dec-26), [INC-03](#inc-03), [INC-08](#inc-08), [INC-09](#inc-09), [INC-11](#inc-11), [INC-12](#inc-12), [INC-14](#inc-14), [INC-16](#inc-16), [INC-17](#inc-17), [INC-20](#inc-20), [INC-21](#inc-21), [INC-22](#inc-22), [INC-24](#inc-24), [INC-29](#inc-29)

## Questionnaire items reported in the paper

<a id="item-ba1"></a>
### BA1 — Experience

Internal ID: BA1; area: Background.

Question: What is your experience with software development?

Recorded coverage: 2 decrease and 4 increase statements.

Linked statements: [DEC-21](#dec-21), [DEC-23](#dec-23), [INC-10](#inc-10), [INC-16](#inc-16), [INC-23](#inc-23), [INC-25](#inc-25)

<a id="item-ba3"></a>
### BA3 — Team size

Internal ID: BA3; area: Background.

Question: What is the size of your team?

Recorded coverage: 0 decrease and 0 increase statements.

Linked statements: None assigned.

<a id="item-kn1"></a>
### KN1 — Use of TD in the organization

Internal ID: KN1; area: Knowledge.

Question: We use the term "Technical Debt" when communicating across the organization

Recorded coverage: 0 decrease and 0 increase statements.

Linked statements: None assigned.

<a id="item-kn2"></a>
### KN2 — Existing guidelines to manage TD

Internal ID: KN2; area: Knowledge.

Question: In our organization, guidelines are available for guidance on how to manage Technical Debt

Recorded coverage: 3 decrease and 3 increase statements.

Linked statements: [DEC-05](#dec-05), [DEC-17](#dec-17), [DEC-27](#dec-27), [INC-03](#inc-03), [INC-10](#inc-10), [INC-17](#inc-17)

<a id="item-aw1"></a>
### AW1 — Percentage of time wasted because of TD

Internal ID: AW1; area: Awareness.

Question: On average, how much % of the total development time do you estimate was spent by your team(s) on extra activities due to the presence of Technical Debt in the system(s)?

Recorded coverage: 3 decrease and 2 increase statements.

Linked statements: [DEC-04](#dec-04), [DEC-18](#dec-18), [DEC-29](#dec-29), [INC-03](#inc-03), [INC-12](#inc-12)

<a id="item-aw2"></a>
### AW2 — Missed business opportunities

Internal ID: AW2; area: Awareness.

Question: We have missed business opportunities because of existing Technical Debt in the system(s) (e.g. we could not implement new features, new projects, we could not acquire new customers)

Recorded coverage: 0 decrease and 0 increase statements.

Linked statements: None assigned.

<a id="item-en2-c"></a>
### EN2 — Encouragement from other managers — deliberately take on TD for benefits

Internal ID: EN2.c; area: Encouragement.

Question: Other managers (inlcuding engineering managers) encourage my team to: [Deliberate taking on TD if they get benefits out of it (e.g. to speed up a delivery)]

Recorded coverage: 0 decrease and 0 increase statements.

Linked statements: None assigned.

<a id="item-ed1"></a>
### ED1 — Facilitation of education sessions

Internal ID: ED1; area: Education.

Question: I have facilitated and/or participated in knowledge sharing sessions on the management of TD (e.g. education sessions, seminars, interest groups inthecompany,etc.)

Recorded coverage: 2 decrease and 3 increase statements.

Linked statements: [DEC-21](#dec-21), [DEC-23](#dec-23), [INC-10](#inc-10), [INC-16](#inc-16), [INC-25](#inc-25)

<a id="item-or1"></a>
### OR1 — Clarity of budget responsibility

Internal ID: OR1; area: Organization.

Question: It's clear for me and my team who is responsible to approve or deny budget (e.g. team capacity, team bandwidth) to remove TD

Recorded coverage: 0 decrease and 0 increase statements.

Linked statements: None assigned.

<a id="item-or2"></a>
### OR2 — Follow-up on TD decisions

Internal ID: OR2; area: Organization.

Question: Someone will check if I have successfully removed TD (e.g. by code reviews etc.) and how much time was spent on the activity (it could be a manger, an architect, another team member, etc.)

Recorded coverage: 2 decrease and 2 increase statements.

Linked statements: [DEC-14](#dec-14), [DEC-27](#dec-27), [INC-21](#inc-21), [INC-24](#inc-24)

<a id="item-pc1"></a>
### PC1 — Understanding of TD risks

Internal ID: PC1; area: Process.

Question: It’s easy for me to understand if the current TD in the system(s) is risky (e.g. leading to negative consequences) or not

Recorded coverage: 5 decrease and 7 increase statements.

Linked statements: [DEC-01](#dec-01), [DEC-15](#dec-15), [DEC-21](#dec-21), [DEC-23](#dec-23), [DEC-26](#dec-26), [INC-08](#inc-08), [INC-11](#inc-11), [INC-16](#inc-16), [INC-17](#inc-17), [INC-23](#inc-23), [INC-25](#inc-25), [INC-29](#inc-29)

<a id="item-pc2"></a>
### PC2 — Systematic and iterative process

Internal ID: PC2; area: Process.

Question: My team iteratively engages in a systematic assessment (discussing costs, benefits and risks) of TD (this includes re-assessing known TD)

Recorded coverage: 2 decrease and 3 increase statements.

Linked statements: [DEC-14](#dec-14), [DEC-27](#dec-27), [INC-12](#inc-12), [INC-21](#inc-21), [INC-24](#inc-24)

<a id="item-pc3-a"></a>
### PC3 — Dedicated time to manage TD — formal allocation

Internal ID: PC3.a; area: Process.

Question: We have formally allocated time for removing TD

Recorded coverage: 3 decrease and 2 increase statements.

Linked statements: [DEC-04](#dec-04), [DEC-18](#dec-18), [DEC-29](#dec-29), [INC-03](#inc-03), [INC-10](#inc-10)

<a id="item-to1"></a>
### TO1 — Use of data and measurements

Internal ID: TO1; area: Tools.

Question: We use data and measurements to assess TD costs and benefits

Recorded coverage: 0 decrease and 0 increase statements.

Linked statements: None assigned.

<a id="item-to2"></a>
### TO2 — Tools chosen by teams

Internal ID: TO2; area: Tools.

Question: Are the current tools in your organization to manage TD more chosen by the teams or more chosen as standard tools by the organization? (adjust the bar to one or the other extreme according to your experience with the tools that you can use to manage TD)

Recorded coverage: 5 decrease and 2 increase statements.

Linked statements: [DEC-03](#dec-03), [DEC-13](#dec-13), [DEC-18](#dec-18), [DEC-27](#dec-27), [DEC-29](#dec-29), [INC-10](#inc-10), [INC-28](#inc-28)

<a id="item-or3"></a>
### OR3 — Clarity of technical responsibility

Internal ID: OR3; area: Organization.

Question: It's clear for me and my team who is responsible for technical support if we need to add or remove TD that can affect other teams

Recorded coverage: 1 decrease and 1 increase statements.

Linked statements: [DEC-18](#dec-18), [INC-03](#inc-03)

<a id="item-pc5"></a>
### PC5 — Removal of TD

Internal ID: PC5; area: Process.

Question: To what extent do you remove code-TD before releasing the software?

Recorded coverage: 14 decrease and 2 increase statements.

Linked statements: [DEC-04](#dec-04), [DEC-06](#dec-06), [DEC-11](#dec-11), [DEC-14](#dec-14), [DEC-15](#dec-15), [DEC-17](#dec-17), [DEC-18](#dec-18), [DEC-22](#dec-22), [DEC-25](#dec-25), [DEC-29](#dec-29), [DEC-30](#dec-30), [DEC-31](#dec-31), [DEC-32](#dec-32), [DEC-33](#dec-33), [INC-08](#inc-08), [INC-14](#inc-14)

<a id="item-pc6"></a>
### PC6 — Tracking of larger TD items

Internal ID: PC6; area: Process.

Question: We track the bigger TD issues in our official backlogs, together with details on their cost to remove and their risks if not removed (bigger issues are e.g. multiple architectural componentsthatmightaffectotherteams)

Recorded coverage: 0 decrease and 0 increase statements.

Linked statements: None assigned.

<a id="item-pc7"></a>
### PC7 — Helpfulness of code reviews

Internal ID: PC7; area: Process.

Question: I think that, in our organization, code reviews helps identifying TD

Recorded coverage: 7 decrease and 9 increase statements.

Linked statements: [DEC-02](#dec-02), [DEC-03](#dec-03), [DEC-09](#dec-09), [DEC-14](#dec-14), [DEC-15](#dec-15), [DEC-25](#dec-25), [DEC-27](#dec-27), [INC-03](#inc-03), [INC-08](#inc-08), [INC-09](#inc-09), [INC-10](#inc-10), [INC-12](#inc-12), [INC-14](#inc-14), [INC-16](#inc-16), [INC-21](#inc-21), [INC-24](#inc-24)

<a id="item-to6"></a>
### TO6 — Confidence in code analyzers

Internal ID: TO6; area: Tools.

Question: We confidently use the output of code analyzers to identify TD automatically and plan refactoring

Recorded coverage: 4 decrease and 0 increase statements.

Linked statements: [DEC-01](#dec-01), [DEC-07](#dec-07), [DEC-09](#dec-09), [DEC-30](#dec-30)

<a id="item-to7"></a>
### TO7 — Confidence in risk-assessment tools

Internal ID: TO7; area: Tools.

Question: We confidently use the output of tools to identify the costs and risks associated to TD to prioritize its removal

Recorded coverage: 0 decrease and 0 increase statements.

Linked statements: None assigned.

<a id="item-to8"></a>
### TO8 — Tools supporting TD level assessment and planning

Internal ID: TO8; area: Tools.

Question: We confidently use the output of a tool to visualize the overall level of TD in our system(s), its costs and risks to plan future development

Recorded coverage: 2 decrease and 1 increase statements.

Linked statements: [DEC-18](#dec-18), [DEC-20](#dec-20), [INC-17](#inc-17)

## Reported correlations

AI1: AI use; TD1: perceived increase; TD2: perceived decrease. All numerical values reproduce the paper table.
A reported p-value of 0.000 is rounded, not exactly zero.

| Correlation ID | Focal measure | Paper item | rho | p | n | Qualitative mapping |
| --- | --- | --- | ---: | ---: | ---: | --- |
| <a id="c-ai1-ba1"></a>C-AI1-BA1 | AI1 | BA1 | 0.019 | 0.879 | 70 | false |
| <a id="c-td1-ba1"></a>C-TD1-BA1 | TD1 | BA1 | 0.002 | 0.988 | 70 | false |
| <a id="c-td2-ba1"></a>C-TD2-BA1 | TD2 | BA1 | -0.072 | 0.553 | 70 | false |
| <a id="c-ai1-ba3"></a>C-AI1-BA3 | AI1 | BA3 | 0.121 | 0.317 | 70 | false |
| <a id="c-td1-ba3"></a>C-TD1-BA3 | TD1 | BA3 | 0.062 | 0.608 | 70 | false |
| <a id="c-td2-ba3"></a>C-TD2-BA3 | TD2 | BA3 | 0.062 | 0.611 | 70 | false |
| <a id="c-ai1-kn1"></a>C-AI1-KN1 | AI1 | KN1 | 0.300 | 0.012 | 70 | true |
| <a id="c-td1-kn1"></a>C-TD1-KN1 | TD1 | KN1 | 0.042 | 0.729 | 70 | false |
| <a id="c-td2-kn1"></a>C-TD2-KN1 | TD2 | KN1 | 0.083 | 0.494 | 70 | false |
| <a id="c-ai1-kn2"></a>C-AI1-KN2 | AI1 | KN2 | 0.236 | 0.049 | 70 | false |
| <a id="c-td1-kn2"></a>C-TD1-KN2 | TD1 | KN2 | -0.002 | 0.987 | 70 | false |
| <a id="c-td2-kn2"></a>C-TD2-KN2 | TD2 | KN2 | -0.032 | 0.792 | 70 | false |
| <a id="c-ai1-aw1"></a>C-AI1-AW1 | AI1 | AW1 | -0.036 | 0.765 | 70 | false |
| <a id="c-td1-aw1"></a>C-TD1-AW1 | TD1 | AW1 | 0.014 | 0.905 | 70 | false |
| <a id="c-td2-aw1"></a>C-TD2-AW1 | TD2 | AW1 | 0.186 | 0.123 | 70 | false |
| <a id="c-ai1-aw2"></a>C-AI1-AW2 | AI1 | AW2 | -0.134 | 0.268 | 70 | false |
| <a id="c-td1-aw2"></a>C-TD1-AW2 | TD1 | AW2 | 0.041 | 0.735 | 70 | false |
| <a id="c-td2-aw2"></a>C-TD2-AW2 | TD2 | AW2 | 0.072 | 0.553 | 70 | false |
| <a id="c-ai1-en2-c"></a>C-AI1-EN2.c | AI1 | EN2 | 0.313 | 0.008 | 70 | true |
| <a id="c-td1-en2-c"></a>C-TD1-EN2.c | TD1 | EN2 | 0.183 | 0.129 | 70 | false |
| <a id="c-td2-en2-c"></a>C-TD2-EN2.c | TD2 | EN2 | 0.034 | 0.778 | 70 | false |
| <a id="c-ai1-ed1"></a>C-AI1-ED1 | AI1 | ED1 | 0.172 | 0.154 | 70 | false |
| <a id="c-td1-ed1"></a>C-TD1-ED1 | TD1 | ED1 | 0.112 | 0.358 | 70 | false |
| <a id="c-td2-ed1"></a>C-TD2-ED1 | TD2 | ED1 | -0.032 | 0.792 | 70 | false |
| <a id="c-ai1-or1"></a>C-AI1-OR1 | AI1 | OR1 | 0.345 | 0.003 | 70 | true |
| <a id="c-td1-or1"></a>C-TD1-OR1 | TD1 | OR1 | -0.252 | 0.035 | 70 | false |
| <a id="c-td2-or1"></a>C-TD2-OR1 | TD2 | OR1 | 0.323 | 0.006 | 70 | true |
| <a id="c-ai1-or2"></a>C-AI1-OR2 | AI1 | OR2 | 0.225 | 0.062 | 70 | false |
| <a id="c-td1-or2"></a>C-TD1-OR2 | TD1 | OR2 | 0.040 | 0.742 | 70 | false |
| <a id="c-td2-or2"></a>C-TD2-OR2 | TD2 | OR2 | 0.008 | 0.945 | 70 | false |
| <a id="c-ai1-pc1"></a>C-AI1-PC1 | AI1 | PC1 | -0.086 | 0.477 | 70 | false |
| <a id="c-td1-pc1"></a>C-TD1-PC1 | TD1 | PC1 | 0.082 | 0.502 | 70 | false |
| <a id="c-td2-pc1"></a>C-TD2-PC1 | TD2 | PC1 | 0.077 | 0.528 | 70 | false |
| <a id="c-ai1-pc2"></a>C-AI1-PC2 | AI1 | PC2 | 0.341 | 0.004 | 70 | true |
| <a id="c-td1-pc2"></a>C-TD1-PC2 | TD1 | PC2 | -0.091 | 0.453 | 70 | false |
| <a id="c-td2-pc2"></a>C-TD2-PC2 | TD2 | PC2 | 0.116 | 0.341 | 70 | false |
| <a id="c-ai1-pc3-a"></a>C-AI1-PC3.a | AI1 | PC3 | 0.447 | 0.000 | 70 | true |
| <a id="c-td1-pc3-a"></a>C-TD1-PC3.a | TD1 | PC3 | -0.113 | 0.350 | 70 | false |
| <a id="c-td2-pc3-a"></a>C-TD2-PC3.a | TD2 | PC3 | 0.137 | 0.258 | 70 | false |
| <a id="c-ai1-to1"></a>C-AI1-TO1 | AI1 | TO1 | 0.366 | 0.002 | 70 | true |
| <a id="c-td1-to1"></a>C-TD1-TO1 | TD1 | TO1 | -0.126 | 0.298 | 70 | false |
| <a id="c-td2-to1"></a>C-TD2-TO1 | TD2 | TO1 | 0.097 | 0.425 | 70 | false |
| <a id="c-ai1-to2"></a>C-AI1-TO2 | AI1 | TO2 | 0.267 | 0.026 | 70 | false |
| <a id="c-td1-to2"></a>C-TD1-TO2 | TD1 | TO2 | 0.086 | 0.479 | 70 | false |
| <a id="c-td2-to2"></a>C-TD2-TO2 | TD2 | TO2 | 0.036 | 0.769 | 70 | false |
| <a id="c-ai1-or3"></a>C-AI1-OR3 | AI1 | OR3 | 0.313 | 0.008 | 70 | true |
| <a id="c-td1-or3"></a>C-TD1-OR3 | TD1 | OR3 | -0.086 | 0.480 | 70 | false |
| <a id="c-td2-or3"></a>C-TD2-OR3 | TD2 | OR3 | 0.084 | 0.491 | 70 | false |
| <a id="c-ai1-pc5"></a>C-AI1-PC5 | AI1 | PC5 | 0.376 | 0.001 | 70 | true |
| <a id="c-td1-pc5"></a>C-TD1-PC5 | TD1 | PC5 | 0.109 | 0.369 | 70 | false |
| <a id="c-td2-pc5"></a>C-TD2-PC5 | TD2 | PC5 | 0.383 | 0.001 | 70 | true |
| <a id="c-ai1-pc6"></a>C-AI1-PC6 | AI1 | PC6 | 0.317 | 0.007 | 70 | true |
| <a id="c-td1-pc6"></a>C-TD1-PC6 | TD1 | PC6 | -0.086 | 0.481 | 70 | false |
| <a id="c-td2-pc6"></a>C-TD2-PC6 | TD2 | PC6 | 0.200 | 0.097 | 70 | false |
| <a id="c-ai1-pc7"></a>C-AI1-PC7 | AI1 | PC7 | 0.157 | 0.195 | 70 | false |
| <a id="c-td1-pc7"></a>C-TD1-PC7 | TD1 | PC7 | -0.036 | 0.770 | 70 | false |
| <a id="c-td2-pc7"></a>C-TD2-PC7 | TD2 | PC7 | 0.370 | 0.002 | 70 | true |
| <a id="c-ai1-to6"></a>C-AI1-TO6 | AI1 | TO6 | 0.316 | 0.008 | 70 | true |
| <a id="c-td1-to6"></a>C-TD1-TO6 | TD1 | TO6 | 0.155 | 0.199 | 70 | false |
| <a id="c-td2-to6"></a>C-TD2-TO6 | TD2 | TO6 | 0.290 | 0.015 | 70 | false |
| <a id="c-ai1-to7"></a>C-AI1-TO7 | AI1 | TO7 | 0.257 | 0.032 | 70 | false |
| <a id="c-td1-to7"></a>C-TD1-TO7 | TD1 | TO7 | -0.058 | 0.634 | 70 | false |
| <a id="c-td2-to7"></a>C-TD2-TO7 | TD2 | TO7 | 0.197 | 0.102 | 70 | false |
| <a id="c-ai1-to8"></a>C-AI1-TO8 | AI1 | TO8 | 0.319 | 0.007 | 70 | true |
| <a id="c-td1-to8"></a>C-TD1-TO8 | TD1 | TO8 | -0.026 | 0.832 | 70 | false |
| <a id="c-td2-to8"></a>C-TD2-TO8 | TD2 | TO8 | 0.235 | 0.050 | 70 | false |

## Correlation and pattern evidence

<a id="evidence-c-ai1-kn1"></a>
### C-AI1-KN1

AI use ↔ Use of TD in the organization; ρ=0.300, p=0.012, n=70

Archived IDs: III:KN1.

Linked statements: None assigned.

<a id="evidence-c-ai1-en2-c"></a>
### C-AI1-EN2.c

AI use ↔ Encouragement from other managers (taking on TD); ρ=0.313, p=0.008, n=70

Archived IDs: III:EN2.

Linked statements: None assigned.

<a id="evidence-c-ai1-or1"></a>
### C-AI1-OR1

AI use ↔ Clarity of budget responsibility; ρ=0.345, p=0.003, n=70

Archived IDs: III:OR1.

Linked statements: None assigned.

<a id="evidence-c-td2-or1"></a>
### C-TD2-OR1

perceived TD decrease ↔ Clarity of budget responsibility; ρ=0.323, p=0.006, n=70

Archived IDs: V:OR1.

Linked statements: None assigned.

<a id="evidence-c-ai1-pc2"></a>
### C-AI1-PC2

AI use ↔ Systematic and iterative process; ρ=0.341, p=0.004, n=70

Archived IDs: III:PC2.

Linked statements: [DEC-14](#dec-14), [DEC-27](#dec-27)

<a id="evidence-c-ai1-pc3-a"></a>
### C-AI1-PC3.a

AI use ↔ Dedicated time to manage TD; ρ=0.447, p=0.000, n=70

Archived IDs: III:PC3.

Linked statements: [DEC-04](#dec-04), [DEC-18](#dec-18), [DEC-29](#dec-29)

<a id="evidence-c-ai1-to1"></a>
### C-AI1-TO1

AI use ↔ Use of data and measurements; ρ=0.366, p=0.002, n=70

Archived IDs: III:TO1.

Linked statements: None assigned.

<a id="evidence-c-ai1-or3"></a>
### C-AI1-OR3

AI use ↔ Clarity of technical responsibility; ρ=0.313, p=0.008, n=70

Archived IDs: III:OR3.

Linked statements: None assigned.

<a id="evidence-c-ai1-pc5"></a>
### C-AI1-PC5

AI use ↔ Removal of TD; ρ=0.376, p=0.001, n=70

Archived IDs: III:PC5.

Linked statements: [DEC-04](#dec-04), [DEC-06](#dec-06), [DEC-11](#dec-11), [DEC-17](#dec-17), [DEC-18](#dec-18), [DEC-22](#dec-22), [DEC-25](#dec-25), [DEC-29](#dec-29), [DEC-30](#dec-30), [DEC-31](#dec-31), [DEC-32](#dec-32), [DEC-33](#dec-33)

<a id="evidence-c-td2-pc5"></a>
### C-TD2-PC5

perceived TD decrease ↔ Removal of TD; ρ=0.383, p=0.001, n=70

Archived IDs: V:PC5.

Linked statements: [DEC-04](#dec-04), [DEC-06](#dec-06), [DEC-11](#dec-11), [DEC-17](#dec-17), [DEC-18](#dec-18), [DEC-22](#dec-22), [DEC-25](#dec-25), [DEC-29](#dec-29), [DEC-30](#dec-30), [DEC-31](#dec-31), [DEC-32](#dec-32), [DEC-33](#dec-33)

<a id="evidence-c-ai1-pc6"></a>
### C-AI1-PC6

AI use ↔ Tracking of larger TD items; ρ=0.317, p=0.007, n=70

Archived IDs: III:PC6.

Linked statements: None assigned.

<a id="evidence-c-td2-pc7"></a>
### C-TD2-PC7

perceived TD decrease ↔ Helpfulness of code reviews; ρ=0.370, p=0.002, n=70

Archived IDs: V:PC7.

Linked statements: [DEC-02](#dec-02), [DEC-03](#dec-03), [DEC-09](#dec-09), [DEC-14](#dec-14), [DEC-15](#dec-15), [DEC-25](#dec-25), [DEC-27](#dec-27), [INC-03](#inc-03), [INC-08](#inc-08), [INC-10](#inc-10), [INC-12](#inc-12), [INC-14](#inc-14), [INC-21](#inc-21)

<a id="evidence-c-ai1-to6"></a>
### C-AI1-TO6

AI use ↔ Confidence in code analyzers; ρ=0.316, p=0.008, n=70

Archived IDs: III:TO6.

Linked statements: [DEC-01](#dec-01), [DEC-07](#dec-07)

<a id="evidence-c-ai1-to8"></a>
### C-AI1-TO8

AI use ↔ Tools supporting TD level assessment and planning; ρ=0.319, p=0.007, n=70

Archived IDs: III:TO8.

Linked statements: None assigned.

<a id="evidence-f02"></a>
### F02

Relationship between AI use and increased technical debt.

Stable manuscript reference: `fig:ai-increment-td`.

Archived IDs: F02.

Linked statements: [DEC-14](#dec-14), [DEC-21](#dec-21), [INC-01](#inc-01), [INC-02](#inc-02), [INC-03](#inc-03), [INC-04](#inc-04), [INC-05](#inc-05), [INC-06](#inc-06), [INC-08](#inc-08), [INC-09](#inc-09), [INC-10](#inc-10), [INC-11](#inc-11), [INC-12](#inc-12), [INC-13](#inc-13), [INC-14](#inc-14), [INC-15](#inc-15), [INC-16](#inc-16), [INC-17](#inc-17), [INC-19](#inc-19), [INC-20](#inc-20), [INC-21](#inc-21), [INC-22](#inc-22), [INC-23](#inc-23), [INC-24](#inc-24), [INC-25](#inc-25), [INC-26](#inc-26), [INC-29](#inc-29), [INC-30](#inc-30)

<a id="evidence-f03"></a>
### F03

Relationship between AI use and decreased technical debt.

Stable manuscript reference: `fig:ai-decrement-td`.

Archived IDs: F03.

Linked statements: [DEC-01](#dec-01), [DEC-02](#dec-02), [DEC-03](#dec-03), [DEC-04](#dec-04), [DEC-05](#dec-05), [DEC-06](#dec-06), [DEC-08](#dec-08), [DEC-09](#dec-09), [DEC-10](#dec-10), [DEC-11](#dec-11), [DEC-12](#dec-12), [DEC-15](#dec-15), [DEC-16](#dec-16), [DEC-17](#dec-17), [DEC-18](#dec-18), [DEC-19](#dec-19), [DEC-20](#dec-20), [DEC-21](#dec-21), [DEC-22](#dec-22), [DEC-23](#dec-23), [DEC-24](#dec-24), [DEC-25](#dec-25), [DEC-29](#dec-29), [DEC-30](#dec-30), [DEC-31](#dec-31), [DEC-32](#dec-32), [DEC-33](#dec-33), [INC-23](#inc-23)

<a id="evidence-f04"></a>
### F04

Relationship between decreased and increased technical debt.

Stable manuscript reference: `fig:decrement-increment-td`.

Archived IDs: F04.

Linked statements: [DEC-21](#dec-21), [INC-23](#inc-23)

<a id="evidence-f05"></a>
### F05

Relationship between decreased technical debt and clear budget responsibility.

Stable manuscript reference: `fig:decrement-td-clear-budget`.

Archived IDs: F05.

Linked statements: None assigned.

<a id="evidence-f06"></a>
### F06

Relationship between decreased technical debt and code reviews helping to identify technical debt.

Stable manuscript reference: `fig:decrement-td-code-reviews`.

Archived IDs: F06.

Linked statements: [DEC-02](#dec-02), [DEC-03](#dec-03), [DEC-09](#dec-09), [DEC-14](#dec-14), [DEC-15](#dec-15), [DEC-25](#dec-25), [DEC-27](#dec-27), [INC-03](#inc-03), [INC-08](#inc-08), [INC-09](#inc-09), [INC-10](#inc-10), [INC-12](#inc-12), [INC-14](#inc-14), [INC-16](#inc-16), [INC-21](#inc-21), [INC-24](#inc-24), [INC-29](#inc-29)

<a id="evidence-f07"></a>
### F07

Relationship between decreased technical debt and the extent to which code debt is removed.

Stable manuscript reference: `fig:decrement-td-removal-extent`.

Archived IDs: F07.

Linked statements: [DEC-04](#dec-04), [DEC-06](#dec-06), [DEC-11](#dec-11), [DEC-17](#dec-17), [DEC-18](#dec-18), [DEC-22](#dec-22), [DEC-25](#dec-25), [DEC-29](#dec-29), [DEC-30](#dec-30), [DEC-31](#dec-31), [DEC-32](#dec-32), [DEC-33](#dec-33)

<a id="evidence-f08"></a>
### F08

Relationship between decreased technical debt and the use of static code analyzers to identify technical debt.

Stable manuscript reference: `fig:decrement-td-static-analyzers`.

Archived IDs: F08.

Linked statements: [DEC-01](#dec-01), [DEC-02](#dec-02), [DEC-07](#dec-07), [DEC-27](#dec-27)

<a id="evidence-f09"></a>
### F09

Relationship between decreased technical debt and the negative impact of architectural technical debt.

Stable manuscript reference: `fig:decrement-td-architectural-impact`.

Archived IDs: F09.

Linked statements: [DEC-15](#dec-15), [DEC-19](#dec-19), [INC-03](#inc-03), [INC-12](#inc-12), [INC-19](#inc-19)

<a id="evidence-f10"></a>
### F10

Relationship between increased technical debt and managerial encouragement to take on technical debt.

Stable manuscript reference: `fig:increment-td-manager-encouragement`.

Archived IDs: F10.

Linked statements: [INC-03](#inc-03)

<a id="evidence-f11"></a>
### F11

Relationship between increased technical debt and lower priority given to maintenance costs.

Stable manuscript reference: `fig:increment-td-maintenance-cost-priority`.

Archived IDs: F11.

Linked statements: [INC-03](#inc-03), [INC-04](#inc-04), [INC-11](#inc-11), [INC-12](#inc-12), [INC-19](#inc-19)

## Statement traceability

Each entry records an anonymous statement ID, question context, and retained connections.

<a id="dec-01"></a>
### DEC-01

Question context: decrease.

Content codes: type of debt; process; benefit; example.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)
- [TO6 — Confidence in code analyzers](#item-to6)
- [C-AI1-TO6](#evidence-c-ai1-to6)
- [F03](#evidence-f03)
- [F08](#evidence-f08)

<a id="dec-02"></a>
### DEC-02

Question context: decrease.

Content codes: process.

Connections:

- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F03](#evidence-f03)
- [F06](#evidence-f06)
- [F08](#evidence-f08)

<a id="dec-03"></a>
### DEC-03

Question context: decrease.

Content codes: tool; process.

Connections:

- [PC7 — Helpfulness of code reviews](#item-pc7)
- [TO2 — Tools chosen by teams](#item-to2)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F03](#evidence-f03)
- [F06](#evidence-f06)

<a id="dec-04"></a>
### DEC-04

Question context: decrease.

Content codes: process; benefit; example; scope; decision.

Connections:

- [AW1 — Percentage of time wasted because of TD](#item-aw1)
- [PC3 — Dedicated time to manage TD — formal allocation](#item-pc3-a)
- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [C-AI1-PC3.a](#evidence-c-ai1-pc3-a)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-05"></a>
### DEC-05

Question context: decrease.

Content codes: process; benefit; limitation; specification; scope.

Connections:

- [KN2 — Existing guidelines to manage TD](#item-kn2)
- [F03](#evidence-f03)

<a id="dec-06"></a>
### DEC-06

Question context: decrease.

Content codes: process; benefit; example; specification.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-07"></a>
### DEC-07

Question context: decrease.

Content codes: process; scope.

Connections:

- [TO6 — Confidence in code analyzers](#item-to6)
- [C-AI1-TO6](#evidence-c-ai1-to6)
- [F08](#evidence-f08)

<a id="dec-08"></a>
### DEC-08

Question context: decrease.

Content codes: tool; process; benefit; scope.

Connections:

- [F03](#evidence-f03)

<a id="dec-09"></a>
### DEC-09

Question context: decrease.

Content codes: type of debt; tool; process; benefit.

Connections:

- [PC7 — Helpfulness of code reviews](#item-pc7)
- [TO6 — Confidence in code analyzers](#item-to6)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F03](#evidence-f03)
- [F06](#evidence-f06)

<a id="dec-10"></a>
### DEC-10

Question context: decrease.

Content codes: benefit.

Connections:

- [F03](#evidence-f03)

<a id="dec-11"></a>
### DEC-11

Question context: decrease.

Content codes: process; benefit; scope.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-12"></a>
### DEC-12

Question context: decrease.

Content codes: type of debt; benefit; limitation.

Connections:

- [F03](#evidence-f03)

<a id="dec-13"></a>
### DEC-13

Question context: decrease.

Content codes: tool.

Connections:

- [TO2 — Tools chosen by teams](#item-to2)

<a id="dec-14"></a>
### DEC-14

Question context: decrease.

Content codes: process; decision.

Connections:

- [OR2 — Follow-up on TD decisions](#item-or2)
- [PC2 — Systematic and iterative process](#item-pc2)
- [PC5 — Removal of TD](#item-pc5)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [C-AI1-PC2](#evidence-c-ai1-pc2)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="dec-15"></a>
### DEC-15

Question context: decrease.

Content codes: type of debt; process; benefit; limitation; scope.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)
- [PC5 — Removal of TD](#item-pc5)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F03](#evidence-f03)
- [F06](#evidence-f06)
- [F09](#evidence-f09)

<a id="dec-16"></a>
### DEC-16

Question context: decrease.

Content codes: process; benefit; scope.

Connections:

- [F03](#evidence-f03)

<a id="dec-17"></a>
### DEC-17

Question context: decrease.

Content codes: type of debt; process; benefit; limitation; specification; scope.

Connections:

- [KN2 — Existing guidelines to manage TD](#item-kn2)
- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-18"></a>
### DEC-18

Question context: decrease.

Content codes: tool; process; benefit; scope; decision.

Connections:

- [AW1 — Percentage of time wasted because of TD](#item-aw1)
- [OR3 — Clarity of technical responsibility](#item-or3)
- [PC3 — Dedicated time to manage TD — formal allocation](#item-pc3-a)
- [PC5 — Removal of TD](#item-pc5)
- [TO2 — Tools chosen by teams](#item-to2)
- [TO8 — Tools supporting TD level assessment and planning](#item-to8)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [C-AI1-PC3.a](#evidence-c-ai1-pc3-a)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-19"></a>
### DEC-19

Question context: decrease.

Content codes: tool; process; benefit; limitation; example; specification; scope.

Connections:

- [F03](#evidence-f03)
- [F09](#evidence-f09)

<a id="dec-20"></a>
### DEC-20

Question context: decrease.

Content codes: process; benefit; limitation; specification; decision.

Connections:

- [TO8 — Tools supporting TD level assessment and planning](#item-to8)
- [F03](#evidence-f03)

<a id="dec-21"></a>
### DEC-21

Question context: decrease.

Content codes: benefit; limitation; scope.

Connections:

- [BA1 — Experience](#item-ba1)
- [ED1 — Facilitation of education sessions](#item-ed1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)
- [F03](#evidence-f03)
- [F04](#evidence-f04)

<a id="dec-22"></a>
### DEC-22

Question context: decrease.

Content codes: process; benefit; example; scope.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-23"></a>
### DEC-23

Question context: decrease.

Content codes: process; limitation; scope.

Connections:

- [BA1 — Experience](#item-ba1)
- [ED1 — Facilitation of education sessions](#item-ed1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [F03](#evidence-f03)

<a id="dec-24"></a>
### DEC-24

Question context: decrease.

Content codes: tool; process; limitation.

Connections:

- [F03](#evidence-f03)

<a id="dec-25"></a>
### DEC-25

Question context: decrease.

Content codes: type of debt; tool; process; benefit; limitation; scope.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F06](#evidence-f06)
- [F07](#evidence-f07)

<a id="dec-26"></a>
### DEC-26

Question context: decrease.

Content codes: process; limitation; decision.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)

<a id="dec-27"></a>
### DEC-27

Question context: decrease.

Content codes: tool; process; example; specification.

Connections:

- [KN2 — Existing guidelines to manage TD](#item-kn2)
- [OR2 — Follow-up on TD decisions](#item-or2)
- [PC2 — Systematic and iterative process](#item-pc2)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [TO2 — Tools chosen by teams](#item-to2)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [C-AI1-PC2](#evidence-c-ai1-pc2)
- [F06](#evidence-f06)
- [F08](#evidence-f08)

<a id="dec-28"></a>
### DEC-28

Question context: decrease.

Content codes: No assignment.

Connections:

No questionnaire or result connection is retained in the selected paper scope.

<a id="dec-29"></a>
### DEC-29

Question context: decrease.

Content codes: tool; process; benefit; limitation; scope.

Connections:

- [AW1 — Percentage of time wasted because of TD](#item-aw1)
- [PC3 — Dedicated time to manage TD — formal allocation](#item-pc3-a)
- [PC5 — Removal of TD](#item-pc5)
- [TO2 — Tools chosen by teams](#item-to2)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [C-AI1-PC3.a](#evidence-c-ai1-pc3-a)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-30"></a>
### DEC-30

Question context: decrease.

Content codes: type of debt; process; benefit; example.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [TO6 — Confidence in code analyzers](#item-to6)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-31"></a>
### DEC-31

Question context: decrease.

Content codes: type of debt; process; benefit; specification.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-32"></a>
### DEC-32

Question context: decrease.

Content codes: type of debt; process; benefit; limitation.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-33"></a>
### DEC-33

Question context: decrease.

Content codes: process; benefit; scope.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="inc-01"></a>
### INC-01

Question context: increase.

Content codes: benefit; scope.

Connections:

- [F02](#evidence-f02)

<a id="inc-02"></a>
### INC-02

Question context: increase.

Content codes: process; benefit; limitation.

Connections:

- [F02](#evidence-f02)

<a id="inc-03"></a>
### INC-03

Question context: increase.

Content codes: type of debt; process; limitation; example; specification; scope; decision.

Connections:

- [KN2 — Existing guidelines to manage TD](#item-kn2)
- [AW1 — Percentage of time wasted because of TD](#item-aw1)
- [OR3 — Clarity of technical responsibility](#item-or3)
- [PC3 — Dedicated time to manage TD — formal allocation](#item-pc3-a)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)
- [F09](#evidence-f09)
- [F10](#evidence-f10)
- [F11](#evidence-f11)

<a id="inc-04"></a>
### INC-04

Question context: increase.

Content codes: benefit; limitation.

Connections:

- [F02](#evidence-f02)
- [F11](#evidence-f11)

<a id="inc-05"></a>
### INC-05

Question context: increase.

Content codes: type of debt; process; limitation; example.

Connections:

- [F02](#evidence-f02)

<a id="inc-06"></a>
### INC-06

Question context: increase.

Content codes: process; limitation.

Connections:

- [F02](#evidence-f02)

<a id="inc-07"></a>
### INC-07

Question context: increase.

Content codes: process.

Connections:

No questionnaire or result connection is retained in the selected paper scope.

<a id="inc-08"></a>
### INC-08

Question context: increase.

Content codes: type of debt; process; limitation; example; decision.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)
- [PC5 — Removal of TD](#item-pc5)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-09"></a>
### INC-09

Question context: increase.

Content codes: process; limitation; decision.

Connections:

- [PC7 — Helpfulness of code reviews](#item-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-10"></a>
### INC-10

Question context: increase.

Content codes: type of debt; tool; process; limitation; specification; scope.

Connections:

- [BA1 — Experience](#item-ba1)
- [KN2 — Existing guidelines to manage TD](#item-kn2)
- [ED1 — Facilitation of education sessions](#item-ed1)
- [PC3 — Dedicated time to manage TD — formal allocation](#item-pc3-a)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [TO2 — Tools chosen by teams](#item-to2)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-11"></a>
### INC-11

Question context: increase.

Content codes: process; limitation; decision.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)
- [F11](#evidence-f11)

<a id="inc-12"></a>
### INC-12

Question context: increase.

Content codes: type of debt; tool; process; limitation; example; specification; decision.

Connections:

- [AW1 — Percentage of time wasted because of TD](#item-aw1)
- [PC2 — Systematic and iterative process](#item-pc2)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)
- [F09](#evidence-f09)
- [F11](#evidence-f11)

<a id="inc-13"></a>
### INC-13

Question context: increase.

Content codes: type of debt; process; limitation; specification.

Connections:

- [F02](#evidence-f02)

<a id="inc-14"></a>
### INC-14

Question context: increase.

Content codes: process; limitation; scope; decision.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-15"></a>
### INC-15

Question context: increase.

Content codes: scope.

Connections:

- [F02](#evidence-f02)

<a id="inc-16"></a>
### INC-16

Question context: increase.

Content codes: process; limitation; scope; decision.

Connections:

- [BA1 — Experience](#item-ba1)
- [ED1 — Facilitation of education sessions](#item-ed1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-17"></a>
### INC-17

Question context: increase.

Content codes: tool; limitation; specification; scope; decision.

Connections:

- [KN2 — Existing guidelines to manage TD](#item-kn2)
- [PC1 — Understanding of TD risks](#item-pc1)
- [TO8 — Tools supporting TD level assessment and planning](#item-to8)
- [F02](#evidence-f02)

<a id="inc-18"></a>
### INC-18

Question context: increase.

Content codes: No assignment.

Connections:

No questionnaire or result connection is retained in the selected paper scope.

<a id="inc-19"></a>
### INC-19

Question context: increase.

Content codes: type of debt; process; benefit; limitation; example; specification; scope.

Connections:

- [F02](#evidence-f02)
- [F09](#evidence-f09)
- [F11](#evidence-f11)

<a id="inc-20"></a>
### INC-20

Question context: increase.

Content codes: type of debt; process; limitation; example; decision.

Connections:

- [F02](#evidence-f02)

<a id="inc-21"></a>
### INC-21

Question context: increase.

Content codes: process; benefit; scope; decision.

Connections:

- [OR2 — Follow-up on TD decisions](#item-or2)
- [PC2 — Systematic and iterative process](#item-pc2)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-22"></a>
### INC-22

Question context: increase.

Content codes: type of debt; process; limitation; decision.

Connections:

- [F02](#evidence-f02)

<a id="inc-23"></a>
### INC-23

Question context: increase.

Content codes: process; benefit; limitation; example; specification; scope.

Connections:

- [BA1 — Experience](#item-ba1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)
- [F03](#evidence-f03)
- [F04](#evidence-f04)

<a id="inc-24"></a>
### INC-24

Question context: increase.

Content codes: process; benefit; scope; decision.

Connections:

- [OR2 — Follow-up on TD decisions](#item-or2)
- [PC2 — Systematic and iterative process](#item-pc2)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-25"></a>
### INC-25

Question context: increase.

Content codes: process; limitation; scope.

Connections:

- [BA1 — Experience](#item-ba1)
- [ED1 — Facilitation of education sessions](#item-ed1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)

<a id="inc-26"></a>
### INC-26

Question context: increase.

Content codes: benefit; scope.

Connections:

- [F02](#evidence-f02)

<a id="inc-27"></a>
### INC-27

Question context: increase.

Content codes: No assignment.

Connections:

No questionnaire or result connection is retained in the selected paper scope.

<a id="inc-28"></a>
### INC-28

Question context: increase.

Content codes: tool; scope.

Connections:

- [TO2 — Tools chosen by teams](#item-to2)

<a id="inc-29"></a>
### INC-29

Question context: increase.

Content codes: process; limitation; decision.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-30"></a>
### INC-30

Question context: increase.

Content codes: type of debt; limitation; specification.

Connections:

- [F02](#evidence-f02)

