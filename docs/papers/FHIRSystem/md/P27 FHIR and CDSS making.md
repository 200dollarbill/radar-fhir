International Journal of
Environmental Research
and Public Health
Article
Experience in Developing an FHIR Medical Data
Management Platform to Provide Clinical
Decision Support
IliaSemenov1,RomanOsenev1,SergeyGerasimov1,GeorgyKopanitsa2,*,DmitryDenisov1
andYuriyAndreychuk1
1 MedlinxLLC,Saint-Petersburg197101,Russia;ilia.semenov@medlinx.ru(I.S.);
roman.osenev@medlinx.ru(R.O.);sergey.gerasimov@medlinx.ru(S.G.);
dmitry.denisov@medlinx.ru(D.D.);yuriy.andreychuk@medlinx.ru(Y.A.)
2 NationalCenterforCognitiveResearch,ITMOUniversity,Saint-Petersburg197101,Russia
* Correspondence: kopanitsa.g@medlinx.com
(cid:1)(cid:2)(cid:3)(cid:1)(cid:4)(cid:5)(cid:6)(cid:7)(cid:8)(cid:1)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:6)(cid:7)
Received: 28August2019;Accepted: 10December2019;Published: 20December2019
Abstract: ThispaperisanextensionofworkoriginallypresentedtopHealth2019—16thInternational
Conference on Wearable, Micro and Nano Technologies for Personalized Health. To provide an
efficientdecisionsupport,itisnecessarytointegrateclinicaldecisionsupportsystems(CDSSs)in
informationsystemsroutinelyoperatedbyhealthcareprofessionals,suchashospitalinformation
systems (HISs), or by patients deploying their personal health records (PHR). CDSSs should be
abletousethesemanticsandtheclinicalcontextofthedataimportedfromothersystemsanddata
repositories. ACDSSplatformwasdevelopedasasetofseparatemicroservices. Inthiscontext,
we implemented the core components of a CDSS platform, namely its communication services
andlogicalinferencecomponents. Afasthealthcareinteroperabilityresources(FHIR)-basedCDSS
platformaddressestheeaseofaccesstoclinicaldecisionsupportservicesbyprovidingstandard-based
interfacesandworkflows. ThistypeofCDSSmaybeabletoimprovethequalityofcarefordoctors
who are using HIS without CDSS features. The HL7 FHIR interoperability standards provide a
platformusablebyallHISsthatareFHIRenabled. Theplatformhasbeenimplementedandisnow
productive,witharule-basedengineprocessingaround50,000transactionsadaywithmorethan
400decisionsupportmodelsandaBayesEngineprocessingaround2000transactionsadaywith
128Bayesiandiagnosticsmodels.
Keywords: semanticinteroperability;FHIR;clinicaldecisionsupport;integration
1. Introduction
This paper is an extension of work originally presented to pHealth 2019—16th International
ConferenceonWearable,Micro&NanotechnologiesforPersonalizedHealth[1].
Decision support systems (DSSs) are currently being implemented to solve a high variety of
clinicalandenvironmentaltasks. Successfulimplementationofadecisionsupportsystemrequires
efficientplanningstrategies,acommonunderstandingofdecisionssupportgoals,performance,and
usability. Thiscanincreaseacceptanceandmaketheoverallprojectsuccessful[2]. Thetasksthatcan
beefficientlysolvedbydecisionsupportsystemsvaryfromtheimplementationofurbanclimateaction
plans[3]andsupportofroadplanningtothediagnosisofrarediseases[4].
Healthcareindustryisincreasinglybecomingaknowledge-basedcommunity,connectingdifferent
providers,decreasingadministrativecosts,andimprovingqualityandcontinuityofcare. Thiscreates
challengesandopportunitiesforclinicaldecisionsupportsystems(CDSSs)thatfacilitatehealthcare
proceduresinknowledge-basedsettings[5]. ACDSSisanycomputerprogramdesignedtohelpmake
Int.J.Environ.Res.PublicHealth2020,17,73;doi:10.3390/ijerph17010073 www.mdpi.com/journal/ijerph

Int.J.Environ.Res.PublicHealth2020,17,73 2of18
clinical decisions [6,7]. This definition demonstrates the variety and evolution of clinical decision
supportfromsmall,focusedapplicationstolarge-scaleplatformscapableofstoringandmanaging
medicaldatatoassistdoctorsandpatientsbydeliveringrecommendations[8,9].
Toprovideefficientdecisionsupport,itisnecessarytointegrateCDSSsininformationsystems
routinely operated by healthcare professionals, such as hospital information systems (HIS), or by
patientsdeployingtheirpersonalhealthrecords(PHRs)[10]. CDSSsshouldbeabletousethesemantics
andtheclinicalcontextofthedatathatwereimportedfromothersystemsanddatarepositories[11–13].
Semantic interoperability becomes a key issue when it comes to communication between
heterogeneousinformationsystems[14]. Oneofthewaystoconnectdifferentinformationsystemsis
tobuildaplatformthatprocessesstandard-basedmedicaldataandprovidesunifiedinterfaces. Using
clinicaldataexchangestandardssuchasopenEHR[15],CEN/ISOEN13606[16–18],HL7CDA[19],
andfasthealthcareinteroperabilityresources(FHIR)[14]canprovidedata-levelinteroperability. These
standardsspecifycommonelectronichealthrecord(EHR)datastructures[20]andarewidelyusedin
clinicaldecisionsupportsystems[21,22]. OneofthelatestformatsofEHRdataspecificationsisthe
FHIRstandardthatprovidesdataelements(“resources”)andanapplicationprogramminginterface
(API)toretrieveandexchangeelectronichealthrecords[23].
The current medical software ecosystem can be characterized by its high innovation needs,
disturbinginteractionsbetweensystemsandhamperingsemanticinteroperability[24]. Toavoidsuch
problems,developerscanclustersoftwareapplicationsintosmall,easilysupportablefunctionalunits
thatcanbechangedondemandwithoutaffectingotherpiecesofsoftware. Thisapproachiscommonly
referredtoasmicroservicearchitecture[25].
Specifyingstandardinterfaces,CDSHooks(https://cds-hooks.org),providesahook-basedpattern
forautomaticallyinvokingCDSSfunctionswithinroutineclinicalworkflows[26]. Thisspecification
natively supports HL7 FHIR R4 to simplify the data flow, enabling easy integration of HISs and
CDSSservices.
TheexperienceshowsthatmostoftheCDSSsarestandaloneimplementationsfocusedonone
clinicalconditionorworkflow[27–29]. However,theimplementationofsophisticatedclinicaldecision
supportplatformsthatarecapableofprovidingafullspectrumofclinicaldecisionsupportfunctionality
tovariousmedicalinformationsystemsisstillmissing. Thereisapersistentneedforhigh-quality,
effectiveplatformsthatwillunifydesign,development,presentation,implementation,evaluation,and
maintenanceofalltypesofclinicaldecisionsupportcapabilitiesforclinicians,patients[30],andother
stakeholders[31]. WeadvanceexistingexperiencesinimplementingCDSplatforms[32]byadding
standard-baseddatainterfacesandstructurestodeliverdecisionsupportfeaturestodifferenthealth
careecosystems.
ThegoalofthisresearchistodevelopanFHIR-basedmicroserviceplatformthatintegratesHISs
andCDSSsintoaunifiedinformationspace.
2. Methods
2.1. PlatformArchitecture
Structurally, a CDSS platform was developed as a set of separate services, that is, nodes
distributedingroups. MicroservicescommunicatewitheachotherasynchronouslyusingtheREST
communicationprotocol.
2.2. Services
AlltheservicesoperatethroughpubliccontractsrepresentedinFHIRJSONformat,providing
theuniqueresourceidentifier(URI)oftheresources. Servicesutilizetwointeractionmodels: remote
procedurecall(RPC)andevent-basedinteraction. Logsaresenttothecentrallogservicewithaunique
transactionID.

Int.J.Environ.Res.PublicHealth2020,17,73 3of18
AmodeloftheservicesisshowninFigure1. BusinessAPIendpointsallowsendingservice-specific
requeIsntt.s J,. Efonvrireonx.a Rmes.p Plueb,lict oHeraeltthu 2r02n0,s 1p7,e xc ificartifactsorterminologyfromtheknowledgebase.3 of 18
The EventAPI endpoint (e.g., HTTP/event) allowsan external serviceto send eventrequests.
The Event API endpoint (e.g., HTTP /event) allows an external service to send event requests.
Sotheserviceknowsthestatusofotherservicesoftheplatform.
T
S
h
o
e
th
H
e
e
se
a
r
l
v
th
ice
C
k
h
n
e
o
c
w
k
s
A
t
P
he
I e
st
n
a
d
tu
p
s
o
o
i
f
n
o
t
t
(
h
e
e
.g
r
.
s
,
e
H
rv
T
ic
T
e
P
s /o
h
f
e
t
a
h
l
e
t h
p
)
la
r
t
e
fo
tu
rm
rn
.
sthehealthstatusoftheservicetoits
The Health Check API endpoint (e.g., HTTP /health) returns the health status of the service to
handlertoprovidecontinualmonitoring. TheAPIendpointhandlerperformsvariouschecks,suchas
its handler to provide continual monitoring. The API endpoint handler performs various checks, such
• t a h s e statusoftheconnectionstotheinfrastructureservicesusedbytheserviceinstance;
• t • h esttahteu sstaotufsth oef thhoes cto,nfonrecetxioanms ptole t,hde iisnkfrsapstarcuec;ture services used by the service instance;
• a • p pli t c h a e t i s o ta n t - u s s p o e f c t i h fi e c h lo o g st i , c f . or example, disk space;
• application-specific logic.
BusinessLBougsiicneissst hLeomgica iins tphaer tmoafinth peasret rovfi ctheet hseartvisicree tshpaot niss irbelsepfoonrstihblee ifmorp tlheem iemnptaletmioennotafttihone foefa tthuer ethe
servicfeeaitsudree stihgen seedrvfiocre, fiso rdeesxiagmnepdl ef,otrh, efolro egxiacmofplloe,a tdhien glofgaicc tosff rlooamditnhge fdacattsa fbraosme itnhteo daantaibnafseer einntcoe aenn gine.
EinvfeenretnScteo ernegainned. BusinessLogicStoreareresponsibleformanagingandsavingdatarelatedtothe
corresponEdvienngt pStroorcee sasndo fBtuhseinseesrsv Licoeg.ic Store are responsible for managing and saving data related to
the corresponding process of the service.
OtherServiceClientisresponsibleforactivecommunicationwithotherservicesoftheplatform,
Other Service Client is responsible for active communication with other services of the platform,
forexample,sendingtheeventsandtheresultsofthework.
for example, sending the events and the results of the work.
FigurFeig1u.rGe 1e.n Gereanlermalo mdeoldoelf osfe srevrivcieceo offt htheep pllaattffoorrmm.. AAPPI:I :apapplpiclaictaiotnio pnropgrroagmramminmg iinngterifnatceer.f ace.
EachEsaecrhv siceervhicaes haans ainn dinedpeepnednednetntr erleeleaassee ccyyccllee,, ssoo tthhee ppuubblilci cinitnertefarcfeasc essupspuoprpt ovretrsvioenrisniog ntion g to
provide consistent operation of the system.
provideconsistentoperationofthesystem.
2.3. Clinical Modelling
2.3. ClinicalModelling
The CDSS platform requires designing a set of FHIR profiles suitable for the decision support.
TheCDSSplatformrequiresdesigningasetofFHIRprofilessuitableforthedecisionsupport. We
We used Forge (https://fhir.furore.com/forge/), the official HL7®FHIR® profile editor, a desktop
usedForge(https://fhir.furore.com/forge/),theofficialHL7 ® FHIR ® profileeditor,adesktopapplication
application for profile modelling and validation. We used Logical Observation Identifiers Names and
for prCoofidlees m(LoOdINelCli)n [g33a]n adndv aSlyisdteamtioatniz.eWd NeoumseedncLlaotugriec aolf OMbesdeicrivnaet—ioCnliIndiceanl tTifieremrss N(SaNmOeMsEaDn dCTC) odes
(LOIN[3C4]) c[o3d3]esa ntod dSeyfisntee mthae tsiezmedanNtiocsm oefn thclea mtuerdeicoafl Mcoendceicpitnse. —ClinicalTerms(SNOMEDCT)[34]codes
todefinetAh e“Psaetmienant”t iwcsaso ufstehde ams tehdei mcaalinco rnescoeuprtcse. of the platform. To provide semantic interoperability,
Athe“ Ppalattifeonrtm” swuapspuorstesd thaes ftohlleowmianign FrHesIRo uRr4c e[3o5f] rtheseopurlacetfso arsm in.pTuot panrodv oiudtepuset mdaatna:t icinteroperability,
thepl1a. tfoCrmaresPulpanp ortsthefollowingFHIRR4[35]resourcesasinputandoutputdata:
2. MedicationRequest
1. CarePlan
3. ActivityDefinition
2.
4
M
.
ed
D
ic
e
a
t
t
e
i
c
o
t
n
ed
R
I
e
ss
q
u
u
e
e st
3. 5A. ctivRiitsykDAsesfienssitmioennt

Int.J.Environ.Res.PublicHealth2020,17,73 4of18
4. DetectedIssue
5. RiskAssessment
6. Questionnaire
7. QuestionnaireResponse
8. ResearchDefinition
9. PlanDefinition
10. Goal
11. Observation
12. Condition
13. FamilyMemberHistory
14. DiagnosticReport
15. Group
16. RequestGroup
17. AllergyIntolerance
18. Immunization
19. Procedure
20. Encounter
21. Appointment
2.4. RuleEngine
Weaccomplishedextractionandconceptualizationoftheinferencerulesbymanualformalization
ofclinicalguidelines. Weidentifiedthreetypesofinferencerules: thedefinition,operationrule,and
aggregationrule:
Definitionisanatomicdomainconceptconsistingofanomenclatureandacode.
OperationRule(OP)isanoperationalinferencerulethatdealswithaDefinitionthatdetermines
referenceintervalsforaDefinition. Forexample,
• Definition_1. Value>1. Definition_2. Value=0
• OperationRulehasthefollowingstructure:
DefinitionID
(cid:35) Nomenclature
(cid:35) Code
(cid:35) Name
(cid:35) Operation
(cid:35) Value
(cid:35)
AggregateRuleisanAggregationRule(AG)thatperformslogicaloperationsonOperationRules.
AggregationRulesarebuiltupontheIF-THENparadigm,withtheconditionalcombinationofcriteria
(OPs)intheIFpartandthesuggestedArtifactsintheTHENpart. Forexample: if(Op1andop2)or
(op3andop4)thenArtifact.
AnArtifactisapieceofafree-textrecommendationthatshallbeincludedinthereportasthe
resultofthedecisionsupport. Thesystemsupportsthefollowingtypesofartifacts:
• Scaleisusedfortheresultsofevaluationscales,questionnaires(asacodedvalueoftheresultor
asanumber);
• Riskisusedtodetermineifthereisariskofanydiseaseorcondition;
• Diagnosisisusedtoevaluatethepossiblediagnosisbasedonlaboratoryorinstrumentalstudies;
• DiagnosticReportisusedforcodedlogicgroupstointerpretclinicalobservations;

Int.J.Environ.Res.PublicHealth2020,17,73 5of18
• ReferralRequestisusedtorecommendspecialistappointmentandroutingofpatients;
• ProcedureRequestisusedtorecommendinstrumentalexaminations;
• DiagnosticRequestisusedtorecommendlaboratorytests;
• Descriptionisusedtodescribetheconclusionsdrawn(e.g.,anexplanationoftheidentifiedrisk
level);
• Recommendationisusedforfreetextrecommendations;
• BehaviorRecommendationisusedforcodedlifestylerecommendations.
WhenaspecificFHIRinstanceofapatient’scasereachesadecisionsupportsystem,patientdata
isfirstcheckedtomatchtheformaldefinitionofFHIR.Then,thedatainstancesareregisteredinthe
factdatabase. Later,theyareanalyzedfortheexistenceofaconceptofaDefinitionobjectforevery
fact. TheconceptsthathavecorrespondingDefinitionsareusedforlogicalinference,whereengine
servicescreateaninferencesequencetogenerateaJSONfilewithartifactstobeincludedinthereport.
Theresultingservicecreatesahuman-readabledocumentbasedontheinference.
Dependingontheinputdata,theRuleEnginecanbeusedfordifferentpurposes:
• Calculationofrisksofdisease;
• Interpretationandmonitoringofclinicalobservations;
• Analysis of medical services provided to a patient for compliance with the standards of the
insurancecompany;
• Treatmentplanmanagement;
• Analysisofprescriptionsfordruginteractionsandcontraindicationsforprescribing.
TheRuleEngineincludestheservicespresentedinFigure2.
• FHIR Adapter: the service converts data from the FHIR format into the internal Rule Engine
format. ThisservicealsoprovidesthepossibilityofRuleEngineinvocationaccordingtotheCDS
Hooksspecification.
• RuleAPI:theserviceperformsinternalroutingandsavesprocesseddataforfurtheranalysis.
• Filter: theserviceisresponsibleforfilteringthedatatotheactualstate,applicabletothemechanism
oflogicaloutput.
• RuleEngine: theserviceisresponsibleforthelogicalinferencemechanismbasedontherules.
• Formatter: theserviceisresponsibleforformattingtheresultsoflogicalinference.
• Api.KnowledgeService: the knowledge service is responsible for CRUD operations with the
graphicalknowledgebase. IsusedbytheRuleEnginetosearchforrules,artifacts,anddefinitions.
• Api.FactService: fact service is responsible for preserving and providing facts at all stages
ofinference.
• Api.JobStatusService: thestatusserviceisresponsibleforcreatingnewtasksandsavingstatuses.
• Api.ErrorService: theerrorserviceisresponsibleforsavingandreportingerrorsthatoccurduring
theinferenceprocess.
• Api.ResultService: theresultserviceisresponsibleforsavingandprovidingtheresultsobtained
bytheRuleEngineinference.
• TerminologyServiceisresponsibleforthestorageandprovisionofmedicalterminology.

Int.J.Environ.Res.PublicHealth2020,17,73 6of18
Int. J. Environ. Res. Public Health 2020, 17, x 6 of 18
Int. J. Environ. Res. Public Health 2020, 17, x 6 of 18
FFiigguurree 22.. SSeerrvviicceess ooff tthhee RRuullee EEnnggiinnee.. FFHHIIRR:: ffaasstt hheeaalltthhccaarree iinntteerrooppeerraabbiilliittyy rreessoouurrcceess..
Figure 2. Services of the Rule Engine. FHIR: fast healthcare interoperability resources.
TThhee RRuullee EEnngginineei sisb absaesdedo nonp rpordoudcuticotniornu lreusleths atthaarte aloreg ilcoagliecxapl reexspsiroensssiroenpsr erseepnrteesdenintetdh einfo trhme
The Rule Engine is based on production rules that are logical expressions represented in the
fooframg roafp ah .grAanphe.x aAmnp elxeaomfaplger aopf ha mgroadpehl omforudleels offo rrualsesse sfsoirn gastsheessriinskg othfety rpisek2 odfi atybpetee s2 idsisahboewtens iins
form of a graph. An example of a graph model of rules for assessing the risk of type 2 diabetes is
sFhigouwrne 3in. Figure 3.
shown in Figure 3.
Figure3. Exampleofagraphicalmodelofrulesforassessingtheriskoftype2diabetes.
Figure 3. Example of a graphical model of rules for assessing the risk of type 2 diabetes.
Figure 3. Example of a graphical model of rules for assessing the risk of type 2 diabetes.

Int.J.Environ.Res.PublicHealth2020,17,73 7of18
Int. J. Environ. Res. Public Health 2020, 17, x 7 of 18
Int. J. Environ. Res. Public Health 2020, 17, x 7 of 18
Int. J. Environ. Res. Public Health 2020, 17, x 7 of 18
RuleEditor
Rule Editor
Rule Editor
Rule Editor
Theruleeditorhasanintuitiveinterfacethatallowscreatinglogicalexpressions(Figures4–6).
The rule editor has an intuitive interface that allows creating logical expressions (Figures 4–6).
The rule editor has an intuitive interface that allows creating logical expressions (Figures 4–6).
TChoen rduitleio endsitionrl ohgasic aanl einxpturietsivsieo innsteinrfcalcued tehcaot malploawriss ocrneoatfinacgt uloaglivcaall ueexsprweistshiotnhse (rFeifgeurerensc e4s–6a)n. d
Conditions in logical expressions include comparison of actual values with the references and
Conditions in logical expressions include comparison of actual values with the references and
absoCluotendviatliuoness (iFni glougreic4a)l .expressions include comparison of actual values with the references and
absolute values (Figure 4).
absolute values (Figure 4).
absolute values (Figure 4).
FiguFF riige g uu 4r. r ee C 44 D.. SCC SDD (Sc S lSS in ((ci c cllia inn l ii dccae alc l idd sei e occ niiss is ioo unn p sp suu opp rtpp soo yrr stt t ss eyy msst) tee rmm u)l ) e rr suu elled ess it ee odd ri. i ttoorr..
Figure 4. CDSS (clinical decision support system) rules editor.
ConCdointidointiso anrsea croemcobminbeidn eindtoin rtuolreus lbeys bloygliocgali coapleorpaetiroantiso nAsNADN, DO,RO, NR,ONTO (TFig(Fuirgeu 5re) 5).
Conditions are combined into rules by logical operations AND, OR, NOT (Figure 5)
Conditions are combined into rules by logical operations AND, OR, NOT (Figure 5)
Figure 5. Rules combination.
FFiigguurree 55.. RRuulleess ccoommbbiinnaattiioonn..
Figure 5. Rules combination.
Conclusions of the rules are provided as Artifact type and contain additional information about
CCoonncclluussiioonnss ooff tthhee rruulleess aarree pprroovviiddeedd aass AArrttiiffaacctt ttyyppee aanndd ccoonnttaaiinn aaddddiittiioonnaall iinnffoorrmmaattiioonn aabboouutt
Conclusions of the rules are provided as Artifact type and contain additional information about
the interpretation of laboratory analyses, recommendations for appointment, recommendations for
tthhee iinntteerrpprreettaattiioonn ooff llaabboorraattoorryy aannaallyysseess,, rreeccoommmmeennddaattiioonnss ffoorr aappppooiinnttmmeenntt,, rreeccoommmmeennddaattiioonnss ffoorr
the interpretation of laboratory analyses, recommendations for appointment, recommendations for
additional instrumental and laboratory studies, and so forth. (Figure 6).
aaddddiittiioonnaall iinnssttrruummeennttaall aanndd llaabboorraattoorryys sttuuddiieess,,a anndds soof foorrtthh.. ((FFiigguurree 66))..
additional instrumental and laboratory studies, and so forth. (Figure 6).
Figu
F
r
i
e
g u
6.
r e
F r
6
e
.
e
F
-t
r
e
e
x
e
t
- t
r
e
e
x
c
t
o
r
m
ec
m
om
en
m
da
en
ti
d
on
at
s
i
.
o ns.
FFiigguurree 66.. FFrreeee--tteexxtt rreeccoommmmeennddaattiioonnss..
2.5. Bayes Engine
2.5. Bayes Engine
2.5. Bayes Engine

Int.J.Environ.Res.PublicHealth2020,17,73 8of18
2.5. BayesEngine
ABayesEngineisaDSSsystembasedonBayesianLogic. BayesianStatisticsallowasystemto
makeconclusionsaboutthepresenceofpathologyinthepatientintheconditionsofhighuncertainty.
BayesEnginemodelsenabletocarryoutinitialpatientinterview,guidethepatienttotherightdoctor,
andtoassistthedoctorinmakingapreliminarydiagnosis. Modelsaredevelopedbyexpertphysicians
on the bInat.s Ji. sEnovifrogn.e Rnese. Pruablllicy Haeacltch e20p2t0e, 1d7, xc linical guidelines and scientific publications with8a ohf i1g8 h level
ofevidence.
A Bayes Engine is a DSS system based on Bayesian Logic. Bayesian Statistics allow a system to
BayesEngineserviceswereimplementedusing
make conclusions about the presence of pathology in the patient in the conditions of high uncertainty.
Bayes Engine models enable to carry out initial patient interview, guide the patient to the right doctor,
1. C#+.netcore2.2forthecorelogic;
and to assist the doctor in making a preliminary diagnosis. Models are developed by expert
2. aspp.hnyesticciaonrse o2n.2 t—hef obarstihs eofw geebneirnatlleyr faaccceep;ted clinical guidelines and scientific publications with a
3. Infheirg.hN lEevTel( Mof eLv.nideetn)c—e. aframeworkforrunningBayesianinferenceingraphicalmodels. Inour
Bayes Engine services were implemented using
caseitwasusedforprobabilisticprogramming.
4. Po1s.t greСS#Q + L.n1et1 cfoorer 2d.2a tfaors tthoer acogree. logic;
2. asp.net core 2.2—for the web interface;
Bay3e. sEInnfgeirn.NeEiTn c(MluLd.neestt)—hea fforallmoewwionrgk sfeorr vruicnensin(Fg iBgauyreesi7a)n: inference in graphical models. In our
case it was used for probabilistic programming.
• FH4I.R APdosatpgrteeSrQ: Lth 1e1 sfoerr vdiactae sctoornavgee.r tsdatafromtheFHIRformatintotheinternalBayesEngine
format.BFayuerst hEenrgminoe rien,cltuhdisess tehrev fioclelopwrionvgi sdeervsitchese (pFiogsusrieb 7il)i: tyofRuleEngineinvocationaccordingto
the•C DS
FH
H
IR
o o
A
k
d
s
a
s
p
p
te
e
r
c
:
i
t
fi
he
c a
s
t
e
i
r
o
v
n
ic
.
e converts data from the FHIR format into the internal Bayes Engine
• BayesAfoPrIm:atht. eFusertrhveircmeopree,r tfhoirsm sesrvinictee prnroavlirdoeus tthineg poasnsdibisltitoyr eosf Rpurloec Eenssgeinde dinavtoacfaotironfu arctchoerdrianng alysis;
• Interprteot athtieo CnDSS Herovokicse s:peciftihcaetionse. rvice performs data processing before calculation on
• Bayes API: the service performs internal routing and stores processed data for further analysis;
Bayesiannetworks;
• Interpretation Service: the service performs data processing before calculation on Bayesian
• KnowledgeService: theservicestoresBayesianmodelscreatedbyexpertsandcollectsprobabilities
networks;
use•d fo
K
r
n
c
o
a
w
lc
l
u
ed
la
g
t
e
i o
S
n
e
s
r
;
vice: the service stores Bayesian models created by experts and collects
• InferenpceroEbanbgiliintiee:s tuhseeds feorrv ciaclecuplaetrifoonrsm; sinferenceonthebasisofBayesianmodels;
• Qb • o t: thInefesreernvceic Eenvgainleid: tahtee sseirnvficeer epnercfeorrmessu inltfseraenncde mono tdhee lbsawsisi tohf Beaxypeesriatsn imnotdheelsl; earningmode;
• Qbot: the service validates inference results and models with experts in the learning mode;
• ModelManager: supportsmodelmanagementintheKnowledgeService(CRUDonmodels).
• Model Manager: supports model management in the Knowledge Service (CRUD on models).
FiguFirgeu7re. 7B.a ByaeysesE Ennggiinnee ccoommppoonennetn dtiadgiraagmra m

Int.J.Environ.Res.PublicHealth2020,17,73 9of18
Int. J. Environ. Res. Public Health 2020, 17, x 9 of 18
TheprocessofcreatingdiagnosticBayesianmodelsincludesthefollowingsteps:
The process of creating diagnostic Bayesian models includes the following steps:
1. Creatingamodelprototype;
12.. CMreoadtienlgs tar umctoudreel vparloidtoattyiopne;b yexperts;
23.. MImodperlo svtermucetnutreo fvtahliedmatoiodne lbsyt reuxcptuerrtes;;
34.. ImDepfironviteiomneonft porf otbhaeb miliotdieesl; structure;
45.. DVeafliindiatitoionn oof fptrhoebamboilditeilesb;y expertsusingrealvalidatedclinicalcases.
5. Validation of the model by experts using real validated clinical cases.
TheBayesiannetworkeditorisusedtocreatediagnosticmodels. Amodelisagraphwithnodes
The Bayesian network editor is used to create diagnostic models. A model is a graph with nodes
representingdiagnoses,riskfactors,symptoms,objectivesigns,aswellaslaboratoryandinstrumental
r
d
e
a
p
t
r
a
e
.
se
E
n
d
ti
g
n
e
g
s b
d
e
i
t
a
w
g
e
n
e
o
n
se
t
s
h
,
e
r
n
is
o
k
d es
fa
i
c
n
to
d
r
ic
s,
a te
sy
c
m
au
p
s
t
e
o
–
m effs,
e c
o
t
b
r
j
e
e
l
c
a
t
t
i
i
v
o
e
n s
s
h
i
i
g
p
n
s
s
a
,
n
a
d
s
co
w
rr
e
e
ll
l at
a
i
s
o n
l
s
a
.
b
A
or
ll
at
n
o
o
r
d
y
es
an
ar
d
e
instrumental data. Edges between the nodes indicate cause–effect relationships and correlations. All
codedusinginternationalclassifiers(LOINCandSNOMEDCT).
nodes are coded using international classifiers (LOINC and SNOMED CT).
2.6. CDSHooks
2.6. CDS Hooks
FortheintegrationoftheCDSHooksAPIintotheCDSSplatform,weutilizedthelatestversionof
thesFpoerc itfihcea itniotengoraftCioDnS oHf tohoek CsD(1S.0 HSoToUk)s. API into the CDSS platform, we utilized the latest version
of theT sopeencsifuicraetiinotne roofp CeDraSb iHlitoyo,kthse (1C.0D SSTMUa).n agerserviceisincludedintheCDSSplatformtoperform
thefTooll oewnisnugreta sinktse:roperability, the CDS Manager service is included in the CDSS platform to
perform the following tasks:
1. StoreadirectoryofavailableCDSSservicesontheplatform,provideregistration,andallowthe
1. Store a directory of available CDSS services on the platform, provide registration, and allow the
clientapplicationtoconfigurewhichCDSStouseforspecificneeds.
client application to configure which CDSS to use for specific needs.
2. ProvideproxyingcallsfromtheclienttotheselectedCDSSandcollectusagestatistics.
2. Provide proxying calls from the client to the selected CDSS and collect usage statistics.
TThhee pprroocceessss aanndd ccoommppoonneennttss ooff iinntteerraaccttiioonn bbeettwweeeenn HHIISSss aanndd tthhee CCDDSS mmaannaaggeerr aarree sshhoowwnn iinn
FFiigguurreess 88,9a.n d9.
Figure8. CDSHookinteractionworkflow. HIS:hospitalinformationsystem.
Figure 8. CDS Hook interaction workflow. HIS: hospital information system.
TheCDSmanagerallowsconnectionsfromanyCDSSservicesthatimplementtheCDSHooks
The CDS manager allows connections from any CDSS services that implement the CDS Hooks
1.0specification.
1.0 specification.

Int.J.Environ.Res.PublicHealth2020,17,73 10of18
Int. J. Environ. Res. Public Health 2020, 17, x 10 of 18
Figure9. CDSmanagerstructuremodel. EHR:electronichealthrecord.
Figure 9. CDS manager structure model. EHR: electronic health record.
ToimplementtheCDSHooks,weconsequentlyimplementedthreemainfeatures:
To implement the CDS Hooks, we consequently implemented three main features:
1. RESTfulinterfacebasedontheCDSHooksspecification. Thisincludedsupportofthedefined
1. RESTful interface based on the CDS Hooks specification. This included support of the defined
formatoftheRESTfulbodyandthereturnoftheCDSresultsascards;
format of the RESTful body and the return of the CDS results as cards;
2
2
.
.
A
A
F
F
H
H
IR
IR
p
p
la
l
t
a
f
t
o
f
r
o
m
rm
ad
a
a
d
p
a
t
p
o
t
r
o
w
r
a
w
s
a
a
s
d
a
ju
d
s
j
t
u
e
s
d
t e
t
d
o s
to
up
s
p
u
o
p
r
p
t
o
in
rt
di
i
v
n
i
d
d
i
u
v
a
id
l
u
FH
al
IR
F H
co
IR
nn
c
e
o
c
n
ti
n
o
e
n
c
f
t
o
io
r
n
ea
fo
ch
r
E
ea
H
c
R
h
EHRsession;
session;
33.. IImmpplleemmeennttaattiioonn oofft htehdea tdaaptao inptosirnetqsu irreeqdubiyretdh ebCyD SthHe ooCkDsSA PHI.oTohkiss iAncPluI.d eTdhitsh eimncalunadgeedm tehnet
mofahnoaogkemsaenndt othf ehodoaktas paonidn ttsheth daattnae peodiendtst othbaet pneree-dfeetdc htoe dbeb yprteh-efectaclhliendg bHyI tSh.e calling HIS.
3. Results
3. Results
3.1. RuleEngine
3.1. Rule Engine
A Rule Engine is an inference system based on production rules. It receives patient-related
A Rule Engine is an inference system based on production rules. It receives patient-related
observationsasaninputandreturnsconclusionsaboutthepatient’sconditionwithrecommendations
observations as an input and returns conclusions about the patient’s condition with
forfurtheractions. Therulesthatareincorporatedintothesystemarereferencedbyclinicalguidelines
recommendations for further actions. The rules that are incorporated into the system are referenced
andscientificpublicationswithahighlevelofevidence.
by clinical guidelines and scientific publications with a high level of evidence.
Intotal,wehavemodelled365nodesoflaboratorytestcomponents,5084nodesofinferencerules,
In total, we have modelled 365 nodes of laboratory test components, 5084 nodes of inference
49,932nodes,and3072blocksoftextformedicalcertificates.
rules, 49,932 nodes, and 3072 blocks of text for medical certificates.
We have developed interpretation algorithms for the following 11 groups of codes of the
We have developed interpretation algorithms for the following 11 groups of codes of the
InternationalStatisticalClassificationofDiseasesandRelatedHealthProblems(ICD-10):
International Statistical Classification of Diseases and Related Health Problems (ICD-10):
N30Cystitis
N30 Cystitis
N04Nephroticsyndrome
N04 Nephrotic syndrome
N10Acutepyelonephritis
N10 Acute pyelonephritis
K75Otherinflammatoryliverdiseases
K75 Other inflammatory liver diseases
K71Toxicliverdisease
K71 Toxic liver disease
K81Cholecystitis
K81 Cholecystitis
K85Acutepancreatitis
K85 Acute pancreatitis
E05Thyrotoxicosis
E05 Thyrotoxicosis
D50Irondeficiencyanemia
D50 Iron deficiency anemia
D72 Other disorders of white blood cells

Int.J.Environ.Res.PublicHealth2020,17,73 11of18
Int. J. Environ. Res. Public Health 2020, 17, x 11 of 18
D72Otherdisordersofwhitebloodcells
N41Inflammatorydiseasesofprostate.
N41 Inflammatory diseases of prostate
3.2.InBt.a Jy. eEsnvEirnong. iRnees. Public Health 2020, 17, x 11 of 18
3.2. Bayes Engine
AnNex41a mInpfllaemomfamtoordye dlissetrausecst uorfe pirsosptraetes entedinFigure10.
An example of model structure is presented in Figure 10.
3.2. Bayes Engine
An example of model structure is presented in Figure 10.
Figure 10. Example of the structure of a probabilistic model.
Fi F g ig u u re re 1 1 0 0 . . EExxaammpplele oof fththe estsrutrcutuctrue roef oa fparopbraobbilaisbtiicli smtiocdmel.o del.
For each node, experts specify disease-specific stratification. To determine the probability values,
ForFeoarc ehacnho ndoed,ee, xepxperetrstss sppeecciiffyy ddiisseeaassee--ssppeecicfiific cstsratrtiafticifiatciaotni.o Tno. dTeotedremteinrem tihnee ptrhoebapbriolibtya bvialliutyesv, alues,
experts use statistical data from clinical guidelines and standards. An example of probability tables
expeexrptserutss eusseta sttiasttiisctaicladl dataataf rfroomm cclliinniiccaall gguuidideelilninese sanadn dstasntadnarddasr. dAsn. Aexnamexpalem opf lperoobfapbriolibtya btaiblilteys tables
is shown in Figure 11. Each model is validated by at least two experts before it can be accepted for
isshiso swhonwinn Fini gFuigruer1e 11.1.E Eaacchh mmooddeell iiss vvaalildidaatetde dbyb yat altealseta tswtotw exopeexrtpse bretfsobree fiot rceani tbcea anccbeeptaecdc efoprt edfor
pro p d r u od cpt urioo cdt n iu. o cA nti.o m An.o Am d e oml d oi e sdl ea ilc s icsa e cap cctce eep dpt te oeddn l ooy nn a llyy ft ae afr ftt ea er r caa o cn cos one nsnesns e usnus ss u b bs eet btwwe e tew eenne ettww not o we exo xpp eere xtr pst e sisr i trs se rai e scahr cee hda e.c d h . e d .
Figure11. ExampleofprobabilitytablesforGastroesophagealrefluxdisease.
Figure 11. Example of probability tables for Gastroesophageal reflux disease.
WehaveimplementedBayesiandiagnosticsmodelsfor128diagnoses.
We haFvigeu imrep 1l1e.m Eexnatmedp lBea oyfe psiraonb adbiailgitnyo tsatibclse sm foodr eGlsa sftorro 1e2so8 pdhiaaggneaols eres.f lux disease.
We have implemented Bayesian diagnostics models for 128 diagnoses.

Int.J.Environ.Res.PublicHealth2020,17,73 12of18
Int. J. Environ. Res. Public Health 2020, 17, x 12 of 18
BBaayyeess EEnnggiinnee WWoorrkkflflooww EExxaammppllee
TThhee eexxaammppllee bbeellooww sshhoowwss tthhee BBaayyeessiiaann ccaallccuullaattiioonnss ffoorr tthhee ddiiaaggnnoossttiiccss ooff rreessppiirraattoorryy ddiisseeaasseess..
FFiigguurreess 112–21–616d edmeomnosntrsattreatthe etphreo cpersoscoefshso wof thheoBwa ytehseia nBaeynegsiniaenc aelncugliantee scparlocbualabtielist iepsroofbpanbeiluitmieos noiaf
apnndeuamcuotneiare aspnidr aatcouryted riessepaisreataoftreyr dreisceeaivsein agftneer wrescyemivpintgo mnse.wT hsyemfipgtuormess.d Teshcer ifbieguforerse adcehscsrtiebpe tfhoer
reeaccahlc ustleapti otnheo frpercoablcaublialittiioens ooffP nperuombaobniliiatiaens doAf cPunteeuremspoinriaat oaryndd isAecausetew rheesnpiirnattroordyu cdinisgeanseew wfahcetsn:
pinrtersoednucecionfgc nheilwl, rfiagchtst:- spidreesdencchee sotf pcahiinll,, arnigdhct-osliodreodf cahsepstu ptuamin., and color of a sputum.
Figure12. InitialstateofaBayesiannetwork.
Figure 12. Initial state of a Bayesian network.

Int.J.Environ.Res.PublicHealth2020,17,73 13of18
InInt.t .J .J .E Ennvvirioronn. .R Rese.s .P Puubblilci cH Heaealtlhth 2 2002200, ,1 177, ,x x 1133 oof f 1188
FFFiiggiguuurrreee 11 1333.. .PP Prrrooobbbaaabbbiilliiilttiyyty tt aatabbblleele ff ooforrr aa a cc chhhiillilll lss syyymmmpppttootommm.. .
Figure14. Servicehasreceiveddataonthepresenceofchill.
FFigiguurree 1 144. .S Seerrvvicicee h haass r reecceeiviveedd d daatata o onn t hthee p prreesseennccee o of fc chhilill.l .

Int. J. Environ. Res. Public Health 2020, 17, x 14 of 18
Int.J.Environ.Res.PublicHealth2020,17,73 14of18
Int. J. Environ. Res. Public Health 2020, 17, x 14 of 18
FFiigguurree 1155.. SSeerrvviiccee hhaass rreecceeiivveedd ddaattaa tthhaatt tthhee ppaattiieenntt hhaass aa cchheesstt ppaaiinn oonn tthhee rriigghhtt ssiiddee dduurriinngg ccoouugghh..
Figure 15. Service has received data that the patient has a chest pain on the right side during cough.
F F i i g g u u r r e e 1 1 6 6 . . SSeerrvviiccee hhaass rreecceeiivveedd ddaattaa tthhaatt tthhee ppaattiieenntt hhaass rruussttyy ssppuuttuumm ccoommiinngg oo ff ff..
4. DiscussionFigure 16. Service has received data that the patient has rusty sputum coming off.
4. Discussion
4. DIinsctuhsissipoanp er,wefocusedonthedevelopmentofthecorecomponentsofaCDSSplatform,thatis,
In this paper, we focused on the development of the core components of a CDSS platform, that
itscommunicationservicesandlogicalinferencecomponents. Themostvaluablecharacteristicofthe
is, its Icno mthmis upnaipceart,i owne s feorcvuicseesd a onnd tlhoeg idceavl einlofeprmenecnet coof mthpeo cnoernet sc.o Tmhpeo mneonstts v oafl uaa CbDleS cSh aprlaactftoerrmist,i cth oaft
proposedplatformisthecompatibilityandinteroperabilityofitsservices,facilitatingthedevelopment
tihse, itps rcoopmomseudn piclaattifoonrm se rivsi ctehse a ncodm lopgaitciabli liintyfe raenndc e icnotemroppoenreanbtisl.i tTyh eo fm iotss t svearlvuiacbesle, cfahcairlaitcatteirnigst itch oef
the proposed platform is the compatibility and interoperability of its services, facilitating the

Int.J.Environ.Res.PublicHealth2020,17,73 15of18
ofatransparentandpluggableCDSSsystem. CDSSsystemscanbeimplementedasstandaloneCDSS
solutionsorbeintegratedintoaclinicalworkflowoperatedbyanHIS.
Ourresearchadvancesthestateoftheartinsemanticallyinteroperableclinicaldecisionsupport
systems. ThepreviouslydevelopedFHIR-basedCDSSs[36–38]focusedononeparticulardecision
supporttask. Ourplatformallowsdefinitionofmultiplepurposedecisionsupportmodels,provided
thatthey(a)useFHIRresourcesasadatasourceand(b)arebasedonproductionrulesorBayesian
Logic. IncomparisonwiththeCDSSsdevelopedbasedonotherstandardsformedicaldataexchange,
suchasopenEHR[39],theproposedplatformdoesnotrequiremodellingofspecificdatasetsforeach
taskandcanprocessstandardFHIRresourcesinstead.
4.1. Architecture
Eachtypeofadecisionsupporttaskintheplatformhasitsownmicroservicetoallowacontinued
deliveryofnewfeaturesanddecisionsupportmodels. Allinteractionbetweenservicesisprocessedbya
commonAPIgateway,whichsupportsversioning. Thisapproachallowsdistinguishingresponsibilities
betweenservicesandperformingparalleldevelopmentoftheservicesbydifferentdedicatedteams.
4.2. ImplicationsandFutureUse
Theresultsofthepresentedresearchhaveavaluableimpactondesignandimplementationof
large-scaleclinicaldecisionsupportsystems. Itisveryimportanttomakeclinicaldecisionsupport
systems valid and easily acceptable by users. To accomplish this, we recommend to run a pilot
applicationofthedecisionsupportsystembytheexpertstoverifyandvalidatetherulestoincrease
thesystem’sreliabilityandacceptance.
A FHIR-based CDSS platform addresses the ease of access to the clinical decision support
services by providing standard-based interfaces and workflows. This type of CDSS may be able
to improve the quality of care for doctors who use HISs without CDSS features. The HL7 FHIR
interoperabilitystandardsmakethisplatformusablebyallHISsthatarecapableofintegratingwith
theHL7FHIRstandard.
4.3. Operation
Atthemoment,theplatformprocessesabout15,000ordersadaywithforeseen50,000orders
aday. Thesystemisablestoreupto50millionorders,withtheaverageoffivetestsineachoneto
providethecapacityforthenext7yearsofoperation.
Duringtheoperationoftheplatform,wediscoveredthesimilarweakpointsofthedeveloped
micro-service-basedsystemasreportedbyothermicro-service-baseddecisionsupportsystems[40–42].
Operationcomplexityhasincreasedduetotheintroductionofservicediscovery,servicebackup,and
automaticrestore. Maintenancealsobecamecomplicatedduetocomplexloggingsystems, where
eachserviceproducesitsownlogs. Weobservedarelativelymoderate,butneverthelessobservable
slowdownoftransactionhandlingduetothedistributedprocessing.
5. Conclusions
In this paper, we proposed a cloud-based interoperable multipurpose CDSS platform system
that makes use of semantic technologies based on the HL7 FHIR standard. We implemented two
types of knowledge modeling formalisms in the platform, namely production rules and Bayesian
Logic. Aflexibleknowledgeeditorsupportsclinicalexpertsimplementingdecisionsupportmodels
foranypurposebasedontheprovidedformalisms. Theplatformiscapableofprovisionofdecision
supportservicesforanyFHIR-enabledHISwithstandardCDSHooksinterfaces. Itmakesaccessto
CDS services easier and promotes their use in routine clinical professes to improve efficiency and
efficacyofhealthcare. Theplatformwasimplementedandisnowproductive,processingaround
50,000transactionsadaywithmorethan400decisionsupportmodels.

Int.J.Environ.Res.PublicHealth2020,17,73 16of18
AuthorContributions: Theauthorsmadethefollowingcontribution: I.S.methodology,R.O.andS.G.software
andvalidation,D.D.formalanalysisandinvestigation,Y.A.resourcesandsupervision,G.K.writing—originaldraft
preparation,review,andediting. Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding: This work was financially supported by the government of the Russian Federation through the
ITMO fellowship and professorship program. This worked was supported by a Russian Fund for Basic
research18-37-20002.
| ConflictsofInterest: | Theauthorsdeclarenoconflictofinterest. |     |     |     |     |     |     |     |
| -------------------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
References
1. Kopanitsa,G.MicroserviceArchitecturetoProvideMedicalDataManagementforDecisionSupport. Stud.
| HealthTechnol. | Inform. | 2019,261,230–235. |     | [PubMed] |     |     |     |     |
| -------------- | ------- | ----------------- | --- | -------- | --- | --- | --- | --- |
2. Pan,H.;Deal,B.ReportingonthePerformanceandUsabilityofPlanningSupportSystems—Towardsa
| CommonUnderstanding. |     | Appl. | Spat. | Anal. | Policy2019. | [CrossRef] |     |     |
| -------------------- | --- | ----- | ----- | ----- | ----------- | ---------- | --- | --- |
3. Pan,H.; Page,J.; Zhang,L.; Chen,S.; Cong,C.; Destouni,G.; Kalantari,Z.; Deal,B.Usingcomparative
socio-ecological modeling to support Climate Action Planning (CAP). J. Clean. Prod. 2019, 232, 30–42.
[CrossRef]
4. Dao Phuoc, T.; Khuong Quynh, L.; Vien Dang Khanh, L.; Ong Phuc, T.; Le Sy, H.; Le Ngoc, T.; Phung
WellcomeOpenRes.
Khanh,L.Clinicalprognosticmodelsforseveredengue: Asystematicreviewprotocol.
| 2019,4,12. | [CrossRef] |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
5. Bose,R.Knowledgemanagement-enabledhealthcaremanagementsystems: Capabilities,infrastructure,
| anddecision-support. |     | ExpertSyst. | Appl. | 2003,24,59–71. |     | [CrossRef] |     |     |
| -------------------- | --- | ----------- | ----- | -------------- | --- | ---------- | --- | --- |
6. Marco-Ruiz,L.;Pedrinaci,C.;Maldonado,J.A.;Panziera,L.;Chen,R.;Bellika,J.G.Publication,discovery
andinteroperabilityofClinicalDecisionSupportSystems: ALinkedDataapproach. J.Biomed. Inform. 2016,
| 62,243–264. | [CrossRef] |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
7. Khalifa,M.;Zabani,I.ImprovingUtilizationofClinicalDecisionSupportSystemsbyReducingAlertFatigue:
| StrategiesandRecommendations. |     |     | Stud. | HealthTechnol. |     | Inform. | 2016,226,51–54. |     |
| ----------------------------- | --- | --- | ----- | -------------- | --- | ------- | --------------- | --- |
8. Chi, C.L.; Nick Street, W.; Robinson, J.G.; Crawford, M.A. Individualized patient-centered lifestyle
recommendations: Anexpertsystemforcommunicatingpatientspecificcardiovascularriskinformation
| andprioritizinglifestyleoptions. |     |     | J.Biomed. |     | Inform. | 2012,45,1164–1174. |     | [CrossRef] |
| -------------------------------- | --- | --- | --------- | --- | ------- | ------------------ | --- | ---------- |
Ann. Intern. Med. 2011,
9. Owens,D.K.Improvingpracticeguidelineswithpatient-specificrecommendations.
| 154,638–639. | [CrossRef] |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
10. Kopanitsa,G.;Semenov,I.Patientfacingdecisionsupportsystemforinterpretationoflaboratorytestresults.
| BMCMed. | Inform. | Decis. Mak. | 2018,18,68. |     | [CrossRef] |     |     |     |
| ------- | ------- | ----------- | ----------- | --- | ---------- | --- | --- | --- |
11. Kam,H.J.; Kim,J.A.; Cho,I.; Kim,Y.; Park,R.W.Integrationofheterogeneousclinicaldecisionsupport
systems and their knowledge sets: Feasibility study with Drug-Drug Interaction alerts. AMIA Annu.
| Symp.Proc. | 2011,2011,664–673. |     |     |     |     |     |     |     |
| ---------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
12. Lee,J.;Kim,J.;Cho,I.;Kim,Y.Integrationofworkflowandruleenginesforclinicaldecisionsupportservices.
| Stud. HealthTechnol. |     | Inform. 2010,160,811–815. |     |     |     |     |     |     |
| -------------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
13. Weber,S.;Crago,E.A.;Sherwood,P.R.;Smith,T.Practitionerapproachestotheintegrationofclinicaldecision
supportsystemtechnologyincriticalcare. J.Nurs. Adm. 2009,39,465–469. [CrossRef]
14. Leroux,H.;Metke-Jimenez,A.;Lawley,M.J.Towardsachievingsemanticinteroperabilityofclinicalstudy
| datawithFHIR.J.Biomed. |     | Semant. | 2017,8,41. |     |     |     |     |     |
| ---------------------- | --- | ------- | ---------- | --- | --- | --- | --- | --- |
[CrossRef]
15. Atalag,K.;Yang,H.Y.;Tempero,E.;Warren,J.Modeldrivendevelopmentofclinicalinformationsytems
| usingopenEHR.Stud. |     | HealthTechnol. |     | Inform. | 2011,169,849–853. |     |     |     |
| ------------------ | --- | -------------- | --- | ------- | ----------------- | --- | --- | --- |
16. Kopanitsa,G.EvaluationStudyforanISO13606ArchetypeBasedMedicalDataVisualizationMethod.
| J.Med.Syst. | 2015,39,82. | [CrossRef] |     |     |     |     |     |     |
| ----------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
17. BarrosCastro,J.;LameloAlfonsin,A.;PrietoCebreiro,J.;RimadaMora,D.;CarrajoGarcia,L.;Vazquez
Gonzalez,G.DevelopmentofISO13606archetypesforthestandardisationofdataregistrationinthePrimary
| Careenvironment. |     | Stud. HealthTechnol. |     | Inform. | 2015,210,877–881. |     |     |     |
| ---------------- | --- | -------------------- | --- | ------- | ----------------- | --- | --- | --- |
18. Paun,I.D.;Sauciuc,D.G.;Iosif,N.O.;Stan,O.;Perse,A.;Dehelean,C.;Miclea,L.LocalEHRmanagement
| basedonopenEHRandEN13606. |     |     | J.Med. | Syst. | 2011,35,585–590. |     | [CrossRef] |     |
| ------------------------- | --- | --- | ------ | ----- | ---------------- | --- | ---------- | --- |

Int.J.Environ.Res.PublicHealth2020,17,73 17of18
19. Pecoraro,F.;Luzi,D.;Ricci,F.L.DataWarehouseDesignfromHL7ClinicalDocumentArchitectureSchema.
| Stud. HealthTechnol. | Inform. | 2015,213,139–142. |     |     |
| -------------------- | ------- | ----------------- | --- | --- |
20. Boussadi,A.;Zapletal,E.AFastHealthcareInteroperabilityResources(FHIR)layerimplementedoveri2b2.
| BMCMed. | Inform. Decis. Mak. | 2017,17,120. | [CrossRef] |     |
| ------- | ------------------- | ------------ | ---------- | --- |
21. Marcos, M.; Maldonado, J.A.; Martinez-Salvador, B.; Bosca, D.; Robles, M. Interoperability of clinical
decision-support systems and electronic health records using archetypes: A case study in clinical trial
| eligibility. | J.Biomed. Inform. | 2013,46,676–689. | [CrossRef] |     |
| ------------ | ----------------- | ---------------- | ---------- | --- |
22. Kashfi,H.AnopenEHR-basedclinicaldecisionsupportsystem: Acasestudy. Stud. HealthTechnol. Inform.
2009,150,348.
23. Khalilia,M.; Choi,M.; Henderson,A.; Iyengar,S.; Braunstein,M.; Sun,J.ClinicalPredictiveModeling
DevelopmentandDeploymentthroughFHIRWebServices. AMIAAnnu. Symp. Proc. 2015,2015,717–726.
24. Wang,L.L.;ThomasHayman,G.;Smith,J.R.;Tutaj,M.;Shimoyama,M.E.;Gennari,J.H.Predictinginstances
ofpathwayontologyclassesforpathwayintegration. J.Biomed. Semant. 2019,10,11. [CrossRef]
25. Ruokolainen,J.MobileMicroserviceArchitectureforPatientsSelf-Care. Stud. HealthTechnol. Inform. 2017,
244,106.
26. Spineth, M.; Rappelsberger, A.; Adlassnig, K.P. Implementing CDS Hooks Communication in an
Arden-Syntax-BasedClinicalDecisionSupportPlatform. Stud. HealthTechnol. Inform. 2018,255,165–169.
27. Wulff,A.;Montag,S.;Marschollek,M.;Jack,T.ClinicalDecision-SupportSystemsforDetectionofSystemic
InflammatoryResponseSyndrome,Sepsis,andSepticShockinCriticallyIllPatients: ASystematicReview.
| MethodsInform. | Med. 2019. | [CrossRef] |     |     |
| -------------- | ---------- | ---------- | --- | --- |
Effects
28. Sakurai, R.; Ohe, K. of Computerized Guideline-Oriented Clinical Decision Support System on
Antithrombotic Therapy in Patients with Atrial Fibrillation: A Systematic Review and Meta-Analysis.
| Stud.HealthTechnol. | Inform. | 2019,264,768–772. | [CrossRef] |     |
| ------------------- | ------- | ----------------- | ---------- | --- |
29. Hussain,M.I.;Reynolds,T.L.;Zheng,K.Medicationsafetyalertfatiguemaybereducedviainteraction
designandclinicalroletailoring: Asystematicreview. J.Am. Med. Inform. Assoc. 2019,26,1141–1149.
[CrossRef]
30. Semenov,I.;Kopanitsa,G.;Denisov,D.;Alexandr,Y.;Osenev,R.;Andreychuk,Y.PatientsDecisionAid
| SystemBasedonFHIRProfiles. |     | J.Med. | Syst. 2018,42,166. | [CrossRef] |
| -------------------------- | --- | ------ | ------------------ | ---------- |
Sittig,D.F.;Wright,A.;Osheroff,J.A.;Middleton,B.;Teich,J.M.;Ash,J.S.;Campbell,E.;Bates,D.W.Grand
31.
challengesinclinicaldecisionsupport. J.Biomed. Inform. 2008,41,387–392. [CrossRef]
32. Šelih,J.;Kne,A.;Srdic´,A.;Žura,M.Multiple-criteriadecisionsupportsysteminhighwayinfrastructure
| management. | Transport2008,23,299–305. |     | [CrossRef] |     |
| ----------- | ------------------------- | --- | ---------- | --- |
Huff,
33. Stram, M.; Gigliotti, T.; Hartman, D.; Pitkus, A.; S.M.; Riben, M.; Henricks, W.H.; Farahani, N.;
Pantanowitz, L. Logical Observation Identifiers Names and Codes for Laboratorians. Arch. Pathol.
| Lab.Med.2019. | [CrossRef] |     |     |     |
| ------------- | ---------- | --- | --- | --- |
34. Arbabi, A.; Adams, D.R.; Fidler, S.; Brudno, M. Identifying Clinical Terms in Medical Text Using
Ontology-GuidedMachineLearning. JMIRMed. Inform. 2019,7,e12596. [CrossRef]
35. Zhang,X.A.;Yates,A.;Vasilevsky,N.;Gourdine,J.P.;Callahan,T.J.;Carmody,L.C.;Danis,D.;Joachimiak,M.P.;
Ravanmehr,V.; Pfaff,E.R.; etal. Semanticintegrationofclinicallaboratorytestsfromelectronichealth
recordsfordeepphenotypingandbiomarkerdiscovery. NPJDigit. Med. 2019,2. [CrossRef]
36. Nguyen,B.P.;Reese,T.;Decker,S.;Malone,D.;Boyce,R.D.;Beyan,O.ImplementationofClinicalDecision
SupportServicestoDetectPotentialDrug-DrugInteractionUsingClinicalQualityLanguage. Stud. Health
| Technol. Inform. | 2019,264,724–728. | [CrossRef] |     |     |
| ---------------- | ----------------- | ---------- | --- | --- |
37. Odigie,E.;Lacson,R.;Raja,A.;Osterbur,D.;Ip,I.;Schneider,L.;Khorasani,R.FastHealthcareInteroperability
Resources, Clinical Quality Language, and Systematized Nomenclature of Medicine-Clinical Terms in
RepresentingClinicalEvidenceLogicStatementsfortheUseofImagingProcedures: DescriptiveStudy.
| JMIRMed. | Inform. 2019,7,e13590. | [CrossRef] |     |     |
| -------- | ---------------------- | ---------- | --- | --- |
38. Dolin,R.H.;Boxwala,A.;Shalaby,J.APharmacogenomicsClinicalDecisionSupportServiceBasedonFHIR
| andCDSHooks. | MethodsInform. | Med. | 2018,57,e115–e123. | [CrossRef] |
| ------------ | -------------- | ---- | ------------------ | ---------- |
39. Kopanitsa,G.IntegrationofHospitalInformationandClinicalDecisionSupportSystemstoEnablethe
ReuseofElectronicHealthRecordData. MethodsInform. Med. 2017,56,238–247. [CrossRef]

Int.J.Environ.Res.PublicHealth2020,17,73 18of18
40. Emami Khoonsari, P.; Moreno, P.; Bergmann, S.; Burman, J.; Capuccini, M.; Carone, M.; Cascante, M.;
de Atauri, P.; Foguet, C.; Gonzalez-Beltran, A.N.; et al. Interoperable and scalable data analysis with
microservices: Applicationsinmetabolomics. Bioinformatics2019,35,3752–3760. [CrossRef]
41. Li,Z.;Seco,D.;SánchezRodríguez,A.E.Microservice-OrientedPlatformforInternetofBigDataAnalytics:
AProofofConcept. Sensors2019,19,1134. [CrossRef]
42. Williams,C.L.; Sica,J.C.; Killen,R.T.; Balis,U.G.Thegrowingneedformicroservicesinbioinformatics.
J.Pathol. Inform.2016,7,45. [CrossRef]
©2019bytheauthors. LicenseeMDPI,Basel,Switzerland. Thisarticleisanopenaccess
articledistributedunderthetermsandconditionsoftheCreativeCommonsAttribution
(CCBY)license(http://creativecommons.org/licenses/by/4.0/).
