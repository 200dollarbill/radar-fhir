JournaloftheAmericanMedicalInformaticsAssociation,28(8),2021,1796–1806
doi:10.1093/jamia/ocab070
AdvanceAccessPublicationDate:8June2021
Review
Review
Contemporary clinical decision support standards using
Health Level Seven International Fast Healthcare
Interoperability Resources
HowardR.Strasberg,1BrynRhodes,2GuilhermeDelFiol ,3RobertA.Jenders,4,5
PeterJ.Haug,6andKensakuKawamoto 3
1ClinicalEffectiveness,WoltersKluwerHealth,SanDiego,California,USA, 2DynamicContentGroup,Orem,Utah,USA,3Depart-
mentofBiomedicalInformatics,UniversityofUtah,SaltLakeCity,Utah,USA,4DepartmentofInternalMedicineandCenterfor
BiomedicalInformatics,CharlesRDrewUniversityofMedicineandScience,LosAngeles,California,USA,5DepartmentofMedi-
cine and Clinical and TranslationalScience Institute, University of California, Los Angeles, Los Angeles, California, USA, and
6MedicalInformatics,IntermountainHealthcare,SaltLakeCity,Utah,USA
CorrespondingAuthor:HowardR.Strasberg,WoltersKluwerHealth,3830ValleyCentreDrSte705,PMB461,SanDiego,
CA,92130,USA;howard.strasberg@wolterskluwer.com
Received13January2021;Revised8March2021;EditorialDecision27March2021;Accepted5April2021
ABSTRACT
Objective:Tofacilitatethedevelopmentofstandards-basedclinicaldecisionsupport(CDS)systems,wereview
thecurrentsetofCDSstandardsthatarebasedonHealthLevelSevenInternationalFastHealthcareInteropera-
bility Resources (FHIR). Widespread adoption of these standards may help reduce healthcare variability, im-
provehealthcarequality,andimprovepatientsafety.
TargetAudience:Thistutorialisdesignedforthebroadinformaticscommunity,someofwhommaybeunfa-
miliarwiththecurrent,FHIR-basedCDSstandards.
Scope:Thistutorialcoversthefollowingstandards:ArdenSyntax(usingFHIRasthedatamodel),ClinicalQual-
ity Language, FHIR Clinical Reasoning, SMART on FHIR, and CDS Hooks. Detailed descriptions and selected
examplesareprovided.
Keywords:HealthLevelSeven,HealthInformationInteroperability,ElectronicHealthRecords,software,medicalinformatics
INTRODUCTION
lacksastandardclinicaldatamodelandastandards-baseddatare-
Therationaleforcreatingandusingstandardsforclinicaldecision trievalmechanism.Instead,dataareretrievedfromlocalsourcesys-
support (CDS) is to support explicit representation of knowledge, temsusingproprietarymechanismsthattypicallyvaryfromsiteto
therebyfacilitatingitsvalidation,andtofosterknowledgesharing, site(knownasthe“curlybracesproblem”),therebylimitinginter-
therebyreducingthecostofknowledgeengineeringandfacilitating operabilityandreuse.Anearlyattempttoaddressthepatientdata
dissemination.CDSstandardshavebeenaroundfor3decades.The model problem was the Virtual Medical Record (vMR).3 In this
earliest of these standards—the Arden Syntax for Medical Logic model,electronichealthrecord(EHR)systemswouldexposeanin-
Systems—was first described in 19911 and is now a Health Level teroperable data layer conforming to the vMR data model. CDS
SevenInternational(HL7)standard.2Itsupportsknowledgerepre- logiccouldthenbewrittenagainstthismodelandusedacrosssites
sentationinmedicallogicmodules(MLMs),but,withnoconsensus andwithdifferentEHRs.TheHL7vMR4isthedatamodelusedin
at the time for such concepts in health information technology, it GELLO,5whichisanobject-orientedqueryandexpressionlanguage
VCTheAuthor(s)2021.PublishedbyOxfordUniversityPressonbehalfoftheAmericanMedicalInformaticsAssociation.
Allrightsreserved.Forpermissions,pleaseemail:journals.permissions@oup.com 1796

JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8 1797
forCDSandalsoanHL7standard.6GELLOwasdevelopedasthe Akeychallengeforimplementersandauthorswhohaveadopted
expressionlanguagefortheGuideLineInterchangeFormat(GLIF),7 theArdenSyntaxhasbeenportabilityofArden-baseddecisionsup-
whichisaformatforrepresentingclinicalguidelines.Inthelastde- port.AseparatedataslotwasincorporatedintotheoriginalArden
cade,HL7alsodevelopedtheClinicalDecisionSupportKnowledge SyntaxtosupporttranslationbetweendatamodelsusedintheEHR
ArtifactSpecification(CDS-KAS).8Thisspecificationwasdesigned systemsofadoptinginstitutionsandthedatarepresentationchosen
torepresentevent-condition-actionrules,ordersets,anddocumen- bytheMLM’sauthor.Thiscapabilityiskeytoreferencingdataele-
tation templates. The specification permitted any patient data ments using medically recognizable terminology. While the func-
model,butitcitedtheHL7vMRasanexample.Earlieriterationsof tionalityofthisdataaccessapproachwasenhancedovertime,the
CDS-KAS included a representation for expression logic, but this absence of a standard way to consume data from disparate EHRs
logicevolvedintoitsownnewstandard,theHL7ClinicalQuality madeitdifficulttotransferMLMsfromoneinstitutiontoanother.
Language(CQL).9ThecurrentversionofCDS-KASthereforeuses Whilethischallengeiscommontoanyclinicalknowledgerepresen-
CQLtorepresentexpressionlogic. tationformalismusedinknowledgetransfer,becauseArden’srefer-
In2014,HL7publishedthefirstdraftversionofanewstandard encestolocalEHRdataelementswereenclosedincurlybraces,this
called Fast Healthcare Interoperability Resources (FHIR).10 FHIR becameknownasthecurlybracesproblem.14
definesahealthcaredatamodelaswellasasetofRESTfulservices TheuptakeoftheHL7FHIRspecificationsforaccessingclinical
forexchanginghealthcaredatabetweenapplications.Givenitspo- dataappearslikelytohelpsignificantlyinaddressingthecurlybra-
tential roles in CDS, the FHIR data model is the successor of the cesproblem.TheArdencommunityanticipatesacomingreleaseof
vMR,althoughthescopeofFHIR(allhealthcaredata,plusservices) thestandard(Arden3.0)thatwillredefinethedataslotinthecon-
ismuchbroaderthanthescopeofvMR(focusedondatatosupport text of a common approach to retrieving and storing EHR data
CDS).In 2020,FHIR Release4 (R4)11 wasincludedin regulation based on FHIR. This update is expected to dramatically diminish
fromtheU.S.OfficeoftheNationalCoordinatorforHealthInfor- thechallengesofportingsetsofMLMsfromoneclinicalsettingto
mation Technology.12 This regulation specifies a time frame of 2 another.
yearsforuseofFHIRR4asaconditionofcertificationofhealthin- Figure1containsanexampleofhowaMLMmightbeauthored
formation technology. Giventhe expected widespreadadoption of for chlamydia screening using FHIR as the data model. The logic
FHIR R4 within this time frame, CDS systems that are based on hasbeensimplifiedsuchthatitevaluates(1)whetherthepatientis
FHIRR4arelikelytobemoreinteroperableacrossdifferenthealth- in the appropriate demographic, (2) whether chlamydia screening
care settings. Therefore, FHIR brings unprecedented opportunities has not occurred within the past year, and (3) whether chlamydia
forwiderdisseminationandsharingofCDSlogic,capabilities,and screeninghasalreadybeenordered.ThisrepresentationusingFHIR
tools. To facilitate the development of standards-based CDS sys- ismeanttobeanearlyindicationofthedirectionofArden3.0,but
tems,inthisarticlewereviewthecurrentsetofCDSstandardsthat thesyntaxmaychangeasthestandardgetsfurtherdeveloped.
arebasedonFHIRandhowthesestandardsrelatetoeachotherin
the context of an example regarding a recommendation for chla-
CLINICALQUALITYLANGUAGE
mydiascreening.
CQLgrewoutofanefforttoharmonizeknowledgerepresentation
standards in use across both CDS and quality measurement, and
ARDENSYNTAX
was built as a general-purpose clinically-focused query language,
The Arden Syntax for Medical Logic Systems has been in use for suitable for use in a variety of clinical quality improvement use
muchofthelast3decades.Duringthatperiod,ithasmovedfrom cases. CQL recently became a normative HL7 standard, meaning
version1.0toversion2.10.TheArdenSyntaxprovidesastructured, thatanyfuturechangeswillbebackwardcompatible.WhileCQLit-
executable formalism for representing clinical, administrative, and selfsupportsarbitrarydatamodels,wewillfocusourdiscussionon
otherknowledge.ItwasdesignedprimarilytobeusedinCDSsys- examplesusingFHIRasthedatamodel.CQLisalignedwithFHIR
tems.Assuch,itfunctionsasaprogramminglanguageforsuchsys- in3importantways.First,thesystem-defineddatatypesinCQLare
tems, allowing knowledge authors and clinical domain experts to aligned directly with the base data types in FHIR, including data
develop and implementapplications designedto improve care and typesforsupportingquantities,intervals,andterminology.Second,
supporttheprocessofhealthcaredelivery.Arden-basedCDSispro- FHIR uses a simple graph-traversal language called FHIRPath to
videdthroughgroupsoftext-basedmodulescalledMLMs. supportdescriptionofpathsandinvariantsthroughoutthespecifica-
Akeygoalofthelanguagehasbeentorepresentmedicalknowl- tion.CQLusesFHIRPathasitsbasegrammar,extendingFHIRPath
edgeinaformaccessibletomedicaldomainexperts.Ardenprovides to support libraries and general-purpose queries. Third, CQL sup-
theabilitytoexpressexecutableknowledgeinanEnglish-language ports terminology using first-class language constructs that align
syntax.ThischaracteristicoftheArdenSyntaxwasdesignedtofa- withthewayterminologyis represented,distributed, andaccessed
cilitatevalidationofknowledgeartifactsbydomainexperts.More- withintheFHIRspecification.
over,Ardenprovidesconstructsforrepresentingthe evidenceused CQL is a query language, meaning that statements of the lan-
in CDS, for defining the triggers used to commence execution of guagearequestions,formulatedintermsofadatamodel(eg,FHIR)
CDS knowledge, and for facilitating output messaging, such as a thatdescribestheavailabledata.Thesequestionsarerepresentedas
Resourcescategorythatallowsmappingofoutputindifferentnatu- namedexpressions, whichare thebasicunitsoflogicdefinitionin
rallanguages. CQL.15
WhiletheinitialapproachtoexpressingMLMswasinastruc- As an example, Figure 2 illustrates CQL logic to determine
turedtextualform,recentversionsofthestandardhaveprovidedan whetherornotchlamydiascreeningisindicated.Thisexamplehas
ExtensibleMarkupLanguage(XML)–basedrepresentationasanal- beensimplifiedfromtheversionavailableaspartofthestandard.16
ternative.Thisformhasbeendemonstratedto simplifyconversion Inthe example, weassignnamesto 2valuesets usingtheirobject
intoexecutableformssuchastheDroolsproductionrulesystem.13 identifiers.ThemembersofthesevaluesetscanbefoundintheNa-

1798 JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8
Figure1.ExampleofanArdenSyntaxmedicallogicmoduleforchlamydiascreeningusingFastHealthcareInteroperabilityResourcesasthedatamodel.
tionalLibraryofMedicineValueSetAuthorityCenterrepository.17 Notehowthisexampletakesadvantageofwhatisknownasthe
Next, we define a named expression “InDemographic,” which retrieve declaration in CQL. The expression [“DiagnosticReport”:
checkstoseeifthepatientisintherightdemographic.Similarly,we “Chlamydia Screening”] returns all DiagnosticReport resources
defineanamedexpression“NoScreening”toseeifthepatienthasa withacodeintheChlamydiaScreeningvalueset.Thesquarebrack-
chlamydiascreeningresult(anFHIRDiagnosticReportwithacode etsinvoketheretrieveoperation.Intheexample,theletter“R”fol-
intheChlamydiaScreeningvalueset)issuedwithinthelastyearor lowing the retrieve expression assigns the results to the alias “R,”
if an order (a FHIR ServiceRequest with a code in the Chlamydia whichisthenusedinthesubsequentWHEREclause.Alsonotehow
Screeningvalueset)hasalreadybeenplacedforthispatient.Finally, wedidnotusethe“ChlamydiaScreeningRequest”inordertoeval-
we define a named expression “NeedScreening,” which returns uate“NoScreening.”Wewillmakeuseofthisdefinitioninthenext
TRUEifboth“InDemographic”and“NoScreening”returnTRUE. section.

JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8 1799
Figure1.Continued
CLINICALREASONING
|     |     |     |     |     |     | the action is applicable. |     | For the | actual logic | of  | the condition, | the |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | ------- | ------------ | --- | -------------- | --- |
PlanDefinitionreferstotheCQLlibraryinFigure2,andinparticu-
AlthoughFHIRisahealthcaredatamodel,itsscopeisnotlimitedto
lartothe“NoScreening”expression.Ifthisexpressionevaluatesto
| data describing | an individual | patient. | The Clinical | Reasoning |     |     |     |     |     |     |     |     |
| --------------- | ------------- | -------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
TRUE,thentheconditionissatisfied.
modulespecifieshowtouseFHIRtorepresentclinicalknowledge.
|                |             |               |      |                |     | When the                | condition | is true,   | the action | has        | several | possible |
| -------------- | ----------- | ------------- | ---- | -------------- | --- | ----------------------- | --------- | ---------- | ---------- | ---------- | ------- | -------- |
| In the example | depicted in | Figure 3, the | FHIR | PlanDefinition | re- |                         |           |            |            |            |         |          |
|                |             |               |      |                |     | approaches toproducethe |           | THENpartof |            | therule.In | the     | simplest |
sourceisusedtorepresentanEvent-Condition-Actionrulethatuses
case,the“textEquivalent”elementoftheactionprovidesatextual
theCQLexpressionsrepresentedinFigure2.Thisexampleisdrawn
descriptionoftheactiontobeperformed.Formoredynamicproc-
fromtheFHIRspecificationforPlanDefinition.18
essing,the“dynamicValue”elementallowsvaluestobeconstructed
Thefirstseverallinesoftheexamplecontainimportantmetadata
byexpressionsaspartofevaluatingtherule.Thesecanbeelements
| about the | artifact. The rule | itself is contained | within | a single, | top |     |     |     |     |     |     |     |
| --------- | ------------------ | ------------------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
oftheresult,suchassettingthedosageonamedicationrequest,or
| level “action” | element. | The condition | (or the | IF part | of an |     |     |     |     |     |     |     |
| -------------- | -------- | ------------- | ------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
theycanbeexpressionsthatreturntheentirerequest,asintheex-
| IF...THEN        | rule) is specified. | In this            | case, | its “kind” | is      |                             |     |               |     |       |            |        |
| ---------------- | ------------------- | ------------------ | ----- | ---------- | ------- | --------------------------- | --- | ------------- | --- | ----- | ---------- | ------ |
|                  |                     |                    |       |            |         | ample in Figure             | 3.  | In this case, | we  | use   | the result | of the |
| “applicability,” | which means         | that the condition |       | describes  | whether |                             |     |               |     |       |            |        |
|                  |                     |                    |       |            |         | “ChlamydiaScreeningRequest” |     | expression,   |     | which | constructs | a      |

1800 JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8
Figure2.ClinicalQualityLanguageexampleforchlamydiascreeningclinicaldecisionsupport.
“ServiceRequest” proposal to indicate that a Chlamydia screening irubin management,25 genomic test ordering and result
should be performed. Finally, the “definition” element allows the interpretation,26,27andopioidprescribing.28
actiontobespecifiedbyreferencingapredefinedactivitydefinition, Fromasecuritystandpoint,appsaregrantedaccessonlytoade-
usingtheActivityDefinitionresource. finedscopeofFHIRresources.29Forexample,thescopecanbelim-
The exampleillustratedhereshowshow asinglerecommenda- itedtocertainspecifiedresourcespertainingtothecurrentpatient.
tioncanbeexpressedusingFHIRClinicalReasoningandCQL,but Thisscenariowouldbecommoninappsthathelpmanagethecare
theresourcesintheClinicalReasoningmodulesupportthedescrip- of an individual patient. For other apps that might assist with the
tionofmanyothertypesofknowledgeartifactstosupportclinical management of manypatients(eg,to supportclinicalrounds),the
qualityimprovement.Forexample,thePlanDefinitionandActivity- scope can be specified at the user level, rather than at the patient
Definition resources can represent many othertypes of knowledge level. In this case, the app could be provided with access to all
artifacts including order sets, order catalogs, documentation tem- resourcesthatthecurrentusercouldotherwiseaccessintheEHR.
plates,questionnaires,processes,protocols,pathways,andcomput- For a more detailed discussion of the security and authorization
ableguidelines.19 components,includingsomeexcellentsequencediagramsandsam-
pleinteractionpayloads,wedirectreaderstotheSMARTonFHIR
specificationitself.21
SMARTONFHIR Usingourchlamydiascreeningexample,aSMARTonFHIRapp
could be developed to provide screening advice for a full range of
SMARTonFHIRisastandardmethodtolaunchexternalapplica-
healthmaintenance andchronicdiseasemanagement needs,rather
tions from an EHR. The SMART (Substitutable Medical Applica-
than just chlamydia screening. The user might launch this app to
tions, Reusable Technologies) component, which handles app
viewtherecommendationsforagivenpatientalongwithadetailed
launchingandauthenticationtotheEHRsystem’sFHIRserverus-
rationaleforeachrecommendation.
ingtheOAuth2.0standard,wasfirstdescribedbyMandletalin
2012.20 At a later date, FHIR was added as the data model and
EHRdataretrievalservice,therebyresultinginthecurrentSMART
CDSHOOKS
onFHIRstandard.21,22
Theresultisastandardtoenableanapp-basedecosystemsimilar CDS Hooks is an HL7 Standard for Trial Use that is a RESTful,
inconcepttotheAppleAppStoreorGooglePlay.Anumberofapps JavaScriptObjectNotation(JSON)–basedWebservicespecification
havebeendescribedintheliterature,includingappsforchronicdis- thatusesFHIRfortheexchangeofpatientdata.30Oneofitsorigi-
easemanagement,23riskpredictioninspinalsurgery,24neonatalbil- nalgoalswastoalertuserstotheexistenceofarelevantSMARTon

JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8 1801
Figure3.PlanDefinitionexampleforchlamydiascreeningclinicaldecisionsupport.
FHIRappforthemanagementofagivenpatient.Forexample,ifa and privacy reasons, the prefetch template option might often be
patienthashypertension,theCDSHooksservicemightsuggestthat preferred.
the user launch a SMART on FHIR app to manage hypertension. CDSHooksservicesreturn“cards”withvariousattributes.The
ThecurrentscopeextendswellbeyondthisusecasetoincludeCDS contentofthesecardswouldtypicallybedisplayedtouserswithin
servicesthatareunrelatedtoanyparticularSMARTonFHIRapp. their workflow. The required card elements include a summary
Forexample,aCDSHooksservicecouldcheckfordrug-druginter- (usuallyonesentence,suchasthetextofanalert),anindicatorof
actions,31providepreventivecarereminders,evaluatetheappropri- thecard’simportance(info,warningorcritical),andasource(toin-
ateness of imaging studies,32 or even be used asynchronously for dicatetheCDSsource).Thecallingapplicationmayusetheindica-
populationhealthmanagementpurposes.33 torvaluetodeterminehowto presentthe cardinformationtothe
As the name implies, CDS Hooks relies on certain workflow user.Forexample,acardwitha“critical”indicatormightbepre-
“hooks”totriggercallstotheWebservice.Somecurrentexamples sentedmoreprominentlythanacardwithan“info”indicator.
include“patient-view”(openingthechart),“order-select”(selecting Optionalcardelementsincludeauniqueidentifierforthecard,
an item from an order catalog), and “order-sign” (signing fully detailedinformation,suggestions,andlinks.Whilelinkscanbegen-
specified orders). When these events occur, the service would be erallinkstowebsites,theycanalsobelinkstolaunchSMARTon
called with contextual data elements specified in the hook defini- FHIR apps, thereby enabling the original CDS Hooks use case of
tion.Forexample,forthe“patient-view”hook,thecontextualele- recommendingSMARTonFHIRapps.Cardsuggestionsrepresent
mentsincludetheuserIdofthecurrentuser,theFHIRPatient.idof suggested actions for the user to consider, such as modifying the
the patient in question, and optionally, the FHIR Encounter.id of doseofamedicationorderororderinganalternativeimagingstudy.
the current encounter.34 Armed with these data, the service could ThesesuggestionsarerepresentedasFHIRresourcesandallowthe
thenrequesttheclinicaldataitneedsfromtheFHIRserverthrough usertosubmitthesuggestiontotheEHRfromwithinthecarditself.
a security mechanism described subsequently. Alternatively, a ser- ToallowtheCDSservicetomakecallstotheFHIRserver,the
vicecouldspecifya“prefetchtemplate”thatspecifiestheFHIRdata CDS client may include fhirServer and fhirAuthorization fields in
theservicegenerallyneedstoperformanevaluation.Inthisway,the thebodyoftheinitialWebservicecall.ThefhirServerfieldcontains
callingapplicationcouldprovidetheFHIRdataaspartoftheinitial thebaseURLoftheCDSclient’sFHIRserver.ThefhirAuthoriza-
servicecall,therebyeliminatingtheneedfortheservicetocallback tionfieldcontainsanOAuth2.0beareraccesstokenfortheFHIR
intotheFHIRservertoobtainclinicaldata.Forbothperformance server.Notethataccesstokensspecifybothanexpirationtimeanda

1802 JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8
Figure4.CDSHooksdiscoveryandrequestexample.
scope,whichwoulddeterminewhichFHIRresourcestheCDSser- eithertheArdenSyntax(withFHIRasthedatamodel)ortheClini-
vicecouldqueryandforwhichpatient. calReasoningartifactswithaCQLlibrary.Userscouldalsolaunch
AnexampleofaCDSHooksdiscoveryendpointandrequestis external SMART on FHIR CDS apps. These apps may choose to
showninFigure4,alongwithacardresponseexampleinFigure5. representsomeoftheirbusinesslogicusingClinicalReasoningand
Theresponseexampleincludesasuggestion,whichisstructuredasa CQL.EHRsmayalsochoosetolaunchexternalCDSHooksWeb
FHIR ServiceRequest resource to request the chlamydia screening services. The providers of these services may choose to represent
procedure.CDSHookshasthepotentialtoenablecloud-basedCDS someoftheirbusinesslogicusingClinicalReasoningandCQL.The
servicesatscalefrommultipleserviceproviders,allusingacommon responsecardsfromCDSHooksservicesaredisplayedtousersin-
setofstandards. sidetheEHRandmaycontainalinktolaunchaSMARTonFHIR
app.ForbothSMARTonFHIRandCDSHooks,FHIRisusedto
representthepatientdata.Notethatthefiguresimplifiesthedepic-
INTEGRATINGSTANDARDS
tionof howtheseexternal componentsare launched. ForSMART
Figure 6 depicts how all of these standards fit together. Local, on FHIR, a FHIR server access token is provided, allowing the
standards-based CDS could be implemented inside the EHR using SMARTonFHIRapptoretrievethenecessarydatafromtheFHIR

JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8 1803
Figure5.CDSHooksresponseexample.
server.ForCDSHooks,thereare2options:theprovisionofaFHIR thecapabilitiesofspecificEHRsystems,wewilldiscussEHRadop-
server access token or direct inclusion of prefetched FHIR data. tioningeneralterms.WeareawareofseveralcommercialEHRsys-
Overall, while the individual members of this suite of standards temsthatincorporatetheArdenSyntaxintotheirsoftware,butwe
havesomeoverlappingcharacteristics,eachoffersdifferentfeatures are also aware of several major EHR systems that do not support
thathelphealthcareorganizationsandhealthcareinformationtech- thisstandard.Thesesystemstendtouseproprietaryexpressionlan-
nologyimplementersaccommodatenuancedCDSneeds. guagesforCDS.CQLwasrecentlyapprovedasanormativestan-
|     |     |     |     |     | dard.However, | even | thoughthe | ArdenSyntax |     | andCQL | are both |
| --- | --- | --- | --- | --- | ------------- | ---- | --------- | ----------- | --- | ------ | -------- |
normativestandards,thereisvastlymoreexperiencewiththeArden
MATURITY,ADOPTION,ANDFUTUREWORK
Syntaxgivenhowlongithasbeeninuse.Weareawareofatleast1
|              |                                |      |                  |          | commercial           | EHR | system that | is working | toward | supporting        | CQL  |
| ------------ | ------------------------------ | ---- | ---------------- | -------- | -------------------- | --- | ----------- | ---------- | ------ | ----------------- | ---- |
| The CDS      | standards described previously | vary | widely in        | terms of |                      |     |             |            |        |                   |      |
|              |                                |      |                  |          | for populationhealth |     | management. | CQL        | is     | also incorporated | into |
| their levels | of maturity and adoption.      | Most | of the standards | de-      |                      |     |             |            |        |                   |      |
theelectronicversionofvariousCMSqualitymeasures35usingthe
scribedhavebeendevelopedinthelast5years,andsignificantwork
CQL-basedHealthQualityMeasureFormatstandard.36Atthepre-
| is still underway | focused on trialing, | fine tuning, | and expanding |     |     |     |     |     |     |     |     |
| ----------------- | -------------------- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
senttime,however,theadoptionofCQLhasbeenmuchgreaterin
thesestandards.Weprovidesubsequentlyasummaryofthecurrent
theclinicalqualitymeasurementdomainthanintheCDSdomain.
| stateof maturity | andadoptionofthesestandards, |     | withthecaveat |     |                |     |                   |     |      |                |         |
| ---------------- | ---------------------------- | --- | ------------- | --- | -------------- | --- | ----------------- | --- | ---- | -------------- | ------- |
|                  |                              |     |               |     | We are unaware |     | of any commercial |     | EHRs | that currently | support |
thatthecurrentstateischangingveryrapidly.Wedirectinterested
|     |     |     |     |     | CQL for | real-time, | patient-specific, |     | locally | developed | CDS that is |
| --- | --- | --- | --- | --- | ------- | ---------- | ----------------- | --- | ------- | --------- | ----------- |
readerstotheHL7Confluencewebpage(https://confluence.hl7.org/
|     |     |     |     |     | outside of | the population | health | management |     | or quality | measure- |
| --- | --- | --- | --- | --- | ---------- | -------------- | ------ | ---------- | --- | ---------- | -------- |
display/CDS/Standards)forthelatestinformationoneachofthese
mentdomains.
standards.
|     |     |     |     |     | The Clinical |     | Reasoning, | SMART | on FHIR, | and | CDS Hooks |
| --- | --- | --- | --- | --- | ------------ | --- | ---------- | ----- | -------- | --- | --------- |
Ofthevariousstandardsdiscussedinthisarticle,theArdenSyn-
standardsareallStandardsforTrialUse,whichmeansthattheyare
taxisthemostmature.IthasbeenanormativeHL7standardforal-
lessmaturethannormativestandards.Weareawareofseveralcom-
most30years.Whileitisbeyondthescopeofthisarticletodiscuss

1804 JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8
Figure6.Anelectronichealthrecord(EHR)systemmayoptionallychoosetoimplementclinicaldecisionsupport(CDS)locallyusingeitherArdenSyntaxorClini-
calReasoning/ClinicalQualityLanguage(CQL)artifacts(knowledgetransferstandards).UsersmaychoosetolaunchaSMARTonFHIRappfromtheEHR.The
SMARTonFHIRappmayoptionallychoosetouseClinicalReasoning/CQLorCDSHooksaspartofitsbusinesslogic.TheEHRmaychoosetoinvokeaCDS
Hooksserviceanddisplaytheresponsecard(s)totheuser.TheCDSHooksserviceprovidermayoptionallychoosetouseClinicalReasoning/CQLtorepresentits
businesslogic.Forexample,aHAPIFastHealthcareInteroperabilityResources(FHIR)ServercanuseFHIRLibraryresourcestostore,load,andevaluatethecon-
tentsofCQLlibrariescontainingthebusinesslogic,aswellastheFHIRPlanDefinitionresourcesrepresentingthestructureofthedecisionsupportrules.SMART
onFHIRandCDSHooksareexamplesofknowledgeaccessstandards.
mercial EHRsystems thatsupportthe SMARTon FHIR standard effectively.Wealsoanticipateexpandedsupportforabroadersetof
and offer catalogs of SMART on FHIR applications in their “app FHIR profiles, both with read and write capabilities. This process
stores.” The number of SMART on FHIR apps currently on the maybeaccelerated byfuturegovernment regulatoryrequirements,
marketappearstobeinthehundreds.TheuseofFHIRandSMART whichwouldexpanduponexistingrequirementsinthe21stCentury
Act12
on FHIR within these apps is relatively mature when it comes to Cures to support SMART on FHIR for provider-facing and
readingdatafromEHRs,especiallyforFHIRresourcesthatarein- patient-facingappsusingdataelementsintheUSCoreFHIRspecifi-
cluded in the US Core profile,37 but it is considerably less mature cation.Weexpecttheregulatoryfocustomovefromread-onlyac-
when it comes to writing data back to EHRs. We are aware of cesstoEHRdatatoincluderead-writecapabilities.
| several                                               | commercial |     | EHRs that | currently | support | CDSHooks. | The |            |     |     |     |     |
| ----------------------------------------------------- | ---------- | --- | --------- | --------- | ------- | --------- | --- | ---------- | --- | --- | --- | --- |
| momentumbehindCDSHooksseemstobestrong,withsignificant |            |     |           |           |         |           |     | CONCLUSION |     |     |     |     |
engagementfromEHRcompanies,whichareleadingthestandards
After3decadesofdevelopmentsinCDSstandards,thecurrentset
developmentprocessfortheCDSHooksspecification.ClinicalRea-
|        |            |                |            |           |            |                 |            | of FHIR-based | CDS standards,      | coupled with | U.S.      | regulatory |
| ------ | ---------- | -------------- | ---------- | --------- | ---------- | --------------- | ---------- | ------------- | ------------------- | ------------ | --------- | ---------- |
| soning | has        | been used      | in various | guideline |            | pilot projects, | including  |               |                     |              |           |            |
|        |            |                |            |           |            |                 |            | requirements  | for the use of FHIR | R4, has the  | potential | to enable  |
| for    | CDC opioid | prescribing,38 |            | U.S.      | Preventive | Services        | Task Force |               |                     |              |           |            |
screening39 widespread adoption of CDS at scale. Longstanding challenges of
| lung | cancer |     | and | World | Health | Organization | antenatal |     |     |     |     |     |
| ---- | ------ | --- | --- | ----- | ------ | ------------ | --------- | --- | --- | --- | --- | --- |
care40 healthcare care variability, healthcare quality, and patient safety
|     | guidelines. |     | However, | we are | unaware | of any | commercial |     |     |     |     |     |
| --- | ----------- | --- | -------- | ------ | ------- | ------ | ---------- | --- | --- | --- | --- | --- |
mayfinallybeaddressed.
EHRsthatcancurrentlyprocessPlanDefinitionFHIRresourcesina
plug-and-playmanner.
|     | Future | work is | anticipated | to include |     | standards | development, | FUNDING |     |     |     |     |
| --- | ------ | ------- | ----------- | ---------- | --- | --------- | ------------ | ------- | --- | --- | --- | --- |
health information technology software implementation, and gov- RAJ was supported by National Institute of Minority Health Disparities
ernmentregulation.Onthestandardsdevelopmentside,ArdenV3.0 grantsU54MD007598andS21MD000103andNationalCenterforAdvanc-
willincorporateFHIRtosolvethecurlybracesproblem.Ongoing ingTranslationalSciencesgrantUL1TR001881fromtheU.S.NationalInsti-
workonCDSHooksiscoveringareassuchasnewhookdefinitions tutesofHealth.KKandGDFweresupportedbyNationalCancerInstitute
forvariousworkflowtriggerpoints,securitybestpractices,CDSre- grantsU24CA204800andU01CA232826andbyAgencyforHealthcareRe-
searchandQualitygrantR18HS026198.Somestandardsandcontentdevel-
| sponse | analytics, | and | interoperable |     | suggestions | such | as for recom- |     |     |     |     |     |
| ------ | ---------- | --- | ------------- | --- | ----------- | ---- | ------------- | --- | --- | --- | --- | --- |
opmentreferencedinthisarticlewerefundedbyTheOfficeoftheNational
mendedprescriptions.WithintheSMARTonFHIRcategory,anew
|           |     |          |          |           |        |       |          | Coordinator | for Health Information | Technology, | contract | numbers |
| --------- | --- | -------- | -------- | --------- | ------ | ----- | -------- | ----------- | ---------------------- | ----------- | -------- | ------- |
| companion |     | standard | is being | developed | called | SMART | Web Mes- |             |                        |             |          |         |
HHSP233201800320G,HHSP233201700044C,andD15PD00739.
saging.41ThisstandardwillallowSMARTonFHIRappstocom-
municatewiththeparentEHRapplicationsfromwhichtheywere
AUTHORCONTRIBUTIONS
| launched, |     | thereby | enabling | orders | and other | actions | that happen |     |     |     |     |     |
| --------- | --- | ------- | -------- | ------ | --------- | ------- | ----------- | --- | --- | --- | --- | --- |
withinanapptobecommunicatedbacktotheparentEHR.Onthe Alltheauthorsmadesubstantialcontributionstotheconception,writing,and
healthinformationtechnologyimplementationside,weexpectmore editingofthemanuscript.
andmoreEHRstobuildsupportforthesestandardsintotheirsoft-
ware,andweexpectotherhealthinformationtechnologycompanies ACKNOWLEDGMENTS
toofferproductsandsolutionsusingthesenewstandards.Somein- HRS,BR,GDF,RAJ,andKKareco-chairsoftheHL7ClinicalDecisionSup-
vestmentwilllikelyberequiredonthepartofhealthsystemstore- portWorkGroup,andRAJandPHareco-chairsoftheHL7ArdenSyntax
| cruit | and train | the | requisite | talent | to use | these new | technologies | WorkGroup. |     |     |     |     |
| ----- | --------- | --- | --------- | ------ | ------ | --------- | ------------ | ---------- | --- | --- | --- | --- |

JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8 1805
CONFLICTOFINTERESTSTATEMENT 14. JendersRA,AdlassnigK-P,FehreK,HaugP.EvolutionoftheArdenSyn-
|            |                        |           |           |            |        | tax: key technical | issues | from | the standards | development |     | organization |
| ---------- | ---------------------- | --------- | --------- | ---------- | ------ | ------------------ | ------ | ---- | ------------- | ----------- | --- | ------------ |
| KK reports | honoraria, consulting, | sponsored | research, | licensing, | or co- |                    |        |      |               |             |     |              |
perspective.ArtifIntellMed2018;92:10–4.
developmentinthepast3yearswithMcKessonInterQual,Hitachi,Pfizer,
|     |     |     |     |     |     | 15. HL7 International. | Clinical | Quality | Language | Release | 1   | STU 4 (1.4). |
| --- | --- | --- | --- | --- | --- | ---------------------- | -------- | ------- | -------- | ------- | --- | ------------ |
Premier,KlesisHealthcare,RTIInternational,MayoClinic,theUniversityof
|     |     |     |     |     |     | https://cql.hl7.org/STU4/02-authorsguide.html. |     |     |     | Accessed |     | August 26, |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | -------- | --- | ---------- |
Washington,theUniversityofCalifornia,SanFrancisco,MDAware,andthe
2020.
U.S.OfficeoftheNationalCoordinatorforHealthInformationTechnology
16. HL7International.ChlamydiascreeningCDS.https://cql.hl7.org/exam-
(viaEnterpriseScienceandComputing[ESAC]andSecurityRiskSolutions)
ples/ChlamydiaScreening_CDS.cql.AccessedAugust26,2020.
intheareaofhealthinformationtechnology.KKwasalsoanunpaidboard
17. NationalLibraryofMedicine.ValueSetAuthorityCenter.https://vsac.
| member of | HL7, he is an unpaid | member | of the | U.S. Health | Information |     |     |     |     |     |     |     |
| --------- | -------------------- | ------ | ------ | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
nlm.nih.gov/.AccessedSeptember3,2020.
| Technology | Advisory Committee, | and he | has helped | develop | a number of |     |     |     |     |     |     |     |
| ---------- | ------------------- | ------ | ---------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
18. HL7International.Plandefinition-chlamydia-screening-intervention.json.
healthinformationtechnologytools,whichmaybecommercializedtoenable
http://www.hl7.org/fhir/plandefinition-chlamydia-screening-intervention.
widerimpact.BRreportshonoraria,consulting,sponsoredresearch,licens-
json.html.AccessedAugust26,2020.
ing,orco-developmentinthepast3yearswiththeOfficeoftheNationalCo-
|               |                              |     |       |             |          | 19. HL7 International. | FHIR | Clinical | Guidelines | (v0.1.0) | (STU1 | Ballot). |
| ------------- | ---------------------------- | --- | ----- | ----------- | -------- | ---------------------- | ---- | -------- | ---------- | -------- | ----- | -------- |
| ordinator for | Health InformationTechnology |     | (ONC) | (via ESAC), | the U.S. |                        |      |          |            |          |       |          |
http://hl7.org/fhir/uv/cpg/2019Sep/.AccessedJanuary1,2021.
CentersforMedicareandMedicaidServices(viaESAC),theU.S.Centersfor
20. MandlKD,MandelJC,MurphySN,etal.TheSMARTPlatform:early
DiseaseControlandPrevention(viaESACandSecurityRiskSolutions),the
|     |     |     |     |     |     | experience enabling |     | substitutable | applications |     | for electronic | health |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------- | ------------ | --- | -------------- | ------ |
WorldHealthOrganization,theAgencyforHealthcareResearchandQuality
records.JAmMedInformAssoc2012;19(4):597–603.
(viaRTIInternational),OregonHealthSciencesUniversity,McKesson,the
21. HL7International.SMARTAppLaunchFramework.http://hl7.org/fhir/
| National Committee | for Quality | Assurance, | University | of  | Utah, Cerner, |     |     |     |     |     |     |     |
| ------------------ | ----------- | ---------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
smart-app-launch/1.0.0/.AccessedAugust28,2020.
Optum,PointofCarePartners,Apervita,andMCG.
22. MandelJC,KredaDA,MandlKD,KohaneIS,RamoniRB.SMARTon
|     |     |     |     |     |     | FHIR: a standards-based, |     | interoperable |     | apps platform | for | electronic |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | ------------- | --- | ------------- | --- | ---------- |
healthrecords.JAmMedInformAssoc2016;23(5):899–908.
DATAAVAILABILITYSTATEMENT 23. CurranRL,KukharevaPV,TaftT,etal.Integrateddisplaystoimprove
chronicdiseasemanagementinambulatorycare:ASMARTonFHIRap-
Nonewdataweregeneratedoranalyzedinsupportofthisresearch.
|     |     |     |     |     |     | plication informed | by  | mixed-methods | user | testing. | J Am | Med Inform |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------- | ---- | -------- | ---- | ---------- |
Assoc2020:27(8):1225–34.
24. KarhadeAV,SchwabJH,DelFiolG,KawamotoK.SMARTonFHIRin
REFERENCES
spine:integratingclinicalpredictionmodelsintoelectronichealthrecords
1. Hripcsak G. Arden Syntax for Medical Logic Modules. MD Comput forprecisionmedicineatthepointofcare.SpineJ2020Jun26[E-pub
| 1991;8(2):76–8. |     |     |     |     |     | aheadofprint.. |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
2. HL7International.ArdenSyntaxv2.10(HealthLevelSevenArdenSyntax 25. KukharevaP,WarnerP,RodriguezS,etal.Balancingfunctionalityversus
forMedicalLogicSystems,Version2.10).http://www.hl7.org/implement/ portabilityforSMARTonFHIRapplications:casestudyforaneonatal
standards/product_brief.cfm?product_id¼372. Accessed August 13, bilirubinmanagementapplication.AMIAAnnuSympProc2020;2019:
| 2020. |     |     |     |     |     | 562–71. |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
3. JohnsonPD,TuSW,MusenMA,PurvesI.Avirtualmedicalrecordfor 26. Metke-JimenezA,HarrapK,ConlanD,GibsonS,PearsonJ,HansenD.A
guideline-baseddecisionsupport.ProcAMIASymp2001:294–8. SMARTonFHIRprototypeforgenomictestordering.StudHealthTech-
4. HL7International.HL7Version3Standard:ClinicalDecisionSupport; nolInform2019;266:121–6.doi:10.3233/SHTI190783
VirtualMedicalRecord(vMR)LogicalModel,Release2.https://www. 27. Watkins M, Eilbeck K. FHIR Lab Reports: using SMART on FHIR
hl7.org/implement/standards/product_brief.cfm?product_id¼338. and CDS Hooks to increase the clinical utility of pharmacogenomic
AccessedNovember22,2020. laboratory test results. AMIA Jt Summits Transl Sci Proc 2020;
| 5. SordoM,OgunyemiO,BoxwalaAA,GreenesRA.GELLO:anobject- |     |     |     |     |     | 2020: 683–92. |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
oriented query and expression language for clinical decision support. 28. SinhaS,JensenM,MullinS,ElkinPL.Safeopioidprescription:aSMART
AMIAAnnuSympProc2003;2003:1012. onFHIRapproachtoclinicaldecisionsupport.OnlineJPublicHealthIn-
6. HL7International.HL7Version3Standard:GELLO,ACommonEx- form2017;9(2):e193.
pressionLanguage,Release2.http://www.hl7.org/implement/standards/ 29. HL7International.SMARTAppLaunch:ScopesandLaunchContext.
product_brief.cfm?product_id¼5.AccessedAugust13,2020. http://hl7.org/fhir/smart-app-launch/1.0.0/scopes-and-launch-context/in-
7. Peleg M, Boxwala AA, Ogunyemi O, et al. GLIF3: the evolution of a dex.html.AccessedSeptember2,2020
guidelinerepresentationformat.ProcAMIASymp2000:645–9. 30. HL7International.CDSHooks.https://cds-hooks.hl7.org/.AccessedSep-
| 8. HL7 International. | HL7 | Standard: | Clinical Decision | Support | Knowl- | tember2,2020. |     |     |     |     |     |     |
| --------------------- | --- | --------- | ----------------- | ------- | ------ | ------------- | --- | --- | --- | --- | --- | --- |
edge Artifact Specification, Release 1.3. http://www.hl7.org/imple- 31. HL7 International. (DRAFT) Potential Drug-Drug Interaction (PDDI)
ment/standards/product_brief.cfm?product_id¼337. Accessed August CDSIG:BallotforComment2.http://hl7.org/fhir/uv/pddi/2020SEP/in-
| 13, 2020. |     |     |     |     |     | dex.html.AccessedSeptember2,2020. |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
9. HL7International.HL7Cross-ParadigmSpecification:ClinicalQuality 32. CDSHooksforPAMA.https://argonautproject.github.io/cds-hooks-for-
Language, Release 1.http://www.hl7.org/implement/standards/product_ pama/.AccessedSeptember2,2020.
brief.cfm?product_id¼400.AccessedAugust25,2020. 33. DelFG,KohlmannW,BradshawRL,etal.Standards-basedclinicaldeci-
10. HL7International.DSTUupdates.http://hl7.org/fhir/DSTU1/.Accessed sionsupportplatformtomanagepatientswhomeetguideline-basedcrite-
August25,2020. ria for genetic evaluation of familial cancer. JCO Clin Cancer Inform
| 11. HL7 International.Welcome |     | to FHIR. | http://hl7.org/fhir/R4/. |     | Accessed | 2020;4:1–9. |     |     |     |     |     |     |
| ----------------------------- | --- | -------- | ------------------------ | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
August25,2020. 34. CDS Hooks patient-view. https://cds-hooks.org/hooks/patient-view/.
12. 21st Century Cures Act: Interoperability, information blocking, and AccessedSeptember2,2020.
the ONC Health IT Certification Program. Fed Regist 2020; 85: 35. eCQMs.https://ecqi.healthit.gov/ecqms.AccessedFebruary14,2021.
25642–961. 36. HL7 International. http://www.hl7.org/implement/standards/product_
13. Jung CY, Sward KA, Haug PJ. Executing medical logic modules brief.cfm?product_id¼405.AccessedFebruary14,2021.
expressedinArdenMLusingDrools.JAmMedInformAssoc2012;19 37. HL7International.https://www.hl7.org/fhir/us/core/.AccessedMarch1,
| (4):533–6. |     |     |     |     |     | 2021. |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |

1806 JournaloftheAmericanMedicalInformaticsAssociation,2021,Vol.28,No.8
38. OpioidPrescribingSupportImplementationGuide.http://build.fhir.org/ 40. WHOAntenatalCareGuidelineImplementationGuide.http://build.fhir.
ig/cqframework/opioid-cds/.AccessedFebruary14,2021. org/ig/who-int/anc-cds/.AccessedMarch1,2021.
39. USPSTFLungCancerScreeningImplementationGuide.http://build.fhir. 41. SMARTWebMessagingImplementationGuide.https://build.fhir.org/ig/
org/ig/cqframework/lcs-cds/.AccessedMarch1,2021. HL7/smart-web-messaging/.AccessedFebruary14,2021.
