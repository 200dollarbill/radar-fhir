JAMIA Open, 2025, 8(4), ooaf085
https://doi.org/10.1093/jamiaopen/ooaf085
Research and Applications
Research and Applications
Assessment of 3 standards-based clinical decision support
(CDS) tools in an academic electronic health record using
Clinical Quality Language, CDS Hooks, and Fast Healthcare
Interoperability Resources: a retrospective evaluation
Mark Isabelle, BA1, Ivan K. Ip, MD, MPH1,2, Michael Bakhtin, PhD1,3, Louise Schneider, MD1,4,
Ali S. Raja, MD, DBA, MPH1,5,6, Sayon Dutta, MD, MPH5,6, Adam Landman, MD6,7,
Ronilda Lacson, MD, PhD
�,1,8
1Center for Evidence-Based Imaging, Department of Radiology, Brigham and Women’s Hospital, Boston, MA 02120, United States,
2Covenant Health, Inc, Tewksbury, MA, 01876, United States, 3Aluna Health, Cambridge, MA, 02142, United States, 4Department of Medicine,
Harvard Medical School, Boston, MA, 02115, United States, 5Department of Emergency Medicine, Massachusetts General Hospital, Boston,
MA, 02114, United States, 6Department of Emergency Medicine, Harvard Medical School, Boston, MA, 02115, United States, 7Department of
Emergency Medicine, Brigham and Women’s Hospital, Boston, MA, 02115, United States, 8Department of Radiology, Harvard Medical
School, Boston, MA, 02115, United States
�
Corresponding author: Ronilda Lacson, MD, PhD, Center for Evidence-Based Imaging, Department of Radiology, Brigham and Women’s Hospital,
1620 Tremont Street, Third floor, Boston, MA 02120, United States (rlacson@bwh.harvard.edu)
Abstract
Objectives: To evaluate clinical decision support (CDS) of varying complexities and care settings represented using Health Information Technol-
ogy (HIT) standards—Clinical Quality Language (CQL) for representing clinical logic and Fast Healthcare Interoperability Resources (FHIR) for
health information exchange.
Materials and Methods: This Institutional Review Board-approved, retrospective study was performed at an academic medical center (January
1, 2023-December 31, 2023). Recommendations extracted from patient-centered outcomes guidelines were translated into standardized syntax
(SNOMED CT) and representations (CQL, FHIR). Clinical decision support Hooks applications were developed for: CDS1—provides education
for emergency department (ED) patients with venous thromboembolism; CDS2—recommends CT pulmonary angiogram in ED patients with
suspected pulmonary embolism (PE) and uses FHIR Questionnaire resources for representing interactive content; CDS3—recommends mam-
mography/breast magnetic resonance imaging surveillance in outpatients with breast cancer history. We randomly selected 50 ED patients
with suspected PE and 50 outpatients undergoing breast imaging surveillance. We compared outcomes of false-positive alerts and the accuracy
of CDS1, the more complex CDS2, and CDS3 for outpatients.
Results: Clinical decision support Hooks applications used CQL logic for trigger expressions and logic files and provided recommendations to
ED and outpatient providers. CDS1 had a false-positive alert and accuracy of 11.1% and 98%, respectively, not significantly different from
CDS2 (0.0% false-positive alerts, P¼.33 and 96% accuracy, P¼.56) or from CDS3 (0.0% false-positive alerts, P¼.15 and 100% accuracy,
P¼.31).
Discussion: Health Information Technology standards can represent recommendations of varying complexities in various care settings.
Conclusion: The potential to represent CDS using standardized syntax and formats can help facilitate the dissemination of CDS-consumable
artifacts.
Lay Summary
This study aimed to evaluate Health Information Technology (HIT) in the form of clinical decision support (CDS) applications to (1) provide educa-
tion for emergency department (ED) patients with blood clots forming in veins (venous thromboembolism); (2) recommend CT pulmonary angio-
gram testing in ED patients with suspected pulmonary embolism (PE) and uses Fast Healthcare Interoperability Resources (FHIR) Questionnaire
resources to represent interactive content; and (3) recommend mammography/breast magnetic resonance imaging surveillance in outpatients
with a history of breast cancer, when appropriate. Clinical decision support is represented using 3 HIT standards—Clinical Quality Language
(CQL) for representing clinical logic, CDS Hooks for invoking CDS from the clinical workflow, and FHIR for health information exchange. We ran-
domly selected 50 ED patients with suspected PE and 50 outpatients undergoing breast imaging surveillance to compare outcomes of
false-positive alerts and accuracy of the 3 CDS applications. We found that the 3 CDS applications represented using HIT standards can repre-
sent recommendations of varying complexities in various care settings and do not differ in false-positive alerts. The ability to represent CDS
using standardized syntax and formats can potentially facilitate the dissemination of CDS-consumable artifacts.
Key words: clinical decision support; information technology; health information exchange.
Received: March 17, 2025; Revised: July 7, 2025; Editorial Decision: July 14, 2025; Accepted: July 18, 2025
© The Author(s) 2025. Published by Oxford University Press on behalf of the American Medical Informatics Association.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which
permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

2 J A M I A O p e n, 2025, Vol. 8, No. 4
Background and significance standards. Level 4 includes case-control studies and those
with poor or nonindependent reference standards. Level 5
Well-implemented clinical decision support (CDS) can improve
health-care processes,1 including medical imaging.2–5 How- refers to expert opinions. The evidence sources were purpose-
fully selected to generate CDS of varying complexities and
ever, if poorly executed, CDS can create interruptive electronic
for various care settings.
health record (EHR) workflows and low-value clinical alerts,
potentially contributing to physician burnout,6,7 with little or CDS1 was a simple CDS Hooks application utilizing CQL
logic for the trigger expression and logic files. It aimed to pro-
no impact on imaging utilization or appropriateness. Integrat-
vide educational materials to ED patients with suspected pul-
ing patient-specific parameters and consideration of human
monary embolism (PE) and those with previous history of
factor design principles are important in developing CDS that
venous thromboembolism (VTE). CDS1 emphasized patients’
provide value to users.8,9Additionally, the strength of the evi-
preference for learning about thromboembolism symptoms,
dence underlying CDS recommendations may enhance or
risk factors, prevention, and complications in the context of a
impede the usability of CDS alerts10,11 and represents an
doctor-patient encounter.16 Educating patients regarding PE
important attribute in assessing practice guideline trustworthi-
can potentially minimize those requiring further manage-
ness.12 High rates of false-positive alerts (ie, low specificity)
ment, including testing and hospitalizations.
also contribute to low-value CDS.
CDS2 was a more complex CDS Hooks application with
The Harvard Medical School Library of Evidence (HMS-
the same trigger for recommending use of computed tomog-
LOE) has developed a publicly available online “evidence
raphy pulmonary angiogram (CTPA) in ED patients with sus-
library”10 to provide a repository of medical evidence that
pected PE. CDS2, however, proceeds to evaluate other
can be utilized in CDS systems, including for the imaging
elements in the EHR (eg, D-dimer) before returning a CDS
domain.13 However, graded evidence must be represented in
Hooks Card, one of which additionally used FHIR Question-
a more structured format for use as CDS. In particular, stand-
naire resources to represent interactive content for providers
ard formats can help facilitate interoperability and public dis-
to assess patient risk for PE. Given that the use of CTPA to
semination of CDS. Therefore, we aimed to evaluate diagnose PE is increasing,25 and that evidence-based guide-
accuracy and false-positive rates (FPRs) for CDS of various
lines for managing patients suspected of having PE exist, it is
complexities and combinations for different care settings,
an excellent target for evaluating the impact of CDS, as inte-
represented using Clinical Quality Language (CQL)14 and
grating CDS for CTPA has the potential to decrease poten-
Fast Healthcare Interoperability Resources (FHIR).15
tially unnecessary diagnostic imaging examinations while
minimizing patient risk.26,27
Materials and methods CDS3 was based on a recommendation in a PCORI-funded
grant19 for using breast magnetic resonance imaging (MRI)
Study setting and human subjects approval
(instead of or in addition to mammography) in outpatient
We conducted a 12-month, retrospective cohort study (Janu-
clinics for diagnosing a second breast cancer in women previ-
ary 1, 2023-December 31, 2023) at a tertiary academic medi-
ously diagnosed with breast cancer and addresses women at
cal center with an emergency department (ED) and an
highest risk for breast cancer. It emphasizes the use of surveil-
outpatient network spanning 183 practices and 1200 physi-
lance breast MRI which resulted in increased biopsy and sub-
cians. The study institution uses Epic (Epic Systems Corpora-
sequent cancer detection rate relative to the use of
tion) as its EHR across all care settings, and imaging orders
mammography alone. Given that only a minority of these
are placed via order entry within Epic. The Institutional women receive breast MRI, the potential impact of this
Review Board approved the study and waived the require- guideline is huge.
ment for informed consent.
CDS design principles and process
CDS applications
We used human factor principles to inform the design of the
We aimed to develop 3 CDS Hooks applications based on CDS applications, including minimizing false alarms, and the
preexisting patient-centered outcomes guidelines.16–19 We format of textual information and alert display.8 We also
specifically focused on CDS to address the need for radiologic included other sociotechnical factors from the Systems Engi-
imaging as the role of radiologic imaging in screening for and neering Initiative for Patient Safety model. Systems Engineer-
diagnosing disease has greatly expanded in the last 2 decades, ing Initiative for Patient Safety is based on a
with an estimated 400 million imaging tests conducted annu- macroergonomics works system model that integrates
ally.20,21Each unit of evidence from the guidelines was previ- Donabedian’s Structure-Process-Outcome framework to
ously extracted and represented in the HMS-LOE as a improve quality and provides a comprehensive conceptual
Clinical Evidence Logic Statement (CELS) of “If-Then” form framework for applying systems engineering.9,28,29 The
in a semistructured layer (level 2) based on a 4-layered frame- model consists of 3 major components: the “Work System,”
work (ie, levels 1-4) for knowledge representation.22In addi- the “Process of Care,” and “Team Outcomes.” The “Work
tion, the CELS were graded using a system developed by the System” component encompasses 5 interconnected elements:
Oxford Centre for Evidence-Based Medicine23 and person (eg, providers); tools and technology (eg, CDS); the
the United States Preventive Service Task Force system.24The external environment (eg, the physical environment); tasks
system has 5 levels: level 1 includes validating cohort studies (eg, task complexity), and organization (eg, organizational
with good reference standards and studies with findings support). We specifically focused on persons, tools, and
whose specificity or sensitivity is so high to rule in/out a diag- tasks.
nosis. Level 2 includes exploratory cohort studies with good Data from 26 patients was intentionally selected to design
reference standards. Level 3 includes studies that are either CDS1 and CDS2, individually and in combination. Data
nonconsecutive or have no consistently applied reference from an additional 14 patients were selected for CDS3. The

JAMIA Open, 2025, Vol. 8, No. 4 3
selection included a range of patient scenarios when the CDS defined baseline of 15% based on an increase in the propor-
should, and should not, trigger. For instance, patients chosen tion of patients triggering a CDS alert between 16.5% and
for CDS2 included those at varying risks for PE, those with 37.0% in previous studies,30,31with a 95% CI level and 80%
and without D-dimer testing results present, and those with power. These patients were subsequently used in the FHIR
and without exclusion criteria from the CDS, including calls in Epic INV.
patients under 18 years, pregnant patients, and those with The Institutional Research Data Warehouse, populated by
estimated glomerular filtration rate (eGFR)<30 or an allergy Epic, was used to extract patient-specific features including
to iodinated contrast (contraindications for CTPA). age, sex, race, and ethnicity. For CDS1 and CDS2, we also
extracted risk factors for PE, including previous history of PE
Implementing CDS in the EHR
or VTE. Other information extracted from the data ware-
After design, we implemented each CDS Hooks application house included D-dimer results, if present, pregnancy status,
in the Epic Innovation environment (Epic INV), a separate eGFR, and iodinated contrast allergy. For CDS3, we
nonproduction Epic environment deployed at the study insti- extracted previous breast cancer and cancer stages. Manual
tution. We first created a web application-type integration review was conducted to verify whether the CDS fired appro-
record or Field Device Integration for Substitutable Medical
priately based on EHR review and the variables extracted.
Applications and Reusable Technologies (SMART) on FHIR,
Clinical decision support inclusion and exclusion criteria, as
a standard for application development for use with EHRs.
well as logic to activate a CDS Hooks Card are shown in
We used the default SMART on FHIR authentication method
Table S2.
for a new application ID. The application was launched in
Epic Workspace from September 2024 to November 2024. Outcome measures and statistical analysis
All patients were recreated in the nonproduction (ie, Epic
As coprimary outcomes of CDS performance, we measured
INV) test environment in the same way it is done in Produc-
the false-positive rate (FPR) and accuracy for each CDS alert.
tion (ie, using a “Create Patient” option). We entered match-
False-positive rate is defined as the number of false-positive
ing demographic information (eg, age, race, sex) with
alerts out of all patients who should not have received an
patients queried from Production. All other patient history
alert (ie, 1—specificity). Accuracy is defined as the number of
gets added into corresponding sections in Epic (eg, surgeries
true positives and true negatives out of all patients analyzed.
into surgical history section, contrast allergies under the
We compared the false-positive alert rate and accuracy for
Allergy section). Laboratory results (eg, D-dimer, eGFR)
the CDS1 application compared to the more complex CDS2
were entered as External Results using a “Enter External
application. We also compared the 2 outcomes for CDS1
Results” option in Epic.
with CDS3 to assess scalability in CDS designed for another
A flowchart of each CDS application and its expected
care setting. Chi-square and Fisher’s Exact tests were used to
responses were created (Figure S1A-C). We noted whether
compare accuracy and FPRs. Finally, we also reported the
the CDS would fire appropriately with an appropriate CDS
precision and recall (ie, true positive rate) for all 3 CDS
Hooks Card, thereby minimizing false-positive alerts, using
applications.
the 40 patients used for the CDS design. For instance, if a
patient has current VTE, the CDS displays the link for VTE
educational materials. However, when an elevated D-dimer is Results
noted in the EHR, the CDS terminates and allows a provider
CDS development
to proceed without further action. In addition, we assessed
The CDS applications were developed using CDS Hooks.
feedback from 4 experts—2 ED physicians and 2 primary
CDS Hooks is an HL7 Standard that is a RESTful, JavaScript
care physicians, who were not involved in the original design
Object Notation-based web service specification that uses
of the CDS. This feedback was collected using a question-
FHIR to exchange patient data. We used CQL logic for the
naire with comments that can be provided as free text (Figure
trigger expression and logic files (Figure S3A-C). We used
S2) and was considered in iterative cycles of refinement of the
CDS applications before implementation. Most common cri- implicit value sets in the CQL expressions (https://build.fhir.
tiques were grouped into themes, according to CDS design org/valueset.html#implicit) that allow us to use the Snomed
principles (Table S1). These are described further below in or International Classification of Diseases, Tenth Revision
Sociotechnical Factors in CDS Design. concept hierarchies to include a large group of conditions. An
Epic “order-select” trigger triggers the workflow for CDS
Study population and data collection for CDS Hooks. Once triggered, the web service then requests the clin-
evaluation ical data it needs from the EHR. The CDS application is using
We retrospectively evaluated each of the 3 CDS applications. a “prefetch template” that instructs Epic to attach selected
The eligible study population included all adult patients from FHIR data elements along the initial call. This eliminates the
Epic’s Enterprise Data Warehouse (EDW) who had: (1) an need for the service to call back into the FHIR server before
order for CTPA for suspected PE at the ED or (2) an order obtaining clinical data, enhancing performance.
for a surveillance breast imaging examination (breast MRI or The CDS Hooks applications evaluate the content using an
mammography) in outpatient women with a previous history internal registry of CQL rules and provide the appropriate
of breast cancer or ductal carcinoma in situ (DCIS), during Card reply, when applicable. In the case of CDS1, the Card
the study period. The EDW was queried to identify all possi- provides a link to a separate URL. In the case of CDS3, it
ble patients and then we randomly selected 100 patients from gives recommendations in text. Finally, the Card provides a
this set; 50 from each of the 2 groups of patients. This sample link to a FHIR Questionnaire resource. The FHIR Question-
size was calculated to detect whether there was a greater than naire retrieves patient data and uses it to answer questions,
27% difference in the FPR of CDS from our previously when available. Otherwise, it asks for additional PE risk

4 J A M I A O p e n, 2025, Vol. 8, No. 4
Figure 1. CDS application workflow. Abbreviation: CDS, clinical decision support.
factors so providers can assess PE risk and receive a tailored cancer are excluded from this recommendation. This is
recommendation for CDS2. graded as level 3 evidence by the HMS-LOE.
This workflow is illustrated in Figure 1.
Data availability
CDS1: recommendations for providing educational
The graded pieces of evidence underlying this article are
materials on VTE prevention
available in the Harvard Medical School Library of Evidence
Clinical decision support artifacts (using CQL and FHIR) (https://libraryofevidence.med.harvard.edu/) upon request.
have been published in CDS Connect32based on a published Other CDS artifacts are available in CDS Connect.32,34,35
study.16 The recommendation aims to provide educational
materials to patients when seen by a physician at the ED for Sociotechnical factors in CDS design
suspected PE. When a physician orders a CTPA while the We utilized results from the questionnaire administered to 4
CDS is in place and when appropriate, the CDS Card pro- experts in assessing the CDS. Results of the questionnaire for
vides a link to educational materials in another URL (Figure physician’s attitude toward the CDS are shown in Figure S2,
S1A),33 which the physician can discuss with the patient or indicating a positive response to the CDS (means 6-7; scale 1-
for another provider to print out for the patient. This is 7) for positive impact on workload, ease of use, reducing
graded as level 4 evidence by the HMS-LOE. diagnostic errors, adequate training, and improving quality
of care. Similarly, responses to questions regarding physician
CDS2: recommendations for diagnostic evaluation
satisfaction with the CDS indicate that physicians were very
of suspected PE with CT pulmonary angiogram
satisfied with the CDS (means 6-7; scale 1-7). Textual com-
Clinical decision support artifacts are published in CDS Con- ments (Table S1) were incorporated into the iterative design
nect34 based on Wells’ criteria for PE management (Figure below.
S1B).17,18 The CDS aims to optimize the appropriate use of
CTPA for evaluating suspected acute PE. Specifically, it is Person factors: minimizing false-positive alerts for providers
triggered by an order for CTPA to evaluate patients with sus- and incorporating patient-specific factors
pected PE. This CDS should only be used in adult patients False alarms increase workload and may cause distraction
(18 years or older). In addition, this CDS has not been vali- and alert fatigue.36,37 This would then contribute to
dated for use in pregnant patients. Caution should be applied decreased performance.38We, therefore, tested the CDS with
in patients with severe allergy to iodinated contrast and data from various patients to ensure that false-positive alerts
patients with eGFR<30 for whom alternative imaging are minimized for providers. We accomplished this by ensur-
should be considered. This is graded as level 2 evidence by ing patient-specific data are accessed by the web service and
the HMS-LOE. exclusions are appropriately determined so they do not cause
false alerts. We were unable to operationalize 2 exclusions—
CDS3: recommendation for surveillance breast
pregnant patients where pregnancy was not noted in the
imaging in women with personal history of breast
problem list (for CDS2) and stage 4 breast cancer (for CDS3).
cancer Cancer staging was not accurately documented in the prob-
Clinical decision support artifacts are published in CDS Con- lem list, thus making it difficult to exclude. We therefore
nect35 to ensure patient preferences are included in the deci- chose to include all cancers, which may lead to false alerts for
sion process for choosing mammograms or breast MRIs in patients with previous stage 4 breast cancer (who should be
outpatients with a history of breast cancer, specifically in excluded from CDS3).
stages 1-3 and DCIS.19 It is intended for women with a per- For the most part, we captured all other patient-specific
sonal history of breast cancer for whom either a mammo- exclusions (eg, age<18 or minors), which decreased the
gram or breast MRI is ordered for surveillance, which act as number of false-positive alerts in the test data. Minimizing
the triggers. Textual information is provided to inform pro- false-positive alerts would reduce the overall number of alerts
viders to assess patient preferences given the limitations of and the frequency with which they activate, a key principle
either examination (Figure S1C). Women with stage 4 breast for alerts and alarms,8and a goal for providers.

JAMIA Open, 2025, Vol. 8, No. 4 5
Figure 2. Example of 2 CDS firing. Abbreviation: CDS, clinical decision support.
Tool factors: optimizing visual design and textual
information
Visual alerts were prioritized, and color was used to make the
alert content distinctive on the Epic best practice alert.8 The
CDS titles and goals were in a bright yellow header, distinct
from the white background of the typical EHR notes. Clinical
decision support titles and goals were at the top of the alerts,
along with textual information and links to URLs for addi-
tional information. These were on a yellow background, to
separate them from the main body of the alert (in lighter yel-
low) where providers could cancel or keep an ordered exami-
Figure 3. Displayed information for providers.
nation (Figure 2).
More importantly, we focused on the textual content of
data in the first display (Figure 3), thus minimizing the task
the information presented. It has been shown that definitive
complexity for providers and facilitating the process of pro-
rather than passive or probabilistic statements can increase
ceeding from the CDS alert.
the effectiveness of alerts. Thus, we used definitive verbs,
such as “Please assess PE risk...” or “Please provide educa-
Study cohort
tional materials....”39 This is preferred over a more passive
statement, such as “Risk assessment can be performed...” or Table 1includes the demographic information of the 2 sets of
50 patients each, randomly selected for CDS application
a probabilistic statement such as “Risk may be assessed in
evaluation.
some patients.” Second, the order of words reflects the
The mean age for patients seen in the ED with an order for
expected order of actions recommended. For instance,
“Please assess PE risk before ordering a CTPA.”8Finally, we CTPA for suspected PE is 62 years, similar to the mean age of
focused on the brevity and clarity of the recommendations 61 years for patients seen in the ambulatory clinic for breast
presented. imaging, and 72% of patients in both groups were White.
Finally, we assessed the design for firing combination alerts However, 20% of patients in the ED were Hispanic, whereas
(with more than 1 CDS firing), as in Figure 2. When CDS1 only 2% were Hispanic in the ambulatory cohort of patients
and CDS2 fired simultaneously, we prioritized CDS2 by plac- for breast imaging in women with previous history of breast
ing it at the top of CDS1. We wanted providers to focus more cancer.
on this alert than the one below, which although educational
False-positive rate and accuracy
does not impact diagnostic examination ordering.
Table 2 includes the FPR, accuracy, precision, and recall for
Task factors: simplifying tasks and reducing number of each CDS application. For patients with suspected PE, the
screens CDS for providing educational materials (CDS1) had a false-
We aimed to minimize providers’ efforts to review CDS positive alert rate and accuracy of 2% and 98%, respectively.
alerts. Alerts that require acknowledgement before the user This was not significantly different from the CTPA CDS
can proceed were kept to a minimum. Specifically, for CDS3, (CDS2), with 0.0% false-positive alert (P¼1.00) and 96%
a FHIR Questionnaire for patients with a prior history of accuracy (P¼1.00). It is also not significantly different from
breast cancer was originally designed on a separate URL. the breast imaging CDS (CDS3), which had an accuracy of
However, it was deemed more efficient to display the textual 100% (P¼1.00).

6                                                                                                                                                                            J  A   M   I A     O   p  e n, 2025, Vol. 8, No. 4
Table 1. Demographics of patients for CDS application evaluation. ED. The accuracy and FPR of the CDS that was used for
breast cancer surveillance in patients with prior history of
| Characteristics of patients with   |     |     | Number of   |     |     |     |     |     |
| ---------------------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- |
breast cancer also did not vary significantly from the CDS
| an order for CTPA |     |     | patients, n¼50 (%) |     |     |     |     |     |
| ----------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
used for ED patients. The CDS can trigger accurately after
| Age |     |     | Mean¼62   |              |                |           |                   |         |
| --- | --- | --- | --------- | ------------ | -------------- | --------- | ----------------- | ------- |
|     |     |     |           | preliminary  | testing  with  | patients  | and  experts  to  | ensure  |
(range 30, 97)
|     |     |     |     | that  CDS  | would  fire  | appropriately,  | thereby  minimizing  |     |
| --- | --- | --- | --- | ---------- | ------------ | --------------- | -------------------- | --- |
Sex
false-positive alerts that have led to alert fatigue, leading
| Male   |     |     | 23 (46%) |                                          |     |     |                      |     |
| ------ | --- | --- | -------- | ---------------------------------------- | --- | --- | -------------------- | --- |
|        |     |     |          | physicians to bypass future alerts.41,42 |     |     | Incorporating socio- |     |
| Female |     |     | 27 (54%) |                                          |     |     |                      |     |
technical factors in CDS design, specifically person factors,8
Race
| White |     |     | 36 (72%) | minimized false-positive alerts. |     |     |     |     |
| ----- | --- | --- | -------- | -------------------------------- | --- | --- | --- | --- |
Black 5 (10%) In addition to Person factors, Tool and Task factors are
| Other       |     |     | 6 (12%) |                                               |     |     |               |     |
| ----------- | --- | --- | ------- | --------------------------------------------- | --- | --- | ------------- | --- |
|             |     |     |         | important for improving provider experience.8 |     |     | In our case,  |     |
| Unavailable |     |     | 3 (6%)  |                                               |     |     |               |     |
the use of definitive rather than probabilistic statements in
Ethnicity
the textual content provided was an important factor that
| Hispanic |     |     | 10 (20%) |     |     |     |     |     |
| -------- | --- | --- | -------- | --- | --- | --- | --- | --- |
Non-Hispanic 40 (80%) has been shown to strengthen CDS effectiveness. Further-
Contrast allergy 3 (6%) more, in addition to textual information, the prioritization of
eGFR<30 4 (8%) the alerts is an effective strategy for improving CDS accept-
Prior DVT/PE 8 (16%) ance, as previously reported.43,44 In our case, we prioritized
Characteristics of patients with an order   Number of patients,   CDS2 by placing it at the top of CDS1 when both fired simul-
n550 (%)
for breast imaging
Age Mean¼61   taneously. This prioritization was designed to enable pro-
|     |     |     | (range 37, 82) | viders to focus more on an alert that will impact diagnostic  |     |     |     |     |
| --- | --- | --- | -------------- | ------------------------------------------------------------- | --- | --- | --- | --- |
Race examination ordering. Our experts agreed with optimizing
White 36 (72%) Tool factors by optimizing alert prioritization and textual
| Black |     |     | 3 (6%)  | content. |     |     |     |     |
| ----- | --- | --- | ------- | -------- | --- | --- | --- | --- |
| Other |     |     | 7 (14%) |          |     |     |     |     |
This study was limited by the number of CDSs assessed
| Unavailable |     |     | 4 (8%) |     |     |     |     |     |
| ----------- | --- | --- | ------ | --- | --- | --- | --- | --- |
and its retrospective design. Future studies will focus on pro-
Ethnicity
spective assessment of these CDS tools in a clinical setting
| Hispanic |     |     | 1 (2%) |     |     |     |     |     |
| -------- | --- | --- | ------ | --- | --- | --- | --- | --- |
Non-Hispanic 49 (98%) with a larger population for testing to assess the accuracy,
Breast imaging modality ordered FPRs, user acceptance, and response to recommendations.
| Mammography |     |     | 49 (98%) |     |     |     |     |     |
| ----------- | --- | --- | -------- | --- | --- | --- | --- | --- |
Second, artificial intelligence (AI) will likely change how CDS
| Breast MRI |     |     | 1 (2%) |     |     |     |     |     |
| ---------- | --- | --- | ------ | --- | --- | --- | --- | --- |
is utilized in health care in many ways. If AI actively triggers
Breast cancer stage
CDS, provider interaction and the use of HIT standards for
| DCIS |     |     | 12 (24%) |     |     |     |     |     |
| ---- | --- | --- | -------- | --- | --- | --- | --- | --- |
such use cases must be explored. Third, we did not assess
| Stage 1 |     |     | 20 (40%) |     |     |     |     |     |
| ------- | --- | --- | -------- | --- | --- | --- | --- | --- |
CDS scalability in institutions other than where the CDS was
| Stage 2 |     |     | 13 (26%) |     |     |     |     |     |
| ------- | --- | --- | -------- | --- | --- | --- | --- | --- |
Stage 3 4 (8%) designed and developed, potentially limiting generalizability.
Stage 4 0 (0%) The  CDS3  cohort  was  comprised  of  98%  non-Hispanic
| Unavailable |     |     | 1 (2%) |         |                  |                    |              |     |
| ----------- | --- | --- | ------ | ------- | ---------------- | ------------------ | ------------ | --- |
|             |     |     |        | women,  | also  impacting  | generalizability.  | These  will  | be  |
assessed in future dissemination studies.
Abbreviations: CDS, clinical decision support; CTPA, computed
tomography pulmonary angiogram; DCIS, ductal carcinoma in situ; eGFR,  In conclusion, it is possible to use HIT standards to repre-
estimated glomerular filtration rate; DVT, deep vein thrombosis; PE,
pulmonary embolism; MRI, magnetic resonance imaging. sent recommendations with various complexities and for dif-
|     |     |     |     | ferent  care  | settings  | embedded  within  | an  EHR.  | Using  |
| --- | --- | --- | --- | ------------- | --------- | ----------------- | --------- | ------ |
sociotechnical factors in CDS design is vital in improving pro-
vider experience. A multifaceted approach, with CDS based
Discussion
on high-quality graded evidence, implemented using AI to
Health Information Technology standards can be used to rep-
enhance workflow efficiency and HIT standards will poten-
resent 3 recommendations for CDS with various complex-
tially improve CDS dissemination and acceptance. This will
| ities—providing  | educational  | materials  | for  patients  with  |     |     |     |     |     |
| ---------------- | ------------ | ---------- | -------------------- | --- | --- | --- | --- | --- |
enhance CDS utilization, thus improving conformance to
suspected PE with previous VTE, recommending the use of  clinical guidelines and recommendations.
CTPA in patients with suspected PE, and using mammogra-
phy and breast MRI for breast cancer surveillance in outpa-
tients  with  prior  history  of  breast  cancer.  Substitutable  Acknowledgments
Medical Applications and Reusable Technologies on FHIR  The authors would also like to thank Ms Laura Peterson for
apps have been used with CDS Hooks to increase CDS uti- reviewing the manuscript.
| lization in a previous study.40 |     | The second CDS, in addition  |     |     |     |     |     |     |
| ------------------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
to using CDS Hooks for invoking CDS from the clinical
Author contributions
workflow and CQL for representing clinical logic, also uses
FHIR Questionnaire resources for representing interactive  Mark  Isabelle  (Conceptualization,  Data  curation,  Formal
content. This provides an additional layer of complexity to  analysis,  Investigation,  Methodology,  Writing—original
the representation, albeit still using HIT standards. The accu- draft, Writing—review & editing), Ivan K. Ip (Conceptualiza-
racy and false-positive alert rate between the CDS did not  tion, Formal analysis, Investigation, Methodology, Supervi-
vary significantly despite the added complexity. sion, Writing—original draft, Writing—review & editing),
We also assessed the scalability of standards for evaluating  Michael Bakhtin (Conceptualization, Data curation, Formal
CDS designed for an outpatient care setting compared to the  analysis, Investigation, Methodology, Software, Writing—

JAMIA Open, 2025, Vol. 8, No. 4                                                                                                                                                                            7
Table 2. False positive rate (FPR), accuracy, precision, and recall for each CDS application.
CDS True positives False positives False negatives True negatives FPR Accuracy Precision Recall
| CDS1 | 8   | 1   | 0   | 41  | 1/42 (2%) 49/50 (98%)  |         |         |
| ---- | --- | --- | --- | --- | ---------------------- | ------- | ------- |
|      |     |     |     |     |                        | 8/9     | 8/8     |
|      |     |     |     |     |                        | (89%)   | (100%)  |
| CDS2 | 18  | 0   | 2   | 30  | 0/30 (0%) 48/50 (96%)  |         |         |
|      |     |     |     |     |                        | 18/18   | 18/20   |
|      |     |     |     |     |                        | (100%)  | (90%)   |
| CDS3 | 50  | 0   | 0   | 0   | 0/0 (n/a) 50/50 (100%) |         |         |
|      |     |     |     |     |                        | 50/50   | 50/50   |
|      |     |     |     |     |                        | (100%)  | (100%)  |
Abbreviation: CDS, clinical decision support.
Precision¼true positive/(true positiveþfalse positive).
Recall¼true positive/(true positiveþfalse negative).
tomography for suspected pulmonary embolism. Am J Emerg
original draft, Writing—review & editing), Louise Schneider
(Conceptualization,  Data  curation,  Investigation,  Supervi- Med. 2018;36:540-544. https://doi.org/10.1016/j.ajem.2017.09.
| sion, Writing—review & editing), Ali S. Raja (Conceptualiza- |     |     |     | 004 |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
tion,  Formal  analysis,  Investigation,  Methodology,  06. Noseworthy JH, Madara J, Cosgrove D, et al. Physician burnout is
a public health crisis: a message to our fellow health care CEOs.
Supervision, Writing—review & editing), Sayon Dutta (Con-
Accessed June 1, 2017. http://healthaffairs.org/blog/2017/03/28/
ceptualization, Formal analysis, Investigation, Methodology,
physician-burnout-is-a-public-health-crisis-a-message-to-our-fel-
Supervision, Writing—review & editing), Adam Landman
low-health-care-ceos/
(Conceptualization, Formal analysis, Investigation, Method-
07. Collier R. Electronic health records contributing to physician
ology, Supervision, Writing—review & editing), and Ronilda  burnout.  CMAJ.  2017;189:E1405-E1406.  https://doi.org/10.
Lacson (Conceptualization, Data curation, Formal analysis,  1503/cmaj.109-5522
Funding acquisition, Investigation, Methodology, Software,  08. Phansalkar S, Edworthy J, Hellier E, et al. A review of human fac-
Supervision,  Validation,  Visualization,  Writing—original  tors principles for the design and implementation of medication
safety alerts in clinical information systems. J Am Med Inform
draft, Writing—review & editing)
|     |     |     |     | Assoc.  | 2010;17:493-501.  | https://doi.org/10.1136/jamia.2010.  |     |
| --- | --- | --- | --- | ------- | ----------------- | ------------------------------------ | --- |
005264
Supplementary material 09. Carayon P, Wetterneck TB, Rivera-Rodriguez AJ, et al. Human
factors systems approach to healthcare quality and patient safety.
Supplementary materialis available at JAMIA Open online.
|     |     |     |     | Appl  Ergon.  | 2014;45:14-25.  | https://doi.org/10.1016/j.apergo.  |     |
| --- | --- | --- | --- | ------------- | --------------- | ---------------------------------- | --- |
2013.04.023
10. Lacson R, Raja AS, Osterbur D, et al. Assessing strength of evi-
Funding
dence of appropriate use criteria for diagnostic imaging examina-
This work was supported by the Agency for Healthcare  tions. J Am Med Inform Assoc. 2016;23:649-653. https://doi.org/
Research and Quality grant number R18HS028616 (PI: R.  10.1093/jamia/ocv194
11. Khorasani R, Hentel K, Darer J, et al. Ten commandments for
L.).
effective clinical decision support for imaging: enabling evidence-
based practice to improve quality and reduce waste. AJR Am J
Conflicts of interest
Roentgenol. 2014;203:945-951. https://doi.org/10.2214/AJR.14.
| The authors have no competing interests to declare. |     |     |     | 13134 |     |     |     |
| --------------------------------------------------- | --- | --- | --- | ----- | --- | --- | --- |
12. Ransohoff DF, Pignone M, Sox HC. How to decide whether a clin-
ical practice guideline is trustworthy. JAMA. 2013;309:139-140.
| References |     |     |     | https://doi.org/10.1001/jama.2012.156703 |                   |                  |                |
| ---------- | --- | --- | --- | ---------------------------------------- | ----------------- | ---------------- | -------------- |
|            |     |     |     | 13. HMS-LOE.                             | Harvard  Medical  | School  Library  | of  Evidence.  |
01. Lobach D, Sanders GD, Bright TJ, et al. Enabling health care  Accessed March 10, 2019. https://libraryofevidence.med.harvard.
| decision-making through clinical decision support and knowledge  |     |     |     | edu/ |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | ---- | --- | --- | --- |
management.  Evid  Rep  Technol  Assess  (Full  Rep).  14. Lin Y, Staes CJ, Shields DE, Kandula V, Welch BM, Kawamoto K.
2012;203:1-784. Design, development, and initial evaluation of a terminology for
02. Ip IK, Schneider LI, Hanson R, et al. Adoption and meaningful use  clinical decision support and electronic clinical quality measure-
of computerized physician order entry with an integrated clinical  ment. AMIA Annu Symp Proc. 2015;2015:843-851.
decision support system for radiology: ten-year analysis in an  15. Benson  T,  Grieve  G.  Principles  of  Health  Interoperability:
urban teaching hospital. J Am Coll Radiol. 2012;9:129-136. SNOMED CT, HL7 and FHIR. 3rd ed. Springer-Verlag; 2016.
03. Ip IK, Schneider L, Seltzer S, et al. Impact of provider-led, technol- 16. Popoola VO, Lau BD, Shihab HM, et al. Patient preferences for
ogy-enabled radiology management program on imaging. Am J  receiving education on venous thromboembolism prevention—a
Med.  2013;126:687-692.https://doi.org/10.1016/j.amjmed.2012.  survey  of  stakeholder  organizations.  PLoS  One.  2016;11:
11.034 e0152084. https://doi.org/10.1371/journal.pone.0152084
04. Tajmir S, Raja AS, Ip IK, et al. Impact of clinical decision support  17. Wells PS, Anderson DR, Rodger M, et al. Derivation of a simple
on radiography for acute ankle injuries: a randomized trial. West J  clinical model to categorize patients probability of pulmonary
Emerg  Med.  2017;18:487-495.https://doi.org/10.5811/westjem.  embolism: increasing the models utility with the SimpliRED D-
| 2017.1.33053 |     |     |     | dimer. Thromb Haemost. 2000;83:416-420. |     |     |     |
| ------------ | --- | --- | --- | --------------------------------------- | --- | --- | --- |
05. Mills AM, Ip IK, Langlotz CP, Raja AS, Zafar HM, Khorasani R.  18. Wells PS, Ginsberg JS, Anderson DR, et al. Use of a clinical model
Clinical decision support increases diagnostic yield of computed  for  safe  management  of  patients  with  suspected  pulmonary

8 J A M I A O p e n, 2025, Vol. 8, No. 4
embolism. Ann Intern Med. 1998;129:997-1005. https://doi.org/ 32. Brigham and Women’s Hospital. Recommendation for providing
10.7326/0003-4819-129-12-199812150-00002 educational materials on venous thromboembolism prevention in
19. Wernli KJ, Ichikawa L, Kerlikowske K, et al. Surveillance breast CDS connect. Accessed October 11, 2024. https://cds.ahrq.gov/
MRI and mammography: comparison in women with a personal cdsconnect/artifact/recommendation-providing-educational-mate-
history of breast cancer. Radiology. 2019;292:311-318. https:// rials-venous-thromboembolism
doi.org/10.1148/radiol.2019182475 33. Brigham and Women’s Hospital. Deep vein thrombosis and pul-
20. Smith-Bindman R, Miglioretti DL, Johnson E, et al. Use of diag- monary embolism. Accessed October 11, 2024. https://cebi.bwh.
nostic imaging studies and associated radiation exposure for harvard.edu/signature-initiatives/pe/
patients enrolled in large integrated health care systems, 1996- 34. Brigham and Women’s Hospital. Recommendations for diagnostic
2010. JAMA. 2012;307:2400-2409. https://doi.org/10.1001/ evaluation of suspected pulmonary embolism in CDS connect.
jama.2012.5960 Accessed October 11, 2024. https://cds.ahrq.gov/cdsconnect/arti-
21. Office USGA. Medicare part B imaging services: rapid spending fact/recommendations-diagnostic-evaluation-suspected-pulmo-
growth and shift to physician offices indicate need for CMS to con- nary-embolism
sider additional management practices. Accessed September 15, 35. Brigham and Women’s Hospital. Recommendation for surveil-
2015. http://www.gao.gov/products/GAO-08-452 lance breast imaging in women with personal history of breast can-
22. Boxwala AA, Rocha BH, Maviglia S, et al. A multi-layered frame-
cer. Accessed October 11, 2024. https://cds.ahrq.gov/cdsconnect/
work for disseminating knowledge for computer-based decision
artifact/recommendation-surveillance-breast-imaging-women-per-
support. J Am Med Inform Assoc. 2011;18:i132-i139. https://doi.
sonal-history-breast-cancer
org/10.1136/amiajnl-2011-000334
36. Ash JS, Sittig DF, Campbell EM, Guappone KP, Dykstra RH.
23. Oxford Centre for Evidence Based Medicine.2015. Accessed July
Some unintended consequences of clinical decision support sys-
25, 2025. https://www.cebm.ox.ac.uk/resources/levels-of-evi-
tems. AMIA Annu Symp Proc. 2007; 2007:26-30.
dence/ocebm-levels-of-evidence
37. Phansalkar S, van der SH, Tucker AD, et al. Drug-drug interac-
24. Harris RP, Helfand M, Woolf SH, et al. Current methods of the
tions that should be non-interruptive in order to reduce alert
US preventive services task force: a review of the process. Am J
fatigue in electronic health records. J Am Med Inform Assoc.
PrevMed. 2001;20:21-35.
2013;20:489-493.
25. Lee J, Kirschner J, Pawa S, Wiener DE, Newman DH, Shah K.
38. Bliss JP, Dunn MC. Behavioural implications of alarm mistrust as
Computed tomography use in the adult emergency department of
a function of task workload. Ergonomics. 2000;43:1283-1300.
an academic urban hospital from 2001 to 2007. Ann Emerg Med.
https://doi.org/10.1080/001401300421743
2010;56:591-596. https://doi.org/10.1016/j.annemergmed.2010.
39. Heaps C, Henley T. Language matters: wording considerations in
05.027
hazard perception and warning perception. J Psychol.
26. Rosovsky RP, Isabelle M, Abbasi N, et al. CT pulmonary angio-
1999;133:341-351.
gram clinical pretest probability tool: impact on emergency depart-
40. Morgan KL, Kukhareva PV, Warner PB, et al. Using CDS Hooks
ment utilization. J Am Coll Radiol. 2024;21:1851-1861. https://
to increase SMART on FHIR app utilization: a cluster-randomized
doi.org/10.1016/j.jacr.2024.07.024
trial. J Am Med Inform Assoc. 2022;29:1461-1470. https://doi.
27. Sharma A, Isabelle M, Hunsaker A, et al. Impact of a clinical deci-
org/10.1093/jamia/ocac085
sion support system on CT pulmonary angiography yield and uti-
41. Yoshida E, Fei S, Bavuso K, Lagor C, Maviglia S. The value of mon-
lization in hospitalized patients. J Am Coll Radiol.
2025;22:449-460. https://doi.org/10.1016/j.jacr.2024.11.030 itoring clinical decision support interventions. Appl Clin Inform.
28. Holden RJ, Carayon P, Gurses AP, et al. SEIPS 2.0: a human fac- 2018;9:163-173. https://doi.org/10.1055/s-0038-1632397
tors framework for studying and improving the work of healthcare 42. Ip IK, Lacson R, Hentel K, et al. Journal Club: predictors of pro-
professionals and patients. Ergonomics. 2013;56:1669-1686. vider response to clinical decision support: lessons learned from
https://doi.org/10.1080/00140139.2013.838643 the medicare imaging demonstration. AJR Am J Roentgenol.
29. Carayon P, Schoofs Hundt A, Karsh BT, et al. Work system design 2017;208:351-357. https://doi.org/10.2214/AJR.16.16373
for patient safety: the SEIPS model. Qual Saf Health Care. 43. Phansalkar S, Zachariah M, Seidling HM, Mendes C, Volk L,
2006;15:i50-i58. https://doi.org/10.1136/qshc.2005.015842 Bates DW. Evaluation of medication alerts in electronic health
30. Yan AP, Parsons C, Caplan G, et al. Clinical decision support to records for compliance with human factors principles. J Am Med
enhance venous thromboembolism pharmacoprophylaxis pre- Inform Assoc. 2014;21:e332-e340. https://doi.org/10.1136/
scribing for pediatric inpatients with COVID-19. Pediatr Blood amiajnl-2013-002279
Cancer. 2024;71:e30843. https://doi.org/10.1002/pbc.30843 44. Seidling HM, Phansalkar S, Seger DL, et al. Factors influencing
31. Schiff GD, Volk LA, Volodarskaya M, et al. Screening for medica- alert acceptance: a novel approach for predicting the success of
tion errors using an outlier detection system. J Am Med Inform clinical decision support. J Am Med Inform Assoc.
Assoc. 2017;24:281-287. https://doi.org/10.1093/jamia/ocw171 2011;18:479-484. https://doi.org/10.1136/amiajnl-2010-000039
© The Author(s) 2025. Published by Oxford University Press on behalf of the American Medical Informatics Association.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits
unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.
JAMIA Open, 2025, 8, 1–8
https://doi.org/10.1093/jamiaopen/ooaf085
Research and Applications
