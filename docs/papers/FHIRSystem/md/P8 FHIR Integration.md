JournaloftheAmericanMedicalInformaticsAssociation,28(10),2021,2220–2225
doi:10.1093/jamia/ocab110
AdvanceAccessPublicationDate:19July2021
ResearchandApplications
Research and Applications
A novel application of SMARTon FHIR architecture for
interoperable and scalable integration of patient-reported
outcome data with electronic health records
DeliyaB.Wesley,12JosephBlumenthal,1,3ShrenikkumarShah,4RobinA.Littlejohn,1,3
ZoePruitt,1,3RamDixit,1,3Chun-JuHsiao,5ChristineDymek,5andRajM.Ratwani1,23
1MedStar Health Research Institute, Hyattsville, Maryland, USA, 2Georgetown University School of Medicine, Washington,
DistrictofColumbia,USA,3MedStarNationalCenterforHumanFactorsinHealthcare,Washington,DistrictofColumbia,USA,
4MedStarInstituteforInnovation,Washington,DistrictofColumbia,USA,and5DivisionofDigitalHealthcareResearch,Center
forEvidenceandPracticeImprovement,AgencyforHealthcareResearchandQuality,Rockville,Maryland,USA
CorrespondingAuthor:DeliyaB.Wesley,PhD,MedStarHealthResearchInstitute,HealthcareDeliveryResearch,3007
TildenSt.NW,Suite6N,Washington,DC20008,USA(Deliya.B.Wesley@medstar.net)
Received16February2021;Revised14April2021;EditorialDecision15May2021;Accepted26May2021
ABSTRACT
Objective: Despite a proliferation of applications (apps) to conveniently collect patient-reported outcomes
(PROs)frompatients,PROdataareyettobeseamlesslyintegratedwithelectronichealthrecords(EHRs)ina
waythatimprovesinteroperabilityandscalability.WeappliedthenewlycreatedPROstandardsfromtheOffice
oftheNationalCoordinatorforHealthInformationTechnologytofacilitatethecollectionandintegrationofstan-
dardizedPROdata.AnovelmultitieredarchitecturewascreatedtoenableseamlessintegrationofPROdatavia
SubstitutableMedicalAppsandReusableTechnologiesonFastHealthcareInteroperabilityResourcesappsand
scaledtodifferentEHRplatformsinmultipleambulatorysettings.
MaterialsandMethods:Weusedastandards-basedapproachtodeploy2appsthatsourceandsurfacePRO
datainreal-timeforproviderusewithintheEHRandwhichrelyonPROassessmentsfromanexternalcenterto
streamlineappandEHRintegration.
Results:Theappsweredevelopedtoenablepatientstoanswervalidatedassessments(eg,aPatient-Reported
Outcomes Measurement Information System including using a Computer Adaptive Test format). Both apps
weredevelopedtopopulatetheEHRinrealtimeusingtheHealthLevelSevenFHIRstandardallowingproviders
toviewpatients’dataduringtheclinicalencounter.Theprocessofimplementingthisarchitecturewith2differ-
entappsacross18ambulatorycaresitesand3differentEHRplatformsisdescribed.
Conclusion:Ourapproachandsolutionprovedfeasible,secure,andtime-andresource-efficient.Weofferac-
tionableguidanceforthistechnologytobescaledandadaptedtopromoteadoptionindiverseambulatorycare
settingsandacrossdifferentEHRs.
Keywords:patient-reportedoutcomes,HL7FHIR,interoperability,datastandards,electronichealthrecord,patientgenerated
healthdata
VCTheAuthor(s)2021.PublishedbyOxfordUniversityPressonbehalfoftheAmericanMedicalInformaticsAssociation.
Allrightsreserved.Forpermissions,pleaseemail:journals.permissions@oup.com 2220

JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.10 2221
Figure1.TimelineforPhase1andPhase2.
INTRODUCTION Tobegintoaddressthesechallenges,theOfficeoftheNational
CoordinatorforHealthInformationTechnology(ONC),partofthe
Apatient-reportedoutcome(PRO)isametricreporteddirectlyby
UnitedStatesDepartmentofHealthandHumanServices,developed
thepatientabouttheirownhealthandqualityoflife,presentingan
standardsspecifictoPROsandreleasedanewPROFastHealthcare
opportunitytoinformpatientcareonanindividualandpopulation-
InteroperabilityResources(FHIR)implementationguide(IG)detail-
level.1PROsofferacomplementaryperspectivetothatofprovider
ingsuchstandards.7
assessmentsandmayprovidegreaterinsightsintoapatient’shealth
status,function,symptomburden,adherence,andhealthbehaviors.
Historically, PROs have been captured through structured inter- OBJECTIVE
viewsorpaperformsintheprovider’soffice,limitingtheiruseand
usabilitybypatientsandhealthcareproviders.2Recently,therehas Inthisimplementationproject,weimplementanovelapplicationof
beenaproliferationofdigitalapplications(apps)thatcanberapidly Substitutable Medical Applications, Reusable Technologies
developed to collect PRO data. These apps now allow patients to (SMART)onFHIRarchitecturetobetterandmoreefficientlyinte-
answerPROsurveysondevicessuchassmartphonesortablets,or gratePROappdatawithmultipleEHRs.WeinstantiatetheONC’s
on a computer, making it easier to collect PRO data.3–5 Research standardstodeterminewhethertheyenablegreaterinteroperability
hasshownthattheseappscanaddresspreviouslydocumentedchal- and scalability between different PRO apps and EHRs. Using
lengesaroundusabilityandaccessibilityandcanreducepatientbur- SMARTandthePROFHIRIG,twodifferentPROappswereinte-
denfromcumbersomeandrepeateddataentry. gratedwithmultipleEHRsindifferentambulatorycaresettings.We
The widespread adoptionof PROappsbypatientsandhealth- describetheprocessandresultsofourimplementationanddiscuss
carefacilitiesisstilllimitedinlargepartbecauseappsmustbecus- implicationsofthestandardsandarchitectureforscalablePROdata
tomizedtotheirspecificinstancesofuse,includingcustomizationto captureanduse.
integratewithahealthcarefacility’selectronichealthrecord(EHR).
WithEHRsusedbyover90%ofhealthcarefacilitiesintheUnited
MATERIALSANDMETHODS
States, as well as many other countries, PRO data should be inte-
grated in the EHR to support provider workflow and, ultimately, Applyingthearchitectureacrossdifferentapps,EHRs,
clinicaldecision-making.InstanceswherePROappshavebeeninte- andhealthcarefacilities
grated with the EHR have shown promise. Yet, researchers who Twodifferentappswereintegratedandpilot-testedat18ambula-
havedonethisworknotethatacoresetofcross-cuttingstandards torycarefacilitiesacrossMedStarHealth,alarge,not-for-profit,in-
forappandEHRintegrationarenecessarytoprovideaplatformfor tegrated healthcare delivery system in the Maryland/Washington,
widespread adoption.6 The convergence and optimization of PRO DCregion.Theappsweretestedin2phases(Figure1).Acommer-
data collection for clinical use and research is dependent on a ciallyavailableapp was the focus of Phase 1. After completionof
standards-basedsolutionthatissecure,interoperable,andscalable thisintegrationandpilotassessment,asecond,newlydevelopedapp
toenabletheconnectionofnowwidelydevelopedPROappswith was integrated and pilot-tested during Phase 2, leveraging lessons
EHRs.4 learnedfromthephase1integration.Participatingsiteswereofvari-
ThelackofstandardsforthecaptureandexchangeofPROdata, ous sizes and geographies (rural, urban, suburban), had varied
aswellastheintegrationofPROdatainEHRs,posesseveralspe- workflows,andserveddifferentpatientpopulations.
cificchallenges.First,itmakesitdifficultforappdeveloperstouni- Phase 1: The commercial app was a cloud-based PRO app
formly use validated PRO measures, such as the Patient-Reported hosted by HIPAA-compliant Amazon Web Services. The original
OutcomesMeasurementInformationSystem(PROMIS)sincethere app’s ecosystem relied on proprietary standards and technologies.
isvariabilityinthewaytheitemsandresponsescanberepresented. Cliniciansandpatientsaccessedtheappbyusinganindividuallogin
Second, providers may want patients to complete different PRO createdbyregisteringanaccountforeachuser.Theappwasprevi-
measures, and, without standards, the methods of assigning meas- ouslyusedinanorthopedicsettingtocollectdemographicandPRO
ures to patients can vary across apps and result in data that are databyimplementinglogictoadaptivelyservecontent.Itwasnot
harder to interpret. Finally, without standards for how PRO data integrated with the EHR and requiredproviders to navigate to an
arerepresented,integrationwiththeEHRrequiresacustomizedap- external,vendor-hostedsitewithseparatecredentialstoretrieveand
proachforeachPROandEHRinstance,whichcanbeburdensome viewthePROdata.Wemodifiedtheapptobringituptotheindus-
andlimitsscalability. trystandardofHealthLevelSeven(HL7)SMARTonFHIRusing

2222 JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.10
Figure2.ComponentsoftheDataonDemandarchitectureshowingdirectionaldataflow.
theONCPROFHIRIG.PatientsaccessedandcompletedthePRO sessmentcenter(EAC),andaweb-basedprovider-facinginterfacein
instrumentusingtabletsprovidedateachclinic. theEHR(seeFigure2andTable1).
Phase2:Thesecondapp,developedspecificallyfortheAgency
| for Healthcare | Research | and | Quality (AHRQ) |     | challenge | competi- |     |     |     |     |     |     |     |     |
| -------------- | -------- | --- | -------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
FHIR-enabledPROcollectionapp
tionfocusedonPROsandwasbuiltusingtheONCPROFHIRIG,
Ourappintegrationandimplementationweredesignedtofacilitate
| resultingin | an architecture | where | the | chosen cloud | provider | hosts |     |     |     |     |     |     |     |     |
| ----------- | --------------- | ----- | --- | ------------ | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
datacollectioneitherusinganapproachinwhichthehealthcarefa-
andscalesthesolution.Inthisphase,weusedthe“bringyourown
cilityprovidedadevice(tablet)forpatientstouse,oraBYODap-
device”(BYOD)approachtodeterminefeasibilityofhavingpatients
|     |     |     |     |     |     |     | proach | using a | patient’s | own | compatible | smartphone. |     | Both |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --------- | --- | ---------- | ----------- | --- | ---- |
completethePROinstrumentontheirowndeviceateachofthe9
|     |     |     |     |     |     |     | approaches | allowed | patients | to register | and | complete | their | assess- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | ----------- | --- | -------- | ----- | ------- |
additionalsites.Allaspectsofthisstudywereapprovedbyaninde-
|     |     |     |     |     |     |     | ments within | the | app (in | this case, | validated | PROMIS |     | question- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ---------- | --------- | ------ | --- | --------- |
pendentInstitutionalReviewBoard(IRB).
|     |     |     |     |     |     |     | naires). Patients                              | who | used | the practice’s |     | device | accessed | the pre- |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | ---- | -------------- | --- | ------ | -------- | -------- |
|     |     |     |     |     |     |     | loadedapponcetheyarrivedfortheirappointment.In |     |      |                |     |        | theBYOD  |          |
model,patientswhoconsentedtosharetheirPROdatawiththeir
RESULTS providers downloaded the app on their device, completed the
assignedassessment,andwereabletoreviewtheirresults.
Weintegrated2differentPROapps,1commerciallyavailableprod-
Inbothscenarios,patients’accountswerelinkedtotheirunique
uctand1productnewlydevelopedspecificallyfortheAHRQchal-
medicalrecordidentifierintheEHR,allowingproviderstosecurely
| lenge competition. |     | The same | ONC PRO | FHIR | IG was | used to |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | ------- | ---- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
modifythecommercialappandtodevelopthenewapp.7Theresult- retrievetheseresponsesimmediatelyupondataentrybythepatient.
TheappsusedSMARTauthenticationandthelatestFHIRprotocol
| ing apps | were built | on a SMART | on  | FHIR security | framework. |     |     |     |     |     |     |     |     |     |
| -------- | ---------- | ---------- | --- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toauthenticatepatientcredentials,administertheassessments,and
| SMARTisasecuritystandards-basedplatformthatallowsthe |                    |     |                |      |      | de-      |          |               |     |          |                |     |            |     |
| ---------------------------------------------------- | ------------------ | --- | -------------- | ---- | ---- | -------- | -------- | ------------- | --- | -------- | -------------- | --- | ---------- | --- |
|                                                      |                    |     |                |      |      |          | transfer | the responses | to  | the data | hub (described |     | in section | (2) |
| velopment                                            | of interchangeable |     | healthcareapps | that | draw | from and |          |               |     |          |                |     |            |     |
communicatewithanyEHRdatainahealthcarefacility.8ThePRO Cloud-Based FHIR Data Hub). The apps also used a cloud-based
|     |     |     |     |     |     |     | middlelayerarchitectureandwere |     |     |     | hostedon | secure | HealthInsur- |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | -------- | ------ | ------------ | --- |
appsweredevelopedtoenablepatientstoanswervalidatedassess-
|            |        |           |       |            |          |      | ance Portability | and      | Accountability |     | Act (HIPAA) |         | compliant | plat- |
| ---------- | ------ | --------- | ----- | ---------- | -------- | ---- | ---------------- | -------- | -------------- | --- | ----------- | ------- | --------- | ----- |
| ments (eg, | PROMIS | including | using | a Computer | Adaptive | Test |                  |          |                |     |             |         |           |       |
|            |        |           |       |            |          |      | forms. To        | initiate | data flow,     | the | apps first  | ensured | patients  | were  |
[CAT]format9).BothappsweredevelopedtopopulatetheEHRin
correctlyregisteredthroughaSMARTStandaloneAppLaunchSe-
realtimeusingtheHL7FHIRstandardallowingproviderstoview
|     |     |     |     |     |     |     | quence, authenticating |     | their | details | with | the FHIR | authorization |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ----- | ------- | ---- | -------- | ------------- | --- |
patients’dataduringtheclinicalencounter.Wedescribetheoverall
serverbeforeallowingtheapptoproceedtodatacollection.Once
architectureandthespecificcomponentsdevelopedtointegratethe
|     |     |     |     |     |     |     | the patient | was authorized, |     | the app | retrieved | the | patient’s | profile |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | --- | ------- | --------- | --- | --------- | ------- |
apps.
fromthedatahubandexchangedresponseswithanexternalassess-
|     |     |     |     |     |     |     | ment center | (EAC) | to appropriately |     | administer |     | the instrument, |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ---------------- | --- | ---------- | --- | --------------- | --- |
whichutilizedcomputeradaptivetesting(CAT).Theresponseswere
Architectureoverview
thenstoredasFHIRQuestionnaireResponseitemsinthedatahub.
| The primary | objective | of our        | architecture | was | to instantiate  | the |     |     |     |     |     |     |     |     |
| ----------- | --------- | ------------- | ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ONC PRO     | FHIR      | IG and design | a secure     | and | scalable method | by  |     |     |     |     |     |     |     |     |
whichstructuredPROsurveydatacollectedfromathird-partyapp Cloud-basedFHIRdatahub
couldbeintegratedwithdifferentEHRs.Wedevelopedanarchitec- TheONCPROFHIRIGinstantiatedinourarchitecturehasnotyet
tureenablingthedisplayofpatientdata“OnDemand”(described beenwidelyadoptedbyEHRvendorsresultinginthepotentialneed
below),andanoveralltemplateadaptableforimplementationatdif- forcustomdevelopmenttointegratetheappwitheachEHRprod-
ferentclinicalsitesaddressingdatastorageandretrievalaswellas uct.Toaddressthisissue,akeyfeatureofourapproachwastore-
administration and analysis of survey responses using FHIR end- duce the complexity of integration needed between the PRO app
points.Thepatient-centricdatafloworiginatedwiththepatientand andEHRsbyusinganintermediarydatahub.Thedatahubisase-
flowed to the provider in a clinical setting. The architecture con- cureclouddatabaseandFHIRendpointthathandlespatientauthen-
sistedof4maincomponents:thepatient-facingFHIR-enabledPRO ticationalongwithexchangeandstorageofPROdata.StoringPRO
datacollectionapp,acloud-basedFHIRdatahub,anexternalas- data in this intermediary layerfacilitatesan easilyscalable “light”

JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.10 2223
Table1.DataonDemandarchitecturecomponentdescriptions
| Component |     |     |     | Task                                            |     |     |     |     |     |     |
| --------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
| A         |     |     |     | PatientopensthePROapptoaccessassignedinstrument |     |     |     |     |     |     |
| B         |     |     |     | Patiententerscredentials                        |     |     |     |     |     |     |
C PatientcredentialsverifiedthroughtheFHIRauthorizationserver
D Thenowauthorizedappretrievespatient’sprofilefromthe“datahub”andservespatientthefirstsur-
veyitemfromtheEAC
Patient’ssurveyresponsedeterminessubsequentsurveyitemservedviaCATintheEAC
EACservessubsequentitemsuntilpatientcompletes‘n’itemsdeterminedbyCAT
| E   |     |     |     | CompletedsurveyresponsesarestoredintheFHIRenableddatahub |     |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| F   |     |     |     | Providerreadytoviewpatients’datalogsintoHER              |     |     |     |     |     |     |
Provideraccessespatient’schartthroughHER
G,H EHRpullssurveyresponsesfrom‘datahub’andtransferstoEHRforrealtimedisplay
Q Question1(throughn)/firsttonthsurveyitemservedfromEACtothepatient
1-n
| A   |     |     |     | Answer1(throughn)/firsttonthsurveyresponsefrompatienttoEAC |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
1-n
EHR integration where data can be retrieved from the hub when the web component was embeddedin the patient’s chart, the pro-
needed by providers. This approachleveraged FHIR standards for viderinterfaceonlyretrieveddatarelevanttothatspecificpatient.
exchangingPROdatatoshifttheburdenofstoringPROdatawithin
| each EHR | implementation’s |     | unique | and often complicated |     | clinical |     |     |     |     |
| -------- | ---------------- | --- | ------ | --------------------- | --- | -------- | --- | --- | --- | --- |
datamodelontothecloudwhereitcouldbedynamicallyaccessed Appusageandsiteimplementation
| throughasecurewebinterfaceembeddedintheEHR.Thedatahub |     |     |     |     |     |     | Phase1 |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
alsoincludesanadministratorinterfacewhichallowsclinicstaffto All90consentingpatientswereabletoaccessandusetheapptoen-
registerpatientsinthesystem,reviewtheircompletedPROsurveys, tertheirPROdataimmediatelypriortotheirappointment.Patients
and troubleshoot issues that patients may have with their account all used tablets providedby the clinic at registration. All practices
access.
|     |     |     |     |     |     |     | had full technical | assistance | to support the integration | and imple- |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ---------- | -------------------------- | ---------- |
mentation,learningsfromwhichinformedPhase2integrationand
implementation.NoneofthepatientshaddifficultiesusingthePRO
Externalassessmentcenter
app,andnoneoftheprovidershaddifficultyaccessingPROdatain
| The external | assessment | center | (EAC) | is an agnostic | decentralized |     |     |     |     |     |
| ------------ | ---------- | ------ | ----- | -------------- | ------------- | --- | --- | --- | --- | --- |
theirrespectiveEHR.
| engine that | serves survey | questions |     | based on predetermined |     | logic |     |     |     |     |
| ----------- | ------------- | --------- | --- | ---------------------- | --- | ----- | --- | --- | --- | --- |
and/orpreviousresponsestoasurvey.TheEACwasusedtoadmin-
| isterCAT | and to track | andanalyzepatients’ |     | PRO | data.The | EAC |     |     |     |     |
| -------- | ------------ | ------------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
Phase2
implementedthelogictocapturethePROMISassessments,produc-
Attheendoftheenrollmentperiod,84patientsconsented,and58
ingaFHIR-formattedbundleofresponsesandscoresinastandard-
patientswereabletosuccessfullyaccessanddownloadtheappon
| ized format. | The FHIR | IG  | provided | specifications | for | the EAC, |     |     |     |     |
| ------------ | -------- | --- | -------- | -------------- | --- | -------- | --- | --- | --- | --- |
theirdevicestoentertheirPROdataacrossthe9practicesites.The
allowingamoregeneralizable,scalable,andmoresecuresolutionto
remainingpatientswereunabletousetheapptocompletiondueto
| buildinga | survey question | distributor. |     | Weused | SMARTon | FHIR |     |     |     |     |
| --------- | --------------- | ------------ | --- | ------ | ------- | ---- | --- | --- | --- | --- |
technicalchallengesrelatedtotheirsmartphones.Thisincludedcon-
| and Questionnaire | Response |     | resources | as per HL7 | FHIR | R4. The |     |     |     |     |
| ----------------- | -------- | --- | --------- | ---------- | ---- | ------- | --- | --- | --- | --- |
nectivityissues(lackofaccesstowi-fiorinsufficientbroadbandac-
standardizationofbidirectionaldataflowprovidesastreamlinedso-
cess),orlackofcompatiblesmartphoneoroperatingsystemontheir
lutionrelyingonopenstandards.
devices.Atotalof13providersaccessedthepatients’previouslyen-
|     |     |     |     |     |     |     | tered data during | their encounter | with the patients. | Each practice |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --------------- | ------------------ | ------------- |
Web-basedproviderapp hadvaryinglevelsoftechnicalassistancetosupporttheintegration
Once the patient completed their PRO assessment, their provider and implementation. The challenges the patients faced with using
wasabletoaccessthesedatathroughthepatient’schartintheEHR. thePROappwereunrelatedtothestandardsandarchitecture.The
Thiswasenabledbyasinglepageembeddedapplication,whichau-
providerswereabletoaccessthePROdata,whensuccessfullyen-
thenticatedtheprovider’scredentialsandretrievedpatientdataspe- teredthroughtheapp,withoutanychallenges.
cifictothecharttheproviderwasaccessing.ToviewthePROdata,
theproviderhadaccesstoavisualizationofthePROscoresthrough
webpagesthatwereviewablewithintheEHR.EachEHRproduct
DISCUSSION
| had pathways | to surface | custom | visualizations |     | using modern | web |     |     |     |     |
| ------------ | ---------- | ------ | -------------- | --- | ------------ | --- | --- | --- | --- | --- |
programming languages including HyperText Markup Language ThewidespreadadoptionofPROappsrequiresamorestandardized
(HTML),CascadingStyleSheets(CSS),andJavaScript.Thesecus- processtocapturePROdatafrompatient-facingappsandtointe-
tomvisualizationscannativelycommunicatewithRepresentational gratethisinformationwiththeEHRforclinicaluse.TheONChas
State Transfer (RESTful) APIs using JavaScript Object Notation developed the PRO FHIR IG to address these needs; however, to
(JSON) upon which the FHIR standard is modeled. The general date,thesestandardshavenotbeen instantiatedin an architecture
structureforeachinterfacewasabletotakeadvantageofgeneral, andimplemented across apps,EHRs, andhealthcarefacilities. We
system-level SMART on FHIR authorization and authentication have demonstrated that these standards can be used to seamlessly
standards to seamlessly validate the provider’s access to the data, capture PRO data, and these data can be made available to clini-
| preventingtheneedforanadditionalauthenticationstep.Finally,as |     |     |     |     |     |     | cianson-demand. |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- |

2224 JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.10
AdaptationofthearchitecturetodifferentEHRs tionalsecurityinfrastructuretobuildsincetheEACdoesnotstore
EvenwiththeONCPROFHIRIGthereweresomechallengesand anyprotectedhealthinformation.
keylessonslearnedasweimplementedourarchitecturetoconnect Healthsystemlevelapprovalsnecessaryforfullappintegration
PRO data from the 2 apps with different EHRs. Several of these andappdeployment: One of the most significantbarriers encoun-
were realized in the Phase 1 implementation, allowing for a more tered,particularlyinPhase2,wasunanticipateddelaysinimplemen-
optimizedimplementationinPhase2. tationduetoahealthsystem’sinstitutionalpoliciesandregulations
EHR-specific differences in provider web app implementation: necessary to secure approval and clearance to integrate new PRO
Implementation of the provider-facing web app at the 18 clinical apptechnologywiththehealthsystem’snativeinformationsystems
sitesyieldedkeyinsightsrelatedtotheirEHRdifferences.Theim- architecture.Thesepoliciesandregulationswilllikelybehighlyvari-
plementationprocessesin2differentEHRswerefoundtohavedif- ablebyinstitutionbutwillneedtobeanticipatedinanyimplemen-
ferentunderlyingbrowserstacks,whichresultedinthecreationof2 tation timeline. Technical teams should allow significant time to
different provider-facing visualizations. The advantages of navigatetheseprocessesandtomeetinstitutionalrequirements,par-
standards-basedSMARTsecurityandFHIRdataexchange donot ticularlywhennewvendorsareworkingwithasystemforthefirst
eliminatethevendorandEHR-specificvariationsinhowthesedata time(see“DemandManagement”ontimelineinFigure1).
visualizationsmayberendered.OnesalientexampleisiftheEHR These issues all highlightcritical points at which the coordina-
only provides older platforms for custom data visualization, the tionofhumanandtechnicalprocessesiscrucialtoensurethesuc-
suiteoftoolsfordevelopmentofadvancedvisualizationsmaynotbe cessful use of PRO data. There are a few limitations to our
available.Insomecases,thismayintroducevariabilityinthemeth- implementationstudy.First,PRO appimplementationandpatient
ods by which the provider-facing web interface brokers communi- andproviderenrollmentwerecloselycontrolledbythestudyteam
catewithservers.Wefoundhavingaconsistenttargetplatformfor inPhase1.Thisexperiencedoesnotrepresenttheclinicalimplemen-
webappdevelopmentiscriticaltocross-siteprovider-facingvisuali- tationprocessesanduse“inthewild”whereadedicatedstudyteam
zationimplementation. and intervention by a research coordinator or other facilitator
Necessity to design for the least amount of client variability: wouldnotbeavailable.However,thisstudydemonstratedfeasibil-
EHRscanbeinstalledinworkstationsinavarietyofways,includ- ityand,inPhase2,providedkeyinsightsaboutthelevelofresources
ing a local installation or as a remote display such as Citrix. The needfor eachcomponent of implementation.These resultsare de-
EHR installation method can affect performance and render any scribedseparately.Second,thereislikelyselectionbiasintermsof
third-partyappunlessthatrenderingistightlycoupledwiththecli- theclinics,providers,andpatientswhoagreedtoparticipate.Actual
ent. We therefore implemented the PRO provider-facing app in a adoptionbyprovidersandpracticesislikelyhighlyvariable.Despite
way that allowed us to manage client level variability as much as theselimitations,wesuccessfullydemonstratedfeasibilitythat,with
possible,andinawaythatmadeiteasiertoaddresstechnicalissues somemodifications,theSMARTonFHIRplatformeffectivelybrid-
from installation variability without extensive support from the gesthegapbetweenefficientcollectionofPROsurveyswithhighly
EHRvendor.Thiswasachievedbyusingbasictoolsforimplement- usablepatient-facingapps,seamlessEHRintegration,andreal-time
ingthecustomdatavisualizationaswellasprovidingamiddletier provideraccessanduseofPROdata.
(thedatahub). The SMART specification and design allow this solution to be
Avoiding user re-authentication by using the EHR as the deployedinanyclinicalsettingandisnotconfinedtoambulatory.
trusted app: Under our current architecture, because the provider Futureworkisneededtoidentifycommonimplementationfacilita-
was already logged into the EHR, the most efficient workflow torsandbarriersacrossdifferentclinicalcontextstoinformfuture
wasachievedbylaunchingtheprovider-facingwebappwithinthe adoption.
EHR and avoiding user re-authentication. This approach treated
theEHRasthetrustedapp.Welockeddownourwebapptospe-
cific EHR Internet Protocols (IPs), thus allowing it to work se-
CONCLUSION
curely from within the EHR. The provider-facing app that was
visible from withinthe EHR never storedany data locally and al- Wewereabletosuccessfullydeploythisarchitecturein18clinical
ways used HTTPs for secured transmission of data. These func- sites and across 3 EHR platforms, facilitating integration of PRO
tions were all achieved with minimum modification to the actual data into the ambulatory care workflow using the PRO FHIR IG.
EHR, making it relatively easy to install on different EHRs, and Our approach demonstrated the ability to take standards-based
scalableasaresult. technical guidance specific to PROs and translate these into func-
BuildinganExternalAssessmentCentertosupportthesolution tional solutions for different systems and clinical settings. Further
at different sites: Across both phases of PRO app integration, we ourimplementationandtestingindistinctambulatorysettingsdem-
employeddifferentmodificationstoincorporatetheEAC.TheEAC onstratedthevalueofournovelarchitecture’s(“thehub”)scalabil-
is generally ‘buy-or-build’. Building an EAC to provide adaptive ityandinteroperability.TheuseofSMARTonFHIRstandardswas
contentrequiresdomainexpertise,istechnicallychallenging,andre- importantin3distinctaspects:1)Facilitatedthecreationofadata
sourceintensive.However,thetradeoffforthisisthecostincurred hub, which provided an intermediary layer capable of receiving
from licensing fees to implement the existing EAC. Not using an PROdatafromthird-partyappsinastructuredFHIRformat;2)Fa-
EACforthemanagementofcontentwouldleadtoincreaseddevel- cilitated secure SMART user authentication and storage of these
opment costs, prolonged timelines, and greater customization for data;and3)Providedastandardtargetforweb-basedEHRinterfa-
eachimplementationofthetoolindifferenthealthcarefacilitiesand ces that reduced the burden for “deep” integration of PRO data
EHRproducts.InPhase1ofourimplementation,theEACwasbuilt withcomplicatedEHRclinicaldatamodels.Theseaspectsarepar-
bythevendor.ForPhase2,itwaslicensedandcustomizedforthe ticularlyimportant, given the hundredsof different EHR products
build. Whether the approach is to buy or build, there is no addi- usedinambulatorycaresettings.

JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.10 2225
FUNDING REFERENCES
ThisworkwasfundedbytheAgencyforHealthcareResearchandQuality’s 1. DeshpandeP,SudeepthiB,RajanS,etal.Patient-reportedoutcomes:anew
ContractNo.233-2015-000221-4whichwasfundedbytheOfficeoftheSec- erainclinicalresearch.PerspectClinRes2011;2(4):137.
retary Patient-Centered Outcomes Research Trust Fund under Interagency 2. CoonsSJ,EremencoS,LundyJJ,etal.Capturingpatient-reportedoutcome
Agreement#HP-17-003. (PRO)dataelectronically:thepast,present,andpromiseofePROmeasure-
mentinclinicaltrials.Patient2015;8(4):301–9.
3. BlackN.Patientreportedoutcomemeasurescouldhelptransformhealth-
care.BMJ2013;346(jan281):f167.
AUTHORCONTRIBUTIONS
4. LavalleeDC,ChenokKE,LoveRM,etal.Incorporatingpatient-reported
Allauthorscontributedtotheanalysisanddraftingofthemanuscript.Allauthors outcomesintohealthcaretoengagepatientsandenhancecare.HealthAff
approvedthefinalworkandareaccountablefortheresults. (Millwood)2016;35(4):575–82.
5. ValderasJM,KotzevaA,EspallarguesM,etal.Theimpactofmeasuring
patient-reportedoutcomesinclinicalpractice:asystematicreviewofthelit-
erature.QualLifeRes2008;17(2):179–93.
DATAAVAILABILITYSTATEMENT
6. JensenRE,RothrockNE,DeWittEM,etal.Theroleoftechnicaladvances
Theanalyzeddatasetisavailablefromthecorrespondingauthoruponre- in the adoption and integration of patient-reported outcomes in clinical
quest. care.MedCare2015;53(2):153–9.
7. USCoreImplementationGuide(FHIRIG).http://www.hl7.org/fhir/us/pa-
tient-reported-outcomes/2018Sep.AccessedJanuary24,2021.
8. MandelJC,KredaDA,MandlKD,etal.SMARTonFHIR:astandards-
CONFLICTOFINTERESTSTATEMENT based,interoperableappsplatformforelectronichealthrecords.JAmMed
InformAssoc2016;23(5):899–908.
Nonedeclared.Thefindingsandconclusionsinthismanuscriptarethoseof
9. BroderickJ,DeWitEM,RothrockN,etal.Advancesinpatientreported
the authors and do not necessarily represent the official position of the
outcomes:TheNIHPROMISmeasures.EGEMS2013;1(1):12.
AgencyforHealthcareResearchandQuality.