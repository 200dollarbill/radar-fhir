FHIR FLI: An Open Source Platform for Storing, Sharing and Analysing
Lifestyle Data
KiranGopinathan1,NikolaosAlexandrosKaloumenos1,KinnariAjmera1,AlexandruMatei1,
IanWilliams2 andAndrewDavis2
1UniversityCollegeLondon,UnitedKingdom
2NuffieldHealth,UnitedKingdom
Keywords: PersonalHealthRecord,LifestyleData,FHIR.
Abstract: Consumersandhealthcareorganisationsalikeareincreasinglyinterestedinusingdigitalhealthsolutionsto
reducetheriskofchronicconditionsortohelpmanagetheseconditionsoutsidehospitals. Equally,thereis
astrongpublichealthbenefitinhelpingindividualsadoptandimprovehealthylifestylebehaviours. Thefirst
stepinthisdirectionistheabilitytorecordandanalyselifestyledata. Currently,lifestyleloggingplatforms
use proprietary data formats. Data is segregated among different platforms, impacting consumers, service
providers, research institutes and public health bodies. Our aim is to facilitate the transfer of information
betweenindividualsandorganisationsthatholdorrequiretheirlifestyledata. Wedemonstratethatanopen
sourceplatformbasedonaclinicallyrecognisedinteroperabilitystandard-FastHealthcareInteroperability
Resources(FHIR)-canmeetbothconsumersandindustryneeds. Weuseasanexamplethecaseofpeople
managing arthritis. Our contributions are: (i) an extension of the FHIR standard for lifestyle data, (ii) a
reference architecture for a Personal Lifestyle Record, (iii) integration with voice-enabled digital assistants
forlifestyledatacaptureand(iv)anopensourceimplementationofthisarchitecturethatretrieves,savesand
analyseslifestyledatafromwearabledevices.
1 INTRODUCTION We consider lifestyle data any measurement re-
latedto:
The UK population is living longer, but at the same • lifestyleriskfactors(e.g. physicalactivity)
timepeoplespendmoreyearsinill-health,managing
• mentalhealth(e.gqualityofsleep,stresslevels)
chronicconditions(PublicHealthEngland,2015).
To cope with the increasing burden of disease, • monitoring of chronic conditions (e.g blood glu-
more and more resources are dedicated to preven- cose)
tionandmanagementofchronicconditionswithinthe
• maintainingorimprovingability(e.gphysiother-
community. For example, a recent study in the UK
apy,rehabilitation,mentalresilience,elitesports).
has shown a remission in Type 2 diabetes for par-
ticipants following a low-calorie, diet-based, weight Thecurrentlandscapeintheindustryisveryfrag-
management programme. Throughout the process, mented - each organisation that generates lifestyle
thetrialparticipantshadinteractionwiththeirGPand datausesproprietaryformats. Thechallengeweaim
couldaccessadietician(Leanetal.,2017) toaddressinthispaperisthelackofatrueplatform
As fitness, well-being and lifestyle data becomes approach,inthewell-beingandlifestyledomain.
more relevant in the provision of care, consumers In a platform approach, the analysis of data (for
andhealthcareprofessionalsneedtheabilitytoaggre- day-to-daymonitoring,servicepersonalisationorbe-
gatedisparateinformationaboutone’slifestyleintoa haviourchange)isseparatedfromdatacollection.For
consolidated view spanning across the years, across this to happen, there is a need for an encompassing
providers,andcoveringmanydatasources.Improved andopenstandardtodescribelifestyledatainacon-
access to lifestyle data can lead to better quality of sistent manner, agnostic of the source systems gen-
care, better health outcomes and improved customer erating the data. This will open the way for services
satisfaction. specifically designed to deliver value by interpreting
227
Gopinathan,K.,Kaloumenos,N.,Ajmera,K.,Matei,A.,Williams,I.andDavis,A.
FHIRFLI:AnOpenSourcePlatformforStoring,SharingandAnalysingLifestyleData.
DOI:10.5220/0006791302270233
InProceedingsofthe4thInternationalConferenceonInformationandCommunicationTechnologiesforAgeingWellande-Health(ICT4AWE2018),pages227-233
ISBN:978-989-758-299-8
Copyright c 2019bySCITEPRESS–ScienceandTechnologyPublications,Lda.Allrightsreserved
(cid:13)

ICT4AWE2018-4thInternationalConferenceonInformationandCommunicationTechnologiesforAgeingWellande-Health
the data in new, useful ways. This is the path fol- Cloud-basedplatformslikeOpenMHealthorMi-
lowed in the medical community, where much effort crosoftHealthVaulthavecross-platformaccessibility
has been put into defining interoperability standards andallowdeveloperstoextendthedatamodel. Infor-
todescribeclinicaldata. mation can be shared with service providers. How-
Inthispaper,weproposeanarchitectureforaPer- ever,theseplatformsalsohavesomelimitations.
sonal Lifestyle Record that offers capabilities to re- • atthemoment,theystilluseproprietarydatafor-
| trieve, store | and | analyse | lifestyle | data in | a provider- |     |     |     |     |     |     |
| ------------- | --- | ------- | --------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
mats
| agnostic | environment, | illustrating |     | the potential | of a |     |     |     |     |     |     |
| -------- | ------------ | ------------ | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- |
• third-partydeveloperscannotdevelopcustomvi-
| platformapproach. |     | Toinformourproposal,weuseas |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sualisationsorpredictivemodels
anillustrativecasestudythemanagementofarthritis.
The paper is organised as follows. Section 2 There are two conclusions we can draw from re-
|          |             |            |     |           |          | viewing | the current | landscape. | First, | there | is a clear |
| -------- | ----------- | ---------- | --- | --------- | -------- | ------- | ----------- | ---------- | ------ | ----- | ---------- |
| presents | the current | technology |     | landscape | for man- |         |             |            |        |       |            |
aging and using lifestyle data. Section 3 discusses direction towards enabling data movement. Many
an illustrative customer journey, in arthritis manage- wearable companies allow customers to download
theirowndataforexample.Conversely,othercompa-
| ment. Section |     | 4 proposes | a method | for | standardis- |     |     |     |     |     |     |
| ------------- | --- | ---------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
ation of lifestyle data and offers two specific exam- niespositionthemselvesasdatarepositories,offering
ples. Section 5 presents a reference architecture that thenecessaryintegrationsforconsumerstobringdata
| decouples        | data | generation | from             | data analysis. | Sec-      | intotheirplatforms. |       |       |                |     |             |
| ---------------- | ---- | ---------- | ---------------- | -------------- | --------- | ------------------- | ----- | ----- | -------------- | --- | ----------- |
|                  |      |            |                  |                |           | Second,             | there | is no | open, standard |     | information |
| tion 6 discusses |      | emerging   | user interaction |                | channels, |                     |       |       |                |     |             |
such asvoice-enabled digitalassistants for capturing model for lifestyle data, with clear governance sup-
lifestyledata. Section7describestheimplementation porting it, which is not tied to a specific commercial
organisation.
workdonetodateandSection8summarisesourcon-
tributionsanddiscussesfuturework. We argue that such an information model could
|     |     |     |     |     |     | well be   | developed    | following | an open         | and  | inclusive  |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | --------- | --------------- | ---- | ---------- |
|     |     |     |     |     |     | approach, | as opposed   | to        | being developed |      | internally |
|     |     |     |     |     |     | by any    | one company. | There     | is a large      | body | of work    |
2 BACKGROUND
whichcouldinformtheseefforts,stemmingfromthe
|     |     |     |     |     |     | clinical | community | pursuit | to standardise |     | the way |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ------- | -------------- | --- | ------- |
Smart-phones have become a leading consumer medicaldataisrepresented.
| choice for | managing | lifestyle | data.       | They | are a nat- |                 |         |        |                |         |         |
| ---------- | -------- | --------- | ----------- | ---- | ---------- | --------------- | ------- | ------ | -------------- | ------- | ------- |
|            |          |           |             |      |            | FHIR            | (Bender | and    | Sartipi, 2013) | is such | a stan- |
| ural hub   | to bring | together  | data coming | from | built-in   |                 |         |        |                |         |         |
|            |          |           |             |      |            | dard, supported |         | by HL7 | and adopted    | by      | a grow- |
sensorsonthephone,datacomingfromwearablede- ingnumberofhealthcareorganisations,includingthe
vicesthatsynchronisewiththephoneanddatacom-
NHS(Kavanagh,2017).
| ing from | mobile | apps installed | on  | the phone. | There |     |      |               |         |       |             |
| -------- | ------ | -------------- | --- | ---------- | ----- | --- | ---- | ------------- | ------- | ----- | ----------- |
|          |        |                |     |            |       | The | FHIR | specification | defines | a set | of core re- |
areanumberoflimitationswhenusingasmart-phone sources (Person, Observation, Diagnostic etc). and
basedlifestylerecord: an infrastructure for handling resources. FHIR Ob-
• it is not an inclusive approach: Apple Healthkit servationsarealreadyusedtodescribe:
datacanonlybeaccessedfromaniPhone.
|     |     |     |     |     |     | • Vitalsigns: |     | e.g. temperature |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------- | --- | --- | --- |
• it does not cover the needs of service providers, • LaboratoryData: e.g. bloodglucose
| who | need to | access | and aggregate | data | from a |                        |     |     |                    |     |     |
| --- | ------- | ------ | ------------- | ---- | ------ | ---------------------- | --- | --- | ------------------ | --- | --- |
|     |         |        |               |      |        | • DevicesMeasurements: |     |     | e.g. pulseoximetry |     |     |
populationofclients
|     |     |     |     |     |     | • Clinicalassessments: |     |     | e.g. GlasgowComaScore |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --------------------- | --- | --- |
Solutionscreatedbywearablecompanieshavethe
|           |          |            |        |            |     | • Personalcharacteristics: |     |     | e.g. eyecolour |     |     |
| --------- | -------- | ---------- | ------ | ---------- | --- | -------------------------- | --- | --- | -------------- | --- | --- |
| advantage | of being | accessible | across | platforms, | mo- |                            |     |     |                |     |     |
bileandweb. Theyfocusonanalysingandproviding The FHIR standard can be extended to suit par-
insightondatacollectedthroughthewearable. They ticular contexts of use - including management of
|     |     |     |     |     |     | lifestyledata. |     | ExtendingFHIRtosuitparticularsce- |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --------------------------------- | --- | --- | --- |
havetwomainlimitations:
nariosofuseisachievedbycreatingFHIRProfiles.A
| • the | data model | of each | platforms | is  | controlled |     |     |     |     |     |     |
| ----- | ---------- | ------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
profileextendsorrestrictscoreFHIRresources,based
| bythevendoranditonlycontainsitems |     |     |     |     | relevant |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
onthedomain-specificneeds.
withinthecontextofuseforeachwearable-third
AFHIRextensionforlifestyledataisbeingdevel-
partiescannotextendthedatamodel.
|     |     |     |     |     |     | oped as | part of | the Finnish | national | Personal | Health |
| --- | --- | --- | --- | --- | --- | ------- | ------- | ----------- | -------- | -------- | ------ |
• the data is still locked, as Fitbit users can only Record infrastructure (Kanta, 2017). However, their
comparethemselvesagainstotherFitbitusersfor approach is to create a limited number of FHIR ob-
example. servations, describing fitness information aggregated
228

FHIRFLI:AnOpenSourcePlatformforStoring,SharingandAnalysingLifestyleData
overaperiodoftime-forexample’Distancereached The first scenario we aim to support is a person
in24h’. Wefavouranapproachwhereanydatapoint centric view: allowing one individual to aggregate
createdatthesourcesystemismappedtoaFHIRob- data about himself which is held by different plat-
servation. In our approach, three distinct walking / formsandproviders. Forexample,somebodymanag-
runningepisodesina24hourwindowwouldberep- ingosteoarthritiscouldattendphysiotherapysessions,
resentedasthreeFHIRobservations,notasingleone. he could run in the park during the weekend and at-
|     |     |     |     |     |     |     | tend a T’ai | chi class | in  | the gym | once | a week. He |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ------- | ---- | ---------- |
shouldhaveaccess,combineandownallofthisdata
3 ILLUSTRATIVE CASE STUDY -informationgeneratedbyaspecialist,byawearable,
byafitnessserviceprovider,orselfreported.
|           |      |        |         |         |            |     | The                    | second scenario |                            | we aim | to support | is an or- |
| --------- | ---- | ------ | ------- | ------- | ---------- | --- | ---------------------- | --------------- | -------------------------- | ------ | ---------- | --------- |
| Lifestyle | data | can be | used to | improve | the health | and |                        |                 |                            |        |            |           |
|           |      |        |         |         |            |     | ganisationcentricview: |                 | allowingserviceprovidersto |        |            |           |
well-beingofpeopleofallages.
|            |     |              |     |              |     |           | receivedatasharedwiththembytheirclients. |     |     |     |     | Forex- |
| ---------- | --- | ------------ | --- | ------------ | --- | --------- | ---------------------------------------- | --- | --- | --- | --- | ------ |
| To discuss |     | our proposal |     | for managing |     | lifestyle |                                          |     |     |     |     |        |
ample,aphysiotherapistshouldbeabletoaccessdata
| data, we    | consider   | the    | case   | of arthritis, | a    | group of  |                                         |             |        |      |               |               |
| ----------- | ---------- | ------ | ------ | ------------- | ---- | --------- | --------------------------------------- | ----------- | ------ | ---- | ------------- | ------------- |
|             |            |        |        |               |      |           | about physical                          | activity    | levels | and  | self          | reported pain |
| chronic     | conditions | that   | affect | the joints    | in   | the body. |                                         |             |        |      |               |               |
|             |            |        |        |               |      |           | levelsfromeachindividualundertreatment. |             |        |      |               | Equally,      |
| As of 2017, | 400,000    | adults |        | in the UK     | have | rheuma-   |                                         |             |        |      |               |               |
|             |            |        |        |               |      |           | a research                              | institution | may    | want | to accumulate | large         |
toidarthritis,andprevalenceincreaseswithage. Fur- datasets of lifestyle data for clinical research, from
| ther, 8.75 | million | people | in  | the UK | have | sought |     |     |     |     |     |     |
| ---------- | ------- | ------ | --- | ------ | ---- | ------ | --- | --- | --- | --- | --- | --- |
patientswillingtosharetheirdata.
treatmentforosteoarthritis,whereprevalencealsoin-
Third,wearelookingtosupportorganisationsthat
creaseswithage(ArthritisResearchUK,2017).
holdlifestyledataabouttheirclientsandwanttoof-
| For      | the management |     | of rheumatoid |     | arthritis,      | the |            |         |         |                 |     |             |
| -------- | -------------- | --- | ------------- | --- | --------------- | --- | ---------- | ------- | ------- | --------------- | --- | ----------- |
|          |                |     |               |     |                 |     | fer access | to this | data to | the individuals |     | themselves. |
| National | Institute      | for | Health        | and | Care Excellence |     |            |         |         |                 |     |             |
Forexample,agymchainlookingtoshareindividual
(NICE)intheUKrecommendsaccesstophysiother-
|               |     |         |         |     |           |      | attendance | data with | the | gym members, |     | so that they |
| ------------- | --- | ------- | ------- | --- | --------- | ---- | ---------- | --------- | --- | ------------ | --- | ------------ |
| apy services, | to  | improve | fitness | and | encourage | reg- |            |           |     |              |     |              |
canfurthersharethisdatawithaphysiotherapist.
| ular exercise  | (Deighton |                   | et al., | 2009).        | Similarly, | for |        |          |     |     |     |     |
| -------------- | --------- | ----------------- | ------- | ------------- | ---------- | --- | ------ | -------- | --- | --- | --- | --- |
| the management |           | of osteoarthritis |         | NICE          | recommends |     |        |          |     |     |     |     |
| physical       | exercise  | for local         | muscle  | strengthening |            | and |        |          |     |     |     |     |
|                |           |                   |         |               |            |     | 4 FHIR | PROFILES |     | FOR |     |     |
generalaerobicfitness(Conaghanetal.,2008).
In term of assessing pain intensity - a key mea- LIFESTYLE DATA
| surement                     | for arthritis |      | management | -      | there          | are differ- |           |              |     |                 |     |            |
| ---------------------------- | ------------- | ---- | ---------- | ------ | -------------- | ----------- | --------- | ------------ | --- | --------------- | --- | ---------- |
| ent scales                   | available,    | with | good       | degree | of correlation |             |           |              |     |                 |     |            |
|                              |               |      |            |        |                |             | Our first | contribution | is  | a demonstration |     | of how the |
| amongthem(Downieetal.,1978). |               |      |            |        | Oncecouldusea  |             |           |              |     |                 |     |            |
FHIRstandardmaybeusedtodescribelifestyledata
descriptivescale(nil,mild,moderate,severe,veryse-
|     |     |     |     |     |     |     | inaprovideragnosticfashion. |     |     | Therearemanypoten- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ------------------ | --- | --- |
vere),anumericscale(0-nopain,10-worstpossible
tialdatasourcesforlifestyledata:
| pain) (Farrar | et  | al., 2001) | or  | a visual | analogue | scale |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
(100 mm in length anchored by the two extremes) • self-recordedobservations
(Hawkeretal.,2011).
|              |        |              |          |             |          |          | • observations |                                 | captured | by providers |     | of a certain |
| ------------ | ------ | ------------ | -------- | ----------- | -------- | -------- | -------------- | ------------------------------- | -------- | ------------ | --- | ------------ |
| Based        | on the | clinical     | context, | there       | is       | a demon- |                |                                 |          |              |     |              |
|              |        |              |          |             |          |          | service:       | healthassessments,personalcoach |          |              |     |              |
| strable need | for    | data related |          | to physical | activity | and      |                |                                 |          |              |     |              |
painlevelstobesharedbetweenusers,GPsandphys- • smartphones,wearablesandbodysensors
| iotherapists. | The                    | hypothetical |     | customer | journey  | we  |         |               |     |       |         |             |
| ------------- | ---------------------- | ------------ | --- | -------- | -------- | --- | ------- | ------------- | --- | ----- | ------- | ----------- |
|               |                        |              |     |          |          |     | • smart | home devices: |     | smart | meters, | environment |
| useasa        | sourceofrequirementsis |              |     | then:    | apatient | di- |         |               |     |       |         |             |
sensors,smartspeakerswithvoice-enableddigital
agnosedwitharthritishasbeenreferredbyhisGPto
assistants
| aphysiotherapist. |     | Thephysiotherapistrecommendsa |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
regimeofmoderatephysicalactivity, whichincludes Inordertocapturethisvarietyofdataweneeded
outsiderunningsessionsandpilatesclassesatalocal to identify a set of profiles capable of representing
gym. Theuserwouldliketoshareafullrecordofhis it. FollowingFHIRbestpractices(Furore,2017),we
physical activity with the physiotherapist, as well as chose to extend the Observation profile, prioritizing
be able to track how his symptoms (i.e. pain levels) removingfieldsirrelevantforourcontextofuse,and
| change | over time, | as  | a result | of his | efforts. | In turn, |                  |     |            |      |             |        |
| ------ | ---------- | --- | -------- | ------ | -------- | -------- | ---------------- | --- | ---------- | ---- | ----------- | ------ |
|        |            |     |          |        |          |          | only introducing |     | new fields | when | no existing | fields |
thephysiotherapistwouldliketosharesummarydata couldpossiblyrepresentthedata.Theconstructedob-
withthepatientsGP. servationprofileisshowninFigure1. Thiscouldbe
To support this journey, we need to enable three usedforexampletocreatearecordingofselfreported
typesofinformationflows. painintensity,inreferencetoourarthritiscasestudy.
229

ICT4AWE2018-4thInternationalConferenceonInformationandCommunicationTechnologiesforAgeingWellande-Health
observations(duplicatedata,contradictorydata,com-
plementarydata)shallbeestablishedifandwhennec-
essarytoansweraspecificquery.
Third,dependingonthesourcesystem,datamay
|     |     |     |     |     |     |     | be more     | or less | sensitive, |           | so different   | access | rules  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ---------- | --------- | -------------- | ------ | ------ |
|     |     |     |     |     |     |     | would apply | to      | data.      | To enable | differentiated |        | access |
rulesfordifferenttypesofobservation,weaddtothe
profileafieldtorecordhowsensitivethedatais.
|     |     |     |     |     |     |     | In reference |     | to our | arthritis | case | study, | the other |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | --------- | ---- | ------ | --------- |
typeoflifestyleinformationthatshouldbesavedre-
|     |     |     |     |     |     |     | lates to | physical | workout | sessions. |     | To document | an  |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------- | --------- | --- | ----------- | --- |
exercisesession,weproposeusingaDiagnosticRe-
|     |     |     |     |     |     |     | portprofile,showninFigure2. |     |     |     | Thisisanothertype |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ----------------- | --- | --- |
ofFHIRresourcethatgroupsobservationsrelatedto
|     |     |     |     |     |     |     | thesameepisode. |     | First,ourprofileonDiagnosticRe- |        |         |           |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------------------------- | ------ | ------- | --------- | --- |
|     |     |     |     |     |     |     | port specifies  |     | the same                        | fields | we have | discussed | for |
Figure1:FHIRObservationProfile.
|     |     |     |     |     |     |     | individual    | observations: |            | a     | code, subject, | performer, |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------- | ---------- | ----- | -------------- | ---------- | --- |
|     |     |     |     |     |     |     | time. Second, |               | the result | field | contains       | reference  | to  |
Thecodefieldisusedtospecifythetypeofobser-
vation (in our case, a pain intensity recording). The additionalobservations. Thelistweprovideisnotex-
haustive. Dependingonwhatinformationisavailable
subjectfieldisareferencetothepersontheobserva-
fromthesourcesystem,implementersmayaddaddi-
| tion concerns. |     | The performer |     | field | is a reference | to  |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | --- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionalreferencestoobservations,sothatallavailable
| the source | system | (e.g. | device, | organisation |     | or per- |     |     |     |     |     |     |     |
| ---------- | ------ | ----- | ------- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
informationiscaptured.
son). Torecordthemeasurementresult,weuseaset
|            |         |         |       |            |     |       | Many    | lifestyle | devices |       | also make | the distinction |         |
| ---------- | ------- | ------- | ----- | ---------- | --- | ----- | ------- | --------- | ------- | ----- | --------- | --------------- | ------- |
| of related | fields, | grouped | under | Component. |     | These |         |           |         |       |           |                 |         |
|            |         |         |       |            |     |       | between | aggregate | and     | trace | data -    | running         | watches |
includetheactualvalue,butalsotheadmissiblerange
|          |        |                 |           |     |                  |           | are able    | to record | a       | user’s   | heart rate   | every          | few sec-   |
| -------- | ------ | --------------- | --------- | --- | ---------------- | --------- | ----------- | --------- | ------- | -------- | ------------ | -------------- | ---------- |
| and the  | method | of measurement. |           |     | Finally,         | we record |             |           |         |          |              |                |            |
|          |        |                 |           |     |                  |           | onds during | a         | session | (trace), | and          | also calculate | an         |
| both the | time   | period          | described | by  | this observation | -         |             |           |         |          |              |                |            |
|          |        |                 |           |     |                  |           | average     | heart     | rate at | the end  | (aggregate). |                | To reflect |
theeffectivetime(inourcase,whendidthepainoc-
cur)andalsothedatetheFHIRobservationhasbeen this, where applicable, fields for both types of data
|     |     |     |     |     |     |     | have been | added | to the | profile | - heartRate |     | and aver- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------ | ------- | ----------- | --- | --------- |
created-theissueddate.
ageHeartRate.
| The     | fields       | discussed | so    | far are  | applicable | to any |     |     |     |     |     |     |     |
| ------- | ------------ | --------- | ----- | -------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| type of | observation. |           | There | are some | additional | con-   |     |     |     |     |     |     |     |
siderationsthatarespecifictothelifestyledomain.
| First,                          | we need | to  | account | for              | the varying | degree |     |     |     |     |     |     |     |
| ------------------------------- | ------- | --- | ------- | ---------------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| ofreliabilityforthedatasources: |         |     |         | lookingatasimple |             |        |     |     |     |     |     |     |     |
measuresuchasweightmeasuredinkilograms-this
| could be    | self-reported, |     | retrieved | from        | a smart | scale,     |     |     |     |     |     |     |     |
| ----------- | -------------- | --- | --------- | ----------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| or measured | during         | a   | health    | assessment. |         | To capture |     |     |     |     |     |     |     |
this’trustworthiness’ofthedata,weintroduceafield
| for reliability, |     | that takes | numerical |     | values. | Each or- |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | --------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
ganisationusingtheseFHIRprofilemayspecifyrules
| thatassignreliabilityscorestosourcesystems. |     |     |     |     |     | Every |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
FHIRobservationcreatedbasedondatacomingfrom
| a given | source | would | then carry | the | same | reliability |     |     |     |     |     |     |     |
| ------- | ------ | ----- | ---------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
valueasthatassignedtothesourcesystem.
| Second,                      | the         | same                             | event              | (measurement) |                 | may be      |     |     |     |     |     |     |     |
| ---------------------------- | ----------- | -------------------------------- | ------------------ | ------------- | --------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| capturedinmorethanonesystem. |             |                                  |                    |               | Thesamephysical |             |     |     |     |     |     |     |     |
| workout(e.g.                 |             | apilatesclass)couldbecapturedbya |                    |               |                 |             |     |     |     |     |     |     |     |
| consumer                     | wearable    | device                           | and                | by            | the class       | booking     |     |     |     |     |     |     |     |
| systemofthegym.              |             | However,theeventwouldbede-       |                    |               |                 |             |     |     |     |     |     |     |     |
| scribed                      | differently | in                               | the two            | platforms.    |                 | Our design  |     |     |     |     |     |     |     |
| approach                     | is to       | avoid                            | any reconciliation |               |                 | or aggrega- |     |     |     |     |     |     |     |
| tion at this                 | stage.      | We                               | recommend          |               | creating        | two dis-    |     |     |     |     |     |     |     |
Figure2:FHIRFLIProfile-WorkoutSession.
| tinct FHIR | observations. |     | The | relation | between | these |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | --- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
230

FHIRFLI:AnOpenSourcePlatformforStoring,SharingandAnalysingLifestyleData
5 REFERENCE ARCHITECTURE wheneveranewFHIRprofileforlifestyledataiscre-
atedbyorganisationsimplementingthisarchitecture,
theconvertercomponentisupdatedaccordingly.
| A range  | of EHR | platforms     | already    | use | the FHIR |        |     |           |              |          |     |       |
| -------- | ------ | ------------- | ---------- | --- | -------- | ------ | --- | --------- | ------------ | -------- | --- | ----- |
|          |        |               |            |     |          | Third, | the | reference | architecture | requires | a   | docu- |
| standard | as a   | data exchange | mechanism. |     | However, |        |     |           |              |          |     |       |
FHIR messages are mapped to an internal clinical ment database, to store each FHIR observation in its
nativeformat-aJSONmessage.
| model (for   | example,  | OpenEHR) |        | and then     | saved in |         |     |           |              |          |     |        |
| ------------ | --------- | -------- | ------ | ------------ | -------- | ------- | --- | --------- | ------------ | -------- | --- | ------ |
|              |           |          |        |              |          | Fourth, | the | reference | architecture | includes |     | a data |
| a structured | database. | Data     | can be | interrogated | ei-      |         |     |           |              |          |     |        |
therthroughstructuredquerylanguagesontheinter- visualisation component, which comes with built-in
nalclinicalmodel. visualisations for common lifestyle data. We pro-
|              |     |       |         |         |         | pose a process |     | whereby | whenever | a new | FHIR | pro- |
| ------------ | --- | ----- | ------- | ------- | ------- | -------------- | --- | ------- | -------- | ----- | ---- | ---- |
| For example, |     | SMART | ON FHIR | (Mandel | et al., |                |     |         |          |       |      |      |
fileiscreated,thedatavisualisationcomponentisex-
| 2016) is | an EHR | platform | built to | support | importing |     |     |     |     |     |     |     |
| -------- | ------ | -------- | -------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
andexportinghealthcaredatathroughFHIRcompli- tended so that it can graphically represent the new
|     |     |     |     |     |     | type of | data. | Organisations |     | implementing | the | archi- |
| --- | --- | --- | --- | --- | --- | ------- | ----- | ------------- | --- | ------------ | --- | ------ |
antmessages-however,alldataisstoredinternallyas
tecturemaydevelopcustomdatavisualisationstosuit
asetofkeyvaluepairsinarelationaldatabase.
|                |     |        |                |         |     | theirspecificneeds. |     |        | Oneclearbenefitofbuildingvi- |      |            |     |
| -------------- | --- | ------ | -------------- | ------- | --- | ------------------- | --- | ------ | ---------------------------- | ---- | ---------- | --- |
| In comparison, |     | we aim | to investigate | whether | an  |                     |     |        |                              |      |            |     |
|                |     |        |                |         |     | sualisations        | on  | top of | a standard                   | data | model such | as  |
infrastructurebasedsolelyonFHIRmessagescanbe
FHIRisthatvisualisationoverthedatawillcontinue
| used for | reporting | and analytics. |     | By designing | and |             |     |           |      |                |          |     |
| -------- | --------- | -------------- | --- | ------------ | --- | ----------- | --- | --------- | ---- | -------------- | -------- | --- |
|          |           |                |     |              |     | to function | as  | expected, | even | if the systems | generat- |     |
implementingsuchaplatform,weaimtoevaluatethe
ingthedatachange.
| role of the | FHIR | standard | when it | comes | to storing |     |     |     |     |     |     |     |
| ----------- | ---- | -------- | ------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Fifth, thereferencearchitectureallowsforanad-
| data, as | opposed | to transmitting | data | (as it | has been |        |           |            |     |              |         |     |
| -------- | ------- | --------------- | ---- | ------ | -------- | ------ | --------- | ---------- | --- | ------------ | ------- | --- |
|          |         |                 |      |        |          | vanced | analytics | component. |     | This enables | machine |     |
traditionallyseen).
|           |              |            |        |            |          | learning                      | experts | to build           | predictive | models           | against    | a   |
| --------- | ------------ | ---------- | ------ | ---------- | -------- | ----------------------------- | ------- | ------------------ | ---------- | ---------------- | ---------- | --- |
| In this   | section,     | we discuss | the    | components | of a     |                               |         |                    |            |                  |            |     |
|           |              |            |        |            |          | standardrepresentationofdata. |         |                    |            | Thesemodelscanbe |            |     |
| reference | architecture | built      | around | the FHIR   | profiles |                               |         |                    |            |                  |            |     |
|           |              |            |        |            |          | evaluated                     | and     | used independently |            | of the           | underlying |     |
forlifestyledata.
|     |     |     |     |     |     | datasource. | Thetypeofmodelsparticularlysuitable |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ----------------------------------- | --- | --- | --- | --- | --- |
First,theplatformshouldhaveaConnectorcom-
|                       |       |                           |             |           |      | to lifestyle | data    | is based | on    | time series | analysis | of     |
| --------------------- | ----- | ------------------------- | ----------- | --------- | ---- | ------------ | ------- | -------- | ----- | ----------- | -------- | ------ |
| ponent to             | allow | consumers                 | to retrieve | lifestyle | data |              |         |          |       |             |          |        |
|                       |       |                           |             |           |      | behavioural  | traces, | in       | order | to predict  | trends   | in be- |
| fromdifferentsources. |       | Theconnectorisrequiredbe- |             |           |      |              |         |          |       |             |          |        |
havioursofinterestoroccurrenceofspecificevents.
| cause lifestyle              |            | data is usually | spread           | across   | a multi-  |        |     |            |     |     |     |     |
| ---------------------------- | ---------- | --------------- | ---------------- | -------- | --------- | ------ | --- | ---------- | --- | --- | --- | --- |
| tude of                      | systems    | and platforms,  | each             | offering | an in-    |        |     |            |     |     |     |     |
| completeviewoftheindividual. |            |                 | Weaimtooffercon- |          |           |        |     |            |     |     |     |     |
|                              |            |                 |                  |          |           | 6 USER |     | EXPERIENCE |     |     |     |     |
| sumers an                    | easy       | way to retrieve | their            | own      | data from |        |     |            |     |     |     |     |
| these various                | platforms. |                 | The connector    | comes    | with      |        |     |            |     |     |     |     |
built-in integrations to the main consumer-oriented In this section, we discuss new ways for customers
| lifestyle | tracking | platforms. | The connector |     | can also |                   |     |     |          |                |          |     |
| --------- | -------- | ---------- | ------------- | --- | -------- | ----------------- | --- | --- | -------- | -------------- | -------- | --- |
|           |          |            |               |     |          | and organisations |     | to  | interact | with lifestyle | records. |     |
be extended by each organisation implementing the Whereas health records are accessed by clinicians in
reference architecture so that it also retrieves data controlledenvironments(aGPclinic,ahospitaletc),
fromcompany-specificinternaldatabasesorsystems. interactionwithlifestylerecordsaremorediverse,in
Theconnectorisalsoresponsibletoretrieveandsend termsofusers,contextandpurpose.
dataintheFHIRformat.Thisensuresinteroperability One such interaction model is that of voice-
between different organisations that have committed enabled services, which, aside from increasing con-
toexposingdatainFHIRformat.
venience,couldremoveahostofaccessibilitybarriers
| Second, | the | architecture | requires | a   | Converter | fromusers. |     |     |     |     |     |     |
| ------- | --- | ------------ | -------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
component, which maps data from proprietary for- Apersonallifestylerecordcouldallowconsumers
mats onto FHIR profiles for lifestyle data. The con- tocreateself-reportedobservations(forexample, re-
verter is also responsible to record the source of the lated to pain levels) using voice-enabled digital as-
information for each FHIR observation created. It sistants. Throughthis, elderlypeoplefacingaccessi-
alsoenactsthebusinessrules,assigningvaluestothe
bilityproblemswhenausingasmartphonecanmore
reliabilityandsensitivityfieldsoftheFHIRprofiles. easilymanageachronicconditionusingvoicetotrack
Theconvertercomponentreliesonalibraryofse- their symptoms. Conversely, when developing these
|     |     |     |     |     |     | interfaces, | itisimportanttoensurethattheyrespond |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------------------------------------ | --- | --- | --- | --- | --- |
lectedFHIRprofilessuitabletocapturecommondata
items in the lifestyle domain. Organisations imple- logicallyasotherwisecouldleadtofrustration.
menting the infrastructure for internal use could de- Similarly,lifestylerecordscanalsobyqueriedby
velop additional FHIR profiles for data they hold in- voice, askingforexampleforthenextphysiotherapy
ternally. Weproposeadevelopmentprocesswhereby sessionbookedatthegym.
231

ICT4AWE2018-4thInternationalConferenceonInformationandCommunicationTechnologiesforAgeingWellande-Health
Due to the nature of the interfaces provided by 8 CONCLUSIONS
| voice enabled | services, |     | the types | of  | data that | can be |     |     |     |     |     |
| ------------- | --------- | --- | --------- | --- | --------- | ------ | --- | --- | --- | --- | --- |
recordedmustbepredefined. Forexample,theAma- FHIR FLI is an open source Personal Lifestyle
| zon Alexa | interface | does | not | allow | users to submit |     |        |                 |           |                   |     |
| --------- | --------- | ---- | --- | ----- | --------------- | --- | ------ | --------------- | --------- | ----------------- | --- |
|           |           |      |     |       |                 |     | Record | that helps both | consumers | and organisations |     |
voice recordings as inputs, hence it would not be to combine and analyse lifestyle data, independently
| possible | to record | qualitative |     | data. | However | most | ofthesourcesystems. |     |     |     |     |
| -------- | --------- | ----------- | --- | ----- | ------- | ---- | ------------------- | --- | --- | --- | --- |
lifestyledatacanberecordedquantitatively.Forthose Using FHIR ensures interoperability, allowing
thatcan’t,quantitativemappingscanbedefined(anu-
|     |     |     |     |     |     |     | consumers | to share data | with | service providers | or  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ---- | ----------------- | --- |
mericalscaleinthecaseofpain)mitigatingthisissue. research institutes and empowering organisations to
sharemoredatawithcustomers.
Thenextstepwearepursuingisassessingthefea-
7 FHIR FLI - OPEN SOURCE sibilityandperformanceofaFHIRbaseddatareposi-
torycomparedwithdatarepositoriesbasedonclinical
IMPLEMENTATION
modelssuchasOpenEHR.
Futureworkshouldalsoconcentrateontheimple-
| Based on | the reference |     | architecture, |     | we have | started |     |     |     |     |     |
| -------- | ------------- | --- | ------------- | --- | ------- | ------- | --- | --- | --- | --- | --- |
mentationofaccesscontrolpoliciesanddevelopment
| development | of   | an open-source |            | implementation |               | -   |                             |            |         |                 |        |
| ----------- | ---- | -------------- | ---------- | -------------- | ------------- | --- | --------------------------- | ---------- | ------- | --------------- | ------ |
|             |      |                |            |                |               |     | ofthemachinelearningmodule. |            |         | Thiswoulddemon- |        |
| FHIR FLI.   | This | acts as        | a starting | point          | for organisa- |     |                             |            |         |                 |        |
|             |      |                |            |                |               |     | strate how                  | large data | sets of | lifestyle data  | can be |
tionswishingtodeployasoftwaresolutionthatcon-
|     |     |     |     |     |     |     | assembled | from individuals | willing | to anonymously |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | ------- | -------------- | --- |
formstotheproposedreferencearchitecture.
sharetheirdatawithresearchinstitutes,tobuildnew
| FHIR | FLI contains |     | a number | of  | FHIR profiles |     |     |     |     |     |     |
| ---- | ------------ | --- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
predictivemodelslinkinglifestylebehaviourstoclin-
| specifically | developed |     | for the | lifestyle | domain. | For |     |     |     |     |     |
| ------------ | --------- | --- | ------- | --------- | ------- | --- | --- | --- | --- | --- | --- |
icalrisksandoutcomes.
| example,          | a profile | to standardise |          | sleep | information, |         |     |     |     |     |     |
| ----------------- | --------- | -------------- | -------- | ----- | ------------ | ------- | --- | --- | --- | --- | --- |
| or for describing |           | a workout      | session. |       | The full     | list is |     |     |     |     |     |
availableathttps://simplifier.net/FhirFli/resources
ACKNOWLEDGEMENTS
| FHIR | FLI offers | out | of the | box | connectors | that |     |     |     |     |     |
| ---- | ---------- | --- | ------ | --- | ---------- | ---- | --- | --- | --- | --- | --- |
allowconsumerstoauthenticateandpulllifestyledata
fromFitbit, GoogleFitandAppleHealthkit. Datais We are indebted to Dr. Dean Mohamedally, our
thenconvertedintothenewFHIRprofilesandsaved projectsupervisor,forguidingourresearch.
intoadocumentdatabase.
| Finally,                                   | FHIR | FLI | contains | a data | visualisation |     |            |     |     |     |     |
| ------------------------------------------ | ---- | --- | -------- | ------ | ------------- | --- | ---------- | --- | --- | --- | --- |
| componentandanAmazonAlexaskillundercurrent |      |     |          |        |               |     | REFERENCES |     |     |     |     |
development.
TheFHIRFLIdatavisualizationcomponentpro-
|          |           |          |           |       |                |     | Arthritis | Research UK (2017).                        | State | of musculoskeletal |     |
| -------- | --------- | -------- | --------- | ----- | -------------- | --- | --------- | ------------------------------------------ | ----- | ------------------ | --- |
| vides an | interface | for both | corporate |       | and individual |     |           |                                            |       |                    |     |
|          |           |          |           |       |                |     | health    | 2017. https://www.arthritisresearchuk.org/ |       |                    |     |
| users to | view and  | analyse  | FHIR      | data. | Using          | the |           |                                            |       |                    |     |
arthritis-information/data-and-statistics/state-of-
dashboard, individual users can view their own per- musculoskeletal-health.aspx.
sonal data, whereas corporate users can view aggre- Bender,D.andSartipi,K.(2013). Hl7fhir: Anagileand
gate anonymised data for all users registered with restfulapproachtohealthcareinformationexchange.
theircompanies. Thedashboarddrawsitsdatafroma In Computer-Based Medical Systems (CBMS), 2013
documentdatabase,butalsoreroutesrequeststhrough IEEE 26th International Symposium on, pages 326–
331.IEEE.
| an Apache | Drill | connector | to  | allow | for larger | scale |     |     |     |     |     |
| --------- | ----- | --------- | --- | ----- | ---------- | ----- | --- | --- | --- | --- | --- |
Conaghan,P.G.,Dickson,J.,andGrant,R.L.(2008).Care
queries(inthecaseofcorporateusers).
|          |     |        |     |       |                |     | andmanagementofosteoarthritisinadults: |                        |     |     | summary |
| -------- | --- | ------ | --- | ----- | -------------- | --- | -------------------------------------- | ---------------------- | --- | --- | ------- |
| The FHIR | FLI | Amazon |     | Alexa | skill provides |     |                                        |                        |     |     |         |
|          |     |        |     |       |                |     | ofniceguidance.                        | Bmj,336(7642):502–503. |     |     |         |
users a fluid interface for making specific prede- Deighton, C., OMahony, R., Tosh, J., Turner, C., Rudolf,
fined queries on FHIR data stored within a docu- M., Group, G. D., et al. (2009). Management of
mentdatabase-queriessuchas”Whatwasmyaver- rheumatoidarthritis:summaryofniceguidance.BMJ,
ageheartrateyesterday?”willretrieveandreturnany 338(mar16 1):b702–b702.
matchingdatathroughtheAmazonAlexadevice.The Downie, W., Leatham, P., Rhind, V., Wright, V., Branco,
skillalsoallowsuserstorecorddataintoadocument J.,andAnderson,J.(1978). Studieswithpainrating
databasethroughanAmazonAlexa, andonceauser scales. Annalsoftherheumaticdiseases,37(4):378–
381.
| has submitted | the | data, | it is | converted | into the | new |     |     |     |     |     |
| ------------- | --- | ----- | ----- | --------- | -------- | --- | --- | --- | --- | --- | --- |
Farrar,J.T.,Young,J.P.,LaMoreaux,L.,Werth,J.L.,and
FHIRprofilesandstoredintothedocumentdatabase.
|     |     |     |     |     |     |     | Poole,R.M.(2001). |     | Clinicalimportanceofchanges |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------------------------- | --- | --- |
Thesourcecodeisavailableathttps://github.com/
inchronicpainintensitymeasuredonan11-pointnu-
| fhirfli |     |     |     |     |     |     | mericalpainratingscale. |     | Pain,94(2):149–158. |     |     |
| ------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | ------------------- | --- | --- |
232

FHIRFLI:AnOpenSourcePlatformforStoring,SharingandAnalysingLifestyleData
Furore (2017). Fhir best practices. https://simplifier.net/
guide/ProfilingAcademy/Best-practices.
Hawker, G. A., Mian, S., Kendzerska, T., and French,
M. (2011). Measures of adult pain: Visual analog
scaleforpain(vaspain),numericratingscaleforpain
(nrs pain), mcgill pain questionnaire (mpq), short-
formmcgillpainquestionnaire(sf-mpq),chronicpain
gradescale(cpgs),shortform-36bodilypainscale(sf-
36bps),andmeasureofintermittentandconstantos-
teoarthritis pain (icoap). Arthritis care & research,
63(S11).
Kanta (2017). Phr for developers. https://www.hl7.org/
documentcenter/public temp B8B93A79-1C23-BA
17-0CD130736D1F56A7/wg/mobile/Kanta%20PHR
%20for%20Developers.pdf.
Kavanagh, R. (2017). How is nhs digital using fhir.
http://www.hl7.org.uk/doc store/FHIR/NHSDigital
FHIR.pdf.
Lean, M.E., Leslie, W.S., Barnes, A.C., Brosnahan, N.,
Thom,G.,McCombie,L.,Peters,C.,Zhyzhneuskaya,
S.,Al-Mrabeh,A.,Hollingsworth,K.G.,Rodrigues,
A. M., Rehackova, L., Adamson, A. J., Sniehotta,
F.F.,Mathers,J.C.,Ross,H.M.,McIlvenna,Y.,Ste-
fanetti, R., Trenell, M., Welsh, P., Kean, S., Ford, I.,
McConnachie, A., Sattar, N., and Taylor, R. (2017).
Primary care-led weight management for remission
of type 2 diabetes (direct): an open-label, cluster-
randomisedtrial. TheLancet.
Mandel, J. C., Kreda, D. A., Mandl, K. D., Kohane,
I. S., and Ramoni, R. B. (2016). Smart on fhir: a
standards-based,interoperableappsplatformforelec-
tronichealthrecords. JournaloftheAmericanMedi-
calInformaticsAssociation,23(5):899–908.
Public Health England (2015). England has the potential
to have the lowest disease burden in the world.
https://www.gov.uk/government/news/england-has-
the-potential-to-have-the-lowest-disease-burden-in-
the-world.
233