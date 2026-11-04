JournaloftheAmericanMedicalInformaticsAssociation,2023,30(12),2050–2063
https://doi.org/10.1093/jamia/ocad180
Advanceaccesspublication30August2023
Review
Review
| Effects   |     | of machine |                  |     | learning-based   |        |     |                                          | clinical  |     | decision |     | support |     |     |
| --------- | --- | ---------- | ---------------- | --- | ---------------- | ------ | --- | ---------------------------------------- | --------- | --- | -------- | --- | ------- | --- | --- |
| systems   |     | on         | decision-making, |     |                  |        |     | care                                     | delivery, |     |          | and | patient |     |     |
| outcomes: |     |            | a scoping        |     |                  | review |     |                                          |           |     |          |     |         |     |     |
|           |     |            |                  |     | 1,2,*,DavidLyell |        |     | 1,BambangWidyantoro2,3,ShlomoBerkovsky1, |           |     |          |     |         |     |     |
AnindyaPradiptaSusanto
1
FarahMagrabi
1CentreforHealthInformatics,AustralianInstituteofHealthInnovation,MacquarieUniversity,Sydney,NSW2109,Australia,2Facultyof
Medicine,UniversitasIndonesia,Jakarta,DKIJakarta10430,Indonesia,3NationalCardiovascularCenterHarapanKitaHospital,Jakarta,DKI
Jakarta11420,Indonesia
*Correspondingauthor:AnindyaPradiptaSusanto,MD,CentreforHealthInformatics,AustralianInstituteofHealthInnovation,MacquarieUniversity,Sydney,
NSW2109,Australia(anindya.susanto@hdr.mq.edu.au,anindya.susanto@ui.ac.id)
Abstract
Objective:Thisstudyaimstosummarizetheresearchliteratureevaluatingmachinelearning(ML)-basedclinicaldecisionsupport(CDS)systems
inhealthcaresettings.
Materialsandmethods:WeconductedareviewinaccordancewiththePRISMA-ScR(PreferredReportingItemsforSystematicReviewsand
MetaAnalysesextensionforScopingReview).Fourdatabases,includingPubMed,Medline,Embase,andScopusweresearchedforstudies
publishedfromJanuary2016toApril2021evaluatingtheuseofML-basedCDSinclinicalsettings.Weextractedthestudydesign,caresetting,
clinicaltask,CDStask,andMLmethod.ThelevelofCDSautonomywasexaminedusingapreviouslypublished3-levelclassificationbasedon
thedivisionofclinicaltasksbetweentheclinicianandCDS;effectsondecision-making,caredelivery,andpatientoutcomesweresummarized.
Results:Thirty-twostudiesevaluatingtheuseofML-basedCDSinclinicalsettingswereidentified.Allwereundertakenindevelopedcountries
andlargelyinsecondaryandtertiarycaresettings.ThemostcommonclinicaltaskssupportedbyML-basedCDSwereimagerecognitionand
interpretation(n¼12)andriskassessment(n¼9).ThemajorityofstudiesexaminedassistiveCDS(n¼23)whichrequiredclinicianstoconfirm
or approveCDS recommendations for risk assessment in sepsis and for interpreting cancerouslesions in colonoscopy. Effects on decision-
making,caredelivery,andpatientoutcomesweremixed.
Conclusion:ML-basedCDSarebeingevaluatedinmanyclinicalareas.ThereremainmanyopportunitiestoapplyandevaluateeffectsofML-
basedCDSondecision-making,caredelivery,andpatientoutcomes,particularlyinresource-constrainedsettings.
Keywords:artificialintelligence;automation;clinicaldecisionsupport;evaluation;machinelearning.
Backgroundandsignificance Previous reviews have examined the application of AI in
|              |     |          |          |         |       |         |     | specific | health | conditions, |     | such as | colonoscopy, | stroke, | and |
| ------------ | --- | -------- | -------- | ------- | ----- | ------- | --- | -------- | ------ | ----------- | --- | ------- | ------------ | ------- | --- |
| Contemporary |     | clinical | decision | support | (CDS) | systems |     | are      |        |             |     |         |              |         |     |
sepsis.9–11Thisscopingreviewaimstotakeabroaderviewby
| increasingly | being   | embedded |     | with | artificial     | intelligence | (AI),     |             |     |     |          |            |           |            |     |
| ------------ | ------- | -------- | --- | ---- | -------------- | ------------ | --------- | ----------- | --- | --- | -------- | ---------- | --------- | ---------- | --- |
|              |         |          |     |      |                |              |           | summarizing |     | the | research | literature | about the | evaluation | of  |
| especially   | machine | learning |     | (ML) | models trained |              | on a wide |             |     |     |          |            |           |            |     |
varietyofclinical datasets.1,2 Like theprevious generationof ML-based CDS in clinical settings. Here, ML models must
|           |      |         |       |     |                  |     |        | perform |       | well on    | real-world | populations | and      | ML-based  | CDS |
| --------- | ---- | ------- | ----- | --- | ---------------- | --- | ------ | ------- | ----- | ---------- | ---------- | ----------- | -------- | --------- | --- |
| CDS which | were | largely | based | on  | human-engineered |     | rules, |         |       |            |            |             |          |           |     |
|           |      |         |       |     |                  |     |        | need    | to be | seamlessly | integrated | with        | clinical | workflows | as  |
ML-basedCDScansupportcliniciansintaskssuchasdisease
|            |           |     |            |         |             |     |          | well | as the | existing | information | technology |     | (IT) infrastruc- |     |
| ---------- | --------- | --- | ---------- | ------- | ----------- | --- | -------- | ---- | ------ | -------- | ----------- | ---------- | --- | ---------------- | --- |
| diagnosis, | treatment |     | selection, | patient | monitoring, |     | and risk |      |        |          |             |            |     |                  |     |
ture.12
stratification for primary prevention.3 While many studies To better understand the role of ML-based CDS in
havedemonstratedtheperformanceofMLmodelsforspecific clinical tasks, we examined the level of system autonomy13
tasks,4,5 and summarized effects on decision-making, care delivery,
| clinical |     | little | is known | about | the | use of | ML-based |     |     |     |     |     |     |     |     |
| -------- | --- | ------ | -------- | ----- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
andpatientoutcomes.14AsML-basedCDSoperateswithina
CDSinhealthcaresettingsaswellastheireffectsondecision-
making, care delivery, and patient outcomes.6 In contrast, human-technology system, clinician interaction with CDS
rule-basedCDShavebeenshowntobeeffectiveinimproving influenceshowtheymakedecisionsthatthenaffectcaredeliv-
care delivery and patient outcomes in a wide-variety of clini- ery and patient outcomes. Previous reviews that have exam-
cal tasks such as computerized provider order entry (CPOE) ined AI in clinical settings have not considered the level of
andelectronic prescribing, diagnosticassistance, andforpre- system autonomy or the specific role of the CDS in clinical
| ventivecarereminders.7,8 |     |     |     |     |     |     |     | tasks.15–17 |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Received:May10,2023;Revised:August1,2023;EditorialDecision:August20,2023;Accepted:August23,2023
VC TheAuthor(s)2023.PublishedbyOxfordUniversityPressonbehalfoftheAmericanMedicalInformaticsAssociation.
Allrightsreserved.Forpermissions,pleaseemail:journals.permissions@oup.com

JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12 2051
Materialsandmethods
Geo-economicsetting
|     |     |     |     |     |     |     |     | We examined | the | countries | where | the | study | took place | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ----- | --- | ----- | ---------- | --- |
GiventhattheresearchliteratureabouttheevaluationofML-
based CDS appears young and heterogeneous, a scoping classified them using the World Bank’s classification by
| reviewwasundertakenfocusingonstudiesreportingtheeval- |     |     |     |     |     |     |     | income.22 |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
uationofML-basedCDSsystemsinclinicalsettingsandtheir
CDStask
effectsondecision-making,caredelivery,orpatientoutcomes.
|     |     |     |     |     |     |     |     | CDS systems | can | assist | with | a variety | of clinical | tasks. | We  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | ---- | --------- | ----------- | ------ | --- |
Thereviewwasconductedusingthemethodologyoutlinedby
into1:
Arksey and O’Malley18 and refined by Levac et al.19 This categorized CDS tasks evidence retrieval, CPOE and
electronicprescribing,diagnosticassistance,therapyplanning
| framework | consists | of 5 | steps: | setting | the research | question; |     |                 |     |                  |     |         |         |     |          |
| --------- | -------- | ---- | ------ | ------- | ------------ | --------- | --- | --------------- | --- | ---------------- | --- | ------- | ------- | --- | -------- |
|           |          |      |        |         |              |           |     | and critiquing, |     | risk assessment, |     | process | support |     | systems, |
searchingrelevantstudies;selectingthestudybasedoninclu-
|     |     |     |     |     |     |     |     | image recognition |     | and | interpretation |     | including | computer |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | -------------- | --- | --------- | -------- | --- |
sionandexclusioncriteria;extractingthedata;andcollating,
summarizing,andreportingtheresults.Reportingwasguided aideddiagnosis,andexpertlaboratoryinformationsystems.
| by the PRISMA-ScR |     | (Preferred |     | Reporting | Items | for | System- |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | --- | --------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
MLtypeandmethod
| atic Reviews | and | Meta | Analyses | extension |     | for | Scoping |     |     |     |     |     |     |     |     |
| ------------ | --- | ---- | -------- | --------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
WhereavailablethetypeandmethodofMLwereexamined.
Reviews)standard.20
|     |     |     |     |     |     |     |     | ML type | was categorized |     | into | supervised | learning, | unsuper- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ---- | ---------- | --------- | -------- | --- |
Searchstrategy visedlearning,andreinforcementlearning.MLmethodswere
|               |     |            |           |     |         |          |     | reported | as extracted |     | from the | literature. | A   | study could | be  |
| ------------- | --- | ---------- | --------- | --- | ------- | -------- | --- | -------- | ------------ | --- | -------- | ----------- | --- | ----------- | --- |
| Bibliographic |     | databases, | including |     | PubMed, | Medline, |     |          |              |     |          |             |     |             |     |
assignedto1ormoremethod(s).
Embase,andScopusweresearchedinApril2021.Thesearch
| query used | was | (“artificial |     | intelligence” |     | OR “machine |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------------ | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Levelofautonomy
| learning” | OR  | “deep learning”) |     | AND | (“clinical |     | decision |     |     |     |     |     |     |     |     |
| --------- | --- | ---------------- | --- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thelevelofautonomywasexaminedusingapreviouslypub-
| support” | OR        | “computer-assisted”) |     |           | AND | (predict* | OR  |                |                |     |       |     |              |       |     |
| -------- | --------- | -------------------- | --- | --------- | --- | --------- | --- | -------------- | -------------- | --- | ----- | --- | ------------ | ----- | --- |
|          |           |                      |     |           |     |           |     | lished 3-level | classification |     | based | on  | how clinical | tasks | are |
| screen*  | ORdiagno* | ORtreat*             |     | OR manag* |     | ORdetect* | OR  |                |                |     |       |     |              |       |     |
dividedbetweentheclinicianandCDS13:
prescri*ORprognosisORtriageORmonitor*)AND(inpa-
tient* OR in-patient OR “clinical setting” OR “hospital 1) Autonomous information: These CDS systems are char-
| setting”            | OR “primary | care”). |                 | Appropriate | vocabulary |            | terms |           |            |              |           |         |      |             |        |
| ------------------- | ----------- | ------- | --------------- | ----------- | ---------- | ---------- | ----- | --------- | ---------- | ------------ | --------- | ------- | ---- | ----------- | ------ |
|                     |             |         |                 |             |            |            |       | acterized | by         | a separation |           | between | what | CDS and     | clini- |
| were included(Table |             | S1),    | andtheretrieval |             | set        | waslimited | to    |           |            |              |           |         |      |             |        |
|                     |             |         |                 |             |            |            |       | cian      | contribute | to           | the task, | where   | CDS  | contributes |        |
articles published in 2016 or later. In addition to the 4 data- information that clinicians can use to make decisions,
bases, we searched ClinicalTrials.gov and manually searched for example, an imaging system provides a colored dis-
| the reference | lists | of the | retrieved | articles | using | a forward- |     |      |            |     |             |            |     |                  |     |
| ------------- | ----- | ------ | --------- | -------- | ----- | ---------- | --- | ---- | ---------- | --- | ----------- | ---------- | --- | ---------------- | --- |
|               |       |        |           |          |       |            |     | play | to enhance |     | clinician’s | perception |     | to differentiate |     |
backwardsnowballingapproach.
|     |     |     |     |     |     |     |     | human         | tissue | images. |     |               |     |            |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ------- | --- | ------------- | --- | ---------- | --- |
|     |     |     |     |     |     |     |     | 2) Assistive: | These  | CDS     | are | characterized |     | by overlap | in  |
Studyselection
|     |     |     |     |     |     |     |     | what | clinician | and | CDS | contribute | to  | the task, | but |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --- | --- | ---------- | --- | --------- | --- |
Thesearchidentifiedatotalof1255studies(Figure1).After where clinicians provide the decision on the task. Such
| removal | of duplicates, | the | title | and abstract |     | of 1111 | articles |         |     |             |        |      |            |     |         |
| ------- | -------------- | --- | ----- | ------------ | --- | ------- | -------- | ------- | --- | ----------- | ------ | ---- | ---------- | --- | ------- |
|         |                |     |       |              |     |         |          | overlap | or  | duplication | occurs | when | clinicians |     | need to |
werescreenedindependentlyby2reviewers(A.P.S.andF.M.) confirm or approve CDS provided information or deci-
to identify relevant studies according to inclusion and exclu- sions; for example, a CDS assists clinicians to detect
sion criteria (Table S2).21 Articles were limited to literature osteoarthritis from a knee X-ray image with a disclaimer
published in commercial bibliographic databases, including that the system should be used in lieu of full patient
| primary | studies | published | over | a 5-year | period | (2016-2021). |     | evaluation. |     |     |     |     |     |     |     |
| ------- | ------- | --------- | ---- | -------- | ------ | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Our search was limited to 5 years as the application of ML- 3) Autonomousdecision:HereCDSprovidesthedecisionfor
based CDS and medical device approvals were mostly since theclinicaltaskwhichcanthenbeenactedbycliniciansor
2016.13,15 Studies aboutsystems notused byhealthcare pro- theCDSitself,forexample,aCDSprovidesscreeningfor
fessionals (ie, consumer facing systems without clinician diabeticretinopathyinprimarypracticewheretheresultis
supervision) or those reporting development or validation of directlyusedasreferraldecisions.
modelsonretrospectivedatasetswereexcluded.Non-English
Todeterminethelevelofautonomy,weexaminedtheCDS
articles and conference abstracts were also excluded leaving task, the stage of human information processing that was
45 studies for further assessment. Full-length articles were CDS,23
|     |     |     |     |     |     |     |     | automated | by the |     | as well | as the | CDS | input and | out- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --- | ------- | ------ | --- | --------- | ---- |
retrievedandassessedindependentlyagainsttheinclusioncri-
put.ThecliniciantaskandCDStaskweresubsequentlycom-
| teria by | 2 reviewers | (A.P.S. | and | F.M.). | Articles | not | meeting |          |        |         |            |        |     |                  |     |
| -------- | ----------- | ------- | --- | ------ | -------- | --- | ------- | -------- | ------ | ------- | ---------- | ------ | --- | ---------------- | --- |
|          |             |         |     |        |          |     |         | pared to | assess | whether | clinicians | needed | to  | verify decisions |     |
the inclusion criteria were excluded and any disagreements provided by the CDS system (assistive) or could rely on the
about inclusion or exclusion of an article were resolved by CDSinformationordecisions(autonomous).Classificationof
consensus.
thestageofautomationandlevelofautonomywasperformed
byA.P.S.andreviewedbyD.L.
Dataextractionandsynthesis
For each included study, descriptive information about the Effectsondecision-making,caredelivery,andpatient
| clinicaltask,caresetting,studydesign,CDSusers,CDStask, |     |        |                 |     |     |          |       | outcomes    |      |          |       |     |             |           |     |
| ------------------------------------------------------ | --- | ------ | --------------- | --- | --- | -------- | ----- | ----------- | ---- | -------- | ----- | --- | ----------- | --------- | --- |
| ML type,                                               | and | method | were extracted. |     | Key | findings | about |             |      |          |       |     |             |           |     |
|                                                        |     |        |                 |     |     |          |       | CDS effects | were | examined | using | an  | established | framework |     |
CDS effects on clinical decision-making, care delivery, and calledtheinformationvaluechain,whichshowsthatmultiple
patient outcomes were also identified. The following data steps are necessary from using ML-based CDS to impacting
wereextracted: patient outcomes including clinicians interacting with CDS

2052 JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12
Figure1.Articlesearchandretrievalprocessflowdiagram.
systems,receivingnewinformationthatthenaltersdecisions, Assistive:CDSassistshumandecisions
the care delivery process, and outcomes.14,24 For instance, a Most studies examined ML-based CDS that were assistive
clinicianmayinteractwithaCDSsystemtoreceiveimportant (n¼23; Table 2). Here clinicians needed to confirm or
new information based on which they decide to implement approve CDS provided information or decisions such as rec-
(decision-making)anintervention(caredelivery)thatleadsto ommendations, alerts, or risk scores for diagnosis or further
changesinthepatient’sclinicalcondition(patientoutcomes). actions. The following sections summarize these studies by
Thus, effects of CDS systems were examined based on theCDStask.
changes in decision-making, care delivery, or patient out-
Riskassessment
comes. When studies did not evaluate these effects, we sum-
marizedtheirkeyfindings. EightstudiesrelatedtoCDSthat assistedcliniciansinassess-
A narrative synthesis then integrated findings into descrip- ingtheriskofcomplicationsduringhospitalization.Ofthese,
tivesummariesforeachlevelofautonomy.Wefocusedonthe 5alertedcliniciansaboutsepsisriskbytextmessageorphone
clinicaltaskassistedbyCDSandreportedeffectsondecision- callprovidingthemwithapredictiveriskscoreforinterpreta-
making,caredelivery,orpatientoutcomes. tion, triggering re-assessment and further action should the
clinician observe heightened risks.27–29,42,43 One study used
the learning health system framework to integrate a deep
Results learningsepsisCDSintoroutinecare.42In2otherstudies,the
Descriptiveanalysisofallstudies majority of clinicians (55-62%) did not change their percep-
tions about sepsis risk and reported no change in care deliv-
We identified 32 studies describing the evaluation of ML-
ery, although few orders were significantly increased such as
based CDS in healthcare settings (Figure 1, Table 1). The
intravenous bolus, hematology, and metabolic blood
majority were prospective cohort studies (n¼18; 56%) or
tests.28,29 However, 2 studies, including 1 RCT by Shimabu-
randomized controlled trials (RCTs) (n¼9; 28%) in
kuroetal.,demonstratedthattheuseofaCDStopredictsep-
secondary-tertiary care settings (n¼29; 91%). Only 14
sisriskshortenedhospitalstayandreducedmortality.27,43
(44%) reported the clinical trial registration. Most studies
Risk of delirium, another complication of hospitalization,
were conducted after 2019 (n¼27; 84%) in high-income
was predicted by 1 CDS using a random forest-based algo-
nations(n¼24;75%;Figure2).
rithm achieving a sensitivity of 74% and a specificity of
Of the 32 studies reviewed, the most common task sup-
82%.32,33 Although most clinicians indicated that the infor-
ported by ML-based CDS was image recognition and inter-
mationaboutdeliriumanditsearlydetectionprovidedbythe
pretation (n¼12; 38%) followed by risk assessment (n¼9;
CDS was useful (n¼47; 68%), only 1 in 3 (33%) reported
28%) where sepsis (n¼5) was the predominant risk to be
usingthesystemandconsideringitsrecommendationsintheir
evaluated (Table 2). Most CDS were based on supervised clinical decisions (19%).32 Another study that compared the
learning (n¼28; 88%) using a wide variety of methods, accuracy of perioperative risk assessment between physicians
includingrandomforest(n¼7)andconvolutionalneuralnet- and CDS found physicians changing their risk-assessment
works (n¼7). While convolutional neural networks were scoreinmorethan75%ofcases(n¼150).26
mainly used for image recognition (n¼6), classic ML meth-
ods such as random forest (n¼4) and gradient boosting Imagerecognitionandinterpretation
(n¼2;Table3)wereutilizedforriskassessment.Asummary ThenextmostcommonCDStaskwasimagerecognitionand
ofthestudiesbythelevelofautonomyoftheCDSisgivenin interpretation (n¼8). Six studies examined polyp detection
thefollowingsections(Table4). during colonoscopy, where CDS assisted clinicians to

JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12 2053
Table1.CharacteristicsofstudiesreportingevaluationofML-basedCDS provideinterpretationreports.Outofthe104potentialpul-
inhealthcaresettings(n¼32). monary cancer nodules flagged by the system, decisions on
|                 |     |     |     |     | 7 cases       | (7%) were  | subsequently |        | corrected | by re-issuing |     |
| --------------- | --- | --- | --- | --- | ------------- | ---------- | ------------ | ------ | --------- | ------------- | --- |
| Characteristics |     |     | n   | %   |               |            |              |        |           |               |     |
|                 |     |     |     |     | results about | clinically | significant  | nodule | requiring | follow-       |     |
Studydesign
|                                        |     |     |     |     | up care.  | Another | CDS that     | assisted | clinicians        | in magnetic |     |
| -------------------------------------- | --- | --- | --- | --- | --------- | ------- | ------------ | -------- | ----------------- | ----------- | --- |
| Experimental,randomizedcontrolledtrial |     |     | 10  | 31  |           |         |              |          |                   |             |     |
|                                        |     |     |     |     | resonance | imaging | segmentation |          | for radiotherapy  |             | was |
| Experimental,nonrandomizedtrial        |     |     | 1   | 3   |           |         |              |          |                   |             |     |
|                                        |     |     |     |     | shown to  | shorten | segmentation | time     | while maintaining |             | the |
| Experimental,cross-overtrial           |     |     | 1   | 3   |           |         |              |          |                   |             |     |
safetyoforgans-at-risk.40
| Observational,prospectivecohort |     |     | 17  | 53  |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Observational,cross-sectional   |     |     | 2   | 6   |     |     |     |     |     |     |     |
Diagnosticassistance
| Mixed-methods |     |     | 1   | 3   |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Yearofpublication Three CDS assisted clinician in diagnosis. A CDS that pro-
2021 8 25 vided a probability score, based on web-based patient ques-
| 2020 |     |     | 13  | 41  |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2019 6 19 tionnaires,predicteddifferentialdiagnosisofvariouspediatric
diseases.31
| 2018 |     |     | 2   | 6   | neuromuscular |     |     | An antibiotic | selection | CDS | used |
| ---- | --- | --- | --- | --- | ------------- | --- | --- | ------------- | --------- | --- | ---- |
2017 2 6 blood and microbiological data to predict the probability of
2016 1 3 bacterialinfection.37TheCDSprovidedrecommendationsfor
| Clinicaltrialregistration |     |     | 14  | 44  |              |                |     |           |          |         |        |
| ------------------------- | --- | --- | --- | --- | ------------ | -------------- | --- | --------- | -------- | ------- | ------ |
|                           |     |     |     |     | prescription | of antibiotics |     | within 72 | hours of | patient | admis- |
Geo-economicsetting
sion.AnotherRCTofaCDSassistingemergencydispatchers
| High-incomecountries(HIC)         |     |     | 24  | 75  |                    |     |             |             |               |              |     |
| --------------------------------- | --- | --- | --- | --- | ------------------ | --- | ----------- | ----------- | ------------- | ------------ | --- |
|                                   |     |     |     |     | in diagnosing      | out | of hospital | cardiac     | arrest        | demonstrated |     |
| Uppermiddle-incomecountries(UMIC) |     |     | 8   | 25  |                    |     |             |             |               |              |     |
|                                   |     |     |     |     | higher sensitivity |     | when        | dispatchers | were assisted | by           | CDS |
| Lowermiddle-incomecountries(LMIC) |     |     | –   | –   |                    |     |             |             |               |              |     |
Low-incomecountries(LIC) – – (85%)comparedtodispatchersalone(77%).25However,this
Clinicalsetting
|                        |     |     |     |     | study observed               | lower | specificity | in              | CDS-assisted | dispatchers |     |
| ---------------------- | --- | --- | --- | --- | ---------------------------- | ----- | ----------- | --------------- | ------------ | ----------- | --- |
| Primarycare            |     |     | 2   | 6   |                              |       |             |                 |              |             |     |
|                        |     |     |     |     | versusdispatchersalone(97.4% |       |             | vs99.6%,P<.001) |              | andno       |     |
| Secondary-tertiarycare |     |     | 29  | 91  |                              |       |             |                 |              |             |     |
differenceindispatchers’decisiontorecognizecardiacarrest.
| Communitycare |     |     | 1   | 3   |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CDStask
Treatmentplanning
| Imagerecognition&interpretation |     |     | 12  | 38  |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Riskassessment 9 28 TwostudiescomparedtheuseofML-basedCDSintreatment
Diagnosticassistance 5 16 planning with conventional techniques. In the first, an ML
Treatmentplanning&critiquing 3 9 algorithm that assisted with planning of prostate cancer bra-
| Processsupportsystem |     |     | 2   | 6   |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CPOE&electronicprescribing 1 3 chytherapywasshowntoshortenplanningtimeandmaintain
levels.36
Evidenceretrieval – – safe dosimetry The second involved computed
Expertlaboratoryinformationsystem – – tomography-guided radiotherapy planning where CDS used
| MLtype                |     |     |     |     | reducedtreatmenttimeandtheradiotherapydoseby42%.44 |          |       |                 |          |     |       |
| --------------------- | --- | --- | --- | --- | -------------------------------------------------- | -------- | ----- | --------------- | -------- | --- | ----- |
| Supervisedlearning    |     |     | 28  | 88  |                                                    |          |       |                 |          |     |       |
| Reinforcementlearning |     |     | 1   | 3   | Processsupport                                     |          |       |                 |          |     |       |
| Unsupervisedlearning  |     |     | –   | –   |                                                    |          |       |                 |          |     |       |
|                       |     |     |     |     | One study                                          | examined | a CDS | that identified | patients | at  | high- |
| Notreported           |     |     | 3   | 9   |                                                    |          |       |                 |          |     |       |
MLmethoda risk for glycemic control and recommended socio-clinical
Supportvectormachine 3 9 interventionstoassistcliniciansinmanagingdiabeticpatients
| Randomforest       |     |     | 7   | 22  |              |      | setting.39 |              |            |          |     |
| ------------------ | --- | --- | --- | --- | ------------ | ---- | ---------- | ------------ | ---------- | -------- | --- |
|                    |     |     |     |     | in a primary | care |            | Undesirably, | clinicians | reported |     |
| Logisticregression |     |     | 2   | 6   |              |      |            |              |            |          |     |
thatthesystemwasunhelpfulinidentifyingtherightinterven-
| Gradientboosting |     |     | 3   | 9   |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tions(medianscore11outof0-100onhelpfulnessscale).
| Convolutionalneuralnetwork |     |     | 7   | 22  |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Artificialneuralnetwork    |     |     | 3   | 9   |     |     |     |     |     |     |     |
CPOE&Electronicprescribing
| (Unspecified)deeplearning |     |     | 3   | 9   |           |           |     |            |       |       |        |
| ------------------------- | --- | --- | --- | --- | --------- | --------- | --- | ---------- | ----- | ----- | ------ |
|                           |     |     |     |     | One study | evaluated | an  | ML-enabled | order | entry | system |
Abbreviations:CDS,clinicaldecisionsupport;CPOE,computerprocessed
|     |     |     |     |     | designed | to provide | both | synchronous | and | asynchronous |     |
| --- | --- | --- | --- | --- | -------- | ---------- | ---- | ----------- | --- | ------------ | --- |
orderentry;ML,machinelearning.
a CDScouldbeassignedto1ormoreMLmethod(s). alertsaboutprescriptionerrorsusingoutlierdetection.41 The
systemwasshowntohavehighaccuracy(85%)andwascon-
|     |     |     |     |     | sidered        | to be clinically | useful | with 43%   | of alerts  | resulting | in  |
| --- | --- | --- | --- | --- | -------------- | ---------------- | ------ | ---------- | ---------- | --------- | --- |
|     |     |     |     |     | the subsequent | modification     |        | of orders. | Clinicians | changed   |     |
distinguish between cancerous adenoma lesions and benign prescriptions in response to system flags about bradycardia,
polyps.30,34,35,38,46,47Ofthese,5RCTsdemonstratedsuperi- elevatedliverfunctiontests,andhypotension.
| ority of CDS | in assisting clinicians.30,34,38,46,47 |     | CDS-assisted |     |     |     |     |     |     |     |     |
| ------------ | -------------------------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Autonomousinformation:CDSprovides
| colonoscopywas | found to increasethe | adenoma | finding | rate |     |     |     |     |     |     |     |
| -------------- | -------------------- | ------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
leading to better clinical outcomes. In another prospective informationtomakedecisions
study, the real-world performance of a colonoscopy image Only 2 studies examined ML-based CDS that contributed
recognition system was shown to be comparable to expert information for clinicians to make decisions. In the first, a
gastroenterologists.35 CDSthatprovidedanobjectivepredictionofthepatient’sdry
Another study evaluated a radiology double reading sys- weight for hemodialysis prescription was shown to be effec-
tem whereby a CDS was used to detect discrepancies tive in lowering or stopping antihypertensive treatments in
between CT scans and the interpretation reports provided 29% of cases compared to a subjective estimation by clini-
by radiologists.45 Here, the CDS combined ML algorithms cians.49 The second study examined use of a CDS that pro-
with natural language processing to process lung CTs and vided body mass index (BMI) prediction based on 190

2054 JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12
Figure2.Geographicaldistributionoftheincludedstudies.
Table2.IncludedstudiesbyCDStaskandlevelofsystemautonomy.13
|         |     | Levelofautonomy                 |     | Assistive |     | Autonomous  |     |     | Autonomous |     | Total |
| ------- | --- | ------------------------------- | --- | --------- | --- | ----------- | --- | --- | ---------- | --- | ----- |
|         |     |                                 |     |           |     | information |     |     | decision   |     |       |
| CDStask |     | Imagerecognition&interpretation |     | 8         |     | –           |     |     | 4          |     | 12    |
|         |     | Riskassessment                  |     | 8         |     | –           |     |     | 1          |     | 9     |
|         |     | Diagnosticassistance            |     | 3         |     | 1           |     |     | 1          |     | 5     |
|         |     | Treatmentplanning               |     | 2         |     | 1           |     |     | –          |     | 3     |
|         |     | Processsupportsystem            |     | 1         |     | –           |     |     | 1          |     | 2     |
|         |     | CPOE&electronicprescribing      |     | 1         |     | –           |     |     | –          |     | 1     |
|         |     |                                 |     | 23        |     | 2           |     |     | 7          |     | 32    |
Abbreviations:CDS,clinicaldecisionsupport;CPOE,computerizedproviderorderentry.
Table3.IncludedstudiesbyMLmethodandCDStask.
|          |                            | CDStask | CPOE&         | Diagnostic |     | Treatment | Risk       | Process |     | Image       | Total |
| -------- | -------------------------- | ------- | ------------- | ---------- | --- | --------- | ---------- | ------- | --- | ----------- | ----- |
|          |                            |         | e-prescribing | assistance |     | planning  | assessment | support |     | recognition |       |
| MLmethod | Supportvectormachine       |         | –             |            | 2   | –         | –          |         | –   | 1           | 3     |
|          | Randomforest               |         | –             |            | 2   | –         | 4          |         | –   | 1           | 7     |
|          | Logisticregression         |         | –             |            | 2   | –         | –          |         | –   | –           | 2     |
|          | Gradientboosting           |         | –             |            | 1   | –         | 2          |         | –   | –           | 3     |
|          | Convolutionalneuralnetwork |         | –             |            | –   | 1         | –          |         | –   | 6           | 7     |
|          | Artificialneuralnetwork    |         | –             |            | 2   | –         | 1          |         | –   | –           | 3     |
|          | Unspecifieddeeplearning    |         | –             |            | 1   | –         | –          |         | –   | 2           | 3     |
Abbreviations:CDS,clinicaldecisionsupport;CPOE,computerizedproviderorderentry.
variablesrelatedtogenetic,social,diet,andotherriskfactors, CDS. A CDS which processed clinical dermatology photo-
identifying4importantpredictivevariablesforearlyinterven- graphs to distinguish between fungal onychomycosis and
tion in childhood obesity and predicting disease risk, includ- noninfectiousonychodystrophywasfoundtoreduceprescrip-
ing nutri-status perception, energy expenditure, mother’s tionsforunnecessaryantifungalmedications.52Anotherstudy
BMI,andfather’sBMI.48
|     |     |     |     |     | involving | an RCT | with | 300 patients | examined | the | diagnosis |
| --- | --- | --- | --- | --- | --------- | ------ | ---- | ------------ | -------- | --- | --------- |
images.53
|     |     |     |     |     | of childhood |     | cataract based | on  | anterior | ocular |     |
| --- | --- | --- | --- | --- | ------------ | --- | -------------- | --- | -------- | ------ | --- |
Autonomousdecision:CDSdecidesinplaceof
Here,theCDSprovidedrecommendationsforsurgeryorcon-
human servative follow-up based on the diagnosis. Although real-
Seven studies examined ML-based CDS that provided deci- world performance was degraded compared to expert clini-
sions for clinical tasks that could be enacted by clinicians. cians, patients managed in the CDS group reported faster
Four of these involved image recognition and interpretation service (2.79 vs 8.53 minutes, P<.001) and better

Table4.StudiesreportingevaluationofML-basedCDSinclinicalsettingsgroupedbythelevelofautonomy(n¼32).
AuthorCountry Clinicaltask Caresetting;study CDSusers CDStask1 Stageofhuman Effectsondecision-making,caredeliv-
design information eryandpatientoutcomes,orotherkey
processing23 findings
Assistive:CDSassistshumandecisions(n523)
Blombergetal.(2021)25 Identifyingpatientssus- Secondary-tertiarycare; Emergencydispatchers, Diagnosticassistance Decisionselection Decision:Nosignificantdifferencein
Denmark pectedofoutsideof experimentalrandom- Emergencyphysicians dispatchers’decisiontorecognize
hospitalcardiacarrest izedcontrolledtrial cardiacarrest.PerformanceofCDS-
inemergencyphone assisteddispatchersversusdispatch-
calls ersalone:sensitivity(85%vs78%,
P<.001)andspecificity(97%vs
100%)
Brennanetal.(2019)26 Riskassessmentfor6 Secondary-tertiarycare; Surgeons, Riskassessment Decisionselection Decision:Physicianschangedtheir
UnitedStates postoperative experimentalnon- anesthesiologists risk-assessmentscoreinmorethan
complications randomizedtrial 75%cases(n¼150)
Burdicketal.(2020)27 Predictingsepsisinhos- Secondary-tertiarycare; Doctors/CriticalCare Riskassessment Decisionselection Outcomes:Decreasedhospitalmortal-
UnitedStates pitalizedpatientsand observationalpro- ityby39.5%,hospitallengthofstay
providingalertsto spectivecohort by32.3%,and30-dayreadmission
clinician rateforsepsis-relatedpatientsby
22.7%
Gianninietal.(2019)28 Predictingsepsisinhos- Secondary-tertiarycare; Doctors/CriticalCare Riskassessment Informationanalysis Care:Slightincreaseinlactatetest-
UnitedStates pitalizedpatientsand observationalpro- ing,administrationofIVfluid
providingalertsto spectivecohort boluses,andbloodtest(complete
clinician bloodcountandmetabolicpanel)
Outcomes:ShorteningtimetoICU
transfer.Nosignificanteffecton
hospitallengthofstayand
mortality
Ginestraetal.(2019)29 Predictingsepsisinhos- Secondary-tertiarycare; Nursesanddoctors Riskassessment Decisionselection Decision:Majorityofclinicians
UnitedStates pitalizedpatientsand observationalpro- (55%nursesand62%providers)
providingalertsto spectivecohort reportednochangeinperception
clinician ofthepatient’sriskforsepsis
Care:Someclinicians(30%nurses
and9%providers)reported
changeofcareuponalertfrom
CDS
Gongetal.(2020)30 Detectingcolonoscopy Secondary-tertiarycare; Gastroenterologist/ Imagerecognition& Informationanalysis Outcomes:Increasedadenomadetec-
China insertion-withdrawal experimentalrandom- Endoscopist interpretation tionrateoverthecontrolgroup
timeandendoscope izedcontrolledtrial (oddsratio2.30,95%CI1.40–
slippingtoaidclini- 3.77;P¼.0010)
ciandistinguish
betweenadenomatous
colorectalcancerand
benignpolyps
Grigulletal.(2016)31 Diagnosingneuromus- Secondary-tertiarycare; Primarycarephysicians Diagnosticassistance Decisionselection Realworldaccuracyreached89%in
Germany culardiseases(7diag- observationalpro- diagnosingdifferentneuromuscular
nosis)basedon spectivecohort diseases
questionnaire
responses
(continued)
JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12
2055

Table4.(continued)
AuthorCountry Clinicaltask Caresetting;study CDSusers CDStask1 Stageofhuman Effectsondecision-making,caredeliv-
design information eryandpatientoutcomes,orotherkey
processing23 findings
Jauketal.(2021)32 Predictingtheriskof Secondary-tertiarycare; Physiciansandnurses Riskassessment Decisionselection Decision:Majorityofclinicianagreed
Austria deliriumamonghos- mixed-method thattheCDSprovidedadditional
pitalizedpatients information(68%),butonly19%
consideredtheoutputofCDSin
clinicaldecisionsand33%usedthe
CDSregularly
Jauketal.(2020)33 Predictingtheriskof Secondary-tertiarycare; Physiciansandnurses Riskassessment Decisionselection CDSperformedwithsensitivityof
Austria deliriumamonghos- observationalpro- 74%andspecificityof82%
pitalizedpatients spectivecohort Care:High-riskpatientobtained
nonpharmacologicalpreventive
treatment(eg,reinforcementofvis-
ualandhearingaids,hydration,
sleeptimemanagement,clear
communication).
Liuetal.(2020)34 Detectingpolypsin Secondary-tertiarycare; Gastroenterologists/ Treatmentplanning Decisionselection Outcomes:Increaseinadenomadetec-
China colonoscopyanddis- experimentalrandom- Endoscopists &critiquing tionrateversusthecontrolgroup
tinguishingbetween izedcontrolledtrial (39%vs24%,P<.001)
adenomatouscolorec-
talcancerandbenign
polyps
Morietal.(2020)35 Detectingpolypsin Secondary-tertiarycare; Gastroenterologists/ Imagerecognition& Decisionselection Inclinicalsetting,CADperformedas
Japan colonoscopyanddis- observationalpro- Endoscopist interpretation goodasexpertgastroenterologistin
tinguishingbetween spectivecohort distinguishingbetweenadenoma-
adenomatouscolorec- touscolorectalcancerandbenign
talcancerandbenign polyps.NPV¼96%
polyps
Nicolaeetal.(2020)36 Planningtreatmentfor Secondary-tertiarycare; Urologists Imagerecognition& Informationanalysis Care:Shorterplanningmeanplan-
Canada low-dose-ratebrachy- experimentalrandom- interpretation ningtimeforthePIPAarm
therapytobeinput izedcontrolledtrial (2.38þ0.96minutes)compared
intoaTreatment withtheconventional
PlanningSystem (43.13þ58.70minutes)P(cid:2).05
(TPS) Outcomes:Excellentsafetybythe
CDSwithnosignificantdifferences
wasobservedinpreimplantorday
30dosimetry
Rawsonetal.(2018)37 Diagnosingacommun- Secondary-tertiarycare; Physicians Diagnosticassistance Decisionselection Care:Orderingmicrobiologicallabo-
UnitedKingdom ity-acquiredbacterial observationalpro- ratorytestsforindividualswithhigh
infectionwithin72 spectivecohort possibilityofbacterialinfection
hoursofadmission, priortoantibioticprescription
leadingtodecisionof
antibioticprescription
Repicietal.(2020)38 Detectingpolypsin Primarycare;experi- Gastroenterologists/ Processsupport Informationanalysis Outcomes:Increaseinadenomadetec-
Italy colonoscopyanddis- mentalrandomized Endoscopists system tionrateoverthecontrolgroup
tinguishingbetween controlledtrial (55%vs40%,P<.001)
adenomatouscolorec-
talcancerandbenign
polyps
(continued)
2056
JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12

JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12
Table4.(continued)
CDStask1
AuthorCountry Clinicaltask Caresetting;study CDSusers Stageofhuman Effectsondecision-making,caredeliv-
|     | design |     | information | eryandpatientoutcomes,orotherkey |
| --- | ------ | --- | ----------- | -------------------------------- |
processing23
findings
Romero-Brufauetal.(2020)39 Predictinghighglycemic Primarycare;observa- Primarycarephysicians, CPOE&electronic Informationanalysis Care:Clinicianfeltthatcarewasbetter
UnitedStates riskinpatientwith tionalcross-section registerednurses, prescribing coordinated(P<.001)
| diabetesandprovid- |     | licensedpractical    |     |     |
| ------------------ | --- | -------------------- | --- | --- |
| ingrecommendation  |     | nurses,socialworkers |     |     |
Savenijeetal.(2020)40 Segmentingorgans-at- Secondary-tertiarycare; Radiotherapists Imagerecognition& Informationanalysis FasterinferencetimebyCDScom-
Netherlands riskforprostate observationalpro- interpretation paredtoconventionalmethods(14
radiotherapywhile spectivecohort minutesvs60seconds)whilemain-
| manualsegmentation |     |     |     | taininggoodperformancebydice       |
| ------------------ | --- | --- | --- | ---------------------------------- |
| istimeconsuming    |     |     |     | similaritycoefficient(0.92-0.98for |
variousorgans)
Segaletal.(2019)41 Preventingprescription Secondary-tertiarycare; Physicians Riskassessment Decisionselection Decision:43%ofthealertscaused
Israel errorbasedon observationalpro- changesinsubsequentmedical
| irregularities | spectivecohort |     |     | orders,39%oftheerroneousmedi- |
| -------------- | -------------- | --- | --- | ----------------------------- |
cationordersweremodifiedduring
theorderofmedication(synchro-
nousflags),and61%weremodified
duringmonitoringphase(asynchro-
nousflags)followingachangein
clinicalindicators
Sendaketal.(2020)42 Predictingsepsisinhos- Secondary-tertiarycare; Intensivists,emergency Riskassessment Decisionselection Learninghealthsystemframework
UnitedStates pitalizedpatientsand observationalpro- departmentclinicians, wasusedtointegratesystemtorou-
| providingalertsto | spectivecohort | rapidresponseteam, |     | tinecare |
| ----------------- | -------------- | ------------------ | --- | -------- |
| clinicians        |                | nurses             |     |          |
Shimabukuroetal.(2017)43
Predictingsepsisinhos- Secondary-tertiarycare; Criticalcaredoctors Riskassessment Informationanalysis Outcomes:Decreasedlengthofstay
UnitedStates pitalizedpatientsand experimentalrandom- from13.0to10.3days(P¼.042).
providingalertsto izedcontrolledtrial Decreasedin-hospitalmortalityby
| clinicians |     |     |     | 12%(P¼.018) |
| ---------- | --- | --- | --- | ----------- |
Siboltetal.(2021)44 Generatingpre-treat- Secondary-tertiarycare; Radiotherapists Treatmentplanning Decisionselection Care:Patientsobtainedfastertreat-
Denmark mentplansforadap- observationalpro- &critiquing mentadaptiveCDSwithmedian
| tiveguided          | spectivecohort |     |     | durationof17.6minutesfrom      |
| ------------------- | -------------- | --- | --- | ------------------------------ |
| radiotherapyinblad- |                |     |     | preparationtotreatmentdelivery |
| dercancer           |                |     |     | Outcomes:AdaptiveCDSreduced    |
high-doseplanningtargetvolume
inbladderby42%comparedto
thescheduledconventional
technique
Tanetal.(2021)45 Recognizingpulmonary Secondary-tertiarycare; Radiologists,patient Imagerecognition& Informationanalysis Decision:Sevencasesof104flagged
Singapore nodulesinCTscanas observationalpro- safetyofficers interpretation imagesweredeemedclinicallysig-
| adoublereadsafety | spectivecohort |     |     | nificantandclinicianswere  |
| ----------------- | -------------- | --- | --- | -------------------------- |
| system            |                |     |     | informedtochangesubsequent |
management
(continued)
2057

2058
Table4.(continued)
CDStask1
AuthorCountry Clinicaltask Caresetting;study CDSusers Stageofhuman Effectsondecision-making,caredeliv-
|     | design |     | information | eryandpatientoutcomes,orotherkey |
| --- | ------ | --- | ----------- | -------------------------------- |
processing23
findings
Wangetal.(2019)46 Detectingpolypsin Secondary-tertiarycare; Gastroenterologists/ Imagerecognition& Informationanalysis Outcomes:Increasedadenomadetec-
China colonoscopyanddis- experimentalrandom- Endoscopists interpretation tionrateversusthecontrolgroup
| tinguishingbetween | izedcontroltrial |     |     | (29%vs20%,P<.001) |
| ------------------ | ---------------- | --- | --- | ----------------- |
adenomatouscolorec-
talcancerandbenign
polyps
Wangetal.(2020)47 Detectingpolypsin Secondary-tertiarycare; Gastroenterologists/ Imagerecognition& Informationanalysis Outcomes:Decreasedinadenoma
China colonoscopyanddis- observationalperspec- Endoscopists interpretation missrateversusthecontrolgroup
| tinguishingbetween | tivecohort |     |     | (14%vs40%,P<.0001) |
| ------------------ | ---------- | --- | --- | ------------------ |
adenomatouscolorec-
talcancerandbenign
polyps
Autonomousinformation:CDSprovidesinformationtomakedecisions(n52)
Marcos-Paseroetal.(2021)48
Calculatingpredicted Community;observatio- Clinicalnutritionists Diagnosticassistance Informationanalysis Thisstudycollectedinformationby
Spain bodymassindex nalcross-section self-questionnaire.Fivetoppredic-
| (BMI)topredictchild- |     |     |     | torswerenutritionperception,dif- |
| -------------------- | --- | --- | --- | -------------------------------- |
| hoodobesityandgive   |     |     |     | ferencebetweenenergyintakeand    |
JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12
| earlyintervention |     |     |     | expenditure,father’sBMI,mother’s |
| ----------------- | --- | --- | --- | -------------------------------- |
BMI,andmother’smeals
Nieletal.(2018)49 Estimatingdryweightin Secondary-tertiarycare; Nephrologists Treatmentplanning Informationanalysis Care:discontinuationordecreasein
France hemodialysispatient experimentalcross- &critiquing antihypertensiveprescription.
toavoidsideeffectsof overtrial Outcomes:significantdecreasein
| hypertensiondueto |     |     |     | systolicbloodpressureorbetter |
| ----------------- | --- | --- | --- | ----------------------------- |
| underestimationor |     |     |     | hypertensioncontrol.          |
overestimationofdry
weight
Autonomousdecision:CDSdecidesinplaceofhuman(n57)
Chenetal.(2020)50 Decidingwhetherto Secondary-tertiarycare; Physicians Processsupport Decisionselection Care:Weeklycountsofshinglesvacci-
UnitedStates acceptorignorealerts observationalpro- system nationremainedstableafteractiva-
andfollowingupwith spectivecohort tionofsuppressionsystemversus
| shinglesvaccination |     |     |     | controlgroup(326.3vs331.3, |
| ------------------- | --- | --- | --- | -------------------------- |
P¼.38).
Isma’eeletal.(2017)51
Predictingthepresence Secondary-tertiarycare; Cardiologists,primary Riskassessment Decisionselection Decision:Changephysician’sdeci-
Lebanon ofcardiacischemia observationalpro- carephysicians siontoperformdownstreamstress
|     | spectivecohort |     |     | testing. |
| --- | -------------- | --- | --- | -------- |
CDSperformedbetterthanconven-
tionalriskmodelwithhigherdis-
criminatorypower1.61,NPV
98%,sensitivity91%
Kimetal.(2020)52 Diagnosingonychomy- Secondary-tertiarycare; Dermatologists,other Imagerecognition& Decisionselection Decision:Changephysician’sprescrip-
SouthKorea cosisbyclinicalpho- observationalpro- physicians interpretation tionofantifungalmedication(82%)
| tograph,leadingto | spectivecohort | (nondermatologist) |     |     |
| ----------------- | -------------- | ------------------ | --- | --- |
decisionofantifungal
prescription
(continued)

JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12
Table4.(continued)
AuthorCountry Clinicaltask Caresetting;study CDSusers CDStask1 Stageofhuman Effectsondecision-making,caredeliv-
|     | design | information | eryandpatientoutcomes,orotherkey |
| --- | ------ | ----------- | -------------------------------- |
processing23 findings
Linetal.(2019)53 Diagnosingchildhood Secondary-tertiarycare; Ophthalmologists,pri- Imagerecognition& Decisionselection Fastertimeinreceivingdiagnosisby
China cataract,providing experimentalrandom- marycarephysicians interpretation CDS(2.79minutes)comparedto
comprehensiveevalu- izedcontrolledtrial experts(8.52minutes),P<.001
| ationofthedisease, |     |     | CDShadinferioraccuraciescom-   |
| ------------------ | --- | --- | ------------------------------ |
| andrecommending    |     |     | paredtoexperts,bothindetermin- |
| optionofsurgery    |     |     | ingcataractdiagnosis(87%)and   |
treatmentrecommendation(71%)
Wintjensetal.(2020)54
DiagnosingCOVID-19 Secondary-tertiarycare; Physicians Diagnosticassistance Decisionselection TheCDSdemonstratedrealworldsen-
Netherlands byrecognizingthe observationalpro- sitivityof86%andNPVof92%to
patternofvolatile spectivecohort beusedastriagetoolforpatients
| organiccompound |     |     | undergoelectedsurgery |
| --------------- | --- | --- | --------------------- |
fromabreathana-
lyzertoexclude
infectedpatientsfor
electedsurgery
Xiao(2021)55 Diagnosinghepatobili- Secondary-tertiarycare; Ophthalmologists,hepa- Imagerecognition& Decisionselection TheROCwere0.93(0.91-0.94)for
China arydiseasesusing observationalpro- tobiliarysurgeons interpretation slitlampand0.68forfundusimages
| ocularimages | spectivecohort |     |     |
| ------------ | -------------- | --- | --- |
Yaoetal.(2021)56
Identifyingpatientswith Primarycare;experi- Primarycarephysicians Imagerecognition& Decisionselection Outcomes:Increasediagnosisoflow
UnitedStates ventriculardysfunc- mentalrandomized interpretation ejectionfractionwithin90daysof
| tiontorecommend      | controlledtrial |     | theECG(2.1%ininterventionarm |
| -------------------- | --------------- | --- | ---------------------------- |
| forfurthersupporting |                 |     | vs1.6%incontrolgroupOR1.32   |
| examination          |                 |     | P¼.007)                      |
Abbreviations:CDS:clinicaldecisionsupport;CPOE:computerizedproviderorderentry;CT:computedtomography;ECG:electrocardiogram;NPV:negativepredictivevalue;ROC:receivingoperating
characteristic.
2059

2060 JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12
satisfaction. The third study demonstrated real-world per- usedbycliniciansaswell astheireffectsondecision-making,
formanceofaCDStoscreenpatientsfor7hepatobiliarydis- caredelivery,andpatientoutcomes.
easesbasedonchangesineyeappearanceandcolorusingslit
lamp and fundus images (AUC¼0.74).55 The fourth study ClinicaldecisionsassistedbyCDS
involved a CDS that identified ventricular dysfunction from The level of autonomy determines how clinicians interact
analysisofelectrocardiogram(ECG)imagesandwasfoundto withanduseCDS.Ourfindingsareconsistentwiththe find-
maintainreferralsrateforechocardiography(18%controlvs ings of previous reviews of ML-based medical devices13 and
19% CDS intervention, P¼.17), while increasing the case nursingCDS58whichfoundthatmostcontemporarysystems
| findingatthesametime(oddsratio¼1.32;P¼.007).56 |     |     |     |     |     |     |     | wereassistive. |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
The fifth study evaluated a CDS that automated referrals Only 1 in 4 studies (26%) examined effects on decision-
for costly stress test and noninvasive imaging based on the making which were mixed. While 3 studies demonstrated
risk of cardiac ischemia from clinical data.51 The CDS was improvements with the use of assistive CDS,26,41,45 3 others
|     |     |     |     |     |     |     |     | found no | improvement.25,29,32 |     |     | Although | such | observational |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------------- | --- | --- | -------- | ---- | ------------- | --- |
showntoperformbetterthanaconventionalriskmodelwith
|           |           |     |                |     |       |          |     | studies | provide | an opportunity |     | to examine |     | effects | in real- |
| --------- | --------- | --- | -------------- | --- | ----- | -------- | --- | ------- | ------- | -------------- | --- | ---------- | --- | ------- | -------- |
| potential | to reduce | 59% | of unnecessary |     | tests | (n¼486). | The |         |         |                |     |            |     |         |          |
sixthstudy related toa CDSthatautomated the diagnosisof world settings, controlled experiments which enable patient-
COVID-19 to screen patients for elective surgery.57 The sys- and risk-free evaluation are useful to better understand spe-
cificeffectsondecision-making.59
| tem utilized | biosensors |              | for breath  | analysis | and     | was | demon-   |            |           |           |     |      |           |         |     |
| ------------ | ---------- | ------------ | ----------- | -------- | ------- | --- | -------- | ---------- | --------- | --------- | --- | ---- | --------- | ------- | --- |
|              |            |              |             |          |         |     |          | Clinicians | typically | integrate |     | many | different | sources | of  |
| strated      | to have    | a real-world | sensitivity |          | of 0.86 | and | negative |            |           |           |     |      |           |         |     |
informationincludingCDSadvicetomakedecisions.60Inthis
| predictive | value | of 0.92. | The | final study | examined |     | CDS to |     |     |     |     |     |     |     |     |
| ---------- | ----- | -------- | --- | ----------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
suppress irrelevant alerts from another CDS about shingles context,assistiveCDSmayoftenrequireclinicianstoconsider
vaccination.50TheCDSdeploymentwasabletoreduce44% “black-box” CDS advice against their own decisions. For
|                  |     |        |                |     |         |             |     | instance,   | when | predicting | the        | risk of | surgical      | complications, |        |
| ---------------- | --- | ------ | -------------- | --- | ------- | ----------- | --- | ----------- | ---- | ---------- | ---------- | ------- | ------------- | -------------- | ------ |
| of inappropriate |     | alerts | and maintained |     | similar | vaccination |     |             |      |            |            |         |               |                |        |
|                  |     |        |                |     |         |             |     | to validate | CDS  | advice     | clinicians | must    | independently |                | assess |
counts.
|     |     |     |     |     |     |     |     | risk based | on  | history taking, |     | physical | examination, |     | labora- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------------- | --- | -------- | ------------ | --- | ------- |
EffectsofML-basedCDSondecision-making,care tory results, and other supporting examinations on top of
CDS.26
delivery,andclinicaloutcomes using the Such a double up in the clinical workflow
|     |     |     |     |     |     |     |     | may require | more | time | and delay | decisions, |     | especially | if the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ---- | --------- | ---------- | --- | ---------- | ------ |
Only8studies(25%)examinedtheeffectsofML-basedCDS
|                    |     |     |            |          |     |           |       | clinician’s | decision | does | not agree | with | the CDS, | potentially |     |
| ------------------ | --- | --- | ---------- | -------- | --- | --------- | ----- | ----------- | -------- | ---- | --------- | ---- | -------- | ----------- | --- |
| on decision-making |     | in  | healthcare | settings |     | reporting | mixed |             |          |      |           |      |          |             |     |
increasingriskstopatientsafety.61
| results. | Of these, | 5 reported | benefits | and | improvements |     | in a |     |     |     |     |     |     |     |     |
| -------- | --------- | ---------- | -------- | --- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
assessment,26 Still, early demonstration of benefits supports the use of
| variety    | of decisions | including | surgery                |     | risk |          | new  |           |              |              |           |        |               |     |         |
| ---------- | ------------ | --------- | ---------------------- | --- | ---- | -------- | ---- | --------- | ------------ | ------------ | --------- | ------ | ------------- | --- | ------- |
|            |              |           |                        |     |      |          |      | assistive | CDS in       | clinical     | settings. | Of the | 23 studies    | we  | exam-   |
| clinically | significant  | CT        | scan interpretation,45 |     |      | reducing | fur- |           |              |              |           |        |               |     |         |
|            |              |           |                        |     |      |          |      | ined, 5   | demonstrated | improvements |           | in     | care delivery |     | such as |
therexaminations,51andbetterprescriptiondecisions.41,52In
increasingpreventiveordersinhigh-riskpatients,28,37shorter
| the other | 2 studies, | CDS | implementation |     | did | not | influence |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | -------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
timetotreatment,36,44andimprovedcarecoordination.39Six
diagnosticsofcardiacarrest25aswellaspredictingriskofsep-
|                     |     |                           |     |     |     |      |       | studies               | showed | enhanced | patient  | outcomes   | including |          | higher   |
| ------------------- | --- | ------------------------- | --- | --- | --- | ---- | ----- | --------------------- | ------ | -------- | -------- | ---------- | --------- | -------- | -------- |
| sis29anddelirium.32 |     |                           |     |     |     |      |       | finding,30,34,38,46   |        |          |          |            |           |          |          |
|                     |     |                           |     |     |     |      |       | case                  |        | shorter  |          | hospital   | length    | of stay, | and      |
| Theeffectsof        |     | ML-basedCDSoncaredelivery |     |     |     | were | exam- |                       |        |          |          |            |           |          |          |
|                     |     |                           |     |     |     |      |       | lower mortality.27,43 |        | Such     | benefits | strengthen |           | the      | case for |
inedin10studies(31%).Patientspredictedtobeathighrisk
usingthesesystemsandarelikelytoincreaseimplementation.
| of hospital | complications |     | were | given | more | aggressive | treat- |     |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | ---- | ----- | ---- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ments. Patients with high-risk bacterial infection and sepsis TaskssupportedbyML-basedCDS
| prediction | were  | ordered     | more               | blood | tests and | administered |     |           |               |     |                    |            |     |         |          |
| ---------- | ----- | ----------- | ------------------ | ----- | --------- | ------------ | --- | --------- | ------------- | --- | ------------------ | ---------- | --- | ------- | -------- |
|            |       |             |                    |       |           |              |     | Different | to rule-based | CDS | that               | are mostly |     | focused | on sup-  |
| more IV    | fluid | bolus.28,37 | Nonpharmacological |       |           | preventive   |     |           |               |     |                    |            |     |         |          |
|            |       |             |                    |       |           |              |     | porting   | prescribing   | and | care reminders,7,8 |            | we  | found   | that the |
treatments, such as hydration and sleep management, were most common task supported by ML-based CDS was in
giventohigh-riskdeliriumpatients.32,33UseofCDSintreat-
|               |     |          |       |           |      |     |         | image recognition |       | and interpretation |       | followed  |     | by risk | assess-  |
| ------------- | --- | -------- | ----- | --------- | ---- | --- | ------- | ----------------- | ----- | ------------------ | ----- | --------- | --- | ------- | -------- |
| ment planning |     | was also | shown | to reduce | time | and | improve |                   |       |                    |       |           |     |         |          |
|               |     |          |       |           |      |     |         | ment. This        | shift | in clinical        | tasks | supported | by  | CDS     | could be |
carecoordination.36,39,44However,in1studythatevaluated
attributedtothewideavailabilityofdeeplearningMLmeth-
a CDS to predict sepsis, no changes were observed in the 12 ods such as convolutional neural networks34,38,40,52,53,56 as
outof15careprocessmeasuresassessed.29
|     |     |     |     |     |     |     |     | well as | the large | amounts        | of standardized |        | data   | readily | avail-  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | -------------- | --------------- | ------ | ------ | ------- | ------- |
|     |     |     |     |     |     |     |     | able in | imaging   | and electronic |                 | health | record | data    | in risk |
Discussion assessment. For instance, a CDS for sepsis risk assessment
|     |     |     |     |     |     |     |     | wastrainedwithdatafrom684443encountersover5 |     |     |     |     |     |     | years |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
Despite rapid growth in the development of ML-based CDS, from across 6 institutions.27,62 While rule-based CDS have
few studies have evaluated these CDS in clinical settings to been shown to improve care delivery (57%) and patient out-
examine their effects on decision-making, care delivery, or comes (30%) especially in drug ordering and preventive
patientoutcomes.WefoundthatmostCDSevaluatedinclini- care,7theeffectsofML-basedCDSweremixed.
calsettingswereassistive(n¼23),requiringclinicianstocon-
EvaluatingML-basedCDSinclinicalsettings
firmorapproveCDSprovidedinformationordecisions,and
where the responsibility for the final decision generally rests Moststudiesinthisreviewcomewithhighlevelsofheteroge-
with the clinician. The most common use of assistive CDS neity in outcome measures making comparison difficult. We
wasinriskassessmentforsepsis27–29,42,43andforinterpreting
observedmanydifferentstudydesignsrangingfromRCTsto
colonoscopy.30,34,35,38,46,47
cancerous lesions in While ML- qualitativeinterviews,usingawidevarietyofoutcomemeas-
based CDS are being applied in many clinical areas, further urestoexamineeffectsondecision-making,caredelivery,and
observationalstudiesarerequiredtounderstandhowtheyare patientoutcomes.Thereportingofevaluationstudiesislikely

JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12 2061
to improve with recent publication of reporting standards, considerable heterogeneity in the study designs and outcome
such as DECIDE-AI for early-stage clinical evaluation63 and measures which prevented quantitative examination of the
CONSORT/SPIRIT-AIforlargerclinicaltrials.64,65 effects on decision-making, care delivery, and patient
Onlyafewofthestudieswereviewedexaminedeffectson
outcomes.
decision-making(25%),caredelivery(31%),andclinicalout-
| comes (38%). | To  | that | end | we have | demonstrated | the | use of |     |     |     |     |     |     |     |
| ------------ | --- | ---- | --- | ------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Conclusion
| 2 frameworks. |     | The first | is  | the level | of autonomy, |     | a 3-level |     |     |     |     |     |     |     |
| ------------- | --- | --------- | --- | --------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
classificationbasedonhowclinicaltasksaredividedbetween ML-basedCDSarebeingappliedinavarietyofclinicalareas,
theclinicianandCDSthatallowsexaminationofthespecific
butevaluationoftheireffectsondecision-making,caredeliv-
tasks.13
role of the CDS in clinical The second is an estab- ery,andpatientoutcomesislimited.Thereremainopportuni-
lished information value chain framework, which separates ties to evaluate the feasibility of using ML-based CDS in
| the multiple      | steps | from | system | use       | to impacting | clinical         | out- |                    |     |            |                         |     |           |     |
| ----------------- | ----- | ---- | ------ | --------- | ------------ | ---------------- | ---- | ------------------ | --- | ---------- | ----------------------- | --- | --------- | --- |
|                   |       |      |        |           |              |                  |      | clinical settings, |     | especially | in resource-constrained |     | contexts, |     |
| comes—interacting |       | with | CDS,   | receiving |              | new information, |      |                    |     |            |                         |     |           |     |
tosupportclinicaldecisionswherethereisalackofspecialist
decision-making,andcaredelivery.9Werethesetobeusedas
expertiseandsophisticatedmedicalequipment.
| standard | templates | in  | future | studies, | it would | be possible | to  |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------ | -------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
makecomparativeassessmentsbetweenstudies.
There is also a need to examine the actual use of CDS by Acknowledgments
cliniciansintherealworld.Noneofthestudiesexaminedpat-
WewishtoacknowledgetheinvaluablecontributionsofYing
ternsofuse,andonly10(31%)reportedthenumberofclini-
|                              |     |     |     |             |     |                  |     | Wang, who | is providing | technical | advice | about | ML methods |     |
| ---------------------------- | --- | --- | --- | ----------- | --- | ---------------- | --- | --------- | ------------ | --------- | ------ | ----- | ---------- | --- |
| cians involvedinevaluations. |     |     |     | Thenumberof |     | clinicians,their |     |           |              |           |        |       |            |     |
andtheirapplications.
| expertise, | and      | experience | with   | CDS | are important |              | variables |     |     |     |     |     |     |     |
| ---------- | -------- | ---------- | ------ | --- | ------------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| affecting  | adoption | and        | use.63 | To  | that end,     | mixed-method |           |     |     |     |     |     |     |     |
studiesareparticularlyvaluabletomeasureactualuseandto Authorcontributions
understandfactorsaffectingacceptanceofMLsystems.32
A.P.S.conceivedthisstudy,designed,andconductedtheanal-
ML-basedCDSinresource-constrainedsettings ysis with advice and input from F.M. and D.L. A.P.S. and
F.M.selectedthestudies.A.P.S.andD.L.assessedthestageof
| Most studies | were | undertaken |           | at secondary |         | and tertiary | set- |            |     |                          |     |         |     |       |
| ------------ | ---- | ---------- | --------- | ------------ | ------- | ------------ | ---- | ---------- | --- | ------------------------ | --- | ------- | --- | ----- |
|              |      |            |           |              |         |              |      | automation | and | level of autonomy.A.P.S. |     | drafted | the | manu- |
| tings (91%)  | in   | the        | developed | world        | (100%). | Despite      | the  |            |     |                          |     |         |     |       |
potential for AI to improve health services in resource- script withinput from allauthors. All authors providedrevi-
settings,66–68 sions for intellectual content. All authors have approved the
| constrained |          |     | our               | review  | has identified |           | a gap in |                  |     |     |     |     |     |     |
| ----------- | -------- | --- | ----------------- | ------- | -------------- | --------- | -------- | ---------------- | --- | --- | --- | --- | --- | --- |
|             |          |     |                   |         | settings.69,70 |           |          | finalmanuscript. |     |     |     |     |     |     |
| evaluating  | ML-based |     | CDS               | in such |                | Resource- |          |                  |     |     |     |     |     |     |
| constrained | settings |     | are characterized |         | by             | limited   | medical  |                  |     |     |     |     |     |     |
expertiseandinfrastructureleadingtothesuboptimaldelivery
Supplementarymaterial
ofservices.71Suchconditionsarenotboundbytheeconomic
|            |     |          |             |     |          |             |     | Supplementary | material | is  | available at | Journal | of the | Ameri- |
| ---------- | --- | -------- | ----------- | --- | -------- | ----------- | --- | ------------- | -------- | --- | ------------ | ------- | ------ | ------ |
| conditions | as  | resource | limitations |     | are also | experienced | by  |               |          |     |              |         |        |        |
canMedicalInformaticsAssociationonline.
| developed | countries, |              | such as | in rural   | or regional | areas           | with |     |     |     |     |     |     |     |
| --------- | ---------- | ------------ | ------- | ---------- | ----------- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| limited   | access     | to expertise |         | and modest | IT          | infrastructure. | In   |     |     |     |     |     |     |     |
addition,theremaybeagreaterroleforAItoprovidespecific
Funding
clinicalexpertiseinprimarycarewiththeshifttowardpromo-
ThisstudywassupportedbyaMacquarieUniversitydoctoral
| tive and | preventive | care | which | is increasing |     | the demand | for |             |         |           |         |           |     |         |
| -------- | ---------- | ---- | ----- | ------------- | --- | ---------- | --- | ----------- | ------- | --------- | ------- | --------- | --- | ------- |
|          |            |      |       |               |     |            |     | scholarship | awarded | to A.P.S. | (iMQRES | 20201869) |     | and the |
primaryhealthservices.
Thesefacts,combinedwiththemainfindingofthisreview NHMRC Centre for Research Excellence (CRE) in Digital
that most ML-based CDS were assistive and still required Health(APP1134919).Thefundingsourcesdidnotplayany
experts to oversee decision-making, make it necessary to role in the study design, in the collection and analysis, and
examine the appropriateness of ML-based CDS in resource- interpretationofdata,orinthewritingofthereport.
constrainedsettingsasthesesystemsmayincreasetheburden
| on clinicians | and | even | increase | risks. | Accordingly, |     | we argue |     |     |     |     |     |     |     |
| ------------- | --- | ---- | -------- | ------ | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Conflictsofinterest
| that autonomous                                          |     | CDS | may | be more | suitable | for | resource- |               |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | ------- | -------- | --- | --------- | ------------- | --- | --- | --- | --- | --- | --- |
| constrainedsettings.Forinstance,3studiesinthisreviewpro- |     |     |     |         |          |     |           | Nonedeclared. |     |     |     |     |     |     |
posedpotentialuseoftheirautonomousCDStoscreenhepa-
|           | disease,55 |     |           |     | cataract,53 |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tobiliary |            |     | childhood |     |             |     | and |     |     |     |     |     |     |     |
Dataavailability
onychomycosis52inremoteorpoorlyservicedareas.
Alldatarelevanttotheanalysisareincludedinthearticleand
Limitations onlinesupplementarymaterial.Therearenonewdataassoci-
There are several limitations. First, this review is limited to atedwiththisarticle.
thepublishedresearchliteratureaboutML-basedCDSinclin-
icalsettings.Wedidnotincludegrayliterature,suchaswhite
References
| papers and | reports. | Second, |     | our analysis | of          | the level | of CDS   |                                                              |     |     |     |     |     |     |
| ---------- | -------- | ------- | --- | ------------ | ----------- | --------- | -------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| autonomy   | was      | limited | to  | the CDS      | information |           | that was |                                                              |     |     |     |     |     |     |
|            |          |         |     |              |             |           |          | 1. CoieraE.Clinicaldecisionsupportsystem.In:CoieraE,ed.Guide |     |     |     |     |     |     |
reportedinthepapersandpriorvalidationstudies.Thisinfor- toHealthInformatics.3rded.Taylor&FrancisGroup;2015:417.
mationwaslessstructuredthantheindicationsofuseinmedi- 2. SuttonRT,PincockD,BaumgartDC,etal.Anoverviewofclinical
cal device approval documents which informed the decisionsupportsystems:benefits,risks,andstrategiesforsuccess.
development of the level of autonomy.13 Finally, there was NPJDigitMed.2020;3:17.

2062 JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12
3. YuK-H,BeamAL,KohaneIS.Artificialintelligenceinhealthcare. assessment: a pilot usability study. Surgery (United States).
NatBiomedEng.2018;2(10):719-731. 2019;165(5):1035-1045.
4. CoieraE.Onalgorithms,machines,andmedicine.LancetOncol. 27. BurdickH,PinoE,Gabel-ComeauD,etal.Effectofasepsispredic-
2019;20(2):166-167. tionalgorithmonpatientmortality,lengthofstayandreadmission:
5. VaseyB,UrsprungS,BeddoeB,etal.Associationofcliniciandiag- a prospective multicentre clinical outcomes evaluation of real-
nosticperformancewithmachinelearning-baseddecisionsupport world patientdatafrom US hospitals. BMJHealthCare Inform.
systems:asystematicreview.JAMANetw.2021;4(3):e211276. 2020;27(1):e100109.
6. MagrabiF,AmmenwerthE,McNairJB,etal.Artificialintelligence 28. GianniniHM,GinestraJC,ChiversC,etal.Amachinelearning
inclinicaldecisionsupport:challengesforevaluatingAIandpracti- algorithmtopredictseveresepsisandsepticshock:development,
calimplications.YearbMedInform.2019;28(1):128-134. implementation, and impact on clinical practice. Crit Care Med.
7. JaspersMW,SmeulersM,VermeulenH,etal. Effectsofclinical 2019;47(11):1485-1492.
decision-supportsystemsonpractitionerperformanceandpatient 29. GinestraJC,GianniniHM,SchweickertWD,etal.Clinicianper-
outcomes:asynthesisofhigh-qualitysystematicreviewfindings.J ceptionofamachinelearning-basedearlywarningsystemdesigned
AmMedInformAssoc.2011;18(3):327-334. to predict severe sepsis and septic shock. Crit Care Med.
8. KwanJL,LoL,FergusonJ,etal.Computerisedclinicaldecision 2019;47(11):1477-1484.
supportsystemsandabsoluteimprovementsincare:meta-analysis 30. GongD,WuL,ZhangJ,etal.Detectionofcolorectaladenomas
ofcontrolledclinicaltrials.BMJ.2020;370:m3216. withareal-timecomputer-aidedsystem(ENDOANGEL):arando-
9. LiJW,WangLM,AngTL.Artificialintelligence-assistedcolono- mised controlled study. Lancet Gastroenterol Hepatol.
scopy:anarrativereviewofcurrentdataandclinicalapplications. 2020;5(4):352-361.
SingaporeMedJ.2022;63(3):118-124. 31. GrigullL,LechnerW,PetriS,etal.Diagnosticsupportforselected
10. YeoM,KokHK,KutaibaN,etal.Artificialintelligenceinclinical neuromusculardiseasesusinganswer-patternrecognitionanddata
decisionsupportandoutcomeprediction-applicationsinstroke.J miningtechniques:aproofofconceptmulticenterprospectivetrial.
MedImagingRadiatOncol.2021;65:518-528. BMCMedInformDecisMak.2016;16:31.
11. WuM,DuX,GuR,etal.Artificialintelligenceforclinicaldecision 32. Jauk S, Kramer D, Avian A, et al. Technology acceptance of a
supportinsepsis.FrontMed(Lausanne).2021;8:665464. machinelearningalgorithmpredictingdeliriuminaclinicalsetting:
12. CoieraE.Thelastmile:whereartificialintelligencemeetsreality.J amixed-methodsstudy.JMedSyst.2021;45(4):48.
MedInternetRes.2019;21(11):e16323. 33. JaukS,KramerD,GroßauerB,etal.Riskpredictionofdeliriumin
13. LyellD,CoieraE,ChenJ,etal.Howmachinelearningisembedded hospitalized patients using machine learning: an implementation
tosupportcliniciandecisionmaking:ananalysisofFDA-approved and prospective evaluation study. J Am Med Inform Assoc.
medicaldevices.BMJHealthCareInform.2021;28(1):e100301. 2020;27(9):1383-1392.
14. CoieraE.Assessingtechnologysuccessandfailureusinginforma- 34. LiuWN,ZhangYY,BianXQ,etal.Studyondetectionrateofpol-
tion value chain theory. Stud Health Technol Inform. yps and adenomas in artificial-intelligence-aided colonoscopy.
2019;263:35-48. SaudiJGastroenterol.2020;26(1):13-19.
15. YinJ,NgiamKY,TeoHH.Roleofartificialintelligenceapplica- 35. MoriY,KudoSE,MisawaM,etal.Real-timeuseofartificialintel-
tionsinreal-lifeclinicalpractice:systematicreview.JMedInternet ligenceinidentificationofdiminutivepolypsduringcolonoscopya
Res.2021;23(4):e25759. prospectivestudy.AnnInternMed.2018;169(6):357-366.
16. TriantafyllidisAK,TsanasA.Applicationsofmachinelearningin 36. Nicolae A, Semple M, Lu L, et al. Conventional vs machine
real-lifedigitalhealthinterventions:reviewoftheliterature.JMed learning-based treatment planning in prostate brachytherapy:
InternetRes.2019;21(4):e12286. results of a Phase I randomized controlled trial. Brachytherapy.
17. KnopM,WeberS,MuellerM,etal.Humanfactorsandtechnolog- 2020;19(4):470-476.
icalcharacteristicsinfluencingtheinteractionofmedicalprofessio- 37. RawsonTM,HernandezB,MooreLSP,etal.Supervisedmachine
nals with artificial intelligence-enabled clinical decision support learningforthepredictionofinfectiononadmissiontohospital:a
systems:literaturereview.JMIRHumFactors.2022;9(1):e28639. prospectiveobservationalcohortstudy.JAntimicrobChemother.
18. ArkseyH,O’MalleyL.Scopingstudies:towardsamethodological 2019;74(4):1108-1115.
framework.IntJSocResMethodol.2005;8(1):19-32. 38. Repici A, Badalamenti M, Maselli R, et al. Efficacy of real-time
19. LevacD,ColquhounH,O’BrienKK.Scopingstudies:advancing computer-aideddetectionofcolorectalneoplasiainarandomized
themethodology.ImplementSci.2010;5(69):1-9. trial.Gastroenterology.2020;159(2):512-520.e7.
20. TriccoAC,LillieE,ZarinW,etal.PRISMAextensionforscoping 39. Romero-BrufauS,WyattKD,BoyumP,etal.Alessoninimple-
reviews (PRISMA-ScR): checklist and explanation. Ann Intern mentation:apre-poststudyofproviders’experiencewithartificial
Med.2018;169(7):467-473. intelligence-based clinical decision support. Int J Med Inform.
21. PetersMD,GodfreyCM,SoaresPMCB,etal.JoannaBriggsInsti- 2020;137:104072.
tuteReviewers’Manual.2015edition/supplement.Adelaide:The 40. SavenijeMHF,MasperoM,SikkesGG,etal.Clinicalimplementa-
JoannaBriggsInstitute;2015. tionofMRI-basedorgans-at-riskauto-segmentationwithconvolu-
22. The World Bank. World Bank Country and Lending Groups. tional networks for prostate radiotherapy. Radiat Oncol.
2021. Accessed February 15, 2021. Available from: https://data- 2020;15(1):104.
helpdesk.worldbank.org/knowledgebase/articles/906519-world-bank- 41. SegalG,SegevA,BromA,etal.Reducingdrugprescriptionerrors
country-and-lending-groups. andadversedrugeventsbyapplicationofaprobabilistic,machine-
23. ParasuramanR,SheridanT,WickensC.Amodelfortypesandlev- learningbasedclinicaldecisionsupportsysteminaninpatientset-
elsofhumaninteractionwithautomation.IEEETransSystMan ting.JAmMedInformAssoc.2019;26(12):1560-1565.
CybernB.2000;30(3):286-297. 42. SendakMP,RatliffW,SarroD,etal.Real-worldintegrationofa
24. Coiera E. A new informatics geography. Yearb Med Inform. sepsis deep learning technology into routine clinical care: imple-
2016;(1):251-255. mentationstudy.JMIRMedInform.2020;8(7):e15182.
25. BlombergSN,ChristensenHC,LippertF,etal.Effectofmachine 43. Shimabukuro DW, Barton CW, Feldman MD, et al. Effect of a
learningondispatcherrecognitionofout-of-hospitalcardiacarrest machine learning-based severe sepsis prediction algorithm on
duringcallstoemergencymedicalservices:arandomizedclinical patientsurvivalandhospitallengthofstay:arandomisedclinical
trial.JAMANetwOpen.2021;4(1):e2032320. trial.BMJOpenRespirRes.2017;4(1):e000234.
26. BrennanM,PuriS,Ozrazgat-BaslantiT,etal.Comparingclinical 44. SiboltP,AnderssonLM,CalmelsL,etal.Clinicalimplementation
judgmentwiththeMySurgeryRiskalgorithmforpreoperativerisk ofartificialintelligence-drivencone-beamcomputedtomography-

JournaloftheAmericanMedicalInformaticsAssociation,2023,Vol.30,No.12 2063
guided online adaptive radiotherapy in the pelvic region. Phys supporttoolforcalculatingCHA(2)DS(2)-VAScscores.CircCar-
ImagingRadiatOncol.2021;17:1-7. diovascQualOutcomes.2020;13(2):e006286.
45. TanJR,CheongEHT,ChanLP,etal.Implementationofanartifi- 58. AkbarS,LyellD,MagrabiF.Automationinnursingdecisionsup-
cialintelligence-baseddoublereadsystemincapturingpulmonary port systems: a systematic review of effects on decision making,
nodule discrepancy in CT studies. Curr Probl Diagn Radiol. care delivery, and patient outcomes. J Am Med Inform Assoc.
| 2021;50(2):119-122. |     |     |     |     |     | 2021;28(11):2502-2513. |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
46. WangP,BerzinTM,GlissenBrownJR,etal.Real-timeautomatic 59. CarayonP,HoonakkerP,HundtAS,etal.Applicationofhuman
detectionsystemincreasescolonoscopicpolypandadenomadetec- factorstoimproveusabilityofclinicaldecisionsupportfordiagnos-
tion rates: a prospective randomised controlled study. Gut. ticdecision-making:ascenario-basedsimulationstudy.BMJQual
| 2019;68(10):1813-1819. |     |     |     |     |     | Saf.2020;29(4):329-340. |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
47. WangP,LiuP,GlissenBrownJR,etal.Loweradenomamissrate 60. vanBaalenS,BoonM,VerhoefP.Fromclinicaldecisionsupportto
ofcomputer-aideddetection-assistedcolonoscopyvsroutinewhite- clinical reasoning support systems. J Eval Clin Pract.
light colonoscopy in a prospective tandem study. Gastroenterol- 2021;27(3):520-528.
ogy.2020;159(4):1252-1261.e5. 61. Lyell D, Magrabi F, Raban MZ, et al. Automation bias in elec-
48. Marcos-PaseroH,ColmenarejoG,Aguilar-AguilarE,etal.Rank- tronicprescribing.BMCMedInformDecisMak.2017;17(1):28.
ing of a wide multidomain set of predictor variables of children 62. MaoQ,JayM,HoffmanJL,etal.Multicentrevalidationofasepsis
obesity by machine learning variable importance techniques. Sci prediction algorithm using only vital sign data in the emergency
Rep.2021;11(1):1910. department, general ward and ICU. BMJ Open.
49. NielO,BastardP,BoussardC,etal.Artificialintelligenceoutperforms 2018;8(1):e017833.
|     |     |     |     |     |     | 63. Vasey | B, Nagendran | M, Campbell |     | B, et al.; | DECIDE-AI | Expert |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | ----------- | --- | ---------- | --------- | ------ |
experiencednephrologiststoassessdryweightinpediatricpatientson
Group.Reportingguidelinefortheearlystageclinicalevaluationof
chronichemodialysis.PediatrNephrol.2018;33(10):1799-1803.
decisionsupportsystemsdrivenbyartificialintelligence:DECIDE-
50. ChenJ,ChokshiS,HegdeR,etal.Development,implementation,
AI.BMJ.2022;377:e070904.
| and evaluation | of a personalized |            | machine learning | algorithm    | for |          |        |                |     |     |                |     |
| -------------- | ----------------- | ---------- | ---------------- | ------------ | --- | -------- | ------ | -------------- | --- | --- | -------------- | --- |
|                |                   |            |                  |              |     | 64. Cruz | Rivera | S, Liu X, Chan | AW, | et  | al.; SPIRIT-AI | and |
| clinical       | decision support: | case study | with shingles    | vaccination. | J   |          |        |                |     |     |                |     |
CONSORT-AIConsensusGroup.Guidelinesforclinicaltrialpro-
MedInternetRes.2020;22(4):e16848.
tocolsforinterventionsinvolvingartificialintelligence:theSPIRIT-
| 51. Isma’eel | H, Sakr G, Serhan | M,  | et al. Artificial | neural | network- |     |     |     |     |     |     |     |
| ------------ | ----------------- | --- | ----------------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
AIextension.NatMed.2020;26(9):1351-1363.
basedmodelenhancesriskstratificationandreducesnon-invasive
|         |                |          |                      |     |     | 65. LiuX,CruzRiveraS,MoherD,etal.;SPIRIT-AIandCONSORT- |     |     |     |     |     |     |
| ------- | -------------- | -------- | -------------------- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| cardiac | stress imaging | compared | to Diamond–Forrester |     | and |                                                        |     |     |     |     |     |     |
AIWorkingGroup.Reportingguidelinesforclinicaltrialreports
Moriseriskassessmentmodels:aprospectivestudy.JNuclCardiol.
forinterventionsinvolvingartificialintelligence:theCONSORT-AI
2018;25(5):1601-1609.
extension.NatMed.2020;26(9):1364-1374.
52. KimYJ,HanSS,YangHJ,etal.Prospective,comparativeevalua-
|     |     |     |     |     |     | 66. AlamiH,RivardL,LehouxP,etal.Artificialintelligenceinhealth |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
tionofadeepneuralnetworkanddermoscopyinthediagnosisof
care:layingthefoundationforresponsible,sustainable,andinclu-
onychomycosis.PLoSOne.2020;15(6):e0234334.
siveinnovationinlow-andmiddle-incomecountries.GlobHealth.
| 53. Lin H, | Li R, Liu Z, | et al. Diagnostic | efficacy | and therapeutic |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ----------------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2020;16(1):52.
| decision-making | capacityof | an  | artificial intelligence | platform | for |                                                               |     |     |     |     |     |     |
| --------------- | ---------- | --- | ----------------------- | -------- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                 |            |     |                         |          |     | 67. WahlB,Cossy-GantnerA,GermannS,etal.Artificialintelligence |     |     |     |     |     |     |
childhoodcataractsineyeclinics:amulticentrerandomizedcon-
(AI)andglobalhealth:howcanAIcontributetohealthinresource-
trolledtrial.EClinicalMedicine.2019;9:52-59.
poorsettings?BMJGlobHealth.2018;3(4):e000798.
54. WintjensA,HintzenKFH,EngelenSME,etal.Applyingtheelec-
|     |     |     |     |     |     | 68. KiyassehD,ZhuT,CliftonD.Thepromiseofclinicaldecisionsup- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
tronicnoseforpre-operativeSARS-CoV-2screening.SurgEndosc.
|     |     |     |     |     |     | port | systems targetting | low-resource |     | settings. | IEEE Rev | Biomed |
| --- | --- | --- | --- | --- | --- | ---- | ------------------ | ------------ | --- | --------- | -------- | ------ |
2021;35(12):6671-6678.
Eng.2020;15:354-371.
55. XiaoW,HuangX,WangJH,etal.Screeningandidentifyinghepa-
|     |     |     |     |     |     | 69. FraserHSF,ZahiriK,KimN,etal.TheGlobalHealthInformatics |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
tobiliarydiseasesthroughdeeplearningusingocularimages:apro-
|           |             |        |        |       |         | landscape | and | JAMIA. | J Am | Med | Inform | Assoc. |
| --------- | ----------- | ------ | ------ | ----- | ------- | --------- | --- | ------ | ---- | --- | ------ | ------ |
| spective, | multicentre | study. | Lancet | Digit | Health. |           |     |        |      |     |        |        |
2023;30(4):775-780.
2021;3(2):e88-e97. 70. Ciecierski-HolmesT,SinghR,AxtM,etal.Artificialintelligence
56. Yao X, Rushlow DR, Inselman JW, et al. Artificial intelligence- for strengthening healthcare systems in low- and middle-income
enabledelectrocardiogramsforidentificationofpatientswithlow countries: a systematic scoping review. NPJ Digit Med.
| ejectionfraction:apragmatic,randomizedclinicaltrial.NatMed. |     |     |     |     |     | 2022;5(1):162. |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
2021;27(5):815-819. 71. van Zyl C, Badenhorst M, Hanekom S, et al. Unravelling ‘low-
57. AbedinZ,HoernerR,HabbousheJ,etal.Implementationofafast resourcesettings’:asystematicscopingreviewwithqualitativecon-
healthcare interoperability resources-based clinical decision tentanalysis.BMJGlobHealth.2021;6(6):e005190.
