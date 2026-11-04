JournaloftheAmericanMedicalInformaticsAssociation,29(9),2022,1461–1470
https://doi.org/10.1093/jamia/ocac085
AdvanceAccessPublicationDate:31May2022
ResearchandApplications
Research and Applications
Using CDS Hooks to increase SMARTon FHIR app
utilization: a cluster-randomized trial
KeatonL.Morgan 1,2,PolinaV.Kukhareva 1,PhillipB.Warner1,JonahWilkof3,
MeirSnyder3,DevinHorton 4,TroyMadsen 2,JosephHabboushe3,and
KensakuKawamoto 1
1DepartmentofBiomedicalInformatics,UniversityofUtah,SaltLakeCity,Utah,USA,2DepartmentofEmergencyMedicine,Uni-
versityofUtah,SaltLakeCity,Utah,USA,3MDCalc(MDAware,LLC),NewYork,NewYork,USAand and 4DepartmentofInternal
Medicine,UniversityofUtah,SaltLakeCity,Utah,USA
CorrespondingAuthor:KeatonMorgan,MD,MS,AssistantProfessor,DepartmentofBiomedicalInformatics,University
ofUtah,421WakaraWay,Suite140,SaltLakeCity,UT84108,USA;keaton.morgan@utah.edu
Received8March2022;Revised15May2022;EditorialDecision16May2022;Accepted18May2022
ABSTRACT
Objective:HL7SMARTonFHIRappshavethepotentialtoimprovehealthcaredeliveryandEHRusability,but
providers mustbe awareof the apps anduse them for these potentialbenefitsto be realized.TheHL7CDS
Hooksstandardwasdevelopedinpartforthispurpose.Theobjectiveofthisstudywastodetermineifcontextu-
allyrelevantCDSHookspromptscanincreaseutilizationofaSMARTonFHIRmedicalreferenceapp(MDCalc
forEHR).
MaterialsandMethods:Weconducteda7-month,provider-randomizedtrialwith70providersinasingleemer-
gencydepartment.TheinterventionwasacollectionofCDSHookspromptssuggestingtheuseof6medical
calculatorsinaSMARTonFHIRmedicalreferenceapp.Theprimaryoutcomewasthepercentageofprovider–
patientinteractionsinwhichtheappwasusedtoviewarecommendedcalculator.Secondaryoutcomeswere
appusagestratifiedbyindividualcalculators.
Results:Interventiongroupprovidersviewedastudycalculatorintheappin6.0%ofinteractionscomparedto
2.6%inthecontrolgroup(oddsratio¼2.45,95%CI,1.2–5.2,Pvalue.02),anincreaseof130%.Appusewassig-
nificantlygreaterfor2of6calculators.
DiscussionandConclusion:ContextuallyrelevantCDSHookspromptsledtoasignificantincreaseinSMART
onFHIRapputilization.ThisdemonstratesthepotentialofusingCDSHookstoguideappropriateuseofSMART
onFHIRappsandwasaprimarymotivationforthedevelopmentofthestandard.Futureresearchmayevaluate
potentialimpactsonclinicalcaredecisionsandoutcomes.
Keywords:SMARTonFHIR,CDSHooks,clinicaldecisionsupport,electronichealthrecords,standards
BACKGROUNDANDSIGNIFICANCE
health record (EHR) system.1 SMART on FHIR has seen a quick
TheHealthLevelSevenInternational(HL7)SubstitutableMedical rise in adoption,2 and the development of an extensive EHR app-
Applications,ReusableTechnologies(SMART)onFastHealthcare basedecosystemappearstobeonthehorizon.
Interoperability Resources (FHIR) standard allows for a standard The proliferation of SMART on FHIR apps creates a need for
method for launching external applications from an electronic suggesting relevant apps to end-users. Among the reasons for this
VCTheAuthor(s)2022.PublishedbyOxfordUniversityPressonbehalfoftheAmericanMedicalInformaticsAssociation.
Allrightsreserved.Forpermissions,pleaseemail:journals.permissions@oup.com
1461

1462 JournaloftheAmericanMedicalInformaticsAssociation,2022,Vol.29,No.9
need, clinical decision support (CDS) is generally more effective Inthisstudy,weconceivedandconductedthefirstRCTtofor-
whenitispresentedatthetimeandlocationofdecision-makingand mallyevaluatetheuseofCDSHookstoprovideclinicalcarerecom-
withintheclinician’sworkflow.3,4Thus,suggestingtheuseofadd- mendations. Inaddition,thisrepresentsthefirstformalevaluation
onappsintherightclinicalcontextscouldimprovetheiruseandim- ofusingCDSHookstosuggestaSMARTonFHIRapp.Wehypoth-
pact.Anothermotivationforsuggestingappstousersatappropriate esized that contextually relevant CDS Hooks prompts would in-
timesisthattheproliferationofSMARTonFHIRappscouldresult creaseappropriateuseofaSMARTonFHIRapp.
inappfatigue,wheretherearetoomanyavailableappsfortheend-
usertochoosefrom,leadingtotheappsbeinglargelyignored.5This
OBJECTIVE
isakintowhathasincreasinglyoccurredtoCDSalerts,intheform
ofalertfatigue.6RecommendingarelevantSMARTonFHIRappin
Theobjectiveofthisstudywastodetermineifcontextuallyrelevant
real-time and within the right clinical context could help address CDSHookspromptscanincreaseutilizationof6 medicalcalcula-
bothoftheseissues.
|     |     |     |     |     |     |     | tors in a | SMART on FHIR | medical | reference | app | (MDCalc for |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ------- | --------- | --- | ----------- |
LikeSMARTonFHIR,CDSHooksisaFHIR-basedHL7stan-
EHR).TherewereadditionalclinicalobjectivesrelatedtotheCDS
dardfordeliveringCDS,andaprimarymotivationbehinditsdevel- system,butthesewereoutsidethescopeofthispublication.
opmentwastorecommendrelevantSMARTonFHIRappstoend-
users.7InCDSHooks,theCDSserviceistriggeredbya“hook”and
theCDSlogicisexecutedusingdataexchangedviatheFHIRstan- MATERIALSANDMETHODS
| dard. A CDS | card | is then returned |     | to the | EHR, where | it provides |     |     |     |     |     |     |
| ----------- | ---- | ---------------- | --- | ------ | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
Studydesign
careguidancebydisplayingacombinationoftext,alternativesug- Thisstudywasacluster-randomizedclinicaltrialinvolvingresident
gestionsand/orlinkstoappsorreferencematerialtotheend-user.8
|     |       |                |     |           |     |              | physicians | and advanced practice | providers |     | (APPs). | We deployed |
| --- | ----- | -------------- | --- | --------- | --- | ------------ | ---------- | --------------------- | --------- | --- | ------- | ----------- |
| CDS | Hooks | is a promising |     | mechanism | for | recommending |            |                       |           |     |         |             |
theCDSHooksserviceonFebruary17,2021anddiscontinuedthe
| SMART | on FHIR | apps for | several | reasons. | First, | like SMART on |     |     |     |     |     |     |
| ----- | ------- | -------- | ------- | -------- | ------ | ------------- | --- | --- | --- | --- | --- | --- |
serviceonNovember18,2021becausestudyenrollmentgoalswere
FHIR,CDSHooksusesFHIRasitsdatamodelandexchangestan-
|     |     |     |     |     |     |     | met. Since | first-year and non-emergency |     | medicine | (“off-service”) |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------------------- | --- | -------- | --------------- | --- |
dard.Thisreducestheburdenofdevelopment,sincethesamelogic residentphysiciansseeonaveragefewerpatientspershift,14weran-
canbesharedbetweentheCDSHooksserviceandtheapp.Second,
|           |           |      |       |         |       |               | domizedthem | separately. Randomization |     | wasperformedtwice, |     | at  |
| --------- | --------- | ---- | ----- | ------- | ----- | ------------- | ----------- | ------------------------- | --- | ------------------ | --- | --- |
| CDS Hooks | services, | like | SMART | on FHIR | apps, | can be shared |             |                           |     |                    |     |     |
thebeginningofthestudyinFebruary2021andinJune2021when
acrossEHRplatformsandhealthsystemsduetotheirinteroperable,
|              |         |       |     |                |     |                  | a new group | of resident physicians | was | on-boarded | at  | the institu- |
| ------------ | ------- | ----- | --- | -------------- | --- | ---------------- | ----------- | ---------------------- | --- | ---------- | --- | ------------ |
| EHR-agnostic | nature. | Thus, | CDS | promptinglogic |     | that is too time |             |                        |     |            |     |              |
tion.Aprovider-randomizeddesignwaschosenduetopatientsafety
consuming to reimplement at each health system could potentially concerns with randomizing by patient, since in a patient-
| be broadly | shared | via CDS | Hooks | services, | just as | the associated |            |                   |       |         |         |          |
| ---------- | ------ | ------- | ----- | --------- | ------- | -------------- | ---------- | ----------------- | ----- | ------- | ------- | -------- |
|            |        |         |       |           |         |                | randomized | design a provider | would | see the | prompts | for some |
SMARTonFHIRappscanbesharedinthisway.Third,theuseof
patientswhomeetcriteriabutnotothers.
anexternalCDSenginebyCDSHooksservicescanenabletheim-
ThisstudywasapprovedbytheUniversityofUtahInstitutional
| plementation | of  | more complex | decision | logic | than | can be imple- |              |                |     |                |     |              |
| ------------ | --- | ------------ | -------- | ----- | ---- | ------------- | ------------ | -------------- | --- | -------------- | --- | ------------ |
|              |     |              |          |       |      |               | Review Board | (IRB 00137874) | and | was registered |     | on Clinical- |
mented using native EHR CDS approaches. Finally, CDS Hooks Trials.gov(Identifier:NCT04702308).
includesafeaturetoprovideahyperlinktoaSMARTonFHIRapp
(“applinkcard”),allowingtheusertolaunchtheappfromtheCDS
Setting
Hookspromptwithasingleclick.
SeveralstudieshavedescribedhowCDSHookscanbeintegrated ThisstudywasconductedattheUniversityofUtahHealth(UUH)
recommendations.9–13 EmergencyDepartment(ED).UUHisanacademicmedicalcenterin
| into an EHR | to  | provide clinical | care |     |     | In the |     |     |     |     |     |     |
| ----------- | --- | ---------------- | ---- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
SaltLakeCity,UT.TheUUHEDhasanannualvolumeofapproxi-
majorityofthesestudies,theCDSHooksdeploymentswerelimited
mately50000patients.
todevelopmentplatforms.9–11TwostudiesdescribedtheuseofCDS
Hooks-basedCDSsystemsinproductionenvironments.Semenovet
al12 described a CDS platform implemented in a production envi- Studyparticipants
|     |     |     |     |     |     |     | Study participants | included | all emergency | medicine | (EM) | resident |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | -------- | ------------- | -------- | ---- | -------- |
ronment,buttheydidnotevaluatetheefficacyofthesystem.Rubin
|     |     |     |     |     |     |     | physicians, | any non-EM resident | physicians |     | who rotated | through |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------- | ---------- | --- | ----------- | ------- |
etaldeployedaCDSHooks-basedCDSsysteminaproductionenvi-
ronment to recommend HIV screening in patients where the HIV theEDduringthestudyperiodandallfull-timeEMAPPsworking
statuswasunknown.Theyperformedabefore-and-afterstudyand atthestudysite.Attendingphysicianswereexcludedfromthestudy
foundanactionwastakenbyproviderson1%oftheCDSHooks toavoidrandomizingmembersofthesameattending-residentteam
| reminders.13 |            |       |      |         |            |            | todifferentstudygroups. |     |     |     |     |     |
| ------------ | ---------- | ----- | ---- | ------- | ---------- | ---------- | ----------------------- | --- | --- | --- | --- | --- |
| To our       | knowledge, | there | have | been no | randomized | controlled |                         |     |     |     |     |     |
trials (RCTs) studying the use of CDS Hooks to provide clinical SixstudycalculatorsandMDCalcforEHRapp
carerecommendations.Inaddition,wearenotawareofanystudy We selected 6 clinical decision support rules (“study calculators”)
| evaluating | the use | of CDS | Hooks | to suggest | a SMART | on FHIR |     |     |     |     |     |     |
| ---------- | ------- | ------ | ----- | ---------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
fromthecalculatorsavailableontheMDCalcforEHRSMARTon
app. We believe this is a unique and important use case for CDS FHIRapp.MDCalcisapopularCDStoolcreatedbyMDAware.It
Hooks, because opening and using an application can take sub- containshundredsofmedicalcalculatorsandisusedbymorethan
stantially more clicks and effort than other responses to EHR 65%ofUSphysicianseverymonth.15Previously,theMDCalctool
prompts, such as ordering HIV screening laboratory tests with a wasonlyaccessibleviatheWeborasmartphoneapp.TheUniver-
singleclick.Thus,webelievethatidentifyinghowbesttofacilitate
sityofUtahpartneredwithMDAwaretocreateaSMARTonFHIR
the appropriate use of such apps is of specific importance, espe- versionthatisintegratedintheEHR.TheEHR-integratedappauto-
cially given the amount of time and resources required to develop fills calculator fields with relevant data from the EHR (Figure 1).
theseapplications. TheMDCalcforEHRapp(previouslycalledMDCalcConnect)was

JournaloftheAmericanMedicalInformaticsAssociation,2022,Vol.29,No.9 1463
Figure1.HeartScoreCalculatorintheMDCalcforEHRapp.
deployedat the studysite in September2018.It is availableto all recommendingtheuseofthestudycalculatorsweretodecreasethe
end-usersatthestudysiteandispinnedtothetopofthetoolbarfor numberofunnecessaryadvancedimagingstudiesperformedandto
all providers (physicians and APPs) (Figure 2, purple box). Addi- improve risk-stratification of associated medical conditions. For
tionalinformationontheMDCalcforEHRappcanbefoundina eachstudycalculator,analgorithmwasdevelopedby2EMattend-
previouspublication.5 ing physicians (KLM and JH) for identifying potentially relevant
The6studycalculatorswereselectedfromacombinationofper- patientsforwhomtosuggestuseofthecalculator.Theappsugges-
ceivedvalueandbestpracticerecommendationsfromtheAmerican tionalgorithmsusedacombinationofpatientlocation,chiefcom-
CollegeofEmergencyPhysicians.16Thecombinedclinicalgoalsof plaint,patientageand/orvitalsignsasdatainputs.Thealgorithms

1464 JournaloftheAmericanMedicalInformaticsAssociation,2022,Vol.29,No.9
Figure2.TwoCDSHookspromptsrecommendingtheuseoftheMDCalcforEHRSMARTonFHIRappandasamplehoverovermessage.
were intentionally designed to prioritize sensitivity over specificity All EM resident physicians received baseline education on the
(Table1). study at either a weekly education conference or during EHR on-
boarding training. For non-EM resident physicians and APPs, a
Intervention short(4-min)tutorialvideowasemailedtointerventiongrouppro-
The primary interventionwas a collection of noninterruptive CDS viders.Thevideoreviewedthemotivationforimplementingthecal-
Hooks prompts recommending the use of 6 medical calculators in culatorprompts,demonstratedtheappearanceofthepromptsand
theMDCalcforEHRapp(Table1).TheCDSHookspromptswere showedhowtoaccessthecalculatorsintheMDCalcforEHRapp.
showninaleft-handsummarycolumnofthepatientchartthatisal- Allparticipants,includingcontrolgroupproviders,hadaccessto
waysdisplayedwheninthecontextofanindividualpatient,referred theMDCalcforEHRapp.Theappfunctionedidenticallybetween
toasthe“Storyboard”intheEHRutilizedforthisstudy(Epic). the control and intervention groups with the exception of the
EachCDSHookspromptrecommendedtheuseofapotentially “SuggestedCalculators”landingpage,whichwasavailableonlyto
relevant calculator, and more than 1 prompt could be displayed. providers in the intervention group. To facilitate impact analysis,
The prompts consisted of a short title recommending the use of a theCDSHookssystemwasruninsilentmodeforthecontrolgroup,
singlecalculator(Figure2,redbox),alongwithahover-oversum- whereineachpatientwasevaluatedinthesamemannerastheinter-
maryofhowtoaccessthecalculatorintheMDCalcforEHRapp ventiongroupbutgeneratedpromptsweresuppressed.
(Figure2,greenbox).Ifthepromptwasclicked,apop-upversion
woulddisplaythesamesummaryalongwithaclickablehyperlink Systemarchitecture
thatwouldlaunchtheMDCalcforEHRapp(Figure3).Providers ThesystemarchitectureisshowninFigure5.The8stepsinvolved
could also access the app directly through the MDCalc tab in the in intervention group users’ interaction with CDS Hooks prompts
EHR(Figure2,purplebox). andtheSMARTonFHIRappareshowninthefigureanddescribed
A new landing page was built for the MDCalc for EHR app here.(1)TheEHRinvokestheCDSHooksservicewhenaclinician
(“Suggested Calculators,” Figure4) which recommended the same opensapatient’schart.(2)TheCDSHooksserviceretrievespatient
calculatorsastheCDSHookspromptstoalloweasyaccesstothe datafromtheEHRthroughtheEHR’sFHIRserver.(3)TheCDS
suggestedcalculators.Regardlessofhowtheyaccessedtheapp,in- Hooksserviceexecutestheappsuggestionalgorithmsusingthedata
terventionprovidersaccessingtheappwerealwayspresentedwith retrievedfromtheEHR’sFHIRserver.(4)Ifthepatientmeetscrite-
theSuggestedCalculatorslandingpageifthepatientmetcriteriafor ria,aprompttoconsiderappuseisdisplayedintheEHR(Figure2,
oneormoreprompts.Otherwise,thestandard“MyFavorites”land- redbox).Hoveringoverthepromptdisplaysadditionalinformation
ingpagewasdisplayed. (Figure2,greenbox).Ifthepromptisclicked,apop-upversiondis-

JournaloftheAmericanMedicalInformaticsAssociation,2022,Vol.29,No.9 1465
Table1.Appsuggestionalgorithms
Calculator Calculatorgoal Appsuggestioncriteria
CanadianCTheadrule Clearheadinjurywithoutimaging 1. LocatedintheED
2. Chiefcomplaintrelevanttoheadtrauma
3. Age(cid:2)16yoand<65yo
CanadianC-spinerule Clearcervicalspineinjurywithoutimaging 1. LocatedintheED
2. Chiefcomplaintrelevanttonecktrauma
3. Age(cid:2)16yoand<65yo
HEARTscore Riskstratifypatientswithundifferentiated 1. LocatedintheED
chestpain 2. Chief complaint relevant to chest pain or
shortnessofbreath
3. Age>40yo(chestpainchiefcomplaint)or
>50yo(shortnessofbreathchiefcomplaint)
PERCrule Ruleoutpulmonaryembolism(PE)without 1. LocatedintheED
imaging 2. ChiefcomplaintrelevanttoPE
3. Age(cid:2)18yoand<50yo
4. Peripheral oxygen saturation (SpO ) (cid:2)90%
2
and
5. Heartrate<100beatsperminute(bpm)
Wells’criteriaforPE RiskstratifypatientsbeingevaluatedforPE 1. LocatedintheED
2. ChiefcomplaintrelevanttoPE
3. Age(cid:2)18yo
4. SpO <90%
2
5. Heartrate(cid:2)100bpm
Wells’criteriafordeepvenousthrombosis(DVT) RiskstratifypatientsbeingevaluatedforDVT 1. LocatedintheED
2. ChiefcomplaintrelevanttoDVT
3. Age(cid:2)18yo
C-spine:cervicalspine;CT:computedtomography;DVT:deepvenousthrombosis;ED:emergencydepartment;PE:pulmonaryembolism;PERC:pulmonary
embolismrule-outcriteria;SpO2:peripheraloxygensaturation;yo:yearsold.
Figure3.SamplemessagethatdisplayswhentheproviderclicksontheCDSHooksprompt.SelectingthehyperlinkopenstheSuggestedCalculatorslanding
pageintheMDCalcforEHRapp(seeFigure4).
plays(Figure3).(5)Theusertriggersthelaunchoftheappbyclick- promptpriority(careguidance)didnotmeetthestudyinstitution’s
ingthehyperlinkintheCDSHookspop-upprompt(Figure3)orby typicalstandardforaninterruptivealert.Thus,itwasdesignedtobe
opening the app directly from the EHR toolbar (Figure 2, purple noninterruptive. Chart opening was the best trigger option for a
box). (6) The app is launched by the EHR using the SMART on noninterruptive prompt that ensured the provider would see the
FHIRprotocol.(7)TheappretrievesdataasneededviatheEHR’s promptpriortoorderentry.
FHIRserver.(8)TheMDCalcforEHRappisdisplayedtotheend- CDSHookssupportssingle-clickapplaunching,butthiswasnot
user,withtheappsuggestingthesamecalculatorsasrecommended implementedinoursystemarchitecture.Thisfeatureisavailablein
bytheCDSHooksprompts(Figure4). theEpicEHRforcertainprompttypes(eg,pop-upalerts)butnot
ChartopeningwaschosenastheCDStriggerduetoconstraints forStoryboardprompts,whichwereusedinthisstudy.Tolaunch
in displaying noninterruptive prompts prior to order entry. The the app, the user had to click on the Storyboard prompt, which

1466 JournaloftheAmericanMedicalInformaticsAssociation,2022,Vol.29,No.9
Figure4.SuggestedCalculatorslandingpageinMDCalcforEHR,whichsuggeststhesamecalculatorsastheCDSHookspromptsforinterventiongrouppro-
viders.
Figure5.CDSsystemarchitecture.
would launch a pop-up version of the prompt with the embedded Epicandhaverequestedthatthesingle-clickapplaunchingfeature
app hyperlink. Instructions on launchingthe app from the pop-up beaddedtotheStoryboardprompt.
message were included in the Storyboard prompt (Figure 2, green The CDS Hooks specification also supports deep linking to a
box),sincewefeltmostuserswouldnotknowhowtoaccessthehy- specificpageofanapp(eg,openingdirectlytoaspecificcalculator
perlinkintuitively.We havediscussedthis issue with colleaguesat intheMDCalcforEHRapp).Wewereunabletosuccessfullycon-

JournaloftheAmericanMedicalInformaticsAssociation,2022,Vol.29,No.9 1467
figurethisfeatureinourlocalEHRenvironmentpriortothestartof Table2.Studyparticipantsattimeofenrollment
thisstudy,butwehavesinceconfirmedthatitisanavailablefeature
|     |     |     |     |     |     |     |     |     | Control | Intervention |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | --- |
inEpic.Thepop-uppromptresponseoptions(AcceptandCancel,
|     |     |     |     |     |     |     |     |     | group | group |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- |
Figure3)areconfiguredbytheEHRvendor.Theoptionslistedde-
pendonwhatactions(ifany)areincludedintheprompt,andthey Numberofproviders 35 35
cannotbemodified.SelectingAcceptorCancelresultsintheprompt JuniorEMproviders 17 18
closing.SelectingtheapphyperlinkisconsideredequivalenttoAc- Non-EMresidentphysicians 9 8
| ceptandalsoclosestheprompt. |     |     |     |     |     | PGY-1EMresidentphysicians |     |     | 8   |     | 10  |     |
| --------------------------- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
|                             |     |     |     |     |     | SeniorEMProviders         |     |     | 18  |     | 17  |     |
|                             |     |     |     |     |     | APPs                      |     |     | 9   |     | 8   |     |
Studypower
|     |     |     |     |     |     | PGY-2/PGY-3EMresidentphysicians |     |     | 9   |     | 9   |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
Poweranalysiswasperformedpriortostudyinitiationusingthefol-
lowing variables: alpha¼0.05, power¼0.8, intraclass correlation APPs:advancedpracticeproviders;EM:emergencymedicine;PGY:post-
| coefficient | (ICC)¼0.3, proportion | of  | times the | control | group used | graduateyear. |     |     |     |     |     |     |
| ----------- | --------------------- | --- | --------- | ------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- |
theMDCalcforEHRapp¼0.1,proportionoftimestheexperiment
| group used | the app¼0.2, | and number | of study | subjects¼4000. |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ---------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Table3.Studypatientpopulation
Basedonthesenumbers,itwasdeterminedthatatleast60clusters
(providers)wouldbeneededtoadequatelypowerthestudy.AnICC Outcomes Controlgroup Interventiongroup
| of 0.3 was | estimated based | off recommendations |     |     | by Campbell |                  |     |     |      |     |      |     |
| ---------- | --------------- | ------------------- | --- | --- | ----------- | ---------------- | --- | --- | ---- | --- | ---- | --- |
|            |                 |                     |     |     |             | Numberofpatients |     |     | 3335 |     | 3424 |     |
etal.17Proportionsofappuseforthecontrolgroupwereestimated
|                    |           |          |                     |     |     | Numberofuniqueinteractions |     |     | 3776 |     | 3978 |     |
| ------------------ | --------- | -------- | ------------------- | --- | --- | -------------------------- | --- | --- | ---- | --- | ---- | --- |
| from retrospective | data. The | numberof | studysubjects(4000) |     | was |                            |     |     |      |     |      |     |
|                    |           |          |                     |     |     | CanadianCTheadrule         |     |     | 1058 |     | 1069 |     |
chosen because this was the estimated number of patients that CanadianC-spinerule 821 815
wouldmeetappsuggestioncriteriaina6-monthperiod.Allpower HEARTscore 1388 1536
calculationswereperformedusingtheRpowerClusterpackage(ver- PERCrule 857 875
| sion0.7.0). |     |     |     |     |     | Wells’criteriaforPE  |     |     | 1630 |     | 1788 |     |
| ----------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ---- | --- | ---- | --- |
|             |     |     |     |     |     | Wells’criteriaforDVT |     |     | 466  |     | 488  |     |
Outcomemeasures
|             |                 |       |         |            |           | C-spine: | cervical spine; CT: | computed | tomography; | DVT: | deep | venous |
| ----------- | --------------- | ----- | ------- | ---------- | --------- | -------- | ------------------- | -------- | ----------- | ---- | ---- | ------ |
| The primary | outcome of this | study | was the | percentage | of unique |          |                     |          |             |      |      |        |
thrombosis;PE:pulmonaryembolism;PERC:pulmonaryembolismrule-out
| provider–patient | interactions | (“unique | interactions”) |     | in which the | criteria. |     |     |     |     |     |     |
| ---------------- | ------------ | -------- | -------------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- |
MDCalcforEHRappwasusedtoviewastudycalculator.Aunique
interactionwasdefinedasastudyprovideropeningthechartofa
|     |     |     |     |     |     | non-EM | resident physicians | (internal |     | medicine, | obstetrics- |     |
| --- | --- | --- | --- | --- | --- | ------ | ------------------- | --------- | --- | --------- | ----------- | --- |
patientwhometcriteriaforatleast1CDSHookspromptduringa
|     |     |     |     |     |     | gynecology | or psychiatry), | and 17 | full-time | EM APPs. | Thirty-five |     |
| --- | --- | --- | --- | --- | --- | ---------- | --------------- | ------ | --------- | -------- | ----------- | --- |
givenEDencounter.Ifaprovideropenedapatient’schartmultiple
|     |     |     |     |     |     | participantswere | randomized | to the | intervention | group | and | 35 to |
| --- | --- | --- | --- | --- | --- | ---------------- | ---------- | ------ | ------------ | ----- | --- | ----- |
times, that would only be counted once. Unique interactions were thecontrolgroup.Thecontrolgroupconsistedof17juniorand18
chosenbecausemorethan1providercouldbeinvolvedinthecare seniorEMproviders,andtheinterventiongroupconsistedof18ju-
ofasinglepatient.Thus,itwasimportanttocaptureeachprovider’s
niorand17seniorEMproviders(Table2).
involvementinthecareprocess.Theuniqueinteractionswerethen
stratifiedbyindividualcalculatorsandbyEMprovidertypeandin-
Patientpopulation
cludedassecondaryoutcomes.Thisstudywasnotadequatelypow-
|                      |           |             |     |              |         | Intervention | group providers | saw | 3424 patients | who | received | at  |
| -------------------- | --------- | ----------- | --- | ------------ | ------- | ------------ | --------------- | --- | ------------- | --- | -------- | --- |
| ered to definitively | determine | statistical |     | significance | for the |              |                 |     |               |     |          |     |
least1CDSHookspromptwhilecontrolgroupproviderssaw3335
secondaryoutcomes.
|     |     |     |     |     |     | patients who | met criteria        | for at least | 1 CDS | Hooks  | prompt. | The     |
| --- | --- | --- | --- | --- | --- | ------------ | ------------------- | ------------ | ----- | ------ | ------- | ------- |
|     |     |     |     |     |     | number of    | unique interactions | between      | the   | groups | was     | similar |
Statisticalanalysis
(3978intheinterventiongroupvs3776inthecontrolgroup).Fur-
Logisticregressionwasusedtoestimatemeanpercentagesand95%
therstratificationbycalculatortypeisshowninTable3.
confidenceintervals(CIs)forinterventionandcontrolgroups,odds
| ratios(ORs), | and P values.Generalizedestimating |     |     | equationswere |     |     |     |     |     |     |     |     |
| ------------ | ---------------------------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Outcomesmeasures
usedtoaccountforcorrelationbetweentheinteractionsofthesame
| providerusinganexchangeablecorrelationmatrixstructure.Odds |     |     |     |     |     | Primaryoutcome |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
ratios were calculated by exponentiation of the regression coeffi- ProvidersintheinterventiongroupusedtheMDCalcforEHRapp
cient.Probabilitiesandconfidenceintervalswereback-transformed toviewastudycalculatorin6.0%oftheuniqueinteractionscom-
paredto2.6%inthecontrolgroup(OR,2.45[95%CI,1.15–5.22],
fromthelogitscale.Fisher’sexacttestwasusedforanalysisofunad-
Pvalue.02)(Table4).Thisrepresentsanincreaseinapputilization
| justed data         | included in the | Supplementary | Material. |              | A P value of |         |     |     |     |     |     |     |
| ------------------- | --------------- | ------------- | --------- | ------------ | ------------ | ------- | --- | --- | --- | --- | --- | --- |
| <.05 was considered | statistically   | significant.  |           | All analyses | we per-      | of130%. |     |     |     |     |     |     |
formedusingtheRgeepackpackage(version1.3.2).
Secondaryoutcomes
MDCalcforEHRappusagewassignificantlygreaterfortheinter-
RESULTS
ventiongroupprovidersfor2ofthe6calculators(CanadianC-spine
Providerparticipants
|     |     |     |     |     |     | rule and Wells’ | criteria for | pulmonary | embolism). |     | App usage | was |
| --- | --- | --- | --- | --- | --- | --------------- | ------------ | --------- | ---------- | --- | --------- | --- |
Seventy providers participated in the study. Study participants at greater for the remaining 4 calculators, but these differences were
timeofenrollmentincluded18postgraduateyear(PGY)-1EMresi- not statistically significant. App use with any study calculator in-
dentphysicians,18PGY-2andPGY-3EMresidentphysicians,17 creasedfrom3.5%to4.6%(Pvalue.57)forseniorEMproviders

1468 JournaloftheAmericanMedicalInformaticsAssociation,2022,Vol.29,No.9
Table4.Percentageofuniqueinteractionswhereastudycalculatorwasviewedinthecontrolandinterventiongroups
MDCalcforEHRappuse Percentageofuniqueinteractionswithastudycalculator Oddsratio Pvalue
viewed(estimateand95%CI)
Controlgroup Interventiongroup
Anystudycalculator 2.6(1.5–4.4) 6.0(3.7–9.6) 2.45(1.15–5.22) .02*
CanadianCTheadrule 1.9(1.0–3.7) 3.6(2.1–6.0) 1.92(0.79–4.64) .15
CanadianC-spinerule 0.9(0.4–2.0) 2.9(1.6–5.2) 3.38(1.21–9.42) .02*
HEARTscore 3.2(1.7–5.6) 6.5(3.9–10.6) 2.15(0.94–4.89) .069
PERCrule 4.8(2.8–8.1) 7.1(4.2–11.7) 1.52(0.7–3.32) .29
Wells’criteriaforPE 2.6(1.4–4.8) 6.2(3.6–10.4) 2.44(1.05–5.64) .038*
Wells’criteriaforDVT 1.9(0.7–5.4) 4.0(2.2–7.1) 2.11(0.62–7.26) .24
SeniorEMproviders,anystudycalculator 3.5(1.9–6.4) 4.6(2.4–8.6) 1.31(0.52–3.28) .57
JuniorEMproviders,anystudycalculator 1.2(0.4–3.5) 8.2(4.2–15.5) 7.67(2–29.42) .003*
AllEMresidents,anystudycalculator 1.6(0.6–4.3) 2.9(1.2–6.7) 2.11(0.62–7.26) .36
CI:confidenceinterval;C-spine:cervicalspine;CT:computedtomography;DVT:deepvenousthrombosis;EM:emergencymedicine;PE:pulmonaryembo-
lism;PERC:pulmonaryembolismrule-outcriteria.
*Pvalue<.05.
andfrom1.2%to8.2%(Pvalue.003)forjuniorEMproviders(Ta- solelybeattributedtotheEHRprompts.Inordertobetterunder-
ble4).Inaddition,thepercentageofproviderswhoviewedatleast1 stand the impact of each, we conducted post hoc analysis that in-
study calculator in the app during a unique interaction increased cluded only EM resident physicians, since this was the only
from37.1%inthecontrolgroupto80%intheinterventiongroup subgroupwhereallproviders(interventionandcontrol)receivedthe
(Pvalue<.001).Thisrepresentsanincreaseof116%.Thepercent- baselineeducation.Thisanalysisshowedthatappusewashigherin
age of users increased for all study calculators, but the difference theinterventiongroupcomparedtothecontrol(2.9%vs1.6%,re-
wasonlystatisticallysignificantfor2(SupplementaryTableS5).As spectively), but these results were not statistically significant (P
previouslynoted,thisstudywasnotadequatelypoweredtodetect value.36)(Table4).Thisstudywasnotpoweredtodetectdifferen-
differences in app usage for individual calculators or participant ces in this subgroup, and traditional education alone has consis-
subgroups. The raw app use data without adjusting for intraclass tently been shown to be ineffective in increasing compliance with
correlationisincludedinSupplementaryTableS6. clinicalguidelines.19However,itisstillpossiblethatatleastpartof
the intervention effect was due to the education provided or the
updatesmadetothelandingpageoftheMDCaclcforEHRapp.
Athirdlimitationwasthattheoverallrateofappusewasrela-
DISCUSSION
tivelylow(6.0%ofuniqueinteractionsintheinterventiongroup).
The results from this study demonstrate that contextually relevant There are several possible explanations for this observation. First,
CDSHookspromptsrecommendingtheuseofaSMARTonFHIR we purposely designed the CDS logic to prioritize sensitivity over
app can significantly increase app utilization. In this study, it in- specificity,soalowuseratewasexpected.Second,itisnotexpected
creasedapputilizationby130%(Table4)andthenumberofapp thataproviderwillviewthecalculatorintheappforeverypatient
usersby116%(SupplementaryTableS5).Toourknowledge,thisis withaprompt.Inmanycases,itisobviousapatientdoesnotmeet
thefirstRCTtoevaluatetheuseofCDSHookstoprovideclinical criteria without needing to view the calculator (eg, a significant
carerecommendationsandisthefirststudytoevaluateusingCDS trauma mechanism is an exclusion criterion for the Canadian CT
HookstorecommendarelevantSMARTonFHIRapp.Thisisan head rule). In addition, a provider may be viewing the chart well
important finding since recommending relevant HL7 SMART on past the point of making diagnostic decisions. Finally, providers
FHIR apps was a primary motivation for the development of the could have accessed the calculators outside the SMART on FHIR
HL7CDSHooksstandard,7anditalsodemonstratesthepotential app,suchasbyusingtheWeborsmartphoneversionsofMDCalc.
forCDSHookstobeusedtomitigateusabilityissuesthatmayarise Whilewedidnotmeasuretheutilizationofcalculatorsexternalto
with the development of an extensive EHR app-based ecosystem, theapp,apreviousstudyconductedatthestudysitefoundthatthe
suchasappfatigue. PERC rule, a calculator included in our study, was not frequently
CDS Hooks offers many advantages over current, native CDS appliedinroutineclinicalcare.20
systemsincommercialEHRs.Examplesincludeimprovedscalabil- Anotherlimitationisthatthisstudywasperformedusing1com-
ity,decreasedsystemdevelopmentcostandenhancedfunctionality. mercial EHR platform (Epic) at a single academic medical center.
Unfortunately,CDSHooksisnotcurrentlyavailableacrossallEHR FurtherevaluationindifferentEHRplatformsandhospitalsystems
platforms,andthisisalimitationofthisstudy.Toourknowledge, isneededtoconfirmthegeneralizabilityoftheseresults.Inaddition,
CDSHooksisavailableatthistimeinproductionenvironmentsin implementationatasinglecentercreatedthepotentialforcrossover
Epic(allsites)andCerner(limiteddeployment).AllScriptspublicly effectsbetweenthestudygroups,withprovidersintheintervention
announcedsupportofthestandardinFebruary2020,18butitisnot grouppotentiallyeducatingcontrolgroupprovidersabouttheappli-
yetavailableinproductionsystems. cation.However,suchcontaminationwouldhavebeenexpectedto
Asecondlimitationwasthattheinterventionconsistedof3com- decreasetheobservedimpactoftheintervention.
ponents (EHR prompts, a new landing page on the MDCalc for ThisstudywasalsolimitedtoresidentphysiciansandAPPs,and
EHRappandprovidereducation),andtheobservedimpactcannot these results may not be generalizable to experienced, board-

JournaloftheAmericanMedicalInformaticsAssociation,2022,Vol.29,No.9 1469
certifiedemergencyphysicians,whomaynotfinditnecessarytouti- CONFLICTOFINTERESTSTATEMENT
lizetheapporbepromptedtousetheappduetoarealorperceived
JHiscofounder,CEO,andpartownerofMDAware,LLC,whichownsand
familiaritywiththecalculators.Oursubgroupanalysisbyprovider
operatesMDCalc.JWandMSareemployeesofMDAware.TheUniversity
type supports this conclusion. Control group senior EM providers ofUtahhascodevelopmentandlicensingagreementswithMDAwaretoas-
used the app more frequently than control group junior EM pro- sistwiththeEHRintegrationofMDCalc.KKandPBWmaybenefitfinan-
viders(3.5%vs1.2%,respectively),andappuseincreasedsignifi- ciallyifMDCalcforEHRiscommerciallysuccessful.Theotherauthorshave
cantly between the control group and intervention group for the nocompetinginteresttodeclare.
juniorEMproviders(1.2%–8.2%,Pvalue.003)butnotforthese-
niorEMproviders(3.5%–4.6%,Pvalue.57).Theseresultssuggest
that these prompts may be more useful to more novice EM pro- DATAAVAILABILITYSTATEMENT
viders,whoarenotasfamiliarwiththecalculators.Apoststudysur-
vey could have helped to further understand these usage patterns, ThedataunderlyingthisarticlecannotbesharedpubliclyduetoUUHpoli-
andthisrepresentsalimitationofthestudyandapotentialareaof ciesregardingtheprivacyofpatientsandtheprotectionofsensitivepatient
healthinformation.
furtherresearch.
| Finally,     | this study | was      | not powered                     | to evaluate | clinical | out- |                                                       |     |     |     |
| ------------ | ---------- | -------- | ------------------------------- | ----------- | -------- | ---- | ----------------------------------------------------- | --- | --- | --- |
| comes. Thus, | further    | research | is needed                       | to evaluate | whether  | CDS  | REFERENCES                                            |     |     |     |
| Hookscan     | be usedto  | improve  | clinicaloutcomesthroughcontext- |             |          |      |                                                       |     |     |     |
|              |            |          |                                 |             |          |      | 1. MandelJC,KredaDA,MandlKD,KohaneIS,RamoniRB.SMARTon |     |     |     |
appropriatesuggestionsofSMARTonFHIRapps.
|     |     |     |     |     |     |     | FHIR: a standards-based, | interoperable |     | apps platform for electronic |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | ------------- | --- | ---------------------------- |
healthrecords.JAmMedInformAssoc2016;23(5):899–908.
|     |     |     |     |     |     |     | 2. TaberP,RadloffC,DelFiolG,StaesC,KawamotoK.Newstandardsfor |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- |
clinicaldecisionsupport:asurveyofthestateofimplementation.Yearb
CONCLUSION
MedInform2021;30(1):159–71.
Inthisprovider-randomizedstudy,wedemonstratedthatusingCDS 3. OsheroffJATeichJM,LevickD,etal.ImprovingOutcomeswithClinical
HookstorecommendaSMARTonFHIRappcanenableasignifi- DecisionSupport:AnImplementer’sGuide.Chicago,IL:HimssPublish-
ing;2012.
| cant increase | in app | usage. | To our | knowledge, this | represents | the |                                                                 |     |     |     |
| ------------- | ------ | ------ | ------ | --------------- | ---------- | --- | --------------------------------------------------------------- | --- | --- | --- |
|               |        |        |        |                 |            |     | 4. KawamotoK,HoulihanCA,BalasEA,LobachDF.Improvingclinicalprac- |     |     |     |
firstRCTtoevaluatetheuseofCDSHooksforprovidingclinical
ticeusingclinicaldecisionsupportsystems:asystematicreviewoftrialsto
| care recommendations |     | and | the first | study to evaluate | using | CDS |     |     |     |     |
| -------------------- | --- | --- | --------- | ----------------- | ----- | --- | --- | --- | --- | --- |
identifyfeaturescriticaltosuccess.BrMedJ2005;330(7494):765–8.
| Hooks to    | recommend   | a SMARTon |            | FHIR app, which | was   | one of |                                                                 |     |     |     |
| ----------- | ----------- | --------- | ---------- | --------------- | ----- | ------ | --------------------------------------------------------------- | --- | --- | --- |
|             |             |           |            |                 |       |        | 5. KawamotoK,KukharevaPV,WeirC,etal.Establishingamultidiscipli- |     |     |     |
| the primary | motivations | behind    | developing | the CDS         | Hooks | stan-  |                                                                 |     |     |     |
naryinitiativeforinteroperableelectronichealthrecordinnovationsatan
dard.ThisstudyillustrateshowCDSHooksmayhelpmitigateus- academicmedicalcenter.JAMIAOpen2021;4(3):1–15.
ability issues that may arise with the proliferation of SMART on 6. VanDerSijsH,AartsJ,VultoA,BergM.Overridingofdrugsafetyalerts
FHIR EHR add-on apps. Future research may evaluate potential incomputerizedphysicianorderentry.JAmMedInformAssoc2006;
| impactsonclinicalcaredecisionsandoutcomes. |     |     |     |     |     |     | 13(2):138–47.                                               |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- |
|                                            |     |     |     |     |     |     | 7. StrasbergHR,RhodesB,DelFiolG,JendersRA,HaugPJ,KawamotoK. |     |     |     |
Contemporaryclinicaldecisionsupportstandardsusinghealthlevelseven
internationalfasthealthcareinteroperabilityresources.JAmMedInform
FUNDING
Assoc2021;28(8):1796–806.
|     |     |     |     |     |     |     | 8. CDSHooksOverview.https://cds-hooks.org/.AccessedMay14,2022. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- |
ThisprojectwassupportedbygrantnumberT15LM007124fromtheNa-
|                |              |     |         |                              |     |        | 9. DolinRH,BoxwalaA,ShalabyJ.Apharmacogenomicsclinicaldecision |     |     |     |
| -------------- | ------------ | --- | ------- | ---------------------------- | --- | ------ | -------------------------------------------------------------- | --- | --- | --- |
| tional Library | of Medicine. | The | content | is solely the responsibility |     | of the |                                                                |     |     |     |
supportservicebasedonFHIRandCDSHooks.MethodsInfMed2018;
authorsanddoesnotnecessarilyrepresenttheofficialviewsoftheNational
57(S02):E115–23.
LibraryofMedicineortheNationalInstitutesofHealth.
|     |     |     |     |     |     |     | 10. NguyenBP,ReeseT,DeckerS,MaloneD,BoyceRD,BeyanO.Imple- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- |
mentationofclinicaldecisionsupportservicestodetectpotentialdrug-
druginteractionusingclinicalqualitylanguage.StudHealthTechnolIn-
| AUTHORCONTRIBUTIONS |     |     |     |     |     |     | form2019;264(viii):724–8.                                |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
|                     |     |     |     |     |     |     | 11. WatkinsM,EilbeckK.FHIRlabreports:usingSMARTonFHIRand |     |     |     |
Eachauthormadesubstantialcontributionsto:(1)thedesignandimplemen-
CDSHookstoincreasetheclinicalutilityofpharmacogenomiclaboratory
tationoftheCDSsystem(allauthors);(2)studydesign(KLM,PVK,KK,TM,
testresults.AMIAJtSummitsTranslSciProc2020;2020:683–92.http://
| DH,andJH);(3)theacquisition, |     |     | analysis,orinterpretationofdata(PVK, |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
www.ncbi.nlm.nih.gov/pubmed/32477691%0Ahttp://www.pubmedcen-
KLM,andKK);(4)thecreationofnewsoftwareusedinthework(KK,PBW,
tral.nih.gov/articlerender.fcgi?artid=PMC7233102.
JW,MS,andJH);or(5)thedraftingorsubstantialrevisionofthemanuscript
|     |     |     |     |     |     |     | 12. SemenovI,OsenevR,GerasimovS,KopanitsaG,DenisovD,AndreychukY. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- |
(KLM,PVK,andKK).
ExperienceindevelopinganFHIRmedicaldatamanagementplatformtopro-
videclinicaldecisionsupport.IntJEnvironResPublicHealth2019;17(1):73.
|     |     |     |     |     |     |     | 13. RubinL,Lo(cid:2)pezNP,GaieraA,CamposF,LunaD,DeQuiro(cid:2)sFBG.Devel- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------------- | --- | --- | --- |
SUPPLEMENTARYMATERIAL opment,implementationandpreliminaryresultsofanelectronicreminder
forHIVscreeningusingaserviceorientedarchitecture.StudHealthTech-
SupplementarymaterialisavailableatJournaloftheAmericanMedicalInfor- nolInform2019;264:763–7.
maticsAssociationonline. 14. HenningDJ,McgillicuddyDC,SanchezLD.Evaluatingtheeffectofemer-
gencyresidencytrainingonproductivityintheemergencydepartment.J
EmergMed2013;45(3):414–8.
|     |     |     |     |     |     |     | 15. MDCalc: About. | Published 2021. | https://www.mdcalc.com/about-us. |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --------------- | -------------------------------- | --- |
ACKNOWLEDGMENTS
AccessedMay14,2022.
WewouldliketothankScottGoodellandChristopherReedforthecontribu- 16. ChoosingWisely.AmericanCollegeofEmergencyPhysicians:FiveThings
tionstheymadeindeployingthedescribedintervention. PhysiciansandPatientsShouldQuestion.Published2014.https://www.

1470 JournaloftheAmericanMedicalInformaticsAssociation,2022,Vol.29,No.9
choosingwisely.org/wp-content/uploads/2015/02/ACEP-Choosing- 19. Prior M, Guerin M, Grimmer-Somers K. The effectiveness of clinical
Wisely-List.pdf.AccessedMay14,2022. guidelineimplementationstrategies–asynthesisofsystematicreviewfind-
17. CampbellM,GrimshawJ,SteenN,ProfessionalC.Samplesizecalculations ings.JEvalClinPract2008;14(5):888–97.
forclusterrandomisedtrials.JHealthServResPolicy2000;5(1):12–6. 20. BuchananI,TeeplesT,CarlsonM,SteenblikJ,BledsoeJ,MadsenT.Pul-
18. AllscriptsTouchWorksVREHR20.0nowgenerallyavailable.https://inves- monaryembolismtestingamongemergencydepartmentpatientswhoare
tor.allscripts.com/news-releases/news-release-details/allscripts-touch- pulmonaryembolismrule-outcriterianegative.AcadEmergMed2017;
worksr-ehr-200-now-generally-available.AccessedMay14,2022. 24(11):1369–76.
