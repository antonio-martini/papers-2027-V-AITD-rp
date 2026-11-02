# Anonymous coding traceability

Statements appear once; the reverse indexes link back to them.
Recorded content assignments and mapping targets are preserved. Rationales and evidential limits provide interpretive context.

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

Each entry is an anonymous analytical summary, not a participant quotation.

<a id="dec-01"></a>
### DEC-01

Assistance identifies poor coding practices and obsolete code.

Question context: decrease.

Content codes: type of debt; process; benefit; example.

Coding rationale: Finding bad practices and deprecated code is an identification benefit; deprecated code supplies a concrete code-quality example.

Result interpretation: Identifying bad practices and deprecated code is a possible enabling activity for TD reduction.

Evidential limit: The tool, review method, static-analysis use, and actual debt removal are unspecified.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)
- [TO6 — Confidence in code analyzers](#item-to6)
- [C-AI1-TO6](#evidence-c-ai1-to6)
- [F03](#evidence-f03)
- [F08](#evidence-f08)

<a id="dec-02"></a>
### DEC-02

Code review and generation are listed as assisted activities.

Question context: decrease.

Content codes: process.

Coding rationale: Names code review and code generation without identifying a product or stating an outcome.

Result interpretation: Names AI code review and generation as activities.

Evidential limit: Names activities without stating review usefulness or a TD decrease; AI review is not evidence of static analysis.

Connections:

- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F03](#evidence-f03)
- [F06](#evidence-f06)
- [F08](#evidence-f08)

<a id="dec-03"></a>
### DEC-03

Unnamed assistants have been adopted for review and implementation suggestions.

Question context: decrease.

Content codes: tool; process.

Coding rationale: Identifies unnamed assistants used for review and implementation suggestions.

Result interpretation: Reports adoption of AI review and implementation suggestions.

Evidential limit: Reports use, not a measured or explicit reduction, review effectiveness, or a frequency–outcome relationship.

Connections:

- [PC7 — Helpfulness of code reviews](#item-pc7)
- [TO2 — Tools chosen by teams](#item-to2)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F03](#evidence-f03)
- [F06](#evidence-f06)

<a id="dec-04"></a>
### DEC-04

Selected small debt fixes accompany feature work; assistance may reduce their effort.

Question context: decrease.

Content codes: process; benefit; example; scope; decision.

Coding rationale: Describes deliberately tackling simpler TD alongside business tasks, with AI reducing the time investment.

Result interpretation: Intentional smaller-TD work and lower time investment illustrate AI-assisted repayment.

Evidential limit: Does not describe formally allocated capacity, repayment before release, or quantify removed debt.

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

Debt reduction may depend on standards compliance and narrowly bounded changes.

Question context: decrease.

Content codes: process; benefit; limitation; specification; scope.

Coding rationale: TD reduction is conditional on guideline compliance, avoidance of bad practices and small, isolated changes.

Result interpretation: Describes conditional TD reduction when AI follows guidelines and handles small, isolated changes.

Evidential limit: The described benefit depends on conditions; the response does not measure how often or how much debt was reduced.

Connections:

- [KN2 — Existing guidelines to manage TD](#item-kn2)
- [F03](#evidence-f03)

<a id="dec-06"></a>
### DEC-06

Refactoring instructions make method consolidation and component separation easier.

Question context: decrease.

Content codes: process; benefit; example; specification.

Coding rationale: Gives concrete refactoring prompts for method consolidation and component separation and describes asking for them as easy.

Result interpretation: Consolidating methods and separating components illustrate structural refactoring.

Evidential limit: Ease of refactoring does not measure removal extent or establish release timing.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-07"></a>
### DEC-07

The activity described is inspection of bounded code sections.

Question context: decrease.

Content codes: process; scope.

Coding rationale: Identifies analysis of code blocks as the activity and its bounded unit; no tool or benefit is specified.

Result interpretation: Code-block analysis is related to technical inspection.

Evidential limit: Does not identify a static analyzer, confidence in one, or a TD outcome.

Connections:

- [TO6 — Confidence in code analyzers](#item-to6)
- [C-AI1-TO6](#evidence-c-ai1-to6)
- [F08](#evidence-f08)

<a id="dec-08"></a>
### DEC-08

Automated or collaborative assistance helps address specific problems.

Question context: decrease.

Content codes: tool; process; benefit; scope.

Coding rationale: Describes agentic or peer-programmer assistance with solving specific issues.

Result interpretation: AI assistance with specific issues supplies possible task-level context for benefits.

Evidential limit: Solving an issue is not necessarily removing TD; no quantified outcome is stated.

Connections:

- [F03](#evidence-f03)

<a id="dec-09"></a>
### DEC-09

Assisted review is perceived to reduce incorrect code.

Question context: decrease.

Content codes: type of debt; tool; process; benefit.

Coding rationale: Identifies assisted review and a perceived reduction in incorrect code.

Result interpretation: Explicitly connects AI-assisted review with less incorrect code.

Evidential limit: Incorrect-code reduction is not a quantified TD measure; existing debt versus prevention is unspecified.

Connections:

- [PC7 — Helpfulness of code reviews](#item-pc7)
- [TO6 — Confidence in code analyzers](#item-to6)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F03](#evidence-f03)
- [F06](#evidence-f06)

<a id="dec-10"></a>
### DEC-10

Assistance is believed to sometimes suggest better debt-related solutions.

Question context: decrease.

Content codes: benefit.

Coding rationale: Expresses a belief that AI can sometimes suggest better TD-related solutions than a developer.

Result interpretation: Suggests AI may propose better TD-related solutions than a developer.

Evidential limit: An expectation/comparison without an observed reduction or implemented solution.

Connections:

- [F03](#evidence-f03)

<a id="dec-11"></a>
### DEC-11

Assistance may improve clarity and modernization of older code.

Question context: decrease.

Content codes: process; benefit; scope.

Coding rationale: Describes refactoring, modernization and clarity benefits in legacy code; no particular debt type is named.

Result interpretation: Legacy refactoring, modernization, and clarity illustrate repayment activities.

Evidential limit: The comment supplies no removal extent, release timing, or comparable usage scores.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-12"></a>
### DEC-12

Current adoption is inadequate despite perceived potential for code debt.

Question context: decrease.

Content codes: type of debt; benefit; limitation.

Coding rationale: Names code-related TD, anticipates substantial potential and reports that AI is not yet properly utilized.

Result interpretation: Underuse despite perceived potential qualifies claims about current benefits.

Evidential limit: Potential is not achieved debt reduction; no frequency score is linked.

Connections:

- [F03](#evidence-f03)

<a id="dec-13"></a>
### DEC-13

The response identifies unnamed software assistance without an activity or outcome.

Question context: decrease.

Content codes: tool.

Coding rationale: Identifies unnamed assistance without describing an activity or outcome.

Result interpretation: Identifies only unnamed software assistance.

Evidential limit: No activity, usefulness, or TD outcome is described; no defensible result-level match.

Connections:

- [TO2 — Tools chosen by teams](#item-to2)

<a id="dec-14"></a>
### DEC-14

Generated changes undergo human checks before integration.

Question context: decrease.

Content codes: process; decision.

Coding rationale: Describes vetting AI output as a gate before accepting it into the integration branch.

Result interpretation: Vetting before merge gives context for review and controlled integration.

Evidential limit: Does not establish TD-specific review usefulness, a systematic cost/benefit/risk assessment, or absence of new debt.

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

Assisted inspection may address code issues while leaving architectural debt unresolved.

Question context: decrease.

Content codes: type of debt; process; benefit; limitation; scope.

Coding rationale: Contrasts useful AI review for code-level issues with lack of help for architectural TD.

Result interpretation: Explicitly contrasts useful AI review for code issues with an architectural-TD limitation.

Evidential limit: Supports a scope explanation, not the association magnitude or identification of the debt types reduced in the figure.

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

Assistance is described for investigating complicated problems.

Question context: decrease.

Content codes: process; benefit; scope.

Coding rationale: Reports assistance with investigation and identifies complex issues as the task context.

Result interpretation: Investigation of complex issues can enable later maintenance work.

Evidential limit: Investigation alone does not show debt removal, TD-level measurement, or planning-tool use.

Connections:

- [F03](#evidence-f03)

<a id="dec-17"></a>
### DEC-17

Bounded code debt may be repairable when instructions are suitable.

Question context: decrease.

Content codes: type of debt; process; benefit; limitation; specification; scope.

Coding rationale: Fixing code-related TD is described as conditional on limited debt size and suitable prompting.

Result interpretation: Fixing bounded code-level TD with suitable prompting illustrates conditional repayment.

Evidential limit: A stated capability; no removal amount, release timing, or causal prompt effect is measured.

Connections:

- [KN2 — Existing guidelines to manage TD](#item-kn2)
- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-18"></a>
### DEC-18

Automated execution speeds substantial changes while people choose what changes are needed.

Question context: decrease.

Content codes: tool; process; benefit; scope; decision.

Coding rationale: Agents execute large changes quickly while people retain responsibility for deciding what changes are needed.

Result interpretation: Rapid human-directed changes suggest reduced implementation effort.

Evidential limit: Changes need not remove TD; faster execution is not evidence of dedicated capacity or cross-team support responsibility.

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

Instructed assistants may fix smaller issues but struggle with large system migrations.

Question context: decrease.

Content codes: tool; process; benefit; limitation; example; specification; scope.

Coding rationale: Instructed agents may resolve some issues but struggle with larger migration tasks; a generic system migration illustrates the limit.

Result interpretation: Limited success on larger migration tasks qualifies AI benefit claims.

Evidential limit: A migration example is contextual to scope; it is not a direct architectural-TD assessment or a universal limit.

Connections:

- [F03](#evidence-f03)
- [F09](#evidence-f09)

<a id="dec-20"></a>
### DEC-20

Useful alternatives require people to define the task first.

Question context: decrease.

Content codes: process; benefit; limitation; specification; decision.

Coding rationale: AI offers useful alternatives, but someone must supply the task that directs its work.

Result interpretation: Human-selected tasks and alternative solutions give context for useful assistance.

Evidential limit: Suggestions are not proven repayments and do not establish budget or technical-support responsibility.

Connections:

- [TO8 — Tools supporting TD level assessment and planning](#item-to8)
- [F03](#evidence-f03)

<a id="dec-21"></a>
### DEC-21

Perceived debt outcomes depend on expertise; less experienced users may add more debt.

Question context: decrease.

Content codes: benefit; limitation; scope.

Coding rationale: Attributes perceived decreases and increases to differences between senior and junior users; this is a respondent attribution.

Result interpretation: Within one account, perceived increases and decreases depend on developer expertise.

Evidential limit: A respondent attribution about different users, not paired quantitative outcomes or an AI-use gradient.

Connections:

- [BA1 — Experience](#item-ba1)
- [ED1 — Facilitation of education sessions](#item-ed1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)
- [F03](#evidence-f03)
- [F04](#evidence-f04)

<a id="dec-22"></a>
### DEC-22

Assistance eases sizeable refactoring and automated creation of tests.

Question context: decrease.

Content codes: process; benefit; example; scope.

Coding rationale: Describes easier refactoring of largish modules and automatic test addition as concrete maintenance actions.

Result interpretation: Easier module refactoring and automatic tests illustrate assistance with debt-related work.

Evidential limit: No amount of existing debt removed or release timing is established; tests may prevent future debt.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-23"></a>
### DEC-23

Usefulness depends on understanding existing code and its dependencies.

Question context: decrease.

Content codes: process; limitation; scope.

Coding rationale: Benefits are described as depending on the user's reading and understanding of a legacy project.

Result interpretation: Code understanding and user judgment are described as conditions for benefits.

Evidential limit: Does not report a decrease, its magnitude, or a specific organizational capability.

Connections:

- [BA1 — Experience](#item-ba1)
- [ED1 — Facilitation of education sessions](#item-ed1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [F03](#evidence-f03)

<a id="dec-24"></a>
### DEC-24

The account reports limited capability for autonomous debt-related work.

Question context: decrease.

Content codes: tool; process; limitation.

Coding rationale: Identifies autonomous AI task solving and reports a current capability gap.

Result interpretation: Difficulty with autonomous TD tasks qualifies current AI capability.

Evidential limit: Does not show absence of assisted benefits or quantify reductions.

Connections:

- [F03](#evidence-f03)

<a id="dec-25"></a>
### DEC-25

Assisted reviews help newly written code, with less benefit for accumulated debt.

Question context: decrease.

Content codes: type of debt; tool; process; benefit; limitation; scope.

Coding rationale: Assisted reviews are useful for newly written code, while help with accumulated debt is limited.

Result interpretation: Explicit new-code review benefits coexist with little help for old debt.

Evidential limit: Distinguishes prevention from repayment; does not support a general reduction of accumulated debt.

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

Whether developers consider debt consequences when giving instructions is uncertain.

Question context: decrease.

Content codes: process; limitation; decision.

Coding rationale: Expresses uncertainty about whether developers consider TD increases and decreases when deciding how to prompt AI.

Result interpretation: Uncertainty about whether developers consider TD while prompting.

Evidential limit: No directional outcome, organizational use of the TD term, or quantitative relationship is resolved.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)

<a id="dec-27"></a>
### DEC-27

Integration workflows use automated reviewers with distinct instructions and supporting context.

Question context: decrease.

Content codes: tool; process; example; specification.

Coding rationale: Describes an integration workflow with review assistants configured for debt concerns and retrieved context.

Result interpretation: A pull-request workflow with two review agents illustrates review infrastructure.

Evidential limit: Does not state review effectiveness, systematic TD assessment, or use of a static analyzer.

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

The response provides no substantive information.

Question context: decrease.

Content codes: No assignment.

Coding rationale: No substantive content supports a content-code assignment.

Result interpretation: Administrative/non-substantive entry.

Evidential limit: No interpretable content for the targeted results.

Connections:

No questionnaire or result connection is retained in the selected paper scope.

<a id="dec-29"></a>
### DEC-29

Unnamed assistants automate repetitive maintenance, but limited adoption constrains the contribution.

Question context: decrease.

Content codes: tool; process; benefit; limitation; scope.

Coding rationale: Identifies assisted repetitive maintenance with limited current adoption and contribution.

Result interpretation: Repetitive maintenance automation offers a benefit mechanism, qualified by limited current focus.

Evidential limit: Maintenance is not necessarily repayment; limited focus is not a measure of formally allocated time or maintenance-cost priority.

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

Assisted cleanup targets unused artifacts and code organization.

Question context: decrease.

Content codes: type of debt; process; benefit; example.

Coding rationale: Names unused files, features/classes and style refactoring as concrete identification and cleanup activities.

Result interpretation: Finding unused files and refactoring styles illustrate code cleanup.

Evidential limit: Does not quantify debt removal or state when cleanup occurs relative to release.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [TO6 — Confidence in code analyzers](#item-to6)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-31"></a>
### DEC-31

Understanding code context may make debt-related restructuring easier.

Question context: decrease.

Content codes: type of debt; process; benefit; specification.

Coding rationale: Describes easier refactoring of code with TD and identifies current-code context as the basis for useful assistance.

Result interpretation: Explicitly describes easier AI-assisted refactoring of code with TD.

Evidential limit: A perceived ease/capability claim without measured removal or usage intensity.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-32"></a>
### DEC-32

The possible benefit of simplification for debt removal remains uncertain.

Question context: decrease.

Content codes: type of debt; process; benefit; limitation.

Coding rationale: Tentatively links code simplification with TD removal while explicitly expressing uncertainty.

Result interpretation: Tentatively links simplification with debt removal.

Evidential limit: The statement itself is uncertain and provides no concrete implemented example.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="dec-33"></a>
### DEC-33

Easier test creation and broader coverage are described as preventing future debt.

Question context: decrease.

Content codes: process; benefit; scope.

Coding rationale: Describes easier test creation and greater coverage to prevent newly written code from becoming TD; repayment of existing debt is unspecified.

Result interpretation: Easier tests and greater coverage are described as preventing new TD.

Evidential limit: Prevention is not removal of existing TD; neither coverage nor future debt is measured here.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [C-AI1-PC5](#evidence-c-ai1-pc5)
- [C-TD2-PC5](#evidence-c-td2-pc5)
- [F03](#evidence-f03)
- [F07](#evidence-f07)

<a id="inc-01"></a>
### INC-01

The account perceives no additional debt attributable to assistance.

Question context: increase.

Content codes: benefit; scope.

Coding rationale: Reports no perceived AI-related increase in TD; no prevention mechanism or quantitative amount is supplied.

Result interpretation: Reports no perceived AI-related TD increase.

Evidential limit: No usage score, numerical estimate, or explanation is linked to this comment.

Connections:

- [F02](#evidence-f02)

<a id="inc-02"></a>
### INC-02

Convenient generation may also create maintenance liabilities.

Question context: increase.

Content codes: process; benefit; limitation.

Coding rationale: Describes easy code generation alongside the possibility of introducing TD.

Result interpretation: Suggests AI code generation can introduce TD.

Evidential limit: Possibility rather than a clear observed increase or an association with use frequency.

Connections:

- [F02](#evidence-f02)

<a id="inc-03"></a>
### INC-03

Generated structures may violate architectural rules; rejecting accepted output and proposing alternatives burdens reviewers.

Question context: increase.

Content codes: type of debt; process; limitation; example; specification; scope; decision.

Coding rationale: Describes architecture-misaligned scaffolding, defined rules and standards, production acceptance, and the reviewer burden of blocking it and proposing alternatives.

Result interpretation: Architecture-misaligned code and demanding review illustrate risk; acceptance by an owner supplies limited organizational context.

Evidential limit: Owner acceptance does not establish managerial encouragement; review effort does not establish cost priority, budget clarity, or cross-team support responsibility.

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

Speed gains may accompany weaker code quality.

Question context: increase.

Content codes: benefit; limitation.

Coding rationale: Pairs fast solutions with poorer code quality, describing a speed/quality trade-off.

Result interpretation: Fast solutions with poorer code illustrate a possible speed/quality trade-off.

Evidential limit: Does not identify management decisions or the priority assigned to maintenance costs.

Connections:

- [F02](#evidence-f02)
- [F11](#evidence-f11)

<a id="inc-05"></a>
### INC-05

Generated output can introduce unused code and repeated implementations.

Question context: increase.

Content codes: type of debt; process; limitation; example.

Coding rationale: Names dead code and unnecessary duplication as concrete problems created by generation.

Result interpretation: Dead code and duplication illustrate forms of additional maintenance burden.

Evidential limit: No amount of introduced debt or use-frequency relationship is supplied.

Connections:

- [F02](#evidence-f02)

<a id="inc-06"></a>
### INC-06

Careless assistance may lead to adopting poor implementation patterns.

Question context: increase.

Content codes: process; limitation.

Coding rationale: Describes careless use as a condition for adopting poor patterns; no specific pattern is named.

Result interpretation: Careless use is described as a condition for bad-pattern adoption.

Evidential limit: The described outcome depends on usage; the response does not measure debt increases or specify a review process.

Connections:

- [F02](#evidence-f02)

<a id="inc-07"></a>
### INC-07

Existing implementation patterns are reused without a stated outcome.

Question context: increase.

Content codes: process.

Coding rationale: Describes reuse of existing patterns. The statement does not establish whether that reuse is beneficial or harmful.

Result interpretation: Says existing patterns are reused.

Evidential limit: The direction is ambiguous: reuse may help or perpetuate poor patterns; no defensible support direction.

Connections:

No questionnaire or result connection is retained in the selected paper scope.

<a id="inc-08"></a>
### INC-08

Weak understanding and superficial review allow irrelevant tests and unnecessary safeguards; later maintainers hesitate to remove them.

Question context: increase.

Content codes: type of debt; process; limitation; example; decision.

Coding rationale: Describes poorly understood generated code, insufficiently critical review, questionable tests and impossible-case guards, and uncertainty about whether later maintainers can remove them.

Result interpretation: Poorly understood code and insufficiently critical review illustrate how problematic output can be accepted.

Evidential limit: A review-failure account qualifies effectiveness; it does not test the helpful-review/decrease correlation.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)
- [PC5 — Removal of TD](#item-pc5)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-09"></a>
### INC-09

Suggestions are accepted without independent validation.

Question context: increase.

Content codes: process; limitation; decision.

Coding rationale: Describes accepting AI suggestions without verification or critical judgment.

Result interpretation: Uncritical acceptance illustrates a risk and the relevance of validation.

Evidential limit: No formal code-review practice or its measured usefulness is specified.

Connections:

- [PC7 — Helpfulness of code reviews](#item-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-10"></a>
### INC-10

Inexperienced users produce noncompliant code; expert capacity for review and teaching is insufficient.

Question context: increase.

Content codes: type of debt; tool; process; limitation; specification; scope.

Coding rationale: Identifies unnamed assistance, noncompliant code, and insufficient expert capacity to review and teach less experienced users.

Result interpretation: Limited senior review capacity and standards mismatch qualify review as a safeguard.

Evidential limit: Review capacity is not a measure of management encouragement, budgets, or cross-team responsibility.

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

Users may overlook or knowingly accept suggestions that increase debt.

Question context: increase.

Content codes: process; limitation; decision.

Coding rationale: Describes following TD-increasing suggestions despite recognizing their problems, or failing to recognize them.

Result interpretation: Recognized poor suggestions may still be accepted, illustrating a possible quality trade-off.

Evidential limit: Individual shortcuts do not establish organizational maintenance-cost priority or managerial encouragement.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)
- [F11](#evidence-f11)

<a id="inc-12"></a>
### INC-12

Iterative automated fixes may add unnecessary conditions and documentation mismatches that escape review.

Question context: increase.

Content codes: type of debt; tool; process; limitation; example; specification; decision.

Coding rationale: Names an LLM and describes bloated conditions, architecture/documentation mismatch, mistaken review acceptance and iterative fixes for introduced bugs.

Result interpretation: Code bloat, architecture/documentation mismatch, and failures in review illustrate maintenance risk.

Evidential limit: Iterative bug fixing is not systematic TD assessment; the comment does not measure maintenance-cost priority or paired reductions.

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

Generated implementations can conflict with existing codebase conventions.

Question context: increase.

Content codes: type of debt; process; limitation; specification.

Coding rationale: Describes generated code that fits the codebase poorly, making codebase compatibility the unmet criterion.

Result interpretation: Poor codebase fit illustrates a reported source of TD risk.

Evidential limit: Codebase mismatch is not a quantified architectural-TD result or an AI-use gradient.

Connections:

- [F02](#evidence-f02)

<a id="inc-14"></a>
### INC-14

Broad, complex tasks limit adoption; assisted portions are checked and improved before integration.

Question context: increase.

Content codes: process; limitation; scope; decision.

Coding rationale: Links limited AI use to complex, broadly scoped work and describes people checking and improving output before integration.

Result interpretation: Limited AI use combined with checking before merge provides a qualifying account.

Evidential limit: Does not isolate the effects of low use and checking or explicitly measure prevention.

Connections:

- [PC5 — Removal of TD](#item-pc5)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-15"></a>
### INC-15

Only a small debt increase is perceived.

Question context: increase.

Content codes: scope.

Coding rationale: A brief extent response indicates a small perceived increase; no mechanism or percentage is inferred.

Result interpretation: A brief answer suggests a limited perceived increase.

Evidential limit: Magnitude and mechanism remain unspecified; it should not be converted to zero or a percentage.

Connections:

- [F02](#evidence-f02)

<a id="inc-16"></a>
### INC-16

Unfamiliar implementation languages undermine objective review and encourage uncritical acceptance.

Question context: increase.

Content codes: process; limitation; scope; decision.

Coding rationale: Describes assistant-driven coding in unfamiliar languages and accepting output without the knowledge needed for objective review.

Result interpretation: Unfamiliar languages and weak ability to review outputs illustrate validation limitations.

Evidential limit: Does not establish formal review usefulness, organizational responsibility, or a numerical increase.

Connections:

- [BA1 — Experience](#item-ba1)
- [ED1 — Facilitation of education sessions](#item-ed1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-17"></a>
### INC-17

Limited context can yield incomplete, verbose output and questionable task choices despite instructions.

Question context: increase.

Content codes: tool; limitation; specification; scope; decision.

Coding rationale: Describes assistant context-window limits, missing relevant information despite strict instructions, partial output and work on tasks judged to have dubious value.

Result interpretation: Context-window limits and verbose partial solutions illustrate technical limitations.

Evidential limit: No debt-level measurement, planning-tool use, or measured use-frequency association is supplied.

Connections:

- [KN2 — Existing guidelines to manage TD](#item-kn2)
- [PC1 — Understanding of TD risks](#item-pc1)
- [TO8 — Tools supporting TD level assessment and planning](#item-to8)
- [F02](#evidence-f02)

<a id="inc-18"></a>
### INC-18

An unexplained numerical response provides no interpretable information.

Question context: increase.

Content codes: No assignment.

Coding rationale: An unexplained numerical entry supplies no interpretable basis for a content code.

Result interpretation: Isolated numeric free-text entry.

Evidential limit: No interpretable mechanism; do not treat it as a verified survey percentage or a quote supporting a relationship.

Connections:

No questionnaire or result connection is retained in the selected paper scope.

<a id="inc-19"></a>
### INC-19

Immediate fixes may work locally while diverging from architecture and duplicating existing solutions.

Question context: increase.

Content codes: type of debt; process; benefit; limitation; example; specification; scope.

Coding rationale: Contrasts working immediate fixes with architecture mismatch and duplicated solutions, distinguishing local task success from wider maintenance consequences.

Result interpretation: Architecture-misaligned quick fixes and duplication illustrate long-term maintenance concerns.

Evidential limit: Working immediate solutions are not measured TD decreases; the comment does not establish cost-priority ranking.

Connections:

- [F02](#evidence-f02)
- [F09](#evidence-f09)
- [F11](#evidence-f11)

<a id="inc-20"></a>
### INC-20

New redundant implementations replace opportunities to reuse available functions.

Question context: increase.

Content codes: type of debt; process; limitation; example; decision.

Coding rationale: Describes redundant new implementations being generated instead of choosing existing or library functions.

Result interpretation: Redundant implementation instead of reuse illustrates maintenance risk.

Evidential limit: No quantified increase, managerial decision, or code-review effect is stated.

Connections:

- [F02](#evidence-f02)

<a id="inc-21"></a>
### INC-21

Review is described as attempting to prevent additional debt.

Question context: increase.

Content codes: process; benefit; scope; decision.

Coding rationale: Tentatively reports preventing AI-related TD increases by stopping problematic output at code review.

Result interpretation: Code review is explicitly described as stopping an AI-related increase.

Evidential limit: A prevention account, not evidence of removal of existing debt or proof that helpful reviews caused the reported decreases.

Connections:

- [OR2 — Follow-up on TD decisions](#item-or2)
- [PC2 — Systematic and iterative process](#item-pc2)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [C-TD2-PC7](#evidence-c-td2-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-22"></a>
### INC-22

Convenient reimplementation may displace reuse of existing functionality.

Question context: increase.

Content codes: type of debt; process; limitation; decision.

Coding rationale: Describes easy reimplementation of existing functionality instead of selecting library reuse, creating a duplication risk.

Result interpretation: Reimplementation instead of library reuse illustrates a potential new-debt mechanism.

Evidential limit: Does not measure extent, use intensity, or priority preferences.

Connections:

- [F02](#evidence-f02)

<a id="inc-23"></a>
### INC-23

Results depend on instructions and expertise; unfamiliar dependencies make older-code integration problematic.

Question context: increase.

Content codes: process; benefit; limitation; example; specification; scope.

Coding rationale: Describes occasional useful solutions but also prompting- and expertise-dependent integration problems involving relationships between functions in legacy projects.

Result interpretation: One account combines useful solutions with legacy-integration problems, illustrating mixed experiences.

Evidential limit: Useful solutions are not explicit TD decreases; no linked increase/decrease estimates or net balance are available.

Connections:

- [BA1 — Experience](#item-ba1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)
- [F03](#evidence-f03)
- [F04](#evidence-f04)

<a id="inc-24"></a>
### INC-24

Comprehensive output checking accompanies a perception of no additional debt.

Question context: increase.

Content codes: process; benefit; scope; decision.

Coding rationale: Describes responsible use and checking all output alongside a reported absence of AI-related TD increase.

Result interpretation: Checking output accompanies a reported absence of increased TD.

Evidential limit: General checking is not necessarily formal code review; the causal effect of checking is not established.

Connections:

- [OR2 — Follow-up on TD decisions](#item-or2)
- [PC2 — Systematic and iterative process](#item-pc2)
- [PC7 — Helpfulness of code reviews](#item-pc7)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-25"></a>
### INC-25

Incomplete understanding of existing code and generated output complicates integration.

Question context: increase.

Content codes: process; limitation; scope.

Coding rationale: Describes integration of AI output with legacy code as challenging when developers lack product-code and output understanding.

Result interpretation: Limited code understanding and difficult legacy integration illustrate maintenance risk.

Evidential limit: Does not identify a particular architectural-TD level, cross-team support role, or budget decision.

Connections:

- [BA1 — Experience](#item-ba1)
- [ED1 — Facilitation of education sessions](#item-ed1)
- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)

<a id="inc-26"></a>
### INC-26

No debt increase is attributed to assistance in this account.

Question context: increase.

Content codes: benefit; scope.

Coding rationale: Explicitly reports no perceived AI-related TD increase, without naming a mechanism or measured amount.

Result interpretation: The account describes no added maintenance debt associated with assistance.

Evidential limit: No usage category, scale value, or mechanism is supplied.

Connections:

- [F02](#evidence-f02)

<a id="inc-27"></a>
### INC-27

No interpretable response content is available.

Question context: increase.

Content codes: No assignment.

Coding rationale: No substantive content supports a content-code assignment.

Result interpretation: Administrative/non-substantive entry.

Evidential limit: No interpretable evidence for a correlation or figure.

Connections:

No questionnaire or result connection is retained in the selected paper scope.

<a id="inc-28"></a>
### INC-28

Assistance is used sparingly inside an unnamed development environment.

Question context: increase.

Content codes: tool; scope.

Coding rationale: Describes limited assisted work within an unnamed development environment; the activity is unspecified.

Result interpretation: Mentions limited use inside an editor.

Evidential limit: No debt outcome or sufficiently clear relationship is stated.

Connections:

- [TO2 — Tools chosen by teams](#item-to2)

<a id="inc-29"></a>
### INC-29

Usage-dependent weaknesses in suggested solutions can be difficult to recognize.

Question context: increase.

Content codes: process; limitation; decision.

Coding rationale: Describes difficulty recognizing suboptimal AI solutions, making output assessment and judgment problematic.

Result interpretation: Use-dependent, hard-to-detect suboptimal solutions illustrate a validation challenge.

Evidential limit: Does not establish formal review scores, measured debt, or a frequency–outcome relationship.

Connections:

- [PC1 — Understanding of TD risks](#item-pc1)
- [F02](#evidence-f02)
- [F06](#evidence-f06)

<a id="inc-30"></a>
### INC-30

Generated code may fall short of cleanliness and stated requirements.

Question context: increase.

Content codes: type of debt; limitation; specification.

Coding rationale: Describes code cleanliness and compliance with requirements as unmet quality criteria.

Result interpretation: Code quality and requirements mismatch illustrate a reported risk.

Evidential limit: No quantified increase, specific governance practice, or review outcome is supplied.

Connections:

- [F02](#evidence-f02)

