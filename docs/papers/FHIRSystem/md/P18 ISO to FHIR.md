OPENACCESS
ResearchArticle
| Mapping     |     | of  | medical |     | device |     | data | from | ISO/IEEE |
| ----------- | --- | --- | ------- | --- | ------ | --- | ---- | ---- | -------- |
| 11073-10207 |     |     | to      | HL7 | FHIR   |     |      |      |          |
AbbildungmedizinischerGerätedatenvonISO/IEEE11073-10207nach
HL7 FHIR
Abstract
The ISO/IEEE 11073-10207 Domain Information and Service Model KathrinPiaRiech1
focuses on cross-manufacturer device-to-device communication, HannesUlrich2
whereasHL7FastHealthcareInteroperabilityResources(FHIR)support
JosefIngenerf1,2
thedataexchangebetweensoftwaresystemsinhealthcare.Thecon-
tentsofbothstandardsoverlap,yettheydifferinstructure.Inthiswork, BjörnAndersen1
wepresentanImplementationGuidethatcontainsamappingofmed-
| icaldevicedatafrom |     | ISO/IEEE11073-10207 |     |     |     | to HL7 | FHIRin | order to |     |
| ------------------ | --- | ------------------- | --- | --- | --- | ------ | ------ | -------- | --- |
1 InstituteofMedical
improvevendor-independentinteroperability.ThisImplementationGuide
Informatics,Universityof
| helps to | bridge | the structural | interoperability |     |     | gap between |     | these two |     |
| -------- | ------ | -------------- | ---------------- | --- | --- | ----------- | --- | --------- | --- |
Lübeck,Germany
communicationarchitecturesformedicaldevicesandclinicalinformation
systems.Thisfurthermorepromotesthereuseofmedicaldevicedata, 2 ITCenterforClinical
Research,Universityof
e.g.forclinicalresearchpurposes.
Lübeck,Germany
Tofacilitatethemappingwhileretainingcontextualinformationdespite
thestructuraldifferences,itwasonlynecessarytocreatefiveprofiles
fortwoFHIRresources.ThisImplementationGuideisdescribedinrela-
tiontosimilareffortsincludingdifficultiesthataroseduringtheimple-
| mentation | of the | mapping. | Approximately |     | 25  | problems | occurred, | but |     |
| --------- | ------ | -------- | ------------- | --- | --- | -------- | --------- | --- | --- |
inallcasestheyarenotcriticalandmostofthemcouldbesolvedfor
| our use cases. |     | In the future, | this | work | will be | merged | with | the Imple- |     |
| -------------- | --- | -------------- | ---- | ---- | ------- | ------ | ---- | ---------- | --- |
mentationGuideforpoint-of-caremedicaldevices.
Keywords:ISO/IEEE11073SDC,HL7FHIR,medicalcommunication
standards,systeminteroperability
Zusammenfassung
| Das ISO/IEEE     | 11073-10207 |                    | Domain                      |          | Information | and              | Service           | Model |     |
| ---------------- | ----------- | ------------------ | --------------------------- | -------- | ----------- | ---------------- | ----------------- | ----- | --- |
| konzentriert     | sich        | auf                | die herstellerübergreifende |          |             |                  | Device-to-Device- |       |     |
| Kommunikation,   |             | während            | HL7                         | Fast     | Healthcare  | Interoperability |                   | Re-   |     |
| sources          | (FHIR)      | den Datenaustausch |                             | zwischen |             | Softwaresystemen |                   | im    |     |
| Gesundheitswesen |             | unterstützt.       |                             | Beide    | Standards   | überschneiden    |                   | sich  |     |
inhaltlich,unterscheidensichjedochinihrerStruktur.IndieserArbeit
stellenwireinenImplementationGuidevor,derdieAbbildungmedizini-
scherGerätedatenvonISO/IEEE11073-10207nachHL7FHIRenthält,
| um die herstellerunabhängige |     |     | Interoperabilität |     |     | zu verbessern. |     | Dieser |     |
| ---------------------------- | --- | --- | ----------------- | --- | --- | -------------- | --- | ------ | --- |
ImplementationGuidehilftbeiderÜberbrückungderstrukturellenIn-
teroperabilitätslückezwischendiesenbeidenKommunikationsarchitek-
turenfürMedizinprodukteundklinischeInformationssysteme.Darüber
hinausförderterdieSekundärnutzungmedizinischerGerätedaten,z.B.
fürklinischeForschungszwecke.
UmdieAbbildungzuerleichternundgleichzeitigtrotzderstrukturellen
| Unterschiede | die  | Kontextinformationen |          |                 | zu erhalten, |     | war es     | lediglich |     |
| ------------ | ---- | -------------------- | -------- | --------------- | ------------ | --- | ---------- | --------- | --- |
| notwendig,   | fünf | Profile              | für zwei | FHIR-Ressourcen |              | zu  | erstellen. | Dieser    |     |
ImplementationGuidewirdinBezuggesetztzuähnlichenBemühungen
| einschließlich | der | Schwierigkeiten, |     | die | bei der | Implementierung |     | des |     |
| -------------- | --- | ---------------- | --- | --- | ------- | --------------- | --- | --- | --- |
Mappingsaufgetretensind.Estratenetwa25Problemeauf,dieaber
inallenFällennichtkritischsind.FürunsereAnwendungsfällekonnte
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 1/10

Riechetal.:MappingofmedicaldevicedatafromISO/IEEE11073-10207...
überwiegendeineLösungerarbeitetwerden.DiehiervorgestelltenLö-
sungenwerdeninZukunftmitdemImplementationGuidefürPoint-of-
Care-Medizingerätezusammengeführt.
Schlüsselwörter:ISO/IEEE11073SDC,HL7FHIR,medizinische
Kommunikationsstandards,System-Interoperabilität
| Introduction |     |     |     |     |     |     | ofcurrentwebstandardsandfocusesonaneasyimple- |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
mentation.
Inclinicalenvironments,communicationtakesplacenot
Interoperabilityisakeyfactorforthesuccessofinforma-
tionsystemsinhealthcare.Withtheincreasingnumber onlywithinthedomainsofmedicaldevicesandclinical
ofmedicaldevicesandclinicalinformationsystems,there information systems, but also between them. Focusing
|     |     |     |     |     |     |     | on only | one of | these | two domains | would | not | lead to a |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ----- | ----------- | ----- | --- | --------- |
isalsoagrowingdemandforvendor-independentinter-
operability to integrate medical systems and software holistic solution. Interoperability between devices and
informationsystemsisthereforenecessarytomaximise
solutionsintoacomprehensiveinfrastructureinoperating
rooms,intensivecareunits,andhospitalsingeneral. the potential for optimising healthcare delivery and
Whereastherearealreadysolutionsforintegratedoper- streamliningclinicalworkflows.
|     |     |     |     |     |     |     | An Implementation |     | Guide | (IG) | is a document |     | published |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----- | ---- | ------------- | --- | --------- |
atingroomscommerciallyavailable,theyofferlittleflex-
ibility,asonlydevicesfromthesameproprietaryecosys- byadomain,institution,orprovider.Itcharacteriseshow
HL7FHIRistunedtosupportaparticularusecaseora
| tem can | be used, | which usually | significantly |     | limits | the |     |     |     |     |     |     |     |
| ------- | -------- | ------------- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
choiceofdevicesforaspecificusecase.Onceadecision set of use cases. In this context, the use of medical
hasbeenmadeinfavourofoneofthesesolutions,the devicesusingtheISO/IEEE11073SDCcommunication
protocolisausecasetowhichHL7FHIRshouldbeadap-
dependencyontheproviderisveryhigh.Inmanycases
it is thus not possible to integrate the best device for a ted. Such an IG comprises a collection of functional in-
|     |     |     |     |     |     |     | structions, | profiles, | value | ranges, | and | documentation |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ----- | ------- | --- | ------------- | --- |
givenapplicationortoacquiretheproductwiththebest
price-performance ratio. Therefore, an integrated OR describing a variety of interoperable applications. The
basedonmulti-vendorinteroperabilitynotonlyimproves maincomponentinthisworkisthemapping.AnIGthat
|     |     |     |     |     |     |     | includes | the | mapping | of medical | device |     | data from |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | ---------- | ------ | --- | --------- |
thesurgicalworkflowandincreasespatientsafety,itmay
alsobemoreeconomicallyviable[1]. ISO/IEEE11073-10207toHL7FHIRisexpectedtofacil-
|     |     |     |     |     |     |     | itate more | flexible | communication |     |     | between | medical |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------------- | --- | --- | ------- | ------- |
Manufacturer-independentinteroperabilitycancontribute
toimprovinghealthcaredelivery,whereasalackofinter- devicesandclinicalinformationsystemswithoutlossof
| operabilitypreventsthedevelopmentofcooperativeas- |     |     |     |     |     |     | information. |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Theconsistentuseofcommunicationstandardsshould
sistancesystems.Inthecontextofmedicaldevices,inter-
operabilityischaracterisedbytheexchangeofinformation alsoenablethestorageandreferencingofmedicaldevice
datainclinicalrepositoriesinthefuture.Atypicalclinical
betweenindependent,heterogeneoussystems.Semantic
interoperability furthermore enables these systems to information system would filter out a lot of device data
consistentlyinterpretandusetheinformationbeingex- becausethedatamodelisonlyusedtostoreresultsand
findingsratherthanlargeamountsofmeasurementdata
| changed | [1]. This | can be | achieved | through | consistent |     |     |     |     |     |     |     |     |
| ------- | --------- | ------ | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
application of standards that define the syntactic rules frommanymedicaldevices.Also,today’sclinicalITinfra-
structurehardlyincludesextensivedataanalysiscapabil-
andsemanticinterpretationofdata.Tomeetthesespe-
cificneeds,communicationarchitecturesandprotocols itiesthatcouldeffectivelyreusethedata,e.g.toassess
have been developed and standardised. For integrated qualityofcareortoconductclinicalresearch.Onepos-
siblesolutionistheintroductionofclinicalrepositories.
| clinical environments, |     | the | most recent | innovations |     | are |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
captured in the standards ISO/IEEE 11073 Service-ori- They are commonly described as databases that refer-
enceandstoredatafrommultiplesourcestoenablee.g.
entedDeviceConnectivity(SDC)andHL7FastHealthcare
InteroperabilityResources(FHIR). bigdataanalysis,telemedicine,integratedcare,etc.[2].
ISO/IEEE 11073 SDC focuses on cross-manufacturer FHIRserversareonepossibleimplementationapproach
toestablishaclinicalrepositoryarchitecturewithunder-
| device-to-device | communication |     | in  | high-acuity |     | environ- |     |     |     |     |     |     |     |
| ---------------- | ------------- | --- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ments and provides interoperability of point-of-care lying storage and retrieval capabilities that enable the
|         |                 |     |          |     |             |     | processing | of  | larger amounts |     | of heterogenuous |     | clinical |
| ------- | --------------- | --- | -------- | --- | ----------- | --- | ---------- | --- | -------------- | --- | ---------------- | --- | -------- |
| medical | devices (PoCD). | The | ISO/IEEE |     | 11073-10207 |     |            |     |                |     |                  |     |          |
DomainInformationandServiceModeldefinesthenet- datathancurrenthospitalinformationsystems.Through
work representation of generic medical devices and storing more contextual information and metadata as
wellastheabilitytoefficientlystorelargesetsofvalues
consistsofthedevicedescriptionanddynamicinforma-
tionaboutthecurrentdevicestate. onFHIRserversforclinicalrepositories,theuseofHL7
|         |               |          |     |          |     |         | FHIR has | the | potential | to  | increase | interoperability |     |
| ------- | ------------- | -------- | --- | -------- | --- | ------- | -------- | --- | --------- | --- | -------- | ---------------- | --- |
| The HL7 | FHIR standard | supports | the | exchange |     | of data |          |     |           |     |          |                  |     |
between software systems in the healthcare sector. It betweendifferentclinicaldomains[3].
combinestheadvantagesoftheestablishedHL7stand- In this work, we presentan IG that containsa mapping
|     |     |     |     |     |     |     | of medical | device | data | from | ISO/IEEE | 11073-10207 | to  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---- | ---- | -------- | ----------- | --- |
ardproductlinesVersion2,Version3andCDAwiththose
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 2/10

Riechetal.:MappingofmedicaldevicedatafromISO/IEEE11073-10207...
HL7FHIRinordertoimprovevendor-independentinter- care with ca. 150 specifications. Therefore, resources
operability. can not only be used for the communication of clinical
A similar approach is described in an article by Trigo et data but also cover business processes, vocabularies,
al.[4],whichdealswithharmonisingtheuseofopenEHR IGs, and more [5]. The expression of the specifications
andISO/IEEE11073.Hospitalsandhealthcareproviders in resources simplifies machine processability enor-
using openEHR, just like those using HL7 FHIR, need mously. Each resource contains structured data that
properintegrationofdatafromexternalsources,suchas coverstheusualusecases,ahuman-readablesummary
ISO/IEEE 11073. Therefore, the classes and attributes ofthecontent,andso-calledextensionstosupportfurther
ofarepresentativenumberofISO/IEEE11073special- individualusescenarios,whicharenotalreadycontained
isationsformedicaldevices–weight,temperature,blood intheusualusecases.Resourcescanuselinkstorefer
pressure,pulseandheartrate,oximetryandelectrocar- to other resources. These references create a network
diograph – were analysed and mapped to openEHR ar- thatcan,forexample,describeanentirepatientrecord.
chetypestogetherwiththeISO/IEEE11073-20601core The parallel development processes of the data model
documentonPersonalHealthDevice(PHD)communica- ISO/IEEE 11073-10207 and HL7 FHIR have influenced
tion[4].Theirproposedmethodologyreusestheexisting eachother.Therefore,HL7FHIRalreadyofferspractical
archetypeswherepossibleandproposesnewones–or buildingblocksforthemodellingofISO/IEEE11073SDC
appropriatemodifications–elsewhere. devices and the representation of their attributes and
measurementsthroughtheuseofresources[9].
Material
|        |       |       |      |            |     |     | ISO/IEEE | 11073 |     |     |     |     |
| ------ | ----- | ----- | ---- | ---------- | --- | --- | -------- | ----- | --- | --- | --- | --- |
| Health | Level | Seven | Fast | Healthcare |     |     |          |       |     |     |     |     |
TheISO/IEEE11073Healthinformatics–PointofCare
medicaldevicecommunicationseriesconsistsofcommu-
| Interoperability |     | Resources |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nicationstandardsthatenablecommunicationbetween
medicaldevices,healthcaredevices,andexternalcom-
FHIRisthemostrecentdevelopmentofHL7:astandard
|              |     |               |     |            |           |     | puter systems. | They | provide | automatic | and detailed |     |
| ------------ | --- | ------------- | --- | ---------- | --------- | --- | -------------- | ---- | ------- | --------- | ------------ | --- |
| that focuses | on  | implementable |     | artifacts, | so-called | Re- |                |      |         |           |              |     |
electronicdatacollectionofinformationaboutthepatient,
| sources, | for exchanginghealthcare-related |     |     |     | data. | It con- |     |     |     |     |     |     |
| -------- | -------------------------------- | --- | --- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- |
vitaldata,andoperatingdataofthedevices[1].Themain
tainsneitheraninformationmodelnorareferencearchi-
tecture [5] but defines a uniform interface that aims to componentsarethefollowingthreesub-standards:
acceleratetheuptakethroughsimplicity[6].Thedefini- 1. ISO/IEEE11073-10101–Nomenclature
| tions used | herein | are | based | on HL7 | FHIR version | R4  |               |     |          |              |       |         |
| ---------- | ------ | --- | ----- | ------ | ------------ | --- | ------------- | --- | -------- | ------------ | ----- | ------- |
|            |        |     |       |        |              |     | This standard |     | contains | nomenclature | codes | for the |
4.0.0.HL7FHIRisfocusedonaRESTfulapproachusing unique identificationand descriptionof objectsand
asimpleandestablishedmechanismfordataaccessin attributes as well as parameters and measurement
distributedsystems.
data.Thenomenclatureisdividedintodifferentparti-
RepresentationalStateTransfer(REST)isanabstraction tionstodefinethecontentandfunctionofthecode.
| of the structure                                |     | and behaviour |     | of the | World Wide | Web |                                               |     |     |     |     |     |
| ----------------------------------------------- | --- | ------------- | --- | ------ | ---------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
|                                                 |     |               |     |        |            |     | 2. ISO/IEEE11073-10201–DomainInformationModel |     |     |     |     |     |
| [7].Theresourceparadigmandthestatelessnessofthe |     |               |     |        |            |     | (DIM)                                         |     |     |     |     |     |
HypertextTransferProtocol(HTTP)enableahighscalabil- TheISO/IEEE11073-10201DIMreflectstherelation-
| ity [8]. | The implementation |     | of  | REST follows | four | basic |     |     |     |     |     |     |
| -------- | ------------------ | --- | --- | ------------ | ---- | ----- | --- | --- | --- | --- | --- | --- |
shipsofelementsinanobject-orientedhierarchyand
designprinciples: provides the data structure: The medical device is
1. UsingHTTPmethodsandcaching, representedbyaMedicalDeviceSystem(MDS)object
thatcomprisesoneormoreVirtualMedicalDevices
2. statelessness,
(VMD).AVMDmaycontainChannelsthatarelogical
3. uncoverdirectory-structuretoresourceslikeURI,and
|     |     |     |     |     |     |     | groupings | of  | Metrics, | possibly multiple | instances | of  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | ----------------- | --------- | --- |
4. transmissionofdataformatsXML,JSONandRDFas
aparticulartypeofmeasurement.Themetricobject
resourcerepresentations.
|     |     |     |     |     |     |     | is the basic |     | element | of actual data | transmission, |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | -------------- | ------------- | --- |
HL7FHIRdoesnotmakeanyassumptionabouttheexist-
|     |     |     |     |     |     |     | which | generally | represents | a particular |     | type of |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ---------- | ------------ | --- | ------- |
ingsystemimplementationandallowsfasterintegration measurementorobservationandisassociatedwith
anddevelopmentcycles[6],[8].TheHL7FHIRstandard
|     |     |     |     |     |     |     | a particular | code | from | the ISO/IEEE | 11073-10101 |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ---- | ------------ | ----------- | --- |
also includes implementation examples, and reference Nomenclatureaswellasunitofmeasure.Eachlevel
implementationsformultipleplatforms,includinglivetest
|         |      |               |     |               |     |       | of the so-called |     | Containment | Tree | of the model | are |
| ------- | ---- | ------------- | --- | ------------- | --- | ----- | ---------------- | --- | ----------- | ---- | ------------ | --- |
| servers | over | the Internet. | HL7 | FHIR consists | of  | three |                  |     |             |      |              |     |
annotatedwithnomenclaturetermstofacilitatema-
buildingblocks:Resources,references,andprofiles. chineinterpretability.
Resourcesarecompact,logicallydelimitedunitsofdata
|     |     |     |     |     |     |     | 3. ISO/IEEE11073-20101–BaseStandard |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
exchange with a well-defined behaviour and unique se- TheBaseStandarddefinesthestructureandtransfer
| mantics. | They | represent | the basic | information | unit | in  | a          |     |             |               |     |      |
| -------- | ---- | --------- | --------- | ----------- | ---- | --- | ---------- | --- | ----------- | ------------- | --- | ---- |
|          |      |           |           |             |      |     | of objects | and | attributes. | A distinction | is  | made |
RESTfulenvironment.Resourcesarethesmallestunitof
betweentheCommunicationModelandtheInforma-
transmission,representingtheentirespectrumofhealth tionModel.Thecommunicationmodeldescribeslay-
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 3/10

Riechetal.:MappingofmedicaldevicedatafromISO/IEEE11073-10207...
ers5to7oftheOSIlayermodelandtheinformation Relationships to other implementation
modeldefinesthemodelling,formattingandtransmis-
guides
sioncodingoftherespectiveobjects[10].
The IG for ISO/IEEE 11073 SDC developed within the
ISO/IEEE 11073 SDC
scopeofthispaperisalignedwithworkinotherguideline
documents,includingthe HL7 FHIR IG for PHD and the
Since the transport mechanisms of the original series,
generalIGforPoCD,i.e.patient-orienteddiagnosticsand
which focused on point-to-point communication for
therapy.
medicaldevicesclosetopatients,cannotbeimplemented
formultipoint-to-multipointcommunication,theISO/IEEE
PersonalHealthDeviceDataImplementation
11073 SDC standard series was developed. This is a
Guide
communicationprotocolformedicaldevicesusedinhigh-
acuityenvironments.Theinitialsetofthreecorestand-
ThisIGdescribeshowinformationfromPersonalConnect-
ards was developed in the OR.NET research project
ed Health Alliance (PCHA)-certified PHD is represented
fundedbytheGermanFederalMinistryofEducationand
inHL7FHIR.PHDsaredevicesmainlyusedinhomecare
Research (BMBF) [1]. The fundamental idea for this
andincludePCHA-certifieddevicessuchasbloodglucose
communicationisbasedontheService-OrientedArchitec-
meters,bloodpressurecuffs,scales,thermometers,etc.
ture (SOA) paradigm, which was extended to a Service-
In this context, the data from a PHD includes both the
Oriented Medical Device Architecture (SOMDA) during
measurements performed by the PHD and information
theOR.NETproject.
aboutthePHDitself.PHDdataincludesfeatures,operat-
ISO/IEEE11073SDCaddressescross-vendordevice-to-
ingstatus,andfunctionsoftheinstrument,suchasserial
device communicationand aims for the interoperability
number, manufacturer name, and firmware version.
of PoCD. ISO/IEEE 11073 SDC thus describes the first
Typically,thePHDislocatedathomewiththepatientor
technicalspecificationforafullydistributedarchitecture
onthepersonthemselves.
that implements the SOMDA. Therein, ISO/IEEE 11073
The purpose of this IG is to define the mapping of PHD
SDCdoesnotcompetewithothermedicalcommunication
data to HL7 FHIR resources. For the consumers of the
standardssuchasHL7orDICOM,butcomplementsthem
HL7FHIRresources,thisIGspecifiestheHL7FHIRcom-
forpreviouslyunsolvedusecases.
ponentsthatcontainthenecessaryPHDinformation.
The ISO/IEEE 11073 SDC standard family consists of
threecomponents.Firstly,itcontainsthetransporttech-
GeneralImplementationGuideforPoint-of-Care
nologystandardISO/IEEE11073-20702MedicalDevices
Devices
CommunicationProfileforWebServices,whichensures
the foundational interoperability of medical devices
This guide defines the use of HL7 FHIR resources to
throughsafedataexchange.Secondly,thefamilyincludes
transmitmeasurementsandsupportingdatafromPoCD
theISO/IEEE1173-10207StandardforDomainInforma-
foracutecaretoreceivingsystemsforelectronicpatient
tionandServiceModelforService-OrientedPoCDCom-
records, to support clinical decisions, and to archive
munication.Thisdescribesthestructureofthedatabeing
medicaldatae.g.formeasuringthequalityofcareorre-
exchangedandisdividedintothedevicedescriptionand
searchpurposes.Theguidefocusesonacutecaredevices
the current device state of the medical device. This
forprofessionaluse,mainlyinhealthcarefacilities.The
standardthusaddressesstructuralinteroperability.Lastly,
main objectives include the addition of full data prove-
it contains the ISO/IEEE 11073-20701 Standard for
nanceinformationfortraceabilityaswellasfurtherdetails
Service-Oriented Medical Device Exchange Architecture
ondevicearchitectureandattributes,suchascalibration
andProtocolBinding.Thisspecifiestheservice-oriented
historyandbatterycondition.Thesearenotincludedin
medical device architecture by i.a. binding the domain
acommonHL7FHIRObservationresource.
informationandservicemodeltothewebserviceimple-
TheguidelinesforPoCDandISO/IEEE11073SDCboth
mentations.ThemandatoryuseoftheISO/IEEE11073
use information models and nomenclatures from the
Nomenclature on all levels of the containment tree en-
ISO/IEEE11073MedicalDeviceCommunicationStand-
ablessemanticinteroperability[1],[11].
ardSeries.TheIGsforalltypesofdevicesarebeingde-
IntheISO/IEEE11073-10207:2019standard,thedevice
velopedincollaborationwiththeDevices-On-FHIR(DoF)
information is organised hierarchically into four levels.
[13] project with the goal of consistency and usability
Theuppermostlevelistheobject-orientedabstractionof
whentheresourcesareconsumedbyreceivingsystems.
aPoCD,theMDS,followedbytheVMDonthenextlevel,
whichrepresentstheabstractionofamedicalsubsystem.
They represent structural levels of complex PoCD and
cannotbefoundinPHD.TheChannelallowsforthelogi-
calgroupingofMetricsforhierarchicalinformationorga-
nisation.AMetricisanabstractionofaPoCDcomponent
that generates or stores biosignal measurements, set-
tings,orstatusvalues([12],p.57–68).
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 4/10

Riechetal.:MappingofmedicaldevicedatafromISO/IEEE11073-10207...
Methods A profile contains restrictions for an HL7 FHIR base re-
|     |     |     |     |     |     |     | source | or another | HL7 | FHIR | profile. | The | term profiling |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | ---- | -------- | --- | -------------- | --- |
referstotheapplicationofrestrictionstoresources.The
Data mapping
|              |      |               |     |        |             |      | process            | of creating |       | a profile | is a     | process     | of restricting |        |
| ------------ | ---- | ------------- | --- | ------ | ----------- | ---- | ------------------ | ----------- | ----- | --------- | -------- | ----------- | -------------- | ------ |
|              |      |               |     |        |             |      | different          | aspects     | of    | a basic   | resource | or          | data type,     | so-    |
| Data mapping |      | is defined    |     | as the | alignment   | of   | data               |             |       |           |          |             |                |        |
|              |      |               |     |        |             |      | called constraint. |             | These | may       | include  | limitations |                | on al- |
| elements     | from | two different |     | data   | structures. | This | is a               |             |       |           |          |             |                |        |
lowedvaluesets,limitingoreliminatingcardinality,and
methodforanalysing,organising,andpresentinginforma-
|           |              |     |          |     |               |     | adding | elements | (extensions). |     | The | first step | in creating |     |
| --------- | ------------ | --- | -------- | --- | ------------- | --- | ------ | -------- | ------------- | --- | --- | ---------- | ----------- | --- |
| tion. The | presentation |     | is based | on  | the interests |     | of the |          |               |     |     |            |             |     |
target group and the purpose of the information. The aprofileinvolvesselectingabaseresourceordatatype
(e.g.apatient).Thenextstepistonametheprofileand
methodismainlyusedinthedesignanddevelopmentof
|     |     |     |     |     |     |     | provide | a unique | canonical |     | Uniform | Resource |     | Locator |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --------- | --- | ------- | -------- | --- | ------- |
technicalcommunication[14].
(URL).Aftercreatingaprofile,itispossibletostartrestrict-
| Data mapping |     | is used | to  | transform | or mediate |     | data |     |     |     |     |     |     |     |
| ------------ | --- | ------- | --- | --------- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
ingtheelements.Forinstance,fixedvaluescanbeused
betweenadatasourceandadestination.Thisrequires
theidentificationofdatarelationships.Essentially,adata tospecifyavaluethatshouldbesetexactlyasthevalue
forthiselement.Anexampleofhowtospecifyavalueis
mappingonattribute-to-attributebasisanalyseshowdata
tocreateaprofilespecificallyfortheweightofanewborn.
| can be | transferred |     | from one | system | to  | another. | This |     |     |     |     |     |     |     |
| ------ | ----------- | --- | -------- | ------ | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Thisisdonebycreatinganobservationprofilethatisas-
analysisensuresthateachpieceofinformationismapped
signedafixedvalueforObservation.codeusingaLogical
tothemostappropriatelocationinthetargetdatastruc-
ture.Toachievethisgoal,adatamappingcontainsalist ObservationIdentifiersNamesandCodes(LOINC)code,
asystem,andadisplaynametospecifywhatinformation
withtheattributesoftheoriginaldatasourceandacor-
|     |     |     |     |     |     |     | is specified. | The | various | constraints |     | make | profiled | re- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ----------- | --- | ---- | -------- | --- |
respondinglistwithattributesofthetargetdatamodel.
|     |     |     |     |     |     |     | sources | more | suitable | for | the specific | needs, | but | also |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | -------- | --- | ------------ | ------ | --- | ---- |
Themappingalsoincludestranslationrulesthatdefine
raisethebarintermsofwhatcriterianeedtobefulfilled
| any transformation |     | that | may | have | to take | place | when |     |     |     |     |     |     |     |
| ------------------ | --- | ---- | --- | ---- | ------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
informationisexchangedbetweenthetwoformats,such inorderforaresourcetomeetthespecifiedrequirements
|     |     |     |     |     |     |     | [16]. To | create | a guide | that | meets | the | needs | of the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | ---- | ----- | --- | ----- | ------ |
asmappingvaluesets,settingdefaultvalues,orcombin-
|     |     |     |     |     |     |     | ISO/IEEE | 11073 | SDC | standard, |     | changes | (restrictions) |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --- | --------- | --- | ------- | -------------- | --- |
ingfields.
hadtobemadetoseveralexistingresources.Ifelements
Creatingadatamappingrequiresidentifyingandresolving
arenotsupportedbythebaseresourceyet,theycanbe
| potential | problems | on  | a conceptual |     | level | before imple- |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | ------------ | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
menting it. In data migration and integration tasks, a addedbyusingextensions.FirsttheHL7FHIRdocumen-
tation[17]mustbecheckedwhethersuchanextension
varietyofdifferencesinthewaydataisstoredcancause
alreadyexists.Ifnoextensioncanbefound,anewexten-
datatobelostormisrepresented[15].
|     |     |     |     |     |     |     | sioncanbe | created. |     | In the | properties, | context | informa- |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ------ | ----------- | ------- | -------- | --- |
ThefirsttaskistoidentifyHL7FHIRresourcesequivalent
tion,acanonicalURL,thenameandotherrelevantinfor-
| to concepts | from | ISO/IEEE |     | 11073-10207. |     | For example, |     |     |     |     |     |     |     |     |
| ----------- | ---- | -------- | --- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
theMdsDescriptorrepresentsthesameconceptasthe mationcanbespecified.Thecontextinformationcontains
|          |        |           |     |             |            |     | a type that | specifies |     | whether | the | extension | extends | a   |
| -------- | ------ | --------- | --- | ----------- | ---------- | --- | ----------- | --------- | --- | ------- | --- | --------- | ------- | --- |
| HL7 FHIR | Device | resource. |     | Afterwards, | equivalent |     | data        |           |     |         |     |           |         |     |
resource,adatatype,amapping,oranotherextension.
| items that   | meet          | the                                 | requirements |                        | must be | connected. |          |              |          |       |           |      |             |         |
| ------------ | ------------- | ----------------------------------- | ------------ | ---------------------- | ------- | ---------- | -------- | ------------ | -------- | ----- | --------- | ---- | ----------- | ------- |
|              |               |                                     |              |                        |         |            | Then the | specific     | resource |       | or data   | type | that should | be      |
| For example, |               | the MdsDescriptor/MetaData/Manufac- |              |                        |         |            |          |              |          |       |           |      |             |         |
|              |               |                                     |              |                        |         |            | extended | is selected. |          | A new | extension |      | begins      | with an |
| tureDate     | correspondsto |                                     | the          | Device.manufatureDate. |         |            | If       |              |          |       |           |      |             |         |
thereisnomatchingelement,anewelementhastobe elementthatcontainsavaluethatcanbespecifiedfrom
allavailabledatatypes.Figure1showsanexampleofa
extended.Thisincludeslimitingthecardinalityofexisting
profiledandextendedresource.
| elements, | making | them | mandatory, |     | or removing |     | them |     |     |     |     |     |     |     |
| --------- | ------ | ---- | ---------- | --- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
entirely.Forexample,theinformationabouttheapproved
| jurisdictions | of  | a device | is present |     | in ISO/IEEE | 11073- | Results |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ---------- | --- | ----------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
10207,butitisnotmodeledinHL7FHIR.Inopposite,if
thereisanequivalentelement,datatypesarechecked
Thiswork,inextensionofbothISO/IEEE11073SDCand
andadjustedifnecessary.Ifthereisnolossofdata,then
HL7FHIR,enablesthedataexchangebetweenmedical
theconceptisaccuratelymapped.Theresultsarethen
devicesandclinicalinformationsystems.Thepurposeof
reviewedsystematicallybyexpertswhoparticipateinthe
|     |     |     |     |     |     |     | this IG | and the | relationships |     | to other | IGs | have | already |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------- | --- | -------- | --- | ---- | ------- |
standardisationofISO/IEEE11073SDCandHL7FHIR.
beencomprehensivelypresentedintheIntroductionand
|     |     |     |     |     |     |     | Material | & Methods |     | of this | paper. | This | IG [18], | which |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ------- | ------ | ---- | -------- | ----- |
Profiling
containsthemapping,newprofiles,valuesets,andcode
systems,isintendedformedicaldevicemanufacturers,
| Profiles | define | how | individual | systems | may | use | and    |              |     |          |             |     |           |     |
| -------- | ------ | --- | ---------- | ------- | --- | --- | ------ | ------------ | --- | -------- | ----------- | --- | --------- | --- |
|          |        |     |            |         |     |     | system | integrators, |     | HL7 FHIR | architects, |     | patients, | and |
combineHL7FHIRresources.Theydetailwhichresources
clinicalusersofpatient-relateddeviceinformation.
andextensionsasystemcancommunicate.Theprofiles
canbespecifiedandpublishedbyHL7,byregionaluser
groupsadoptingnationallaws,orevenlocallytosupport
individualusecases[5].
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 5/10

Riechetal.:MappingofmedicaldevicedatafromISO/IEEE11073-10207...
Figure1:ExampleoftheprofiledDeviceresourceSDCDeviceMDS.ThedifferenceviewfortheMDSprofileshowsindetailthe
fiveextensionsandthatthesafetyattributehasbeenmodified.Aterminologybindingwasaddedtothecodeofthesafety
elementandareferencewasspecifiedunderthesystemunderwhichthevaluesetcanbefound.Ashortdescription,adefinition,
thedatatype,andthelinkunderwhichtheextensioncanbefoundaregivenforeachextension.
Figure2:ThegraphsummarisestheinteractionoftheHL7FHIRresources.Therespectiveresourcesareshownasentities.
Theseareconnectedbyarrows,whichrepresentthereferences.Thesolidarrowsrepresentreferencesthatarecontainedin
themappingofthisIG.ThedottedarrowsshowreferencesthatarehelpfulforunderstandingtheinteractionofHL7FHIR
resources.Inthefigure,nodistinctionismadebetweenthedifferently-profileddeviceresources.
Data mapping Defining HL7 FHIR profiles
Aligningthetwodatastructureswasnecessarytoachieve Withthehelpofprofilingmechanisms,HL7FHIRprofiles
interoperabilitybetweenbothcommunicationstandards. weredefinedthatenabletherepresentationofISO/IEEE
Therefore, ten different base resources were selected 11073SDCdevicesforcommunicationwhileminimising
and two of them were profiled (five profiles) (Figure 2). the loss of information. The containment tree of the
Wherever possible,a mappingfor the elementsandat- ISO/IEEE11073-10207DIMismodelledusingthebase
tributesoftheISO/IEEE11073-10207DIMwasdefined resources Device and DeviceMetric (Figure 3). The
(213 mappings), and 33 extensions were added where SDCDeviceMetric represents a single parameter of a
therewasnosuitablecorrespondingelementavailable. PoCD,e.g.ameasurementorasetting.DeviceMetric,the
Theresultshavebeenreviewedsystematicallybyexperts basicresourceofSDCDeviceMetric,isalreadydesigned
whoparticipateinthestandardisationofISO/IEEE11073 todescribeclassicISO/IEEE11073-10201DIMmetrics.
SDCandHL7FHIR. It was therefore only necessary to build an extension
adding support for the ISO/IEEE 11073-10207 DIM
MetricDescriptor.Thisincludes,forexample,therelation.
Arelationenablesthemodelingofrelationshipsbetween
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 6/10

Riechetal.:MappingofmedicaldevicedatafromISO/IEEE11073-10207...
ametricandothercontainmenttreeelements,represent- The SDCDeviceMDS contains information about the
inge.g.theeffectthatasettinghasonotherparameters. medicaldeviceasawhole,suchasmanufacturer,model
InSDCthecurrentvalueofaMetriccanbeobtainedfrom number,andotheridentifyingfeatures.Informationabout
the instances of MetricState. Representing an actual the ApprovedJurisdictions,operationalinformation,and
(clinical) data element, the profile SDCObservation, de- areferencetotheoperatorofthedevicewereaddedto
rived from the observation resource, is the equivalent theresourceasextensions(Figure1).
HL7FHIRstructure.Allofthemetadatacontainedherein Furthermore, the device description includes a safety
generallyreferstotheactualvalueitself,suchastiming, classificationofthedatacontainedinthisdescriptor.The
subject, body site, performer, etc., as opposed to the safety classification allows manufacturers of medical
device’scapabilitytoobtainthevalue,whichisdescribed devicestolimittheirresponsibilityfortheobjectsprovided
intheDeviceMetric.Thevalidityofasinglemeasurement [12]. ISO/IEEE 11073-10207 provides a value set for
isanexampleofametadataelementthathadtobead- this,butHL7FHIRdoesnot.Inordertomakethevalue
dedtotheprofile. setavailableforthemapping,acodesystemwascreated
The MdsDescriptor, VmdDescriptor, and withtheexistingcodesandthenlinkedtoanewbinding
ChannelDescriptorcontainmenttreelevelsaremapped valueset(Figure1).
to profiled Device resources (Figure 3). An ThePatientContext,LocationContext,andOperatorContext
SDCDeviceChannelasagroupingofmetricsdealingwith elementsweremappedtotheresourcesPatient,Location,
semantically related information, e.g. a blood pressure Organisation,andPractitioner.Thesearenotvisualised
channelwithinapatientmonitorVMDtogrouptogether in Figure 3 because the resources did not need to be
| allmetricsthatdealwithbloodpressure,canbeindepend- |                    |           |         |          |           | profiled. |     |     |     |     |     |     |
| -------------------------------------------------- | ------------------ | --------- | ------- | -------- | --------- | --------- | --- | --- | --- | --- | --- | --- |
| ent of the                                         | physical structure | of the    | device. | Elements | at        |           |     |     |     |     |     |     |
| this level                                         | include a parent   | reference | and     | a set    | of attri- |           |     |     |     |     |     |     |
Discussion
| butes shared      | with the component |     | descriptors   |     | at higher |     |     |     |     |     |     |     |
| ----------------- | ------------------ | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
| levels, including | for example        |     | OperatingMode |     | and       |     |     |     |     |     |     |     |
ApprovedJurisdictions. The OperatingCycles and This section discusses structural difficulties as well as
OperatingHours can be defined for the Channel itself, resource-specificproblemsthathaveoccurredduringthe
creationoftheIG.
| thus they | were added as | extensions | to  | the profile. | An  |     |     |     |     |     |     |     |
| --------- | ------------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
SDCDeviceVMD is a subsystem of an SDCDeviceMDS, ISO/IEEE 11073-10207 and HL7 FHIR have significant
|     |     |     |     |     |     | overlap | in content, | but | differ | in structure. |     | Most promi- |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ------ | ------------- | --- | ----------- |
suchasthegasdeliveryandventilationfunctionsofan
anaesthesiamachine,orasoftwarecomponentthatin- nently,informationaboutamedicaldeviceintheISO/IEEE
tegrates multiple measurements from other VMDs into 11073-10207standardisdividedintothedevicedescrip-
tionandthedevicestate.HL7FHIR,ontheotherhand,
| a risk assessment | for clinical | decision |     | support. | As with |     |     |     |     |     |     |     |
| ----------------- | ------------ | -------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
the SDCDeviceChannel, the OperatingCycles and doesnotdifferentiatebetweendescriptionandstatebut
|                |           |           |     |         |        | collates | this data | in units | with | a unique | semantic, | the |
| -------------- | --------- | --------- | --- | ------- | ------ | -------- | --------- | -------- | ---- | -------- | --------- | --- |
| OperatingHours | have been | extended, |     | as well | as the |          |           |          |      |          |           |     |
ApprovedJurisdictions. resources.Itisthusnotpossible,nornecessary,tomap
identifierssuchastheHandleoccurringineveryelement
ofthedomaininformationandservicemodel.Thisunique
identifierisusedi.a.forreferencefromthedevicestate
tothedescriptor.
Anotherstructuraldifferencecanbeseenintheopposing
directionalityofreferencesinthetwostandards.Torecord
theinformationaboutalocationinHL7FHIR,references
mustbeusedinascendingorderstartingwiththelowest
|     |     |     |     |     |     | hierarchical | instance.      |     | In ISO/IEEE |      | 11073-10207 | this  |
| --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | ----------- | ---- | ----------- | ----- |
|     |     |     |     |     |     | data is not  | hierarchically |     | ordered.    | This | difference  | leads |
todifficultiesinpresentingthemappingandmadeitne-
cessarytoaddexplanatorynotesonimplementingloca-
|     |     |     |     |     |     | tionreferencesin |     | the | IG. Besides,for |     | a locationin | HL7 |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --------------- | --- | ------------ | --- |
FHIR,itisnotalwaysclearlydefinedwhetherthelocation
ispartofanotherlocationorpartofamanagingorganisa-
tion.
Therepresentationofthehierarchyofthedeviceinforma-
tionaspartofthemappingisnoteasilypossibleasthe
|     |     |     |     |     |     | references | of HL7 | FHIR | and | ISO/IEEE | 11073 | SDC are |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | ---- | --- | -------- | ----- | ------- |
inverted.InHL7FHIR,thephysicalorlogicalcomposition
ofadeviceisrepresentedbythedevicepointingupwards
|     |     |     |     |     |     | using the | Device.parent |     | element. |     | In ISO/IEEE | 11073 |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | -------- | --- | ----------- | ----- |
Figure3:Asubsetofprofiledresources(baseresourcesin
parentheses),andreferencesincludingcardinality SDC,however,acontainmenttreeelementhasalistof
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 7/10

Riechetal.:MappingofmedicaldevicedatafromISO/IEEE11073-10207...
child nodes but carries no reference to its parent tivationstateoftheMdsStatearemappedtothecodes
(Figure4). ofthevaluesetstatusReasonforthedeviceavailability.
|     |     |     |     |     |     |     | Three values | from | ISO/IEEE |     | 11073-10207 |     | are mapped |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | -------- | --- | ----------- | --- | ---------- | --- |
to“not-ready”,wherebythemoreprecisesemanticsare
lost.Aftertransformation,itisthereforenolongerpossible
totracewhichstatethedeviceoriginallyreported.
Atotalofapproximately25conflictsoccurred.Thesein-
clude,forexample,thelossofsemanticswhenmapping
thevaluesetsinseveralcases.However,thisisnotcon-
|     |     |     |     |     |     |     | sidered              | critical, | since             | in all cases | the           | granularity  |          | of the |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --------- | ----------------- | ------------ | ------------- | ------------ | -------- | ------ |
|     |     |     |     |     |     |     | value sets           | in        | ISO/IEEE          | 11073-10207  |               | is higher    | than     | in     |
|     |     |     |     |     |     |     | HL7 FHIR             | (e.g.     | the distinctionof |              | metric        | categories)  |          | and    |
|     |     |     |     |     |     |     | this information     |           | is not            | considered   |               | to be highly | relevant |        |
|     |     |     |     |     |     |     | for our applications |           | of                | HL7 FHIR.    | Nevertheless, |              | this     | re-    |
strictsthebidirectionalityofourmapping.Infourcases,
eithernosolutioncouldbefoundoritwasnotnecessary
Figure4:Invertedrelationdirectionality to do so. One of the cases where it is not necessary to
buildanextension,isthatISO/IEEE11073-10207differ-
| Apart from | the structural |     | differences, |     | there | were also |     |     |     |     |     |     |     |     |
| ---------- | -------------- | --- | ------------ | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
entiatesbetweenaneonateandapatient.HL7FHIRdoes
| problems | concerning | specific |     | ISO/IEEE | 11073 | or HL7 |                   |     |         |           |     |         |      |       |
| -------- | ---------- | -------- | --- | -------- | ----- | ------ | ----------------- | --- | ------- | --------- | --- | ------- | ---- | ----- |
|          |            |          |     |          |       |        | not differentiate |     | between | patients. |     | Another | case | where |
FHIRcontents.Theseincludedatathateithercouldnot
noextensionwascreatedistheconflictwiththesexand
bemappedorcouldonlybemappedwithlossofinforma-
genderofapatient,asdescribedabove.Theinformation
tion.
|                 |     |         |     |             |     |            | of a battery, | e.g. | the capacity |     | or voltage | of  | a battery, | is  |
| --------------- | --- | ------- | --- | ----------- | --- | ---------- | ------------- | ---- | ------------ | --- | ---------- | --- | ---------- | --- |
| The AlertSystem |     | has not | yet | been mapped |     | as it only |               |      |              |     |            |     |            |     |
notrepresentedinourmapping,becauseuptonowthis
relatestoalertcommunicationmanagement,whichhas
informationdoesnotneedtobetransferredtoahospital
lowrelevancetoclinicalITsystemforpurposesotherthan
informationsystemforourapplication.Thefactthatthis
| logging | and was thus | out | of the | scope | of this | work [3]. |     |     |     |     |     |     |     |     |
| ------- | ------------ | --- | ------ | ----- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
dataalsodoesnotappearinthemappingsoftherelated
Thereare,however,currenteffortstodefineaDeviceAlert
IGscontributedtothisdecision.Foralarms,forexample,
resourceforHL7FHIRaswellasworkonacorresponding
|             |           |               |     |       |     |           | a solution | is under | investigation. |     | In  | all other | cases, | a   |
| ----------- | --------- | ------------- | --- | ----- | --- | --------- | ---------- | -------- | -------------- | --- | --- | --------- | ------ | --- |
| IHE profile | for alert | dissemination |     | using | HL7 | FHIR that |            |          |                |     |     |           |        |     |
solutioncouldbeworkedout.
| could be                   | used e.g.   | to distribute |     | alerts | to the       | pagers of |            |     |     |        |     |      |     |     |
| -------------------------- | ----------- | ------------- | --- | ------ | ------------ | --------- | ---------- | --- | --- | ------ | --- | ---- | --- | --- |
| clinical                   | staff. Upon | maturity      | of  | these  | definitions, | the IG    |            |     |     |        |     |      |     |     |
| willbeextendedaccordingly. |             |               |     |        |              |           | Conclusion |     | and | future |     | work |     |     |
Furthermore,thesexandgenderofapatient(oranew-
| born) cannot | be mapped |     | from | ISO/IEEE | 11073-10207 |     |     |     |     |     |     |     |     |     |
| ------------ | --------- | --- | ---- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Inthiswork,anIGforthemappingofmedicaldevicedata
toHL7FHIR.Thedomaininformationandservicemodel
fromISO/IEEE11073-10207toHL7FHIRhasbeencre-
onlycontainsanattributeforsexasdefinedbybiological ated.Thismappinghelpstobridgethestructuralinterop-
andphysiologicalcharacteristics.HL7FHIR,ontheother
erabilitygapbetweentwocommunicationarchitectures
hand,onlyprovidesafieldforgenderasdefinedbythe
|     |     |     |     |     |     |     | for medical | devices | and | clinical | information |     | systems. |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | -------- | ----------- | --- | -------- | --- |
sociallyconstructedroles,behaviours,activities,andat-
Thereby,wecreatethebasisforsemanticinteroperability
| tributes | that a given | society | considers |     | appropriate. | The |          |             |     |         |                |     |     |         |
| -------- | ------------ | ------- | --------- | --- | ------------ | --- | -------- | ----------- | --- | ------- | -------------- | --- | --- | ------- |
|          |              |         |           |     |              |     | that can | be achieved |     | through | the consistent |     | use | of ter- |
biological sex, however, does not necessarily match a minologies. By retaining contextual information and
person’sadministrativegender.Mappingfromonetothe
metadataandtheabilitytoefficientlystorelargesetsof
| otherwouldthereforeintroduceerrors.Ifnecessary, |     |     |     |     |     | an  |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
valuesonFHIRserversinaclinicalrepository,theappli-
| implementer | can | convey | the biological |     | sex as | a coded |        |         |        |      |           |                  |     |     |
| ----------- | --- | ------ | -------------- | --- | ------ | ------- | ------ | ------- | ------ | ---- | --------- | ---------------- | --- | --- |
|             |     |        |                |     |        |         | cation | of this | IG not | only | increases | interoperability |     |     |
observationtype.
betweendifferentclinicaldomains,butalsoenablessafe
In comparison to the IG for PHD, the information about andreliableautomatedinterpretationofthetransformed
theoperatorofamedicaldeviceismodelleddifferently.
|         |                   |     |        |          |     |           | data. It | furthermore | enables   |     | effective | reuse       | of       | device |
| ------- | ----------------- | --- | ------ | -------- | --- | --------- | -------- | ----------- | --------- | --- | --------- | ----------- | -------- | ------ |
| In this | IG, the reference |     | to the | operator | of  | a medical |          |             |           |     |           |             |          |        |
|         |                   |     |        |          |     |           | data for | secondary   | purposes, |     | such      | as clinical | research |        |
deviceonlyallowsforapractitioner,whoisahealthcare
orqualityofcareassessment.
professional.ForPHD,however,apatientcouldalsobe
Atotalof213dataelementsweremapped.Fiveprofiles
theoperator. werecreated,aswellasthreevaluesetswiththecorres-
Anotherproblemariseswhenmappingthevaluesetsof
pondingcodesystems.Incaseswhereconflictsoccurred,
theISO/IEEE11073-10207DIMtothevaluesetsofHL7
asolutioncouldalmostalwaysbefound,ortheconflicts
FHIR.Insomecases,thesevaluesetsdonotmatchex-
werenotconsideredtobecritical.
| actly. If | the HL7 FHIR | value | set | is not | extensible, | it can |     |     |     |     |     |     |     |     |
| --------- | ------------ | ----- | --- | ------ | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Theobjectiveofimprovingtheinteroperabilityofmedical
happen that several codes from the ISO/IEEE 11073- deviceswillcontinuetobepursuedafterthecompletion
10207DIMhavetobemappedtoonecodeinHL7FHIR.
ofthiswork.Ontheonehand,theDoFinitiativepursues
Thisisthecase,forexample,whenthecodesoftheac-
theinterestofbeingabletorepresenttheinformationof
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 8/10

Riechetal.:MappingofmedicaldevicedatafromISO/IEEE11073-10207...
eventsandalertsofPoCDusinganewHL7FHIRresource 5. OemigF,BlobelB,HelmerA,BirkleM.Vergleichverschiedener
[13].Ontheotherhand,workhasbeguntoconsolidate LösungsansätzefürInteroperabilitätinderMedizin.HL7-
Mitteilungen.2018;41:6-17.
thegeneralIGforPoCDandtheIGpresentedinthispa-
per.Forthemostpart,therespectivemappingsremain 6. SaripalleR.FastHealthInteroperabilityResources(FHIR):Current
StatusintheHealthcareSystem.IJEHMC.2019Jan;10(1):76-
unchanged.Theprofiles,however,havetobemergedto
93.DOI:10.4018/IJEHMC.2019010105
theultimategoalofbeingabletorepresentallkindsof
7. FieldingRT.ArchitecturalStylesandtheDesignofNetwork-based
PoCD,irrespectiveofwhethertheyprovideanISO/IEEE
SoftwareArchitectures[Dissertation].2000.
11073SDCinterface,classicISO/IEEE11073,IHEPCD-
01 messages proprietary interconnection, or solely rely 8. BenderD,SartipiK.HL7FHIR:AnAgileandRESTfulapproach
tohealthcareinformationexchange.In:Proceedingsofthe26th
onHL7FHIR.
IEEEInternationalSymposiumonComputer-BasedMedical
Inaddition,furtherdevelopmentoftheISO/IEEE11073 Systems;2013Jun20-22;Porto,Portugal.p.326-31.DOI:
SDC series of standards is taking place. The research 10.1109/CBMS.2013.6627810
projectModularSpecialisationsforPoint-of-CareMedical
9. HeckmannS,SpronkR.FHIRfürEinsteiger:HL7FHIR–Standard
Devices (PoCSpec, 2019-2020) develops particular fürmobileKommunikation.HL7-Mitteilungen.2015;35:6-10.
standardsforspecificdevicetypesfromthedomainsof
10. SchlichtingS,PöhlsenS.AnArchitecturefordistributedsystems
endoscopy and high-frequency surgical equipment. The ofmedicaldevicesinhighacuityenvironments.2014.
goal is to precisely define the scope, structure, and se-
11. AndersenB,KasparickM,UlrichH,FrankeS,SchlamelcherJ,
manticsofthedataandservicesofferedonthenetwork RockstrohM,IngenerfJ.ConnectingtheclinicalITinfrastructure
as well as the behaviour of these specific devices at toaservice-orientedarchitectureofmedicaldevices.Biomed
runtime[19].UsingtheIGdescribedinthiswork,itwill Tech(Berl).2018Feb;63(1):57-68.DOI:10.1515/bmt-2017-
0021
be possible to automatically transform their network
representationstoHL7FHIRandunlockthepotentialof 12. IEEE11073-10207-2017–IEEEHealthinformatics–Point-of-
caremedicaldevicecommunicationPart10207:Domain
theiroperatingdataforsecondaryuse.
InformationandServiceModelforService-OrientedPoint-of-Care
MedicalDeviceCommunication.2018.
Notes 13. HL7International.DevicesonFHIR.[lastedited2018Feb19,
lastaccessed2019Nov20].Availablefrom:
https://wiki.hl7.org/Devices_on_FHIR
Competing interests
14. HornRE.Mappinghyptertext:Analysis,Linkage,andDisplayof
KnowledgefortheNextGenerationofOn-LineTextandGraphics.
The authors declare that they have no competing in- LexingtonInstitute;1989
terests.
15. HaqQSU.DataMappingforDataWarehouseDesign.Morgan
Kaufmann;2015.
Funding
16. Simplifier.net.[lastaccessed2019Nov15].Availablefrom:
https://simplifier.net
Thecorrespondingauthorwassupportedbyascholarship
17. HL7FHIRRelease4.[lastaccessed2019Nov20].Available
oftheFriedrich-Wingert-Stiftung. from:http://hl7.org/fhir/
18. RiechK.IEEE11073-10207IG.[lastaccessed2019Dec20].
References Availablefrom:https://simplifier.net/guide/ieee11073-
10207ig2/home
19. PoCSpec–ModulcarSpecialisationsforPoint-of-CareMedical
1. KasparickM,SchmitzM,AndersenB,RockstrohM,FrankeS,
Devices.[lastaccessed2019Nov22].Availablefrom:
SchlichtingS,GolatowskiF,TimmermannD.OR.NET:aservice-
https://pocspec.de/
orientedarchitectureforsafeanddynamicmedicaldevice
interoperability.BiomedTech(Berl).2018Feb;63(1):11-30.DOI:
10.1515/bmt-2017-0020
2. MacKenzieSL,WyattMC,SchuffR,TenenbaumJD,Anderson
Correspondingauthor:
N.Practicesandperspectivesonbuildingintegrateddata
repositories:resultsfroma2010CTSAsurvey.JAmMedInform KathrinPiaRiech
Assoc.2012Jun;19(e1):e119-24.DOI:10.1136/amiajnl-2011- InstitutfürMedizinischeInformatik,UniversitätzuLübeck,
000508 RatzeburgerAllee160,23562Lübeck,Germany
3. AndersenB,KasparickM,UlrichH,SchlichtingS,GolatowskiF, k.riech@uni-luebeck.de
TimmermannD,IngenerfJ.Point-of-caremedicaldevicesand
systemsinteroperability:AmappingofICEandFHIR.In:
Pleaseciteas
Proceedingsofthe2016IEEEConferenceonStandardsfor
RiechKP,UlrichH,IngenerfJ,AndersenB.Mappingofmedicaldevice
CommunicationsandNetworking(CSCN);2016Oct31-Nov2;
datafromISO/IEEE11073-10207toHL7FHIR.GMSMedInformBiom
Berlin,Germany.p.1-5.DOI:10.1109/CSCN.2016.7785165
Epidemiol.2021;17(2):Doc08.
4. TrigoJD,KohlCD,EguzkizaA,Martínez-EsproncedaM,Alesanco DOI:10.3205/mibe000222,URN:urn:nbn:de:0183-mibe0002225
Á,SerranoL,GarcíaJ,KnaupP.Ontheseamless,harmonized
useofISO/IEEE11073andopenEHR.IEEEJBiomedHealth
Thisarticleisfreelyavailablefrom
Inform.2014May;18(3):872-84.DOI:
https://www.egms.de/en/journals/mibe/2021-17/mibe000222.shtml
10.1109/JBHI.2013.2285441
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 9/10

Riechetal.:MappingofmedicaldevicedatafromISO/IEEE11073-10207...
Published:2021-04-26 Copyright
©2021Riechetal.ThisisanOpenAccessarticledistributedunder
thetermsoftheCreativeCommonsAttribution4.0License.Seelicense
informationathttp://creativecommons.org/licenses/by/4.0/.
GMSMedizinischeInformatik,BiometrieundEpidemiologie2021,Vol.17(2), ISSN1860-9171 10/10