sensors
Article
RADAR-IoT: An Open-Source, Interoperable, and Extensible IoT
Gateway Framework for Health Research
YatharthRanjan1 ,JiangengChang2,HeetSankesara1 ,PaulineConde1 ,ZulqarnainRashid1 ,
RichardJ.B.Dobson1 andAmosFolarin1,*
1 BiostatisticsandHealthInformatics,InstituteofPsychiatry,Psychology&Neuroscience,
King’sCollegeLondon,LondonSE58AF,UK;yatharth.ranjan@kcl.ac.uk(Y.R.);
heet.sankesara@kcl.ac.uk(H.S.);pauline.conde@kcl.ac.uk(P.C.);zulqarnain.rashid@kcl.ac.uk(Z.R.);
richard.j.dobson@kcl.ac.uk(R.J.B.D.)
2 SawSweeHockSchoolofPublicHealth,NationalUniversityofSingapore,Singapore119077,Singapore;
e0950658@u.nus.edu
* Correspondence:amos.folarin@kcl.ac.uk
Abstract: IoT sensors offer a wide range of sensing capabilities, many of which have potential
healthapplications.ExistingsolutionsforIoTinhealthcarehavenotablelimitations,suchasclosed-
source,limitedI/Oprotocols,limitedcloudplatformsupport,andmissingspecificfunctionality
for health use cases. Developing an open-source internet of things (IoT) gateway solution that
addressestheselimitationsandprovidesreliability,broadapplicability,andutilityishighlydesirable.
CombiningawiderangeofsensordatastreamsfromIoTdeviceswithambulatorymHealthdata
wouldopenupthepotentialtoprovideadetailed360-degreeviewoftherelationshipbetweenpatient
physiology,behavior,andenvironment. WehavedevelopedRADAR-IoTasanopen-sourceIoT
gatewayframework,toharnessthispotential. ItaimstoconnectmultipleIoTdevicesattheedge,
performlimitedon-devicedataprocessingandanalysis,andintegratewithcloud-basedmobilehealth
platforms,suchasRADAR-base,enablingreal-timedataprocessing. Wealsopresentaproof-of-
Citation:Ranjan,Y.;Chang,J.; conceptdatacollectionfromthisframework,usingprototypehardwareintwolocations.TheRADAR-
Sankesara,H.;Conde,P.;Rashid,Z.;
IoTframework,combinedwiththeRADAR-basemHealthplatform,providesacomprehensiveview
Dobson,R.J.B.;Folarin,A.
ofauser’shealthandenvironmentbyintegratingstaticIoTsensorsandwearabledevices.Despite
RADAR-IoT:AnOpen-Source,
itscurrentlimitations,itoffersapromisingopen-sourcesolutionforhealthresearch,withpotential
Interoperable,andExtensibleIoT
applicationsinmanaginginfectioncontrol,monitoringchronicpulmonarydisorders,andassisting
GatewayFrameworkforHealth
patientswithimpairedmotorcontrolorcognitiveability.
Research.Sensors2024,24,4614.
https://doi.org/10.3390/s24144614
Keywords:IoT;gateway;health;research;RADAR-base;mHealth;remotemonitoring;extensible
AcademicEditors:SafakDogan,Xiyu
Shi,YogachandranRahulamathavan,
AndrewWeightman,GlenCooper,
HelenDawesandKatherineBradbury
1. Introduction
Received:29May2024 Intherapidlyevolvingworldofdigitalhealth,integratingmobilehealth(mHealth)
Revised:11July2024 andinternetofthings(IoT)platformsisrevolutionizinghowwecollect,analyze,andutilize
Accepted:13July2024 health data. This paper delves into the opportunities and challenges thistechnological
Published:16July2024
convergencepresentsandproposesourinnovativesolutiontoaddressingtheidentified
limitations. Given these challenges, our work was motivated by the need for an open-
source,mHealth-focusedIoTplatformthatseamlesslyintegratesandprocessesdatafrom
diversesources. OurgoalistobridgethegapbetweentheburgeoningIoTmarketand
Copyright: © 2024 by the authors.
specific health research needs, thereby unlocking the IoT’s full potential for advancing
Licensee MDPI, Basel, Switzerland.
healthresearch.
Thisarticleisanopenaccessarticle
Thelandscapeiswitnessingasignificantexpansioninmodernsensingcapabilities
distributed under the terms and
andnetwork-connecteddevices. Thisgrowthpresentsanopportunitytocollectlarge-scale
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// health data continuously and remotely, facilitating timely analysis for identifying and
creativecommons.org/licenses/by/ monitoring individuals’ health status [1]. Numerous established and emerging mobile
4.0/). health (mHealth) and internet of things (IoT) platforms exist within the market. These
Sensors2024,24,4614.https://doi.org/10.3390/s24144614 https://www.mdpi.com/journal/sensors

Sensors2024,24,4614 2of22
platformshavegainedincreasingimportance,duetotechnologicaladvancementsandthe
widespreadintegrationofwearablesintodailylife. Asaresult,unprecedentedpossibilities
(e.g.,home-basedandambulatorymonitoringandjust-in-timeinterventions)haveemerged
inresearchandclinicalapplications[2].
Theinternetofthingsisanetworkofphysicalobjects,“things”,comprisedofsensors,
software,andothertechnologies,tointeractdatawithotherdevicesandsystemsoverthe
internet. Theinternetofthingsrepresentsabroadcategoryofdevicesandsensorswiththe
commonattributeofnetworkconnectivity;theyformasupersetthatincludeswearable
devicesandsmartphones[3]. AnIoTgatewaydeviceactsasahub. Itinterconnectsall
IoTdevicesatalocation(called“at-edge”,i.e.,nearthesourceofthedata)tothecloud-
basedplatformsandIoTdevicesinotherlocations[4]. Itsfunctionalitymayalsoinclude
rudimentaryprocessingofdataandsecurity-andprivacy-orientedaccess. Thisscenario
hasbecomeincreasinglyrealisticandexcitingwithrecentdevelopments,suchasneural
processingunits(NPUs),64-bitCPUsat-edge,andadvancedartificialintelligence.
ThemaincontributionofthispaperisimplementingaflexibleIoTgatewayframework,
RADAR-IoT,directedtowardsimprovinghealthresearch. ByincorporatingIoTcapabilities
intotheopen-sourceRADAR-basemHealthplatform,weaimtoovercomethelimitations
ofwearabledeviceintegrationandtounlockabroaderspectrumofhealthdatacollection
possibilities,therebyenhancingthedepthandbreadthofinsightsderivedfromthecollected
data. ThispaperpresentsacomparativeanalysisofIoTframeworksandthemotivations
behind the proposed solution. This proposed IoT framework focuses on extensibility,
modularity, interoperability, performance, and utility in health research, among other
vitalfeatures.
Thepaperisdividedintosixsections,asfollows: Section2discussesthebackground
oftheIoTinthehealthdomain,theRADAR-baseplatformanditsapplications,related
work,andthedesignrequirementsfortheIoTgateway. Section3describesthearchitecture
ofourproposedIoTgatewayframework,asinformedbytherequirementsinSection2;
thissectionalsoprovidesdetailsaboutthesalientfeaturesoftheframework,including
performance, security, and privacy. Section 4 demonstrates the proof of concept (PoC)
for RADAR-IoT, to evaluate the framework in real-world settings. Section 5 discusses
thecontributionofourproposedsolutiontotheIoTinhealthresearchanditspotential
applications. Section6providestheconclusionoftheoverallpaper,includinglimitations
andfuturework.
Motivation
Theinternetofthings(IoT)sectorofthehealthcaremarketisprojectedtoreachUSD
534.3billionby2025,expandingatacompoundannualgrowthrate(CAGR)of19.9%[5],
asshowninFigure1. In2018,themarketwasvaluedatUSD147.1billion. Thissignificant
growthcanbeattributedtotheproliferationofwearablesandIoT-enableddevicesindaily
life,suchassmartvirtualassistantsandsmartlighting,aswellastheemergenceofcloud
computing, which enables the management and deployment of millions of connected
IoTdevices. However, theuptakeofthesetechnologiesinthemedical/healthresearch
domainismoreattenuated,withmorethan50%ofdoctorsexpressingconcernsoverIoT
devices’reliability[6]. TheseconcernsarisebecausetheIoTdataareoftenunprocessed,
non-standardized, and lack actionable or valuable intelligence. Integrating data from
multipledatasourceswithanmHealthplatformcapableofanalyzingreal-timedataatboth
thenetworkedgeandinthecloudhasthepotentialtogenerateactionableinformation.
Thesystemcanachieveadetailed360-degreeviewofthepatient’sphysiology,behavior,
and environment by leveraging this confluence of data and edge-processing capability,
combinedwithappropriatevalidation.

Sensors2024,24,4614 3of22
Figure1.Themarkettrendoftheinternetofthings(IoT)inhealth[5].
WhileawiderangeofIoTplatformsisavailableinthemarket,mostarecommercial
orclosed-source,andevenopen-sourcedplatformsaretypicallyconsumer-oriented,such
asthosedesignedforcontrollingsmarthomedevices. However,thereisaneedforopen-
sourcemHealthplatformsthatallowforinterconnectedIoTdevicesandofferastandard
interfaceforcollecting,aggregating,andanalyzingreal-timedatafrommultiplesources.
Thesesourcesincludewearables,IoTsensors,mobiledevices,andmedicaldevices,which
areessentialforhealthresearchandmorechallengingtotranslatetoclinicaldomains.
2. Background
AddressingchallengesinhealthresearchandthelimitationsofexistingIoTframe-
works is necessary. Specific requirements, such as extensibility, modularity, reliability,
security,andefficiency,shouldguidethedesignanddevelopmentoffuturesolutions,along
withthesupportofhealthplatforms,suchasRADAR-base. Thesesolutionsunderscorethe
IoT’spotentialinhealthresearchandpresentaviablesolutionforresearchersinthefield.
2.1. InternetofThings
Surveys on the IoT in healthcare [7,8] reveal that most IoT platforms suffer from
limitations,suchaslimitedsensorsupport,closed-sourcesystems,limitedI/Oprotocols,no
propercloudplatformsupport,nodemonstrableproofofconcept,andlimitedextensibility.
Thelimitationsidentifiedinthesesurveyshavesignificantpracticalimplicationsforhealth
research. Open-source software promotes transparency, community collaboration, and
potentialcost-effectivenessandcouldbolsterapplicationsinhealthresearch. Thelimited
sensorsupportandclosed-sourcesystemscanhindertheintegrationofdiversemedical
devicesanddatasources,potentiallylimitingthescopeandaccuracyofhealthresearch.
Additionally,theabsenceofpropercloudplatformsupportandlimitedI/Oprotocolsmay
impedetheseamlesscollection,storage,andanalysisofhealthdata,whichiscrucialfor
conductingcomprehensiveresearch.
Moreover, the need for verifiable proof of concept and limited extensibility could
restrict the scalability and adaptability of IoT platforms in health research, potentially
constraining innovation and advancements in the field. Addressing these limitations
is essential to ensure the robustness and effectiveness of IoT applications in healthcare
research. To address these issues, we have designed an open-source internet of things
(IoT)gatewayframeworkthatcaninterconnectmultipleIoTdevicesontheedge,perform
rudimentaryanalysis,andintegratewellwithestablishedmHealthplatformsinthecloud.
Finally,weevaluatedthesecapabilitiesinaproof-of-conceptdeployment.
2.2. RADAR-BasePlatform
RADAR-base[9]isanopen-sourceplatformthatintegratesdatastreamsfromvarious
wearablesandmobiletechnologies,tocollectsensordatainrealtimeandtostore,manage,
andsharethecollecteddata,knowledge,andinsightswithresearchersforanalysisand
actionable intelligence. As shown in Figure 2, it supports both passive and active data
collectionthroughtwoapplications,pRMTandaRMT,whichmonitormovement,loca-
tion,audio,calls,texts,andappusage,anditincludesquestionnaires,togatherpatient

Sensors2024,24,4614 4of22
information. RADAR-basehasbeenandiscurrentlybeingusedinvariousresearchstudies.
Refs. [10–14] focusing on personal sensing. However, the vendor availability of SDKs
and REST APIs limits the platform’s integration with wearable devices. The proposed
frameworkinthispaperextendstheplatformtoincludeIoTsensingcapability,expanding
therangeofusecases.
Figure2.An.overviewoftheRADAR-baseplatform[9]andintegrationofRADAR-IoT.
2.3. RelatedWork
We compare various IoT gateway frameworks in Table 1. RADAR-IoT [15] takes
inspirationfromsuchframeworksforitsdesignanddoesnotmeantoreplacethem.Instead,
ithasthepotentialtoconnecttothem,tocollectorpassdatatothem,hencemakinguseof
theexistingfunctionalitiesoftheseplatforms. Whilegeneralizedplatformsliketheseare
goodforbroaderusecases,theydonotshineforspecificusecases,suchashealthresearch
andremotemonitoringofpatients. Mostoftheplatformstypicallyuseaplatform-specific
messagebus,likeD-Bus.Still,thebenefitsofhavinganexternalindustry-standardmessage
broker are manifold, such as (i) event-driven programming and analysis, (ii) language
andplatform-agnosticpublishersandsubscribers,(iii)performance,(iv)extensibility,and
(v)interoperability. Someplatformsareprimarilycloud-based(thesecanonlyfunction
withaconnectiontotheirrespectivecloudservers);thishasclearlimitationsinprivacy-
constrained environments, such as hospitals, where a local network is preferred. The
existingIoTgatewaysshowninTable1areprimarilyintendedforcommercialorindustrial
use. Somehealthandresearchorganizationsprovidegatewaysasphysicaldevices[16],
limitingtheiradoptionandcontrol. Kesavanetal. [17]proposedagatewayframeworkfor
smarthealth;whilewell-designed,itislimitedtoafewbody-attachedsensors,supports
onlyBluetoothandWi-Fi,andprovideslimitedinformationoncloudplatformintegration.

Sensors2024,24,4614
5of22
Table1.IoTgatewayframeworkscomparison.
Open-
| No. Name |     | Usage | Protocols | Advantages | Disadvantages |
| -------- | --- | ----- | --------- | ---------- | ------------- |
Source?
ESFIoTEdge
|                 |     | Commercial | Generalindustrial    | Multipleclouds      |                   |
| --------------- | --- | ---------- | -------------------- | ------------------- | ----------------- |
| Framework       |     |            |                      |                     | Nohealth-specific |
| 1               | No  | or         | protocolsupport(like | supported;visual    |                   |
| (basedonEclipse |     |            |                      |                     | features.         |
|                 |     | Industrial | GPIO).               | wiringfordataflows. |                   |
Kura)[18]
Commercial Mostindustrial ExtensibleusingJava, Limitedcloudsupport,
2 EclipseKura[19] Yes or protocols(likeGPIO) withvisualwiringfor andhardtosetup.No
|     |     | Industrial | andMQTT. | dataflows. | health-specificfeatures. |
| --- | --- | ---------- | -------- | ---------- | ------------------------ |
Limiteddataprocessing
|               |     |     |     | Goodsupportand    | usingRules;only     |
| ------------- | --- | --- | --- | ----------------- | ------------------- |
| ASmartGateway |     |     |     | extensibilitywith | supportsThingspeak; |
3 Frameworkfor No Industrial Variable. ontologies,context requiresat-edgeHTTP
| IoTServices[20] |     |     |     | manager,anddevice | serverthatneedstoopen   |
| --------------- | --- | --- | --- | ----------------- | ----------------------- |
|                 |     |     |     | catalog.          | ports.Nohealth-specific |
features.
ubiworxIoT
|          |     | Commercial |               | Goodconnections    | Extendingcanbehard       |
| -------- | --- | ---------- | ------------- | ------------------ | ------------------------ |
| Gateway  |     |            | Mostprotocols |                    |                          |
| 4        | No  | or         |               | andprotocolsupport | withLuascripting.No      |
| Software |     |            | supported.    |                    |                          |
|          |     | Industrial |               | forclouds.         | health-specificfeatures. |
Framework[21]
Addedcomplexityfor
| ANovel | No,onlya |     | Unclearbut | Computationand |     |
| ------ | -------- | --- | ---------- | -------------- | --- |
extending.Noclear
CognitiveIoT theoretical Anyuse theoreticallycouldbe analyticsondata
| 5       |        |      |            |                  | supportforprotocolsor |
| ------- | ------ | ---- | ---------- | ---------------- | --------------------- |
| Gateway | frame- | case | addedinthe | fromsensorsbased |                       |
thecloud.No
| Framework[22] | work |     | cognitiveframework. | ontherulesset. |     |
| ------------- | ---- | --- | ------------------- | -------------- | --- |
health-specificfeatures.
Poorcloudsupport.No
|                  |     | Anyuse |                 | Goodsupportfor  | edgecomputingordata |
| ---------------- | --- | ------ | --------------- | --------------- | ------------------- |
| 6 DeviceHive[23] | Yes |        | Limitedsupport. |                 |                     |
|                  |     | case   |                 | featuresatedge. | processing.No       |
health-specificfeatures.
Onlyself(Thingspeak)
cloudsupport;noedge
None;primarilya
|                  |     | Anyuse |             | Easeofsetupand | computing(only         |
| ---------------- | --- | ------ | ----------- | -------------- | ---------------------- |
| 7 ThingSpeak[24] | Yes |        | cloud-based |                |                        |
|                  |     | case   |             | use.           | cloud-basedanalytics). |
platform.
Nohealth-specific
features.
Node-REDflows
|                  |     | Anyuse | None;primarilya |                    | Cloud-basedonly.No       |
| ---------------- | --- | ------ | --------------- | ------------------ | ------------------------ |
| 8 Thinger.io[25] | Yes |        |                 | wiringandreal-time |                          |
|                  |     | case   | cloudplatform.  |                    | health-specificfeatures. |
displayandtriggers.
Goodextensibilityof
|             |     | Anyuse |                 |                   | Noedgecomputing.No       |
| ----------- | --- | ------ | --------------- | ----------------- | ------------------------ |
| 9 Zetta[26] | Yes |        | Limitedsupport. | devicesatedgewith |                          |
|             |     | case   |                 |                   | health-specificfeatures. |
reactiveparadigm.
Goodsupportfor
Onlyself(OpenRemote)
|                   |     |            | Mostcommon          | edgecomputingwith    |                   |
| ----------------- | --- | ---------- | ------------------- | -------------------- | ----------------- |
| 10 OpenRemote[27] | Yes | Industrial |                     |                      | cloudsupported.No |
|                   |     |            | protocolssupported. | dataanalytics,rules, |                   |
health-specificfeatures.
andautomation.
|     |     |     |     | Easeofuseandsetup; | OnlyThingsBoardcloud |
| --- | --- | --- | --- | ------------------ | -------------------- |
ThingsBoard Anyuse Mostprotocols supportscommon supported.Limitededge
| 11          | Yes |      |            |                  |                          |
| ----------- | --- | ---- | ---------- | ---------------- | ------------------------ |
| Gateway[28] |     | case | supported. | protocolsforeasy | computing.No             |
|             |     |      |            | integration.     | health-specificfeatures. |
The IoT ecosystem is very diverse, with a wide range of hardware manufacturers,
andapplicationareasandstandardshavethusfarbeenchallengingtorealize. Thelarge-
scalenetwork,IoTsensorsheterogeneity,andthevolumeofIoTdataposechallengesfor
applicationdevelopment[29]. Middlewarecanofferstandardservicesforapplicationsand

Sensors2024,24,4614 6of22
supportinteroperabilitywithinapplicationsandservicesrunningonthesehubdevices.
RADAR-IoTaimstobeamiddlewaretoovercomesuchchallenges.
The proposed IoT framework’s (RADAR-IoT) primary objective is to augment the
existing RADAR-base mHealth platform [9] by incorporating IoT sensing capabilities.
RADAR-basepresentlyfocusesonambulatorymHealthdatafromphonesandwearables;
RADAR-IoTwillprovideabroaderrangeofsensoryinsightsintothecomplexinterplay
between patients’ physiology, behavior, and the surrounding environment. The addi-
tion of RADAR-IoT will lead to more informed healthcare decisions and personalized
interventions,e.g.,exposuretopoorairqualityinpulmonarydisorders,suchasCOPD.
2.4. DesignRequirements
Tomeettherequirementsdiscussedpreviously,weproposeanIoTedgeframework.
ThedesignideasfortheproposedIoTedgeframeworkaredepictedinFigure3. Essentially,
thedesignwasinformedbasedonthefollowingrequirements:
Figure3.RADAR-IoTdesignrequirements.
1. Extensibilityandflexibility: allowintegrationofanysensor,source,anddestination.
2. Modularity: allowforservices/componentstocommunicatethroughastandardAPI,
allowingthemtobeaugmentedorreplacedbycustomimplementations,facilitating
re-usability.
3. Supportapublish–subscribedesignpattern[30]: allowlocal-levelinteroperability,
reliability,andscalabilityattheedge.
4. Allowdatatobeconsumed,processed,anduploadedflexibly.
5. Operateonlow-powerandresource-edgedevices(likeRaspberryPizero[31]).

Sensors2024,24,4614 7of22
6. Observability: thesystemshouldallowcontinuousmonitoringfromvarioussensors
withdifferenthardwareinterfaceswithdatastandardization.
7. Reliability: supporthigh-fidelitydatacollectionatscaleandthroughput.
8. Dataanalysis: includingartificialintelligence(AI)applicationsandmachinelearning
(ML)attheedge.
9. Enableremotedeploymentandorchestrationofservicesatscale.
10. ProvideforinteroperabilitywithotherIoTdevicescomplyingwithasubsetofthe
OGCSensorThingsAPIstandard[32].
11. Supportserviceandmachinediscoveryattheedge.
12. Designedusingmoderntechnologies,toobtainbest-in-classfeaturesandperformance.
3. ProposedSolution
WedesignedRADAR-IoT(RADAR-base—internetofthings)asanIoTgateway[4]
frameworkforconnectingawidevarietyofsensorsandflexibleIoTsensordataprocessing
anduploading. RADAR-IoTalsosupportsuploadingtotheRADAR-baseplatformand
InfluxDb[33](localorcloud). Italsoprovidesreal-timevisualizationonGrafana[34]dash-
boardsandcanbeextendedtoincludemoreclouddestinations.Alltheentitiesarebasedon
abstractbasecomponentsandprovideextensionsforaddingmoredata-processingvariants
and sensors. The use of an external industry standard publish–subscribe [30] platform
likeRedisPub/Sub[35]orMQTT[36]makestheRADAR-IoTframeworklanguageand
platformagnostic.
3.1. ArchitectureOverview
The architecture of the RADAR-IoT framework, as shown in Figure 4, illustrates
its components and data flows from left to right, culminating in data transmission to
externalservices. TheframeworkisflexibleandcompatiblewithvariousIoTsensors(e.g.,
environmentsensors,video,andaudio)throughstandardinput/outputprotocols(like
I2C, GPIO, Serial, and more). Data are validated using a schema and converted into a
formatsuitablefordownstreamcomponents. Thesemessagesarethenforwardedtoor
published on the publisher–subscriber platform, where multiple consumers can access
them. Theconsumerreadsthesemessagesanduploadsthemtoexternalservices,suchas
thedashboardandtheRADAR-baseplatform[9]. Oncedataarepublished,theycanbe
usedindiverseways,includingcloudtransmission,on-devicedataanalysisorprocessing,
andNode-RED[37]flows(seebelow).
3.2. Publish–SubscribeBrokerorMessageQueue
RADAR-IoTusesaPublish–Subscribe(pub–sub)broker[30]asamessagequeuefor
publishing and consuming sensor data, providing several benefits. Firstly, an external
andwidelyusedpub–subsystem(suchasRedis[35],Kafka[38],orMQTT[36])enhances
reliability compared to a custom internal message bus by allowing direct data syncing
to the cloud running the same pub–sub broker. Secondly, the framework enables bi-
directionalproductionandconsumptionofdatabetweenthedataconsumerandexternal
applicationsorservices,enablingmultipletypesofpublishers,suchasbroadcastingdata
from one device to another anywhere on the same network. Thirdly, event-driven pro-
grammingandanalysisaresupported. Lastly,publishersandsubscribersarelanguage-
andplatform-agnostic.
3.3. OGCSensorThingsAPI
TheOpenGeospatialConsortiumOGCSensorThingsAPIprovidesanopen,geospatial-
enabled,andunifiedwaytointerconnectinternetofthings(IoT)devices,data,andapplica-
tionsovertheWeb[32]. WeusedasubsetofspecificationsfromtheOGCAPIspecification
todesigntheRADAR-IoTframework.
The channel or topic names in the publish–subscribe system provide a standard
to specify the task, hence providing a standardized way to publish and consume data.

Sensors2024,24,4614 8of22
This approach can expose canonically named endpoints to control and configure the
sensors. Forinstance,forasensorwith<sensor-name>,weusethefollowingformatfor
variousendpoints:
• /sensor/<sensor-name>/data-stream
• /sensor/<sensor-name>/error
• /sensor/<sensor-name>/control
• /sensor/<sensor-name>/config
Wehaveexposedanendpointthatcontainscomprehensivemetadatafromthesensors
inoperation,makingthesystemself-describing.
Figure4.ArchitectureoverviewofRADAR-IoT.
3.4. StateMachine
Astatemachine,alsoknownasafinitestatemachine,isamathematicalmodelthat
describesthediscretebehaviorofsystems. Itconsistsofasetofstates,transitionsbetween
thosestates,andactions. Inastatemachine,thesystem’selementsarealwaysinoneofa
finitenumberofstates,andeventsorconditionstriggerthetransitionsbetweenthosestates.
Incorporating a state machine [39] into the sensor abstractions, to capture and monitor
sensorlifecycleevents,confersenhancedvisibilityandinsightintotheframeworkand
sensors, enabling more resilient fault isolation, diagnosis, and efficient resolution. The
resulting event logs of a particular state are also disseminated to the pub–sub system,
thereby enabling downstream and upstream consumers to have full awareness of the
systemstateandtoleveragethisinformationresponsivelyforawiderangeofapplications.

Sensors2024,24,4614 9of22
3.5. Abstraction
The RADAR-IoT framework leverages interfaces and abstract classes. Adopting
object-orientedprogrammingprinciples[40]grantsthesystemenhancedflexibilityand
extensibility. Amongthespecificadvantagesarethefollowing:
• Themajorityofthecomponentsareabstractedandre-usable. TheSensorabstractclass
isthefundamentalunitforcollectingsensordata,withallsensorimplementations
requiredtoextendthisclassoroneofitssubclasses.
• The framework facilitates the creation of new abstractions based on existing ones.
Forinstance,byaddingagroupofsensorsthatinteractcoherentlythroughasensor
HAT or interface (like GrovePi HAT [41]) we can extend the Sensor class to add
HAT-specificimplementations(likeGrovePiSensor),allowingustoextendabstract
functionsinfurthersensor-specificsubclasses(likeGrovePiTemperatureSensor). This
approach provides a modular and extensible design, where the core Sensor class
handlesstandardfunctionality. Atthesametime,sensor-specificimplementationsare
encapsulatedinsubclasses,promotingcodere-use,maintainability,andflexibilityin
accommodatingdiversesensortypeswithinthesystem.
• Thisapproachenablesreliableincrementaltesting. Sincetheabstractionshavealready
beentested,onlythespecificextensionsmustbeunit-tested. Incrementaltestingen-
ablestargetedandefficienttesting,asweonlyneedtoverifythenewimplementation
detailsratherthanre-testingtheentiresystem.
3.6. SecurityandPrivacy
Securityandprivacyareparamountconcernswhencollectinghealthandenvironmen-
taldata,particularlygivenIoTsystems’substantialnumberofendpoints. Toaddressthese
issues,RADAR-IoTincorporatesseveralmeasures:
• SecureDataCollection: Asecurechannel,accessibleonlythroughhardwareinterfaces,
gatherssensordata.Packagingthehardwareinarobust,tamper-proofcasecanfurther
ensuresecurity.
• AuthenticationandAuthorization: Afterthedataaregatheredfromthesensor,they
are transmitted to the publish–subscribe broker. The broker runs in a trusted en-
vironment and is inaccessible through the network. The broker can be configured
withsolidsecurity,ensuringpublishersandsubscribersauthenticatebeforeaccess-
ingorsubmittingdata,andpreventingunauthorizedaccess. Thesecurityfeatures
will vary based on the publish–subscribe system used. Redis Pub/Sub [35] and
MQTT[36]brokerssupportpasswordauthenticationandaccesscontrollists(ACLs)
authorizationmethods. MQTTadditionallyalsosupportsencryptionandauditing.
Thepub–subchannelscanbesecuredusingindustry-standardencryptionprotocols,
suchasTLS/SSL,ensuringthedataareprotectedfromeavesdroppingortampering
duringtransmission.
• Pseudonymization: Alldataareassociatedwithpseudonymizedidentifiers,tosafe-
guardprivacyandpreventuserorenvironmentidentification. Thisprocessensures
thatthedatacannotbedirectlylinkedtoaspecificuserorenvironment. Theuser’s
privateidentifiableinformation(PII)iskeptseparatelyinasecureenvironmentwith
limitedaccessanddecoupledfromthesensordata.
• On-DeviceFeatureExtraction: Whenidentifiabledata,suchasaudio,areinvolved,
edge devices perform feature extraction of non-reversible features, which can be
sharedinsteadoftheoriginaldata. Thisfeatureextractioncapabilityisintegratedinto
theRADAR-IoTframeworkasaNode-REDmodule,ensuringthatsensitiverawdata
neverleavethedevice.
• Cloud Security: When uploading data to the cloud, RADAR-IoT conforms to the
standardsecuritymechanismsofthetargetsystems. Forinstance,RADAR-IoTem-
ploystheOAuth2.0[42]industrystandardforsecuringdataatRESTwhenuploading
datatotheRADAR-baseplatform,alongwithTLS/SSLencryption. Thesemeasures

Sensors2024,24,4614 10of22
ensurethatthedataareprotectedbothintransitandatrestandthatonlyauthorized
applicationscanaccessthedata.
Byimplementingthesemeasures,RADAR-IoTprovidesarobustsecurityandprivacy
framework,toprotectsensitivehealthandenvironmentaldatafrompotentialthreats.
3.7. Performance
RADAR-IoT’s performance is optimized through several key strategies, including
multi-processscheduling, efficientsensordataprocessing, queueuse, robustexception
handling,andfaultisolation.
• Multi-ProcessScheduling: RADAR-IoTemploysamulti-processschedulingapproach
tohandlingmultipletasksconcurrently. Thisapproachallowsthesystemtoprocess
data from multiple sensors simultaneously, significantly improving the system’s
overallthroughput. EachprocessisensuredadequateCPUtimebythescheduling
algorithm,preventinganyprocessfrommonopolizingthesystemresources.
• ProcessingofSensorData: Thesystemefficientlyprocesseslargevolumesofsensor
data. Itemploysefficientdatastructuresandalgorithms,minimizingthecomputa-
tionaloverhead. Thesystemalsousescachingtechniquestostorefrequentlyaccessed
datainmemory,reducingtheneedforexpensivediskI/Ooperations.
• Use of Queues: RADAR-IoT uses queues to manage the data flow after receiving
thedatafromthesensors. Queuesensurethatevenifacomponentistemporarily
unabletoprocessincomingdata(e.g.,ifthepub–subsystemisbusyordown),thedata
arenotlostbutareinsteadqueuedforlaterprocessing. Thisqueue-basedapproach
enablesordereddataprocessingandhelpstosmoothoutvariationsindataarrival
rates,preventingsystemoverloads.
• RobustExceptionHandling: Thesystemincludesrobustexception-handlingmecha-
nisms,toensurethatitcanrecovergracefullyfromerrors. Whenanexceptionoccurs,
thesystemlogstheerrorforlateranalysistheneitherattemptstocorrecttheerroror
skipstheproblematicoperation,dependingonthenatureoftheerror. Thisensures
thatasingleerrordoesnotcausetheentiresystemtofail.
• FaultIsolation: WedesignedRADAR-IoTwithfaultisolationinmind. Eachsystem
componentrunsinitsownprocessspace,soifonecomponentfails,itdoesnotaffect
theothers. Eachcomponentcanbeeasilyidentifiedanddiagnosedforfaultswiththis
design,aseverypartistestableanddebuggableindependently.
Byimplementingthesestrategies,RADAR-IoTensureshighperformanceandreliabil-
ity,evenwhendealingwithlargevolumesofsensordataandhighsystemactivitylevels.
3.8. DataTypingandSchematization
Avroschemas[43]areacrucialtoolfordatatyping,validation,andstandardization.
Beforepublishingsensordatatothepub–subbroker,thesystemvalidatesandconverts
it,usingAvroschemas. Thisprocessensuresconsistentdatarepresentationandfacilitates
schema evolution and backward compatibility. The converter can read schemas from
various sources, including local files, GitHub-hosted files, and the Confluent Schema
Registrycomponent[44]. TheRADAR-baseplatformacceptsAvro-formatteddata,hence
streamliningdataupload.
3.9. DataProcessingandAnalysis
TheRADAR-IoTframeworkisdesignedtohandlereal-timesensordataandprovides
anextensiblemodulefordataprocessingandanalysisthatcansupportvariousmethods.
Hereisabreakdownofsomeofthecurrentlysupportedmethods:
• tinyML[45]: ThisisaparadigmthatenablesAIandmachinelearning(ML)inlow-
powerandresource-constrainededgedevices. TherationalebehindusingtinyMLis
tobringthepowerofMLtoIoTdevices,whicharetypicallyconstrainedbypowerand

Sensors2024,24,4614 11of22
computationalresources. Thisallowsforreal-time,on-deviceprocessingandanalysis
ofsensordata,reducingtheneedfordatatransmissionandpreventingprivacyleaks.
• Dataaggregationsandtransformations: Theseareessentialdataprocessingmethods
that are used to prepare and clean the sensor data for further analysis. Aggrega-
tionmethodsmightincludecalculatingspecificfeaturesoverprecisetimeintervals.
Transformationmethodsmightincludenormalizationandscaling. Thesemethods
areessentialfordealingwithreal-timesensordata,whichcanbenoisyandcomein
largevolumes.
• Node-RED [37]: Node-RED is a programming tool for wiring together hardware
devices, APIs, andonlineservicesinnewandexcitingways[46–49]. Itprovidesa
browser-basedfloweditorthatmakesiteasytowiretogetherflows,usingthewide
rangeofnodesinthepalette. Flowscanthenbedeployedtotheruntimeinasingle
click.UsingNode-REDallowsforeasyandflexibledataanalytics,usingano-codeweb
interface,makingitaccessibletouserswithoutacodingbackground. Figure5shows
anexampledataprocessingpipelineusingNode-REDforaudiofeatureextraction.
• RADAR-basecloudplatform[9]: Formoreadvancedanalysisthatrequireshighcom-
putationalresources,theframeworkcandelegatetheanalysistocloudplatforms. This
allowsforusingmorecomplexMLmodelsandalgorithmsthatmaynotbefeasible
torunonedgedevices,duetoresourceconstraints. Moreover,thesecloudplatforms
canalsointegrateandanalyzedatafromvarioussources,includingwearablesand
mobilephones. Thismulti-sourcedataintegrationcanprovideamorecomprehensive
viewofthesituation,therebyimprovingthequalityoftheanalysisandtheaccuracy
oftheresults.
In summary, the rationale behind the chosen methods and models is to provide a
flexible, scalable, and accessible framework for real-time sensor data analysis, capable
ofrunningbothonresource-constrainededgedevicesandonpowerfulcloudplatforms.
Thechoiceofmethodsallowsforawiderangeofanalysistasks,frombasicdatacleaning
and preparation to advanced ML models. The use of tools like Node-RED also makes
the framework accessible to non-programmers. More advanced analysis methods are
planned for future implementation, which will further enhance the capabilities of the
RADAR-IoTframework.
Figure5.ExampleNode-REDworkflowsaugmentingRADAR-IoT.
3.10. Node-REDWorkflows
Node-REDisalow-codeprogrammingtoolthatenablestheintegrationofhardware
devices,APIs,andonlineservicesinnovelandinnovativeways.Itfeaturesabrowser-based
editorthatfacilitatesthecreationofflows,usingadiverserangeofnodesfromthepalette,
which can be deployed to its runtime with a single click [37]. Node-RED can generate

Sensors2024,24,4614 12of22
manyflowcombinationsforvarioususecases,asdemonstratedbyanexampleusecase
ofalertinginFigure5. TheRedis-InorMQTTnode(basedonthepub–subbrokerinuse)
is required to read data from RADAR-IoT. The example in Figure 5 illustrates an alert
workflowthattriggersanemailifnodataarereceivedwithinaspecifiedtimewindow.
This feature enables administrators to investigate potential issues with data collection.
AnotherflowdemonstratedisreadingaudiofromtheMQTTbroker,performingfeature
extraction,andthenuploadingittothecloud.
Thislow-codesolutionusingnodesandflowsmakestheframework’sconfiguration
highlyextensible,and,withrelativelyloweffort,awidevarietyofusecasesispossible.
3.11. MethodsofDeployment
The RADAR-IoT platform is modular, comprising three separate components that
needtobedeployed. (asshowninFigure4):
1. The Python module that connects to sensors and handles I/O. This module also
validates and converts the data, using Avro schemas [46] before publishing to the
pub–subbroker,asdepictedbythebluecomponentsinFigure4.
2. Thepublish–subscribebroker(currentoptionsincludeRedis[35],MQTT[36])shown
bythedashedpinklinesinthemiddleinFigure4.
3. Thedataconsumermodulesubscribestothesensordata,uploadsdatatothecloud,
andperformslimitedon-deviceanalytics. Theseareshownbythecrimsoncompo-
nentsinFigure4.
PackagingtheframeworkasDockerimagesallowsustouseorchestrationframeworks
likeNebula[50]toremotelydeploy,maintain,andupgradelargefleetsofIoThubdevices.
TheRADAR-IoTframeworksupportsvisualizationtoolslikeGrafanaandtheRADAR-
baseplatformasbackends. MostcloudIoTplatformssupportpublish–subscribebrokers,
allowing RADAR-IoT to integrate into multiple cloud backends easily. These types of
extensions are supported through the simple no-code Node-RED configuration flows
(seebelow).
3.12. DeploymentConfigurations
TheRADAR-IoTframework’smodulararchitectureallowsfordeploymentinvarious
configurations,tomeetdiverseusecases. Belowaresometypicalpatterns.
3.12.1. MultiplePrimaryDevices
AsFigure6ashows,thisconfigurationallowsoneormultipleautonomousIoTgateway
devices running RADAR-IoT to gather data from sensor sets. These devices operate
independentlyanddonotcommunicatewitheachother.
(a)
Figure6.Cont.

Sensors2024,24,4614 13of22
(b)
(c)
Figure6.RADAR-IoTdeploymentconfigurations.(a)RADAR-IoTsimpledeploymentconfiguration.
(b)RADAR-IoTdeploymentinprimary–subordinateconfiguration. (c)RADAR-IoTdeployment
configurationforlocalnetwork(nointernetaccessrequired).
3.12.2. PrimaryandSubordinates
Theproposedconfiguration,asillustratedinFigure6b,involvestheutilizationofa
primary–subordinatearchitecturewithintheRADAR-IoTframework. Asingledevicehost-
ingallframeworkcomponentsistheprimarygatewayinthissetup. Multiplesubordinate
devicesequippedwithsensorsareresponsibleforinterfacingwithandcollectingsensor
data. Thesesubordinatedevicestransmitthecollecteddatatotheprimarydevice. The
primarydevicecanalsodirectlyinterfacewithandcollectdatafromthesensorsifneeded.
However,onlytheprimarydeviceinteractswithdatauploadingandconsumingservices,
likedashboardsandcloudplatforms.
This configuration offers several advantages, especially when deploying multiple
independentIoTgatewaydevicesisnotfeasibleorresourceconstraintsexist. Theprimary–
subordinate architecture optimizes data collection and management while minimizing
resourceutilization. Thisapproachensuresefficientandcentralizeddataprocessingwhile
accommodatinglimitationsregardingavailableresourcesordeploymentfeasibility. This
architectural approach may be more susceptible to failures, as the primary device can
representasinglepointoffailureattheedge.Iftheprimarydevicemalfunctionsorbecomes
unavailable, it could cause a complete outage of all sensor data collection, potentially
resultinginsignificantdatalossorinterruptionofcriticalmonitoringfunctions.
3.12.3. LocalNetworkOnly
While deployment configurations (a) and (b) typically utilize a remote or cloud-
hosted RADAR-base platform, it is also possible to deploy RADAR-base on the local
networkserversandsosatisfycriteriaforlocaldeployment. Thisconfigurationprecludes
internetaccess,typicallydesignatedforin-hospitalswheretransmittingdataoutsidethe

Sensors2024,24,4614 14of22
internalnetworkisnotdesired. SinceallRADAR-IoTcomponentsandassociatedexternal
servicesareopen-source,theycanbedeployedonlocalnetworkcomputers/serversand
operate effectively in a completely isolated “air-gapped” environment. The example
configuration depicted in Figure 6c comprises the RADAR-base platform, the Grafana
dashboard for visualization, and the AI/ML data consumer for anomaly detection, all
supportedbyRADAR-IoT.
3.13. MethodsforManagement,Maintenance,andMonitoring
The management and orchestration of services on an IoT platform is an essential
aspectofnon-trivialdeployments,asthedeploymentmayneedtoscaletohundredsof
thousandsofdevices. Atypicalscenarioishavingmanydevicesandneedingtoupdate
theversionofthesensorinterfaceserviceonallofthem;doingthismanuallyoneachof
those(evenremotely)isnotfeasible.RADAR-IoTaddressesthisthroughautomation,using
externalopen-sourcemanagement,maintenance,andmonitoringsolutions. Theseoptions
presentlyincludethefollowing:
• Managementandmaintenance: Nebula[50](anorchestrationtoolforIoTdevicesthat
useDocker-basedservices)andDataplicity[51](aremoteIoTdevicemanagement
service)
• Monitoring: Node-RED[37]+Grafana[34](providinginter-andintra-devicemoni-
toringandalerting)andNetdata[52](professionalsystemmonitoring)
4. ProofofConcept(PoC)
Theproofofconcept(PoC)demonstrationoftheRADAR-IoTframeworkaimedto
evaluate the framework in real-world settings, confirm the reliability of the integrated
frameworkandsensors,andcollectsensordataundercontrolledtestconditions. ARasp-
berryPi4Bdevice[31]withfourtypesofsensorswasusedtodeploytheframeworkinboth
anofficeandahomeenvironment. Datawerecollectedoverthreemonths,withnotable
eventsdocumentedfor14days,andtheywereanalyzedusingaGrafanadashboardand
theRADAR-baseplatform. ThePoCisanevaluationoftheframeworkanditsintegrations
ratherthanofthehardwaredevicesused.
4.1. Aims
Theobjectivesoftheproofofconcept(PoC)demonstrationoftheRADAR-IoTframe-
workareasfollows:
• Evaluateanddemonstratetheframeworkinareal-worldsetting.
• Establishthattheintegrationframeworkandthesensorsperformasexpected.
• Collectreal-worldsensordatawithcontroltestconditions,toassesschangesinstate
toaknownperturbation.
4.2. Methods
Forthisstudy,wedeployedtheRADAR-IoTframeworkintwodistinctsettings: a
sharedofficespaceandahome-basedenvironment,usingaRaspberryPi4Bdevice(4GB
model)[31]equippedwithfoursensors—airquality,motion,temperature,humidity,and
light—connected via the Grove Pi hat [41]. The 64-bit Raspbian OS (based on Debian
Linux)wasusedtodeploytheRADAR-IoTframeworkonthedevice. Wedeployedthe
frameworkcomponentsusingDockerimages,toensurereproducibleenvironments. The
DockerimageswerebasedonPython3.9forthePythonsensorinterfacemoduleandJava
Development Kit (JDK) version 11 for the Kotlin-based data consumer module. Redis
Pub/Subwasthechoiceofpublish–subscribebroker, deployedusingtheofficialRedis
Dockerimage. TheDockerComposefilesusedinthisproofofconceptareprovidedin
theGitHubrepository[53]. Theconfigurationsusedforvarioussensorsanddestination
targetsinthePoCareprovidedintheprojectwiki[54]. Thisinformationcanbeusedto
reproducetheexactenvironmentandsettingsusedfortheproofofconcept.

Sensors2024,24,4614 15of22
Datawerecollectedoverthreemonths,duringwhichadiarywaskeptfor14days,
to document any positive control events in the home-based setting, such as coughing,
sneezing,openingawindow,physicalactivityintheroom,andturningheatingon/off. We
configuredtheRADAR-IoTframeworktouploadthedatatoareal-timeGrafanadashboard
forvisualizationandtheRADAR-baseplatformforhistoricalanalysis.
4.3. Results
ThefirstdeploymentoftheframeworkwasonaRaspberryPi4B[31]withaGrovePi
Plushat[41]andthreeplugged-insensorsinstalledinasharedofficespace. Figure7shows
thedashboardscreenforaweekofdatacollectedfromtheaboveofficedeployment.
Figure7.Real-timedashboard.Thesensorsareairquality,temperature,humidity,andmotion,from
toptobottom.Thegreenareasaretimesofday(9:00–18:00)duringtheweekends(holiday),while
theblueareasaretimesofday(9:00–18:00)duringtheweekdays. Asexpected,thevaluesdiffer
betweentheweekdaysandweekendsforalmostallthedata,duetovariationsinroompopulation.
Forinstance,weekdayshavehighermotion,airquality,andtemperature,sincepeopleworkinrooms
withlowerhumiditythanonweekends.
Theseconddeploymentwasdoneinahome-basedenvironment. Afterpre-processing
thedata(excludingoutliers)andtakingthedayswithatleastone“open-window”diary
event,thecorrelationbetweenthepositivediaryeventof“open-window”withthe“air-
quality”sensorvalueswasfoundtobe,onaverage,−0.61usingtheSpearmancorrelation
coefficient[55]. Openingthewindowimprovedtheroom’sairqualityanddecreasedthe
airpollutants(asmeasuredbythesensor),resultinginanegativecorrelation.
Figure8presentsthelightsensordatacollectedoveraweekofmonitoring. Theplot
showsexpectedpatternsoflightvalues,withhighervaluesrecordedinthemorningwhen
thesunroseandtheroomreceivednaturallight. Asthesunstartedtoset, therewasa
gradualdecreaseintheamountoflightrecordedbythesensor. Whentheartificiallight
in the room was turned on, the values jumped steeply, to form a second smaller peak
(to the right side of the sunlight peak). The red line in the plot marks the local time of
10:30p.m.,whichisapproximatelywhentheroomuserwouldgotosleepandturnoffthe
light,resultinginthelightsensorvaluesdroppingtonear0.
Thedatacollectionapparatuswasleftonforapproximatelythreemonths,tomeasure
thecompletionofdata. Monitoringofthesetupwaslimitedtobiweeklychecks,withonly
one issue reported during the monitoring period, due to a change in the home’s Wi-Fi
network. Table2presentsthecompletionmetricsforthesensorsoverthethreemonths,pro-
vidingvaluableinsightsintothereliabilityandperformanceofthedatacollectionsystem.

Sensors2024,24,4614 16of22
Figure8.Lightsensordata.Intradaychangescanbeseencorrespondingtosunriseandsunset.
Table2.Completionofdatafromhome-basedmonitoring.
PercentCompletion SamplingInterval
Sensor Description
(%) (Seconds)
Thissensorisacomprehensiveindoorairmonitor,
AirQuality[56] responsivetoavarietyofharmfulgases,includingcarbon 90.94 5
monoxide,alcohol,acetone,thinner,andformaldehyde.
Thissensorisapre-calibrateddigitaldeviceformeasuring
Temperatureand temperatureviaanegativetemperaturecoefficient(NTC)
91.46 10
Humidity[57] thermistorandrelativehumiditythroughaunique
capacitiveelement.
Thissensordetectsmotion,specificallyhumanmovement
Motion[58] withinitsrange,andoutputsHIGHonitssignalpinwhen 83.58 1
motionisdetected.
Thissensorusesaphoto-resistortodetectlightintensity,
Light[59] producingananalogoutputsignalthatincreaseswith 86.59 30
brightness,facilitatedbyanon-boardLM358OpAmpchip.
5. Discussion
As shown in Figure 9, using the RADAR-IoT framework with the RADAR-base
mHealthplatformprovidesa360-degreeviewintoauser’shealthandenvironment,com-
biningstaticIoTsensorsdependentonanedgedeviceandambulatorywearabledevices,
providingthepossibilityofcombiningrichinformationfromwearabledevices, mobile
phonesensorsandinteractions,questionnairesandtasks,andenvironmentalsensors(such
asindoorairquality,temperature,humidity,andtoxicgaslevels).

Sensors2024,24,4614 17of22
Figure9. RADAR-IoTandRADAR-baseplatformsenablethecaptureofpotentialmodalitiesfor
healthresearch.
ComparedtootherIoTplatformsinTable1,theRADAR-IoTframeworkoffersseveral
uniqueadvantagesandinnovationsthatmakeitstandout:
• 360-DegreeView: Unlikemanyotherplatforms,RADAR-IoTprovidesacomprehen-
sive360-degreeviewintotheuser’shealthandenvironment, asmentionedabove.
Thisrichinformationsetprovidesamoreholisticunderstandingoftheuser’scontext.
• Open-Source and Versatile: RADAR-IoT is an open-source solution, which means
it can be freely used, modified, and distributed. It can be used in any use case
andsupportsmostprotocols,makingitmoreversatilethanmanyotherproprietary
platformsthatarelimitedintheirusecasesandprotocolsupport.
• EdgeSupport: OneofthecriticaladvantagesofRADAR-IoTisitsedgesupport. It
providesdashboards,dataprocessing,andanalysiscapabilitiesattheedge,which
isuncommoninmanyotherplatforms. Thesecapabilitiesenablemoreefficientdata
processingandreal-timeinsights.
• Cloud Support for Health Data: RADAR-IoT offers cloud support for health data,
usingtheRADAR-baseplatform[9]. ThisfeatureisuniquetoRADAR-IoTandisnot
foundinmanyotherplatforms,especiallythosewithouthealth-specificfeatures.
• No-Code Extensions: RADAR-IoT supports no-code extensions, using Node-RED
wiring[37],allowingeasycustomizationandextensionoftheplatformwithoutthe
needforextensivecoding,makingitmoreaccessibletonon-technicalusers.
In comparison, many other platforms listed in the table either lack health-specific
features, have limited cloud or edge support, are not open-source, or do not provide a
360-degreeviewofauser’shealthandenvironment.Thesefactorshighlighttheadvantages
and innovations of RADAR-IoT in the IoT for Health landscape. While RADAR-IoT is

Sensors2024,24,4614 18of22
still in development and has a few limitations, such as a lack of ease during setup and
nosupportforwirelesssensors, itsongoingdevelopmentmeanstheseissuesarebeing
addressedandimproved.
WenowdiscusssomepotentialapplicationareascombiningRADAR-IoTwiththe
existing ambulatory data collection capabilities of RADAR-base. Managing infection
controlcanbechallenginginhospitalwards. Exposuremonitoringcouldbeperformed
by tracking room visits and using air quality sensors to measure room particulate and
airhumiditylevels,togiveareadoutofairqualitystatusorairflowdynamicsthrougha
building. Additionally,wecouldcombinecoughcountingwithmicrophonesanduseedge
deviceclassificationanalysisoftheaudio.
Similarly,wecouldenablecontinuouspassivemonitoringofcoughs,sneezing,and
snoring(includingapneaandhypopnea)inhomesettingswithasimilarsetup,usinga
microphone,airqualitysensor,wearabledevices,andstaticbedmattresssensors. Combin-
ingIoTwithambulatorysensorsisattractive,especiallyincaseswheretheenvironment
contributesdirectlytothediseaseanditssymptoms. Forinstance,inthecaseofchronic
pulmonarydisorders(e.g., COPDorasthma), poorairqualityorallergenscanhavean
adverseeffectontheuser’shealth,includingincreaseddurationandintensityofcoughing
and wheezing. Poor air quality can be an essential factor in the relapse of depression
andanxiety[60]. SimilarstudiesshowairqualityimprovedafterintroducingtheLondon
ultra-lowemissionzones(ULEZ)[61]. Thesewereintroducedduetohighairpollutionin
thecitycausinghealthissuesforresidents[62].
Anotherexampleusecaseisformonitoringconditionswheretheparticipant’sim-
pairedmotorcontrolorcognitiveabilityaffectstheircapacityforeverydaylivingfunction:
forexample,indementia,suchasAlzheimer’sdisease[63]. Insuchcases,theRADAR-IoT
frameworkcancapturecertainenvironmentalevents,whichcouldhelpinunderstanding
theprogressionofdiseaseorlossofactivitiesofdailyliving,e.g.,usingdoorormotion
sensorstodetectwhenaparticipantopensadoororcupboard—usingarangeofdifferent
sensingcapabilitiestomonitorandbuildupapictureofhome-basedutilitywhilesimulta-
neouslycomplementingthiswithwearablesensors,toprovideinsightintotheirbehavior
andphysiology. Withanincreasinglyelderlypopulation,improvedin-communitycarefor
patientpopulationswillbeasignificantrequirement;thistypeofcontinuous,passivemon-
itoringandriskassessmentoralertingondetectingcriticaleventscouldbeincorporated
intoandaugmentafuturecaresystem.
TheRADAR-IoTframeworkcouldalsobeimplementedintheclinicalenvironment,
totracetheconversationbetweenapatientandadoctor. Usingaudiosensors, itcould
recordtheseeventsandfurtheranalysisthatwouldsufficientlyprovideinsightintothe
patient’shealthstatusorevenaprognosisonhoweffectivespecifictreatmentsare. This
wouldbeparticularlyusefulinamentalhealthclinic,whereinsubtlespeechcharacteristics
mayrevealapatient’smentalstate. Itcouldpickupontone,speed,andvolumeofspeech,
even detecting feelings of distress or confusion, allowing real-time feedback to health
professionalssothattheycouldadjusttheirapproachortreatmentplanasneeded.
TheRADAR-IoTframeworkfurtherpermitsmonitoringapatient’sphysicalhealthin
anon-intrusivemanner. Toelaborate,continuousfollow-upofvitalsignsthatincludeheart
rate,bloodpressure,andoxygenlevelcouldbemanagedwithwearabledevices. These
datacouldbelinkedtoenvironmentalsensordatacapturingtemperatureandhumidity
levelstobuildanall-roundedviewofpatients’healthandenvironment. Thiscouldbe
veryusefulinchronicconditions,suchasdiabetesorheartdisease,wherebycontinuous
monitoringwouldgiveindicatorsofanoncominghealthcrisis.
6. Conclusions
RADAR-IoTtakesinspirationfromexistingworkinIoTandseekstoaddressseveral
limitations with current IoT gateway frameworks for health research. The limitations
encompasssourcecodeavailability,sensortypesandI/Oprotocols,interoperabilityand
scalability,cloudplatformsupport,andedgeprocessing[7,8,29,64].

Sensors2024,24,4614 19of22
The design and proof-of-concept deployment highlight some critical areas where
RADAR-IoTdifferentiatesitselffromrelatedsystems. Firstly,thesystemisdevice-,sensor-,
and programming language-agnostic for interoperability. The open-source nature of
RADAR-IoTmakesitreadilyextensible,andthemodulardesignallowsforeaseofcomposi-
tion. Lastly,itsupportsawiderangeofIoTinput/outputprotocolsandmultipledatasinks,
includingbutnotlimitedtotheRADAR-basemHealthplatform,on-devicedataprocessing,
and Grafana dashboards [34]. On the security and privacy side, RADAR-IoT supports
industry-leading security and privacy, using standards such as identity management,
OAuth2.0[42],encryptionintransitandatrest,pseudonymization,anddatatypingand
schematization. IntegrationwithRADAR-base[9]providesawell-establishedopen-source
mHealthcloudbackendfordatacollection,aggregation,transformation,compute-intensive
analytics,andacombinationofdifferenttypesofdatasources,likewearables,IoTsensors,
mobileapps,andeCRFs.
WehavedemonstratedaproofofconceptusingRADAR-IoTtoflexiblyconnectarange
ofIoTsensorsandhowthesedatacouldbecollectedandusedwithvariousthird-party
integrations. IncorporatingstaticIoTsensorswiththeRADAR-baseplatformprovidesa
comprehensiveviewofthepatient’shealthandenvironment,allowingforamoreholistic
understandingofhowthesefactorsinteractwithandimpactpatientoutcomes.
RADAR-IoTprovidesareferencearchitectureasasolidfoundationforimplementing
IoTinhealthresearch. Itsopen-sourcedatacollectioncapabilitiesarecrucialforthefuture
ofresearch,healthcareautomation,andresponsiveinfrastructure. Despiteitsnoveltyand
effectivenessinreal-worldsettings, theplatformhaslimiteddeveloperdocumentation,
unprovenusefulnessinahealthresearcharea,complexityduringinitialsetup,andlimited
remotemanagementandcontrolsupport.
Lookingahead,weplantointegrateRADAR-IoTwithabroaderrangeofsensortypes.
Thisexpansionwillenablethesystemtocollectamorediverserangeofdata,enhancingits
abilitytoprovideacomprehensiveviewoftheuser’shealthandenvironment. Wealsoaim
toenhanceRADAR-IoT’sdataanalysiscapabilitiesbyincorporatingmoresophisticated
algorithms for interpreting sensor data and deriving insights. This enhancement will
improve the system’s ability to detect patterns and trends in the data, which could be
vitalforearlyidentificationofhealthissues. Inadditiontotheseimprovements,weplan
todeployRADAR-IoTmorebroadlyinclinicalsettings. Thisbroaderdeploymentwill
allowustogathermoredataandbetterunderstanditsperformanceandeffectivenessina
real-worldhealthenvironment. Wealsoplantobundlethesoftwareframeworkandthe
hardwaredeviceasasolutionforeaseofuse. Thissolutioncouldbepreconfiguredwith
sensors,e-simsformobilenetworkconnectivity,portablepowersources,andpredefined
softwarecomponentsbasedondiseasetypesforaplug-and-playsolution.
Tofullydemonstratethepracticalvalueoftheframework,weplantoconductfurther
pilotstudiesthatevaluateitsperformanceinreal-worldhealthresearchusecases. These
studieswillinvolveadetailedanalysisofdatacollectedfromwearables,apps,andIoT
sensorsandwillaimtoprovideconcreteevidenceoftheframework’seffectivenessand
combined utility in improving patient outcomes. As part of our future work, we will
scientificallyevaluatequantitativeperformancemetrics,suchasdatathroughput,latency,
andenergyconsumptionforthedeployedsensors. Thisevaluationwillhelpusidentify
areas where the system’s performance could be improved, ensuring that RADAR-IoT
continuestomeettheneedsofthehealthdomain.
Author Contributions: Conceptualization, Y.R., P.C., Z.R., R.J.B.D. and A.F.; methodology, Y.R.,
P.C.,Z.R.,R.J.B.D.andA.F.;software,Y.R.,J.C.,H.S.,P.C.andA.F.;validation,Y.R.,J.C.,H.S.and
A.F.;formalanalysis,Y.R.,J.C.,R.J.B.D.andA.F.;investigation,Y.R.andJ.C.;resources,R.J.B.D.and
A.F.;datacuration,Y.R.andA.F.;writing,Y.R.,J.C.,H.S.,Z.R.andA.F.;writing,R.J.B.D.,P.C.and
A.F.; visualization, Y.R.; supervision, R.J.B.D.andA.F.; projectadministration, Y.R., R.J.B.D.and
A.F.; fundingacquisition, R.J.B.D.Allauthorshavereadandagreedtothepublishedversionof
themanuscript.

Sensors2024,24,4614 20of22
Funding:TheauthorsreceivedfundingsupportfromtheNIHRBiomedicalResearchCentreatSouth
LondonandtheMaudsleyNHSFoundationTrustandKing’sCollegeLondon.Theviewsexpressed
arethoseoftheauthorsandnotnecessarilythoseoftheNHS,theNIHR,ortheDepartmentofHealth.
InstitutionalReviewBoardStatement:Theethicalapprovalforthisproofofconceptwaswaivedby
theResearchEthicsCommittee(REC)ofKing’sCollegeLondon(KCL)astherewasnocollectionof
primarydatafromhumanparticipants.
InformedConsentStatement:Notapplicable
DataAvailabilityStatement: Allthedatafromtheproofofconcept(includingtheeventsdiary
data)areavailablepubliclyonline[65].Thedataarepseudonymizedaccordingtothepoliciesand
processesoftheRADAR-baseplatform,whichprovidespseudonymizedsensordata.
Acknowledgments: Backend infrastructure facilities were provided by the King’s College Lon-
donOpenStackCloud“Rosalind”. Rosalindwasfundedwiththefollowingcapitalequipment
grants:GSTTCharityreference:STR130505andMaudsleyCharityreference980.Theauthorsalso
acknowledgethesupportofNIHRUniversityCollegeLondonHospitalsBiomedicalResearchCentre.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
AI artificialintelligence
API applicationprogramminginterface
CAGR compoundannualgrowthrate
COPD chronicobstructivepulmonarydisease
ESF everywaresoftwareframework
GPIO general-purposeinput/output
GSTT Guy’sandStThomas’NHSFoundationTrust
HTTP hypertexttransferprotocol
IoT internetofthings
I/O input/output
KCL King’sCollegeLondon
ML machinelearning
MQTT MQtelemetrytransport
NHS NationalHealthService
NIHR NationalInstituteforHealthandCareResearch
OGC OpenGeospatialConsortium
OSGI openservicesgatewayinitiative
PoC proofofconcept
RADAR remoteassessmentofdiseaseandrelapse
REC ResearchEthicsCommittee
UK UnitedKingdom
ULEZ ultra-lowemissionzone
URL uniformresourcelocator
mHealth mobilehealth
USD UnitedStatesdollars
References
1. Jat, A.S.; Grønli, T.M. Harnessing the Digital Revolution: A Comprehensive Review of mHealth Applications for Remote
MonitoringinTransformingHealthcareDelivery. InInternationalConferenceonMobileWebandIntelligentInformationSystems;
Younas,M.,Awan,I.,Grønli,T.M.,Eds.;SpringerNature:Cham,Switzerland,2023;pp.55–67. [CrossRef]
2. Just-in-TimeAdaptiveInterventions(JITAIs)inMobileHealth: KeyComponentsandDesignPrinciplesforOngoingHealth
BehaviorSupport|AnnalsofBehavioralMedicine|OxfordAcademic. Availableonline:https://academic.oup.com/abm/article/
52/6/446/4733473(accessedon26June2024).
3. Kumar,S.;Tiwari,P.;Zymbler,M. InternetofThingsisarevolutionaryapproachforfuturetechnologyenhancement:Areview.
J.BigData2019,6,111. [CrossRef]
4. WhatIsanIoTGatewayandHowDoIKeepItSecure? Availableonline:https://www.globalsign.com/en/blog/what-is-an-iot-
gateway-device(accessedon15May2023).

Sensors2024,24,4614 21of22
5. InternetofThingsinHealthcareMarketSizeReport.2030. Availableonline:https://www.grandviewresearch.com/industry-
analysis/internet-of-things-iot-healthcare-market(accessedon15May2023).
6. BiranAchituv,D.;Haiman,L. Physicians’attitudestowardtheuseofIoTmedicaldevicesaspartoftheirpractice. OnlineJ.Appl.
Knowl.Manag.(OJAKM)2016,4,128–145. [CrossRef]
7. Alshehri,F.;Muhammad,G. AComprehensiveSurveyoftheInternetofThings(IoT)andAI-BasedSmartHealthcare. IEEE
Access2021,9,3660–3678. [CrossRef]
8. Islam,S.M.R.;Kwak,D.;Kabir,M.H.;Hossain,M.;Kwak,K.S. TheInternetofThingsforHealthCare:AComprehensiveSurvey.
IEEEAccess2015,3,678–708. [CrossRef]
9. Ranjan,Y.;Rashid,Z.;Stewart,C.;Conde,P.;Begale,M.;Verbeeck,D.;Boettcher,S.;Hyve,T.;Dobson,R.;Folarin,A.;etal.
RADAR-Base:OpenSourceMobileHealthPlatformforCollecting,Monitoring,andAnalyzingDataUsingSensors,Wearables,
andMobileDevices. JMIRmHealthuHealth2019,7,e11734. [CrossRef][PubMed]
10. DallaCosta,G.;Leocani,L.;Montalban,X.;Guerrero,A.I.;Sørensen,P.S.;Magyari,M.;Dobson,R.J.B.;Cummins,N.;Narayan,
V.A.;Hotopf,M.;etal. Real-timeassessmentofCOVID-19prevalenceamongmultiplesclerosispatients:AmulticenterEuropean
study. Neurol.Sci.2020,41,1647–1650. [CrossRef][PubMed]
11. Sun,S.;Folarin,A.A.;Ranjan,Y.;Rashid,Z.;Conde,P.;Stewart,C.;Cummins,N.;Matcham,F.;Costa,G.D.;Simblett,S.;etal.
UsingSmartphonesandWearableDevicestoMonitorBehavioralChangesduringCOVID-19. J.Med.InternetRes.2020,22,e19992.
[CrossRef][PubMed]
12. Stewart,C.;Ranjan,Y.;Conde,P.;Rashid,Z.;Sankesara,H.;Bai,X.;Dobson,R.J.B.;Folarin,A.A. InvestigatingtheUseofDigital
HealthTechnologytoMonitorCOVID-19andItsEffects:ProtocolforanObservationalStudy(CovidCollabStudy). JMIRRes.
Protoc.2021,10,e32587. [CrossRef]
13. Ranjan,Y.;Althobiani,M.;Jacob,J.;Orini,M.;Dobson,R.J.;Porter,J.;Hurst,J.;Folarin,A.A. RemoteAssessmentofLungDisease
andImpactonPhysicalandMentalHealth(RALPMH):ProtocolforaProspectiveObservationalStudy. JMIRRes.Protoc.2021,
10,e28873. [CrossRef][PubMed]
14. CaseStudies. Availableonline:https://radar-base.org/case-studies/(accessedon15May2023).
15. Ranjan,Y.;Sankesara,H.;Conde,P.;Chang,J.;Rashid,Z.;Dobson,R.J.;AFolarin,A.RADAR-IoT:AnOpen-Source,Interoperable
andExtensibleIoTGatewayFrameworkforHealthcareandBeyond. InAdjunctProceedingsofthe2022ACMInternationalJoint
ConferenceonPervasiveandUbiquitousComputingandthe2022ACMInternationalSymposiumonWearableComputers;Associationfor
ComputingMachinery:NewYork,NY,USA,2023;UbiComp/ISWC’22Adjunct;pp.102–104. [CrossRef]
16. IoTMedicalDeviceGateway—RemotePatientMonitoring|Lantronix. Availableonline:https://www.lantronix.com/solutions/
healthcare/(accessedon15May2023).
17. Kesavan,S.;Kalambettu,G.K. IOTenabledcomprehensive,plugandplaygatewayframeworkforsmarthealth. InProceedings
ofthe2018SecondInternationalConferenceonAdvancesinElectronics,ComputersandCommunications(ICAECC),Bangalore,
India,9–10February2018;pp.1–5. [CrossRef]
18. IoTEdgeFramework. Availableonline:https://esf.eurotech.com/docs/edge-computing-platform(accessedon24November2022).
19. EclipseKura™Documentation. Availableonline:http://eclipse.github.io/kura/docs-release-5.2/(accessedon24November2022).
20. Lee,Y.H.;Nair,S. ASmartGatewayFrameworkforIOTServices. InProceedingsofthe2016IEEEInternationalConferenceon
InternetofThings(iThings)andIEEEGreenComputingandCommunications(GreenCom)andIEEECyber,PhysicalandSocial
Computing(CPSCom)andIEEESmartData(SmartData),Chengdu,China,15–18December2016;pp.107–114. [CrossRef]
21. ubiworxIoTGatewaySoftwareFramework. Availableonline:https://ubiworx.com/legal/2-general/34-ubiworx-iot-gateway-
software-framework(accessedon25November2022).
22. Adesina,T.;Osasona,O. ANovelCognitiveIoTGatewayFramework:TowardsaHolisticApproachtoIoTInteroperability. In
Proceedingsofthe2019IEEE5thWorldForumonInternetofThings(WF-IoT),Limerick,Ireland,15–18April2019. [CrossRef]
23. DeviceHiveOverview. Availableonline:https://docs.devicehive.com/docs(accessedon25November2022).
24. ThingSpeakDocumentation—MathWorksUnitedKingdom. Availableonline:https://uk.mathworks.com/help/thingspeak/
index.html?s_tid=CRUX_lftnav(accessedon25November2022).
25. ThingerOverview. Availableonline:https://docs.thinger.io/(accessedon25November2022).
26. HomeZettajs/ZettaWiki. Availableonline:https://github.com/zettajs/zetta(accessedon25November2022).
27. OpenRemote|The100%OpenSourceIoTPlatform. Availableonline:https://www.openremote.io/(accessedon25November2022).
28. ThingsBoardIoTGateway. Availableonline:https://github.com/thingsboard/thingsboard-gateway(accessedon25November2022).
29. Razzaque,M.A.;Milojevic-Jevric,M.;Palade,A.;Clarke,S. MiddlewareforInternetofThings:ASurvey. IEEEInternetThingsJ.
2016,3,70–95. [CrossRef]
30. Publish–Subscribe Pattern. Available online: https://en.wikipedia.org/w/index.php?title=Publish%E2%80%93subscribe_
pattern&oldid=1141729418(accessedon15May2023).
31. Ltd,RaspberryPi BuyaRaspberryPiZero. Availableonline: https://www.raspberrypi.com/products/raspberry-pi-zero/
(accessedon15May2023).
32. Liang,S.;Huang,C.Y.;Khalafbeigi,T. OGCSensorThingsAPIPart1:Sensing. Availableonline:https://docs.opengeospatial.
org/is/15-078r6/15-078r6.html(accessedon15May2023).
33. InfluxDBTimeSeriesPlatform. Availableonline:https://www.influxdata.com/products/influxdb/(accessedon15May2023).
34. grafana/grafana. Availableonline:https://github.com/grafana/grafana(accessedon15May2023).

Sensors2024,24,4614 22of22
35. Redis. Availableonline:https://redis.io/(accessedon15May2023).
36. MQTT—TheStandardforIoTMessaging. Availableonline:https://mqtt.org/(accessedon15May2023).
37. Node-RED. Availableonline:https://github.com/node-red/node-red(accessedon15May2023).
38. ApacheKafka. Availableonline:https://kafka.apache.org/(accessedon15May2023).
39. Gu,Z.;Wang,Y.;Shi,W.;Tian,Z.;Ren,K.;Lau,F.C.M. APracticalNeighborDiscoveryFrameworkforWirelessSensorNetworks.
Sensors2019,19,1887. [CrossRef][PubMed]
40. Object-OrientedProgramming. Availableonline:https://en.wikipedia.org/w/index.php?title=Object-oriented_programming&
oldid=1154120068(accessedon15May2023).
41. GrovePiPlus|SeeedStudioWiki. Availableonline:https://wiki.seeedstudio.com/GrovePi_Plus/(accessedon15May2023).
42. OAuth2.0—OAuth. Availableonline:https://oauth.net/2/(accessedon15May2023).
43. AvroDocumentation. Availableonline:https://avro.apache.org/docs/(accessedon15May2023).
44. SchemaRegistry. Availableonline:https://github.com/confluentinc/schema-registry(accessedon15May2023).
45. tinyML. Availableonline:https://www.tinyml.org/(accessedon26June2024).
46. node-red-contrib-datakitjs. Availableonline:http://flows.nodered.org/node/node-red-contrib-datakitjs(accessedon26June2024).
47. node-red-contrib-machine-learning. Availableonline: http://flows.nodered.org/node/node-red-contrib-machine-learning
(accessedon26June2024).
48. Node-RED ML Flows (Collection)—Node-RED. Available online: https://flows.nodered.org/collection/nRKXqYoATZfZ
(accessedon26June2024).
49. AnamolyDetectionUsingNode-Red-Contrib-Industrial-Machine-Forecast(Flow)—Node-RED. Availableonline:https://flows.
nodered.org/flow/05bb091acda87d6b5803e54c122837bb(accessedon26June2024).
50. NebulaDockerOrchestratorforIoT&DistributedSystems. Availableonline:https://nebula-orchestrator.github.io/(accessed
on15May2023).
51. Dataplicity. Availableonline:https://www.dataplicity.com/(accessedon15May2023).
52. netdata/netdata: Real-TimePerformanceMonitoring,DoneRight! Availableonline: https://github.com/netdata/netdata
(accessedon15May2023).
53. RADAR-IoT/Docker/ProductionatMasterRADAR-Base/RADAR-IoT. Availableonline:https://github.com/RADAR-base/
RADAR-IoT/tree/master/docker/production(accessedon9July2024).
54. ConfigurationsRADAR-Base/RADAR-IoTWikiGitHub. Availableonline:https://github.com/RADAR-base/RADAR-IoT/
wiki/Configurations(accessedon9July2024).
55. Spearman,C. TheProofandMeasurementofAssociationbetweenTwoThings. Am.J.Psychol.1904,15,72–101. [CrossRef]
56. Grove—AirQualitySensorv1.3|SeeedStudioWiki. Availableonline: https://wiki.seeedstudio.com/Grove-Air_Quality_
Sensor_v1.3/(accessedon15May2023).
57. Grove—Temperature&HumiditySensor(DHT11)|SeeedStudioWiki. Availableonline:https://wiki.seeedstudio.com/Grove-
TemperatureAndHumidity_Sensor/(accessedon15May2023).
58. Grove—PIRMotionSensor|SeeedStudioWiki. Availableonline:https://wiki.seeedstudio.com/Grove-PIR_Motion_Sensor/
(accessedon15May2023).
59. Grove—LightSensor|SeeedStudioWiki. Availableonline:https://wiki.seeedstudio.com/Grove-Light_Sensor/(accessedon15
May2023).
60. Braithwaite,I.;Zhang,S.;Kirkbride,J.B.;Osborn,D.P.J.;Hayes,J.F. AirPollution(ParticulateMatter)ExposureandAssociations
withDepression,Anxiety,Bipolar,PsychosisandSuicideRisk:ASystematicReviewandMeta-Analysis. Environ.HealthPerspect.
127,126002. [CrossRef][PubMed]
61. Ma,L.;Graham,D.J.;Stettler,M.E.J. HastheultralowemissionzoneinLondonimprovedairquality? Environ.Res.Lett.2021,
16,124001. [CrossRef]
62. London Air Quality Network: Welcome to the London Air Quality Network Statistics Maps. Available online: https://
www.londonair.org.uk/london/asp/reportdetail.asp?ReportID=2019laqnr&ReportType=LAQN_Annual_Report(accessedon21
August2023).
63. Stavropoulos,T.G.;Papastergiou,A.;Mpaltadoros,L.;Nikolopoulos,S.;Kompatsiaris,I. IoTWearableSensorsandDevicesin
ElderlyCare:ALiteratureReview. Sensors2020,20,2826. [CrossRef][PubMed]
64. Calvillo-Arbizu,J.;Román-Martínez,I.;Reina-Tosina,J. Internetofthingsinhealth:Requirements,issues,andgaps. Comput.
MethodsProgramsBiomed.2021,208,106231. [CrossRef][PubMed]
65. Ranjan,Y. RADAR-IoTProofofConcept(PoC).2023. Availableonline:https://ieee-dataport.org/documents/radar-iot-proof-
concept-poc(accessedon1July2024).
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.