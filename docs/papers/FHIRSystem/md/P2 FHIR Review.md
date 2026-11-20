JMIR MEDICAL INFORMATICS Vorisek et al
Review
Fast Healthcare Interoperability Resources (FHIR) for
Interoperability in Health Research: Systematic Review
Carina Nina Vorisek1, MD, MSc; Moritz Lehne1, PhD; Sophie Anne Ines Klopfenstein1,2, MD; Paula Josephine
Mayer1; Alexander Bartschke1, MA; Thomas Haese1, BSc; Sylvia Thun1, MD, PhD
1Core Facility Digital Medicine and Interoperability, Berlin Institute of Health at Charité – Universitätsmedizin Berlin, Berlin, Germany
2Institute for Medical Informatics, Charité – Universitätsmedizin Berlin, Berlin, Germany
Corresponding Author:
Carina Nina Vorisek, MD, MSc
Core Facility Digital Medicine and Interoperability
Berlin Institute of Health at Charité – Universitätsmedizin Berlin
Anna-Louisa-Karsch-Str. 2
Berlin, 10178
Germany
Phone: 49 30 450 543049
Email: carina-nina.vorisek@bih-charite.de
Abstract
Background: The standard Fast Healthcare Interoperability Resources (FHIR) is widely used in health information technology.
However, its use as a standard for health research is still less prevalent. To use existing data sources more efficiently for health
research, data interoperability becomes increasingly important. FHIR provides solutions by offering resource domains such as
“Public Health & Research” and “Evidence-Based Medicine” while using already established web technologies. Therefore, FHIR
could help standardize data across different data sources and improve interoperability in health research.
Objective: The aim of our study was to provide a systematic review of existing literature and determine the current state of
FHIR implementations in health research and possible future directions.
Methods: We searched the PubMed/MEDLINE, Embase, Web of Science, IEEE Xplore, and Cochrane Library databases for
studies published from 2011 to 2022. Studies investigating the use of FHIR in health research were included. Articles published
before 2011, abstracts, reviews, editorials, and expert opinions were excluded. We followed the PRISMA (Preferred Reporting
Items for Systematic Reviews and Meta-Analyses) guidelines and registered this study with PROSPERO (CRD42021235393).
Data synthesis was done in tables and figures.
Results: We identified a total of 998 studies, of which 49 studies were eligible for inclusion. Of the 49 studies, most (73%,
n=36) covered the domain of clinical research, whereas the remaining studies focused on public health or epidemiology (6%,
n=3) or did not specify their research domain (20%, n=10). Studies used FHIR for data capture (29%, n=14), standardization of
data (41%, n=20), analysis (12%, n=6), recruitment (14%, n=7), and consent management (4%, n=2). Most (55%, 27/49) of the
studies had a generic approach, and 55% (12/22) of the studies focusing on specific medical specialties (infectious disease,
genomics, oncology, environmental health, imaging, and pulmonary hypertension) reported their solutions to be conferrable to
other use cases. Most (63%, 31/49) of the studies reported using additional data models or terminologies: Systematized
Nomenclature of Medicine Clinical Terms (29%, n=14), Logical Observation Identifiers Names and Codes (37%, n=18),
International Classification of Diseases 10th Revision (18%, n=9), Observational Medical Outcomes Partnership common data
model (12%, n=6), and others (43%, n=21). Only 4 (8%) studies used a FHIR resource from the domain “Public Health &
Research.” Limitations using FHIR included the possible change in the content of FHIR resources, safety, legal matters, and the
need for a FHIR server.
Conclusions: Our review found that FHIR can be implemented in health research, and the areas of application are broad and
generalizable in most use cases. The implementation of international terminologies was common, and other standards such as
the Observational Medical Outcomes Partnership common data model could be used as a complement to FHIR. Limitations such
as the change of FHIR content, lack of FHIR implementation, safety, and legal matters need to be addressed in future releases to
expand the use of FHIR and, therefore, interoperability in health research.
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 1
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
(JMIR Med Inform 2022;10(7):e35724) doi: 10.2196/35724
KEYWORDS
Fast Healthcare Interoperability Resources; FHIR; interoperability; health research; health care; health information technology;
research; clinical research; public health; epidemiology
different solutions can be implemented [5]. To cover information
Introduction
not included in the basic resources, FHIR provides a built-in
extension mechanism and can be adapted for specific use cases
Within the current COVID-19 pandemic, there was a broad
while ensuring interoperability. Additional rules and constraints
realization of the currently limited data collection processes and
within resources can be defined in profiles. Therefore, FHIR
how powerful the exchange of scientific data could be if
covers various domains of health care with its resources and
interoperability between health care and research was provided
can be used for different purposes and in various contexts and
[1]. Although there was a large amount of data in the health
workflows.
care ecosystem, there was lack of data that adheres to Findable,
Accessible, Interoperable, and Reusable [2] principles for users With regard to health research, there is still a lack of use of
to find, use, analyze, and share data on COVID-19. This applies international standards when exchanging data between health
specifically to academic health research where the lack of care and research institutions. However, there have been recent
interoperability between health care and research often inhibits regulative and legislative changes promoting standards and
the use of existing data sources for research. Commonly, the interoperability in health care [6-8]. In addition, there are
data collections of health research are stored in decentralized, initiatives of HL7 promoting FHIR’s use in health research,
autonomous data infrastructures which requires integration into such as the Vulcan HL7 FHIR Accelerator aiming to connect
common frameworks to enable centralized search and access. clinical research and health care, the MedMorph project aiming
to advance public health by using standards such as FHIR, and
However, processing national and cross-national scientific data
the collaboration of HL7 and OHDSI on a single common data
across different institutions and software systems requires
model [9-11]. As many research platforms and modern data
international standards and terminologies: the Observational
management systems, such as the Extensible Neuroimaging
Health Data Sciences and Informatics (OHDSI) Observational
Archive Toolkit open-source imaging informatics platform, use
Medical Outcomes Partnership (OMOP) common data model
extensible REST APIs [12,13], FHIR may be the new standard
(CDM) is used in observational research, whereas the Clinical
to fill the interoperability gap in health research with its REST
Data Interchange Standards Consortium (CDISC) Operational
architecture. Existing reviews on FHIR investigate the general
Data Standard (ODM) is used specifically for the exchange of
use of FHIR in digital health [14] or its use in electronic health
data within clinical trials [3]. CDISC is providing standards
records [15]. However, to the best of our knowledge, the use of
such as standardized raw data sets (Study Data Tabulation
FHIR in health research has not been systematically investigated.
Model; SDTM), also considered a CDM, as well as standardized
Therefore, the aim of our study was to provide a systematic
analysis data sets models. Further established standards are the
review of existing literature to determine the current state of
terminologies Systematized Nomenclature of Medicine Clinical
use cases, implementation, goals, and limitations of FHIR in
Terms (SNOMED CT) and Logical Observation Identifiers,
health research.
Names, and Codes (LOINC). SNOMED CT is the most
comprehensive clinical health care terminology worldwide
Methods
providing more than 350,000 concepts, whereas LOINC is a
standard for laboratory tests and clinical observations. One of
Protocol, Registration, and Ethical Considerations
the latest emerging standards for the exchange of health data is
the standard Fast Healthcare Interoperability Resources (FHIR). This systematic review was conducted in accordance with the
(PRISMA) Preferred Reporting Items for Systematic Reviews
FHIR is a standard used in health information technology
and Meta-Analyses guidelines [16]. The review was registered
introduced in 2011 by the Standard Developing Organization
with the International Prospective Register of Systematic
Health Level Seven International (HL7). FHIR is based on
Reviews (PROSPERO; CRD42021235393) [17]. As data
previous HL7 standards (HL7 versions 2 and 3 and Clinical
originated from published studies, ethical approval for this study
Document Architecture) and combines their advantages with
was not requested.
established modern web technologies such as a Representational
State Transfer (REST) architecture; application programming Inclusion and Exclusion Criteria
interface (API), XML, and JSON formats; and authorization We included studies investigating the use of FHIR in health
tools (Open Authorization). In FHIR, all exchangeable content research. We did not focus on particular patient populations,
is defined by distinct basic building blocks—referred to as interventions, control groups, or outcomes, except the use of
resources—which define the content and structure of information FHIR in health research. Details on inclusion and exclusion
and can refer to each other using reference mechanisms [4]. criteria are presented in Textbox 1.
The base FHIR specification serves as a foundation providing
basic resources, frameworks, APIs, and a platform in which
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 2
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
Textbox 1. Inclusion and exclusion criteria for paper review.
Inclusion criteria
• Studies focusing on the use of FHIR in health care research
• Original papers published in peer-reviewed journals in English
• Studies with publication dates no earlier than 2011
Exclusion criteria
• Studies focusing on the use of FHIR in electronic health records, mobile and web apps, decision support, and data protection or security
• General overviews on FHIR
• Comments, books, editorials, or reviews
• Language other than English
• Studies conducted before 2011
Data Extraction and Analysis
Information Sources and Search Strategy
Data synthesis was conducted in tables and figures. For
A comprehensive literature search was performed through the
categorical variables, simple and relative frequencies and
PubMed/MEDLINE, Embase, Web of Science, IEEE Xplore,
proportions were used. To identify the networks of coauthors,
and Cochrane Library databases. In addition, citation tracking
we also performed a network analysis that investigated, for all
and reference list checking were performed. The goal of the
authors of the included studies, whether they were coauthors in
search strategy was to retrieve all relevant studies related to our
a study. Results were visualized in a network graph. We did not
research question published between 2011 and 2022. Search
assess bias in studies due to the lack of quantitative tools
terms were therefore relatively broad to make sure that all
applicable to technical papers on standards. All analyses were
potentially relevant studies were identified. Search terms used
done with R statistical software (version 4.0.5; R Foundation
for the database searches were “FHIR” and “Fast Healthcare
for Statistical Computing) [19] and the tidyversepackages [20].
Interoperability Resources.” Information on the detailed search
All data and analyses scripts are provided in a GitHub repository
strategy for each database is provided as an appendix to this
[21].
review (Multimedia Appendix 1). The search was conducted
on February 26, 2022.
Results
Study Selection and Data Collection Process
Study Selection and Extraction
Study selection included 2 screening levels: (1) screening of
titles and abstracts of all studies identified in the literature search A total of 998 articles were identified through the database
and (2) full-text review of studies that had not been excluded searches (344 from MEDLINE, 359 from Embase, 201 from
in the first step. Review at the first stage of screening was Web of Science, 84 from IEEE Xplore, and 10 from Cochrane
performed independently by 2 authors (ML and SAIK) using Library). No additional records were identified through citation
the Rayyan web app [18]. Remaining disagreements were tracking and reference list checking. We excluded 477 duplicates
resolved by a third author (CNV). Further full-text screening and 422 articles that did not meet the inclusion criteria or met
at the second stage and data extraction were performed by 6 the exclusion criteria. Among the 99 full-text articles assessed
authors (CNV, ML, SAIK, PJM, AB, and TH), and for eligibility, an additional 50 studies were excluded. Finally,
disagreements of at least two authors at this stage were resolved 49 [1,12,22-68] articles met the inclusion criteria and were
by the last author (ST). included in the systematic review (Figure 1). Details on the
exclusion reasons for the full-text evaluation can be found in
Multimedia Appendix 2, and the exclusion reasons for the
abstract evaluation can be found in the GitHub repository [21].
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 3
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
Figure 1. PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) flow diagram for identifying articles eligible for inclusion.
FHIR: Fast Healthcare Interoperability Resources.
occurred more than 6 times within the included studies. Most
Characteristics of Included Studies
coauthorship networks were restricted to individual studies,
Publication dates ranged from 2016 to 2022 with the median in with occasional connections between networks (ie, authors
2020. Of the 49 included studies, 73% (n=36) were published having published studies with different groups of coauthors).
between 2020 and 2022. The increase of publications from 2020
Of the 49 studies, the majority were conducted in Germany
onward is visualized in Figure 2, showing the temporal trend
(47%, n=23) [12,26,28-31,34,35,40-42,45-47,52,53,56-58,60,62,
of all FHIR publications identified in the databases with the
63,69], the United States (27%, n=13) [22,25,36,44,48-50,61,
search terms “FHIR” OR “Fast Healthcare Interoperability
64-66,68,70], and Australia (6%, n=3) [1,43,67]. The remaining
Resources” and the number of publications included into the
studies were performed in Austria (2%, n=1) [32], Canada (2%,
analysis per year.
n=1) [24], France (2%, n=1) [51], Greece (2%, n=1) [59], Japan
The results of the network analysis of coauthorships are shown (2%, n=1) [27], Pakistan (2%, n=1) [38], Spain (2%, n=1) [55],
in Figure 3. Of a total of 256 authors, most (85%, n=217) Switzerland (2%, n=1) [39], Taiwan (2%, n=1) [23], and the
appeared only once in the included studies, and no author United Kingdom (2%, n=1) [37].
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 4
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
Figure 2. Number of publications per year (all: all FHIR publications identified in the databases with the search terms “FHIR” OR “Fast Healthcare
Interoperability Resources”; included: studies included in this review). FHIR: Fast Healthcare Interoperability Resources.
Figure 3. Network of coauthorships. Each point represents an author. Point size and color indicate the number of publications of this author (between
1 and 6). Lines indicate that authors have coauthored at least one paper together. Line thickness represents the number of coauthorships.
50,63,69]. The included studies used FHIR for the
Research Domain and Area of FHIR Application
standardization of data (41%, n=20) [23,26,30,34,41,45-48,
Of the 49 studies, most (73%, n=36) studies covered the research 51-53,57-60,63,66,67,70], data capture (29%, n=14)
domain of clinical research, of which 10 (20%) studies were [1,12,22,24,27,35-37,43,44,55,61,64,65], recruitment (14%,
clinical trials [22,29-31,36,39,43,56,65,66]; 3 (6%) studies n=7) [28,29,31,32,49,56,62], analysis (12%, n=6)
focused on solutions in public health and epidemiology [25,38,42,50,68,69], and consent management (4%, n=2; Table
[38,40,64], and the remaining studies did not specify their 1) [39,40]. Details on the included studies are presented in Table
research domain (20%, n=10; Figure 4) [24,32,41,42,45-47, 2.
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 5
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
Figure 4. Number of studies according to research domain.
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 6
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
Table 1. Numbers of studies according to area of FHIR application, medical specialty, and international standard.
Area Studies (N=49), n (%)
FHIRaapplication
Standardization of data 20 (41)
Data capture 14 (29)
Recruitment 7 (14)
Analysis 6 (12)
Consent management 2 (4)
Medical specialty
Generic approach 27 (55)
Infectious disease 8 (16)
Oncology 6 (12)
Genomics 4 (8)
Pulmonary hypertension 1 (2)
Neuroimaging research 1 (2)
Genomic cancer medicine 1 (2)
Environmental health 1 (2)
International standard
Other 21 (43)
None 18 (37)
LOINCb 14 (29)
SNOMED CTc 18 (37)
ICD-10d 9 (18)
OMOPe 6 (12)
aFHIR: Fast Healthcare Interoperability Resources.
bLOINC: Logical Observation Identifiers Names and Codes.
cSNOMED CT: Systematized Nomenclature of Medicine Clinical Terms.
dICD-10: International Classification of Diseases 10th Revision.
eOMOP: Observational Medical Outcomes Partnership.
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 7
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
Table 2. Characteristics of studies.
Source, year Country Item mapped to FHIRa Objective for FHIR use FHIR resources
Banach et al [56], Germany Medical and demographic data Estimation of the number of potentially eligible pa- —b
2021 from free-text eligibility criteria tients for planning multicenter trials based on free-
text criteria and using a consented data set based on
FHIR
Bauer et al [1], Australia Questionnaire Ontology-based standard questionnaire for linking Questionnaire
2020 genomic data with clinical outcomes
Bialke et al [40], Germany Modular consent templates Support improvement for consent definition and Consent
2018 consent documentation
Bild et al [28], Germany Informed consent template Cross-site interoperability layer for representing the Consent and Patient
2020 validity of data use policies derived from signed in-
formed consent templates and regulatory framework
Brandt et al [71], United States Phenotype definitions from the Repository of structured phenotype definitions for Patients, Encounter, Pro-
2021 Phenotype Knowledgebase automation of cohort identification. cedure, Medication or-
repository ders, Condition, and Ob-
servation
Cheng et al [44], United States EHRcData Seamless data exchange between the REDCapdre- Patient, Observation, Al-
2021 search electronic data capture and any EHR system lergyIntolerance,Medica-
with a FHIR APIe tionOrder, and Condition
Deppenwieset al Germany Oncology data Provide a transformation tool from oncology data Medication, Medication-
[57], 2021 XML files to FHIR for oncological data to enable Statement, and Procedure
clinical research
Eapen et al [24], Canada Electronic form components Management, editing, and rendering of electronic Questionnaire and Ques-
2019 forms in the form of an open-source framework tionnaireResponse
Fischer et al [35], Germany Common data set from a Ger- Feasibility of HL7fFHIR Bundle and XSLTgas a Patient, Encounter, and
2020 man pulmonary hypertension generic ETLhprocess to populate an OMOPiCDMj Observation
registry
Garza et al [61], United States Concomitant medications, de- Developing and implementing a systematic mapping Observation, Patient,
2020 mographics, eligibility, labs, approach for evaluating HL7 FHIR standard coverage Specimen, Encounter,
medical history, therapeutic in multicenter clinical trials. Diagnostic Report, and
area–specific, procedure, en- Condition
counters, vital signs, other, ad-
ministrative, questionnaires,
and study drug administration
González- Castro Spain Clinical patient data (from Collection and aggregation of survivorship data (use Patient, Condition, Obser-
et al [55], 2021 EHR) and patient-generated cases colon cancer and breast cancer) vation, MedicationState-
data ment, Encounter, and
Procedure
Gruendner et al Germany Clinical patient data Analysis within and across institutions —
[69], 2020
Gruendner et al Germany Metadata Developing a Metadata Schema based on FHIR to ResearchStudy, Question-
[42], 2021 gather metadata on clinical, epidemiological, and naire, and DocumentRef-
public health studies; elevate data FAIRnessk; and erence
widen analysis possibilities across health research
domains
Guérin et al [51], France Clinical and omics data in on- Improve and accelerate retrospective and prospective MolecularSequence and
2021 cology clinical and genomic data sharing in oncology Observation
Gulden et al [31], Germany Eligibility criteria of clinical Recruitment of patients for clinical trials using eligi- Condition and Patient
2018 trials bility criteria
Gulden et al [30], Germany Clinical trial data Multisite clinical trial registry ResearchStudy
2021
Hong et al [25], United States Ovarian cancer data Support of clinical statistics and analysis leveraging Patient, Observation,
2017 standardized data exchange and access services based Condition, and Procedure
on FHIR
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 8
XSL FO (page number not for citation purposes)
•
RenderX

| JMIR MEDICAL INFORMATICS |     |     |     | Vorisek et al |
| ------------------------ | --- | --- | --- | ------------- |
Item mapped to FHIRa
| Source, year | Country |     | Objective for FHIR use | FHIR resources |
| ------------ | ------- | --- | ---------------------- | -------------- |
Hund et al [53], Germany Process data Developing a framework to enable standardized, ActivityDefinition, Bina-
2021 shared processes using Business Process Model and ry, Bundle, CodeSystem,
|     |     |     | Notation and FHIR for arbitrary biomedical research | Endpoint,Group, Nam- |
| --- | --- | --- | --------------------------------------------------- | -------------------- |
ingSystem, Organization,
Practitioner, Practitioner-
Role, ResearchStudy,
StructureDefinition, Sub-
scription, and Task
Jiang et al [70], United States Clinical research data Development and assessment of a consensus-based Observation
| 2017 |     |     | approach for harmonizing the OHDSIlCDM with |     |
| ---- | --- | --- | ------------------------------------------- | --- |
HL7 FHIR
Kilintzis et al Greece Clinical information from in- Fusion of clinical information with chest sounds and Media
[59], 2022 ICUmCOVID-19 patients imaging of COVID-19 ICU patients
Klopfenstein et al Germany Metadata of clinical, epidemio- Developing a Metadata Schema based on FHIR to ResearchStudy, Question-
[41], 2021 logical and public health stud- gather metadata on clinical, epidemiological, and naire, and DocumentRef-
|     |     | ies | public health studies; elevate data FAIRness; and | erence |
| --- | --- | --- | ------------------------------------------------- | ------ |
widen analysis possibilities across health research
domains
Khalique and Pakistan EHR Analysis or mining of EHR data and contextual infor- —
| Khan [38], 2017 |     |     | mation to assess the population’s health |     |
| --------------- | --- | --- | ---------------------------------------- | --- |
Khvastova et al Germany Open-source research platform Feasibility study for the full integration of FHIR into Patient
| [12], 2020 |     | (XNATn) | XNAT |     |
| ---------- | --- | ------- | ---- | --- |
Lackerbauer et al Austria Informed consent or question- Automated verification of answers Questionnaire and Ques-
| [32], 2019 |     | naires |     | tionnaireResponse |
| ---------- | --- | ------ | --- | ----------------- |
Lambarki et al Germany Oncology data Use and apply a harmonized FHIR-based modular Condition, Observation,
[58], 2021 data set in a federated data platform for translational Procedure, Medication-
|     |     |     | cancer research to store data in a structured manner | Statement, Patient, Orga- |
| --- | --- | --- | ---------------------------------------------------- | ------------------------- |
|     |     |     | and enable data transfer                             | nization, Specimen,       |
ClinicalImpression, En-
counter, and Ser-
viceRequest
Lee et al [23], Taiwan IPSo FHIR-based global infectious disease surveillance MedicationStatement,
| 2020 |     |     | and case-tracking model | Medication, AllergyIntol- |
| ---- | --- | --- | ----------------------- | ------------------------- |
erance, Condition, Immu-
nization, Procedure, Orga-
nization, Observation,
CarePlan, and Location
Lenert et al [50], United States Clinical data Availability of data for research Patient, Encounter, Con-
| 2021 |     |     |     | dition, Procedure, Obser- |
| ---- | --- | --- | --- | ------------------------- |
vation, MedicationRe-
quest, and MedicationAd-
ministration
Leroux et al [67], Australia Data model Mapping CDISCpODMqto FHIR Patient, Observation,
| 2017 |     |     |     | EpisodeOfCare, En- |
| ---- | --- | --- | --- | ------------------ |
counter, QuestionnaireRe-
sponse, Questionnaire,
and CarePlan
Majeed et al [60], Germany General patient information, Developing a generic ETL framework to process Patient, Observation, and
2021 encounter, or visit related infor- patient data into FHIR and enable data integration in Encounter
|     |     | mation; individual data points; | a single central data warehouse as a prerequisite for |     |
| --- | --- | ------------------------------- | ----------------------------------------------------- | --- |
|     |     | observations; measurements;     | translational research                                |     |
and surveys
Metke-Jimenez et Australia REDCap forms Data export from REDCap into FHIR resources Encounter, Observation,
| al [43], 2019 |     |     |     | Condition, and Patient |
| ------------- | --- | --- | --- | ---------------------- |
Peng et al [52], Germany Genomic Variant Cell Format Coverage of Variant Cell Format data in OMOP MolecularSeqeunce, Pa-
2021 data CDM with and without using FHIR as intermediate tient, and Condition
layer
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 9
(page number not for citation purposes)
XSL FO
•
RenderX

| JMIR MEDICAL INFORMATICS |     |     |     | Vorisek et al |
| ------------------------ | --- | --- | --- | ------------- |
Item mapped to FHIRa
| Source, year | Country |     | Objective for FHIR use | FHIR resources |
| ------------ | ------- | --- | ---------------------- | -------------- |
Pfiffner et al United States ResearchKit data Patient-reported outcomes Contract, Questionnaire,
| [22], 2016 |     |     |     | QuestionnaireResponse, |
| ---------- | --- | --- | --- | ---------------------- |
Patient, and Observation
Reinecke et al Germany Patient ID lists Data-driven recruitment of patients for clinical trials, List
[29], 2020 storage of patient lists, and generation of notifications
Rinaldi et al [45], Germany Microbiology data Standardization of clinical data from patient care and DiagnosticReport, Obser-
2021 medical research in the field of infection control vation, Specimen, and
ServiceRequest
Rinaldi et al [47], Germany OpenEHR Template Mapping infection control related data across 3 dif- DiagnosticReport, Obser-
2021 ferent standards—OpenEHR, FHIR, and OMOP vation, Specimen, Ser-
|     |     |     | CDM—to maximize analysis capabilities | viceRequest, and En- |
| --- | --- | --- | ------------------------------------- | -------------------- |
counter
Sass et al [26], Germany COVID-19 data Standardized data model Patient, Consent, Obser-
| 2020 |     |     |     | vation, Condition, Proce- |
| ---- | --- | --- | --- | ------------------------- |
dure, Encounter, Medica-
tion, and MedicationState-
ment
Sass et al [46], Germany Medication chapter of the Ger- Representation of structured medication data Patient, Procedure, Medi-
| 2021 |     | man Procedure                     |     | cationStatement, and |
| ---- | --- | --------------------------------- | --- | -------------------- |
|      |     | Classification and Identification |     | Medication           |
of Medicinal Products–compli-
ant
medication terminology
Tanaka et al [27], Japan SS-MIX2r Mapping electronic medical record items between Patient, Encounter, Con-
| 2020 |     |     | SS-MIX2 and HL7 FHIR | dition, AllergyIntoler- |
| ---- | --- | --- | -------------------- | ----------------------- |
ance, Observation, Speci-
men, ServiceRequest,
MedicationRequest, and
MedicationDispense
Ulrich et al [34], Germany Metadata or CRFs Metadata repository Questionnaire
2016
Wagholikar et al United States Common data model demo- Clinical apps sharing via a platform —
| [36], 2017 |     | graphics, laboratory results, and |     |     |
| ---------- | --- | --------------------------------- | --- | --- |
diagnoses
Wang et al [48], United States FDAt’s Adverse Event Report- Potential use of FHIR for postmarket safety surveil- AdverseEvent
| 2021 |     |     | lance for drug products |     |
| ---- | --- | --- | ----------------------- | --- |
ing System data
Weber et al [39], Switzerland Electronic consent form Designing of a FHIR-based eConsent app for Android Contract
| 2020 |     |     | and evaluation of acceptance |     |
| ---- | --- | --- | ---------------------------- | --- |
Wettstein et al Germany Clinical data Using FHIR for automated and distributed feasibility Group, ResearchStudy,
[62], 2021 queries to find available cohort sizes across institu- and Task
tions
Wettstein et al Germany Medical routine data HL7 FHIR version R4 is used to define the necessary Group, ResearchStudy,
[63], 2021 communication messages as well as process input and Task
and output variables.
Wu et al [37], United King- EHR data and unstructured Semantic search system for obtaining clinical insights Patient and DocumentRe-
| 2018 | dom | documents | from unstructured clinical notes | ference |
| ---- | --- | --------- | -------------------------------- | ------- |
Xu et al [64], United States Data set of patients with “asth- Impact of airborne pollutant exposures on asthma —
| 2020 |     | ma-like” conditions | (research question) |     |
| ---- | --- | ------------------- | ------------------- | --- |
Zong et al [65], United States Colorectal cancer report Automatic population of eCRFs in colorectal clinical Questionnaire and Ques-
| 2020 |     |     | cancer trials | tionnaireResponse |
| ---- | --- | --- | ------------- | ----------------- |
Zong et al [66], United States Colorectal cancer data model Framework for capturing common data elements DiagnosticReport and
| 2021 |     |     | from CRFs and FHIR resources to | Observation |
| ---- | --- | --- | ------------------------------- | ----------- |
identify clinical information needs
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 10
(page number not for citation purposes)
XSL FO
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
Source, year Country Item mapped to FHIRa Objective for FHIR use FHIR resources
Zong et al [68], United States EHR Discovery of genotype-phenotype associations Condition, and Observa-
2020 tion
aFHIR: Fast Healthcare Interoperability Resources.
bNot available.
cEHR: electronic health record.
dREDCap: Research Electronic Data Capture.
eAPI: application programming interface.
fHL7: Health Level Seven International.
gXSLT: Extensible Stylesheet Language Transformations.
hETL: Extract-Transform-Load.
iOMOP: Observational Medical Outcomes Partnership.
jCDM: common data model.
kFAIR: Findable, Accessible, Interoperable, and Reusable.
lOHDSI: Observational Health Data Sciences and Informatics
mICU: intensive care unit.
nXNAT: Extensible Neuroimaging Archive Toolkit.
oIPS: International Patient Summary.
pCDISC: Clinical Data Interchange Standards Consortium.
qODM: Operational Data Model.
rSS-MIX2: Standardized Structured Medical Information Exchange2.
sCRF: Case Report Form.
tFDA: U.S. Food and Drug Administration.
version used was provided by 45% (n=22) of the studies
Study Objectives
[22,23,25,26,28,30,32,35,40,42,48,49,57,59,60,66,68,70], which
In terms of medical specialty, most (55%, 27/49) of the studies can be found in Multimedia Appendix 4.
[24,27-32,34,36-42,44,46,48,49,53,56,60-63,67,70] were using
Limitations of FHIR Use
a generic approach—implementable in any kind of specialty
(Table 2). Of the remaining studies, 16% (8/49) use cases With regard to the limitations of FHIR use, Bild et al [28],
focused on infectious disease [1,22,23,26,45,47,50,59], whereas Lackerbauer et al [32], and Metke-Jimenez et al [43] reported
12% (6/49) focused on oncology [25,55,57,58,65,66] and 8% the possible content changes of new versions of FHIR resources.
(4/49) on genomics [43,52,68,69]. Further medical specialties Generalizability was a concern in the studies of Khalique et al
were environmental health (2%, 1/49) [64], genomic cancer [38] and Zong et al [65]. The need for a FHIR server [69] and
medicine (2%, 1/49) [51], neuroimaging research (2%, 1/49) the requirement for a protocol for deidentification [1] were
[12], and pulmonary hypertension (2%, 1/49) [35]. Despite additional limitations. Reinecke et al [29] had not tested the
studies implementing FHIR in specific use cases, 55% (12/22) exchange of data between locations and therefore could not
of the studies [1,12,22,23,25,35,43,50,52,58,64,69] reported provide information in terms of use and results of their
generic solutions conferrable to other use cases. Details on study prototype. Wagholikar et al [36] implemented a limited subset
objectives with regards to FHIR use can be found in Table 2 of FHIR resources in their platform and therefore the filtering
and Multimedia Appendix 3. of FHIR resources using complex query formats was not
supported. In terms of electronic consents, safety and legal
International Standards
matters were major concerns [39]. Zong et al [68], investigating
Among the 49 studies, 37% (n=18) did not report on or use the discovery of genotype-phenotype associations, reported the
additional standards or terminologies [12,22-24,27,28,30-32, lack of information on differences in genetic data as well as
38,39,48,50,55,57,64,66,69]. SNOMED CT [1,25,26,35,37,43, extra mapping efforts since the data were from multiple sources.
45-47,51,55,56,65,70] and LOINC [25,26,35,37,42-45, In addition, there was a lack of resources preventing the
47,49,51,55,56,58,61,65,68,70] were reported to be used by demonstration of use in the study. Generalizability was also a
29% (n=14) and 37% (n=18) of the studies, respectively; 18% concern in this study in terms of exploring the FHIR framework
(n=9) of the studies used International Classification of Diseases within other variants and noncancer phenotypes in future work.
10th Revision [25,26,35,37,49,51,58,65,68] and 12% (n=6)
used OMOP CDM [26,29,35,47,52,60]; and 43% (n=21) of the Discussion
studies used additional standards which were categorized under
“Other” (Table 1) [26,34-37,40,42,43,45-47,49,51,56,58-60, Principal Findings
62,63,67,70]. The implemented FHIR resources by each study
This systematic review summarizes the current state of use cases
are listed in Table 2; 5 (10%) studies did not precisely list their
implementing FHIR in health research. As FHIR was developed
FHIR resources used [36,38,56,64,69]. Information on the FHIR
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 11
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
in 2011, we included studies from 2011 to 2022 and found that were also limitations as Leroux et al [67] mapped CDISC SDTM
half of studies were published between 2020 and 2022, and FHIR and found that CDISC SDTM’s use of controlled
displaying an increased use of FHIR in the past years. terminology is inhibiting semantic interoperability solutions;
Interestingly, the first publication of our included studies FHIR uses semantic standards accepted in health care that are
emerged in 2016, indicating a 5-year latency between the usually precoordinated (eg, SNOMED CT and LOINC), whereas
publication of the FHIR standard and the publication of studies CDISC SDTM uses only controlled terminology in
addressing its use in health research. Germany and the United postcoordination. Therefore, there would be the need for
States were the countries with the highest number of sponsors to translate terminologies used within systems. Leroux
publications, which might be due to recent regulatory et al [67] proposed the new FHIR resources “ClinicalStudyPlan”
measurements and initiatives: in the United States, the 21st and “ClinicalStudyData”—equivalent to ODM “Study” and
Century Cures Act requires the use of FHIR for health data; “ClinicalData” elements—which could overcome the semantic
and in Germany, the medical informatics initiative aiming to incompatibility. However, mappings with data transformation
close the gap between research and health care used FHIR in may lead to information loss and errors; therefore, developing
their already established use cases. Our network analysis showed ODM toward FHIR would be preferable, and the draft of ODM
that authorships were dispersed relatively equally across studies, version 2.0 already includes better support for FHIR [74,75].
not dominated by individual research groups or authors. In addition, HL7 and CDISC have jointly released a mapping
implementation guide to help transform FHIR content into
Most studies aimed to primarily standardize their data for health
CDISC Clinical Data Acquisition Standards Harmonization
research and reported using additional international standards
Implementation Guide or SDTM Implementation Guide data
and terminologies. Within studies using FHIR for data capture,
sets. [76,77].
the FHIR resource “Questionnaire” was often used. Further
areas of FHIR use were analysis, recruitment, and consent With regard to limitations using FHIR, there were certain
management. The literature shows that fast and efficient patient drawbacks reported by the included studies such as the possible
screening for clinical trial recruitment support systems is change in the content of different versions of FHIR resources,
important, and there is a current lack of standards and safety, legal matters, and the need for a FHIR server. Not all
interoperability of in these systems, as well as with regard to studies tested the use of FHIR in practice and, therefore, could
eligibility criteria [72]. not provide results on the actual FHIR implementation.
The majority of studies followed a more generic approach rather Limitations
than implementing FHIR for a specific use case. The studies
One limitation of our study is the lack of quality evaluation due
establishing use cases focused on infectious diseases,
to missing established tools for evaluating technical papers on
specifically COVID-19, as well as genomics, oncology, and
standardization in health care. For technical evaluations,
imaging—which are all specialties more advanced in terms of
structured information on additional standards, software, and
digitalization. Among these use cases, only a small number of
FHIR version was missing in several studies. Therefore, our
studies reported limited generalizability of their results.
analysis on additional used standards might be biased as half
Though provided by FHIR specifically for research, resources of the studies did not report on using other international
out of the domains “Public Health & Research” and standards or terminologies. In addition, there were studies that
“Evidence-Based Medicine” were used in only 4 studies. A did not list their FHIR resources clearly or at all. We aimed to
recently published study investigated the feasibility of the FHIR guarantee an optimal systematic review process targeting
resource “ResearchStudy” in a metadata registry for COVID-19 academic peer-reviewed literature that is available in English;
research and found that there was a need for the use of however, limitations remained as we may have missed relevant
extensions on more than 20% of the data items [41]. However, studies that were not published in the target language.
the resources “ResearchStudy” and “ResearchSubject” are Furthermore, we assumed that the published literature provides
currently under revision and will likely be tailored more to a surplus on successful FHIR initiatives because, in general,
researchers’needs when released with FHIR version R5 in 2022 unsuccessful initiatives tend to stay unpublished [78]. Thus, our
[73]. review may suffer from publication bias. In addition, this study
investigated studies with a clear focus on FHIR in health
Our analysis found that FHIR was used as a complement to
research. However, there might be research projects using FHIR
other standards. Studies reporting on terminologies mostly used
without FHIR being the central message or included in title and
SNOMED CT and LOINC, both terminologies supported by
abstract.
FHIR within its value sets. There were 6 studies that used FHIR
in addition to OMOP CDM, a standard widely used in Conclusions
observational research. Using OMOP CDM, a recommended To the best of our knowledge, this is the first systematic review
way of transforming and transferring data from existing investigating the use of FHIR in health research. It was shown
databases—Extract-Transform-Load tools are used for each that FHIR has been successfully implemented in clinical, public
source separately. To connect multiple heterogeneous databases, health, and epidemiological research at the stages of recruitment
FHIR can be used as an intermediate format for local data and consent management, data capture, and standardization as
extraction [35]. Reinecke et al [29] also extended the OMOP well as analysis of patient data. The implementation of
CDM with FHIR to exchange electronic health record data to international terminologies such as SNOMED CT and LOINC
connect the CDM to several health care systems. However, there is common and, together with the REST API, stands out in
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 12
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
comparison with other health research standards. Other standards with CDISC. Resources of the domain “Public Health &
such as OMOP CDM were used as a complement to FHIR in Research” and “Evidence-Based Medicine” were rarely used
some studies, and a future aim could be the development of an and could further elevate interoperability in health research,
infrastructure for the seamless integration and communication specifically after their modifications in FHIR version R5.
of health information across different standards. This approach However, this approach will need to address current limitations
is reinforced by the current development of collaborations of but could, if successfully implemented, elevate digitalized health
different Standards Developing Organizations such as OHDSI research.
and FHIR and the improved support of FHIR in combination
Acknowledgments
This work was done as part of the National Research Data Infrastructure for Personal Health Data Consortium [79]. We gratefully
acknowledge the financial support of the Deutsche Forschungsgemeinschaft (German Research Foundation; NFDI 13/1).
Conflicts of Interest
ST is the vice chair of Health Level Seven Deutschland. The remaining authors declare no other conflicts of interests.
Multimedia Appendix 1
Search strategy for each database.
[DOCX File , 32 KB-Multimedia Appendix 1]
Multimedia Appendix 2
Reasons for the exclusion of full-text evaluation.
[DOCX File , 61 KB-Multimedia Appendix 2]
Multimedia Appendix 3
Word cloud showing the keywords of the main FHIR use objectives of the studies. FHIR: Fast Healthcare Interoperability
Resources.
[PNG File , 31 KB-Multimedia Appendix 3]
Multimedia Appendix 4
Additional information on the included studies.
[DOCX File , 43 KB-Multimedia Appendix 4]
References
1. Bauer DC, Metke-Jimenez A, Maurer-Stroh S, Tiruvayipati S, Wilson LOW, Jain Y, et al. Interoperable medical data: The
missing link for understanding COVID-19. Transbound Emerg Dis 2021 Jul;68(4):1753-1760 [FREE Full text] [doi:
10.1111/tbed.13892] [Medline: 33095970]
2. Wilkinson MD, Dumontier M, Aalbersberg IJ, Appleton G, Axton M, Baak A, et al. The FAIR Guiding Principles for
scientific data management and stewardship. Sci Data 2016 Mar 15;3:160018 [FREE Full text] [doi: 10.1038/sdata.2016.18]
[Medline: 26978244]
3. ODM-XML. Clinical Data Interchange Standards Consortium. URL: https://www.cdisc.org/standards/data-exchange/odm
[accessed 2021-06-17]
4. Resourcelist - FHIR v4.3.0. Health Level Seven International. URL: https://www.hl7.org/fhir/resourcelist.html[accessed
2021-12-20]
5. Index - FHIR v4.3.0. Health Level Seven International. URL: https://hl7.org/FHIR/index.html[accessed 2021-09-03]
6. Neues Bündnis für mehr Interoperabilität im Gesundheitswesen. Ärzte Zeitung. 2020 Aug 26. URL: https://www.aerztezei
tung.de/Wirtschaft/Neues-Buendnis-fuer-mehr-Interoperabilitaet-im-Gesundheitswesen-412313.html[accessed 2021-08-30]
7. Policies and technology for interoperability and burden reduction. Centers for Medicare & Medicaid Services. URL: https:/
/www.cms.gov/Regulations-and-Guidance/Guidance/Interoperability/index[accessed 2021-08-30]
8. Craven J. FDA drafts data standards guidance for RWD. Regulatory Focus. 2021 Oct 22. URL: https://www.raps.org/news-
and-articles/news-articles/2021/10/fda-drafts-data-standards-guidance-for-rwd[accessed 2022-04-22]
9. Vulcan. Health Level Seven International. URL: https://www.hl7.org/vulcan/[accessed 2022-04-22]
10. MedMorph Research Data Exchange Content IG. Health Level Seven International. URL: http://build.fhir.org/ig/HL7/fhir
-medmorph-research-dex-ig/index.html[accessed 2022-04-22]
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 13
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
11. HL7 International and OHDSI announce collaboration to provide single common data model for sharing information in
clinical care and observational research. Observational Health Data Science and Informatics. URL: https://www.ohdsi.org/
ohdsi-hl7-collaboration/[accessed 2022-04-22]
12. Khvastova M, Witt M, Essenwanger A, Sass J, Thun S, Krefting D. Towards interoperability in clinical research - enabling
FHIR on the open-source research platform XNAT. J Med Syst 2020 Jul 09;44(8):137 [FREE Full text] [doi:
10.1007/s10916-020-01600-y] [Medline: 32642856]
13. Marcus DS, Olsen TR, Ramaratnam M, Buckner RL. The Extensible Neuroimaging Archive Toolkit: an informatics platform
for managing, exploring, and sharing neuroimaging data. Neuroinformatics 2007;5(1):11-34. [doi: 10.1385/ni:5:1:11]
[Medline: 17426351]
14. Lehne M, Luijten S, Vom Felde Genannt Imbusch P, Thun S. The use of FHIR in digital health - a review of the scientific
literature. Stud Health Technol Inform 2019 Sep 03;267:52-58. [doi: 10.3233/SHTI190805] [Medline: 31483254]
15. Ayaz M, Pasha MF, Alzahrani MY, Budiarto R, Stiawan D. Correction: The Fast Health Interoperability Resources (FHIR)
standard: systematic literature review of implementations, applications, challenges and opportunities. JMIR Med Inform
2021 Aug 17;9(8):e32869 [FREE Full text] [doi: 10.2196/32869] [Medline: 34403353]
16. Moher D, Liberati A, Tetzlaff J, Altman DG, PRISMA Group. Preferred reporting items for systematic reviews and
meta-analyses: the PRISMA statement. PLoS Med 2009 Jul 21;6(7):e1000097 [FREE Full text] [doi:
10.1371/journal.pmed.1000097] [Medline: 19621072]
17. Vorisek C, Klopfenstein S, Lehne M, Haese T, Bartschke A, Thun S. Use of Fast Healthcare Interoperability Resources
(FHIR) in health care research data – a systematic review. National Institute for Health Research. 2021 Mar 13. URL:
https://www.crd.york.ac.uk/prospero/display_record.php?RecordID=235393[accessed 2021-03-15]
18. Ouzzani M, Hammady H, Fedorowicz Z, Elmagarmid A. Rayyan-a web and mobile app for systematic reviews. Syst Rev
2016 Dec 05;5(1):210 [FREE Full text] [doi: 10.1186/s13643-016-0384-4] [Medline: 27919275]
19. The R Project for Statistical Computing. R Foundation for Statistical Computing. URL: https://www.r-project.org./[accessed
2021-06-17]
20. Wickham H, Averick M, Bryan J, Chang W, McGowan L, François R, et al. Welcome to the Tidyverse. JOSS 2019
Nov;4(43):1686. [doi: 10.21105/joss.01686]
21. FHIR-Research-Review. GitHub. URL: https://github.com/BIH-CEI/FHIR-Research-Review[accessed 2021-12-20]
22. Pfiffner PB, Pinyol I, Natter MD, Mandl KD. C3-PRO: Connecting ResearchKit to the Health System Using i2b2 and
FHIR. PLoS One 2016;11(3):e0152722 [FREE Full text] [doi: 10.1371/journal.pone.0152722] [Medline: 27031856]
23. Lee H, Kung H, Lee Y, Chao JC, Udayasankaran JG, Fan H, et al. Global infectious disease surveillance and case tracking
system for COVID-19: development study. JMIR Med Inform 2020 Dec 22;8(12):e20567 [FREE Full text] [doi:
10.2196/20567] [Medline: 33320826]
24. Eapen BR, Costa A, Archer N, Sartipi K. FHIRForm: an open-source framework for the management of electronic forms
in healthcare. Stud Health Technol Inform 2019;257:80-85. [doi: 10.3233/978-1-61499-951-5-80] [Medline: 30741177]
25. Hong N, Prodduturi N, Wang C, Jiang G. Shiny FHIR: an integrated framework leveraging Shiny R and HL7 FHIR to
empower standards-based clinical data applications. Stud Health Technol Inform 2017;245:868-872 [FREE Full text] [doi:
10.3233/978-1-61499-830-3-868] [Medline: 29295223]
26. Sass J, Bartschke A, Lehne M, Essenwanger A, Rinaldi E, Rudolph S, et al. The German Corona Consensus Dataset
(GECCO): a standardized dataset for COVID-19 research in university medicine and beyond. BMC Med Inform Decis
Mak 2020 Dec 21;20(1):341 [FREE Full text] [doi: 10.1186/s12911-020-01374-w] [Medline: 33349259]
27. Tanaka K, Yamamoto R. Implementation of a secured cross-institutional data collection infrastructure by applying HL7
FHIR on an existing distributed EMR storages. Stud Health Technol Inform 2020 Jun 26;272:155-158. [doi:
10.3233/SHTI200517] [Medline: 32604624]
28. Bild R, Bialke M, Buckow K, Ganslandt T, Ihrig K, Jahns R, et al. Towards a comprehensive and interoperable representation
of consent-based data usage permissions in the German medical informatics initiative. BMC Med Inform Decis Mak 2020
Jun 05;20(1):103 [FREE Full text] [doi: 10.1186/s12911-020-01138-6] [Medline: 32503529]
29. Reinecke I, Gulden C, Kümmel M, Nassirian A, Blasini R, Sedlmayr M. Design for a modular clinical trial recruitment
support system based on FHIR and OMOP. Stud Health Technol Inform 2020 Jun 16;270:158-162. [doi:
10.3233/SHTI200142] [Medline: 32570366]
30. Gulden C, Blasini R, Nassirian A, Stein A, Altun FB, Kirchner M, et al. Prototypical clinical trial registry based on Fast
Healthcare Interoperability Resources (FHIR): design and implementation study. JMIR Med Inform 2021 Jan 12;9(1):e20470
[FREE Full text] [doi: 10.2196/20470] [Medline: 33433393]
31. Gulden C, Mate S, Prokosch HU, Kraus S. Investigating the capabilities of FHIR search for clinical trial phenotyping. Stud
Health Technol Inform 2018;253:3-7. [doi: 10.3233/978-1-61499-896-9-3] [Medline: 30147028]
32. Lackerbauer AM, Krauss O, Helm E. Automated verification of structured questionnaires using HL7. Stud Health Technol
Inform 2019;258:11-15. [doi: 10.3233/978-1-61499-959-1-11] [Medline: 30942704]
33. Jenkins KJ, Gauvreau K, Newburger JW, Spray TL, Moller JH, Iezzoni LI. Consensus-based method for risk adjustment
for surgery for congenital heart disease. J Thorac Cardiovasc Surg 2002 Jan;123(1):110-118. [doi: 10.1067/mtc.2002.119064]
[Medline: 11782764]
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 14
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
34. Ulrich H, Kock AK, Duhm-Harbeck P, Habermann JK, Ingenerf J. Metadata repository for improved data sharing and reuse
based on HL7 FHIR. Stud Health Technol Inform 2016;228:162-166. [doi: 10.3233/978-1-61499-678-1-162] [Medline:
27577363]
35. Fischer P, Stöhr MR, Gall H, Michel-Backofen A, Majeed RW. Data integration into OMOP CDM for heterogeneous
clinical data collections via HL7 FHIR bundles and XSLT. Stud Health Technol Inform 2020 Jun 16;270:138-142. [doi:
10.3233/SHTI200138] [Medline: 32570362]
36. Wagholikar KB, Jain R, Oliveira E, Mandel J, Klann J, Colas R, et al. Evolving research data sharing networks to clinical
app sharing networks. AMIA Jt Summits Transl Sci Proc 2017;2017:302-307 [FREE Full text] [Medline: 28815145]
37. Wu H, Toti G, Morley KI, Ibrahim ZM, Folarin A, Jackson R, et al. SemEHR: a general-purpose semantic search system
to surface semantic data from clinical notes for tailored care, trial recruitment, and clinical research. J Am Med Inform
Assoc 2018 May 01;25(5):530-537 [FREE Full text] [doi: 10.1093/jamia/ocx160] [Medline: 29361077]
38. Khalique F, Khan SA. An FHIR-based framework for consolidation of augmented EHR from hospitals for public health
analysis. 2017 Presented at: 2017 IEEE 11th International Conference on Application of Information and Communication
Technologies (AICT); September 20-22, 2017; Moscow, Russia p. 1-4. [doi: 10.1109/icaict.2017.8687289]
39. Weber M, Griessbach A, Grossmann R, Blaser J. A FHIr-based eConsent app for the digital hospital. Stud Health Technol
Inform 2020 Jun 16;270:3-7. [doi: 10.3233/SHTI200111] [Medline: 32570335]
40. Bialke M, Bahls T, Geidel L, Rau H, Blumentritt A, Pasewald S, et al. MAGIC: once upon a time in consent management-a
FHIR tale. J Transl Med 2018 Sep 14;16(1):256 [FREE Full text] [doi: 10.1186/s12967-018-1631-3] [Medline: 30217236]
41. Klopfenstein SAI, Vorisek CN, Shutsko A, Lehne M, Sass J, Löbe M, et al. Fast Healthcare Interoperability Resources
(FHIR) in a FAIR metadata registry for COVID-19 research. Stud Health Technol Inform 2021 Nov 18;287:73-77. [doi:
10.3233/SHTI210817] [Medline: 34795084]
42. Gruendner J, Gulden C, Kampf M, Mate S, Prokosch H, Zierk J. A framework for criteria-based selection and processing
of Fast Healthcare Interoperability Resources (FHIR) data for statistical analysis: design and implementation study. JMIR
Med Inform 2021 Apr 01;9(4):e25645 [FREE Full text] [doi: 10.2196/25645] [Medline: 33792554]
43. Metke-Jimenez A, Hansen D. FHIRCap: Transforming REDCap forms into FHIR resources. AMIA Jt Summits Transl Sci
Proc 2019;2019:54-63 [FREE Full text] [Medline: 31258956]
44. Cheng AC, Duda SN, Taylor R, Delacqua F, Lewis AA, Bosler T, et al. REDCap on FHIR: clinical data interoperability
services. J Biomed Inform 2021 Sep;121:103871 [FREE Full text] [doi: 10.1016/j.jbi.2021.103871] [Medline: 34298155]
45. Rinaldi E, Saas J, Thun S. Use of LOINC and SNOMED CT with FHIR for microbiology data. Stud Health Technol Inform
2021 May 24;278:156-162. [doi: 10.3233/SHTI210064] [Medline: 34042889]
46. Sass J, Zabka S, Essenwanger A, Schepers J, Boeker M, Thun S. Fast Healthcare Interoperability Resources (FHIR®)
representation of medication data derived from German Procedure Classification Codes (OPS) using Identification of
Medicinal Products (IDMP) compliant terminology. Stud Health Technol Inform 2021 May 24;278:231-236. [doi:
10.3233/SHTI210074] [Medline: 34042899]
47. Rinaldi E, Thun S. From OpenEHR to FHIR and OMOP data model for microbiology findings. Stud Health Technol Inform
2021 May 27;281:402-406. [doi: 10.3233/SHTI210189] [Medline: 34042774]
48. Wang X, Lehmann H, Botsis T. Can FHIR support standardization in post-market safety surveillance? Stud Health Technol
Inform 2021 May 27;281:33-37. [doi: 10.3233/SHTI210115] [Medline: 34042700]
49. Brandt PS, Pacheco JA, Rasmussen LV. Development of a repository of computable phenotype definitions using the clinical
quality language. JAMIA Open 2021 Oct;4(4):ooab094 [FREE Full text] [doi: 10.1093/jamiaopen/ooab094] [Medline:
34926996]
50. Lenert LA, Ilatovskiy AV, Agnew J, Rudisill P, Jacobs J, Weatherston D, et al. Automated production of research data
marts from a canonical fast healthcare interoperability resource data repository: applications to COVID-19 research. J Am
Med Inform Assoc 2021 Jul 30;28(8):1605-1611 [FREE Full text] [doi: 10.1093/jamia/ocab108] [Medline: 33993254]
51. Guérin J, Laizet Y, Le Texier V, Chanas L, Rance B, Koeppel F, et al. OSIRIS: a minimum data set for data sharing and
interoperability in oncology. JCO Clin Cancer Inform 2021 Mar;5:256-265 [FREE Full text] [doi: 10.1200/CCI.20.00094]
[Medline: 33720747]
52. Peng Y, Nassirian A, Ahmadi N, Sedlmayr M, Bathelt F. Towards the representation of genomic data in HL7 FHIR and
OMOP CDM. Stud Health Technol Inform 2021 Sep 21;283:86-94. [doi: 10.3233/SHTI210545] [Medline: 34545823]
53. Hund H, Wettstein R, Heidt CM, Fegeler C. Executing distributed healthcare and research processes - the HiGHmed data
sharing framework. Stud Health Technol Inform 2021 May 24;278:126-133. [doi: 10.3233/SHTI210060] [Medline:
34042885]
54. Greiner MV, Beal SJ, Dexheimer J, Krummen K. Evaluating IDENTITY, an automated data sharing platform to improve
health outcomes for youth in protective custody. Pediatr 2020 Jul 01;146(1_MeetingAbstract):507-508 [FREE Full text]
[doi: 10.1542/peds.146.1MA6.507]
55. González-Castro L, Cal-González VM, Del Fiol G, López-Nores M. CASIDE: A data model for interoperable cancer
survivorship information based on FHIR. J Biomed Inform 2021 Dec;124:103953 [FREE Full text] [doi:
10.1016/j.jbi.2021.103953] [Medline: 34781009]
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 15
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
56. Banach A, Ulrich H, Kroll B, Kiel A, Ingenerf J, Kock-Schoppenhauer AK. APERITIF - Automatic Patient Recruiting for
Clinical Trials Based on HL7 FHIR. Stud Health Technol Inform 2021 May 27;281:58-62. [doi: 10.3233/SHTI210120]
[Medline: 34042705]
57. Deppenwiese N, Delpy P, Lambarki M, Lablans M. ADT2FHIR - a tool for converting ADT/GEKID oncology data to HL7
FHIR resources. Stud Health Technol Inform 2021 Sep 21;283:104-110. [doi: 10.3233/SHTI210547] [Medline: 34545825]
58. Lambarki M, Kern J, Croft D, Engels C, Deppenwiese N, Kerscher A, et al. Oncology on FHIR: A Data Model for Distributed
Cancer Research. Stud Health Technol Inform 2021 May 24;278:203-210. [doi: 10.3233/SHTI210070] [Medline: 34042895]
59. Kilintzis V, Beredimas N, Kaimakamis E, Stefanopoulos L, Chatzis E, Jahaj E, et al. CoCross: An ICT Platform Enabling
Monitoring Recording and Fusion of Clinical Information Chest Sounds and Imaging of COVID-19 ICU Patients. Healthcare
(Basel) 2022 Jan 30;10(2):276 [FREE Full text] [doi: 10.3390/healthcare10020276] [Medline: 35206889]
60. Majeed RW, Stöhr MR, Günther A. HIStream-Import: A Generic ETL Framework for Processing Arbitrary Patient Data
Collections or Hospital Information Systems into HL7 FHIR Bundles. Stud Health Technol Inform 2021 May 24;278:75-79.
[doi: 10.3233/SHTI210053] [Medline: 34042878]
61. Garza MY, Rutherford M, Myneni S, Fenton S, Walden A, Topaloglu U, et al. Evaluating the coverage of the HL7 FHIR
standard to support eSource data exchange implementations for use in multi-site clinical research studies. AMIA Annu
Symp Proc 2020;2020:472-481 [FREE Full text] [Medline: 33936420]
62. Wettstein R, Hund H, Kobylinski I, Fegeler C, Heinze O. Feasibility Queries in Distributed Architectures - Concept and
Implementation in HiGHmed. Stud Health Technol Inform 2021 May 24;278:134-141. [doi: 10.3233/SHTI210061] [Medline:
34042886]
63. Wettstein R, Hund H, Fegeler C, Heinze O. Data Sharing in Distributed Architectures - Concept and Implementation in
HiGHmed. Stud Health Technol Inform 2021 Sep 21;283:111-118. [doi: 10.3233/SHTI210548] [Medline: 34545826]
64. Xu H, Cox S, Stillwell L, Pfaff E, Champion J, Ahalt SC, et al. FHIR PIT: an open software application for spatiotemporal
integration of clinical data and environmental exposures data. BMC Med Inform Decis Mak 2020 Mar 11;20(1):53 [FREE
Full text] [doi: 10.1186/s12911-020-1056-9] [Medline: 32160884]
65. Zong N, Wen A, Stone DJ, Sharma DK, Wang C, Yu Y, et al. Developing an FHIR-Based Computational Pipeline for
Automatic Population of Case Report Forms for Colorectal Cancer Clinical Trials Using Electronic Health Records. JCO
Clin Cancer Inform 2020 Mar;4:201-209 [FREE Full text] [doi: 10.1200/CCI.19.00116] [Medline: 32134686]
66. Zong N, Stone DJ, Sharma DK, Wen A, Wang C, Yu Y, et al. Modeling cancer clinical trials using HL7 FHIR to support
downstream applications: a case study with colorectal cancer data. Int J Med Inform 2021 Jan;145:104308 [FREE Full
text] [doi: 10.1016/j.ijmedinf.2020.104308] [Medline: 33160272]
67. Leroux H, Metke-Jimenez A, Lawley MJ. Towards achieving semantic interoperability of clinical study data with FHIR.
J Biomed Semantics 2017 Sep 19;8(1):41 [FREE Full text] [doi: 10.1186/s13326-017-0148-7] [Medline: 28927443]
68. Zong N, Sharma DK, Yu Y, Egan JB, Davila JI, Wang C, et al. Developing a FHIR-based framework for phenome wide
association studies: a case study with a pan-cancer cohort. AMIA Jt Summits Transl Sci Proc 2020;2020:750-759 [FREE
Full text] [Medline: 32477698]
69. Gruendner J, Wolf N, Tögel L, Haller F, Prokosch H, Christoph J. Integrating genomics and clinical data for statistical
analysis by using GEnome MINIng (GEMINI) and Fast Healthcare Interoperability Resources (FHIR): system design and
implementation. J Med Internet Res 2020 Oct 07;22(10):e19879 [FREE Full text] [doi: 10.2196/19879] [Medline: 33026356]
70. Jiang G, Kiefer RC, Sharma DK, Prud'hommeaux E, Solbrig HR. A consensus-based approach for harmonizing the OHDSI
common data model with HL7 FHIR. Stud Health Technol Inform 2017;245:887-891 [FREE Full text] [doi:
10.3233/978-1-61499-830-3-887] [Medline: 29295227]
71. Brandt PS, Pacheco JA, Rasmussen LV. Development of a repository of computable phenotype definitions using the clinical
quality language. JAMIA Open 2021 Oct;4(4):ooab094 [FREE Full text] [doi: 10.1093/jamiaopen/ooab094] [Medline:
34926996]
72. Köpcke F, Prokosch H. Employing computers for the recruitment into clinical trials: a comprehensive systematic review.
J Med Internet Res 2014 Jul 01;16(7):e161 [FREE Full text] [doi: 10.2196/jmir.3446] [Medline: 24985568]
73. Resourcelist - FHIR v4.2.0. Health Level Seven International. URL: http://hl7.org/fhir/2020Feb/resourcelist.html[accessed
2021-12-21]
74. Kubrick W. CR 3.0 – a manifesto for the next generation of clinical research data standards. Reimagine Research. 2016
Aug 30. URL: https://waynekubick.com/2016/08/30/
cr-3-0-a-manifesto-for-the-next-generation-of-clinical-research-data-standards/[accessed 2021-06-17]
75. Aerts J. Towards a single data exchange standard for use in healthcare and in clinical research. Stud Health Technol Inform
2018;248:55-63. [doi: 10.3233/978-1-61499-858-7-55] [Medline: 29726419]
76. FHIR to CDISC joint mapping implementation guide v1.0. Clinical Data Interchange Standards Consortium. 2021 Sep 01.
URL: https://www.cdisc.org/standards/real-world-data/fhir-cdisc-joint-mapping-implementation-guide-v1-0[accessed
2022-04-22]
77. FHIR to CDISC joint mapping implementation guide 1.0.0 - STU 1. Health Level Seven International. URL: http://hl7.org/
fhir/uv/cdisc-mapping/STU1/[accessed 2022-04-22]
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 16
XSL FO (page number not for citation purposes)
•
RenderX

JMIR MEDICAL INFORMATICS Vorisek et al
78. Olson CM, Rennie D, Cook D, Dickersin K, Flanagin A, Hogan JW, et al. Publication bias in editorial decision making.
JAMA 2002 Jun 05;287(21):2825-2828. [doi: 10.1001/jama.287.21.2825] [Medline: 12038924]
79. National Research Data Infrastructure for Personal Health Data. NFDI4Health Consortium. URL: https://www.nfdi4health.de/
[accessed 2022-06-21]
Abbreviations
API: application programming interface
CDISC: Clinical Data Interchange Standards Consortium
CDM: common data model
FHIR: Fast Healthcare Interoperability Resources
HL7: Health Level Seven International
LOINC: Logical Observation Identifiers Names and Codes
ODM: Operational Data Standard
OHDSI: Observational Health Data Sciences and Informatics
OMOP: Observational Medical Outcomes Partnership
PRISMA: Preferred Reporting Items for Systematic Reviews and Meta-Analyses
PROSPERO: International Prospective Register of Systematic Reviews
REST: Representational State Transfer
SDTM: Study Data Tabulation Model
SNOMED CT: Systematized Nomenclature of Medicine Clinical Terms
Edited by C Lovis; submitted 29.12.21; peer-reviewed by S Hume, J Hüsers; comments to author 25.02.22; revised version received
22.04.22; accepted 18.05.22; published 19.07.22
Please cite as:
Vorisek CN, Lehne M, Klopfenstein SAI, Mayer PJ, Bartschke A, Haese T, Thun S
Fast Healthcare Interoperability Resources (FHIR) for Interoperability in Health Research: Systematic Review
JMIR Med Inform 2022;10(7):e35724
URL: https://medinform.jmir.org/2022/7/e35724
doi: 10.2196/35724
PMID:
©Carina Nina Vorisek, Moritz Lehne, Sophie Anne Ines Klopfenstein, Paula Josephine Mayer, Alexander Bartschke, Thomas
Haese, Sylvia Thun. Originally published in JMIR Medical Informatics (https://medinform.jmir.org), 19.07.2022. This is an
open-access article distributed under the terms of the Creative Commons Attribution License
(https://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium,
provided the original work, first published in JMIR Medical Informatics, is properly cited. The complete bibliographic information,
a link to the original publication on https://medinform.jmir.org/, as well as this copyright and license information must be included.
https://medinform.jmir.org/2022/7/e35724 JMIR Med Inform 2022 | vol. 10 | iss. 7 | e35724 | p. 17
XSL FO (page number not for citation purposes)
•
RenderX