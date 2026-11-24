OriginalInvestigation | HealthInformatics
EffectofElectronicHealthRecordClinicalDecisionSupport
onContextualizationofCare
ARandomizedClinicalTrial
SaulJ.Weiner,MD;AlanSchwartz,PhD;FrancesWeaver,PhD;WilliamGalanter,MD,PhD;SarahOlender,MS,RDN;KarlKochendorfer,MD;
AmyBinns-Calvey,BA;RavishaSaini,BA;SanaIqbal,BS,BA;MoniqueDiaz,MD;AaronMichelfelder,MD;AnitaVarkey,MD
Abstract KeyPoints
Question Cancustomizedclinical
IMPORTANCE Contextualizingcareisaprocessofincorporatinginformationaboutthelife
decisionsupport(CDS)toolsthat
circumstancesandbehaviorofindividualpatients,termedcontextualfactors,intotheirplanofcare.
provideclinicianswithinformation
In4steps,cliniciansrecognizeclues(termedcontextualredflags),cliniciansaskaboutthem(probe
aboutpatientlifechallengesimprove
forcontext),patientsdisclosecontextualfactors,andcliniciansadaptcareaccordingly.Theprocessis
patientoutcomesbyhelpingclinicians
associatedwithadesiredoutcomeresolutionofthepresentingcontextualredflag.
contextualizetheircare?
OBJECTIVE Todeterminewhethercontextualizedclinicaldecisionsupport(CDS)toolsinthe Findings Inthisrandomizedclinicaltrial
electronichealthrecord(EHR)improvecliniciancontextualprobing,attentiontocontextualfactors thatincluded452audio-recorded
incareplanning,andthepresentationofcontextualredflags. patientencounters,customizedCDS
toolsdidnotimprovepatients’
DESIGN,SETTING,ANDPARTICIPANTS Thisrandomizedclinicaltrialwasperformedattheprimary outcomesbutsignificantlyimproved
careclinicsof2academicmedicalcenterswithdifferentEHRsystems.Participantswereadults18 contextualizationoftheircare.
yearsorolderconsentingtoaudiorecordtheirvisitsandtheirphysiciansbetweenSeptember6,
Meaning ThisstudyfoundthatCDS
2018,andMarch4,2021.Patientswererandomizedtoaninterventionoracontrolgroup.Analyses
improvedcontextualizationofcare,
wereperformedonanintention-to-treatbasis.
suggestingthatthetechnologyhasthe
potentialtoimprovepatientoutcomes.
INTERVENTIONS Patientscompletedaprevisitquestionnairethatelicitedcontextualredflagsand
factorsandappearedintheclinician’snotetemplateinacontextualcarebox.TheEHRalsoculled
+
redflagsfromthemedicalrecord,includedtheminthecontextualcarebox,usedpassiveand Supplementalcontent
interruptivealerts,andproposedrelevantorders. Authoraffiliationsandarticleinformationare
listedattheendofthisarticle.
MAINOUTCOMESANDMEASURES Proportionofcontextualredflagsnotedattheindexvisitthat
resolved6monthslater(primaryoutcome),proportionofredflagsprobed(secondaryoutcome),
andproportionofcontextualfactorsaddressedinthecareplanbyclinicians(secondaryoutcome),
adjustedforstudysiteandformultipleredflagsandfactorswithinavisit.
RESULTS Fourhundredfifty-twopatients(291women[65.1%];mean[SD]age,55.6[15.1]years)
completedencounterswith39clinicians(23women[59.0%]).Contextualredflagswerenotmore
likelytoresolveintheinterventionvscontrolgroup(adjustedoddsratio[aOR],0.96[95%CI,0.57-
1.63]).However,theinterventionincreasedbothcontextualprobing(aOR,2.12[95%CI,1.14-3.93])
andcontextualizationofthecareplan(aOR,2.67[95%CI,1.32-5.41]),controllingforwhetherafactor
wasidentifiedbyprobingorotherwise.Acrossstudygroups,contextualizedcareplansweremore
likelythannoncontextualizedplanstoresultinimprovementinthepresentingredflag(aOR,2.13
[95%CI,1.38-3.28]).
(continued)
OpenAccess.ThisisanopenaccessarticledistributedunderthetermsoftheCC-BYLicense.
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 1/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
Abstract(continued)
CONCLUSIONSANDRELEVANCE ThisrandomizedclinicaltrialfoundthatcontextualizedCDSdid
notimprovepatients’outcomesbutdidincreasecontextualizationoftheircare,suggestingthatuse
ofthistechnologycouldultimatelyhelpimproveoutcomes.
TRIALREGISTRATION ClinicalTrials.govIdentifier:NCT03244033
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231
Introduction
Contextualizingcareistheprocessofelicitingandincorporatingrelevantinformationaboutthelife
circumstancesandbehaviorofindividualpatients,termedcontextualfactors,intotheirplanofcare.1
Theprocesstypicallyincludes4steps:First,recognizingcluesofunaddressedcontextualfactors(eg,
lossofcontrolofdiabetes),termedcontextualredflags;second,askingpatientsaboutthem,termed
contextualprobing;third,elicitingrelevantcontextualfactors(eg,deterioratingvisioninapatient
self-administeringinsulin);andfourth,addressingthesefactorsinthecareplan(eg,prescribing
prefilledsyringes)tocontextualizecare.2-4
Contextualizingcareisclinicallyimportantbecauseitisassociatedwithpartialorcomplete
resolutionofthepresentingcontextualredflag,ameaningfulhealthcareoutcome.5Lossofcontrol
ofachroniccondition,missedappointments,andfrequentemergencydepartmentvisitsareall
examplesofcontextualredflagsthatimprovewhentheirunderlyingcontextualfactorsare
addressed.6
Althoughnotallpatientpresentationscontaincontextualfactors,approximately40%to50%
do.6Cliniciansaddressthem60%to70%ofthetime,leavingsubstantialroomforimprovement.6,7
Thesefailurestocontextualizecarearetermedcontextualerrors.7-9
Effortstoimprovecontextualizationofcarethroughauditandfeedbackhaveachieved
measurablebutlimitedsuccess.In1largestudy,5666cliniciansreceivedrecurringfeedbackontheir
performanceatcontextualizingcareduring2yearsbasedoncontentcodingforcontextualization
ofcare(4C)analysisofnearly4500audio-recordedvisits.Attentiontopatientcontextualfactors
increasedfrom67%to72%,withagreaterlikelihoodofimprovedoutcomescomparedwitha
controlgroup,resultinginanestimatedcostsavingsof$25.2millionfromavoidedhospitalizations.
Althoughtheinterventionwaseffective,28%ofcontextualfactorsremainedunaddressed.5
Wehypothesizedthatcustomizedclinicaldecisionsupport(CDS)wouldofferascalable
opportunitytohelpclinicianscontextualizecareand,insodoing,wouldimprovepatientoutcomes.
Inthisstudy,wetestedthosehypothesesusingCDSdesignedtoprovidecliniciansinformationabout
contextualfactorsatthepointofcare.
Methods
StudyDesignandParticipants
Inthis27-monthrandomizedmulticenterclinicaltrial,primarycareattendingclinicianswere
recruitedat2academichealthcentersinChicagousing2differentEHRs,developedbyCerner
Corporation(site1)andEpicSystems(site2).Physicianswereinformedthatthepurposeofthe
projectwastoassesswhetherenhancedclinicaldecisionsupportthatprovidesinformationabout
patientcontextualfactorscouldimproveclinicaldecision-makingandhealthcareoutcomes.They
wereinformedthatiftheyparticipated,asmallnumberofpatientswouldaudiorecordtheirvisits.
Thetrialprotocol(availableinSupplement1)wasapprovedbytheInstitutionalReviewBoardsatthe
UniversityofChicagoandLoyolaUniversityChicago,andbothcliniciansandpatientsprovided
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 2/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
writteninformedconsent.ThisstudyfollowedtheConsolidatedStandardsofReportingTrials
(CONSORT)reportingguideline.
AllEnglish-speakingadultpatientsofparticipatingclinicianswhocouldbecontactedinadvance
oftheirappointmentswereeligibletoparticipate.Patientswereinformedthatiftheyparticipated,
theywouldcompleteaquestionnaireaboutchallengesthatmightimpacttheircare.Theycould
accessitdirectlyinthepatientportalorcompleteitwithassistancefromaresearchassistant.When
theyarrivedfortheirappointment,theyreceivedadigitalaudiorecordertocarryintotheirvisit.
Theyweretoldthatitwaspreferabletoconcealtherecorder,butthattheycouldrevealitiftheyfelt
morecomfortabledoingso.Theywereinformedthatamemberoftheresearchteamwouldaccess
theirmedicalrecordfirsttonotecontextualredflagsandfactorsself-identifiedbypatientsonthe
questionnaire,andthenseveralmonthslatertoseeifkeyhealthcareindicatorsnotedatthevisithad
improved.Finally,theyweretoldthattheirclinicianmightormightnotreceivetheinformationthey
provided,basedonrandomassignment.Patientsreceiveda$20recruitmentincentive.
Intervention
Theinterventiondesign,whichfollowedtheFiveRightsofCDSframework,consistedof2elements:
acontextualcarebox(CCB)thatappearedintheclinician’snoteatthestartofthevisitnotifying
themofcontextualfactorsbasedonpatientquestionnaireresponsesandselectedpassiveandactive
interruptivealertsintendedtodirectthemtowardacontextualizedcareplanandawayfroma
contextualerror.10Bothwerepopulatedby2previsitsourcesofdata:thequestionnaireandasetof
algorithmsthatextractcontextualfactorsfromthepatient’smedicalrecord.
Thequestionnaireincluded7questionsdesignedinapriorstudy11toelicitabroadrangeof
contextualredflagspertainingtomedication,appointment,laboratorytesting,andtestadherence;
decliningrecommendedtreatments,tests,andprocedures;repeatedvisitstotheemergency
department;difficultyaccessingequipmentorsupplies;challengesperformingactivitiesimportant
tostayinghealthy,andotherchallengesrelatedtoself-managingcare(eAppendix1inSupplement2).
Anaffirmativeresponsetoanyitempromptedtherespondenttoselect1ormorecontextualfactors
ifpresent.
Inaddition,thefollowingcontextualredflagswereextractedfromthepatient’smedicalrecord
basedonrulesprogrammedintotheEHRandactivatedforinterventionpatients:missed
appointments,missedtestsandprocedures,multipleemergencydepartmentvisits,lossofcontrol
ofeitherdiabetesorhypertensionwhilereceivingmedication,andself-paystatus.Eachwas
determinedbyasetofparameters,suchasnumberofmissedappointmentsinaspecifictimeframe
(examplesinTable1).Forparticipantsrandomizedtotheintervention,contextualredflagsand
factorsappearedintheCCB(exampleineAppendix2inSupplement2).Interruptivealertswereused
eithertoinitiatenonmedicalinterventionsthatwerelikelytobebeneficial(exampleineAppendix3
inSupplement2)ortoredirectanapparentlymisguidedplanofcare.12FurtherdetailsoftheCDS
designprocessareprovidedineAppendix4inSupplement2.Thesystemdidnotoperateduring
visitsbypatientsinthecontrolgroup.
EndPoints
Theprimarystudyendpointconstitutedproportionsofimprovedorresolved(vsworsenedorno
change)contextualredflags6monthsafterthevisit(Table1).Secondaryendpointswerethe
proportionofcontextualredflagsprobedinthevisitandtheproportionofcontextualfactors
identifiedduringthevisitthatwereaddressedinthevisitcareplan(ie,thecontextualizationofcare
rate).The9categoriesofcontextualredflags,alongwithsubcategories,weredevelopedinprevious
research.13,14ExploratoryoutcomesweretheeffectsoftheEHRalertsonprobingofcontextualred
flagsthatpatientsdidnotthemselvesbringupduringthevisitandtheeffectofthealertsonthered
flags6monthslater.
DatawererecordedusingREDCap.Aftereachencounter,researchassistants(A.B.-C.andS.I.),
whowereblindtotheassignmentofeachpatienttotheinterventionorthecontrolgroup,accessed
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 3/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
theEHRandlistenedtotheaudiorecordingtoidentifycontextualredflags(anddeterminewhether
eachwasprobedbytheclinician)andcontextualfactors(anddeterminewhethereachwas
incorporatedintothecareplanbytheclinician),usingthe4Cmethodology.14,15Trainedcoders
achieveapproximately85%interrateragreementaboutwhetheracareplaniscontextualizedor
not.15Consistentwiththe4Cmethodology,redflagsandcontextualfactorswerenotedbythe
codersfromthepatientquestionnaire,EHR,oraudiorecordingofthevisit;factorsnotedonthe
audiorecordingemergedeitherasaresultofclinicianprobingorspontaneousdisclosurebythe
patient.Foreachredflag,codersprospectivelydefinedtheconditionsunderwhichtheredflag
wouldbeconsideredimprovedorworsenedinthefuture.Sixmonthsaftereachencounter,research
assistants,againblindtotheassignmentofpatientstotheinterventionorthecontrolgroup,applied
thepredefinedconditionstocodeeachofthepatients’redflagsfromEHRreviewasimproved,
worsened,unchanged,orundocumentedatfollow-up.
SampleSize
Basedonpriorstudies,6,16weassumedthatcontextualredflagswithassociatedfactorswouldbe
presentin50%ofrecordedvisits,andthatclinicians,unaided,wouldprobe50%ofcontextualred
flagsandcontextualizecareplansin50%ofvisitswithcontextualfactors.Basedonthenumberof
contextualredflagsandfactorsweexpected,wedeterminedthattoobtain80%powertodetectan
absoluteincreaseincontextualizationrateswhenfactorswerepresentfrom50%to75%,wewould
needrecordingsfrom192interventionand288controlpatients(whichalsoprovidesatleast80%
powertodetecttheexpectedincreaseinprobing).
Table1.ProspectivelyDeterminedOutcomesBasedonthePresentingContextualRedFlag
Outcome
Nochange(redflag
Good(redflagdocumented Bad(redflagdocumented documentedatsamelevelor
Redflag(source) Criteria toimproveorresolve) toworsenorpersist) notdocumentedaschanged)
Uncontrolledchronicconditionforwhichthe HbA levelhasincreasedsince AnydecreaseinHbA level; AnyincreaseinHbA level; NochangeinHbA level;no
1c 1c 1c 1c
patientisbeingtreated(EHR,audiorecording) priormeasurementby>1 anydecreaseinSBPorDBP anyincreaseinSBPorDBP changeinSBPorDBP
percentagepoint;SBPand/or
DBPhasincreasedsinceprior
measurementby>10mmHg
Appointmentnonadherence:clinics,laboratory Missed≥2clinicalencounters Patientmissesfewer Patientmissesmore Patientmissessamenumber
tests,imaging,procedures(EHR,patient inpast4mo;missed≥1 appointmentsduringthenext appointmentsinthenext4 ofappointmentsinnext4
questionnaire,audiorecording) laboratorytestsand/or 4mo;patientcompletes mo;patientcompletesfewer mo;patientmissessame
scheduledstudyinpast4mo scheduledlaboratorytests scheduledlaboratorytests proportionofscheduledtests
and/orscheduledstudies and/orscheduledstudies orstudies
EDvisits(EHR,patientquestionnaire,audio ≥2EDvisitsinpast4mo PatienthasfewerEDvisits PatienthasmoreEDvisits Patienthassamenumberof
recording) EDvisits
Medicationnonadherence(patient Answers“yes”to“Areyou Patienttakesmedicationsas Patientdoesnottake Medicaladherencenot
questionnaire,audiorecording) havinganydifficultytaking prescribed medicationsasprescribed documented
medicationsthewayyouhave
beentoldtotakethem?”
and/ormentionsitduringvisit
Missedpreventivecare(patientquestionnaire, Answers“yes”to“Inthepast6 Patientreceives Patientdoesnotreceive Patientreceiptoftreatments,
audiorecording) mo,haveyoudeclinedany recommendedtreatments, recommendedtreatments, tests,orproceduresnot
treatments,tests,or tests,orprocedures tests,orprocedures documented
proceduresthatyourprovider
recommended,likevaccines,
bloodtests,acolonoscopy?”
and/ormentionsitduringvisit
Weightgainorloss(audiorecording) ≥4.5kg(10lb)gainedorlost Ifoverweight,weightislower; Ifoverweight,weightis Patientweightstaysthesame
sincelastappointment ifunderweight,weightis higher;ifunderweight,
higher weightislower
Unawareofdiagnosisand/orresults(audio Patientmentionsthattheyare Patientisawareofdiagnosis Patientisstillunawareof Patientawarenessor
recording) unawareofdiagnosisortest orresults diagnosisorresults unawarenessnotdocumented
resultsthatshouldhavebeen
communicatedtopatient
Difficultywithequipment(patient Unabletouseordeclinetouse Usingownequipment Notusing(own)equipment Patientuseofequipmentnot
questionnaire,audiorecording) medicalequipment,orusing documented
someoneelse’sequipment
Generalstatementsbypatientsthatare Individualized Individualizedand Individualizedand Individualized,prospectively
concerningsuchas“I’mnoteating”(patient prospectivelydetermined prospectivelydetermined determinedoutcomenot
questionnaire,audiorecording) documented
Abbreviations:DBP,diastolicbloodpressure;ED,emergencydepartment;EHR,electronichealthrecord;HbA ,hemoglobinA ;SBP,systolicbloodpressure.
1c 1c
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 4/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
RandomizationandBlinding
Patientswererandomized2:3toeithercontextualizedCDS(intervention)orusualcare(control)
usingcomputer-generatedrandomization.Wechosearatioof2:3interventiontocontrolpatients
becausetherewouldbefeweropportunitiestocontextualizecareplansinthecontrolgroupiffewer
redflagswereprobed.Randomizedassignmentswereavailabletoresearchpersonnelresponsible
foractivatingtheCDStoolsimmediatelybeforetheencounter,butthoseinvolvedincodingvisitsand
trackingoutcomeswereblinded.Althoughpatientswereblindedastowhethertheywereinthe
interventionorcontrolgroup,itwasnotpossibletoblindcliniciansbecausetheinterventionisaset
ofnovelCDStoolsthatarenotavailableinusualcare.
StatisticalAnalysis
Weappliedalogisticmixed-effectsmodelingapproachtoexaminetheimpactofthestudy
intervention.Wefitted2modelstothe6-monthchangesintheredflags.Onemodelexamined
whethertheredflaghadimproved(ie,resolved)(vsworsenedornochange;primaryendpoint);the
otherexaminedwhethertheredflaghadworsened(vsimprovedornochange).Eachincludedfixed
effectsofstudygroup,studysite,andwhethertheredflag’sassociatedfactorhadbeenincorporated
intothecareplan,andrandomeffectsofvisit,patient,andclinician.Asasensitivityanalysis,wealso
fittedamixedorderedlogitmodeltotheoutcomescategorizedasworsened,nochangeormixed,or
improved.
Foreachredflagnotedbycoders,wefittedamodeltowhethertheredflagwasprobedbythe
clinician(secondaryendpoint).Inadditiontoafixedeffectofstudygroup(interventionvscontrol),
weincludedfixed-effectcovariatesforstudysite,whetherarelevantfactorhadbeenselectedonthe
previsitquestionnaireandwhethertheaudiorecorderwasconcealedordisclosed,andrandom
effectsofvisit,patient,andcliniciantoadjustforclusteringofredflagswithinvisitsandvisitswithin
cliniciansandrepeatedvisitsbythesamepatient.
Similarly,foreachcontextualfactornotedby4Ccoders,wefittedamodeltowhetherthefactor
wasincorporatedinthecareplanbytheclinician(secondaryendpoint).Inadditiontoafixedeffect
ofstudygroup,weincludedfixedeffectsofstudysite;whetherthefactorwasidentifiedbyprobing
ofaredflag,selectedinthepatientquestionnaire,orrevealedspontaneouslybythepatient;
whethertheaudiorecorderwasconcealedorvisible;andrandomeffectsofvisit,patient,and
clinician.
OurexploratoryanalysesoftheimpactofCDSonCCBsandalertswerelimitedtointervention
visitswithredflagsthatcouldbepresentedintheCCB(thatis,redflagsavailablebeforethevisit
itself),andexaminedwhetherthepresenceofaCCBoranalertforaredflagaffectedthelikelihood
ofprobing,incorporatingacontextualfactorinaplanifonewaspresent,orhavinganimprovedor
worsenedredflagat6months,adjustingforsiteandrandomeffectsofvisit,patient,andclinician.
Wealsoexaminedthisquestionusingallvisitsandincludingcovariatesfortheinterventionvsthe
controlgroupsandtheinteractionofinterventionvscontrolgroupandpresenceofCCBoralert
(whichcouldonlyhappenintheinterventiongroups).
Allanalyseswereperformedonanintention-to-treatbasisusingR,version3.6(RCoreTeam).
Two-sidedP<.05indicatedstatisticalsignificance.
Results
StudyParticipantsandRecruitment
FromSeptember6,2018,toMarch4,2021,452visitsbyadultpatients(291women[65.1%]and156
men[34.9%];mean[SD]age,55.6[15.1]years)withupcomingprimarycareappointmentswith36
physiciansand3advancedpracticenurses(23women[59.0%]and16men[41.0%])completedthe
previsitquestionnaire(431[95.4%]withassistance)andcarriedaconcealedaudiorecorderintotheir
visit.Patientdemographiccharacteristicswereextractedfromtheclinicaldatawarehouseateach
siteusingpatientidentifiers.Wecomparedraceandethnicity,alongwithotherdemographics,
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 5/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
betweenthecontrolandinterventiongroupstoensurethatgroupswerebalancedastothese
characteristics,whichhavebeenpreviouslyassociatedwithdifferencesinhealthcare.Asshownin
theFigure,275visitswererandomizedtothecontrolgroupand177totheinterventiongroup.Seven
patientshad2visitsscheduledduringthecourseofthestudy;eachvisitwasindividuallyrandomized.
Table2presentsuniquepatientcharacteristicsbystudygroupatthefirstvisit;patientsdidnotdiffer
betweengroupsindemographiccharacteristics,numbersofredflagsavailablebeforeorduringthe
visit,orwhethertheychosetorevealtheaudiorecorderorkeepitconcealed.Table3provides
physiciandemographiccharacteristics.
Figure.StudyFlowchart
570Patient visits assessed for eligibility
118Declined to participate
452Randomized
| 275Randomized to control group and  |     | 177Randomized to intervention group  |     |
| ----------------------------------- | --- | ------------------------------------ | --- |
| received allocated intervention     |     | and received allocated intervention  |     |
| 160Site 1                           |     | 118Site 1                            |     |
| 115Site 2                           |     | 59Site 2                             |     |
0Lost to follow-up 0Lost to follow-up
Flowofpatientsthroughtheclinicaldecisionsupport
| 275Included in the analysis |     | 177Included in the analysis |     |
| --------------------------- | --- | --------------------------- | --- |
interventiontopreventcontextualerrorstrial.
Table2.ParticipantCharacteristics
Studygroupa
| Characteristic | Control(n=271) | Intervention(n=176) | All(n=447) |
| -------------- | -------------- | ------------------- | ---------- |
Site
| 1   | 159(58.7) | 118(67,0) | 277(62.0) |
| --- | --------- | --------- | --------- |
| 2   | 112(41.3) | 58(33.0)  | 170(38.0) |
Sex
| Women           | 181(66.8)  | 110(62.5)  | 291(65.1)  |
| --------------- | ---------- | ---------- | ---------- |
| Men             | 90(33.2)   | 66(37.5)   | 156(34.9)  |
| Age,mean(SD),yb | 55.6(15.5) | 55.6(14.5) | 55.6(15.1) |
Raceandethnicityb
| Asian                                  | 6(2.2)    | 4(2.3)   | 10(2.3)   |
| -------------------------------------- | --------- | -------- | --------- |
| Black                                  | 132(49.1) | 79(45.1) | 211(47.5) |
| Hispanic                               | 41(15.2)  | 30(17.1) | 71(16.0)  |
| White                                  | 72(26.8)  | 52(29.7) | 124(27.9) |
| Otherc                                 | 18(6.7)   | 10(5.7)  | 28(6.3)   |
| No.ofredflagspervisit,mean(SD)         | 3.9(2.4)  | 4.0(2.3) | 3.9(2.4)  |
| Onlyreportedcontextualredflagonpatient | 78(28.4)  | 57(32.2) | 135(29.9) |
questionnaire Abbreviation:EHR,electronichealthrecord.
Onlyhadacontextualredflagthatcouldbe 33(12.0) 18(10.2) 51(11.3) aUnlessindicatedotherwise,dataareexpressedas
extractedfromtheEHR
No.(%)ofpatients.Percentageshavebeenrounded
| Contextualredflagbothreportedon | 140(50.9) | 87(49.1) | 227(50.2) |
| ------------------------------- | --------- | -------- | --------- |
andmaynottotal100.
questionnaireandextractedfromEHR
bDatawerenotavailablefor2controlpatientsand1
Revealedaudiorecorder
interventionpatient.
| Yes | 49(18.1) | 28(15.9) | 77(10.2) |
| --- | -------- | -------- | -------- |
cIncludesdoesnotfitavailablecategories,prefersnot
| No  | 222(81.9) | 148(84.1) | 370(82.8) |
| --- | --------- | --------- | --------- |
toanswer,orunknown.
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 6/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
Outcomes
Table4summarizesthemainoutcomesofthestudy(inSupplement2,eAppendix5presentsraw
studyoutcomesbygroup;Table1ineAppendix6presentsregressionmodels).Fortheprimaryend
point,thestudygroupdidnothaveadditionalsignificantimpactonoutcomesbeyonditsimpacton
plans(adjustedoddsratio[aOR]forimprovement,0.96[95%CI,0.57-1.63;P=.88];aORfor
worsening,1.31[95%CI,0.84-2.04;P=.86)(Table4).However,acrossgroups,contextualizedplans
wereassociatedwithasignificantlyhigherlikelihoodofanimprovedredflagoutcome(aOR,2.13
[95%CI,1,38-3.28];P=.001)(Table1ineAppendix6inSupplement2),andasignificantlylower
likelihoodofaworsenedredflagoutcome(aOR,0.67[95%CI,0.45-0.99];P=.046).Theordered
logitmodelproducedthesameconclusions(proportionaloddsaORassociatedwithcontextualized
plan,1.76[95%CI,1.23-2.50];P=.002).
Physiciansintheinterventiongroupweremorelikelytoproberedflagsthanphysiciansinthe
controlgroup(aOR,2.12[95%CI,1.14-3.93];P=.02)(Table4).Inaddition,redflagsselectedonthe
previsitquestionnairewerelesslikelytobeprobedthanthoseexpressedorallyduringthevisit(aOR,
0.15[95%CI,0.07-0.30];P<.001)(Table1ineAppendix6inSupplement2).Therewasnoeffect
ofwhethertherecorderwasvisibleorconcealed(aOR,1.57[95%CI,0.63-3.96];P=.34).eAppendix
7inSupplement2showstheproportionofcontextualredflagsprobedbyaclinician,theproportion
Table3.ClinicianCharacteristics
Data(n=39)a
Characteristic
Sex
| Women |     |     | 23(59.0) |     |
| ----- | --- | --- | -------- | --- |
| Men   |     |     | 16(41.0) |     |
Raceandethnicity
| Asian                                     |     |     | 6(15.4)             |     |
| ----------------------------------------- | --- | --- | ------------------- | --- |
| Black                                     |     |     | 5(12.8)             |     |
| Hispanic                                  |     |     | 4(10.3)             |     |
| White                                     |     |     | 23(59.0)            |     |
| MiddleEastern                             |     |     | 1(2.6)              |     |
| Yearofmedicalschoolgraduation,median(IQR) |     |     | 2003(1994.5-2011.5) |     |
Specialtyclinic
| Familymedicine   |     |     | 13(33.3) |     |
| ---------------- | --- | --- | -------- | --- |
| Internalmedicine |     |     | 26(66.7) |     |
Site
aIncludes36physiciansand3advancedpractice
| 1   |     |     | 26(66.7) |     |
| --- | --- | --- | -------- | --- |
nurses.Unlessindicatedotherwise,dataare
| 2   |     |     | 13(33.3) |     |
| --- | --- | --- | -------- | --- |
expressedasNo.(%)ofphysicians.
Table4.PatientOutcomes,ClinicianProbing,andClinicianContextualCarePlanningbyStudyGroup
Unadjustedrate,No./No.(%)
Effectsize,adjusted
|                                   | Controlgroup  | Interventiongroup | aOR(95%CI)a     | Pvalue |
| --------------------------------- | ------------- | ----------------- | --------------- | ------ |
| Outcome:improvementorresolutionof | 247/509(48.5) | 163/383(42.6)     | 0.96(0.57-1.63) | .88    |
redflagsat4-6mo,adjustedforwhether
clinicianincorporatedcontextualfactor
| Probing:clinicianprobescontextualred | 271/540(50.2) | 215/362(59.4) | 2.12(1.14-3.93) | .02 |
| ------------------------------------ | ------------- | ------------- | --------------- | --- |
flags
| Planning:clinicianincorporates | 255/509(50.1) | 221/383(57.7) | 2.67(1.32-5.41) | .006 |
| ------------------------------ | ------------- | ------------- | --------------- | ---- |
contextualfactorsintocareplan
Abbreviation:aOR,adjustedoddsratio.
aAllmodelswereadjustedforrandomeffectsofvisit,patient,andclinicianandfixedeffectsofstudysite.Theprobing
modelalsoadjustedforwhetherthepatientindicatedacontextualfactorontheprevisitquestionnaireandwhether
patientchosetomakerecordervisibletotheclinician.Theplanningmodelalsoadjustedforwhetherthepatient
indicatedacontextualfactorontheprevisitquestionnaire,whetherthepatientchosetomakerecordervisibletothe
clinician,whethertheclinicianidentifiedthecontextualfactorbyprobingaredflag,whetherthepatientspontaneously
revealedthecontextualfactor,andtheinteractionbetweenwhethertheclinicianprobedandwhethertherecorder
wasvisible.
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 7/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
ofcontextualredflagsforwhichacontextualfactorwasnotedbythe4Ccoders,andtheproportion
ofthosecontextualfactorsaddressedinthecareplan(ie,thecontextualizationofcareratebytypes
offlagsinthecontrolandinterventiongroups).Alistof106redflagsintheothercategoryisincluded
ineAppendix8inSupplement2.Overall,215of362contextualredflags(59.4%)wereprobedinthe
interventiongroup,comparedwith271of540(50.2%)inthecontrolgroup.Contextualfactorswere
identifiedin196of362(54.1%)intheinterventiongroupcomparedwith258of540(47.8%)ofthem
inthecontrolgroup,respectively.Overall,156of196contextualfactorswithpresentingredflags
(79.6%;156ofall383contextualfactors[40.7%])wereelicitedintheinterventiongroupcompared
with180of258(69.8%;180ofall509contextualfactors[35.4%])inthecontrolgroup.
Factorsintheinterventiongrouphadahigherlikelihoodofincorporationintothecareplan
(aOR,2.67[95%CI,1.32-5.41];P=.006)(Table4).Asinpaststudies,factorsidentifiedthrough
probingwereadditionallymuchmorelikelytobeincorporatedintocareplansthanthosethatwere
not(aOR,61.65[95%CI,21.92-173.42];P<.001)(Table1ineAppendix6inSupplement2).17Factors
spontaneouslyrevealedbypatientswerealsomorelikelytobeincorporated(aOR,8.55[95%CI,
3.98-18.36];P<.001),butfactorsselectedbypatientsontheprevisitquestionnairewerenot(aOR,
1.42[95%CI,0.57-3.54];P=.45).Therewasnoeffectofwhethertherecorderwasvisibleor
concealed(aOR,0.86[95%CI,0.28-2.66];P=.79).Figure1ineAppendix9inSupplement2
summarizestheresultsofthemodelsasapathanalysisandillustratesthedirectandindirecteffects
oftheinterventiononcontextualprobing,identificationofcontextualfactors,contextualizationof
careplans,andpatientoutcomes.
ImpactofEHRAlerts
WhentheEHRpopulatedtheCCBoractivatedalertsforredflagsbeforethestartofthevisit(ie,from
thepatientquestionnaireorEHRtriggers),thelikelihoodoftheclinicianprobingtheredflag
increasedsignificantly(aOR,3.64[95%CI,1.18-11.20];P=.02),andwhenafactorwaspresent,the
likelihoodofincorporatingitintothecareplanalsoincreased(aOR,11.27[95%CI,2.27-55.85];
P=.003).Inaddition,whentheredflagwasthesubjectofanalert,itwaslesslikelytohave
worsened4monthslater(aOR,0.19[95%CI,0.05-0.73];P=.02)butnotmorelikelytohavebeen
improved(aOR,0.75[95%CI,0.30-1.89];P=.55),beyondtheeffectofwhetherthecareplanhad
beencontextualized.Tables2and3ineAppendix6inSupplement2presenttheregression
coefficientsformodelsexploringtheeffectofEMRCCBandalertsininterventiongroupvisitsandall
visits,respectively.
Discussion
Inthisrandomizedclinicaltrial,CDStoolsdidnotimprovepatientoutcomes;however,thesetools
increasedthelikelihoodthataphysicianwouldaddressrelevantpatientlifecontextintheircareplan.
Asseeninpreviousstudies,thesecontextualizedcareplansweremorelikelytoresultinimproved
prospectivelydefinedpatienthealthcareoutcomes.
Althoughithasbeenpreviouslyestablishedthatcontextualerrorsarecommon,thatthey
adverselyaffectpatientoutcomes,andthatclinicianscanlearntomakefewerofthemwith
feedback,8thisisthefirststudy,toourknowledge,todemonstratethatCDStoolsbuiltintotheEHR
candecreasecontextualerrors.JustasCDScanguidebiomedicallyfocuseddecision-makingby
drawingondatafromevidence-basedguidelinesandotherformsofresearchevidence,itcanalso
guidecontextuallyinformeddecisionmakingbydrawingondataspecifictothelifecircumstances
andbehaviorsofindividualpatients.18
ContextualizedCDScanserveasacorrectivetobiomedicalbiasinwhichcliniciansprioritize
biomedicalinformationovercontextualinformation,evenwhentheyhavecomparableimplications
forapatient’sclinicalstate.7Forinstance,Weiner19describedapatientwhohad3unnecessaryvisits
totheemergencydepartmentwithacuteillnessbecauseshemissedherhemodialysisandnoone
askedherwhy.Itturnedoutthatshewastrappedinasituationbeyondhercontrolthatwaseasily
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 8/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
resolvedwiththehelpofasocialworker.WeinerandSchwartz2havedocumentedhundredsof
similarexamples.
ThecapacityofcontextualizedCDStochangeoutcomesislimited,toavaryingdegree,bythe
resourcesavailabletohelppatientsandthecontextualfactor.Inpriorwork,Binns-Calvey20
identified12broadcontextualdomains,withwidelydifferentresourceneeds.Forinstance,apatient
strugglingwithagapinknowledgeorskills(eg,misunderstandingabouthowtouseaninhaler)may
needonlyafewminutesoftheclinician’stimeandguidance,whereasapatientwithatransportation
needmayrequireassistancethatonlysomeclinicscanprovide.
ThefindingthatphysicianspaylessattentiontocontextualredflagspresentedtothembyCDS
thanthosepresenteddirectlybythepatientpointstoalimitationofthistechnology.Thefindingis
consistentwithpriorworkrevealingthatclinicianspaylessattentiontowrittencomparedwithorally
presentedcontextualinformation.11
ContextualizedCDShastheadvantageofbeingreadilyscalable.Futureworkshouldassessthe
effectivenessoftheCDSwhenpatientsdonothavetheoptiontorequestassistancecompletingthe
questionnaire,becauseweretheynotto,theCDSwoulddefaulttorelyingonlyondataculledfrom
themedicalrecord.
Limitations
Thisstudyhassomelimitations.Althoughthedispositionofsomeredflags,suchasthenumbersof
missedappointmentsorglycatedhemoglobinlevels,couldbecodedobjectively,otheroutcomes,
suchasapatient’sreportofwhethertheyareexercisingmore,areinherentlysubjective.Because
codersareblindedastostudygroup,thislimitationshouldnotskewtheresults.Itwasnotpossible,
however,toblindclinicianstostudygroupbecausetheycantellwhentheyarereceiving
contextualizedCDS.21Itispossiblethatclinicianstryharderintheintervention,independentofthe
CDS.Weattemptedtomitigateanyeffectbyexplainingtocliniciansthattherewouldbenoanalysis
ofhowtheyindividuallyperform.Furthermore,thelackofaneffectofthevisiblerecorderon
clinicianprobingsuggeststhattheywerenotmotivatedtochangetheirbehaviorjustbecausethey
knewtheywereinastudy.
Finally,therealeffectoftheinterventionmaybelargerthanwhatwasfound,becausewehad
patientsinbothstudygroupscompletethequestionnaire,whichmayhaveprimedthoseinthe
controlgrouptoraisecontextualredflagsandfactors.Wedesignedthestudythiswaysowewould
notattributeimpacttotheCDSthatwasreallyfromthequestionnaire.
Conclusions
Informationaboutpatients’lifecircumstancesandbehaviors(ie,patientlifecontext)isessentialto
identifyandaddressincareplanningtoachievedesiredoutcomes;however,itisoftenoverlooked.
ThefindingsofthisrandomizedclinicaltrialsupporttheuseofCDStoolsthatdrawondataelicited
directlyfromthepatientbeforethevisitandfromtheEHRtofacilitatedecision-makingthat
improvescontextualizationofcare.
ARTICLEINFORMATION
AcceptedforPublication:September8,2022.
Published:October24,2022.doi:10.1001/jamanetworkopen.2022.38231
OpenAccess:ThisisanopenaccessarticledistributedunderthetermsoftheCC-BYLicense.©2022WeinerSJ
etal.JAMANetworkOpen.
CorrespondingAuthor:SaulJ.Weiner,MD,UniversityofIllinoisChicagoCollegeofMedicine,840SWoodSt,
CSNRoom445,Chicago,IL60612(sweiner@uic.edu).
AuthorAffiliations:DepartmentofMedicine,CollegeofMedicine,UniversityofIllinoisChicago(Weiner,Galanter,
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 9/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
Binns-Calvey,Saini);MedicalServices,JesseBrownDepartmentofVeteransAffairs(VA)MedicalCenter,Chicago,
Illinois(Weiner,Binns-Calvey,Saini);CenterofInnovationforComplexChronicHealthcare,EdwardHines,JrVA
Hospital,Hines,Illinois(Weiner,Weaver,Binns-Calvey);DepartmentofMedicalEducation,CollegeofMedicine,
UniversityofIllinoisChicago(Schwartz);ParkinsonSchoolofHealthSciencesandPublicHealth,LoyolaUniversity
Chicago,Maywood,Illinois(Weaver);UniversityofIllinoisCancerCenter,CollegeofMedicine,UniversityofIllinois
Chicago(Olender);DepartmentofFamilyandCommunityMedicine,CollegeofMedicine,UniversityofIllinois
Chicago(Kochendorfer);ClinicalResearchOffice,HealthSciencesCampus,LoyolaUniversityChicago,Maywood,
Illinois(Iqbal);DignityHealth,PacificCentralCoastHealthCenters,ArroyoGrande,California(Diaz);Department
ofFamilyMedicine,StritchSchoolofMedicine,LoyolaUniversityChicago,Maywood,Illinois(Michelfelder);Loyola
UniversityHealthSystem,Chicago,Illinois(Michelfelder);OakStreetHealth,EastPoint,Georgia(Varkey).
AuthorContributions:DrsWeinerandSchwartzhadfullaccesstoallofthedatainthestudyandtake
responsibilityfortheintegrityofthedataandtheaccuracyofthedataanalysis.
Conceptanddesign:Weiner,Schwartz,Weaver,Galanter,Olender,Kochendorfer,Diaz.
Acquisition,analysis,orinterpretationofdata:Schwartz,Galanter,Olender,Kochendorfer,Binns-Calvey,Saini,
Iqbal,Michelfelder,Varkey.
Draftingofthemanuscript:Weiner,Diaz.
Criticalrevisionofthemanuscriptforimportantintellectualcontent:Allauthors.
Statisticalanalysis:Schwartz.
Obtainedfunding:Weiner,Galanter.
Administrative,technical,ormaterialsupport:Weaver,Galanter,Olender,Kochendorfer,Binns-Calvey,Saini,Iqbal,
Diaz,Varkey.
Supervision:Weiner,Weaver,Galanter,Olender,Kochendorfer.
ConflictofInterestDisclosures:DrWeinerreportedbeingacofounderoftheInstituteforPracticeandProvider
PerformanceImprovement,whichemployssomeofthesamedataanalysismethodsusedinthisstudybutwasnot
involvedorassociatedwiththisstudy.DrSchwartzreportedbeingacofounderoftheInstituteforPracticeand
ProviderPerformanceImprovementoutsidethesubmittedwork.DrGalanterreportedreceivinggrantsfromthe
USgovernmentduringtheconductofthestudy.DrBinns-CalveyreportedconsultingfortheInstituteforPractice
andProviderPerformanceImprovementoutsidethesubmittedwork.Nootherdisclosureswerereported.
Funding/Support:Thisstudywassupportedbygrant1R01HS025374-01fromtheAHRQ.
RoleoftheFunder/Sponsor:Thesponsorhadnoroleinthedesignandconductofthestudy;collection,
management,analysis,andinterpretationofthedata;preparation,review,orapprovalofthemanuscript;and
decisiontosubmitthemanuscriptforpublication.
Disclaimer:Theviewsexpressedinthisarticlearethoseoftheauthorsanddonotnecessarilyreflecttheposition
orpolicyoftheDepartmentofVeteransAffairsortheUSgovernment.
DataSharingStatement:SeeSupplement3.
AdditionalContributions:ClaraRyan,MS(deceased),formermedicalstudentattheUniversityofIllinoisChicago
CollegeofMedicine,assistedwithdatacollectionanddataanalysis.ThomasKannampallil,PhD,ComputerScience
andEngineering,SchoolofEngineeringandAppliedScience,WashingtonUniversitySchoolofMedicineinStLouis,
assistedwithclinicaldecisionsupport(CDS)designanddataextraction.JoshuaLee,MD,BannerHealth,assisted
withCDSrulesat1site.JeanneCerceo,BA,LoyolaUniversityMedicalCenter,assistedwithlookingupcontextual
redflags.CarolinaRuizGuerrero,medicalstudentatPanAmericanUniversitySchoolofMedicine,translated
transcriptsofvisitsinSpanishtoEnglish.KamelAzhar,MD,EisenhowerHealth,assistedwithtestingand
troubleshootingCDSrules.ZacharySonnier,DO,HealthInformaticsDivision,DefenseHealthAgency,assistedwith
CDSrules.WiththeexceptionofMsRyan,whoreceivedastipend,thesecontributorswerenotcompensated
beyondreceiptofgrantfundingtotheirinstitutions.
REFERENCES
1. WeinerSJ.Contextualizingcare:anessentialandmeasurableclinicalcompetency.PatientEducCouns.2022;
105(3):594-598.doi:10.1016/j.pec.2021.06.016
2. WeinerSJ,SchwartzA.ListeningforWhatMatters:AvoidingContextualErrorsinHealthCare.OxfordUniversity
Press;2016.
3. WeinerSJ.Contextualizingmedicaldecisionstoindividualizecare:lessonsfromthequalitativesciences.JGen
InternMed.2004;19(3):281-285.doi:10.1111/j.1525-1497.2004.30261.x
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 10/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
4. WeinerSJ,SchwartzA,YudkowskyR,etal.Evaluatingphysicianperformanceatindividualizingcare:apilot
studytrackingcontextualerrorsinmedicaldecisionmaking.MedDecisMaking.2007;27(6):726-734.doi:10.1177/
0272989X07306113
5. WeinerS,SchwartzA,AltmanL,etal.Evaluationofapatient-collectedaudioauditandfeedbackquality
improvementprogramonclinicianattentiontopatientlifecontextandhealthcarecostsintheVeteransAffairs
healthcaresystem.JAMANetwOpen.2020;3(7):e209644.doi:10.1001/jamanetworkopen.2020.9644
6. WeinerSJSA,SchwartzA,SharmaG,etal.Patient-centereddecisionmakingandhealthcareoutcomes:an
observationalstudy.AnnInternMed.2013;158(8):573-579.doi:10.7326/0003-4819-158-8-201304160-00001
7. WeinerSJ,SchwartzA,WeaverF,etal.Contextualerrorsandfailuresinindividualizingpatientcare:
amulticenterstudy.AnnInternMed.2010;153(2):69-75.doi:10.7326/0003-4819-153-2-201007200-00002
8. WeinerSJ,SchwartzA.Contextualerrorsinmedicaldecisionmaking:overlookedandunderstudied.AcadMed.
2016;91(5):657-662.doi:10.1097/ACM.0000000000001017
9. WeinerSJ.Contextualerror.In:KattanM,ed.EncyclopediaofMedicalDecisionMaking.SAGE;2009:198-202.
10. OsheroffJA;HealthcareInformationandManagementSystemsSociety.ImprovingOutcomesWithClinical
DecisionSupport:AnImplementer’sGuide.2nded.HIMSS;2012.doi:10.4324/9781498757461
11. WeaverFM,Binns-CalveyA,GonzalezB,etal.Alertingdoctorsaboutpatientlifechallenges:arandomized
controltrialofaprevisitinventoryofcontextualfactors.MDMPolicyPract.2019;4(1):2381468319852334.doi:10.
1177/2381468319852334
12. CoZ,HolmgrenAJ,ClassenDC,etal.Thetradeoffsbetweensafetyandalertfatigue:datafromanational
evaluationofhospitalmedication-relatedclinicaldecisionsupport.JAmMedInformAssoc.2020;27(8):
1252-1258.doi:10.1093/jamia/ocaa098
13. Binns-CalveyAE,SharmaG,AshleyN,KellyB,WeaverFM,WeinerSJ.Listeningtothepatient:atypologyof
contextualredflagsindiseasemanagementencounters.JPatientCentResRev.2020;7(1):39-46.doi:10.17294/
2330-0698.1725
14. WeinerSJ,AshleyN,Binns-CalveyA,KellyB,SharmaG,SchwartzA.Contentcodingforcontextualizationof
caremanual.HarvardDataverse,version12.0.PublishedMay27,2021.AccessedOctober5,2022.https://dataverse.
harvard.edu/dataverse/4C
15. WeinerSJ,KellyB,AshleyN,etal.Contentcodingforcontextualizationofcare:evaluatingphysician
performanceatpatient-centereddecisionmaking.MedDecisMaking.2014;34(1):97-106.doi:10.1177/
0272989X13493146
16. WeinerSJ,SchwartzA,SharmaG,etal.Patient-collectedaudioforperformanceassessmentoftheclinical
encounter.JtCommJQualPatientSaf.2015;41(6):273-278.doi:10.1016/S1553-7250(15)41037-2
17. SchwartzA,WeinerSJ,Binns-CalveyA,WeaverFM.Providerscontextualisecaremoreoftenwhenthey
discoverpatientcontextbyasking:meta-analysisofthreeprimarydatasets.BMJQualSaf.2016;25(3):159-163.
doi:10.1136/bmjqs-2015-004283
18. SuttonRT,PincockD,BaumgartDC,SadowskiDC,FedorakRN,KroekerKI.Anoverviewofclinicaldecision
supportsystems:benefits,risks,andstrategiesforsuccess.NPJDigitMed.2020;3:17.doi:10.1038/s41746-020-
0221-y
19. WeinerSJ.Advancinghealthequitybyavoidingjudgmentalismandcontextualizingcare.AMAJEthics.2021;
23(2):E91-E96.doi:10.1001/amajethics.2021.91
20. Binns-CalveyAE,MalhiotA,KostovichCT,etal.Validatingdomainsofpatientcontextualfactorsessentialto
preventingcontextualerrors:aqualitativestudyconductedatChicagoAreaVeteransHealthAdministrationsites.
AcadMed.2017;92(9):1287-1293.doi:10.1097/ACM.0000000000001659
21. McCambridgeJ,WittonJ,ElbourneDR.SystematicreviewoftheHawthorneeffect:newconceptsareneeded
tostudyresearchparticipationeffects.JClinEpidemiol.2014;67(3):267-277.doi:10.1016/j.jclinepi.2013.08.015
SUPPLEMENT1.
TrialProtocol
SUPPLEMENT2.
eAppendix1.PortalQuestionnaire
eAppendix2.ContextualCareBox
eAppendix3.InterruptiveAlert
eAppendix4.CDSDesignProcess
eAppendix5.RawData
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 11/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026

JAMANetworkOpen | HealthInformatics EffectofEHRClinicalDecisionSupportonContextualizationofCare
eAppendix6.RegressionTables
eAppendix7.ClinicianPerformanceinInterventionvsControl
eAppendix8.ContextualRedFlags,“Other”Category
eAppendix9.PathAnalyticSummaryofMultivariateModels
SUPPLEMENT3.
DataSharingStatement
JAMANetworkOpen.2022;5(10):e2238231.doi:10.1001/jamanetworkopen.2022.38231 (Reprinted) October24,2022 12/12
Downloaded from jamanetwork.​com by guest on 10/​19/​2026
