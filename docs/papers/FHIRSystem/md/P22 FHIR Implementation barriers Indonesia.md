INDONESIAN HEALTH JOURNAL
https://ihj.rivierapublishing.id/index.php/rp P-ISSN: 2963-3044
Volume 5 Number 1 , January 2026 E-ISSN: 2963-3036
Implementation Barriers of Electronic Health Record Interoperability in
Indonesian District Hospitals: A Mixed-Methods Study
Septien Dwi Savandha1*, Elvira Fitriyanti2, Adelia Azzahra3
1, 3Universitas Swadaya Gunung Jati, Indonesia
2Politeknik Siber Cerdika Internasional, Indonesia
Email: 1dwisavandha9@gmail.com*, 2elvirafitriyanti@gmail.com,
3adeliaazzahra349@gmail.com
, adeliaazzahra349@gmail.com
ABSTRACT
The implementation of interoperable Electronic Health Records (EHRs) is essential for strengthening integrated,
patient-centered healthcare delivery in Indonesia; however, district hospitals continue to face substantial barriers
in aligning local hospital information systems with the national SATUSEHAT platform. This study aimed to
identify and analyze the technical, organizational, regulatory, and human resource barriers affecting EHR
interoperability readiness in Indonesian district hospitals. A convergent parallel mixed-methods design was
employed across 12 type C and D district hospitals in West Java, Central Kalimantan, and East Nusa Tenggara.
Data collection was conducted during the e januari-maret period in 2025. Quantitative data were collected from
240 respondents using a structured questionnaire based on the Technology-Organization-Environment framework
and the Unified Theory of Acceptance and Use of Technology, while qualitative data were obtained through
interviews and focus group discussions with 36 key informants. The findings showed that vendor and system
interoperability, technical infrastructure readiness, and human resource competency were the most critical
barriers. Logistic regression indicated that low infrastructure readiness, weak vendor interoperability, limited
digital literacy, lower hospital digital maturity, and geographic location significantly predicted low
interoperability readiness. Qualitative findings further revealed vendor lock-in, unstable connectivity, limited
training, budget constraints, and regulatory implementation gaps. In conclusion, EHR interoperability in
Indonesian district hospitals requires not only technical standardization, but also sustained organizational support,
workforce capacity-building, stronger vendor governance, and differentiated policy assistance for hospitals with
lower digital maturity. This study is novel in that it applies a convergent parallel mixed-methods design integrating
the TOE and UTAUT frameworks specifically at the district-hospital level (RSUD type C and D) across provinces
with contrasting digital maturity, an analytical scope that has not been jointly examined in prior Indonesian EHR
interoperability research.
Keywords: digital health; district hospitals; electronic health records; interoperability; SATU SEHAT
INTRODUCTION
The global transition toward digital health systems has positioned Electronic Health
Records (EHR) as a foundational pillar of modern healthcare delivery. Interoperability the
capacity of different information systems to exchange, interpret, and act upon shared health
data seamlessly stands at the core of this transformation. The World Health Organization
(WHO) has explicitly underscored interoperability as a strategic priority in its Global Strategy
on Digital Health 2020–2027, calling on member states to accelerate the development of
integrated, patient-centered digital health infrastructures Organization (2025) In parallel,
global health data exchange standards such as HL7 Fast Healthcare Interoperability Resources
(FHIR) have emerged as the technical backbone for achieving seamless communication across
heterogeneous health information systems (Faisal & Nakayama, 2024) Despite these global
commitments, the realization of EHR interoperability remains uneven, particularly in low- and
middle-income countries (LMICs) where structural, organizational, and human resource
154

Implementation Barriers of Electronic Health Record Interoperability in Indonesian District Hospitals: A
Mixed-Methods Study
constraints compound the technical challenges of implementation.while cross-national
experience further shows that digital health adoption is shaped as much by organizational and
behavioral factors as by the technology itself (Kyratsis et al., 2022)
Indonesia, as the fourth most populous nation and one of Southeast Asia's largest
archipelagic states, represents a critical case study in the complexities of EHR interoperability
within a resource-constrained, geographically fragmented health system. In 2022, the
Indonesian Ministry of Health issued Regulation Number 24 of 2022 on Medical Records,
mandating all healthcare facilities to adopt Electronic Medical Records (EMR) and integrate
them with the national SATUSEHAT platform no later than December 31, 2023 (Kementerian
Kesehatan Republik Indonesia, 2022). The SATUSEHAT platform, built upon HL7 FHIR
standards, was designed to unify health data across more than 60,000 healthcare facilities
nationwide, enabling the exchange of individual patient records across integrated providers
(Ministry of Health of the Republic of Indonesia, 2022(Faisal & Nakayama, 2024) However,
implementation fidelity data reveals a concerning gap between policy ambition and ground-
level execution.
A national assessment of 33,901 facilities conducted in late 2024 found that only 58%
met the minimum 50% data submission threshold in October, and compliance rates declined
further by December when the target was raised to 100% (Kusumawardani et al., 2025). These
figures underscore a structural implementation deficit that warrants systematic investigation.
Consistent with this implementation deficit, a content analysis of developer discussions on the
SATUSEHAT platform identified recurring technical obstacles, including server instability,
terminology mapping, and FHIR profile selection, that continue to hinder facility-level
integration with the national platform Heryawan et al. (2025)
The challenge is particularly acute in district-level hospitals (Rumah Sakit Umum
Daerah, RSUD), which serve as the backbone of Indonesia's referral healthcare system for rural
and semi-urban populations. A national digital maturity assessment involving 146 provinces
and districts in 2023 revealed an average score of only 2.73 out of 5.00, signifying a
predominantly foundational or emerging level of digital readiness across health service
facilities (Healthcare IT News, 2024). Studies examining EMR adoption patterns across
Indonesian hospitals found significant disparities between facilities in Java where
infrastructure and training support were comparatively stronger and those in outer islands such
as Sulawesi, where adoption was driven largely by regulatory compliance pressure rather than
genuine readiness (Sari et al., 2025).
Comparable patterns have been documented elsewhere in South and Southeast Asia,
where digital health innovations in low- and middle-income health systems remain constrained
by disparities in digital access, fragmented legacy information systems, and the absence of
patient-centered data architectures capable of supporting nationwide interoperability (Yi et al.,
2024) The barriers to EHR interoperability are multidimensional and extend well beyond
technical constraints. Evidence from middle-income countries demonstrates that organizational
factors including inadequate leadership, high staff turnover in key technical roles, insufficient
training frameworks, and limited budget allocation for digital infrastructure are equally, if not
more, consequential for implementation failure (Alzghaibi & Hutchings, 2025) In Indonesia
specifically, the challenge of balancing hospital general strategy with information technology
strategy has been identified as a critical tension, with many lower-class hospitals lacking the
155

financial, human, and infrastructural resources necessary to align with national digital
transformation demands (Yunita et al., 2024). Furthermore, a socio-technical systems analysis
of health information systems in rural Indonesia found that national digital health initiatives
repeatedly underperform due to misalignments between technological deployment and the
local social and organizational contexts in which these systems must operate (Hamzah et al.,
2025).
The electronic health records literature from non-hospital settings in developing
economies similarly emphasizes that human factors including digital literacy, user acceptance,
These socio-environmental, technological, and organizational barriers mirror those identified
in broader reviews of open-source EHR adoption in low- and lower-middle-income countries
(Bostan et al., 2024) and align with Technology-Organization-Environment analyses showing
that the successful adoption of digital health innovations such as telehealth during periods of
system-wide pressure depends on the joint alignment of technological readiness, organizational
capacity, and environmental conditions Policy & (2024)Despite a growing body of literature
on EHR implementation barriers in LMICs, research specifically examining EHR
interoperability challenges in Indonesian district-level hospitals remains sparse. Most existing
studies have focused either on primary health centers (Puskesmas), tertiary referral hospitals in
urban settings, or broad national-level policy analyses, leaving a critical evidence gap regarding
the lived implementation experience of RSUD managers, clinical staff, and health informatics
personnel at the district level. Furthermore, few studies have employed a mixed-methods
design capable of integrating the quantitative breadth of barrier prevalence with the qualitative
depth of stakeholder perspectives necessary to fully characterize the problem.
This study addresses that gap by systematically identifying and categorizing the
technical, organizational, regulatory, and human resource barriers to EHR interoperability in
Indonesian district hospitals, using a convergent parallel mixed-methods approach grounded in
the Technology-Organization-Environment (TOE) Framework and the Unified Theory of
Acceptance and Use of Technology (UTAUT). This study is novel in that it is among the first
to jointly apply the TOE and UTAUT frameworks within a convergent parallel mixed-methods
design at the district-hospital level (RSUD type C and D), thereby integrating the breadth of
quantitative barrier prevalence with the depth of qualitative stakeholder experience across
provinces of differing digital maturity. The findings are intended to inform actionable
recommendations for hospital managers, regional health authorities, and national policymakers
as Indonesia continues its digital health transformation agenda. Specifically, hospital managers
may benefit from evidence-based priorities for internal capacity-building, regional health
authorities may use the findings to target technical assistance to lower-maturity districts, and
national policymakers may draw on the results to design differentiated, rather than uniform,
SATUSEHAT implementation support policies. Grounding this study in the Unified Theory of
Acceptance and Use of Technology is further warranted by recent evidence that behavioral
intention to adopt electronic personal health records is significantly shaped by performance
expectancy, effort expectancy, and privacy-related facilitating conditions, factors that extend
the TOE framework's organizational and environmental dimensions to the level of individual
technology acceptance Kassie et al. (2025).
156

Implementation Barriers of Electronic Health Record Interoperability in Indonesian District Hospitals: A
Mixed-Methods Study
METHOD
This study used a convergent parallel mixed-methods design, where quantitative and
qualitative data were collected at the same time, analyzed separately, and integrated during
interpretation to obtain a comprehensive understanding of EHR interoperability barriers in
Indonesian district hospitals (Creswell, J. W., & Plano Clark, V. L. (2018). Designing... -
Google Scholar, n.d.). The study was conducted in 12 purposively selected district hospitals,
consisting of RSUD type C and D, located in three provinces with different levels of digital
maturity and geographical characteristics: West Java, representing Java with relatively
advanced infrastructure; East Nusa Tenggara, representing eastern Indonesia with limited
connectivity; and Central Kalimantan, representing outer Borneo with moderate infrastructure
capacity. The hospitals were recruited based on three criteria: being classified as RSUD type
C or D under the Ministry of Health classification system, having received written directives
or formal guidance related to SATUSEHAT integration between 2022 and 2024, and having at
least one active health information system or hospital management information system
(SIMRS) during data collection. Within each province, eligible hospitals meeting these three
criteria were identified in coordination with the provincial health office, and the specific
participating hospitals were then selected purposively to maximize variation in digital maturity
level and geographic accessibility (e.g., urban-adjacent versus more remote districts) among
eligible sites Data collection was conducted from January–March 2026. This study was
reviewed and approved by the Health Research Ethics Committee of Swadaya Gunung Jati
University under approval number 001/KEPK-FK/USGJ/I/2026; written informed consent was
obtained from all respondents and informants prior to data collection.
Unified Theory of Acceptance and Use of Technology (UTAUT) Venkatesh et al. (2003)
The questionnaire consisted of 42 items across six domains: technical infrastructure readiness
(9 items), organizational capacity and leadership (8 items), regulatory compliance awareness
(7 items), human resource competency and digital literacy (8 items), vendor and system
interoperability (6 items), and perceived usefulness and behavioral intention to use (4 items).
All items were measured using a five-point Likert scale ranging from 1 (strongly disagree) to
5 (strongly agree). The questionnaire was distributed to 240 respondents from the 12 hospitals,
with 20 respondents from each hospital, including hospital directors or deputy directors, heads
of medical records units, health informatics or IT staff, specialist physicians, and senior nurses.
Respondents were selected through stratified purposive sampling to ensure representation
across professional roles and levels of EHR exposure.
The instrument’s content validity was confirmed through expert review by three health
informatics specialists and one hospital management expert, resulting in a Content Validity
Index (CVI) of 0.89. A pilot study involving 30 respondents from a non-participating RSUD
produced a Cronbach’s alpha coefficient of 0.84, indicating good reliability (Polit & Beck,
2008) Quantitative data were analyzed using IBM SPSS Statistics version 26 through
descriptive statistics, Spearman rank correlation, and binary logistic regression to identify
predictors of low interoperability readiness, defined as a mean domain score below 3.0 (Pallant,
2020)
For the qualitative strand, data were obtained through semi-structured in-depth
interviews and two focus group discussions (FGDs) involving 36 key informants who were
directly involved in EHR or SATUSEHAT-related decision-making. The informants consisted
157

of hospital directors (n = 12), heads of medical records units (n = 12), and IT coordinators or
SIMRS administrators (n = 12). The interview guides were developed iteratively after pilot
review and covered infrastructure experience, organizational decision-making in digital
adoption, perceptions of regulatory mandates, inter-departmental coordination challenges, and
staff readiness. Each interview lasted approximately 45 to 60 minutes and was conducted either
face-to-face or via video call, depending on participant accessibility.
All sessions were audio-recorded with consent and transcribed verbatim. Qualitative data
were analyzed using reflexive thematic analysis following (Braun et al., 2006) six-phase
procedure, supported by NVivo version 14. Trustworthiness was strengthened through member
checking by returning preliminary themes to five participants for validation (Lincoln, Y. S., &
Guba, E. G. (1985). Naturalistic... - Google Scholar, n.d.) Finally, quantitative and qualitative
findings were integrated through joint display analysis by mapping barrier prevalence against
qualitative themes to identify convergence, complementarity, and divergence, thereby
strengthening the interpretive validity of the study (Fetters et al., 2013).
RESULTS AND DISCUSSION
This section presents the integrated findings from the quantitative survey (n = 240) and
qualitative strands (n = 36 key informants) across 12 district hospitals (RSUD) in three
Indonesian provinces. Results are organized into four sub-sections: (1) respondent
characteristics, (2) quantitative barrier domain scores and logistic regression predictors, (3)
qualitative themes, and (4) an integrated joint display analysis.
Result
Respondent Characteristics
A total of 240 respondents completed the structured questionnaire, achieving a response
rate of 100% across all 12 participating hospitals (20 respondents per site). Table 1 summarizes
the sociodemographic and professional characteristics of participants. The largest professional
groups were specialist physicians and senior nurses (35.0% each), followed by health
informatics and IT staff (20.0%). Mean years of EHR-related experience was 3.2 years (SD =
1.8). Regarding hospital-level digital maturity, the majority of facilities (41.7%) fell within the
"Emerging" category (score 2.0–2.9), consistent with national benchmarks reported by the
Indonesian Ministry of Health (2024), with a mean institutional maturity score of 2.81 (SD =
0.73).
158

Implementation Barriers of Electronic Health Record Interoperability in Indonesian District Hospitals: A
Mixed-Methods Study
Table 1. Sociodemographic and Professional Characteristics of Respondents (n = 240)
|     | Characteristic  | n  %  | Mean (SD)  |
| --- | --------------- | ----- | ---------- |
Professional Role
| Hospital Director / Deputy Director  |     | 12  5.0   |     |
| ------------------------------------ | --- | --------- | --- |
| Head of Medical Records Unit         |     | 12  5.0   |     |
| Health Informatics / IT Staff        |     | 48  20.0  |     |
| Specialist Physician                 |     | 84  35.0  |     |
| Senior Nurse                         |     | 84  35.0  |     |
Province
| West Java           |     | 80  33.3  |     |
| ------------------- | --- | --------- | --- |
| Central Kalimantan  |     | 80  33.3  |     |
| East Nusa Tenggara  |     | 80  33.3  |     |
Years of EHR Experience
| < 1 year                                    |     | 42  17.5  |            |
| ------------------------------------------- | --- | --------- | ---------- |
| 1 – 3 years                                 |     | 98  40.8  |            |
| 4 – 6 years                                 |     | 72  30.0  |            |
| > 6 years                                   |     | 28  11.7  |            |
| Mean years of experience (all respondents)  |     |           | 3.2 (1.8)  |
Hospital Digital Maturity (0–5 scale)
| Foundational (0.0–1.9)                |     | 2  16.7  |              |
| ------------------------------------- | --- | -------- | ------------ |
| Emerging (2.0–2.9)                    |     | 5  41.7  |              |
| Established (3.0–3.9)                 |     | 3  25.0  |              |
| Advanced (4.0–5.0)                    |     | 2  16.7  |              |
| Mean hospital digital maturity score  |     |          | 2.81 (0.73)  |
Note: Data reflect purposive stratified sampling across 12 RSUD in West Java, Central
Kalimantan, and East Nusa Tenggara.

Quantitative Findings: Barrier Domain Scores and Predictors
Table 2 presents mean Likert scores and barrier prevalence across the six domains of the
TOE–UTAUT composite instrument. Vendor and System Interoperability recorded the lowest
mean score (M = 2.19, SD = 0.72), indicating the highest perceived barrier, with 61.3% of
respondents classified in the high-barrier tier (score < 2.5). Technical Infrastructure Readiness
was the second most problematic domain (M = 2.31, SD = 0.61), followed by HR Competency
and Digital Literacy (M = 2.47, SD = 0.69). Regulatory Compliance Awareness (M = 3.12)
and Perceived Usefulness (M = 3.45) were the least obstructive domains; however, qualitative
triangulation revealed important nuances around regulatory ambiguity not fully captured by the
quantitative scores (see Section 6.3 and Figure 1)

159

Table 2. Descriptive Statistics of EHR Interoperability Barrier Domains (n = 240)
% High
Barrier
Barrier Domain Mean SD Min Max
(score <
2.5)
1. Technical Infrastructure
2.31 0.61 1.00 4.20 54.2%
Readiness
2. Organizational Capacity
2.58 0.74 1.20 4.80 42.1%
& Leadership
3. Regulatory Compliance
3.12 0.58 1.80 5.00 18.3%
Awareness
4. HR Competency &
2.47 0.69 1.00 4.60 48.8%
Digital Literacy
5. Vendor & System
2.19 0.72 1.00 4.00 61.3%
Interoperability
6. Perceived Usefulness &
3.45 0.53 2.00 5.00 10.4%
Intention
Overall Composite Score 2.69 0.64 — — 45.8%
Note: High barrier = mean domain score < 2.5; scores based on 5-point Likert scale (1 =
strongly disagree, 5 = strongly agree). Items were reverse-coded where appropriate so that
lower scores consistently indicate higher barriers.
Figure 1. Mean Barrier Scores by Domain Across 12 District Hospitals (n = 240; error bars = ±1
SD). Dashed line denotes neutral threshold (3.0).
Provincial disaggregation (Figure 2) revealed a pronounced east-west gradient in barrier
severity. Hospitals in East Nusa Tenggara reported the highest proportion of respondents in the
high-barrier tier (68.8%), compared to 47.5% in Central Kalimantan and 28.8% in West Java,
reflecting the well-documented digital infrastructure deficit in eastern Indonesia.
160

Implementation Barriers of Electronic Health Record Interoperability in Indonesian District Hospitals: A
Mixed-Methods Study
Figure 2. Distribution of EHR Interoperability Barrier Levels by Province (n = 240).
Percentages within bars indicate proportion of respondents per tier.
Binary logistic regression was conducted to identify independent predictors of low
interoperability readiness (composite score < 3.0). As shown in Table 3, low Technical
Infrastructure Readiness (OR = 6.30, 95% CI [2.77, 14.34], p < .001), low Vendor and System
Interoperability (OR = 5.00, 95% CI [2.33, 10.73], p < .001), and low HR Competency (OR =
3.63, 95% CI [1.76, 7.49], p = .001) were the strongest independent predictors. Geographic
location (East Nusa Tenggara vs. West Java: OR = 4.18, p = .002) and lower hospital digital
maturity scores (OR = 0.33 per unit increase, p = .001) were significant control variables.
Regulatory Compliance Awareness did not reach statistical significance (p = .157), though
qualitative data offered explanatory context for this finding,The overall model demonstrated
adequate fit (Nagelkerke R² = 0.41; Hosmer–Lemeshow test, χ² = 6.27, p = .618; overall
classification accuracy = 78.3%).
Table 3. Binary Logistic Regression Predicting Low EHR Interoperability Readiness (n
= 240)
Predictor Variable B SE OR 95% CI p-value
TOE Framework Domains
Technical Infrastructure
1.84 0.42 6.30 [2.77–14.34] < .001*
Readiness (low)
Vendor & System
1.61 0.39 5.00 [2.33–10.73] < .001*
Interoperability (low)
HR Competency & Digital
1.29 0.37 3.63 [1.76–7.49] .001*
Literacy (low)
Organizational Capacity
0.98 0.41 2.66 [1.20–5.93] .016*
(low)
Regulatory Compliance
0.54 0.38 1.72 [0.81–3.63] .157
Awareness (low)
Control Variables
Province (ref = West Java)
Central Kalimantan 0.87 0.44 2.39 [1.01–5.65] .047*
161

Predictor Variable B SE OR 95% CI p-value
East Nusa Tenggara 1.43 0.46 4.18 [1.70–10.28] .002*
Years of EHR Experience
−0.61 0.29 0.54 [0.31–0.96] .036*
(ref = < 1 yr)
Hospital Maturity Score
−1.12 0.33 0.33 [0.17–0.63] .001*
(continuous)
Note. B = unstandardized logistic regression coefficient; SE = standard error; OR = odds ratio;
95% CI = 95% confidence interval. * p < .05.
Qualitative Findings: Thematic Analysis
Reflexive thematic analysis of 36 semi-structured interviews and two FGDs yielded six
primary themes, as illustrated in Figure 3. Inadequate network infrastructure and connectivity
was the most frequently referenced theme (n = 34, 94.4%), followed by low digital literacy
among clinical staff (n = 32, 88.9%) and vendor lock-in and non-standardized SIMRS formats
(n = 29, 80.6%). Ambiguous regulatory guidance was raised by 21 informants (58.3%), often
framed as a perception that enforcement mechanisms lacked teeth at the district level — a
finding that provides explanatory context for the non-significant regulatory compliance
coefficient in the regression model. Leadership and budget constraints (n = 27, 75.0%) and
clinician resistance to workflow change (n = 18, 50.0%) were also prominent themes,
particularly in outer-island sites. These themes were vividly illustrated in informants' own
words. On network infrastructure, an IT coordinator in East Nusa Tenggara described that "our
internet drops constantly during peak hours; staff just give up and write on paper." On vendor
interoperability, a head of medical records in Central Kalimantan explained that "each vendor
uses its own data structure. Connecting to SATUSEHAT feels like building a new system from
scratch." Regarding regulatory enforcement, a head of medical records in West Java observed
that "we know the regulation, but no one came to check. So we are not in a hurry," reinforcing
the study's finding that awareness of the SATUSEHAT mandate did not consistently translate
into implementation urgency.
Figure 3. Frequency of Qualitative Themes Identified Across In-Depth Interviews and FGDs (n
= 36 informants). Dotted line = 50% threshold.
162

Implementation Barriers of Electronic Health Record Interoperability in Indonesian District Hospitals: A
Mixed-Methods Study
Integrated Joint Display: Convergence, Expansion, and Divergence
Table 4 presents the joint display analysis integrating quantitative domain scores with
qualitative themes and representative informant quotes. Convergence between strands was
evident for four of the six domains, particularly for Technical Infrastructure and Vendor
Interoperability, where both datasets consistently signaled high barriers. An expansion function
was observed for HR and Digital Literacy — while the quantitative score identified it as a high
barrier, qualitative data elaborated on the generational and cultural dimensions of technology
resistance not captured by the survey instrument. A partial divergence was noted for Regulatory
Compliance Awareness: the quantitative score was moderate (M = 3.12), suggesting adequate
awareness, yet qualitative accounts revealed that awareness did not translate into urgency due
to perceived weak enforcement by district health offices.

Table 4. Joint Display Analysis: Quantitative–Qualitative Integration of EHR
Interoperability Barriers
Quantitative
| Barrier  |          | Qualitative  | Integration  |                     |     |     |
| -------- | -------- | ------------ | ------------ | ------------------- | --- | --- |
|          | Finding  |              |              | Illustrative Quote  |     |     |
| Domain   |          | Theme        | Outcome      |                     |     |     |
(Mean Score)
|                 |             | Inadequate      |              | "Our                       | internet  | drops  |
| --------------- | ----------- | --------------- | ------------ | -------------------------- | --------- | ------ |
|                 |             | network         |              | constantly                 | during    | peak   |
| Techn  ical     | 2.31 (High  |                 |              |                            |           |        |
|                 |             | connectivity &  | Convergence  | hours; staff just give up  |           |        |
| Infrastructure  | barrier)    |                 |              |                            |           |        |
|                 |             | hardware        |              | and write on paper." (IT   |           |        |
|                 |             | obsolescence    |              | Coordinator, East NTT)     |           |        |
"Each vendor uses its own
|     |     |                  |     | data        | structure.  |     |
| --- | --- | ---------------- | --- | ----------- | ----------- | --- |
|     |     | Vendor lock-in;  |     | Connecting  |             | to  |
Vendor  2.19 (Highest  non-standardized  SATUSEHAT  feels  like
Convergence
Interoperability  barrier)  SIMRS data  building  a  new  system
|     |     | formats  |     | from  scratch."  | (Head  | of  |
| --- | --- | -------- | --- | ---------------- | ------ | --- |
Medical Records, Central
Kalimantan)
"Doctors here are senior;
|     |     | Low digital  |     | some have never used a  |     |     |
| --- | --- | ------------ | --- | ----------------------- | --- | --- |
HR & Digital  2.47 (High  competency;  computer before. Training
Expansion
| Literacy  | barrier)  | resistance to    |     | one hour is not enough."  |            |       |
| --------- | --------- | ---------------- | --- | ------------------------- | ---------- | ----- |
|           |           | workflow change  |     | (Hospital                 | Director,  | East  |
NTT)
"We had a good IT officer
but he left for a private
Budget
|                 | 2.58       |                    |              | hospital.         | We  have  | had     |
| --------------- | ---------- | ------------------ | ------------ | ----------------- | --------- | ------- |
| Organizational  |            | constraints; high  |              |                   |           |         |
|                 | (Moderate– |                    | Convergence  | three  different  | people    | in      |
| Capacity        |            | staff turnover in  |              |                   |           |         |
|                 | high)      |                    |              | that  role        | this      | year."  |
IT roles
(Deputy Director, Central
Kalimantan)
|             |             | Awareness    |             | "We know the regulation,    |     |     |
| ----------- | ----------- | ------------ | ----------- | --------------------------- | --- | --- |
|             |             | present but  |             | but no one came to check.   |     |     |
| Regulatory  | 3.12        |              | Partial     |                             |     |     |
|             |             | enforcement  |             | So we are not in a hurry."  |     |     |
| Compliance  | (Moderate)  |              | Divergence  |                             |     |     |
|             |             | ambiguity    |             | (Head of Medical            |     |     |
|             |             | persists     |             | Records, West Java)         |     |     |
"Everyone agrees that
| Perceived   | 3.45 (Low  | Staff recognize    |            |                            |     |     |
| ----------- | ---------- | ------------------ | ---------- | -------------------------- | --- | --- |
|             |            |                    | Expansion  | having one patient record  |     |     |
| Usefulness  | barrier)   | long-term benefit  |            |                            |     |     |
is good. The question is
163

Quantitative
Barrier Qualitative Integration
Finding Illustrative Quote
Domain Theme Outcome
(Mean Score)
but doubt short- who will pay and who
term feasibility will train us." (Senior
Nurse, West Java)
Note: Integration outcomes classified as Convergence (both strands confirm), Expansion
(qualitative elaborates quantitative), or Partial Divergence (discordant signals requiring
interpretive explanation).
Collectively, these findings indicate that EHR interoperability barriers in Indonesian
district hospitals are predominantly structural and technical in nature, but are substantially
compounded by human resource deficits and organizational governance gaps. The joint display
analysis confirms that mixed-methods integration yielded a richer explanatory picture than
either strand alone could have produced, particularly in explaining the regulatory compliance
paradox and the depth of frontline resistance to digital workflow transformation.
Discussion
Structural and Technical Barriers to EHR Interoperability
The findings indicate that technical infrastructure and vendor interoperability remain the
most critical barriers to EHR interoperability in Indonesian district hospitals. Vendor and
system interoperability recorded the lowest mean score, followed by technical infrastructure
readiness, showing that hospitals continue to face difficulties related to unstable connectivity,
outdated hardware, fragmented SIMRS platforms, and limited standardization across vendors.
These results suggest that the adoption of SATUSEHAT cannot be understood merely as a
regulatory or administrative requirement, but as a complex technical transformation that
depends on the availability of reliable digital infrastructure and compatible information
systems. This finding is consistent with previous studies showing that interoperability in low-
and middle-income countries is frequently constrained by fragmented digital platforms,
inconsistent data structures, and weak technical capacity (Giri & Din, 2025; Hamzah et al.,
2025). These technical constraints are consistent with broader evidence that achieving genuine
interoperability across digital health solutions depends not merely on adopting a common
standard but on resolving persistent gaps in technical implementation, data mapping, and cross-
vendor compatibility Martins et al. (2025) and with Technology-Organization-Environment
analyses in comparable low-resource hospital settings showing that the benefits of digital
health technologies for staff performance are realized only when technological readiness is
matched by adequate organizational and environmental support (Jeilani & Hussein, 2025)
The qualitative findings strengthen this interpretation by showing that hospital
informants frequently described internet instability, obsolete devices, and vendor lock-in as
practical obstacles in daily implementation. The persistence of vendor-specific data structures
makes integration with SATUSEHAT difficult because hospitals must adapt or rebuild parts
of their existing systems to meet national interoperability requirements. This aligns with the
broader digital health literature, which emphasizes that interoperability is not only about
adopting a national platform, but also about ensuring semantic, technical, and organizational
compatibility between local systems and national standards such as HL7 FHIR (Faisal &
Nakayama, 2024) Therefore, the study demonstrates that district hospitals require targeted
164

Implementation Barriers of Electronic Health Record Interoperability in Indonesian District Hospitals: A
Mixed-Methods Study
infrastructure investment and stronger vendor governance before EHR interoperability can be
implemented effectively.
Human Resource Readiness and Digital Literacy
Human resource competency and digital literacy emerged as another major barrier to
EHR interoperability. Although many respondents recognized the long-term value of
integrated patient records, the implementation process was hindered by limited digital skills
among clinical and administrative staff. This gap was especially visible among senior clinicians
and staff who had limited prior exposure to computerized systems. The results support the
Unified Theory of Acceptance and Use of Technology, which explains that technology
adoption is shaped not only by perceived usefulness, but also by effort expectancy, facilitating
conditions, and users’ confidence in operating the system Venkatesh et al. (2003) In this study,
the relatively high perceived usefulness score indicates that staff were not rejecting the idea of
EHR interoperability itself, but were struggling with the practical capacity required to use it
consistently. This pattern reflects the broader concept of digital health literacy as a critical,
multidimensional competency that determines whether healthcare professionals and patients
alike can meaningfully engage with and benefit from digital health technologies, rather than
merely have access to them Wamala Andersson & Gonzalez (2025)
The qualitative data further reveal that short, one-time training sessions are insufficient
to build sustainable digital competency. Informants noted that some staff returned to paper-
based documentation when systems were slow, confusing, or poorly integrated into clinical
workflows. This finding is consistent with previous research showing that digital health
implementation often fails when human factors, workflow adaptation, and continuous training
are treated as secondary issues (Alzghaibi & Hutchings, 2025) Giri & Din, 2025). Therefore,
improving EHR interoperability in district hospitals requires more than technical deployment;
it requires continuous mentoring, role-based training, peer support, and workflow redesign that
allows users to adopt digital systems without increasing their administrative burden. This is
consistent with meta-analytic evidence from other low- and middle-income health systems
showing that digital literacy among health professionals varies substantially by profession,
training exposure, and institutional support, underscoring the need for structured, role-based
digital competency development rather than one-off training sessions Chereka et al. (2024)
Organizational Capacity, Leadership, and Governance
The study also found that organizational capacity and leadership significantly influenced
interoperability readiness. Hospitals with weaker leadership support, limited digital budgets,
and high turnover among IT staff were more likely to report low readiness. In district hospitals,
interoperability implementation often competes with other urgent operational priorities,
making it difficult for leaders to allocate sufficient budget, staff, and time for digital
transformation. As a result, EHR integration becomes a compliance-driven activity rather than
a strategic institutional agenda. This finding echoes a systematic review of information
technology governance in healthcare facilities, which found that the absence of formal
governance structures, unclear role assignment, and insufficient top-management engagement
are recurring obstacles to embedding digital transformation as a core institutional priority rather
than a peripheral compliance task (Saladdin & Handayani, 2025)
165

Qualitative findings showed that some hospitals depended heavily on one or two IT
personnel, creating vulnerability when these staff moved to other institutions. This condition
reflects the limited institutionalization of digital health governance at the hospital level.
Therefore, hospital leadership must play a stronger role in establishing digital governance
teams, assigning clear responsibilities, securing sustainable funding, and coordinating clinical,
administrative, and technical units. Without organizational ownership, interoperability
initiatives may remain fragmented and highly dependent on external vendors or temporary
regulatory pressure. Similarly, evidence from a Technology-Organization-Environment
assessment of big data adoption readiness among healthcare employees indicates that
organizational readiness, rather than technological capability alone, is often the binding
constraint on sustained digital transformation in resource-limited healthcare settings,
reinforcing the need for deliberate investment in institutional capacity alongside infrastructure
(Ghaleb et al., 2021).
Regulatory Awareness and the Implementation Gap
An important finding of this study is the partial divergence between quantitative and
qualitative results in the regulatory domain. Quantitatively, regulatory compliance awareness
was not among the strongest predictors of low interoperability readiness, suggesting that many
respondents were already aware of national requirements related to EMR and SATUSEHAT
integration. However, qualitative findings revealed that awareness did not always translate into
implementation urgency. Some informants perceived that enforcement from district health
authorities was unclear or inconsistent, reducing the pressure to complete integration. This
finding shows that policy awareness alone is insufficient when regulations are not accompanied
by practical guidance, monitoring, incentives, and accountability mechanisms.
This implementation gap reflects the broader challenge of translating national digital
health policy into local hospital practice. Indonesia’s Ministry of Health Regulation Number
24 of 2022 established a clear mandate for healthcare facilities to adopt electronic medical
records and integrate with SATUSEHAT, yet the findings suggest that district hospitals still
require operational support to meet this mandate (Kementerian Kesehatan Republik Indonesia,
2022). Therefore, national and regional authorities should strengthen implementation support
throughclearer technical guidelines, regular monitoring, capacity-building programs, and
differentiated assistance for hospitals in areas with lower digital maturity. International
experience with national digital maturity assessments further suggests that sustained
monitoring of hospital-level digital maturity, covering interoperability, leadership, governance,
and infrastructure, can help identify where regulatory and technical assistance should be
prioritized, although such assessments also carry known risks of self-reporting bias and
measurement inconsistency that should be anticipated in any future SATUSEHAT monitoring
framework Cresswell et al. (2025)
Study Limitations
This study has several limitations that should be considered when interpreting the
findings. First, the 12 RSUD type C and D hospitals were purposively selected across three
provinces, and although this design allowed for in-depth comparison across contrasting digital
maturity contexts, the findings cannot be statistically generalized to all district hospitals in
166

Implementation Barriers of Electronic Health Record Interoperability in Indonesian District Hospitals: A
Mixed-Methods Study
Indonesia. Second, the cross-sectional design of the quantitative strand means that the reported
associations between predictors (e.g., infrastructure readiness, vendor interoperability) and low
interoperability readiness are correlational rather than causal, and the direction of these
relationships cannot be firmly established. Third, self-reported questionnaire and interview
data may be subject to social desirability or recall bias, particularly regarding sensitive topics
such as institutional readiness and regulatory compliance. Finally, one source used to
contextualize national digital maturity benchmarks (Healthcare IT News, 2024) is a news outlet
rather than a peer-reviewed publication; it was retained because it reported figures from an
official Ministry of Health assessment, but readers should treat this contextual benchmark with
appropriate caution pending peer-reviewed confirmation.
CONCLUSION
This study concludes that the implementation of Electronic Health Record (EHR)
interoperability in Indonesian district hospitals remains constrained by interconnected
technical, organizational, regulatory, and human resource barriers. The findings show that
vendor and system interoperability, technical infrastructure readiness, and human resource
competency are the most critical factors influencing low interoperability readiness. Although
hospital staff generally recognize the usefulness of integrated electronic health records, this
awareness has not been fully translated into effective implementation due to unstable internet
connectivity, fragmented SIMRS platforms, vendor lock-in, limited digital literacy, insufficient
training, and weak institutional capacity. These findings confirm that EHR interoperability is
not merely a technological issue, but a socio-technical transformation that requires alignment
between infrastructure, human resources, organizational governance, and regulatory
enforcement.
The mixed-methods approach provided a more comprehensive understanding of the
implementation gap between national digital health policy and district-level hospital readiness.
Quantitative findings identified the strongest predictors of low interoperability readiness, while
qualitative findings explained how these barriers are experienced in everyday hospital
operations. The partial divergence between regulatory awareness and actual implementation
further indicates that policy mandates alone are insufficient without practical technical
guidance, continuous monitoring, adequate funding, and localized capacity-building support.
Therefore, the success of SATUSEHAT integration in district hospitals depends on
coordinated efforts among hospital leaders, regional health authorities, national policymakers,
and system vendors.
The significance of this study lies in its contribution to evidence-based digital health
policy and hospital management practice in Indonesia. By focusing on RSUD type C and D
hospitals across provinces with different levels of digital maturity, this study highlights the
need for differentiated implementation strategies rather than a uniform national approach.
Hospitals in regions with lower infrastructure capacity require stronger technical assistance,
sustained digital literacy programs, interoperable vendor standards, and dedicated financial
support. Future digital health transformation should prioritize not only compliance with
electronic medical record regulations, but also the development of sustainable interoperability
ecosystems that are technically reliable, organizationally supported, and responsive to local
hospital realities. These conclusions should be read in light of the study's limitations,
167

particularly the purposive, non-random selection of 12 RSUD and the cross-sectional design,
which restrict statistical generalizability and preclude causal inference (see Study Limitations).
Building on these findings, future research should pursue: longitudinal assessment of
interoperability readiness before and after structured SATUSEHAT training and technical
assistance interventions; comparative, multi-region studies systematically contrasting Java and
outer-island hospitals to test whether the barrier patterns identified here generalize beyond the
three provinces studied; and (3) development and psychometric validation of a district-hospital-
specific digital readiness index that hospital managers and regional authorities could use for
routine self-assessment.
REFERENCES
Alzghaibi, H., & Hutchings, H. (2025). Exploring electronic health record systems
implementation in primary health care centres in Saudi Arabia: pre-post implementation.
Frontiers in Medicine, 12. https://doi.org/10.3389/FMED.2025.1502184/FULL
Bostan, S., Johnson, O. A., Jaspersen, L. J., & Randell, R. (2024). Contextual barriers to
implementing open-source electronic health record systems for low-and lower-middle-
income countries: scoping review. Jmir.OrgS Bostan, OA Johnson, LJ Jaspersen, R
RandellJournal of Medical Internet Research, 2024•jmir.Org, 26.
https://doi.org/10.2196/45242
Braun, V., psychology, V. C.-Q. research in, & 2006, undefined. (2006). Using thematic
analysis in psychology. Taylor & FrancisV Braun, V ClarkeQualitative Research in
Psychology, 2006•Taylor & Francis, 3(2), 77–101.
https://doi.org/10.1191/1478088706QP063OA
Chereka, A. A., Walle, A. D., Kassie, S. Y., Shibabaw, A. A., Butta, F. W., Demsash, A. W.,
Hunde, M. K., Dubale, A. T., Bekana, T., Kitil, G. W., Emanu, M. D., & Tadesse, M. N.
(2024). Evaluating digital literacy of health professionals in Ethiopian health sectors: a
systematic review and meta-analysis. Journals.Plos.OrgAA Chereka, AD Walle, SY
Kassie, AA Shibabaw, FW Butta, AW Demsash, MK HundePlos One,
2024•journals.Plos.Org, 19(5). https://doi.org/10.1371/JOURNAL.PONE.0300344
Cresswell, K., Jahn, F., Silsand, L., Woods, L., Postema, T., Logan, M., Malkic, S., &
Ammenwerth, E. (2025). Assessing digital maturity of hospitals: viewpoint comparing
national approaches in five countries. Jmir.OrgK Cresswell, F Jahn, L Silsand, L Woods,
T Postema, M Logan, S Malkic, E AmmenwerthJournal of Medical Internet Research,
2025•jmir.Org, 27. https://doi.org/10.2196/57858
Creswell, J. W., & Plano Clark, V. L. (2018). Designing... - Google Scholar. (n.d.). Retrieved
July 1, 2026, from
https://scholar.google.com/scholar?hl=id&as_sdt=0%2C5&q=Creswell%2C+J.+W.%2C
+%26+Plano+Clark%2C+V.+L.+%282018%29.+Designing+and+conducting+mixed+m
ethods+research+%283rd+ed.%29.+SAGE+Publications.&btnG=
Faisal, H. P., & Nakayama, M. (2024). Implementation of the World Health Organization
Minimum Dataset for Emergency Medical Teams to Create Disaster Profiles for the
Indonesian SATUSEHAT. Medinform.Jmir.OrgHP Faisal, M NakayamaJMIR Medical
Informatics, 2024•medinform.Jmir.Org, 12. https://doi.org/10.2196/59651
168

Implementation Barriers of Electronic Health Record Interoperability in Indonesian District Hospitals: A
Mixed-Methods Study
Fetters, M. D., Curry, L. A., & Creswell, J. W. (2013). Achieving integration in mixed methods
designs—principles and practices. Wiley Online LibraryMD Fetters, LA Curry, JW
CreswellHealth Services Research, 2013•Wiley Online Library, 48(6 PART2), 2134–
2156. https://doi.org/10.1111/1475-6773.12117
Ghaleb, E. A. A., Dominic, P. D. D., Fati, S. M., Muneer, A., & Ali, R. F. (2021). The
assessment of big data adoption readiness with a technology–organization–environment
framework: a perspective towards healthcare employees. Mdpi.ComEAA Ghaleb, PDD
Dominic, SM Fati, A Muneer, RF AliSustainability, 2021•mdpi.Com, 13(15).
https://doi.org/10.3390/SU13158379
Heryawan, L., Mori, Y., Yamamoto, G., Kume, N., Lazuardi, L., Fuad, A., & Kuroda, T.
(2025). Fast Healthcare Interoperability Resources (FHIR)–Based Interoperability Design
in Indonesia: Content Analysis of Developer Hub’s Social Networking.
Formative.Jmir.OrgL Heryawan, Y Mori, G Yamamoto, N Kume, L Lazuardi, A Fuad, T
KurodaJMIR Formative Research, 2025•formative.Jmir.Org, 9.
https://doi.org/10.2196/51270
Jeilani, A., & Hussein, A. (2025). Impact of digital health technologies adoption on healthcare
workers’ performance and workload: perspective with DOI and TOE models. SpringerA
Jeilani, A HusseinBMC Health Services Research, 2025•Springer, 25(1), 271.
https://doi.org/10.1186/S12913-025-12414-4
Kassie, S. Y., Shibabaw, A. A., Chereka, A. A., Dubale, A. T., Demsash, A. W., Damtie, Y.,
Ngusie, H. S., & Walle, A. D. (2025). The impact of confidentiality and privacy concerns
on behavioral intention to adopt electronic personal health records among chronic patients
in southwest Ethiopia in 2023: an application of the UTAUT2 model. Frontiers in Digital
Health, 7. https://doi.org/10.3389/FDGTH.2025.1475460/FULL
Kyratsis, Y., Scarbrough, H., Begley, A., & Denis, J. L. (2022). Editorial: Digital health
adoption: Looking beyond the role of technology. Frontiers in Digital Health, 4, 989003.
https://doi.org/10.3389/FDGTH.2022.989003/FULL
Lincoln, Y. S., & Guba, E. G. (1985). Naturalistic... - Google Scholar. (n.d.). Retrieved July 1,
2026, from
https://scholar.google.com/scholar?hl=id&as_sdt=0%2C5&q=Lincoln%2C+Y.+S.%2C+
%26+Guba%2C+E.+G.+%281985%29.+Naturalistic+inquiry.+SAGE+Publications.&bt
nG=
Martins, D., Lewerenz, S., Carmo, A., & Martins, H. (2025). Interoperability of telemonitoring
data in digital health solutions: a scoping review. Frontiers in Digital Health, 7.
https://doi.org/10.3389/FDGTH.2025.1502260/FULL
Organization, W. H. (2025). Global strategy on digital health 2020-2027.
https://books.google.com/books?hl=id&lr=&id=_DWcEQAAQBAJ&oi=fnd&pg=PA2
&dq=World+Health+Organization.+(2021).+Global+strategy+on+digital+health+2020
%E2%80%932025.+World+Health+Organization.+https://www.who.int/publications/i/it
em/9789240020924&ots=rVtEiDs-LW&sig=FofDFWX6ADH36hlFLwE23wncVpU
Pallant, J. (2020). SPSS survival manual: A step by step guide to data analysis using IBM
SPSS. SPSS: SURVIVAL MANUAL: A STEP BY STEP GUIDE TO DATA ANALYSIS
USING IBM SPSS: 7th EDITION, 1–361. https://doi.org/10.4324/9781003117452
169

Policy, B. A. J.-J. of S. and T., & 2024, undefined. (2024). Examining the adoption of telehealth
during public health emergencies based on technology organization environment
framework. Emerald.ComB Anthony JnrJournal of Science and Technology Policy
Management, 2024•emerald.Com, 15(6), 1311–1338. https://doi.org/10.1108/JSTPM-05-
2022-0079
Polit, D., & Beck, C. (2008). Nursing research: Generating and assessing evidence for nursing
practice.
https://books.google.com/books?hl=id&lr=&id=Ej3wstotgkQC&oi=fnd&pg=PA1&dq=
Polit,+D.+F.,+%26+Beck,+C.+T.+(2021).+Nursing+research:+Generating+and+assessi
ng+evidence+for+nursing+practice+(11th+ed.).+Wolters+Kluwer.&ots=wiQxIScEEr&s
ig=pWIbT9C7ZNgYo1ewsdgiKoffmdc
Saladdin, I. R., & Handayani, P. W. (2025). Information Technology Governance
Implementation Challenges in Healthcare Facilities: A Systematic Literature Review.
Journals.Sagepub.ComIR Saladdin, PW HandayaniSage Open,
2025•journals.Sagepub.Com, 15(4). https://doi.org/10.1177/21582440251369322
Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User Acceptance of
Information Technology: Toward A Unified View1. Misq.Umn.EduV Venkatesh, MG
Morris, GB Davis, FD DavisMIS Quarterly, 2003•misq.Umn.Edu, 27(3), 425–478.
https://doi.org/10.2307/30036540
Wamala Andersson, S., & Gonzalez, M. P. (2025). Digital health literacy—a key factor in
realizing the value of digital transformation in healthcare. Frontiers in Digital Health, 7,
1461342. https://doi.org/10.3389/FDGTH.2025.1461342/FULL
Yi, S., Yam, E. L. Y., Cheruvettolil, K., Linos, E., Gupta, A., Palaniappan, L., Rajeshuni, N.,
Vaska, K. G., Schulman, K., & Eggleston, K. N. (2024). Perspectives of digital health
innovations in low-and middle-income health care systems from South and Southeast
Asia. Jmir.OrgS Yi, ELY Yam, K Cheruvettolil, E Linos, A Gupta, L Palaniappan, N
Rajeshuni, KG VaskaJournal of Medical Internet Research, 2024•jmir.Org, 26(1).
https://doi.org/10.2196/57612
170
