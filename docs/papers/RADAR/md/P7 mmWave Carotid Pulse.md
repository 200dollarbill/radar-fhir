(cid:55)(cid:43)(cid:21)(cid:16)(cid:46)(cid:16)(cid:22)
(cid:51)(cid:85)(cid:82)(cid:70)(cid:72)(cid:72)(cid:71)(cid:76)(cid:81)(cid:74)(cid:86)(cid:3)(cid:82)(cid:73)(cid:3)(cid:21)(cid:19)(cid:20)(cid:27)(cid:3)(cid:36)(cid:86)(cid:76)(cid:68)(cid:16)(cid:51)(cid:68)(cid:70)(cid:76)(cid:73)(cid:76)(cid:70)(cid:3)(cid:48)(cid:76)(cid:70)(cid:85)(cid:82)(cid:90)(cid:68)(cid:89)(cid:72)(cid:3)(cid:38)(cid:82)(cid:81)(cid:73)(cid:72)(cid:85)(cid:72)(cid:81)(cid:70)(cid:72)
Contactless Carotid Pulse Measurement Using Continuous Wave
Radar
∗ † ‡ ∗ ∗
Kilin Shi , Sven Schellenberger , Tobias Steigleder , Fabian Michler , Fabian Lurz ,
∗ †
Robert Weigel and Alexander Koelpin
∗
Institute for Electronics Engineering, Friedrich-Alexander University Erlangen-Nuremberg, 91058 Erlangen, Germany
kilin.shi@fau.de
†
Chair for Electronics and Sensor Systems, Brandenburg University of Technology, 03046 Cottbus, Germany
‡
Department of Palliative Care and Department of Neurology, Universita¨tsklinikum Erlangen, 91054 Erlangen, Germany
Abstract—Cardiovasculardiseasesareoneofthemajorcauses pathological changes of carotid vessels is necessary, which
of death. Regular checkups and preventive actions can dras- is easily transportable, comparatively low-cost and operable
tically help reducing fatal incidences. This can be achieved
without special training. Radar-based assessment of carotid
by monitoring the carotid artery or rather the carotid pulse
pulse constitutes an ideal candidate for a wide-ranging and
signal.Commonly,ultrasounddevicesareusedforthatpurpose.
However, these devices are costly, mostly stationary and their cost-effective screening device. This technology has already
usage requires training and experience. This paper investigates been studied for monitoring of vital signs such as heartbeat
thepossibleusageofradarsystemsasacontactlessandlow-cost andrespiration[7],[8].Stiffnessofthevesselwallandstenosis
alternative for carotid pulse measurements. Theoretical inves-
of the carotid reflect in changes in pulse wave configuration
tigations reveal a linear relationship between the measurands
andvelocity[9],[10],e.g.,pulsewaveandbloodflowvelocity
of both devices and synchronous recordings from three test
persons further confirm the feasibility of using radar systems increase[11],systoliclimbbecomessteeperanddiastoliclimb
as a potential device for monitoring cardiovascular diseases. of the pulse wave tapers off [12]. These phenomena can be
Index Terms—biomedical monitoring, biomedical signal anal- recorded by radar-based assessment of the carotid pulse. First
ysis, cardiovascular system, cw radar, medical sensors, radar
radar measurements of the carotid pulse have been performed
signal analysis, ultrasound
using a double sideband continuous wave radar [13]. How-
ever, neither has there been any studies on the qualitative
I. INTRODUCTION
relationship of the measurands of ultrasound carotid pulse
The carotid artery provides large areas of the brain with
measurement and radar-based carotid pulse measurement nor
blood. Its clinical evaluation is of great diagnostic impor-
weretherestudiesusingacontactlessradarsystem.Thispaper
tance. It is susceptible to metabolic challenges, e.g., elevated
presents a theoretical derivation when comparing ultrasound
blood pressure and glucose levels [1]. In vascular diseases
and radar measurements and validates the results through
its cross section narrows gradually, leading to deprivation of
synchronous measurements of both devices.
oxygen and stroke. Also specific changes of the structure
of the vessel wall occur, which herald vascular diseases II. COMPARISONOFULTRASOUNDANDRADAR-BASED
elsewhere in the body and correlate highly with occurrence CAROTIDPULSEMEASUREMENT
of myocardial infarction [2]. Regular screening for stenosis
Thebasicanatomyofthehumanneckincludingtheskeletal
and remodelling of the vessel wall identifies patients at risk
system, the integumentary system as well as the arterial part
and facilitates prophylactic measures in order to maintain
ofthecardiovascularsystemareshowninFig.1.Thecommon
health. If changes proceed unchecked, stroke and myocardial
carotid artery splits up into the internal and external artery in
infarction may occur: the most common causes for death as
the cranial direction. At the end of each heartbeat cycle, the
well as disability [3] and increasingly high economic burden
left ventricle of the heart pumps oxygenated blood into the
in health care [4]. Changes of cross section as well as its
arteries.Thisischaracterizedbyarapidupstrokeandasmooth
impact on dynamics of blood flow and structural changes of
but more gradual downstroke when looking at the blood flow
the carotid wall can be detected by ultrasound examination
velocity. The downstroke is interrupted only by the dicrotic
of the carotid artery [5]. Whereas individuals at risk profit
notch, which is caused by a transient reversal of blood flow
fromregularexaminations[6],implementationisrestrictedby
in the central arteries. [14]
limitedhumanresourcesandconstrictedaccesstotechnology.
Three types of waves occur in the vascular system: veloc-
Ultrasounddevicesarecostlyandmostlystationary.Operating
ity, pressure and wall displacement waves [16]. While the
ultrasounddevicesrequirestrainingandexperience.Tobridge
ultrasound Doppler measures the blood flow velocity, the
the gap between demand and support, a device to identify
measurandoftheradarisproportionaltochangesofthevessel
diameter. The first step is therefore to investigate on the rela-
ThestudywasapprovedbytheethicscommitteeoftheFriedrich-Alexander
UniversityErlangen-Nuremberg(No.85 15B). tionbetweenthesetwoquantities.Tounderstandtheeventsin
(cid:38)(cid:82)(cid:83)(cid:92)(cid:85)(cid:76)(cid:74)(cid:75)(cid:87)(cid:3)(cid:21)(cid:19)(cid:20)(cid:27)(cid:3)(cid:44)(cid:40)(cid:44)(cid:38)(cid:40) (cid:24)(cid:25)(cid:28)
Authorized licensed use limited to: National Tsing Hua Univ.. Downloaded on August 24,2026 at 02:41:11 UTC from IEEE Xplore. Restrictions apply.

| Leftexternal |     |     |     |     |     |     |     |     |     |     | TX  |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
24GHz
carotidartery
Ref.
RX
Leftinternal
Six-PortReceiver
carotidartery
Leftcommon
carotidartery
|     |     |     |     |     |     |     |     |                                                                   |     | ADC |     | PC  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | Fig.2. Blockdiagramoftheutilizedradarsystem.Thereceiverconsistsof |     |     |     |     |     |     |
Fig.1. Thearterialsystemoftheheadandneck.Depictedaretheleftinternal aSix-Portstructureaswellasintegrateddetectors.
andexternalcarotidarteryaswellastheleftcommoncarotidartery.[15]
thearteries,asimplebutsufficientmodelisthefollowing:each A 24GHz signal is generated as reference. A minor part
|         |               |          |                 |           |     |                    |             | (Ref.) is | coupled | into the        | Six-Port | receiver      | whereas | the ma-   |
| ------- | ------------- | -------- | --------------- | --------- | --- | ------------------ | ----------- | --------- | ------- | --------------- | -------- | ------------- | ------- | --------- |
| artery  | is considered |          | as a long,      | isolated, |     | circular           | cylindrical |           |         |                 |          |               |         |           |
|         |               |          |                 |           |     |                    |             | jority is | fed to  | the transmitter |          | (TX) antenna. | The     | signal is |
| elastic | tube.         | The flow | is approximated |           | to  | be one dimensional |             |           |         |                 |          |               |         |           |
and the blood is considered to be homogeneous, non-viscous then reflected at the skin surface and received by the receiver
|                     |      |            |                |     |       |          |            | (RX) antenna.      |     | The Six-Port | is        | a completely | passive | structure     |
| ------------------- | ---- | ---------- | -------------- | --- | ----- | -------- | ---------- | ------------------ | --- | ------------ | --------- | ------------ | ------- | ------------- |
| and incompressible. |      |            | The ventricles |     | cause | the flow | within the |                    |     |              |           |              |         |               |
|                     |      |            |                |     |       |          |            | which superimposes |     | the          | two input | signals      | under   | four relative |
| tubes with          | each | heartbeat. | Furthermore,   |     | each  | wave     | amplitude  |                    |     |              |           |              |         |               |
|                     |      |            |                |     |       |          |            |                    |     |              | 0◦, 90◦,  | 180◦         | 270◦.   |               |
isconsideredsmallandthewavelengthlongcomparedtothe and static phase shifts of and These four
|     |     |     |     |     |     |     |     | outputsignalsareconvertedtobasebandvoltagesB |     |     |     |     |     | using |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | ----- |
tube radius. This way, the radial and circumferential velocity 3...6
|        |           |     |          |           |     |           |        | integrated | detectors. | A movement |     | of the | target corresponds | to  |
| ------ | --------- | --- | -------- | --------- | --- | --------- | ------ | ---------- | ---------- | ---------- | --- | ------ | ------------------ | --- |
| can be | neglected | and | the only | remaining |     | component | is the |            |            |            |     |        |                    |     |
arelativephaseshiftΔσ
longitudinal velocity u(x,t) which is a function of the axial betweenthetwoinputsignalsofthe
|            | x   |         | t.   |     |             |          |       | Six-Port: |     |     |     |     |     |     |
| ---------- | --- | ------- | ---- | --- | ----------- | -------- | ----- | --------- | --- | --- | --- | --- | --- | --- |
| coordinate |     | and the | time | One | basic field | equation | which |           |     |     |     |     |     |     |
is valid for this scenario is the equation of continuity [16]: σ =arg{(B −B 6)+j(B −B 4)}.
|     |     |     |     |     |     |     |     |     |     |     | 5   |     | 3   | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | δA  | δ   |     |     |     |     |     |     |     |     |     |     |
+ (uA)=0, (1) This phase shift can be converted back into a relative dis-
δt δx
|      |        |       |                     |     |     |         |            | placement | measurement |     | Δx by | using the | known | wavelength |
| ---- | ------ | ----- | ------------------- | --- | --- | ------- | ---------- | --------- | ----------- | --- | ----- | --------- | ----- | ---------- |
|      | A(x,t) |       |                     |     |     |         |            | λ=c/f:    |             |     |       |           |       |            |
| with |        | being | the cross-sectional |     |     | area of | the vessel |           |             |     |       |           |       |            |
|      |        | πa    | 2.                  |     |     |         |            |           |             |     | Δσ    | λ         |       |            |
which is equal to i Substitution in Eq. (1) followed by Δx= ·
|            |            |     |       |     |     |     |     |             |     |              |     | .      |              | (6)     |
| ---------- | ---------- | --- | ----- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ------ | ------------ | ------- |
| subsequent | derivation |     | leads | to  |     |     |     |             |     |              |     | 2π 2   |              |         |
|            |            |     |       |     |     |     |     | Synchronous |     | measurements |     | of the | radar system | and the |
|            |            | δa  | δa    | 2   | δu  |     |     |             |     |              |     |        |              |         |
2a i +u i +a 2 =0. ultrasound device from three test persons (one female, two
|     |     | i δt |     | δx  | i δx |     | (2) |             |           |     |                |     |           |           |
| --- | --- | ---- | --- | --- | ---- | --- | --- | ----------- | --------- | --- | -------------- | --- | --------- | --------- |
|     |     |      |     |     |      |     |     | male), were | recorded. |     | The ultrasound |     | probe was | placed on |
Since the wave amplitude is much smaller than the wave- the right carotid whereas the antenna of the radar system was
length, δa i /δx (cid:2) 1. Additionally, small quantities of the focused slightly under and to the right of the larynx. The
secondordercanbeneglected.Hence,Eq.(2)canbeshortened
distancebetweentheantennasandtheskinwasaround30cm.
| to  |     |     |       |     |     |     |     | Aredlaserbeamthatisplacedbetweentheantennasisusedto |           |     |         |              |     |              |
| --- | --- | --- | ----- | --- | --- | --- | --- | --------------------------------------------------- | --------- | --- | ------- | ------------ | --- | ------------ |
|     |     |     |       |     |     |     |     | correctly                                           | determine | the | antenna | positioning. | By  | putting both |
|     |     |     | 2 δ a | δ   | u   |     |     |                                                     |           |     |         |              |     |              |
|     |     | a   | 2(    | i   |     |     |     |                                                     |           |     |         |              |     |              |
i + )=0. (3) measurement points as close to each other as possible, the
|       |       |      | a δ    | t δ     | x          |     |     |                    |     |            |     |             |       |           |
| ----- | ----- | ---- | ------ | ------- | ---------- | --- | --- | ------------------ | --- | ---------- | --- | ----------- | ----- | --------- |
|       |       |      | i      |         |            |     |     | same physiological |     | phenomenon |     | is expected | to be | measured. |
| Since | a >0, | This | can be | further | simplified | to  |     |                    |     |            |     |             |       |           |
i
IV. RESULTS
|     |     |     | 2 δa | δu  |     |     |     |        |       |               |     |         |                   |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | ------ | ----- | ------------- | --- | ------- | ----------------- | --- |
|     |     |     | i    | +   | =0. |     |     | Fig. 3 | shows | a synchronous |     | carotid | pulse measurement |     |
|     |     |     | a δt | δx  |     |     | (4) |        |       |               |     |         |                   |     |
i
|     |     |     |     |     |     |     |     | using ultrasound |     | and radar | of  | person 1. | The ultrasound | mea- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | --- | --------- | -------------- | ---- |
u
Finally, Eq. (4) shows that a change in the velocity over surements correspond to a blood flow velocity measurement
the axial coordinate x is linearly related to a change of the which is represented in cm/s. The radar system measures
|     |     | a   |     | t.  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vessel diameter i over time Therefore, radar displacement the relative displacement change of the skin in mm. A high
measurements and ultrasound velocity measurements of the correlation between both signals can be observed in all three
carotid pulse can be directly related to each other in a testpersons.WhencarefullyexaminingtheradarsignalinFig.
qualitative manner. 3, it can be seen that there is a small incline right before the
|     |     |     |     |     |     |     |     | rapid upstroke |     | that marks | the | start of each | heartbeat. | This is |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | --- | ------------- | ---------- | ------- |
III. MEASUREMENTSYSTEMANDSETUP caused by the jugular vein which is located near the carotid.
AsshowninFig.2,abistaticcontinuouswaveradarsystem The atrial contraction causes a peak at this point in time. A
is used for the contactless carotid pulse measurements. superimposition of both pulse signals is therefore recorded at
(cid:24)(cid:26)(cid:19)
Authorized licensed use limited to: National Tsing Hua Univ.. Downloaded on August 24,2026 at 02:41:11 UTC from IEEE Xplore.  Restrictions apply.

the neck. The ultrasound however will not capture the jugular the feasibility of radar systems for this purpose, it is shown
vein pulse since it can separate these layers from each other. that a linear relationship exists between the velocity signal of
|     |     |     |     |     |     |     |     | the ultrasound |     | and the diameter |     | change | that | is measured | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | --- | ------ | ---- | ----------- | --- |
RadarCarotid radar.Tofurtherdemonstratetheapplicability,synchronousul-
trasoundandradarmeasurementswereperformedfordifferent
)mm(ecnatsiD.leR
0.5
|     |     |     |     |     |     |     |     | persons. | When | comparing | the signals | of  | both | devices, | a high |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --------- | ----------- | --- | ---- | -------- | ------ |
correlationisachievedandtypicalcarotidpulsecharacteristics
|     |     |     |     |     |     |     |     | are observed. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
0
ACKNOWLEDGMENT
0 1 2 3 4 5 6 The research project GUARDIAN is supported by the
FederalMinistryofEducationandResearch,Berlin,Germany,
UltrasoundCarotid
|            | 40  |     |     |     |     |     |     | project grant | No. | 16SV7695.  |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | --- | --- | --- | --- | --- |
| )s/mc(wolF | 30  |     |     |     |     |     |     |               |     | REFERENCES |     |     |     |     |     |
20 [1] M. L. Bots, A. W. Hoes, P. J. Koudstaal, A. Hofman, and D. E.
|     |     |     |     |     |     |     |     | Grobbee, | “Common | carotid | intima-media |     | thickness | and risk | of stroke |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------- | ------------ | --- | --------- | -------- | --------- |
10 and myocardial infarction: the rotterdam study,” Circulation, vol. 96,
no.5,pp.1432–1437,1997.
0 [2] M. Safar, J. Blacher, J. Mourad, and G. London, “Stiffness of carotid
0 1 2 3 4 5 6 artery wall material and blood pressure in humans: application to
antihypertensivetherapyandstrokeprevention,”Stroke,vol.31,no.3,
Fig. 3. Synchronous measurement of the carotid pulse using the radar and pp.782–790,2000.
theultrasounddevice. [3] R.Lozano,M.Naghavi,K.Foreman,S.Lim,K.Shibuya,V.Aboyans,
|     |     |     |     |     |     |     |     | J. Abraham, |     | T. Adair, R. | Aggarwal, | S. Y. | Ahn et | al., “Global | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --------- | ----- | ------ | ------------ | --- |
A single heartbeat complex is extracted and visualized regionalmortalityfrom235causesofdeathfor20agegroupsin1990
and2010:asystematicanalysisfortheglobalburdenofdiseasestudy
| in Fig. | 4   | to distinguish | the | different | phases | of the | signals. |     |     |     |     |     |     |     |     |
| ------- | --- | -------------- | --- | --------- | ------ | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
2010,”Thelancet,vol.380,no.9859,pp.2095–2128,2012.
Both signals show the rapid upstroke at the beginning of the [4] A.DiCarlo,“Humanandeconomicburdenofstroke,”2009.
heartbeat.Atthispointtheejectedbloodarrivesatthecarotid [5] E.G.Grant,C.B.Benson,G.L.Moneta,A.V.Alexandrov,J.D.Baker,
E.I.Bluth,B.A.Carroll,M.Eliasziw,J.Gocke,B.S.Hertzbergetal.,
| artery. | After | reaching | a peak, | a more | gradual | downstroke |     |     |     |     |     |     |     |     |     |
| ------- | ----- | -------- | ------- | ------ | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
“Carotidarterystenosis:gray-scaleanddopplerusdiagnosissocietyof
begins. It is interrupted by the dicrotic notch, which is visible radiologists in ultrasound consensus conference,” Radiology, vol. 229,
in both the ultrasound velocity signal as well as the radar no.2,pp.340–346,2003.
|              |     |         |     |     |     |     |     | [6] D.H.O’Leary,J.F.Polak,R.A.Kronmal,T.A.Manolio,G.L.Burke, |     |     |     |     |     |     |     |
| ------------ | --- | ------- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| displacement |     | signal. |     |     |     |     |     |                                                              |     |     |     |     |     |     |     |
andS.K.WolfsonJr,“Carotid-arteryintimaandmediathicknessasa
|     |     |     |     |     |     |     |     | risk factor | for | myocardial | infarction | and stroke | in  | older adults,” | New |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ---------- | ---------- | --- | -------------- | --- |
Ultrasound Radar EnglandJournalofMedicine,vol.340,no.1,pp.14–22,1999.
80 [7] C. Li, V. M. Lubecke, O. Boric-Lubecke, and J. Lin, “A review on
|     |     |     |     |     |     | 0.5 |     | recent | advances | in Doppler | radar | sensors | for noncontact |     | healthcare |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | ----- | ------- | -------------- | --- | ---------- |
monitoring,”IEEETransactionsonMicrowaveTheoryandTechniques,
|     |     |     |     |     |     |     | )mm(ecnatsidevitaleR | vol.61,no.5,pp.2046–2060,May2013. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
60
|     |     |     |     |     |     |     |     | [8] G. Vinci, | S.  | Lindner, F. | Barbon,   | S. Mann, | M. Hofmann, |            | A. Duda, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --------- | -------- | ----------- | ---------- | -------- |
|     |     |     |     |     |     | 0   |     | R. Weigel,    | and | A. Koelpin, | “Six-Port | radar    | sensor      | for remote | respi-   |
)s/mc(wolF
|     |     |     |     |     |     |     |     | ration | rate andheartbeat |     | vital-sign | monitoring,” | IEEE | Transactions | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------------- | --- | ---------- | ------------ | ---- | ------------ | --- |
40
MicrowaveTheoryandTechniques,vol.61,no.5,pp.2093–2100,May
2013.
DicroticNotch −0.5 [9] E. I. Bluth, A. Stavros, K. Marich, S. Wetzner, D. Aufrichtig, and
20 J. Baker, “Carotid duplex sonography: a multicenter recommendation
|     |     |     |     |     |     |     |     | for standardized |     | imaging | and doppler | criteria.” | Radiographics, |     | vol. 8, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ----------- | ---------- | -------------- | --- | ------- |
no.3,pp.487–506,1988.
0 −1 [10] A. Covic and D. Siriopol, “Pulse wave velocity ratio: the new gold
|     | 0   | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
standardformeasuringarterialstiffness,”2015.
Time(s)
|     |     |     |     |     |     |     |     | [11] W.Blackshear,D.Phillips,P.Chikos,J.Harley,B.Thiele,andD.Strand- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ness,“Carotidarteryvelocitypatternsinnormalandstenoticvessels.”
Stroke,vol.11,no.1,pp.67–71,1980.
| Fig. | 4. A single | heartbeat    | from | a synchronous     | measurement | using   | radar    |            |          |                      |        |           |              |         |          |
| ---- | ----------- | ------------ | ---- | ----------------- | ----------- | ------- | -------- | ---------- | -------- | -------------------- | ------ | --------- | ------------ | ------- | -------- |
|      |             |              |      |                   |             |         |          | [12] A. J. | Bonner,  | H. N. Sacks,         | and M. | E. Tavel, | “Assessing   | the     | severity |
| and  | ultrasound. | Both signals | show | a high similarity | and         | feature | the same |            |          |                      |        |           |              |         |          |
|      |             |              |      |                   |             |         |          | of aortic  | stenosis | by phonocardiography |        |           | and external | carotid | pulse    |
characteristics.
recordings,”Circulation,vol.48,no.2,pp.247–252,1973.
|     |     |     |               |     |     |     |     | [13] S. Pisa, | E. Pittella, | E. Piuzzi, | O.    | Testa, and     | R. Cicchetti, |         | “A double   |
| --- | --- | --- | ------------- | --- | --- | --- | --- | ------------- | ------------ | ---------- | ----- | -------------- | ------------- | ------- | ----------- |
|     |     |     | V. CONCLUSION |     |     |     |     |               |              |            |       |                |               |         |             |
|     |     |     |               |     |     |     |     | sideband      | continuous   | wave       | radar | for monitoring |               | carotid | artery wall |
Ultrasound devices are the gold standard device to perform movements,”in2017IEEEMTT-SInternationalMicrowaveSymposium
regular screenings of the carotid artery to detect vascular (IMS),June2017,pp.1007–1010.
|     |     |     |     |     |     |     |     | [14] S. R. | Braun, | H. Walker, W. | Hall, | and J. Hurst, | “Clinical | methods, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------- | ----- | ------------- | --------- | -------- | --- |
diseases like stenosis or any remodelling of the vessel wall. history,physical,andlaboratoryexaminations,”1990.
However, these devices are costly and have to be operated by [15] Biodigital Inc., “Biodigital human anatomy and disease platform,”
a trained staff. Radar systems might prove as a low-cost, easy https://human.biodigital.com/index.html [Online, accessed Mar. 7,
2018].
to use and contactless alternative to perform regular checkups [16] Y.-C.Fung,Biomechanics:motion,flow,stress,andgrowth. Springer
ofthecarotidarterybyanalyzingthecarotidpulse.Toanalyze Science&BusinessMedia,2013.
(cid:24)(cid:26)(cid:20)
Authorized licensed use limited to: National Tsing Hua Univ.. Downloaded on August 24,2026 at 02:41:11 UTC from IEEE Xplore.  Restrictions apply.