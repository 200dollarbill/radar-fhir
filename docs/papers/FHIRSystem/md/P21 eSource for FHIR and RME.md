Evaluating the Coverage of the HL7® FHIR® Standard to Support eSource
Data Exchange Implementations for use in Multi-Site Clinical Research
Studies
Maryam Y. Garza, MMCi, MPH1,2, Michael Rutherford, MS1, Sahiti Myneni, PhD, MSE2,
Susan Fenton, PhD2, Anita Walden, MS3, Umit Topaloglu, PhD4, Eric Eisenstein, DBA5,
Karan R. Kumar, MD, MS5, Kanecia O. Zimmerman, MD, MPH5, Mitra Rocca, PhD6,
Gideon Scott Gordon, PhD6, Sam Hume, DSc7, Zhan Wang, PhD8, Meredith Zozus, PhD8
1University of Arkansas for Medical Sciences, Little Rock, AR; 2University of Texas Health
Science Center at Houston, Houston, TX; 3Oregon Health and Science University,
Portland, OR; 4Wake Forest University School of Medicine, Winston-Salem, NC; 5Duke
Clinical Research Institute, Duke University, Durham, NC; 6United States Food & Drug
Administration, Silver Springs, MD; 7Clinical Data Interchange Standards Consortium,
Austin, TX; 8University of Texas Health Science Center at San Antonio, San Antonio, TX
Abstract
The direct use of EHR data in research, often referred to as ‘eSource’, has long-been a goal for researchers because
of anticipated increases in data quality and reductions in site burden. eSource solutions should rely on data exchange
standards for consistency, quality, and efficiency. The utility of any data standard can be evaluated by its ability to
meet specific use case requirements. The Health Level Seven (HL7®) Fast Healthcare Interoperability Resources
(FHIR®) standard is widely recognized for clinical data exchange; however, a thorough analysis of the standard’s
data coverage in supporting multi-site clinical studies has not been conducted. We developed and implemented a
systematic mapping approach for evaluating HL7® FHIR® standard coverage in multi-center clinical trials. Study
data elements from three diverse studies were mapped to HL7® FHIR® resources, offering insight into the coverage
and utility of the standard for supporting the data collection needs of multi-site clinical research studies.
Introduction
Since the earliest days of health information systems and electronic health records (EHRs), clinical researchers have
sought to repurpose clinic data for use in clinical research studies.1 The electronic exchange of medical record data
directly from an EHR system to a research data collection system has long-been a goal for researchers because of
anticipated increases in data quality and reductions in site burden. Pursuit of direct extraction and use of EHR data in
multicenter clinical studies has been a long-term and multifaceted endeavor that includes design, development,
implementation and evaluation of methods and tools for semi-automating tasks in the research data collection process,
such as medical record abstraction (MRA).2 Both industry and federal agencies have continued to encourage the
development and advancement of solutions that promote optimal usage of electronic data sources in clinical
research.3,4 In 2013, the Food and Drug Administration (FDA) issued a guidance for use of electronic source (eSource)
data in clinical investigations4 – the term ‘eSource’ often used colloquially to refer to the method of direct capture,
collection, and storage of electronic source data (e.g., EHRs, electronic patient diaries, or wearable devices) in an
effort to streamline clinical research. In 2018, a separate FDA guidance was developed, specifically outlining the use
of EHR data in FDA-regulated clinical studies.5 Although several federal guidelines and industry standards exist, the
development, implementation, and evaluation of EHR-specific eSource solutions has been limited2 and manual
“transcription between electronic systems continues to be the norm”.3 This transcription occurs when a clinical
research coordinator reviews a patient record in the EHR and then copies EHR data from a screen to paper, hand enters
it into a research database, or both in sequence.
Over the last decade, sporadic attempts toward the development and implementation of eSource solutions have been
reported.6,7 Several eSource solutions have been developed, evaluated, and improved to allow for the direct data
extraction from the EHR to the electronic data capture system (EDC). However, most of the existing solutions have
been limited to single-EHR (vendor), single-EDC (electronic data capture), and single-institution implementations,2
which significantly hinders the generalizability and scalability of present solutions. Another significant limitation of
previous eSource implementations is that previous approaches all leveraged older data exchange standards, such as
HL7® Clinical Document Architecture (CDA®) or the Integrating the Healthcare Enterprise (IHE) Retrieve Form for
472

Data Capture (RFD) standards.2,8-12,17-19,21-35 A constraint of existing healthcare standards is the ability to handle the
inherent variability that exists within healthcare and clinical research. Traditionally, this occurs because the standard
lacks flexibility and does not have a formalized way to adapt to the diverse needs to support multiple use cases. Often,
this results in site- or institution-specific adjustments to the standard’s original specification (e.g., to capture more
fields and optionality) that can significantly add to implementation and maintenance costs and increase complexity to
the resulting implementations.36 For example, limitations restricting the ability of the Clinical Data Interchange
Standards Consortium (CDISC) Operational Data Model (ODM) to support a wider variety of eSource-related use
cases has been the lack of (1) a complete implementation model and (2) a formal mechanism for capturing semantics
or logical relationships between data elements.37,38 The Health Level Seven (HL7®) Fast Healthcare Interoperability
Resources (FHIR®) standard is designed to address the limitations of pre-existing standards through improved
specificity of data element definition and representation, as well as implementability, flexibility, and adaptability for
use in a wide variety of contexts without sacrificing information integrity.
Previous efforts have demonstrated the need for additional research and evaluation of eSource data collection for
multi-site clinical research studies.2,6-17 The successful implementation of a generalizable eSource solution requires
(1) use of data standards for consistency, (2) process re-design for efficiency, and (3) rigorous evaluation to assess
improvement (or not) in data quality, site effort, and cost.2,3,6,7,18,19 The work presented in this manuscript aims to
tackle the data standards component and will expand upon the work of previous pivotal studies to address the gaps
identified. The results will help to inform future eSource development efforts by providing insight into the utility of
the HL7® FHIR® standard in supporting EHR- and EDC-agnostic eSource implementations for use in multi-site
clinical research studies. To our knowledge, no work has been previously done to systematically evaluate content
coverage of the HL7® FHIR® standard for supporting data collection and exchange in multi-site clinical research.
While we focus on the clinical research use case, the work presented here is of great relevance to all biomedical
informatics domains (bio-, imaging, clinical, clinical research, public health, and translational informatics).
HL7® FHIR® Standard
The overall effectiveness and utility of any eSource solution is heavily reliant on the data exchange standard
implemented. Data exchange standards are necessary for seamless information flow by facilitating direct data sharing
across multiple systems.20 Unlike more traditional approaches used to support data exchange, i.e., data exchange via
FTP (file transfer protocol) and ETL (extract, transform, load) processes, data exchange standards enable
interoperability and streamline the electronic exchange process by organizing, representing, and encoding data so that
it can be easily understood and accepted by receiving systems.20 Use of international and/or national data and
exchange standards provides consistent approaches. Both of which would ultimately improve quality and efficiency
in data exchange and consumption for multi-site clinical research studies.
The HL7® FHIR® standard, or simply FHIR®, is an international healthcare information exchange standard “that
makes use of an HL7®-defined set of “resources” to support information sharing by a variety of means”.36 A resource
is a small collection of clinical and administrative information that can be captured or shared. All exchangeable
content is defined as a resource. Examples of resources include “Observation”, “Patient”, and “Specimen”. FHIR
was developed to exchange small units of information while incorporating additional structure to the data. It was
initially designed specifically for exchange, but also focuses on the content (boundaries and relationships) as well.
FHIR® resources not only define the units of data to be exchanged, but also provides business rules and defines the
interfaces between electronic systems to support the exchange process.
The FHIR® standard is becoming widely used internationally to support healthcare data exchange using a variety of
applications, primarily EHR-based data collection, including regulatory and clinical decision support purposes.
FHIR® is often referred to as the “next generation” standards framework, developed by incorporating the best features
of previous HL7® format standards, i.e., Version 2 (V2), Version 3 (V3), and Clinical Document Architecture
(CDA®).36 With a strong implementation focus, FHIR® allows for fast uptake and “out-of-the-box” interoperability
for seamless information exchange via RESTful architectures.36 FHIR® evolved from the need to share health
information securely across the web to multiple open systems and a multitude of device types (web browsers, desktop
machines, legacy systems, mobile devices, tablets) in real time.36 Additionally, FHIR®’s simple, yet versatile,
framework allows for the accommodation of diverse healthcare processes as a stand-alone standard or in tandem with
other widely used standards (e.g., CDISC Study Data Tabulation Model (SDTM), which is required for FDA-regulated
clinical trials), including existing HL7® standards (e.g., HL7® CDA®), and terminologies (e.g., LOINC®, SNOMED,
and ICD).
473

Many EHR vendors have shown interest and invested in the use of FHIR® to improve data exchange and
interoperability. Moreover, several vendors are already supporting various versions of the base standard within their
respective systems (i.e., Epic, Cerner) in order to comply with regulatory requirements (i.e., Centers for Medicare and
Medicaid Services (CMS)39 and Office of the National Coordinator for Health Information Technology (ONC)40 Final
Interoperability Rules). However, there is no evidence that the FHIR® standard is comprehensive or expressive
enough to support eSource implementations for multi-site clinical research. To determine the utility of the HL7®
FHIR® standard for multi-site clinical research, this evaluation assesses the extent to which this standard meets the
needs of representative clinical research studies. Our results quantify and classify the extent of data availability to
indicate the level of completeness of the HL7® FHIR® standard in supporting the data collection needs of multi-site
clinical research studies. Understanding the overall utility and content coverage of the HL7® FHIR® standard to
support efficient and accurate data collection is critical across clinical and translational research, for industry and
investigator-initiated studies, and has been communicated as an area in need of continued work across all relevant
stakeholder groups (academic, industry, and government).
Methods
Mapping was performed to assess the level of HL7® FHIR® standard completeness (or data element coverage) in
supporting data collection for multi-site clinical research studies. A systematic approach was developed and used to
map study Case Report Form (CRF), i.e., data collection form, data elements to corresponding HL7® FHIR® standard
resources. The mapping approach is a framework for evaluating the coverage of the standard and can be utilized by
others in the field performing similar work.
Study Selection
The research team requested example studies from several industry and federal sponsors who provided study CRFs
and data dictionaries for mapping. The studies varied in target population (adult vs. pediatric), therapeutic area (TA),
trial type, trial setting (inpatient vs. outpatient) and sponsor type (industry vs. federal). The main objective for
selection was to identify studies that may differ from one another in each of these five areas so that the mapping results
would be more generalizable to a wider range of study types. Briefly, Study A was a federally sponsored, pragmatic
cardiovascular randomized controlled trial (RCT) targeting adults (NCT03296813); Study B was a pharmaceutical
phase III antiepileptic drug (AED) trial also targeting adults (NCT03373383); and Study C was a federally sponsored
pediatric observational study that collected inpatient data retrospectively (https://heal.nih.gov/research/infants-and-
children/act-now).
Additional information on the three studies selected for mapping is available in Table 1. Variation across population,
therapeutic area, trial type, trial setting, and sponsor type ensures that our sample is representative, which is also
reflected by the diversity of data collected across studies. Study data elements were categorized into unique research
domains (i.e., demographics, medications, medical history, adverse events, etc.) in order to better gauge the
representativeness of our sample. In total, 2206 (814 distinct) data elements were evaluated.
Table 1. Clinical Research Study CRFs for FHIR® Mapping
Study Population TA Trial Type Inpatient / Outpatient Sponsor
A Adult CV / CHF Pragmatic RCT Both NIH-NHLBI
B Adult Antiepileptic Phase III Outpatient Pharmaceutical
C Pediatric NAS / NOWS Observational Inpatient NIH
*TA = therapeutic area (CV/CHF = cardiovascular/congestive heart failure, NAS/NOWS = neonatal abstinence syndrome/neonatal opioid
withdrawal syndrome); Trial Type = the type of trial represented by the Study (RCT = randomized control trial); Sponsor = the type of sponsor for
the study that provided the study CRF(s).
FHIR® Mapping
Data elements from electronic CRFs (eCRFs) and data dictionaries for the three representative studies were mapped
to the FHIR® standard. The HL7® US Core Release 4 (US Core R4) implementation guide41 and HL7® FHIR® Version
Release 4 (FHIR® R4) standard resources,36 the most current version of the standard released in late 2019 were
evaluated, i.e., used as the target for mapping. The US Core R4 implementation guide is based on the FHIR® R4
standard and “defines the minimum conformance requirements for accessing patient data”.41 We utilized a systematic
approach, incorporating the methodology developed and used in our earlier work,42,43 adapting the methods slightly
to fit the information needs of this effort. Two mappers, a clinical research informaticist (MYG) and an informatics
programmer (ZW), performed the CRF-to-FHIR resource mappings independently. The lead mapper (MYG) then
consolidated the mappings, and discrepancies were brought to the larger mapping team (MYG, ZW, MR, AW, MZ)
for discussion and adjudication. Adjudications of the mappings were performed to achieve consensus prior to the
474

analysis. In some cases, this required input from HL7® FHIR® experts to assist with interpretation of the standard.
Data elements or questions from the eCRFs were mapped to the data elements in the FHIR® resources. Mappers first
identified the appropriate resource for a CRF data element, and then they mapped the data elements to the resource.
Data elements were classified into two groups (“Available in FHIR” vs. “Not Available in FHIR”) and used to
calculate the actual coverage of the standard. This also provided a representation of the transformation between FHIR®
resources and the study eCRF.
The mapping template is comprised of two sections. The first half of the template (which includes columns 1-3 in
Table 2) contains information about study data elements. For each of the three studies, the following information was
represented for mapping: CRF name, section header (if applicable), question number (if applicable), data element
name and description, data type, units (if applicable), and permissible values (if applicable). The second half of the
template (which includes columns 4-10 in Table 2) contains information about the HL7® FHIR® standard resources:
resource availability (in US Core, FHIR® R4, both, or neither), profile name (if applicable), maturity level, resource
name, data element name and definition, data type, coding system and relevant codes (if applicable), and controlled
terminology (if applicable).
Table 2. FHIR® Mapping Template (to US CORE R4 & FHIR® R4)
Representative Study Data Elements HL7® FHIR® Standard Resources
CRF DE Name Type Core/R4 Resource DE Name Definition Type CS Code
Demographics DOB date Y Patient birthdate date of birth date LOINC 21112-8
Demographics Birth Time time Core only Patient Ext.(birthTime) time of birth datetime N/A N/A
Questionnaires Q1 text N N/A N/A N/A N/A N/A N/A
*The data entered is only for demonstration purposes. CRF = CRF name; DE Name = data element name; Type = data type; Core/R4 = indication
of resource availability in US Core (Core only), R4 (R4 only), both (Y) or neither (N); Resource = resource name; Definition = data element
definition; CS = coding system; Code = code value; PV = permissible value (or controlled terminology) list.
Upon completion of the mapping and adjudication, a comparison of the mappings was performed across studies to
identify differences and commonalities on a study-by-study basis. FHIR coverage was calculated as a percentage for
each individual study (total unique data elements “Available in FHIR” vs. total unique data elements overall). In
addition, FHIR® coverage was observed across the different study domain areas (i.e., demographics vs. medications
vs. vital signs, etc.) in order to identify the domains with the least and most coverage. It was anticipated that several
study data elements would require mapping to more than one FHIR® resource data element (to account for context
such as time, applicable units, etc.). Therefore, the total number of unique fields in the original CRF were compared
to the total number of FHIR® resources required in order to provide insight into the level of complexity for mapping
each individual data element.
Results
A total of 814 distinct data elements (2206 total data elements) across three representative studies were mapped to the
HL7® FHIR® standard resources. Distinct data elements were identified as those that were not repeated within or
shared across studies. For example, all three studies collected demographics data (i.e., date of birth, sex, race, and
ethnicity); these were counted as “in common”. To calculate distinct data elements, these would only be counted once
(i.e., 4 distinct vs. 12 total data elements). The same applied to studies collecting data across multiple visits. In those
cases, repeated data elements (e.g., labs collected at visit 1, 2, and 3) were also considered as “in common” and only
counted once. Our results are presented based on the distinct total (N=814).
The three studies varied significantly in the type of data collected and, ultimately, in the distribution of data elements
across research domains (i.e., demographics vs. vital signs vs. medications vs. therapeutic area (TA) -specific). When
considered in aggregate, the majority of distinct data elements across all three studies were primarily questionnaires
(27%), TA-specific (19%) and labs (8%). Individually, however, the results varied. Data elements for Study A (CHF,
pragmatic RCT) centered on questionnaires (25%) and enrollment/eligibility (20%), the next two major domains being
TA-specific (8%) and labs (7%). In comparison, most of the data elements for Study B (AED, phase III) mimicked
the aggregate spread: questionnaires (33%), TA-specific (20%), and labs (10%). Study C (NOWS,
observational/retrospective) had the largest distribution of data elements across five domains: TA-specific (28%),
encounters (19%), demographics (18%), enrollment/eligibility (14%), and medical history (11%). The data presented
in Table 3 depicts the percentage of total study data elements across the most commonly used domains per study.
475

Table 3. Research domain areas per study (all study data elements)
Conmed  Demog  Eligibility  Encounters  Labs  MH  PX  QA  TA  Vitals  Other
Study
|     | (%)  | (%)  | (%)  | (%)  | (%)  | (%)  | (%)  | (%)  | (%)  | (%)  (%)  |     |
| --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --------- | --- |
| A   | 2%   | 4%   | 20%  | 4%   | 7%   | 3%   | N/A  | 25%  | 8%   | 6%  21%   |     |
| B   | 2%   | 2%   | 1%   | 4%   | 10%  | 8%   | 7%   | 33%  | 20%  | 2%  11%   |     |
| C   | N/A  | 18%  | 14%  | 19%  | N/A  | 11%  | 1%   | N/A  | 28%  | N/A       | 9%  |
*Data presented is representative of all distinct study data elements prior to mapping and categorization. Conmed = concomitant medications;
Demog = demographics; MH = medical history; PX = procedures; QA = questionnaires; TA = therapeutic area-specific; N/A = data not collected
as part of the study.
Of the 814 total (distinct) data elements, approximately half (51%) were “Available in FHIR”, resulting in 418 total
data elements mapping to FHIR® (Table 4).  For two of the three studies (Studies A and C), over half of the study data
elements were “Available in FHIR” (55% and 79% respectively).   For the third study (Study B), a little less than half
of the study data elements were “Available in FHIR” (45%).  The total number of data elements per study, as well as
the total number per mapping category (“Available in FHIR” vs. “Not Available in FHIR”) is available in Table 3.
Table 4. FHIR® Mapping Totals
Study  Available in FHIR (n (%))  NOT Available in FHIR (n (%))  Total Data Elements (DEs) (N)
| A       |     | 67 (55%)   |     |     |     | 55 (45%)   |     |     |     | 122  |     |
| ------- | --- | ---------- | --- | --- | --- | ---------- | --- | --- | --- | ---- | --- |
| B       |     | 264 (45%)  |     |     |     | 318 (55%)  |     |     |     | 582  |     |
| C       |     | 87 (79%)   |     |     |     | 23 (21%)   |     |     |     | 110  |     |
| TOTALS  |     | 418 (51%)  |     |     |     | 396 (49%)  |     |     |     | 814  |     |

The distribution across research domains of the data elements “Available in FHIR” echoed what was seen in Table 3,
except that the questionnaires percentage dropped to 0% for both Studies A and B (questionnaires were not collected
as part of Study C).  Across all three studies, questionnaire data elements were categorized as “Not Available in
FHIR”.  These data elements are representative of patient reported outcomes, typically collected via study surveys or
validated study questionnaires.  Accordingly, when considered in aggregate, the data elements “Available in FHIR”
were primarily distributed across the TA-specific (28%), labs (13%), and medical history (12%) domains.  Figure 1
provides a visual representation of the distribution of data elements “Available in FHIR” across the various domains.

Figure 1. Percentage of study data elements “Available in FHIR” across research domains.
In comparison, Figure 2 represents the distribution of data elements “Not Available in FHIR”, demonstrating the gaps
in content coverage for the three representative studies.  When considered in aggregate, 396 (49%) of data elements
across all studies did not map.  Of the 396 data elements “Not Available in FHIR”, a little over half were part of the
questionnaire domain (56%).  The remaining were distributed relatively evenly across eleven domains: Administrative
|     |     |     |     |     | 476 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

(11%), TA-specific (9%), study drug administration (5%), encounters (4%), adverse events (3%), medical history
(3%), procedures (3%), eligibility (2%), labs (2%), medications (1%), and demographics (1%).
At the study level, Study A and Study B were similar in that close to three-fourths of data elements “Not Available in
FHIR” were contained within the questionnaire (56% and 60%, respectively) and administrative (27% and 9%,
respectively) research domains (Figure 2). In this case, administrative data refers to data that would be collected by
the study team for administrative or operational purposes and not expected to be found in an EHR. For example, this
would include fields related to participant stratification or randomization. As an observational study, Study C did not
collect questionnaire or administrative data. Instead, a significant number of Study C data elements “Not Available
in FHIR” were contained within the encounters (57%) and TA-specific (22%) research domains (Figure 2). Here,
encounters includes hospitalization-related data; but it is important to note that some of the encounter data collected
for Study C was from the institution from which the patient was transferred to the study site. In general, transfer-
related data elements were considered “Not Available in FHIR” because of the high variability across sites with the
availability of transfer records within the EHR. For sites that participated in Study C, several had transfer data stored
in pdf-format, but there was inconsistency across sites with where the files were stored within the EHR.
Figure 2. Percentage of study data elements “Not Available in FHIR” across research domains.
A similar comparison was done across HL7® FHIR® resources to identify patterns or trends in the mapping (Table 5).
In aggregate, study data elements mapped to three FHIR®-specific resources in particular: Observation (25%),
Condition (19%), and Encounter (9%). When evaluated individually, there was some variation between studies. For
Study A, the resources most relevant were Observation (27%), Encounter (16%), Diagnostic Report (14%), and Patient
(13%). For Study B, Condition (27%), Observation (22%), and Specimen (10%) were the most popular. For Study
C, a little over one-third of the data elements mapped to the Observation resource (34%), the remainder distributed
across a variety of others, including Medication Administration (13%), Encounter (10%), Patient (9%), Care Plan
(9%), and Condition (6%).
Table 5. HL7® FHIR® resources most common across the three representative studies
Care Plan Condition DX Report Encounter RX Admin Observation Patient PX Specimen Other
Study
(%) (%) (%) (%) (%) (%) (%) (%) (%) (%)
A 2% 6% 14% 16% 0% 27% 13% 8% 0% 14%
B 0% 27% 7% 7% 0% 22% 3% 5% 10% 19%
C 9% 6% 4% 10% 13% 34% 9% 3% 0% 12%
*Data presented is representative of the FHIR® resources in which study data elements “Available in FHIR” mapped to most. This breakdown is
specific to FHIR®’s standard nomenclature, and does not necessarily echo the research domains represented in the tables and figures above. DX
Report = diagnostic report; RX Admin = medication administration; PX = procedure.
477

Discussion
A systematic mapping approach was developed and used to map study data elements from three therapeutically diverse
studies to HL7® FHIR® resources. The results of this work offer insight into the coverage and utility of the standard
for supporting the data collection needs of multi-site clinical research studies. Through this work, we have greater
insight into the representation of the transformation between FHIR® resources and study data elements collected within
the eCRFs.
With regards to FHIR® coverage, Studies A (CHF, pragmatic RCT) and Study C (NOWS, observational/retrospective)
fared similarly, as over half of the data elements for both studies were available in FHIR® resources (55% and 79%,
respectively. The content coverage for Study B (AED, phase III), was slightly lower, having a little less than half of
its data elements (45%) map to FHIR®. It is anticipated that the dependency of Study B on questionnaire (or Patient
Reported Outcomes) data may be a factor in the reduced coverage, as the questionnaire data elements are not likely to
be captured within an EHR and were, therefore, categorized as “Not Available in FHIR”. Conversely, while Study A
also collected questionnaire data (20% of the total data elements), the distribution of data elements across domains
was much more broad than for Study B. Nearly half of Study A’s data elements were dispersed across a variety of
other domains: enrollment/eligibility, concomitant medications, medical history, and therapeutic area (TA)-specific
content. Although these domains, and the subsequent data elements, are being utilized for research purposes, they are
also much more clinically relevant than questionnaire data elements and much more likely to be available in an EHR
or healthcare record. Similarly, Study C relied heavily on TA-specific data elements within the Diagnosis and
Procedure domains, as well as the Medical History domain, which again are more clinically relevant domains.
Given the distribution of research domains across the three studies, it was not surprising to see that the FHIR®
resources most applicable to support data collection for these studies included the Condition, Procedure, and
Observation resources. The Condition resource encompasses all data related to a clinical condition, problem,
diagnosis or other relevant clinical event.36 In addition to housing data on current conditions or diagnostic events, the
Condition resource also includes items likely found in a problem list or medical history. The Procedure resource
includes data elements to capture any action or intervention performed on or for a patient.36 This can include physical
(e.g., surgery) and behavioral (e.g., counseling) interventions. Lastly, the Observation resource collects measurement
data about a patient.36 The Observation resource is a catchall for data elements commonly collected as part of clinical
research studies, such as vital signs and laboratory data.
Based on these results, it is anticipated that other studies would follow a similar pattern, the distribution of data
elements across FHIR® resources being dependent on the study type and research design (i.e., observational vs.
behavioral vs. pharmacokinetic vs. RCT, etc.), but heavily using those noted here. With regards to data element
coverage, we estimate that late-phase and practice-oriented studies will yield similar results to these three studies, for
which approximately 45-80% of the study data elements would be “Available in FHIR.” Again, we predict that the
variability in FHIR® coverage across studies to be contingent primarily on study type and research design. For
example, retrospective studies that leverage and are designed around EHR data (like Study C) and pragmatic clinical
trials (like Study A) are much more likely to be on the higher end of the scale. Content coverage could also vary
significantly for studies relying heavily on questionnaire data that may not be programmed into or collected within
the EHR. For example, approximately one-third of the data elements for Study B were questionnaire data elements.
If we were to recalculate content coverage by considering only non-questionnaire data elements, the “Available in
FHIR” rate would increase from 45% to 68%. For Study A, the rate would increase from 65% to 81%. (Study C
would not change, as no questionnaire data elements were captured). It should be noted that the HL7® FHIR® standard
does have “Questionnaire” and “Questionnaire Response” resources available that could be utilized to capture
questionnaire data. However, use of these resources would require that (1) the data was input using FHIR®
Questionnaire and (2) that the resulting response data, contained within the Questionnaire Response resource, would
be stored in the EHR to be consumed later. Some studies may implement questionnaires through the EHR patient
portal, but this is not always done. Future research could also reveal that the FHIR® Questionnaire and Questionnaire
Response resources may be utilized to fill the gap in resource coverage, although, that as well would require FHIR®
utilization at input to facilitate the storage and subsequent consumption.
From our results, it appears that the areas for which content coverage was lacking included research domains for which
the data are not traditionally stored (and/or not documented consistently) within the EHR, and would likely be
unavailable through a FHIR®-based, EHR-to-eCRF solution: questionnaires, administrative data, and encounters data
specific to transfers (refer to Figure 2). To address these gaps, we must first consider the variation in the clinical
documentation workflow across study sites (a contributing factor to the “unmappable” nature of transfer-related
478

encounter data), as well as the implementation and utilization of various research-supporting EHR modules (e.g.,
implementing questionnaires through the EHR patient portal). It is important to note that site decisions about where,
when, and how to chart data within the EHR will likely erode the coverage. We continue our effort to address these
gaps and recommend that additional research be done in this area to identify mechanisms for improving data collection
for multi-site clinical research studies.
Limitations in this work are the following. We did not have a clinical research team member from two of the three
studies to review our mapping. A clinical team member may have additional insight to an eCRF field definition item
that could influence the mapping. To reduce the chance for bias amongst the informatics team performing the
mapping, we measured the inter-rater reliability among mappers and found it to be high: 88% on average (89%, 88%,
and 92%, for each individual study, respectively). Due to the time- and resource-intensive nature of the mapping
process, the mapping performed was limited to three clinical research studies, which may impact the generalizability
of our findings. However, the three studies selected for this pilot project were carefully chosen to ensure the greatest
level of diversity (i.e., different study designs, trial types, populations, etc.) to help mitigate any limitations arising
from the small sample size. Future work will include FHIR® mapping for a larger number of studies. It is also
important to note the mapping indicates what the most recent FHIR® release covers, not what is available in the EHR
to populate the eCRFs. The latter should be decreased from what is available per the standard. Thus, the percent
coverage reported here would be lower for what is commonly available across multiple sites. In addition, the FHIR®
standard continues to be improved; therefore, we expect the coverage and expressiveness to improve over time.
Further, as use of FHIR® continues to increase, as new uses of FHIR®-based data exchange are implemented, and as
FHIR® becomes a method by which to get data required for institutional reporting, we anticipate that variability in
clinical documentation to decrease somewhat and improve over time. Therefore, in general, the percentages reported
here should improve somewhat over time. Additional work is underway to investigate this further.
Conclusion
The results of this effort provide insight into the feasibility and generalizability of a FHIR®-based eSource solution
and can be used to inform future eSource work by providing possible ranges of the HL7® FHIR® standard for the
direct extraction of EHR data in clinical research, including examples of types of data available. Across the three
representative studies, two of the three studies achieved close to 50% coverage, the third nearly 80%. This is good
news, as it translates to the potential for a 50% reduction in manual data abstraction by a study coordinator. Through
this work, we have developed and demonstrated a method for quantifying the coverage of the HL7® FHIR® standard
for a particular study. The results presented here demonstrate the maximum potential coverage for these studies at
this time, which are transferrable to many other clinical research studies. It is more than likely, that as the standard
matures and its implementation and use increases, total coverage will also increase. Work is ongoing by this team
and within HL7® to improve FHIR’s utility across clinical research. The results achieved here offer insight into some
of the existing limitations of the standard and may be used to guide existing and future development efforts.
Furthermore, this work has identified the information necessary to, and likely sufficient for, automatically
transforming FHIR®-based data to a study case report form. Ultimately, quantifying the coverage of the standard
could be used to further advance the development of the HL7® FHIR® standard in order to meet the data collection
needs of multi-site clinical research studies.
479

References
1. Collen MF. Clinical research databases--a historical review. J Med Syst 1990; 14: 323–344.
2. Garza MY, Myneni S, Nordo A, et al. eSource for standardized health information exchange in clinical research:
A systematic review. Stud Health Technol Inform. 2019;257: 115-124. doi: 10.3233/978-1-61499-951-5-115
3. Kellar E, Bornstein SM, Caban A, et al. Optimizing the use of electronic data sources in clinical trials: The
landscape, Part 1. Therapeutic Innovation & Regulatory Science. 2016;50(6): 682-696. doi:
10.1177/2168479016670689
4. Food and Drug Administration (FDA). Guidance for industry: Electronic source data in clinical investigations.
Center for Biologics Evaluation and Research, the Center for Drug Evaluation and Research, and the Center for
Devices and Radiological Health at the Food and Drug Administration. 2013. Retrieved from
https://www.fda.gov/media/85183/download
5. Food and Drug Administration (FDA). Use of electronic health record data in clinical investigations, Guidance
for industry. Center for Drug Evaluation and Research, Center for Biologics Evaluation and Research, and Center
for Devices and Radiological Health at the Food and Drug Administration. 2018. Retrieved from
https://www.fda.gov/regulatory-information/search-fda-guidance-documents/use-electronic-health-record-data-
clinical-investigations-guidance-industry
6. Safran C, Bloomrosen M, Hammond WE, Labkoff S, Markel-Fox S, Tang PC, Detmer DE, Expert Panel. Toward
a national framework for the secondary use of health data: An American Medical Informatics Association White
Paper. J Am Med Inform Assoc. 2007;14(1):1-9.
7. Kush R, Alschuler L, Ruggeri R, et al. Implementing Single Source: the STARBRITE proof-of-concept study. J
Am Med Inform Assoc. 2007;14(5):662-673. doi: 10.1197/jamia.M2157
8. Sung NS, Crowley WF, Jr., Genel M, et al. Central challenges facing the national clinical research enterprise.
JAMA. 2003;289(10):1278-1287.
9. Getz KA. Study on Adoption and Attitudes of Electronic Clinical Research Technology Solutions and Standards.
Boston: Tufts Center for the Study of Drug Development (CSDD); August 2007.
10. Eisenstein EL, Collins R, Cracknell BS, et al. Sensible approaches for reducing clinical trial costs. Clin Trials.
2008;5(1):75-84.
11. Levinson DR. Challenges to FDA’s ability to monitor and inspect foreign clinical trials. Office of the Inspector
General, U.S. Department of Health and Human Services. 2010. OEI-01-08-00510.
12. Kaitin KI. The Landscape for Pharmaceutical Innovation: Drivers of Cost-Effective Clinical Research. Pharm
Outsourcing. 2010;3605.
13. Embi PJ, Payne PR, Kaufman SE, Logan JR, Barr CE. Identifying challenges and opportunities in clinical
research informatics: analysis of a facilitated discussion at the 2006 AMIA Annual Symposium. AMIA Annu
Symp Proc. 2007: 221-225.
14. Payne PR, Embi PJ, Sen CK. Translational Informatics: Enabling High Throughput Research Paradigms. Physiol
Genomics. 2009;39(3):131-40. doi: 10.1152/physiolgenomics.00050.2009
15. Embi PJ, Payne PR. Clinical research informatics: challenges, opportunities and definition for an emerging
domain. J Am Med Inform Assoc. 2009;16(3):316-327.
16. Malakoff D. Clinical trials and tribulations. Spiraling costs threaten gridlock. Science. 2008;322(5899):210-213.
17. Eisenstein EL, Nordo AH, Zozus MN. Using Medical Informatics to Improve Clinical Trial Operations. Stud
Health Technol Inform. 2017;234:93-97.
18. Kim D, Labkoff S, Holliday SH. Opportunities for electronic health record data to support business functions in
the pharmaceutical industry--a case study from Pfizer, Inc. J Am Med Inform Assoc. 2008;15(5):581-584.
19. Nordo A, Eisenstein EL, Garza M, Hammond EW, Zozus MN. Evaluative Outcomes in Direct Extraction and
Use of EHR Data in Clinical Trials. Stud Health Technol Inform. 2019;257: 333-340. doi: 10.3233/978-1-61499-
951-5-333
20. Institute of Medicine (US) Committee on Data Standards for Patient Safety; Aspden P, Corrigan JM, Wolcott J,
et al., editors. Patient Safety: Achieving a New Standard for Care. Washington (DC): National Academies Press
(US);2004: 4, Health Care Data Standards. Available from: https://www.ncbi.nlm.nih.gov/books/NBK216088/
21. Nordo AH, Eisenstein EL, Hawley J, et al. A comparative effectiveness study of eSource used for data capture
for a clinical research registry. Int J Med Inform. 2017;103:89-94.
22. Ethier JF, Curcin V, McGilchrist MM, et al. eSource for clinical trials: Implementation and evaluation of a
standards-based approach in a real world trial. Int J Med Inform. 2017;106:17-24.
23. Kiechle M, Paepke S, Shwarz-Boeger U, et al. EHR and EDC Integration in Reality. Applied Clinical Trials
Online. 2009. Retrieved from http://www.appliedclinicaltrialsonline.com/ehr-and-edc-integration-reality
480

24. El Fadly A, Rance B, Lucas N, et al. Integrating clinical research with the Healthcare Enterprise: from the RE-
USE project to the EHR4CR platform. J Biomed Inform. 2011;44 Suppl 1:S94-102.
25. Murphy EC, Ferris FL, 3rd, O'Donnell WR. An electronic medical records system for clinical research and the
EMR EDC interface. Invest Ophthalmol Vis Sci. 2007;48(10):4383-4389.
26. El Fadly A, Lucas N, Rance B, Verplancke P, Lastic PY, Daniel C. The REUSE project: EHR as single datasource
for biomedical research. Stud Health Technol Inform. 2010;160(Pt 2):1324-1328.
27. Raman SR, Curtis LH, Temple R, et al. Leveraging electronic health records for clinical research. Am Heart J.
2018;202:13-19.
28. Beresniak A, Schmidt A, Proeve J, et al. Cost-Benefit Assessment of the Electronic Health Records for Clinical
Research (EHR4CR) European Project. Value Health. 2014;17(7):A630.
29. Beresniak A, Schmidt A, Proeve J, et al. Cost-benefit assessment of using electronic health records data for
clinical research versus current practices: Contribution of the Electronic Health Records for Clinical Research
(EHR4CR) European Project. Contemp Clin Trials. 2016;46:85-91.
30. De Moor G, Sundgren M, Kalra D, et al. Using electronic health records for clinical research: the case of the
EHR4CR project. J Biomed Inform. 2015;53:162-173.
31. Dupont D, Beresniak A, Sundgren M, et al. Business analysis for a sustainable, multi-stakeholder ecosystem for
leveraging the Electronic Health Records for Clinical Research (EHR4CR) platform in Europe. Int J Med Inform.
2017;97:341-352.
32. Doods J, Bache R, McGilchrist M, Daniel C, Dugas M, Fritz F. Piloting the EHR4CR feasibility platform across
Europe. Methods Inf Med. 2014;53(4):264-268.
33. Gersing K, Krishnan R. Clinical Management Information Research System (CMRIS). Psychiatric Services.
2003;54(9):1199-1200.
34. Laird-Maddox M, Mitchell SB, Hoffman M. Integrating research data capture into the electronic health record
workflow: real-world experience to advance innovation. Perspect Health Inf Manag. 2014;11:1e.
35. Lencioni A, Hutchins L, Annis S, et al. An adverse event capture and management system for cancer studies.
BMC Bioinformatics. 2015;16 Suppl 13:S6.
36. HL7.org. HL7® FHIR® Release 4. 2018. Retrieved from http://hl7.org/fhir/R4/index.html
37. Hume S, Aerts J, Sarnikar S, Huser V. Current applications and future directions for the CDISC operational data
model standard: a methodological review. J Biomed Inform. 2016;60:352-362. doi:
https://doi.org/10.1016/j.jbi.2016.02.016
38. Huser V, Sastry C, Breymaier M, Idriss A, Cimino JJ. Standardizing data exchange for clinical research protocols
and case report forms: An assessment of the suitability of the Clinical Data Interchange Standards Consortium
(CDISC) Operational Data Model (ODM). J Biomed Inform. 2015;57:88–99. doi:10.1016/j.jbi.2015.06.023
39. Centers for Medicare & Medicaid Services (CMS). CMS Interoperability and Patient Access final rule (CMS-
9115-F). Centers for Medicare & Medicaid Services at the Department of Health and Human Services. 2020.
Retrieved from https://www.cms.gov/files/document/cms-9115-f.pdf
40. Office of the National Coordinator for Health Information Technology (ONC). 21st Century Cures Act:
Interoperability, Information Blocking, and the ONC Health IT Certification Program. Office of the National
Coordinator for Health Information Technology at the Department of Health and Human Services. 2020.
Retrieved from https://www.healthit.gov/sites/default/files/cures/2020-
03/ONC_Cures_Act_Final_Rule_03092020.pdf
41. Marquard B, Haas E, Grieve G, Bashyam N. HL7® FHIR® US CORE Implementation Guide STU 3. 2019.
Retrieved from https://build.fhir.org/ig/HL7/US-Core-R4
42. Garza M, Del Fiol G, Tenenbaum J, Walden A, Zozus MN. Evaluating common data models for use with a
longitudinal community registry. J Biomed Inform. 2016;64:333-341.
43. Garza M, Seker E, Zozus M. Development of data validation rules for therapeutic area standard data elements in
four mental health domains to improve the quality of FDA submissions. Stud Health Technol Inform.
2019;257:125-132.
481
