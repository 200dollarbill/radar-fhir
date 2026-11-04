PLOS ONE
RESEARCHARTICLE
Towards effective clinical decision support
systems: A systematic review
FranciniHakID*,TiagoGuimarãesID,ManuelSantosID
AlgoritmiResearchCenter,UniversityofMinho,Braga,Portugal
*francini.hak@algoritmi.uminho.pt
a1111111111 Abstract
a1111111111
a1111111111
a1111111111
a1111111111
Background
ClinicalDecisionSupportSystems(CDSS)areusedtoassistthedecision-makingprocess
inthehealthcarefield.DevelopinganeffectiveCDSSisanarduoustaskthatcantake
advantagefrompriorassessmentofthemostpromisingtheories,techniquesandmethods
OPENACCESS
usedatthepresenttime.
Citation:HakF,GuimarãesT,SantosM(2022)
Towardseffectiveclinicaldecisionsupport
systems:Asystematicreview.PLoSONE17(8):
Objective
e0272846.https://doi.org/10.1371/journal.
pone.0272846
ToidentifythefeaturesofClinicalDecisionSupportSystemsandprovideananalysisof
Editor:GabrieleOliva,UniversityCampusBio- theireffectiveness.Thus,tworesearchquestionswereformulated:RQ1—Whatarethe
MedicoofRome,ITALY
mostcommontrendcharacteristicsinaCDSS?RQ2—Whatisthematuritylevelofthe
Received:December6,2020 CDSSbasedonthedecision-makingtheoryproposedbySimon?
Accepted:July27,2022
Published:August15,2022
Methods
PeerReviewHistory:PLOSrecognizesthe
AISe-library,DecisionSupportSystemsjournal,Nature,PlosOneandPubMedwere
benefitsoftransparencyinthepeerreview
process;therefore,weenablethepublicationof selectedasinformationsourcestoconductthissystematicliteraturereview.Studiesfrom
allofthecontentofpeerreviewandauthor 2000to2020werechosencoveringsearchtermsinCDSS,selectedaccordingtodefined
responsesalongsidefinal,publishedarticles.The
eligibilitycriteria.Thedatawereextractedandmanagedinaworksheet,basedonthe
editorialhistoryofthisarticleisavailablehere:
https://doi.org/10.1371/journal.pone.0272846 definedcriteria.PRISMAstatementswereusedtoreportthesystematicreview.
Copyright:©2022Haketal.Thisisanopenaccess
articledistributedunderthetermsoftheCreative
Results
CommonsAttributionLicense,whichpermits
unrestricteduse,distribution,andreproductionin
Theoutcomesshowedthatrule-basedmodulewasthemostusedapproachregarding
anymedium,providedtheoriginalauthorand
knowledgemanagementandrepresentation.Themostcommontechnologicalfeature
sourcearecredited.
adoptedbytheCDSSweretherecommendationsandsuggestions.19,23%ofstudies
DataAvailabilityStatement:Allrelevantdataare
adoptthetypeofsystemasaweb-basedapplication,and51,92%arestandaloneCDSS.
withinthemanuscriptanditsSupporting
informationfiles. Temporalevolutionwasalsopossibletovisualize.Thisstudycontributedtothedevelop-
mentofaMaturityStagingModel,whereitwaspossibletoverifythatmostCDSSdonot
Funding:ThisstudywassupportedbyFCT–
Fundac¸ãoparaaCiênciaeTecnologia,withinthe exceedlevel2ofmaturity.
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 1/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
scopeoftheprojectDSAIPA/DS/0084/2018,FH Conclusion
workwassupportedbythegrant2021.06230.BD.
ThetrendcharacteristicsaddressedintherevisedCDSSwereidentified,comparedtothe
Thefundershadnoroleinstudydesign,data
collectionandanalysis,decisiontopublish,or fourpredefinedgroups.AmaturitystagemodelwasdevelopedbasedonSimon’sdecision-
preparationofthemanuscript. makingtheory,allowingtoassessthelevelofmaturityofthemostcommonfeaturesofthe
Competinginterests:Theauthorshavedeclared CDSS.Withtheapplicationofthemodel,itwasnoticedthatthephasesofchoiceandimple-
thatnocompetinginterestsexist. mentationareunderrepresented.Thisconstitutesthemaingapinthedevelopmentofan
effectiveCDSS.
Introduction
Intheday-to-dayroutineofhealthcareunits,thedomainprofessionalsinteractwithhundreds
ofpatients.Naturally,itisofgreatimportancethatallthisinteractionistransformedintorec-
ords,whetherclinicaloradministrative,whichinturnaretransformedintodata,information,
and,hopefully,knowledge.Despitetechnologicaldevelopments,theserecordsarestillkeptin
physicalformat,whichcreatesadelayintheworkperformedwhencomparedtodigitalver-
sions[1].
Friedman[2]boastedatheoreminwhichitshowsthatanindividualorgroupworking
withthecontributionofatechnologicalresourceofinformation,hasabetterperformance
comparedtoajobwithoutsuchassistance.Forthisfunctionaltheoremtobeverified,the
informationresourcesmustbevalidandreliableandtheusermustknowhowtohandleit
properly.
TheelectronicrepresentationofclinicalrecordsareembodiedbyElectronicHealthRec-
ords(EHR),whichaim,inparticular,toeliminatetheuseofpaperinthehealthcarefield.Not-
withstanding,therepresentationofelectronichealthdatatendstobemorethanjusta
substituteforpaper[1].HIMSS[3]showsthatahealthcareinformationsystemmusthavethe
abilitytogenerateacompleteviewoftheclinicalrecordatameetingwithapatient,including
decisionevidence-basedsupport,qualitymanagementandresultsreporting,apartfromthe
supportofotheractivitiesrelatedtodirectorindirectcarebymeansofasharedarea.Thereby,
itisevidentthatforahealthcareinformationsystemtobeeffective,itiscrucialtheexistenceof
anintegratedcomponentofsupportindecision-makingprocesses.
TheconceptofDecisionSupport(DS)isequivalenttotheactivitythatassistsagivenuser
followingacertainpurpose.Thus,aDecisionSupportSystem(DSS)turnsthisactivityintoa
system-basedformatinanefficientandreliableway,composingmodelsandtechniques
throughaknowledgerepresentationinfrastructure[4].Inthissense,aDSSportraysasystem
designedtosupportaprofessionalinobtainingknowledgeandmakingdecisionsinthespe-
cificarea,therefore,diminishinguncertaintiesduringthedecision-makingprocess[5].
Inthehealthcarefield,thedecision-makingsupportactivityisdesignedasClinicalDecision
Support(CDS).Therepresentationofthisactivityinacomputerized-basedformatistrans-
latedintoaClinicalDecisionSupportSystem(CDSS),whereitprovidesalltheinformation
anddesiredknowledgethatfacilitatethedailytasksofhealthcareprovidersandguaranteean
improvementinthequalityofservices.
Asaclinicalknowledge-basedsystem,thetreatmentofinformationandtheprocessof
knowledgeextractionareconsiderableaspectsforaClinicalDecisionSupportSystemto
achieveitsobjectives.SomefeaturesaremandatoryinaCDSS,butnotallareknownand
somemaybemissedandcontributetosystemfailures[6].
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 2/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
AccordingtoSimon,thedecision-makingprocessistheheartofanyorganizationandit
influencesallprocessesintegratedintoit[7].Thedecision-makingprocesscanbeoutlined
usingvariousmodelsandtheorems.Withinthescopeofthisstudy,theBoundedRationality
theorywasadoptedasareferencetoHerbertSimon’swork[8].Itisstatedthatpeopleactina
rationalwayaccordingtotheknowledgeandperceptionthattheyget.Inaninitialphase,this
modelapproachedthreestages:Intelligence,DesignandChoice.Lateron,anewstagewas
addedbySpragueandCarlson[9],resultingintheimplementationphase.Thus,thefour
phasesresultedbySimon’swork[8],redoundtomodeldecisionmakingprocessofanIntelli-
gentDecisionSupportSystem.
Previoussystematicreviewstudies(SRs)haveaddressedtheuseofaClinicalDecisionSup-
portSystemtoassessitsuseandeffectiveness[10–12],butappliedtoaspecificworkflow.
Instead,thissystematicreviewaimstoanalyseasetofarticlesthataddressaCDSSinorderto
identifythetrendsofthecharacteristicsforitsconception.Inaddition,wealsoidentifyother
aspectssuchasthepurposeofcareandtherecipientoftheintervention.Furthermore,in
ordertoenrichtheoutcomesobtainedfromthereview,wetraceageneraltrendofaCDSS,
relatingitwiththefourphasesproposedbySimon.
Thisarticleisstructuredinfoursections.First,anintroductiontothetopicofstudyispre-
sented.Secondly,thelandscapeofthemethodsusedtomaketheSystematicReview.Thethird
sectionpresentstheresultsoftheSystematicReview.Thefourthsectionisdedicatedtodis-
cussingtheresultsobtained.Atlast,insectionfive,conclusionsaredrawnwhileleavingopen
doorsforfuturework.
Decision-makingtheory
Decision-makingisoneofthemainprocessesdealtwithinanorganization[13].Thisprocess
canbeapproachedusingdifferentmodelsandtheories.Inthepresentstudy,thebounded
rationalitytheoryproposedbySimonwillbefocused.
HerbertSimon[8]wasaneconomistwhocarriedoutresearchinvolvingseveralareas,such
aspsychology,computingandmanagement.OneofSimon’sgreatcontributionstoscientific
researchwasthetheoryofboundedrationality,whereSimonredefineshumanrationality
arguingthatpeopleactrationallyaccordingtotheknowledgeandperceptiontheyobtain.To
formalizehistheory,Simonestablishedfourphasesthatdefinethedecision-makingprocess,
asshowninFig1.
InIntelligencephase,problemsareidentifiedandthepurposeofactioninvolvingthedeci-
sionisdetermined.IntheDesignphase,possiblesolutionsaredesignedandalternativesare
createdtosolvetheproblem.Consequently,intheChoicephase,thealternativethatmostsat-
isfiesthepurposeofactionwillbechosen.Yearslater,Turban[14]wasresponsibleforrefor-
mulatingSimon’stheorybyaddingafourthphaseinordertoassesstheimplementation
process.Thus,theImplementationphaseresultsfromthejoiningofthethreepreviousphases
Fig1.Iterativephasesofthedecision-makingprocess.
https://doi.org/10.1371/journal.pone.0272846.g001
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 3/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
putintopractice.Itshouldbenotedthatthedecision-makingisasequentialanditerativepro-
cess,whichrequiresthecompletionofallphasestoreachthefinalphaseandanongoing
reviewofthesame.
• Intelligence—Processofformalizationoftheproblemanddefinitionofdecisionconditions.
Thedecisionstobemadewiththehelpoftheproposedsystemandthebenefitsitwillbring
arestillunclearandnotunderstood.Inthisphase,realityisexaminedinordertomodelthe
existinginformationfordecomposingtheproblemanddeterminingitsproperties.Theintel-
ligencephaseendswithaproblemstatement.
• Design—Atthisstageitisnecessarytohavetheproblemdefinedtosearchforalternativesor
availableoptions,wherepossiblecoursesofactionareanalysedandvalidated.Problem-situ-
ationmodelsarebuilttoexplorealternativesolutions.Forthis,itisnecessarytohavewell-
definedanddeclaredselectioncriteriaasaresultfortheevaluationofpotentialsolutions
thatwillbeidentified(includestechniques,technologies,format,integration,functionalities,
etc).Severalpossibleoutcomescanbeconsideredforeachalternative,eachwithacertain
probabilityofoccurrence.Incaseswheredecisionsaremadewithuncertainty,thereare
multipleoutcomesforeachalternative.
• Choice—Inthechoicephase,allalternativesareresearched,evaluated,andoneisdefinedas
therecommendedsolution.Inpursuitofgoals,acourseofactionthatisgoodenoughis
selected.Computermodelsorcriticalsuccessfactorscanbeusedastechniquestoevaluate
therecommendedsolution.Normativemodelscanuseeithertheanalyticalmodeloran
exhaustiveandcompleteenumerationmodel.Thesolutionistestedandoncetheproposed
solutionappearsviable,adecisioncanbemade.
• Implementation—Thisphaseisthevalidationofallpreviousphases.Iftheadoptedsolution
seemsgoodenough,itcanbeimplemented.Successfulimplementationresultsinsolvingthe
originalproblem.Incaseoffailure,itmustbereturnedtothepreviousphases.
Methods
ThesystematicreviewwasconductedbasedonPreferredReportingItemsforSystematic
ReviewsandMeta-Analysis(PRISMA)statements[15],followedbyachecklistandaflow
diagram.
Informationsources
Fiveonlinedatasourcesrelatedtoresearchinhealthinformationsystemswereselected.First,
asearchwasperformedonScimago[16]comprisingtwoareasofstudy:informationsystems
andmultidisciplinary.Fromthis,journalswithQ1quartileinthelast5yearsandwithan
impactfactorgreaterthan150wereanalysed.Journalsthathadthepotentialtohavearticles
morerelatedtothepurposeofthisstudyandthatwerealreadyknownbytheauthorswere
selected:DecisionSupportSystems,NatureResearchJournalandPlosOne.Tocomplement
thestudy,twopublicrepositorieswerechosen,suchas:thePubMedlibrary(medline)andthe
AssociationofInformationSystems(AIS)e-library.TheTable1showsinformationaboutthe
selecteddatasourcetypes.
Eligibilitycriteriaandsearchstrategy
Toselectthestudiesforthedevelopmentofthesystematicreview,eligibilitycriteriawere
defined:(i)publishedstudiesinarticleformat;(ii)openaccessorfreefulltext;(iii)writtenin
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 4/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
Table1.Informationofselecteddatasources.Source:ScimagoJournalandCountryRankviawww.scimagojr.com,accessedonMay13,2022.
DataSource PublicationType SubjectArea Quartile H-Index
AISe-library Repository InformationSystems - -
DecisionSupportSystems Journal InformationSystems Q1 161
Nature Journal Multidisciplinary Q1 1276
PlosOne Journal Multidisciplinary Q1 367
PubMed Repository Biomedical - -
https://doi.org/10.1371/journal.pone.0272846.t001
English;(iii)articlesaddressingadecisionsupportsystemsinhealthcare;(iv)computerizedor
electronicdecisionsupportsystems.Tomeetthesecriteria,searchfilterswereapplied.The
selectedarticlesmustaddresspracticalcasesofaspecificclinicaldecisionsupportsystem,
therefore,articlesoftheliteraturereviewtypeorthatdidnotaddressaparticularCDSsystem
wereexcluded.
Thesearchstrategywasperformedconsideringanorderingfromthemostrecentpublica-
tionstotheoldestones,restrictingtoarangefrom2000/01/01to2020/12/31.Toidentifystud-
iesofthedesiredscope,thequerytermswere:((everything:“ClinicalDecisionSupport
System”)OReverything:“ClinicalDecisionSupport”)OReverything:“DecisionSupportSys-
teminHealthcare”.Thetitle,abstractandkeywordsweretheprimarystrategyforanalyzing
eachscientificpublication.Whentheseparameterswerenotsufficient,acompletereadingof
eacharticlewasmade,inordertoguaranteetheeligibilityofinclusioncriteria.
Dataextractionandmanagement
Thescreeningprocesswascarriedoutbytwoauthors(FHandTG)independently,byreading
thetitles,abstractsandkeywordsofthepublicationsofthesearchresults.Whenthecriteria
weremet,thefulltextwasread.Inmomentsofdisagreementordoubt,thethirdreviewer
(MS)tookastandandcontributedtothediscussion.
Throughthereviewofeligiblearticles,dataextractionwasperformedbytworeviewers(FH
andTG)andfocusedonfourcharacteristicsofaCDSS,definedas:knowledgemanagement
andrepresentationtechnique;technologicalresourcesintegratedintothesystem;thetypeof
system;andsystemintegration.Thesefourcategorieswereconsideredbytheauthorsasthe
mostrelevantforthepurposeofthisstudy.Inaddition,thefollowinginformationwas
extracted:clinicalsetting,studydesign,recipientofintervention,andpurposeofcare.Data
extractionwasperformedthroughthetextualanalysisofthearticlesandthesearchforkey-
words.Forbettermanagementandanalysis,theextracteddatawererecordedonanappropri-
atesheet(seeS1File).
Toanswerthesecondresearchquestionofthisstudy,itwasidentifiedinwhichphaseofthe
decision-makingtheorytheCDSSofthereviewedarticleswasfound.Thus,basedonthelitera-
tureondecision-makingtheory[17,18]andthedefinitionsofeachphase,theauthorsconsid-
eredasetofcriteriafortheassignmentofeachphase,asshowninTable2.Forasystemtobe
classifiedinacertainphase,itmustfulfillatleastoneoftheconditionsindicated.
Qualityassessmentanddatasynthesis
AllthereviewedstudiesportrayaClinicalDecisionSupportSystem(CDSS)designedfora
specificpurpose.Thekeypointsforconductingthissystematicreviewweretoidentifythe
trendsoftheCDSSdevelopedregardingtheirtypeofsystem,integration,representationand
formulationofknowledge,andtheirtechnologicalfeatures.
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 5/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
Table2.ChoiceofcriteriasfortheclassificationofSimon’sphases.
Phase Condition1 Condition2 Condition3 Condition4
Intelligence Haveaccesstothehistory Abilitytopredictwhatmayhappento Havingstructuredandavailableinformation Allowaccesstodatato
ofpastdecisions. theclinicalsituation(e.g.withmachine capableofaccessingspecificclinical assesstheclinical
learninganddataminingmodels). informationforthecharacterizationofthe situationofpatients.
situation.
Design Definitionofclinical Abilitytodevelopandpresentalternative Useofmodelingtechniques/procedures. Useofmodelsorsetof
contextvariables. solutionstoaclinicalsituation. modelstolearnto
decide.
Choice Beabletosimulateand Choiceofbestalternativeas Applicationofcomputationalmodelstoensure -
evaluateeachofthe recommendedsolutionbasedonapplied theoperationofthechosensolution.
availablealternatives. criteriaormodels.
Implementation Applicationofthechosen Monitoringandevaluation. Datacollectionfrommonitoringand Beabletorecordpast
optioninareal evaluation. decisions.
environment.
Note:Theconditionspresentedareofdisjunction,thatis,atleastoneofthemmustbemetforthesystemtobeclassifiedinacertainphase.
https://doi.org/10.1371/journal.pone.0272846.t002
ThereportingqualitywasmadefollowingthePRISMAchecklist.Publicationsconsidered
eligiblefortheanalysiswereassessedforthemethodologicalquality,meetingtheinclusioncri-
teria,riskofbias,assumptionsandsimplifications,andclarifiedevidence-basedresults.The
reviewersdidnotapplyanymethodologicalassessmenttool.
Afterdefiningthefivedatasources,thereviewersselectedasetofpublicationswithinthe
scopeofClinicalDecisionSupportSystems,throughthesearchstrategyandtheinclusioncri-
teriapreviouslydefined.Theoutcomespresentedthroughtablesandnarrativesummarychar-
acterizethedifferentClinicalDecisionSupportSystemspresentedintheselectedstudies,in
ordertotraceaglobaltrend.Thedatafromthematchingresultswerepooledoutandevalu-
ated,basedonthetotalvalueofstudiesandtheprobabilityofoccurrence.Thereviewersnoted
thepresenceofclinicalandstatisticalheterogeneityamongthestudies.
Results
Studyselection
ThestudyselectionwascarriedoutfollowingthePRISMAstatement[15],usingachecklist
(seeS2File)andaflowdiagramrepresentedinFig2(S3File).768recordswereidentifiedby
searchingfivedatabasesconsideredmostinfluentialforthepurpose.Afterremovingduplicate
records,690recordswerescreenedtoreadthetitle,abstractandkeywords.Lastly,thearticles
thatdidnotmeettheselectionandsearchcriteriawereexcluded,comprising:non-articlefor-
mat;unpublishedarticles;notinenglish;outofperiod;notopenaccess.Theselectedarticles
werereadinfulltoassesstheireligibility.Finally,52articlesmettheresearchquestionsand
wereelectedeligibleandappropriatetocarryoutthesystematicreview,embracingaspecific
ClinicalDecisionSupportSystemandnotliteraturereviewarticles.
Studycharacteristics
Thestudiesthatmettheinclusioncriteriawerecharacterizedaccordingtoasetofattributes.
Theperiodcoveredbetweenthestudieswasfrom2000to2020,with50%from2020,giving
prioritytothemostrecentones.
Thestudiesweresearchedinthefivepreviouslyselecteddatasources,witheighteenstudies
fromPubMed(34,62%),elevenstudiesfromDecisionSupportSystemsjournal(21,15%),ten
studiesfromPlosOne(19,23%),andfivestudiesfromNature(9,62%).Wenoteadiversityin
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 6/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
Fig2.Flowdiagramofstudyselectionforsystematicreview.
https://doi.org/10.1371/journal.pone.0272846.g002
thecountriesthatdevelopedthestudies,coveringfourdifferentcontinents.However,the
majoritystandouttotheUnitedStatesofAmerica,representingnineteenstudies(34,62%).
Studiesrealizedinanyhealthcaresettingwerethemostfrequentones(28,85%),followed
byhospitalsetting(21,15%)andhospitalacademiccenters(21,15%).Themostcommonrecip-
ientsoftheinterventionare,directly,generalpractitioners(32,69%).StudiesrevealthatCDSS
alsohasanactiononpatients,butmostly,indirectly.
Ingeneral,thestudydesignofthereviewsarticles,demonstratestheevaluationoftheeffec-
tivenessoftheCDSSregardingitscost,implementationandusability.Inaddition,thereview
showedthattheCDSSaddressedhaveanassociatedclinicalintervention,withthemostcom-
monpurposeofcarebeingaspecificworkflow(32,69%),followedbyaspecificpatientdisease
(15,09%).
Outcomes
Theinformationextractedfromthestudiesthatwereconsideredrelevantforthedesiredpur-
posegeneratedasetofoutcomes,basedonthecharacterizationofaClinicalDecisionSupport
System(CDSS).
Knowledgemanagement.Therepresentationandformulationoftheacquiredknowledge
isoneofthemostimportantstepsinthedevelopmentofaCDSS.Inordertoidentifythemost
usedtechniquesforknowledgemanagement,wehaveidentifiedtheapproachesusedinstudies
ofthesystematicreview,asshowninTable3.ClinicalPracticeGuidelines(38,46%),rule-
basedmodule(40,39%)andalgorithmiclogic(38,46%),werethemostusedapproachesto
knowledgemanagementinthedesigningofaCDSS.Thesetechniqueswereusedindividually
orincombinationwithothers.Theformulationofaknowledgebasewasalsoidentifiedin
thirteenstudies(25%),incombinationwithothertechniques.Inferenceengineswere
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 7/19

PLOS ONE
Towardseffectiveclinicaldecisionsupportsystems
Table3.Outcomesofknowledgerepresentationandmanagement.
| Study            | Outcome                    | Total(n) Value(%) |
| ---------------- | -------------------------- | ----------------- |
| [21–41]          | Rule-basedmodule           | 21 40,39%         |
| [21,22,30,40–56] | ClinicalPracticeGuidelines | 20 38,46%         |
[21,24,26,29,32–34,37,39,42–44,49,57–63] Algorithmiclogic 20 38,46%
[24,25,28,30,31,34,37,38,40,51,52,64,65] Knowledgebase 13 25%
| [28,35,52,57,60,66–68] | Variable-based                    | 8 15,39% |
| ---------------------- | --------------------------------- | -------- |
| [25,26,30,40,51–53]    | Inferenceengine                   | 7 13,46% |
| [27,31,68–70]          | StandardizedClinicalTerminologies | 5 9,62%  |
| [35,38,57]             | If/thenstatements                 | 3 5,77%  |
| [29,33,39]             | Dataminingtechniques              | 3 5,77%  |
| [48,57]                | Bayesiannetwork                   | 2 3,85%  |
| [67,68]                | Neuralnetworks                    | 2 3,85%  |
https://doi.org/10.1371/journal.pone.0272846.t003
identifiedinsevenstudies(13,46%),whichwerealsoconsideredinsomestudies,asreasoning
engines.Threestudies(5,77%)providedif/thenstatements,andeightstudies(15,39%)applied
methodsbasedonvariables.Terminologystandardsandclinicalclassificationsystemswere
presentinfivestudies(9,62%),applying,inparticular,theICD-10systemandtheHL7com-
municationprotocol.Bayesianandneuralnetworkswereusedintwodifferentarticles(3,85%
each).Finally,threestudies(5,77%)useddataminingtechniquestoreproducethedesired
knowledge.Twostudies[19,20]wereexcludedfrompooling,asthemethodusedinthe
knowledgerepresentationprocesswasnotidentified.
Technologicalfeatures.Technologicalinterventionsrepresentthefeaturesthatcontribute
tothesystemachievingitspurpose.Themostcommontechnologicalfeatureapproachedin
theCDSSisrecommendationandsuggestionfeature,identifiedintwentyfourstudies
(46,15%),asshowninTable4.Informationmanagementandmonitoringarethesecondmost
commonfeatureinthesystems,coveringeighteenstudies(46,15%).Thethirdmostdesired
featureisalerts,notificationsandreminders,coveringfourteenstudies(26,92%).Therefore,it
followsthepurposeofreducingerrorsasmentionedinelevenstudies(21,15%).Eightarticles
(15,38%)designtheCDSSforassessmentpurposes.Thepredictionfeatureisalsousedfor
Table4.Outcomesoftechnologicalfeatures.
| Study | Outcome | Total Value |
| ----- | ------- | ----------- |
(n) (%)
[20,22,25,29,30,36,38,40–42,46,47,50–55,57,60, Recommendationandsuggestion 24 46,15%
61,64,67,68]
[27,28,35,37,39,40,43,44,45,48,50,53,56,58,62, Informationmanagementand 18 34,62%
| 63,66,70] | monitoring |     |
| --------- | ---------- | --- |
[23,30–32,34,37,38,42,43,45,47,49,50,53] Alerts,notificationsandreminders 14 26,92%
| [19,21,32,37,38,43,48,50,51,68,69] | Errorreduction       | 11 21,15% |
| ---------------------------------- | -------------------- | --------- |
| [24,25,36,45,50,57,59,66]          | Assessment           | 8 15,38%  |
| [33,35,50,59,60,67,68,70]          | Prediction           | 8 15,38%  |
| [2732,36,46,53,61,65]              | Processautomationand | 7 13,46%  |
prioritization
| [31,34,48,65] | Events                | 4 7,69% |
| ------------- | --------------------- | ------- |
| [23,26,61,69] | Standardization       | 4 7,69% |
| [19,52,59]    | Calculationandscoring | 3 5,77% |
| [21,23]       | Costandtimereduction  | 2 3,84% |
https://doi.org/10.1371/journal.pone.0272846.t004
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 8/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
Table5.Outcomesofsystemintegration.
Study Outcome Total Value
(n) (%)
[20,24,25,29,31,35,36,40,41,42,44, StandaloneCDSS 27 51,92%
47,51–55,58–65,69,70]
[19,21,37,39,43,45,46,49,57,66,68] ElectronicHealthRecord(EHR) 11 21,15%
[26–28,30,33] SpecificHealthcareInformationSystem 5 9,62%
[23,34,38,48] ComputerizedProviderOrderEntry(CPOE) 4 7,69%
[22,32,56] ComputerizedProviderOrderEntry(CPOE)and 3 5,77%
ElectronicHealthRecord(EHR)
[50,67] ElectronicMedicalRecord(EMR) 2 3,84%
https://doi.org/10.1371/journal.pone.0272846.t005
eightstudiesfordifferentpurposes(15,38%).Theautomationandprioritizationofprocessesis
consideredtobeofgreatimportanceandisaddressedbysevenarticles(13,46%).Thetrigger-
ingofeventsisaddressedbyfourstudies(7,69%).Thestandardizationoftheclinicalprocessis
desiredbyfourstudies(7,69%).Threearticles(5,77%)highlightedthecalculationandscoring
methodsasfeaturesofaCDSS.Finally,thecostandtimereductionisseenasamainfeaturein
twostudies(3,84%).
Systemintegration.TheresultsrelatedtotheintegrationoftheClinicalDecisionSupport
System(CDSS),showedthat51,92%ofthearticles(twenty-seven)useastandalonesystem,as
showninTable5.TheremainingstudiesshowthattheirCDSSareintegratedwithanothersys-
tem,aswellasusingtheinformationfromthesesystems.Thus,elevenstudies(21,15%)reveal
thattheyintegratetheirCDSSwithanElectronicHealthRecord(EHR)system;fivestudies
(9,62%)integratetheirsystemwithaspecifichealthinformationsystem;fourstudies(7,69%)
integratewithaComputerizedProviderOrderEntry(CPOE)system;inthissequence,three
studies(5,77%)integratetheirCDSSwithbothEHRandCPOE;twostudiesdifferentiatetheir
integrationwithanElectronicMedicalRecord(EMR)system.
Typeofsystem.ThetypologyofaClinicalDecisionSupportSystem(CDSS)differsinsev-
eraltechnologicalaspects,consideringboththepresentationoftheuserinterfaceandthetech-
niqueitisbasedon.Thetypeofsystemsidentifiedinthereviewofstudiesisrepresentedin
Table6.Moststudies(19.23%)useaweb-basedapplicationtopresentthesysteminterfaceto
theuser.Ninestudies(17,31%)describetheirCDSSasacomputerizedtool,notspecifyingthe
typeofsoftwareorinterfaceused.Eightstudies(15,38%)developtheirdecisionsupportsystem
inasoftwareapplication.Regardingthelogicused,fivestudies(9,62%)arebasedonmachine
learningtechniques,andfourstudies(7,69%)areartificialintelligence-based.Threestudies
(5,77%)developtheirCDSSinamobileapplicationand,still,fourstudies(7,69%)covera
mobileandwebapplication.Twostudies(3,85%)describetheirCDSSasknowledge-based,
andothertwostudies(3,85%)presenttheCDSSasdataanalytics.Othertypesofsystemswere
consideredinuniquestudies,suchascloudcomputing(1,92%),data-layerinfraestructure
(1,92%),imageretrievalexpertsystem(1,92%),userinterface(1,92%),andwebapplication
integratedwithdataanalytic(1,92%).
TheoutcomesforeachgroupwerevariedregardingthetypeoftheCDSS,knowledgeman-
agement,integrationofsystemsandthetechnologicalfeatures.Despitethisdiversity,wewere
abletonoticeatrendinresultsbasedontheirfrequentpresenceinthereviewedstudies.As
showninFig3,themostcommonknowledgerepresentationandmanagementtechniques
weretherule-basedmodule,clinicalpracticeguidelinesandalgorithmiclogic.Regardingto
thetechnologicalinterventionorfeature,thethreetoptrendswererecommendationand
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 9/19

PLOS ONE
Towardseffectiveclinicaldecisionsupportsystems
Table6.Outcomesoftypeofsystem.
| Study | Outcome | Total(n) Value(%) |
| ----- | ------- | ----------------- |
[22,25,30,46,47,49,50,51,65,66] Web-basedapplication 10 19,23%
[21,23,26,36,45,48,56,57,68] Specificcomputerizedtool 9 17,31%
| [19,27,35,37,42,54,62,64] | Softwareapplication                  | 8 15,38% |
| ------------------------- | ------------------------------------ | -------- |
| [32,39,58–60]             | Machinelearning-based                | 5 9,62%  |
| [20,33,52,70]             | Artificialintelligence-based         | 4 7,69%  |
| [34,44,53,69]             | Webandmobileapplication              | 4 7,69%  |
| [29,31,61]                | Mobileapplication                    | 3 5,77%  |
| [40,67]                   | DataAnalytics                        | 2 3,85%  |
| [41,55]                   | Knowledge-based                      | 2 3,85%  |
| [38]                      | Userinterface                        | 1 1,92%  |
| [63]                      | Cloudcomputing                       | 1 1,92%  |
| [24]                      | Data-layerinfrastructure             | 1 1,92%  |
| [28]                      | Imageretrievalexpertsystem           | 1 1,92%  |
| [43]                      | Web-basedapplicationanddataanalytics | 1 1,92%  |
https://doi.org/10.1371/journal.pone.0272846.t006
suggestion,informationmanagementandmonitoring,andalerts,notificationsandreminders.
StandaloneCDSSwerethemostcommonone,followingintegrationwithElectronicHealth-
careRecords(EHR)systemsandspecifichealthcareinformationsystems.Themostfrequent
typeofsystemwere,respectively,web-basedapplication,specificcomputerizedtool,andsoft-
wareapplication.Despitetheindividualresults,wealsonoticedatrendtowardsacombination
ofresults.Themostfrequentsequencerelatedtoknowledgemanagementwasthemixofalgo-
rithmiclogicwithclinicalpracticeguidelines.Fortechnologicalfeatures,themostcommon
combinationwasthejoiningofrecommendationandsuggestionwithalerts,notificationsand
reminders.
Temporalevolution
Fig4demonstratesthetemporalevolutionofknowledgemanagementandrepresentation
techniquesusedinstudies.Itispossibletoverifythatrule-basedmoduleandthealgorithmic
logichavebeenpresentsince2000untiltoday,mostly.Asforclinicalpracticeguidelines,on
theotherhand,provedtobeacurrentissueduetotheirpresencefrom2013to2020.Ingen-
eral,thecharacteristicsremaininexistenceovertime,withagreateroccurrencein2020dueto
thenumberofarticlesanalysedthatyear.Incontrast,thecharacteristicsoftheBayesiannet-
work,if/thenstatementsandneuralnetworkswereconsideredmorerecent,emergingfrom
2014.
Fig3.Characterizationofgeneraltrendsobtainedthroughthereview.
https://doi.org/10.1371/journal.pone.0272846.g003
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 10/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
Fig4.Temporalevolutionofknowledgemanagement.
https://doi.org/10.1371/journal.pone.0272846.g004
Fig5.Temporalevolutionofsystemintegration.
https://doi.org/10.1371/journal.pone.0272846.g005
AccordingtoFig5,wecanseethattheintegrationofstandaloneCDSShasbeenincreasing
inrecentyears.TheintegrationwithEHRsystems,oscillatedbetween2014to2020,standing
outalsointhelastyear.Specifichealthinformationsystemshavebeenintegratedintothe
CDSSfrom2000to2020,onaregularbasis.
AccordingtoFig6,thespecificcomputerizedtoolshavebeenpresentsincethebeginning
ofthetimeintervalandweremorepresentintheyear2020.Thesoftwareapplication,machine
learning-based,wasalreadypresent.Themobileapplicationremainedconstant.Web-based
applicationwasmoreprevalentin2013.
Fig6.Temporalevolutionoftypeofsystem.
https://doi.org/10.1371/journal.pone.0272846.g006
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 11/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
Fig7.TemporalevolutionofCDSSfeatures.
https://doi.org/10.1371/journal.pone.0272846.g007
AsshowedinFig7thealerts,notificationsandremindersandtheinformationmanage-
mentandmonitoringfeatureweremorepresentin2020,butalsopresentinsomeprevious
year.Therecommendationsandsuggestionsfeaturewaspresentfrom2003to2020.Standard-
izationwaspresentin2000andonlyreturnedin2020.Thecalculationandscoring,costand
timereductionandpredictionfeatureswereconsideredthemostrecentones.
Maturitystagingmodel
ForaCDSStobeconsideredeffective,ithastoreachtheprestigiouslevelofmaturity.Thus,it
isimportanttorecognizethedegreeofmaturityassociatedwiththecharacterizationofthe
CDSSs.Inordertocomplementthestudy,across-checkingwasmadewiththetrendscharac-
teristicsfacingthefourphasesofSimon’sdecision-makingtheory[8].Thus,fourstageswere
classifiedaimingtorepresentthelevelofmaturityofasystem,basedonSimon’sphases:
• Stage4:Implementation+Choice+Design+Intelligence
• Stage3:Choice+Design+Intelligence
• Stage2:Design+Intelligence
• Stage1:Intelligence
Table7representsthecrossingoftheSimon’sphaseswiththethreemostcommoncharac-
teristicsofeachgroup,inordertoassesstheirstageofmaturity.Thecolumnsreferringtothe
maturitystages,correspondtothenumberofarticlesoftherespectivecharacteristic,given
theirpresenceineachSimonphase.Itshouldbenotedthatthevaluesarecumulative,thatis,
forastagetobereached,itmustcontainthepreviousstage.Allstudiescorrespondingtoeach
characteristicarepresentintheinitialphaseofIntelligence.Maturityiscalculatedusingthe
weightedaverage(WAVG),whichshouldvarybetween1and4,correspondingtoeachstage.
Discussion
Mainfindings
ThisarticleaimedtodevelopasystematicreviewwithinthescopeofClinicalDecisionSupport
Systems(CDSS).Thefirstresearchquestion(RQ1)wastoidentifythetendencyofadopted
approachesinCDSSdevelopmentaddressedinthereviewedstudies,asshowninFig3.To
classifytherevisedstudies,informationaboutfourpredefinedgroupswereextracted:knowl-
edgemanagement,technologicalintervention,systemintegrationandtypeofsystem.
AlthoughthereareothercharacteristicsassociatedwithaCDSS,theauthorschosetoextract
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 12/19

PLOS ONE
Towardseffectiveclinicaldecisionsupportsystems
Table7.MaturityStagingModelappliedonthereviewedstudies.
| Characteristic | Stage1 | Stage2 | Stage3 | Stage4 | WAVG |
| -------------- | ------ | ------ | ------ | ------ | ---- |
KnowledgeRepresentation
| Rule-basedmodule           | 21  | 16  | 4   | 1   | 1.64 |
| -------------------------- | --- | --- | --- | --- | ---- |
| ClinicalPracticeGuidelines | 20  | 12  | 5   | 2   | 1.71 |
| AlgorithmicLogic           | 20  | 13  | 7   | 2   | 1.79 |
Features
| Recommendationandsuggestion        | 24  | 13  | 5   | 0   | 1.55 |
| ---------------------------------- | --- | --- | --- | --- | ---- |
| Informationmanagementandmonitoring | 18  | 9   | 7   | 1   | 1.74 |
| Alerts,notificationsandreminders   | 14  | 9   | 3   | 0   | 1.58 |
SystemIntegration
| StandaloneCDSS            | 27  | 16  | 6   | 1   | 1.62 |
| ------------------------- | --- | --- | --- | --- | ---- |
| ElectronicHealthRecords   | 11  | 6   | 3   | 1   | 1.71 |
| Specificinformationsystem | 5   | 4   | 1   | 0   | 1.6  |
TypeofSystem
| Web-basedapplication     | 10  | 8   | 2   | 0   | 1.6  |
| ------------------------ | --- | --- | --- | --- | ---- |
| Specificcomputerizedtool | 9   | 4   | 2   | 1   | 1.67 |
| Softwareapplication      | 8   | 6   | 1   | 0   | 1.53 |
https://doi.org/10.1371/journal.pone.0272846.t007
specificinformationthatgobeyondthemainobjectiveofaCDSS,whichistoassistthedeci-
sionmakerinthedecision-makingprocess.Theresultsshowedthatthemostusedtechniques
fortheknowledgerepresentationinthesystemsarethecreationofmodulesbasedonrules,
clinicalpracticeguidelinesandlogicalgorithms.Thetechnologicalfeaturesmostpresentin
CDSSarerecommendationandsuggestion,monitoringandinformationmanagement,and
alertsandreminders.Usually,CDSSareusedstandalone,followingtheintegrationwithElec-
tronicHealthSystemsoraspecificinformationsystem.Itwasalsoidentifiedthatthemost
commontypesofsystemsarewebapplications,specificcomputertools,andsoftware
applications.
Inordertoanswerthesecondresearchquestion(RQ2),apreliminaryclassificationduring
thereviewwascarriedoutidentifyingwhichphaseofthedecision-makingprocessmodelthe
CDSSwasin.AccordingtoSimon’sboundedrationalitytheory[8],itwasconsidered:Intelli-
gencephaseasresponsibleforanalysis,explorationanddescriptionoftheproblemtobefaced;
theDesignphaseasthedevelopmentandanalysisofpossiblesolutionstotheproblemathand;
intheChoicephase,themostappropriatesolutionischosentosolvetheproblem;theImple-
mentationseekstoapplythesolutiontotheprobleminquestion.
RegardingthematuritystagingmodelproposedinTable7,whenthestage4isachieved,
thesystemhasreacheditsprestigiouslevelofmaturity.However,thisisnotverifiedinthe
analysis.Theweightedaverage(WAVG)ofthecharacteristicsshowedverysimilarvalues,
meaningthattheCDSSofthereviewedstudiespredominatesinSimon’sIntelligenceand
Designphases,equivalenttostage2ofmaturity.Therecommendationandsuggestion(1.55)
andsoftwareapplication(1.53)characteristicshavethelowestvaluesnearlyreachingtheprevi-
ousphaseofIntelligence.Thealgorithmiclogiccharacteristicstandsoutthemostandshows
thatitisclosertoachievingtheupperstageofmaturity(stage3),meetingtheChoicephase.
ThereareothersystematicreviewsthatstudytheroleofCDSS.However,tothebestofour
knowledge,existingstudiesanalyseCDSSappliedtoaspecificclinicalcontextanddonoteval-
uateitseffectivenessasawhole(as[11,12,71]).Thepresentsystematicreviewselectedasetof
studiesthatapproachthedevelopmentofaCDSScharacterizingtheminordertotraceaglobal
trend,aswellasassesstheirlevelofmaturity.Inthissense,itwaspossibletoanalysetheCDSS
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 13/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
initscompleteness,coveringdifferentapproaches,techniquesandpurposesofuse.Themain
contributionofthisworkwastheproposedmaturitystagingmodel,thatallowedtoidentifya
gapbetweenthestate-of-artandthedesirablestageofmaturityinordertoprovideaneffective
CDSS.TheresultsshowedthattherevisedCDSSdonotgobeyondstage2,meaningthat
CDSSarenotsucceedinginthehealthcarearenaduetothelackofmaturity,i.e.,asCDSSare
notcapableofsupportingthechoiceofactionsinclinicalsettingsandarealsonotinvolvedin
theimplementationoftheseactions.
ThisstudyallowedtoraiseaconcerninthedevelopmentofCDSSandtoraiseawareness
thatlimitedsystemsarebeingcreatedandthatmaybefarfrombeingoptimized.Theprojec-
tionofthisstudyallowedustoportrayarealityofmanydecisionsupportsystemsinthehealth
area,demonstratingtheoppositeofwhatitshouldbe.Whenasystemreachesthemodel
implementationphase,itshouldbeclosertoreachingitsoptimizationandnotgoingbackto
thepreviousphases.Thisimmaturitymaybeduetoalackofunderstandingoftherealprob-
lem,difficultyinchoosingtheidealsolution,andfailuresinusabilitytests.Anin-depthanaly-
sismustbedonetodiscoverthemainconstraintsthatpreventtheinclusionofthedecision-
makingphasesintheCDSS.
Limitationsandfutureresearch
Thematuritystagingmodel,combinedwiththephasesofthedecision-makingprocess,serves
toassesstheeffectivenessofthedecision.Whenanimplementeddecisiondoesnotproduce
thedesiredresults,therearelikelytobeseveralcauses,suchasincorrectproblemdefinition,
poorevaluationofalternatives,orinadequateimplementation[18].Theproposedalternative
maynotbesuccessful,whichwillleadtoanewanalysisoftheproblem,evaluationofalterna-
tivesandselectionofanewalternative.Thus,evaluationisakeyfactorintheprocessbecause
decision-makingisacontinuousandnever-endingprocess.
Somelimitationsshouldbestressed.First,wewereunabletoperformameta-analysisdue
tothevariationinthetypeofstudiesanalysed,aswellastouseaqualityassessmentmethodol-
ogytoassessthequalityofstudies.Thesamplenumberofeligiblestudieswasalsolimited.
AnotherlimitationwasregardingthecharacterizationoftheCDSS,duetosomestudiesnot
directlyexplainingtherespectiveapproachused.Theremayalsobesomeinconsistencyinthe
reviewcarriedoutduetothepersonalopinionsofeachreviewer.
Itisknownthatintheclinicalarearegulationsandethicalissues(e.g.computerbasedcon-
trolofinfusionpumps)limittheapplicationofthemostadvancedphasesofthedecision-mak-
ingprocess(e.g.choiceandimplementation).Thismeansthatthehighestvalueforthe
maturitystagemightbelowerthan4.Thus,somedifficultiesencounteredintheadoptionof
CDSSmayberelatedtothemedicalcontext,suchas:thedevelopmentofmethodsforsupport-
ingchoicephaseofdecisionmaking;interoperabilityamongmedicaldevicesandhealthcare
informationsystems;technologyacceptance;ethicalandregulatoryrestrictions;poorinvolve-
mentofprofessionalsandorganizations.Alotofworkshouldbedoneinthefuturetomitigate
thoselimitations,startingwith:i)consideralargersampleofstudies;ii)determinethe
acceptedrangeofvaluesforthematuritystageinparticularclinicalcontextofapplication;and
iii)depictwhatitshouldbethefocusofresearchinordertofulfiltheactualmaturitygapand
developeffectiveCDSS.
Conclusion
ClinicalDecisionSupportSystems(CDSS)representthedecisionsupportactivityandcanbe
translatedintoamachine-readablecomputerizedformat.Mosthealthcareinformationsys-
temsareencouragedtooralreadyincludeclinicaldecisionsupportpracticestoorganize
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 14/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
clinicalknowledgeandimprovethedecision-makingprocess[3].Inordertoanswerthe
researchquestionsformulatedinthiswork,asystematicreviewwasdevelopedtoidentifythe
techniquesandapproachesusedinCDSSfrom52studies.Theoutcomeswerevariedanddid
notshowamainpattern,leadingtolimitedevidence.Nevertheless,itwasidentifiedthetop
threetrendsofthefourdefinedgroups:knowledgemanagement,technologicalfeatures,type
ofsystem,andsystemintegration.Inaddition,thisstudyallowedamorecompleteanalysisto
understandthestateofmaturityoftheCDSS.Acrossoveroftheidentifiedtrendswasmadeto
identifythematurityregardingthefourphasesproposedbySimon.Theresultsdemonstrated
thelackofmaturityoftheCDSSpresentedbythereviewedstudies.
Decisionmakingisaprocessofmakingachoicebetweenseveralalternativestoachievea
desiredoutcome.Amongthesepossiblecauses,themostcommonandseriouserrorisaninad-
equatedefinitionoftheproblem.Whentheproblemisnotdefinedcorrectly,thealternative
selectedandimplementedwillnotproducethedesiredresult.Thatsaid,webelievethatthe
biggestdifficultiesontheCDSSadoptionareintheoperationalclinicalenvironment,withthe
involvementofcharacteristics,processes,andstakeholders.Furthermore,basedontheidenti-
fiedgapinthisstudy,anagendashouldbecreatedforwhataneffectiveCDSSshouldbe.
Thereisanincentiveforthescientificcommunitytocontributetomitigatethelimitationsin
ordertoachievemoreeffectiveClinicalDecisionSupportSystems.
Supportinginformation
S1File.Informationextractedfromthereview.
(DOCX)
S2File.PRISMAchecklist.
(DOC)
S3File.PRISMAflowdiagramofstudyselection.
(DOC)
AuthorContributions
Conceptualization:FranciniHak,TiagoGuimarães,ManuelSantos.
Datacuration:FranciniHak,TiagoGuimarães.
Formalanalysis:FranciniHak,TiagoGuimarães.
Investigation:FranciniHak,TiagoGuimarães.
Methodology:FranciniHak,TiagoGuimarães.
Projectadministration:ManuelSantos.
Supervision:ManuelSantos.
Validation:ManuelSantos.
Writing–originaldraft:FranciniHak.
Writing–review&editing:FranciniHak,TiagoGuimarães,ManuelSantos.
References
1. SalazarM,DuarteJ,PereiraR,PortelaF,AbelhaA,MachadoJ,etal.SteptowardsPaperFreeHospi-
talthroughElectronicHealthRecord.2013;747:685–694.
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 15/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
2. FriedmanCP.A“FundamentalTheorem”ofBiomedicalInformatics.JournaloftheAmericanMedical
InformaticsAssociation.2009;16(2):169–170.https://doi.org/10.1197/jamia.M3092PMID:19074294
3. HandlerT,HoltmeierR,MetzgerJ,OverhageM,TaylorS,UnderwoodC.HIMSSelectronichealth
recorddefinitionalmodel.2003;(January2003):0–8.
4. MurtyKG,LiuJ,WanYw,LinnR.Adecisionsupportsystemforquaysideoperationsinacontainerter-
minal.DecisionSupportSystems.2005;59(1):312–324.
5. VasconcelosJ,RochaA,GomesR.SistemasdeInformac¸ãodeApoioàDecisãoCl´ınica:Estudode
umcasodeumaInstituic¸ãodeSau´de.2004.
6. NevesJ,SantosM,MachadoJ,AbelhaA,AllegroS,SalazarM.ElectronicHealthRecordsandDeci-
sionSupportLocalandGlobalPerspectives.WSEASTRANSACTIONSonBIOLOGYandBIOMEDI-
CINE.2008;5(8):189–198.
7. KalantariB.HerbertA.Simononmakingdecisions:Enduringinsightsandboundedrationality.Journal
ofManagementHistory.2010;16:509–520.https://doi.org/10.1108/17511341011073988
8. SimonHA.TheNewScienceofManagementDecision. USA: PrenticeHallPTR;1960.
9. SpragueRH,CarlsonED.BuildingEffectiveDecisionSupportSystems.PrenticeHallProfessional
TechnicalReference;1982.
10. BayoumiI,BalasMA,HandlerSM,DolovichL,HutchisonB,HolbrookA.Theeffectivenessofcomput-
erizeddrug-labalerts:Asystematicreviewandmeta-analysis.InternationalJournalofMedicalInfor-
matics.2014;83(6):406–415.https://doi.org/10.1016/j.ijmedinf.2014.03.003PMID:24793784
11. JiaP,ZhangL,ChenJ,ZhaoP,ZhangM.Theeffectsofclinicaldecisionsupportsystemsonmedica-
tionsafety:Anoverview.PLoSONE.2016;11.https://doi.org/10.1371/journal.pone.0167683PMID:
27977697
12. CurtisCE,BaharFA,MarriottJF.Theeffectivenessofcomputeriseddecisionsupportonantibioticuse
inhospitals:Asystematicreview.PLoSONE.2017;12.https://doi.org/10.1371/journal.pone.0183062
PMID:28837665
13. TurpinS,MaraisM.DecisionMaking:TheoryandPractice.TheJournalofFinance.2004;29(4):1341.
14. TurbanE,DelenD,ShardaR.Businessintelligenceandanalytics;2014.
15. MoherD,LiberatiA,TetzlaffJ,AltmanDG,AltmanD,AntesG,etal.Preferredreportingitemsforsys-
tematicreviewsandmeta-analyses:ThePRISMAstatement.PLoSMedicine.2009;6(7).https://doi.
org/10.1371/journal.pmed.1000097
16. Scimago.ScimagoJournalandCountryRank,year=2022,url=https://www.scimagojr.com/.
17. KockE.ABroaderPerspectivetoDecisionSupportSystems.2003.
18. LunenburgFC.THEDECISIONMAKINGPROCESS;2010.
19. FalcigliaGH,MurthyK,HollJL,PalacHL,WoodsDM,RobinsonDT.Lowprevalenceofclinicaldecision
supporttocalculatecaloricandfluidintakeforinfantsintheneonatalintensivecareunit.JournalofPeri-
natology.2020;40(3):497–503.https://doi.org/10.1038/s41372-019-0546-zPMID:31813935
20. LeeK,LeeSH.Artificialintelligence-drivenoncologyclinicaldecisionsupportsystemformultidisciplin-
aryteams.Sensors(Switzerland).2020;20(17):1–12.https://doi.org/10.3390/s20174693PMID:
32825296
21. CatalaniC,GreenE,OwitiP,KenyA,DieroL,YeungA,etal.Aclinicaldecisionsupportsystemforinte-
gratingtuberculosisandHIVcareinKenya:Ahuman-centereddesignapproach.PLoSONE.2014;9
(8).https://doi.org/10.1371/journal.pone.0103205PMID:25170939
22. AkhloufiH,VerhaeghSJC,JaspersMWM,MellesDC,vanderSijsH,VerbonA.Ausabilitystudyto
improveaclinicaldecisionsupportsystemfortheprescriptionofantibioticdrugs.PLoSONE.2019;14
(9):1–14.https://doi.org/10.1371/journal.pone.0223073PMID:31553785
23. TamburranoA,ValloneD,CarrozzaC,UrbaniA,SanguinettiM,NicolottiN,etal.Evaluationandcost
estimationoflaboratorytestoverusein43commonlyorderedparametersthroughaComputerizedClin-
icalDecisionSupportSystem(CCDSS)inalargeuniversityhospital.PLoSONE.2020;15(8
August):1–11.
24. KimHJ,KimHJ,ParkY,LeeWS,LimY,KimJH.ClinicalGenomeDataModel(cGDM)providesInter-
activeClinicalDecisionSupportforPrecisionMedicine.ScientificReports.2020;10(1):1–13.https://
doi.org/10.1038/s41598-020-58088-2PMID:31996707
25. LinL,HuPJH,LiuShengOR.Adecisionsupportsystemforlowerbackpaindiagnosis:Uncertainty
managementandclinicalevaluations.DecisionSupportSystems.2006;42(2):1152–1169.https://doi.
org/10.1016/j.dss.2005.10.007
26. RaoGR,TuroffM.Hypermedia-basedgroupdecisionsupportsystemtosupportcollaborativemedical
decision-making.DecisionSupportSystems.2000;30(2):187–216.https://doi.org/10.1016/S0167-
9236(00)00096-8
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 16/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
27. VanValkenhoefG,TervonenT,ZwinkelsT,DeBrockB,HillegeH.ADDIS:Adecisionsupportsystem
forevidence-basedmedicine.DecisionSupportSystems.2013;55(2):459–475.https://doi.org/10.
1016/j.dss.2012.10.005
28. HuPJH,WeiCP,LiuShengOR.Evaluatingadecisionsupportsystemforpatientimagepre-fetching:
Anexperimentalstudy.DecisionSupportSystems.2006;42(3):1730–1746.https://doi.org/10.1016/j.
dss.2006.02.016
29. MichalowskiW,RubinS,SlowinskiR,WilkS.Mobileclinicalsupportsystemforpediatricemergencies.
DecisionSupportSystems.2003;36(2):161–176.https://doi.org/10.1016/S0167-9236(02)00140-9
30. YaoW,KumarA.CONFlexFlow:IntegratingFlexibleclinicalpathwaysintoclinicaldecisionsupportsys-
temsusingcontextandrules.DecisionSupportSystems.2013;55(2):499–515.https://doi.org/10.
1016/j.dss.2012.10.008
31. LussierYA,WilliamsR,LiJ,JalanS,BorlawskyT,SternE,etal.Partitioningknowledgebasesbetween
advancednotificationandclinicaldecisionsupportsystems.DecisionSupportSystems.2007;43
(4):1274–1286.https://doi.org/10.1016/j.dss.2006.02.006
32. CornyJ,RajkumarA,MartinO,DodeX,LajonchèreJP,BilluartO,etal.Amachinelearning–basedclin-
icaldecisionsupportsystemtoidentifyprescriptionswithahighriskofmedicationerror.Journalofthe
AmericanMedicalInformaticsAssociation.2020;00(0):1–7.https://doi.org/10.1093/jamia/ocaa154
PMID:32984901
33. AltayEV,AlatasB.Anovelclinicaldecisionsupportsystemforliverfibrosisusingevolutionarymulti-
objectivemethodbasednumericalassociationanalysis.MedicalHypotheses.2020;144(May):110028.
https://doi.org/10.1016/j.mehy.2020.110028PMID:32758874
34. YooJ,LeeJ,RheePL,ChangDK,KangM,ChoiJS,etal.AlertOverridePatternswithaMedication
ClinicalDecisionSupportSysteminanAcademicEmergencyDepartment:RetrospectiveDescriptive
Study(Preprint).JMIRMedicalInformatics.2020;8:1–14.https://doi.org/10.2196/23351
35. HamedanF,OroojiA,SanadgolH,SheikhtaheriA.Clinicaldecisionsupportsystemtopredictchronic
kidneydisease:Afuzzyexpertsystemapproach.InternationalJournalofMedicalInformatics.2020;
138(December2019):104134.https://doi.org/10.1016/j.ijmedinf.2020.104134PMID:32298972
36. Holmstro¨mIK,KaminskyE,LindbergY,SpanglerD,WinbladU.RegisteredNurses’experiencesof
usingaclinicaldecisionsupportsystemfortriageofemergencycalls:Aqualitativeinterviewstudy.Jour-
nalofAdvancedNursing.2020;76(11):3104–3112.https://doi.org/10.1111/jan.14542PMID:32924138
37. ChinDL,WilsonMH,TraskAS,JohnsonVT,NeavesBI,GojovaA,etal.RepurposingClinicalDecision
SupportSystemDatatoMeasureDosingErrorsandClinician-LevelQualityofCare.JournalofMedical
Systems.2020;44(10).https://doi.org/10.1007/s10916-020-01603-9PMID:32897483
38. NiazkhaniZ,FereidoniM,RashidiKhazaeeP,ShivaA,MakhdoomiK,GeorgiouA,etal.Translationof
evidenceintokidneytransplantclinicalpractice:Managingdrug-labinteractionsbyacontext-awareclin-
icaldecisionsupportsystem.BMCMedicalInformaticsandDecisionMaking.2020;20(1):1–13.https://
doi.org/10.1186/s12911-020-01196-wPMID:32819359
39. BergeGT,GranmoOC,TveitTO.Combiningunsupervised,supervised,andrule-basedalgorithmsfor
textminingofelectronichealthrecords:Aclinicaldecisionsupportsystemforidentifyingandclassifying
allergiesofconcernforanesthesiaduringsurgery.InformationSystemsDevelopment:Advancesin
Methods,ToolsandManagement—Proceedingsofthe26thInternationalConferenceonInformation
SystemsDevelopment,ISD2017.2017.
40. WasylewiczATM,Scheepers-HoeksAMJW.Clinicaldecisionsupportsystems.FundamentalsofClini-
calDataScience.2018;(June):153–169.
41. SmitK,KoornneefP,NysinghJ,vanZwienenM,BerkhoutM,RavesteynP.Transformingclinicalprac-
ticeguidelineusagethroughtheuseofaclinicaldecisionsupportsystem:Anexplorativestudyatthe
universitymedicalcentreUtrecht.30thBledeConference:DigitalTransformation—FromConnecting
ThingstoTransformingourLives,BLED2017.2017;p.577–592.
42. DalabaMA,AkweongoP,WilliamsJ,SarongaHP,TonchevP,SauerbornR,etal.Costsassociated
withimplementationofcomputer-assistedclinicaldecisionsupportsystemforantenatalanddelivery
care:CasestudyofKassena-NankanadistrictofnorthernGhana.PLoSONE.2014;9(9).https://doi.
org/10.1371/journal.pone.0106416PMID:25180831
43. SimLLW,BanKHK,TanTW,SethiSK,LohTP.Developmentofaclinicaldecisionsupportsystemfor
diabetescare:Apilotstudy.PLoSONE.2017;12(2):1–15.https://doi.org/10.1371/journal.pone.
0173021PMID:28235017
44. BernasconiA,Crabbe´F,AdedejiAM,BelloA,SchmitzT,LandiM,etal.Resultsfromone-yearuseof
anelectronicClinicalDecisionSupportSysteminapost-conflictcontext:Animplementationresearch.
PLoSONE.2019;14(12):1–17.https://doi.org/10.1371/journal.pone.0225634
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 17/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
45. MenonS,TarragoR,CarlinK,WuH,YonekawaK.Impactofintegratedclinicaldecisionsupportsys-
temsinthemanagementofpediatricacutekidneyinjury:apilotstudy.PediatricResearch.2020;
(April):1–7.PMID:32620006
46. ArainY,BandaJM,FaulkenberryJ,BhutaniVK,PalmaJP.Clinicaldecisionsupporttoolforphotother-
apyinitiationinpreterminfants.JournalofPerinatology.2020;40(10):1518–1523.https://doi.org/10.
1038/s41372-020-00782-0PMID:32792630
47. Se´roussiB,Laoue´nanC,GligorovJ,UzanS,Mentre´F,BouaudJ.Whichbreastcancerdecisions
remainnon-compliantwithguidelinesdespitetheuseofcomputeriseddecisionsupport?BritishJournal
ofCancer.2013;109(5):1147–1156.https://doi.org/10.1038/bjc.2013.453PMID:23942076
48. Akc¸uraMT,OzdemirZD.Drugprescriptionbehavioranddecisionsupportsystems.DecisionSupport
Systems.2014;57(1):395–405.
49. JohnsonMP,ZhengK,PadmanR.Modelingthelongitudinalityofuseracceptanceoftechnologywith
anevidence-adaptiveclinicaldecisionsupportsystem.DecisionSupportSystems.2014;57(1):444–
453.https://doi.org/10.1016/j.dss.2012.10.049
50. LamShinCheungJ,PaolucciN,PriceC,SykesJ,GuptaS.AsystemuptakeanalysisandGUIDES
checklistevaluationoftheElectronicAsthmaManagementSystem:Apoint-of-carecomputerizedclini-
caldecisionsupportsystem.JournaloftheAmericanMedicalInformaticsAssociation.2020;27
(5):726–737.https://doi.org/10.1093/jamia/ocaa019PMID:32274495
51. DownieAS,HancockM,AbdelShaheedC,McLachlanAJ,KocaballiAB,WilliamsCM,etal.AnElec-
tronicClinicalDecisionSupportSystemfortheManagementofLowBackPaininCommunityPhar-
macy:DevelopmentandMixedMethodsFeasibilityStudy.JMIRMedicalInformatics.2020;8(5):
e17203.https://doi.org/10.2196/17203PMID:32390593
52. XuF,Sepu´lvedaMJ,JiangZ,WangH,LiJ,LiuZ,etal.EffectofanArtificialIntelligenceClinicalDeci-
sionSupportSystemonTreatmentDecisionsforComplexBreastCancer.JCOClinicalCancerInfor-
matics.2020;(4):824–838.https://doi.org/10.1200/CCI.20.00018PMID:32970484
53. TorresSilvaEA,UribeS,SmithJ,LunaGomezIF,Florez-ArangoJF.XMLDataandKnowledge-
EncodingStructureforaWeb-BasedandMobileAntenatalClinicalDecisionSupportSystem:Develop-
mentStudy.JMIRFormativeResearch.2020;4(10):e17512.https://doi.org/10.2196/17512PMID:
33064087
54. MillerMK,MollenC,BehrK,DowdMD,MillerE,SatterwhiteCL,etal.DevelopmentofaNovelComput-
erizedClinicalDecisionSupportSystemtoImproveAdolescentSexualHealthCareProvision.Aca-
demicEmergencyMedicine.2019;26(4):420–433.https://doi.org/10.1111/acem.13570PMID:
30240032
55. BondSE,ChubatyAJ,AdhikariS,MiyakisS,BoutlisCS,YeoWW,etal.Outcomesofmultisiteantimi-
crobialstewardshipprogrammeimplementationwithasharedclinicaldecisionsupportsystem.Journal
ofAntimicrobialChemotherapy.2017;72(7):2110–2118.https://doi.org/10.1093/jac/dkx080PMID:
28333302
56. StrockbineVL,GehrieEA,ZhouQP,GuzzettaCE.ReducingUnnecessaryPhlebotomyTestingUsing
aClinicalDecisionSupportSystem.Journalforhealthcarequality:officialpublicationoftheNational
AssociationforHealthcareQuality.2020;42(2):98–105.https://doi.org/10.1097/JHQ.
0000000000000245PMID:31972663
57. JiangX,WellsA,BrufskyA,NeapolitanR.Aclinicaldecisionsupportsystemlearnedfromdatatoper-
sonalizetreatmentrecommendationstowardspreventingbreastcancermetastasis.PLoSONE.2019;
14(3):1–18.https://doi.org/10.1371/journal.pone.0213292PMID:30849111
58. DeLimaMarinhoC,MaioliMCP,DoAmaralJLM,LopesAJ,DeMeloPL.Respiratoryresistanceand
reactanceinadultswithsicklecellanemia:Part2—Fractional-ordermodelingandaclinicaldecision
supportsystemforthediagnosisofrespiratorydisorders.PLoSONE.2019;14(3):1–21.
59. WuG,YangP,XieY,WoodruffHC,RaoX,GuiotJ,etal.Developmentofaclinicaldecisionsupport
systemforseverityriskpredictionandtriageofCOVID-19patientsathospitaladmission:Aninterna-
tionalmulticentrestudy.EuropeanRespiratoryJournal.2020;56(2).https://doi.org/10.1183/13993003.
01104-2020PMID:32616597
60. ChoiGH,YunJ,ChoiJ,LeeD,ShimJH,LeeHC,etal.Developmentofmachinelearning-basedclinical
decisionsupportsystemforhepatocellularcarcinoma.ScientificReports.2020;10(1):1–10.https://doi.
org/10.1038/s41598-020-71796-zPMID:32908183
61. LichteneggerKM,AbererF,TucaAC,DonsaK,Ho¨llB,SchauppL,etal.SafeandSufficientGlycemic
ControlbyUsingaDigitalClinicalDecisionSupportSystemforPatientsWithType2DiabetesinaRou-
tineSettingonGeneralHospitalWards.JournalofDiabetesScienceandTechnology.2020.
62. VargasonT,CohnJ,SchultzO.TheOpenRepository@Binghamton(TheORB)AClinicalDecision
SupportSystemforMalignantPleuralEffusionAnalysis.2016.
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 18/19

PLOS ONE Towardseffectiveclinicaldecisionsupportsystems
63. XuB,LiC,ZhuangH,WangJ,WangQ,WangC,etal.Distributedgeneclinicaldecisionsupportsys-
tembasedoncloudcomputing.BMCMedicalGenomics.2018;11.https://doi.org/10.1186/s12920-
018-0415-1PMID:30454054
64. SchaafJ,SedlmayrM,ProkoschHU,GanslandtT,Schade-BrittingerC,WagnerMV,etal.Thestatus
quoofrarediseasescentresforthedevelopmentofaclinicaldecisionsupportsystem—Across-sec-
tionalstudy.StudiesinHealthTechnologyandInformatics.2020;271:176–183.PMID:32578561
65. XuQ,ZhaiJC,HuoCQ,LiY,DongXJ,LiDF,etal.OncoPDSS:Anevidence-basedclinicaldecision
supportsystemforoncologypharmacotherapyattheindividuallevel.BMCCancer.2020;20(1):1–10.
https://doi.org/10.1186/s12885-020-07221-5PMID:32770988
66. BerrouiguetS,Barrigo´nML,BrandtSA,Ovejero-Garc´ıaS,A´lvarez-Garc´ıaR,CarballoJJ,etal.Devel-
opmentofaweb-basedclinicaldecisionsupportsystemfordrugprescription:Non-interventionalnatu-
ralisticdescriptionoftheantipsychoticprescriptionpatternsin4345outpatientsandfutureapplications.
PLoSONE.2016;11(10):1–16.https://doi.org/10.1371/journal.pone.0163796PMID:27764107
67. PiriS,DelenD,LiuT,ZolbaninHM.Adataanalyticsapproachtobuildingaclinicaldecisionsupportsys-
temfordiabeticretinopathy:Developinganddeployingamodelensemble.DecisionSupportSystems.
2017;101:12–27.https://doi.org/10.1016/j.dss.2017.05.012
68. PiriS.Missingcare:Aframeworktoaddresstheissueoffrequentmissingvalues;Thecaseofaclinical
decisionsupportsystemforParkinson’sdisease.DecisionSupportSystems.2020;136(November
2019):113339.https://doi.org/10.1016/j.dss.2020.113339
69. BreitbartEW,ChoudhuryK,AndersenAD,BundeH,BreitbartM,SideriAM,etal.Improvedpatientsat-
isfactionanddiagnosticaccuracyinskindiseaseswithaVisualClinicalDecisionSupportSystem-Afea-
sibilitystudywithgeneralpractitioners.PLoSONE.2020;15(7July):1–12.https://doi.org/10.1371/
journal.pone.0235410PMID:32726308
70. UcuzI,Cic¸ekAU,AriA,OzcanOO,Aybu¨keSariS.Determiningtheprobabilityofjuveniledelinquency
byusingsupportvectormachinesanddesigningaclinicaldecisionsupportsystem.MedicalHypothe-
ses.2020;143(July):110118.https://doi.org/10.1016/j.mehy.2020.110118PMID:32721810
71. AnchalaR,PintoMP,ShroufiA,ChowdhuryR,SandersonJ,JohnsonL,etal.TheRoleofDecision
SupportSystem(DSS)inPreventionofCardiovascularDisease:ASystematicReviewandMeta-Analy-
sis.PLoSONE.2012;7.https://doi.org/10.1371/journal.pone.0047064PMID:23071713
PLOSONE|https://doi.org/10.1371/journal.pone.0272846 August15,2022 19/19
