medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
It is made available under a CC-BY-NC 4.0 International license .
JOURNAL,VOL.XX,NO.XX,XXXX202X 1
A Non-Invasive and Non-Contact Jugular
Venous Pulse Measurement: A Feasibility Study
Shatabdi Das, Girish Dwivedi, Hadi Afsharan, and Omid Kavehei, Senior Member, IEEE
Abstract—The Jugular Venous Pulse (JVP) is a vital gauge of
properhearthealth,reflectingthevenouspressureviatheJugular
Veinobservation.Itofferscrucialinsightsfordiscerningnumerous
cardiacandpulmonaryconditions.Yet,itsevaluationisoftenover-
shadowed by the challenges in its process, especially in patients
with neck obesity obstructing visibility. Although central venous
catheterization provides an alternative, it is invasive and typically
reserved for critical cases. Traditional JVP monitoring methods,
both visual and via catheterization, present significant hurdles,
limitingtheirfrequentapplicationdespitetheirclinicalsignificance.
Therefore,thereisapressingneedforanon-invasive,efficientJVP
monitoring method accessible for home-based and hospitalized
patients. Such a method could preempt numerous hospital admissions by offering early indicators. We introduce a
non-invasive method using a frequency-modulated continuous wave (FMCW) radar for JVP estimation directly from the
skin surface. Our signal processing technique involves an eigen beamforming method to enhance the signal-to-noise
ratio for better estimation of JVP. By meticulously fine-tuning various parameters, we identified the optimal settings to
enhance the JVP signal quality. In addition, we performed a detailed morphological analysis comparing the JVP and
photoplethysmography signals. Our investigation effectively achieved signal localization within a Direction of Arrival
(DoA)rangefrom-20◦ to20◦.Thisinitialstudyvalidatestheeffectivenessofusinga60GHzfar-fieldradarinmeasuring
JVP.
Index Terms—Heart failure, Jugular venous pulse, Non-invasive sensing, Non-contact monitoring, Biomedical signal
processing,Radiofrequency.
I. INTRODUCTION attributed to HF [1]. The yearly count of HF-related hospital
HEART Failure (HF), medically referred to as congestive stays surpasses 150,000 in Australia alone, resulting in an
estimated cost exceeding $350 million due to the necessity
heart failure, occurs when the heart fails to adequately
of in-patient care following re-admissions [2]. This financial
pumptherequiredamountofbloodtomeetthedemandofthe
burden is anticipated to escalate due to the aging Australian
whole body. Thissituation can arisedue to eitherthe inability
population like many other countries worldwide.
of the heart to fill up with an adequate blood volume or its
Venous congestion is a critical factor in right heart fail-
weakened capacity to pump effectively. HF can potentially
ure, with symptoms developing gradually. This has increased
impairthefunctionalityofvitalorgans,suchasthebrain,liver,
emphasis on studying the role of the right ventricle in HF,
or kidneys. In Australia, about 15% of hospitalizations are
with the Jugular Venous Pulse (JVP) being a crucial indicator
This project is supported by The Medical Research Future Fund of heart health [3]. JVP provides insight into heart and
(MRFF)CardiovascularHealthMissiongrant(number:MRF2017760). lungconditionsbymeasuringvenouspressureviatheInternal
The authors acknowledge using ZMT Zurich MedTech AG’s Sim4Life,
JugularVein(IJV).Thejugularveins,spanningfromthehead
Zurich,Switzerland,inthiswork’selectromagneticsimulations.
ShatabdiDasandOmidKaveheiarewiththeSchoolofBiomedical to the heart, consist of six vessels divided into three pairs.
Engineering, The University of Sydney, Sydney, NSW 2006, Australia IllustratedinFig.1,theJVPwaveformunfoldsinfivephases,
(e-mail:sdas0438@uni.sydney.edu.au).
highlighting a biphasic pattern. The ‘a’ wave signifies right
Girish Dwivedi is with the Department of Advanced Clinical and
TranslationalCardiovascularImaging,HarryPerkinsInstituteofMedical atrial contraction, the ‘x’ descent follows, indicating atrial
Research,Murdoch,5RobinWarrenDrive,Perth,WA6150,Australia. relaxation, and the ‘c’ wave emerges from right ventricular
He is also with the School of Medicine, University of Western Aus-
contraction.Subsequent‘x’descentmarksthetricuspidvalve’s
tralia, Perth, WA 6009, Australia, and the Department of Cardiology,
Fiona Stanley Hospital, Murdoch, Perth, WA 6150, Australia (e-mail: downwardmovement,the‘v’wavedenotesvenousfilling,and
girish.dwivedi@perkins.uwa.edu.au). the ‘y’ descent represents rapid atrial to ventricular flow.
Hadi Afsharan is with Department of Advanced Clinical and Trans-
The ‘a’ wave in JVP, indicating atrial contraction, precedes
lationalCardiovascularImaging,HarryPerkinsInstituteofMedicalRe-
search,Murdoch,5RobinWarrenDrive,Perth,WA6150,Australiaand the photoplethysmography (PPG) systolic peak, offering in-
withtheSchoolofMedicine,UniversityofWesternAustralia,Perth,WA sights into cardiac timing. The ‘x’ descent in the JVP, rep-
6150,Australia(e-mail:hadi.afsharan@uwa.edu.au).
resenting atrial relaxation during ventricular systole, parallels
OmidKaveheiisalsowithTheUniversityofSydneyNanoInstitute,
Sydney,NSW2006,Australia(e-mail:omid.kavehei@sydney.edu.au). therisingphaseofPPG.The‘c’wave,relatedtothetricuspid
NOTE: This preprint reports new research that has not been certified by peer review and should not be used to guide clinical practice.

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
2 It is made available under a CC-BY-NC 4.0 International license .  JOURNAL,VOL.XX,NO.XX,XXXX202X
|     |     |     | Diastole | Systole |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a
|     |     | JVP |     | c   |     | v   |     | Right external jugular vein |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
Left external jugular vein
|     |     |     |     | x   |     |     |     | Right internal  jugular  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
Left internal  jugular
vein
|     |     |     |     |     | x`  | y   |     |         |     |     |     | vein |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | ---- | --- | --- |
|     |     | s   |     |     | s   |     |     | Common  |     |     |     |      |     |     |
PPG
carotid
artery
|     |     |     | d   |     |     | d   |     | Superior  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
vena
cava
Right
atrium
Fig.1: (a) Schematic representation of the superficial venous system of the inferior anterior area of the neck which connects
the IJV, External Jugular Vein (EJV) with the right atrium (b) Interpretation of jugular venous pulse contour.
valve movement, coincides with the PPG peak but lacks a minimizessusceptibilitytointerferenceand,mostimportantly,
directPPGanalog.Thev-wave,associatedwithvenousfilling, is flexible towards tailoring different parameters according to
| alignswiththedicroticnotchofPPG,markingtheaorticvalve |     |     |     |     |     |     |     | our needs. |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
closure. The ‘y’ descent, indicating atrial emptying into the WealsoutilizedZMTZurichMedTechAG’sSim4Lifeelec-
ventricle, corresponds with the declining phase of the PPG, tromagneticsimulatortoexploretheimpactofradio-frequency
signalingthecycleendandthereadinessforthenextheartbeat. electromagnetic fields (RF-EMF) on the neck region, specif-
Traditional JVP measurement techniques, such as central ically examining the effectiveness of higher-frequency radar
venous line catheterization, are invasive and limited mainly in estimating the JVP from the skin surface. Sim4Life studies
|               |     |          |     |           |      |     |          | have revealed | that | the external |     | jugular | vein is | close to the |
| ------------- | --- | -------- | --- | --------- | ---- | --- | -------- | ------------- | ---- | ------------ | --- | ------- | ------- | ------------ |
| to critically | ill | patients | in  | intensive | care | or  | coronary | care          |      |              |     |         |         |              |
settings due to the high risk of complications. This technique skin surface. This proximity allows higher-frequency radar to
necessitates critical staffing and key technologies for signal concentrate its effects in this area, minimizing the dispersion
transmission and recording. Therefore, clinicians require a orscatteringofelectromagneticenergythroughtheskinlayers.
reliable, non-invasive, and quick technique to monitor JVP. Consequently, this radar technology is highly effective for
applicationsthatrequireprecisetargetingjustbeneaththeskin
| Also, accessibility                                       |     | (or | ease | of access) | to  | both | at-home | and      |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | ---- | ---------- | --- | ---- | ------- | -------- | --- | --- | --- | --- | --- | --- |
| hospitalpatientsisanotherimportantfactorthatplaysacrucial |     |     |      |            |     |      |         | surface. |     |     |     |     |     |     |
role in the early detection of HF. Forthefirsttime,thisstudyintroducestheuseofFrequency
Studies have investigated plethysmography as a potential Modulated Continuous Wave (FMCW) radar technology for
|            |                |             |            |          |         |            |        | the non-invasive | extraction         |     | of the | JVP. FMCW    | radar  | technol-  |
| ---------- | -------------- | ----------- | ---------- | -------- | ------- | ---------- | ------ | ---------------- | ------------------ | --- | ------ | ------------ | ------ | --------- |
| method     | for estimating |             | JVP;       | however, | the     | dependency | of     | PPG              |                    |     |        |              |        |           |
|            |                |             |            |          |         |            |        | ogy, with        | its afford-ability |     | and    | sensitivity, | offers | a promis- |
| technology | on             | the optical | properties |          | of skin | and        | tissue | intro-           |                    |     |        |              |        |           |
duces significant calibration challenges, adding complexity to ing alternative to patients at risk of hospital readmission,
|     |     |     |     |     |     |     |     | including | those in | urban, | rural, and | remote | areas | of Australia. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | ---------- | ------ | ----- | ------------- |
itsapplicationbyrestrictingpatientsfrommovingorchanging
|           |      |         |           |       |     |         |            | The self-administered, |     | non-invasive |     | JVP | measurement | could |
| --------- | ---- | ------- | --------- | ----- | --- | ------- | ---------- | ---------------------- | --- | ------------ | --- | --- | ----------- | ----- |
| positions | [4], | [5]. On | the other | hand, | RF  | sensing | techniques |                        |     |              |     |     |             |       |
have emerged as a promising alternative, thanks to their significantly reduce hospital readmission by facilitating early
intervention.
| efficacy  | in tracking |          | physiological |         | changes. | Radar  | technolo- |     |     |     |     |     |     |     |
| --------- | ----------- | -------- | ------------- | ------- | -------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| gies have | been        | explored | to            | monitor | vital    | signs, | including |     |     |     |     |     |     |     |
blood pressure and heart rate, with specific investigations into II. RELATED WORK
24GHzmicrowaveradar[6]and900MHznear-fieldradar[3]
Numerousresearchstudieshaveexploredvarioustechniques
forJVPmeasurement.The900MHzband,whileofferingdeep
|              |     |     |         |             |            |     |        | for assessing   | JVP,     | including | invasive, |           | non-invasive, | contact, |
| ------------ | --- | --- | ------- | ----------- | ---------- | --- | ------ | --------------- | -------- | --------- | --------- | --------- | ------------- | -------- |
| penetration, | may | not | deliver | the spatial | resolution |     | needed | for             |          |           |           |           |               |          |
|              |     |     |         |             |            |     |        | and non-contact | methods. |           | In the    | following | sections,     | we will  |
detailedJVPwaveformanalysis.Ourpreferencefora60GHz
|              |            |      |        |           |            |             |           | describe these | findings. |     |     |     |     |     |
| ------------ | ---------- | ---- | ------ | --------- | ---------- | ----------- | --------- | -------------- | --------- | --- | --- | --- | --- | --- |
| radar sensor | over       | a 24 | GHz    | one stems | from       | its ability | to        | offer          |           |     |     |     |     |     |
| greater      | resolution | due  | to its | higher    | frequency, |             | enhancing | its            |           |     |     |     |     |     |
sensitivity to minor, surface-level movements. Such improved A. InvasiveMethod
resolution proves advantageous in precisely delineating the The most common and widely available method for mea-
subtle nuances of JVP waveforms. Specifically, we have cho- suring JVP is cannulation, an invasive technique considered
sen Infineon Technologies AG’s BGT60TR13C radar sensor the gold standard. In this procedure, an experienced anesthe-
sinceitprovidesasophisticatedintegratedantennadesignthat siologistinsertsvenouscathetersintotherightinternaljugular

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
AUTHORetal.:ANON-INVASIVEANDNON-ICt OisN mTAaCdTe JaUvGaUilaLbAlRe VuEnNdOerU aS CPUCL-BSEY-MNECA S4U.0R IEnMteErnNaTt:ioAnFaEl AliSceIBnILsIeT Y. STUDY 3
or subclavian vein (SVC). These catheters are then connected number of patients and was not validated against the gold
to a multi-modular monitor via a pressure transducer. After standard method. Nonetheless, ultrasound utilization involves
zeroing the transducer to the heart level, the mean venous significantcosts,includingtheneedforspecializedequipment
pressure (mm Hg) is displayed in real-time on the monitor andtrainedoperators.Thisrestrictsitsapplicabilitytoclinical
and recorded as invasive venous pressure [7]. settings and short-term recordings, preventing its widespread
Invasive methods can lead to various complications related useforcontinuousorambulatoryJVPsensinginthelongterm.
to vascular access and typically require trained and skilled A recent experimental study developed a prototype non-
physicians to perform. contactsystemthatemploysmicrowaveradar(24GHz,7mW)
for JVP measurement [6]. The main challenge lies in the
B. Non-invasiveContactMethod qualitative nature of pulse description and the variations in
interpretationprovidedbyamedicalprofessionaloftheinher-
The non-invasive are classified as intermittent and contin-
ent conditions. Consequently, mastering pulse palpation tech-
uous. Developing a continuous monitoring technique for JVP
niques becomes arduous, and the diversity in these techniques
is a primary concern for the future of remote heart patient
contributes to disparities in pulse analysis.
monitoring. Recent research has defined several continuous,
In summary, it can be understood that JVP effectively
non-invasive JVP measurement methods based on pressure
reflects changes in right atrial pressure due to its unique valve
sensors, ultrasound, and optical PPG methods.
arrangement, distinguishing it from other veins. However, its
Irene Garc´ıa-Lo´pez et al. [4] proposed an approach where
clinical application is limited due to the challenging nature
reflectance contact PPG is used to sense JVP and obtain its
of the measurements. JVP normal values range between 4–
physiological parameters. The PPG sensor was placed on the
6 mm Hg. Despite JVP details being present in the peaks and
upper chest to trace the JVP. The potential of this method lies
troughs of heartbeats, their small magnitudes often lead to
in its wearability and use of a single point of contact, making
oversight, rendering JVP an inefficient index. Palpation-based
it a promising candidate for a wearable device. However,
measurement involves vein compression,making pulse detec-
the inclusion of an infrared camera increases the cost, and
tion difficult. Hence, monitoring JVP requires high sensitivity
setting up the device on the appropriate venous system can be
to capture these minute signals without obstructing the vein.
complex.
Utilizing microwave radar sensors has recently gained pop-
Another non-invasive technique used accelerometer sensors
ularity over other methods for monitoring vital signs. This
to measure the vibrations of the jugular vein and the carotid
method enables non-invasive tracking of vital signs, elim-
artery [8]. This method can monitor the skin motion caused
inating direct body contact. It can detect minuscule body
by blood volume changes in the IJV. Since the method relies
surface motions resulting from cardiac and respiratory ac-
solely on skin motion to translate the JVP waveform, patient
tivities. The antenna settings allow for precise control over
movement can scramble the signal. It is also challenging to
the measurement area. This technique has been practically
use with obese patients.
employed, such as with a ceiling-mounted microwave radar
Conroy and colleagues proposed a wearable near-field RF
placed approximately two meters above the subject [14]. This
sensor affixed with a neck collar on the clavicle over the IJV
radaraccuratelymonitorsrespiratoryrateseventhroughdense
to enable noninvasive JVP sensing [3]. While this method is
bedding. Furthermore, successfulmonitoring of Heart Rate
moreconvenientcomparedtoothers,theprecisequantification
Variability (HRV) has been demonstrated.
of CVP extracted from JVP is not possible due to its single-
point measurement. Additional research has been conducted on measuring
blood pressure and other vital signs using continuous wave
radar [15], FMCW radar [16] [17] [18]. Given that the
C. Non-invasiveNon-contactMethod
characteristicsofradartechniquesalignwiththerequirements
Imaging-based PPG, where the jugular waveform can be
forJVPmeasurements,thereispotentialforapplicationinthis
consistently observed non-invasively, is a non-contact JVP
context. Such utilization could alleviate the need to subject
assessment approach suggested by Robert Amelard et al. [9].
patients to significant physiological stress.
This technique offers the advantage of ensuring the utmost
Using this technology can also give easy access and af-
comfort among all JVP sensing methods in a clinical environ-
fordability for HF patients in remote areas. Enhancing the
mentwheresubjectsarerelativelyimmobileconfinedtoabed.
efficiency and performance of the technology can benefit
However,itimposesnotablelimitationsonpatientpositioning.
clinicians and specialists involved in HF patient care, po-
Patients must maintain a consistent orientation towards the
tentially influencing decisions regarding re-hospitalization or
camera and hold the same posture throughout the recording,
readmission. Hence, this current study aims to validate the
introducing complexities for continuous or frequent long-term
efficacy of a non-invasive approach employing FMCW radar
monitoring [3].
for JVP measurement. In this paper, we develop a system
The most well-established alternative approach to sensing
basedonFMCWradarforJVPmeasurement.Furthermore,the
JVPinvolvesultrasoundimagingoftheIJVstructure[10] [11]
performance of the system is assessed through experimental
[12]. Bedside ultrasound of the IJV, performed by emergency
data.Additionally,wewillexplorethepotentialofthemethod
physicians, provides immediate, important information that
for future utilization.
cannotbeobtainedwithoutinvasivecatheters.However,Wang
et al., [13] claimed that their study was carried out on a small

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
4 It is made available under a CC-BY-NC 4.0 International license . JOURNAL,VOL.XX,NO.XX,XXXX202X
III. CONCEPT OF FMCW RF SYSTEM the target. In FMCW radar, this beat frequency is used to
determine the range of the target using the formula;
Unlike a CW radar, an FMCW signal offers the added
benefitofachievingrangeresolutionduetoitsvaryingemitted 2∆R·B
f = , (5)
frequency [16]. The FMCW system creates a linear signal b c·T c
that reflects as an echo upon encountering an object. This where, ∆R is the range resolution, B is the bandwidth of
echoed signal is captured, combined with the transmitted chirp, c is the speed of light and T is the chirp duration.
c
signal, filtered, and converted into an Intermediate Frequency The system can determine the target distance in relation
(IF) signal before being displayed. A simple representation of to its position and utilize the reflected signal solely from a
the FMCW RF system is shown in Fig. 2. designated range bin or a range span encompassing multiple
The frequency of this IF signal corresponds to the beat bins. The maximum distance can be obtained by,
frequency, which is utilized to determine the target range. f ·T ·c
The IF signal contains sinusoids with varying frequencies r max = s 2B c , (6)
correspondingtothetargetrangesinmultiple-targetscenarios.
where, f is the sampling rate and T is chirp duration as
s c
The In-Phase (I) and Quadrature (Q) data obtained from
mentioned previously.
an FMCW radar captures the frequency difference resulting
FMCW radar operates best near the target area [17]. Thus,
from the delay between the transmitted and reflected signals,
the FMCW system is believed to return only the most imme-
considering that the transmitted signal’s frequency varies over
diate range skin displacement, while we chose to work with
time. When the transmitted frequency-modulated signal in-
FMCW for JVP measurement.
teracts with a target, the received signal is delayed in time
comparedtothetransmittedsignal.Thetransmittedsignalcan IV. SYSTEM DESIGN
be represented as;
A. SimulationSetup
(cid:0) B (cid:1) The finite difference time domain (FDTD)–based solver
S (t)=A x·cos 2π·(f + t)·t , (1)
tx t c 2·T c of the commercially available software Sim4Life (Zurich
MedTech AG, Switzerland) was used for all dosimetric eval-
where, A is the amplitude of the transmitted signal, f is
tx c
uations. The FDTD method is computationally efficient for
the start frequency (carrier frequency) of the chirp, B is the
studying the electromagnetic (EM) exposures of complex het-
bandwidth of the chirp, T is the chirp duration and t is time.
c
erogeneous dielectric structures, such as anatomical models.
A chirp is characterized by the start frequency (f ), Band-
c
An MRI-based full-body voxel model, Duke V3.0, was
width(B)andduration(T ).Thetimeittakesforthechirpto
c
obtainedfromavirtualpopulationforthehumanbodymodel.
reach the upper frequency from the lower frequency is called
The model was segmented into approximately 80 anatomical
the chirp duration (T ). The slope of a chirp defines the rate
c
body tissues and organs, with a resolution of 0.8×0.8×0.8
at which the chirp ramps up. Bandwidth B is the difference
mm3 throughoutthebody.Theheightandweightofthemodel
between the upper and lower frequencies.
were 1.63 meters and 57.3 kg, respectively. Parameters, such
as permittivity, permeability, and electric conductivity, were
B =f −f . (2)
up low assigned to the tissues according to the IT’IS Database.
The received signal, which is a time-delayed version of the A phased array antenna Fig. 3(a) is used as an EM source,
transmittedsignalduetotheround-triptraveltimetoandfrom with the antenna array excited with an input power of 350
the target(t ), can be represented as: mW. For computational analysis, a limited region (head in-
d
cluding neck) is simulated, represented by a white boundary
S (t)=A x·cos (cid:0) 2π·(f + B (t−td))·(t−td) (cid:1) , (3) inFig.3(b).Thesimulatedregion(neck)accuratelyrepresents
rx r c 2·T c the skin, fat layers, muscle, and blood vessels (jugular veins
where,A istheamplitudeofthetransmittedsignal,t isthe and carotid artery) as shown in Fig. 4.
rx d
time delay of the received signal. In EM simulations, specific absorption rate (SAR) and
Fig. 2(b) demonstrates the computation of the beat fre- power density (PD) are critical parameters for understanding
quency through a Fast Fourier Transform over the IF signal, theinteractionofelectromagneticfieldswithbiologicaltissues.
enabling the estimation of the target range. The figure shows In simulations conducted at 60 GHz, the wavelength of
the linearly increasing frequency of the transmitted and re- the electromagnetic wave is notably short, measuring approx-
flected signals. Since the speed of electromagnetic waves is imately 5 mm in air and further reduced in biological tissues
constant, this time delay can be used to calculate the distance due to their elevated permittivity. Consequently, accurately
to the target using the formula; modeling the electromagnetic fields at this frequency necessi-
tates an excellent spatial resolution for the simulation mesh.
c·t
distance= d . (4) This level of detail significantly increases the computational
2
requirements,includingmemoryandprocessingpower,needed
The beat frequency (f ) is the difference between the for precise simulations. Therefore, we have considered three
b
transmittedsignalfrequencyandthefrequencyofthereceived differentfrequencies(900MHz,5GHz,anduptoamaximum
signal after it has been reflected off a target. Beat frequency of 35 GHz) for the SAR and PD analysis of the neck region.
is directly proportional to the time delay and the distance to The simulation results are discussed in Sec. VI.

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
AUTHORetal.:ANON-INVASIVEANDNON-ICt OisN mTAaCdTe JaUvGaUilaLbAlRe VuEnNdOerU aS CPUCL-BSEY-MNECA S4U.0R IEnMteErnNaTt:ioAnFaEl AliSceIBnILsIeT Y. STUDY 5
|     | a)  |     |     |     |     |     |     |     | b)  |     | Transmitted Signal |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- |
f
Tx Target
Reflected Signal
Power
|     |     |            | t V        | o l t a g e     | Amplifier |     |     |     | y c  |     |                            |     |     |
| --- | --- | ---------- | ---------- | --------------- | --------- | --- | --- | --- | ---- | --- | -------------------------- | --- | --- |
|     |     | Ramp       | C o        | n t r o ll e d  |           |     |     |     | n    | td  |                            |     |     |
|     |     | generation |            |                 |           |     |     |     | e u  |     |                            |     |     |
|     |     |            | Oscillator |                 |           |     |     |     | q    |     |                            |     |     |
|     |     |            |            |                 |           |     | Rx  |     | e rF | fb  | IF Signal/ Receiver Output |     |     |
Time
ADC
|     |     | Converter |     |     |     |     |     |     | t =   |   T i m e   D e l a y     |     |                   |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | ----- | ------------------------- | --- | ----------------- | --- |
|     | 0 1 | 2 3 4     |     |     |     |     |     |     | f d = |   B e a t  F r e q u ency |     | Fourier Transform |     |
b
|     | Display |     | Low    | IF        | Mixer | Low    |     |     |     |     |     |     |     |
| --- | ------- | --- | ------ | --------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |         |     | Pass   | Amplifier |       | Noise  |     |     |     |     |     |     |     |
Amplifier
Filter
Fig.2: (a) A typical FMCW system with one transmitter and one receiver outlines the linear saw tooth ramp generation and
the necessary modules for data processing. The received signal is amplified and low-pass filtered before being converted to
digitalrepresentation.(b)ThebasicworkingprincipleofanFMCWradarsystemhighlightstransmittingafrequency-modulated
signal and mixing it with the incoming signal at the receiver. This action generates an IF signal, represented in the figure as
| a sinusoidal |     | waveform | corresponding  |     | to the            | beat frequency. |     |     |     |     |     |     |     |
| ------------ | --- | -------- | -------------- | --- | ----------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
|              |     |          | Radar top view |     | Radar bottom view |                 |     |     |     |     |     |     |     |
Isometric view
Antenna array
1 Tx
3 Rx
(a)
Simulated
Area
External
jugular vein
Radar
Radar
(b)
Fig. 3: Overview of an FMCW radar simulation setup targeting the external jugular vein. The setup includes (a) isometric
view of the radar system with phased array antenna-integrated RADAR model featuring 1 transmitter (Tx) and 3 receivers
(Rx), and (b) simulation setup and radar positioning relative to the simulated area, focusing on the electromagnetic effects and
| SAR | analysis | in Sim4Life | utilizing | Duke | model. |     |     |     |     |     |     |     |     |
| --- | -------- | ----------- | --------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
B. RadarBoardSpecification radar increases, its ability to detect subtle movements im-
|     |     |     |     |     |     |     |     | proves. |     | Higher frequencies | have shorter | wavelengths, | which |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------------ | ------------ | ------------ | ----- |
Theradarselectedforacquiringdatainthisstudyisoff-the-
|        |               |          |               |              |         |              |        | amplify     |     | the signal’s phase  | with repeated | motions           | [17]–[19]. |
| ------ | ------------- | -------- | ------------- | ------------ | ------- | ------------ | ------ | ----------- | --- | ------------------- | ------------- | ----------------- | ---------- |
| shelf, | relatively    | low-cost | Infineon      | Technologies |         | AG’s         | 60 GHz |             |     |                     |               |                   |            |
|        |               |          |               |              |         |              |        | Therefore,  |     | we selected         | to work with  | a 60 GHz          | system for |
| FMCW   | radar         | chipset  | (BGT60TR13C), |              | with    | one transmit | (T     | )           |     |                     |               |                   |            |
|        |               |          |               |              |         |              |        | x measuring |     | JVP, skin movement, | or            | any displacements | of very    |
| and    | three receive | (R       | ) antennas.   | The          | receive | antennas     | are    |             |     |                     |               |                   |            |
x
|            |             |                 |      |             |     |           |        | small | magnitude. |     |     |     |     |
| ---------- | ----------- | --------------- | ---- | ----------- | --- | --------- | ------ | ----- | ---------- | --- | --- | --- | --- |
| positioned |             | at right angles | to   | each other. |     | The radar | sensor |       |            |     |     |     |     |
| is in      | a laminated | package         | with | dimensions  |     | of 6.5    | × 5.0  | ×     |            |     |     |     |     |
0.9mm3.Itoperateswithinthe58to63GHzrangeandoffers C. RadarDataConfiguration
customization options for samples per chirp (N ), chirps per The radar data within a measurement frame is structured as
s
frame (N ), and chirp duration (T ). The gain of each receive a three-dimensional cube in the time domain Fig. 5(a). Fast
|     | c   |     |     | c   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andtransmitantennais10(dBi)and6(dBi),respectively.This time refers to the time scale within a single chirp associated
chipset creates precise linear frequency modulations. with the samples per chirp. Slow time is the time scale across
Thehighsensitivityofthissensorallowsforsub-millimeter multiple chirps associated with chirps per frame. Both range
motion detection. Generally, as the emitted frequency of a and velocity information can be obtained by performing the

6 JOURNAL,VOL.XX,NO.XX,XXXX202X
Radar
External
jugular vein
Radar
Fig. 4: Realistic human model (Duke) accurately represents Frame
the skin, fat, muscles, and various other tissues.
Fast Fourier Transform (FFT) along the fast and slow times,
respectively. samples
Fig. 5(b) illustrates an example of raw radar data sample Samples
indices. Here, rows represent the number of receive (R )
x
antennasforeachactivetransmit(T )antennaavailableinthe
x
device, and columns indicate the number of chirps configured
in a frame (N ), and slices indicate the number of samples
c
per chirp (N ). Data from each transmit-receive antenna pair
s
is treated as data from a single virtual antenna. The ordering
ofvirtualreceiveantennasfollowsthe(Tx,Rx)sequencebased
onthecountofactivetransmitandreceiveantennas.Whenthe
digitizedsignalisformedintoaframe,itassumesthestructure
of (N × N × N ), which is then utilized for signal
Rx rmc s
processing. The number of samples per chirp indicates the
fast time, whereas the number of chirps per second indicates
the slow time.
D. ExperimentalSetup
The radar was first updated to the latest firmware version
v.2.55. For interfacing with the system, we utilized the lat-
est version of the Radar System Development Kit, v.3.3.0,
provided by Infineon Technologies AG, which is compatible
with MATLAB (2023a, Math Works, Massachusetts, USA).
Additionally, we designed a meshed cover with dimensions
of 30×10.5×2 mm3 using Fusion 360 and 3D printed it
by Creality, which is a biocompatible plastic in a laboratory
environment as shown in Fig. 7(b).
Our trials across various distances have demonstrated the
importance of correctly positioning the radar to achieve op-
timal signal strength. Proper positioning prevents saturation
due to proximity and avoids losing details when the radar is
too distant. Appropriate separation enhances signal process-
ing efficiency and ensures precise tracking of physiological
movements influenced by changes in the signal return time
and frequency attributes.
Tocompleteoursetup,thenextstepwastoidentifytheopti-
malnecklocationandadjustthesubject’spositiontofacilitate
thedetectionofthejugularvein.Venousreturn,cardiacoutput,
and arterial and venous pressures are all affected by gravity.
The ideal angle for measuring the jugular pulse falls between
sannetna
lautriV
)xR
mun
*
xT
mun( Chirps
frames
sprihc
L
1
M
1 N
Slow time, chirps
revieceR slennahc
medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
It is made available under a CC-BY-NC 4.0 International license .
a)
FFT
Azimuth and Range
elevation
angle bins
FFT
Doppler, speed
b)
Fig. 5: (a) Radar data cube representation. The data cube
is structured along three axes: chirps (slow time), receiver
channels, and samples, facilitating the processing of signals
throughmultipleFFTstodeterminerange,Dopplerspeed,and
angles in azimuth and elevation. (b) The frame structure of
the data received by the radar sensor. Each frame comprises
several chirps, and each chirp contains several samples.
Sternocleidomastoid Small Intestine (SI 17),
on the posterior ridge
External Jugular Vein of the mandibular arch
Small Intestine (SI 16), on Internal Jugular Vein
the posterior ridge of the
s m te u r s n c o le c l a e t i d th o e m l a e s v t e o l i d o f the Common Carotid SI17
laryngeal prominence
SI16
Fig. 6: Using Acupoints (acupuncture points) SI16 and SI17
to identify jugular vein Locations. This diagram illustrates
using the Small Intestine meridian acupoints SI16 and SI17
as anatomical references for locating the jugular veins. SI16
is positioned just posterior to the sternocleidomastoid muscle
at the level of the laryngeal prominence, and SI17 is along
the posterior ridge of the mandibular arch. Both points serve
as key landmarks for identifying the paths of the external and
internal jugular veins.
30◦ and45◦.Individualswithvisiblejugulardistensiondonot
require specific positioning. However, in healthy individuals,
the jugular veins are usually not prominent when standing but
may become distended to varying degrees in a lying position.
Therefore, selecting the appropriate intermediate position al-

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
AUTHORetal.:ANON-INVASIVEANDNON-ICt OisN mTAaCdTe JaUvGaUilaLbAlRe VuEnNdOerU aS CPUCL-BSEY-MNECA S4U.0R IEnMteErnNaTt:ioAnFaEl AliSceIBnILsIeT Y. STUDY 7
lows for the observation of the peak of the column in the After carefully considering both acupuncture points, we
neck area between the collarbone and the jawbone. Thus, preferred SI16 as the most optimal choice for the radar
maintainingthisinclinationiscrucialforaccuratelyidentifying placement. As a proof of concept and in adherence to ethical
JVP in healthy individuals and those with venous pressure guidelines, this experiment was conducted on one healthy
conditions. subject (female, aged 26 to 30 years, with a warm skin tone).
|     |     |     |     |     |     |     |     |     |     |     |     |     | [0◦, 30◦, | 45◦, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- |
Now, to narrow down the area of the jugular vein on The subject was positioned at varied angles of
the neck, we considered the Small Intestine (SI) acupuncture 90◦] and the recording period was 30s each time. The device
|             |          |        |            |     |              | was set | up for | recording, |     | and the | data | was | collected | on  |
| ----------- | -------- | ------ | ---------- | --- | ------------ | ------- | ------ | ---------- | --- | ------- | ---- | --- | --------- | --- |
| points SI16 | and SI17 | as our | reference. | The | Fig. 6 shows |         |        |            |     |         |      |     |           |     |
the position of SI16 and SI17 on the neck. SI16 and SI17 the host computer. Furthermore, to analyze the shape of the
are acupuncture points near the jugular vein, yet neither jugularvenouswaveformagainstthecardiacactivitystagesof
directlyoverlapswiththeveinduetotheirrespectivepositions systole and diastole, we gathered finger PPG data Fig. 7(a).
relative to the sternocleidomastoid (SCM) muscle [20]. SI16 The sampling rate of the single-channel PPG recording was
|             |                |        |     |           |           | 273.067 | Hz, and | the supply |     | voltage | was | 5 V. Additionally, |     | it  |
| ----------- | -------------- | ------ | --- | --------- | --------- | ------- | ------- | ---------- | --- | ------- | --- | ------------------ | --- | --- |
| is situated | on the lateral | aspect | of  | the neck, | posterior | to      |         |            |     |         |     |                    |     |     |
the SCM muscle, and approximately level with the laryngeal is worth noting that multiple datasets were gathered across
prominence(Adam’sapple).Givenitslocationposteriortothe different setups of parameters (such as samples per chirp,
SCM, SI16 is somewhat lateral (to the side of) but near the chirps per frame, sampling frequency, and chirp duration) for
internal jugular vein, which lies deep and medial to the SCM experimentationandanalysis.Allthedatawerethenprocessed
muscle. and analyzed using MATLAB. This process aimed to identify
SI17islocatedslightlydifferentlyinthedepressionbetween thebestparametersforaccuratelydetectingthejugularvenous
| the SCM | muscle and the | mandible | (jawbone) |     | and anterior | to waveform. |     |     |     |     |     |     |     |     |
| ------- | -------------- | -------- | --------- | --- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
the edge of the SCM muscle. This places SI17 closer to the (For further details regarding the specific device used in
path of the internal jugular vein as it runs deep and somewhat this study, including its configuration, interested readers are
|           |                   |     |            |      |                 | encouraged | to  | contact | the corresponding |     |     | author1.) |     |     |
| --------- | ----------------- | --- | ---------- | ---- | --------------- | ---------- | --- | ------- | ----------------- | --- | --- | --------- | --- | --- |
| medial to | the SCM. However, |     | like SI16, | SI17 | is not directly |            |     |         |                   |     |     |           |     |     |
over the vein.
|     |     |     |     |     |     | V.  | METHODS  |     | DATA          | ANALYSIS |        | SIGNAL |              |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | -------- | ------ | ------ | ------------ | --- |
|     |     |     |     |     |     |     |          | OF  |               |          |        | AND    |              |     |
|     | a)  |     |     |     |     |     |          |     | PROCESSING    |          |        |        |              |     |
|     |     |     |     |     |     | The | workflow | for | the detection |          | of the | JVP    | is described |     |
radar sensor
|     |     |     |     |     |     | in this | section. | The data | cube | contains | the | normalized |     | ADC |
| --- | --- | --- | --- | --- | --- | ------- | -------- | -------- | ---- | -------- | --- | ---------- | --- | --- |
sensing JVP
|     |     |     |     |     |     | samples | of the | received | signal. | After | obtaining | the | frame | data |
| --- | --- | --- | --- | --- | --- | ------- | ------ | -------- | ------- | ----- | --------- | --- | ----- | ---- |
450
|     |     |     |     |     |     | (N ×N | ×N  | ),sampledatthebeatfrequency,istransformed |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | rx    | c s |                                           |     |     |     |     |     |     |
intoacomplexrangeprofilethroughtheapplicationofanFFT
|     |     |     |     |     |     | over the | fast time | dimension. |              | Peaks | within  | the FFT  | spectrum   |     |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | ------------ | ----- | ------- | -------- | ---------- | --- |
|     |     |     |     |     |     | of the   | range     | indicate   | the presence |       | of      | a target | within     | the |
|     |     |     |     |     |     | mmWave   | radar’s   | detection  | area.        | The   | overall | data     | processing |     |
|     |     |     |     |     |     | sequence | is shown  | in         | Fig. 8.      |       |         |          |            |     |
finger PPG  JVP signals are venous pulsations reflecting changes in
device
|     |     |     |     |     |     | the right   | atrium’s    | pressure |              | during | the cardiac     |       | cycle.     | These |
| --- | --- | --- | --- | --- | --- | ----------- | ----------- | -------- | ------------ | ------ | --------------- | ----- | ---------- | ----- |
|     |     |     |     |     |     | changes     | are subtler | and      | produce      | lower  | amplitude       |       | signals    | than  |
|     |     |     |     |     |     | the strong, | rhythmic    |          | contractions |        | of the          | heart | or the     | more  |
|     |     |     |     |     |     | pronounced  | movements   |          | associated   |        | with breathing. |       | Therefore, |       |
JVP,beingmoredelicatethansignalsfrombreathing,mightbe
b)
|     |     |     |     |     |     | masked          | within          | radar data. | Spotting       |     | deviations | in    | JVP           | signals |
| --- | --- | --- | --- | --- | --- | --------------- | --------------- | ----------- | -------------- | --- | ---------- | ----- | ------------- | ------- |
|     |     |     |     |     |     | also presents   | its             | own set     | of challenges. |     | The        | lack  | of standard-  |         |
|     |     |     |     |     |     | ization         | in experimental |             | frameworks     |     | across     | the   | field compli- |         |
|     |     |     |     |     |     | cates comparing |                 | research    | findings.      |     | To tackle  | these | issues,       | we      |
introducedasimulatorforvitalsigns,emphasizingJVPsignal
|     |     |     |     |     |     | emulation  | through      | sound | speaker     | vibration  |           | estimations. |           | This |
| --- | --- | --- | --- | --- | --- | ---------- | ------------ | ----- | ----------- | ---------- | --------- | ------------ | --------- | ---- |
|     |     |     |     |     |     | allows a   | standardized |       | environment |            | to assess | and          | benchmark |      |
|     |     |     |     |     |     | algorithms | tailored     | to    | JVP signal  | detection. |           |              |           |      |
AsillustratedinFig.9,wecreatedasimulationofapatient
| Fig. 7: Data | recording      | setup. | (a) The  | radar       | sensor is placed |              |         |         |                |         |              |     |               |      |
| ------------ | -------------- | ------ | -------- | ----------- | ---------------- | ------------ | ------- | ------- | -------------- | ------- | ------------ | --- | ------------- | ---- |
|              |                |        |          |             |                  | target using | a       | speaker | plate designed |         | to replicate |     | human         | skin |
| near SI16    | on the jugular | vein   | for data | collection, | while the        |              |         |         |                |         |              |     |               |      |
|              |                |        |          |             |                  | positioned   | towards | the     | radar          | system. | Due          | to  | the speaker’s |      |
PPGdataiscollectedusingthefingerPPGdevice.Thesubject
operationalfrequencyrange,webroadcastasynthesizedaudio
| is reclined | with a sensor | placed | at  | the neck | at an almost |              |         |            |     |     |        |     |         |     |
| ----------- | ------------- | ------ | --- | -------- | ------------ | ------------ | ------- | ---------- | --- | --- | ------ | --- | ------- | --- |
|             |               |        |     |          |              | signal (beat | signal) | comprising |     | two | tones, | f   | = 50 Hz | and |
45◦ angle to monitor cardiovascular parameters. (b) The 3D- 1
| printed plastic | case is | nearly the | size | of a 1-dollar | Australian |              |     |                 |         |     |                   |     |        |     |
| --------------- | ------- | ---------- | ---- | ------------- | ---------- | ------------ | --- | --------------- | ------- | --- | ----------------- | --- | ------ | --- |
|                 |         |            |      |               |            | 1For further |     | details, please | contact |     | the corresponding |     | author | at  |
coin.
sdas0438@uni.sydney.edu.au

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
8 It is made available under a CC-BY-NC 4.0 International license . JOURNAL,VOL.XX,NO.XX,XXXX202X
Raw Data DoA estimation Extract phase
Phase
(Nrx* Nc * FFT-Range and variation from
unwrapping
Ns) Beamforming selected range bin
Display JVP (0.9 – 1.1) Hz Bandstop Filtering (0.75 – 4) Hz Skin
wave (attenuate arterial Lowpass Filtering displacement
pulses) estimation
Fig. 8: Schematic representation of the data processing sequence. After reshaping the raw data, an FFT is performed on the
samplestoobtaintherangeinformation.UponcomputationofFFT,displacementiscalculatedfromthephasevariation,which
is then used to extract the JVP.
.
f 2 =54 Hz of the form: • Inverse Fourier transform (IFFT) of first spectrum bin to
extract IQ complex signal for each antenna.
S (t)=a ·cos(2πf t)+a ·cos(2πf t) (7)
speaker 1 1 2 2
The procedure initiates with the acquisition of raw radar
data. The raw data is subjected to an FFT per-chirp basis
for each antenna. This is executed separately for antennas 1
and 3, as indicated by (range FFT 1) and (range FFT 3).
Followingthe FFT,thealgorithm computestheaverage ofthe
Fourier-transformed data across all frames for each antenna.
Thisaveragingprocessiscrucialfornoisereductionandsignal
clarity enhancement. Subsequently, the algorithm employs an
inverseFFT(IFFT)ontheaverageFFTdata’sfirstbintoyield
thefinalI/Qdataforantennas1and3.Thisstepessentiallyre-
Fig.9: This setup features an experimental design replicating
constructs the time-domain signal from the frequency-domain
a patient target, with a speaker plate strategically oriented to
data while focusing on the first bin, which indicates isolating
face the radar system. The experiment involves the synthesis
the DC component or the specific frequency component of
of an audio signal, meticulously composed of two specific
interest.
frequencies, 50 Hz and 54 Hz, to evaluate the radar system’s
response.
Algorithm 1 I/QSamplesExtractionforEachRadarAntenna
The genesis of this experiment was influenced by [21], 1: proc EXTRACTIQ
where their setup was used for signal processing validation. 2: rawD ← GETRAW(Rdr)
The outcome of this experiment is discussed in Sec. VI. 3: fftD1← COMPFFT(rawD,ant1)
Below, we detail each step in the signal processing sequence, 4: fftD3← COMPFFT(rawD,ant3)
accompanied by the corresponding pseudo codes: 5: avgF1← AVGFR(fftD1)
6: avgF3← AVGFR(fftD3)
STEP 1: RESHAPING RAW DATA VECTOR INTO A 7: iqS1← PERFIFFT(FILTFB(avgF1))
MATRIX 8: iqS3← PERFIFFT(FILTFB(avgF3))
• Size of matrix: (No of frames)×(size of frame) 9: end proc
• Size of frame: No of chirps per frame × 3 ×
No of samples per chirp
STEP 2: PROCESSING EVERY ANTENNA’S SIGNAL A. BeamformingprocessingtoenhancesignalSNR
• Applying FFT processing for every chirp pulse in each
Referencing the I/Q data extraction process in [17], which
frame and to each antenna. (Optional windowing tech-
applied the radar for monitoring blood pressure, our approach
niquecanbeusedbeforeFFTforspectruminterpolation)
diverges in beamforming methodology. The eigenspace-based
• AveragingFFToutputstoreducethenoiseeffectforeach
beamformingmethod(ESBM)usedintheirworkencountered
antenna signal and from each frame.
challenges with ill-conditioned matrices in our setup. Conse-
quently,wehaveimplementedtheeigen-beamformingmethod,
STEP 3: EXTRACTING IQ SIGNAL FROM EACH an adaptive technique that capitalizes on the eigenstructure of
ANTENNA the signal to adjust the antenna array weights optimally. This
• From the averaged spectrum of raw data, each antenna ensures a stable and effective beamforming process for our
detectsthefirstspikeasradarechofromthepatientskin. applications.

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
AUTHORetal.:ANON-INVASIVEANDNON-ICt OisN mTAaCdTe JaUvGaUilaLbAlRe VuEnNdOerU aS CPUCL-BSEY-MNECA S4U.0R IEnMteErnNaTt:ioAnFaEl AliSceIBnILsIeT Y. STUDY 9
STEP 1: CONSTRUCT DATA MATRIX FOR EACH outputsignal,verylownoisecontributionisobservedintheIQ
FRAME signal, which implies an almost noise-free observation vector
“x.” So, the covariance matrix
(cid:20) (cid:21)
Vec IQ =
I
I
Q
Q
S
S
i
i
g
g
n
n
a
a
l
l
f
f
r
r
o
o
m
m
a
a
n
n
t
t
e
e
n
n
n
n
a
a
1
2 Rˆ =
xxH
size(x)
(2×Length of IQ signal) is by definition a rank-one matrix, and with almost noise-
free observation, this covariance matrix is ill-conditioned (the
STEP 2: COVARIANCE MATRIX ESTIMATION ratio of the highest eigenvalue to the smallest eigenvalue is
much greater than 1) and hence non-invertible. Constructing
1
Rˆ = Vec VecH the steering vector (Vector of signal phases in each receiving
X Length of IQ signal IQ IQ antenna) for a given Direction of Arrival α:
(cid:20) (cid:21)
1
STEP 3: EIGENVALUE DECOMPOSITION OF R X A(α)= . (8)
exp(−iπsin(α))
• Eigenvector associated with the highest eigenvalue A
Calculating the received signal power at the output of the
beamformer concerning an angle α:
STEP 4: ESTIMATION OF DOA
PSD(α)=A Rˆ AH , (9)
proj X proj
A=arg max [PSD(α)] such that:
α∈[−40◦,40◦]
A =AAHA(α) . (10)
proj
STEP 5: ENHANCING THE SNR OF THE RECEIVED This last expression is a A(α) projection on the signal
SIGNAL AT THE OUTPUT OF THE BEAMFORMER subspace generated by the eigenvector A associated with the
highesteigenvalue.Theobjectiveofthisprojectionistoreduce
Vec =AHDoA×Vec noise and other radar reflections.
IQ IQ
pFrameBF pFrame
Eigen-beamforming is based on the notion of signal sub- B. I/Qsignalenhancementusingcircularregression
space. In two-dimensional space (two antenna cases), the
SincetheI/Qcomponentsofradarechocreateanoisycircle
signalsubspaceisonedimensiongeneratedbytheeigenvector
in the IQ plan, we have used Taubin Cicular regression to
associatedwiththehighesteigenvalue.Toreducetheeffectof
compensate for offset and noise effects in its Singular Values
the noise (which is isotropic, i.e., occupies all dimensions)
Decomposition(SVD)implementationtoguaranteeasolution,
and combine coherently the two received radar reflections,
as illustrated in the Fig. 10. Taubin’s regression method was
we realize orthogonal projection of the steering vector on
chosen for its ability to minimize algebraic errors and its
signalsubspace,andweuseeigenvectorasamaximumpower
robustness against noise. It typically leads to a more accurate
combiner to enhance Signal-to-Noise Ratio (SNR).
fit than other least squares-based approaches. This technique
has been effectively implemented in previous works as stated
Algorithm 2 Direction of Arrival Estimation and SNR Im-
in [22] and [17].
provement
(cid:20) iq ant1 (cid:21) C. Skindisplacementextractionfromphasevariation
1: Input: x←
iq ant3 To extract phase variation of reflected radar echoes caused
2: Outp (cid:20) ut: x enh(cid:21) by skin displacement, we extract the first instantaneous phase
iq ant1
3: x← of the output signal from our eigen-beamformer. This in-
iq ant3
stantaneous phase must be unwrapped to retrieve its linearly
4: Rˆ ← xxH growing nature over time. Only phase fast variation rather
size(x)
5: [EigVecM,EigValM]←EVD(Rˆ) than linear behavior of instantaneous phase carry information
6: V max ←eigvec.max(EigVecM) about jugular pulse. To extract these variations, we use phase
7: for angle range do differences between successive phase samples.
(cid:2) (cid:3)T
8: a(θ)← 1 exp(−jπsin(θ))
10 9 : : P a S op D t ( ( θ θ ) ) ← ← (cid:104) a V H o | p m H V t a ( x m a θ ax ( ) | θ Rˆ ) (cid:105) a V op m t a ( x θ) • P S ha T s E e P e 1 st : im E a X t I i T o Q R n A : E C N T H IN A G NC P E H D AS S E IG I N N A F L ORMATION FROM
(cid:18) (cid:19)
11: end for θˆ(i )=arctan I signal ∈]−π;π[
12: DoA←Peak angle(PSD(θ)) Frame Q
signal
13: x enh ←aH opt (DoA)x • Phase unwrapping:
θˆ (i )=unwrap(θˆ(i ))
unwrapped Frame Frame
Selecting this modified version of beamforming is due to
one bin selection from the FFT-range function, which induces • Suppressing growing phase component:
pure sine wave function as an I/Q signal. In such one bin θˆ (i )=θˆ(i )−θˆ(i −1)
skin Frame Frame Frame

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
10 It is made available under a CC-BY-NC 4.0 International license .  JOURNAL,VOL.XX,NO.XX,XXXX202X
|     |     |     |     |     |     |     | D. SARandPDSimulationAnalysis |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Input noisy data
Taubin's best fit circle
Taubin's circle center SpecificAbsorptionRate(SAR)quantifiestherateatwhich
0
|     |     |     |     |     |     |     | the body | absorbs  | energy | when  | exposed      |     | to an   | electromagnetic |         |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------ | ----- | ------------ | --- | ------- | --------------- | ------- |
|     |     |     |     |     |     |     | field,   | measured | in     | watts | per kilogram |     | (W/kg). | This            | parame- |
-0.2 ter is essential for evaluating potential thermal impacts and
|      |     |     |     |     |     |     | ensuring                                            | adherence |     | to safety | regulations. |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --------- | --- | --------- | ------------ | --- | --- | --- | --- |
| -0.4 |     |     |     |     |     |     | Powerdensityreferstotheamountofpowerdistributedover |           |     |           |              |     |     |     |     |
aunitareaperpendiculartothedirectionofwavepropagation,
-0.6 indicating the intensity of power impacting a surface. Higher
|     |     |     |     |     |     |     | frequencies | result | in   | shorter | wavelengths. |       | As              | the wavelength |      |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ---- | ------- | ------------ | ----- | --------------- | -------------- | ---- |
|     |     |     |     |     |     |     | decreases,  | the    | same | amount  | of           | power | is concentrated |                | over |
-0.8
|     |     |     |     |     |     |     | a smaller | area.     | Therefore, |     | power          | density | tends | to           | increase |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | --- | -------------- | ------- | ----- | ------------ | -------- |
|     |     |     |     |     |     |     | as the    | frequency | rises.     |     | The mechanisms |         | and   | observations |          |
-1
|      |     |      |      |      |        |     | of these         | analyses | can       | be   | explained     | in        | terms | of skin         | depth |
| ---- | --- | ---- | ---- | ---- | ------ | --- | ---------------- | -------- | --------- | ---- | ------------- | --------- | ----- | --------------- | ----- |
|      |     |      |      |      |        |     | and penetration. |          | The       | skin | depth         | decreases |       | with increasing |       |
|      |     |      |      |      |        |     | frequency,       | as       | described | by   | the equation; |           |       |                 |       |
| -1.2 | -1  | -0.8 | -0.6 | -0.4 | -0.2 0 |     |                  |          |           |      |               |           |       |                 |       |
Fig. 10: Taubin Circular Regression of Noisy and Offset (cid:114)
2
|     |     |     |     |     |     |     |     |     |     | δ   | =   | ,   |     |     | (11) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
CircularData.Thismethodminimizesalgebraicdistancesand
ωµσ
| effectively | captures | the | underlying | circular | structure | in the |     |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | ---------- | -------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
presence of distortions. where, ω is the angular frequency, µ is the permeability, and
|      |     |              |     |                 |     |         | σ is the   | conductivity |                | of   | the tissue. | Higher    | frequencies  |        | lead   |
| ---- | --- | ------------ | --- | --------------- | --- | ------- | ---------- | ------------ | -------------- | ---- | ----------- | --------- | ------------ | ------ | ------ |
|      |     |              |     |                 |     |         | to smaller | δ,           | meaning        | more | energy      | is        | absorbed     | closer | to the |
|      |     |              |     |                 |     |         | surface.   | Also,        | the wavelength |      | is          | inversely | proportional |        | to the |
| STEP | 2:  | CONVERTING   |     | PHASE VARIATION |     | TO SKIN |            | λ            | = c,           |      | c           |           |              |        | f      |
|      |     |              |     |                 |     |         | frequency  |              | where          |      | is the      | speed     | of light     | and    | is the |
|      |     | DISPLACEMENT |     |                 |     |         |            |              | f              |      |             |           |              |        |        |
frequency.
|     |     |     |     |     |     |     | At  | lower | frequencies, |     | electromagnetic |     | waves |     | penetrate |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | --------------- | --- | ----- | --- | --------- |
λ
=θˆ
d skiniFrame skiniFrame × deeperintobiologicaltissues,resultinginalargerskindepth—
4π
|                   |      |            |       |                    |           |           | where     | the wave | power | drops     | to       | about         | 37%         | of its  | original |
| ----------------- | ---- | ---------- | ----- | ------------------ | --------- | --------- | --------- | -------- | ----- | --------- | -------- | ------------- | ----------- | ------- | -------- |
| Skin displacement |      | is related |       | to phase variation | using     | wave      |           |          |       |           |          |               |             |         |          |
|                   |      |            |       |                    |           |           | value—and | a        | more  | dispersed | energy   | distribution, |             | leading | to       |
| number k          | = 2π | rad/m,     | which | represents         | the phase | variation |           |          |       |           |          |               |             |         |          |
|                   | λ    |            |       |                    |           |           | a lower   | SAR      | near  | the skin  | surface. |               | Conversely, | at      | higher   |
1
ofEMwavesoverspace.Thefactor isduetotheround-trip frequencies,suchasat35GHz,thepenetrationdepthismuch
2
timeneededfortheradarsignaltohittheskinandcomeback
smaller,confiningthewaveenergytotheskin’ssurfacelayers.
to its receiver.
|           |        |              |     |            |     |     | This concentration |             |          | of energy | increases |          | the energy | density  | and  |
| --------- | ------ | ------------ | --- | ---------- | --- | --- | ------------------ | ----------- | -------- | --------- | --------- | -------- | ---------- | -------- | ---- |
|           |        |              |     |            |     |     | results            | in a higher | SAR      | at        | the skin  | surface. |            |          |      |
| Algorithm | 3 Skin | Displacement |     | Estimation |     |     |                    |             |          |           |           |          |            |          |      |
|           |        |              |     |            |     |     | Local              | SAR         | measures | the       | maximum   |          | energy     | absorbed | in a |
|           |        | (cid:16)     |     | (cid:17)   |     |     |                    |             |          |           |           |          |            |          |      |
ˆ i m a g ( x ) s m a ll t i s s u e v o l u m e ( ty p i c a l l y 1 g o r 1 0 g o f t i s s u e ) , p r o v i d in g
| 1 : ϕ r a w | ← a ta | n           | e n h a n c e d   |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------ | ----------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|             |        | r e a l ( x | e n h a n c e d ) |     |     |     |     |     |     |     |     |     |     |     |     |
ˆ ˆ a l o c a l i z e d e x p o s u r e e s ti m a t i o n . F o r t h e si m u l a t i o n , t h e p o w e r
| 2 : ϕ | ←   | u n w r a | p ( ϕ | )   |     |     |     |     |     |     |     |     |     |     |     |
| ----- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
u n wr appe d r a w is a v e r a g e d a c r o s s t h e v o l u m e t h a t e n c o m p a s s e s 1 g o f t i s s u e
| ϕˆ  | ←ϕˆ | [frame | (k+1)]−ϕˆ |     | [frame | k]  |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3: skin unwrapped unwrapped using the following calculation [23];
|      | ←ϕˆ  | λ   |     |     |     |     |     |     |     |      |     |       |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ----- | --- | --- | --- |
| 4: d |      | ×   |     |     |     |     |     |     |     |      |     |       |     |     |     |
| skin | skin | 4 π |     |     |     |     |     |     |     |      |     |       |     |     |     |
|      |      |     |     |     |     |     |     |     |     |      | σ   | |E |2 |     |     |     |
|      |      |     |     |     |     |     |     |     |     | SAR= |     |       | ,   |     |     |
(12)
2ρ
| A lowpass | filter | (0.75–4 | Hz) | was applied | to the | displace- |     |     |     |     |     |     |     |     |     |
| --------- | ------ | ------- | --- | ----------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ment signal, followed by a bandstop filter (0.9–1.1 Hz) to where E is the magnitude of the electric field, σ is the
reduce arterial pulsation impact. The filtering process was conductivity, and ρ is the mass density of biological tissue.
| guided by | a correlation |     | threshold | related | to the viability | of  |     |     |     |     |     |     |     |     |     |
| --------- | ------------- | --- | --------- | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pulse waves. We select the best pulse from the recording VI. RESULTS
| as a reference |     | to detect | the | best JVP | pulses. We | scan all |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recordings for pulses with the highest correlation coefficient A. SimulationAnalysisResult
using correlation. When we detect the desired number of best The SAR analysis indicates the amount of radiation ab-
JVP pulses, we mark their peak values. We can choose the sorbed into the skin and external jugular vein, as shown in
degreeofresemblanceconcerningthereferencepulsebyfixing Fig. 11. At 0.9 GHz, the SAR is affected by the wave’s
the correlation threshold of accepted JVP pulses. The JVP capacity to penetrate more deeply into the tissues, spreading
signalpresentsatransienteffectonbothendsoftherecording the energy absorption over a larger volume and consequently
because the filter time delay line is not fully loaded. The yielding a lower SAR at the surface. Conversely, at 35 GHz,
length of these transient portions of the signal is equal to the electromagneticwavesareabsorbedatmuchshallowerdepths,
combinedgroupdelayof765samples,causedbythebandpass concentrating more energy in the surface layers. This leads to
filter (0.75–4 Hz) and bandstop filter (0.9–1.1 Hz). a substantially higher SAR on the skin surface compared to

AUTHORetal.:ANON-INVASIVEANDNON-CONTACTJUGULARVENOUSPULSEMEASUREMENT:AFEASIBILITYSTUDY 11
lower frequencies. This simulation has enhanced our under-
standing of the anatomical positioning of the external jugular
vein, which is very close to the skin surface.
3.29 W/kg 0.22 W/kg 0.07 W/kg
35 GHz 5 GHz 0.9 GHz
seussit
kceN
ecafrus
nikS
nieV
raluguJ
lanretxE
Power density analysis (external Jugular vein)
35 GHz 5 GHz 0.9 GHz
148 W/m2 12 W/m2 1.4 W/m2
0.01 W/m2 1.2 W/m2 0.7 W/m2
Fig. 11: SAR analysis for skin surface, neck tissues, and
the external jugular vein at frequencies of 0.9 GHz, 5 GHz,
and 35 GHz. The visualization aids in understanding the
electromagneticenergyabsorptionpatternswithinthesetissues
at various frequencies.
The SAR analysis at higher frequencies primarily targets
the skin surface, with minimal absorption or scattering deeper
within the tissue. Consequently, this characteristic enables a
60GHzsensortoeffectivelydetectthejugularpulsebasedon
skin displacement.
The Power Density (PD) analysis of Fig. 12 indicates that
as the frequency increases, the wavelength correspondingly
decreases.Thisresultsinthesameamountofpowerdistributed
over a smaller area. As a consequence, the power density in-
creaseswithanincreaseinfrequency.Withlowerfrequencies,
thepowergetsdistributedinskinlayerslikemuscleandtissue.
TheincreaseinbothSARandpowerdensitywithfrequency
is primarily due to the reduced skin depth at higher frequen-
cies, which confines the energy absorption to the superficial
layers of tissue. Understanding this frequency-dependent be-
havioriscrucialforassessingtheapplicationsinvolvinghigher
frequency ranges, such as millimeter waves. This analysis
robustlydemonstratesthatwhenpositionedaccurately,theuse
of 60 GHz radar for estimating JVP predominantly captures
theJVPfromtheskinsurface,leveragingtheproximityofthe
external jugular vein to the skin.
This detailed analysis helps elucidate the underlying phys-
ical principles governing the interaction of EM waves with
biological tissues. It also highlights the importance of consid-
ering frequency when evaluating potential health risks of EM
exposure.
B. DataAnalysisResult
The extraction of the JVP signal experiences amplitude
fluctuations due to the non-quadrature (in-phase) radar re-
ecafrus
nikS
nieV
raluguJ
lanretxE
medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
It is made available under a CC-BY-NC 4.0 International license .
Fig.12:PowerDensityAnalysisfortheSkinSurfaceandEx-
ternalJugularVeinatFrequenciesof0.9GHz,5GHz,and35
GHz. This figure displays the calculated power density values
across different anatomical locations at each frequency. The
results highlight significant differences in power absorption,
with the highest densities observed at 35 GHz, emphasizing
the frequency-dependent behavior of electromagnetic wave
interactions with human tissues.
ceiver’s structure and random phase differences stemming
from varying path lengths, a phenomenon validated in our
acoustic experimental setup with stationary beat signals as
shown in Fig. 17.
Our study explores a proof of concept technology for
JVP detection using varying radar parameters, such as sam-
ples/chirp,chirps/frame,andsamplingfrequency.Ourfindings,
illustrated in Fig. 13, indicate improved JVP visibility with
higher samples/chirp and lower sampling frequencies; here,
we used 512 samples/chirp, 8 chirps/frame, and a 500 KHz
sampling frequency. The chirp duration was 132.987 µs. With
the controlled parameters, Fig. 14 illustrates the alteration in
the JVP waveform shape when the subject torso is in an
upright position. In such observation, ‘a’ peak was mostly
visible compared to other crests.
Observationrevealsthatnoteverypulsefeaturesdistinct‘c’
or ‘v’ peaks. Additionally, the fading phenomenon associated
with this sensor has obscured the shape of some JVP signals.
Hence, based on their clear morphological characteristics, we
chose to show 5 of the best JVP pulses in Fig. 13. The
JVP estimation hinges on pinpointing the genuine spike in
the FFT. With the radar situated in proximity to the skin, the
first range bin’s FFT I/Q data was leveraged to gauge skin
displacement (Fig. 15(a)). Nevertheless, we also successfully
extracted discernible JVP signals from the second and third
bins in certain instances.
Skin displacement measurement effectiveness can differ
basedoneachantenna’ssignalquality.Duetochallengeswith
ill-conditioned covariance matrices in the beamforming algo-
rithm from [17], we exclusively adopted the previously men-
tioned eigen-beamformer method, achieving a similar SNR as
both beamforming approaches produce co-linear vectors.

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
12 It is made available under a CC-BY-NC 4.0 International license . JOURNAL,VOL.XX,NO.XX,XXXX202X
1
0.1 a signal
signal matches found:
0.8 5 inclination: 45 0.05 c
data x
0.6 signals 0
v
0.4
JVP
waveform -0.05 y x'
0.2
50 100 150 200
0
-0.2
0 1000 2000 3000 4000 5000
Fig. 13: Detection of JVP waveforms in a Signal. The main graph displays the overall data signal (blue) with detected JVP
waveformshighlightedinred.Signalmatchesfound:5.Theinset(topright)zoomsintoatypicalJVPwaveform,markedfrom
points ‘a’ to ‘x’ and ‘x’ to ‘v’ indicating the ascent and descent of the waveform, respectively.
0.4 signal matches found: 4 0.05
data inclination: 90 a c signal
signals x
0
0.2
-0.05
50 100 150
0
0 2000 4000
Fig.14: The figure shows the extracted Jugular Venous Pulse (JVP) signal at an inclination of 90 degrees. The graph depicts
the signal variations over time, indicating the characteristic waveform associated with the JVP.
The DoA refers to the angle at which a received signal visualize some JVPs, not all of them are of the same qual-
arrives relative to a reference point or axis. In radar systems ity. These findings enhance our comprehension of parameter
used for physiological monitoring, when the body inclines adjustments necessary for improved JVP visibility.
or changes position, the geometry of signal reflection alters.
This means the reflected signals may travel different paths,
VII. DISCUSSION
changing the perceived DoA at the radar sensor. The DoA
estimationforJVPrangesbetween−20◦ and20◦ fordifferent Our experiment clearly demonstrates that the 60 GHz
inclinations. Fig. 15(b) illustrates the DoA estimation of JVP FMCW radar effectively performs non-invasive extraction of
waveform when tilted at a steep angle. JVP. The selection of a 60 GHz radar system is attributed
to its superior resolution and compact design featuring inte-
Fig. 16 shows the representation when the upper body of
grated antennas, which enhances its portability. Also, its high
thesubjectwasuprightwiththePPGrecordedsimultaneously
sensitivity is crucial for detecting subtle changes in the skin’s
from the right index finger using the mentioned device. A
surface caused by the underlying venous pulsations. In our
time delay of approximately 1.2884 seconds was noted, likely
scenario involving proximity measurements, we employed the
influenced by equipment buffering, processing delays, and
maximum bandwidth of 5.5 GHz for all recordings.
frequency variations. Conventionally, the JVP valley should
ItbecameapparentthatseveralfactorsinfluenceJVPperfor-
matchthePPGsignal’speak.Here,wecanobservethismatch
mance,notablythedistancebetweentheradarandthesubject.
at4,5,6,11and15secs.Itisknownthatduetogravitational
A radar positioned too closely can cause the initial spike to
influence and reduced hydrostatic pressure in the vein, the
blend with the DC component in the FFT, complicating the
visibility of JVP at 90◦ is very lower, but we managed to
identification of the actual spike. Accurately detecting this
get a visible JVP when upright by sticking to our controlled
spike is crucial for achieving high-resolution JVP estimations
parameters of the radar.
related to skin displacement. On the contrary, if the radar is
Fig. 17 shows the estimated JVP for different parameters too far, it cannot detect the pulse as the amplitude of JVP is
whenthesamplingfrequencyishigherat1GHzwithsamples very low. Therefore, we tried to keep an optimum distance of
per chirp as 128 and chirps per sample as 8. Though we can 2 mm from the skin surface for data recording.

AUTHORetal.:ANON-INVASIVEANDNON-CONTACTJUGULARVENOUSPULSEMEASUREMENT:AFEASIBILITYSTUDY 13
3
2.5
2
1.5
1
0.5
0
0 50 100 150 200 250 300 350 400 450 500
Frequency [KHz]
edutilpma
dezilamroN
10-4
(a) FFT-Range
1
0.8
0.6
0.4
0.2
0
-100 -80 -60 -40 -20 0 20 40 60 80 100
DoA [degrees]
DSP
dezilamroN
medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
It is made available under a CC-BY-NC 4.0 International license .
can significantly reduce the performance of the beam-
formerand,eventually,thepulsedetection.Therefore,an
antenna selection procedure must be adopted;
Also,ashorterchirpdurationishelpfulbecauseifthechirp
islonger,thechirpreflectioncollideswiththetransmittedone.
So, for better results, we narrowed down the parameter values
as the following:
TABLEI: Radar Configuration for optimal JVP estimation.
Parameter Value/Condition
Numberofsamplesperchirp 256orthehighestpossiblevalue
(b) Framerate 250Hzortheclosestpossiblevalue
Numberofchirpsperframe ≥8chirps
Chirpduration 0.00013secorclosestpossiblevalue
Note: Longer chirp durations are permissible if the radar-
skin distance increases. Additionally, increasing the receiver’s
gain is essential under these conditions.
The chip receiver incorporates a single in-phase mixer,
lacking a quadrature (Q) component, and thus generates a
real-valued IF signal. A Fourier transform is applied to this
IF signal during the processing, resulting in complex I and
Q signals that carry phase information for each frequency
component. An accurate radar provides time-varying perfor-
Fig. 15: (a) FFT-Range estimation across slow time for the mance compared to IQ radar due to phase variation. This
JVP detected at 45-degree in Fig. 13. The plot displays the architecture suffers from a fading phenomenon due to phase
normalized amplitude across various frequencies, highlighting offset between the reference signal and radar reflection. As
keyfrequencycomponentsthatcharacterizetheJVPsignal.(b) illustrated in the following figure, the signal is a function
PowerSpectralDensity(PSD)distributionforDoAestimation of time. Through the configuration illustrated in the figure
using radar sensor. The graph shows the normalized PSD simulator Fig. 18, we establish the critical enhancements
across different angles, revealing a prominent peak around offered by quadrature (Q) radar receivers over non-quadrature
−5◦, indicating the estimated direction of the signal source. or in-plain (I) counterparts, as outlined in [24].
The original beat signal exhibits a pronounced spike thanks
to its high amplitude, while radar-based beat reconstruction
reveals an inconsistent envelope signal stemming from the
Further observation reveals that reciprocal mixing among
phase difference between the received signal and the local
FFT-range bins mandates adjustments to the radar parameters
oscillator.Thisexperimentnotonlyconfirmstheeffectiveness
andexperimentalsetupenhancementsforoptimalJVPquality.
of our algorithm but also sheds light on the constraints
Despitetheradar’scapabilityforparametercustomization,the
related to the hardware. Therefore, we prefer to use a sensor
hardware imposes a strict correlation between the sampling
equipped with an IQ mixer for future experiments. In the
frequency and the number of samples per chirp. The utilized
phase extraction process, we employed the Taubin Circular
Infineon’s radar functions through fast chirp sequences, pre-
Regression method to identify the optimally centered circle
senting a challenge in detecting phase changes with just two
that aligns with our IQ signal, thereby compensating for any
chirps due to their rapid generation of chirps. To effectively
offset and distortion. Furthermore, the selection of the eigen-
extract phase information from the radar signals, a minimum
beamformer played a crucial role in addressing the issue of
of8chirpsisessentialforachievingaccurateresults.Through
the poorly conditioned correlation matrix.
meticulous evaluation, we established the subsequent config-
Often, JVP signals can overlap with or are superimposed
uration for JVP estimation with this radar:
by stronger signals from arterial pulsations or respiratory
• Higher sampling rate for a fast time (higher number movements.ThisoverlapcanmaskthedelicateJVPwaveform,
of samples per chirp) to increase FFT-range resolution. makingithardertoisolateandanalyze.Although [6]explored
Because a lower value implies a reduction of the signal non-contact JVP measurement with a 24 GHz microwave
quality and even burying the signal in noise; radar, it did not account for the influence of arterial signals.
• Suppress averaging on FFT-range spectrums over all Recognizing this challenge in our research, we employed a
chirps to avoid losing JVP signal details; supplementarybandstopfilterspecificallydesignedtodiminish
• Higher frame rate to get much more time resolution for the influence of arterial pulsations on the JVP signal. Our
JVP signal. DoA measurement gives us an accurate understanding of the
• Insomesituations,asignalwithlowSNRinoneantenna localization of the JVP signal.

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
14 It is made available under a CC-BY-NC 4.0 International license .  JOURNAL,VOL.XX,NO.XX,XXXX202X
1.5
JVP Signal
PPG Signal
edutilpmA dezilamroN 1
0.5
|     |     |     |     |     |     |     |     |     | a   | a   | a   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | a   |     |     |     |     |     | c   |     |     | a   |     |     |     |
a
|     |     |     |     | a   |     |     |     |     |     | c   | c   | a   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | c c |     |     |     |     |     |     |     |     | c   |     |     |
c
0
v
v
|     |     |     |     | v v |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
-0.5
10
|     | 0   |     |     | 5   |     |     | Time [sec] |     |     |     |     |     | 15  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.16:Comparativeanalysisofmanuallyannotated‘a’and‘c’peaksoftheJVPalongsidethereferencePPGsignalobtained
from a finger at a 90◦ angle. This illustration highlights the temporal alignment and amplitude differences between the venous
| pulsations             | observed | in the | neck | and the arterial | pulsations |     | measured | peripherally. |                |                |                  |         |       |             |     |
| ---------------------- | -------- | ------ | ---- | ---------------- | ---------- | --- | -------- | ------------- | -------------- | -------------- | ---------------- | ------- | ----- | ----------- | --- |
| edutilpmA dezilamroN 1 |          |        |      |                  |            |     |          |               |                | IX. CONCLUSION |                  |         |       |             |     |
| 0.5                    |          |        |      |                  |            |     |          | This          | study presents | a proof        | of               | concept | using | an FMCW     |     |
| 0                      |          |        |      |                  |            |     |          | radar sensor  | at 60          | GHz            | for non-invasive |         | JVP   | estimation, |     |
-0.5 offering a cost-effective alternative to traditional methods.
-1 Despite encountering certain hardware and design limitations,
| 0   |     | 5   |     | 10  | 15  |     | 20  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time [sec] we successfully measured the nuanced, millimeter-scale JVP
|     |     |     |     |     |     |     |     | and identified | optimal | parameters | for | its estimation |     | with | this |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ---------- | --- | -------------- | --- | ---- | ---- |
Fig.17:JVPsignalacquiredatanangleof45◦.Thedatawas
|     |     |     |     |     |     |     |     | technology. | This | sensor demonstrated |     | its | value | in precisely |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------------------- | --- | --- | ----- | ------------ | --- |
sampledatahighfrequencyof1GHz,capturing128samples
|                |     |          |      |         |     |     |     | determining | the DoA. | We also | conducted | a   | comparative |     | anal- |
| -------------- | --- | -------- | ---- | ------- | --- | --- | --- | ----------- | -------- | ------- | --------- | --- | ----------- | --- | ----- |
| per chirp over | a   | sequence | of 8 | chirps. |     |     |     |             |          |         |           |     |             |     |       |
ysiswithsimultaneouslyrecordedfingerPPGandexploredthe
impactofvariousbodyinclinationsonJVPmeasurements.It’s
| 1   |     |     |     |     |     |     |     | importanttorecognizethatphysiologicalfactorssuchasbody |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Data: Reconstructed Beat
| 0.5 |     |     |     |     |     |     |     | massindexandthecompositionoffatandtissuecaninfluence |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
JVPreadings,giventhejugularvein’slocationbeneathmuscle,
edutilpmA dezilamroN 0
skin,andfatlayers.Futureresearchwillexpandonthesefind-
| -0.5 |     |     |     |     |     |     |     | ingsinalargercohort.Insummary,the60GHzFMCWradar |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
hasprovenitspotentialinJVPestimationandofferspromising
-1
| 0   | 1 2 | 3   | 4   | 5 6 | 7 8 | 9   | 10  |           |            |             |     |            |       |      |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ----------- | --- | ---------- | ----- | ---- | --- |
|     |     |     |     |     |     |     |     | insights. | Addressing | the current |     | challenges | could | lead | to  |
1
|     |     |     |     |     |     |     |     | an effective | tool | for early | right HF | detection, |     | significantly |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | --------- | -------- | ---------- | --- | ------------- | --- |
Data: Original Beat
| 0.5 |     |     |     |     |     |     |     | reducinghospitaladmissionsbyprovidingavaluableresource |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
0 for clinicians and patients, especially in remote settings.
-0.5
REFERENCES
-1
| 0   | 1 2 | 3   | 4   | 5 6 | 7 8 | 9   | 10  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time [sec] [1] “Heart, stroke and vascular disease: Australian facts, Atrial fibrillation
-AustralianInstituteofHealthandWelfare—aihw.gov.au.”https:
| Fig.18: (Top):  | Beat   | signal | reconstructed | by  | Radar, | (Bottom): |     |                           |                   |             |                       |               |            |     |            |
| --------------- | ------ | ------ | ------------- | --- | ------ | --------- | --- | ------------------------- | ----------------- | ----------- | --------------------- | ------------- | ---------- | --- | ---------- |
|                 |        |        |               |     |        |           |     | //shorturl.at/bnRRb,2023. |                   |             | [Accessed28-05-2024]. |               |            |     |            |
| Original signal | played | on     | speaker       |     |        |           |     |                           |                   |             |                       |               |            |     |            |
|                 |        |        |               |     |        |           |     | [2] Y.-K.                 | Chan, C.          | Tuttle, J.  | Ball, T.-H.           | K. Teng,      | Y. Ahamed, |     | M. J.      |
|                 |        |        |               |     |        |           |     | Carrington,               | and               | S. Stewart, | “Current              | and projected | burden     | of  | heart      |
|                 |        |        |               |     |        |           |     | failure                   | in the Australian | adult       | population:           | A substantive |            | but | still ill- |
definedmajorhealthissue,”BMChealthservicesresearch,vol.16,no.1,
| Inspired | by the | application | of  | 60 GHz radar | for | blood | pres- | pp.1–10,2016. |     |     |     |     |     |     |     |
| -------- | ------ | ----------- | --- | ------------ | --- | ----- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- |
sure estimation in [17], we employed a radar to explore and [3] T.B.Conroy,J.Zhou,andE.C.Kan,“Jugularvenouspulsewaveform
|     |     |     |     |     |     |     |     | extraction | from | a wearable | radio frequency |     | sensor,” | IEEE | Sensors |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- | --------------- | --- | -------- | ---- | ------- |
analyze JVP as a proof of concept. Our study demonstrated Journal,vol.23,no.9,pp.10140–10148,2023.
the radar’s potential in JVP estimation, overcoming its design [4] I.Garc´ıa-Lo´pezandE.Rodriguez-Villegas,“Extractingthejugularve-
limitations. nouspulsefromanteriorneckcontactphotoplethysmography,”Scientific
reports,vol.10,no.1,p.3466,2020.
[5] A.Proto,D.Conti,E.Menegatti,A.Taibi,andG.Gadda,“Plethysmog-
|     |     |              |     |           |     |     |     | raphy | system to | monitor the | jugular venous | pulse: | a feasibility |     | study,” |
| --- | --- | ------------ | --- | --------- | --- | --- | --- | ----- | --------- | ----------- | -------------- | ------ | ------------- | --- | ------- |
|     |     | VIII. ETHICS |     | STATEMENT |     |     |     |       |           |             |                |        |               |     |         |
Diagnostics,vol.11,no.12,p.2390,2021.
The ethics considerations for this study are presented to, [6] S. Suzuki, M. Hoshiga, K. Kotani, and T. Asao, “Assessment of non-
contactmeasurementusingamicrowavesensortojugularvenouspulse
reviewed, and approved by the Human Research Ethics Com- monitoring,” Journal of Biomedical Science and Engineering, vol. 14,
mittee(HREC)atTheUniversityofSydneyunder[2024/104]. no.3,pp.94–102,2021.

medRxiv preprint doi: https://doi.org/10.1101/2024.06.04.24308313; this version posted June 7, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted medRxiv a license to display the preprint in perpetuity.
AUTHORetal.:ANON-INVASIVEANDNON-ICt OisN mTAaCdTe JaUvGaUilaLbAlRe VuEnNdOerU aS CPUCL-BSEY-MNECA S4U.0R IEnMteErnNaTt:ioAnFaEl AliSceIBnILsIeT Y. STUDY 15
[7] M. M. Applefeld, “The jugular venous pressure and pulse contour,”
ClinicalMethods:TheHistory,Physical,andLaboratoryExaminations.
3rded.Butterworths,1990.
[8] T.Nguyen,A.Dinh,F.M.Bui,andT.Vo,“Anovelnon-invasivesystem
for acquiring jugular venous pulse waveforms,” in 5th International
ConferenceonBiomedicalEngineeringinVietnam,pp.75–78,Springer,
2015.
[9] R. Amelard, R. L. Hughson, D. K. Greaves, K. J. Pfisterer, J. Leung,
D.A.Clausi,andA.Wong,“Non-contacthemodynamicimagingreveals
the jugular venous pulse waveform,” Scientific reports, vol. 7, no. 1,
p.40150,2017.
[10] B.Lipton,“Estimationofcentralvenouspressurebyultrasoundofthe
internal jugular vein,” The American journal of emergency medicine,
vol.18,no.4,pp.432–434,2000.
[11] P. Zamboni, A. M. Malagoni, E. Menegatti, R. Ragazzi, V. Tavoni,
M.Tessari,andC.B.Beggs,“Centralvenouspressureestimationfrom
ultrasoundassessmentofthejugularvenouspulse,”PLoSOne,vol.15,
no.10,p.e0240057,2020.
[12] F.Sisini,M.Tessari,G.Gadda,G.DiDomenico,A.Taibi,E.Menegatti,
M. Gambaccini, and P. Zamboni, “An ultrasonographic technique to
assess the jugular venous pulse: a proof of concept,” Ultrasound in
medicine&biology,vol.41,no.5,pp.1334–1341,2015.
[13] L.Wang,J.Harrison,E.Dranow,N.Aliyev,andL.R.Khor,“Accuracy
ofultrasoundjugularvenouspressureheightinpredictingcentralvenous
congestion,”AnnalsofInternalMedicine,vol.175,pp.344–351,2021.
[14] S. Suzuki, T. Matsui, H. Imuta, M. Uenoyama, H. Yura, M. Ishihara,
andM.Kawakami,“Anovelautonomicactivationmeasurementmethod
forstressmonitoring:Non-contactmeasurementofheartratevariability
using a compact microwave radar,” Medical & biological engineering
&computing,vol.46,pp.709–714,2008.
[15] M.PourEbrahim,F.Heydari,T.Wu,K.Walker,K.Joe,J.-M.Redoute,
andM.R.Yuce,“Bloodpressureestimationusingon-bodycontinuous
wave radar and photoplethysmogram in various posture and exercise
conditions,”ScientificReports,vol.9,no.1,p.16346,2019.
[16] J.E.Johnson,O.Shay,C.Kim,andC.Liao,“Wearablemillimeter-wave
deviceforcontactlessmeasurementofarterialpulses,”IEEEtransactions
onbiomedicalcircuitsandsystems,vol.13,no.6,pp.1525–1534,2019.
[17] N. Vysotskaya, C. Will, L. Servadei, N. Maul, C. Mandl, M. Nau,
J. Harnisch, and A. Maier, “Continuous non-invasive blood pressure
measurementusing60GHz-radar—afeasibilitystudy,”Sensors,vol.23,
no.8,p.4111,2023.
[18] M. Arsalan, A. Santra, and C. Will, “Improved contactless heartbeat
estimation in FMCW radar via kalman filter tracking,” IEEE Sensors
Letters,vol.4,no.5,pp.1–4,2020.
[19] A.Ahmad,J.C.Roh,D.Wang,andA.Dubey,“Vitalsignsmonitoring
of multiple people using a FMCW millimeter-wave sensor,” in 2018
IEEERadarConference(RadarConf18),pp.1450–1455,IEEE,2018.
[20] “The Small Intestine Channel of Hand Tai-Yang — meandqi.com.”
https://www.meandqi.com/tcm-education-center/
acupuncture/small-intestine-channel. [Accessed 20-03-
2024].
[21] W.Hu,Z.Zhao,Y.Wang,H.Zhang,andF.Lin,“Noncontactaccurate
measurement of cardiopulmonary activity using a compact quadrature
doppler radar sensor,” IEEE Transactions on Biomedical Engineering,
vol.61,no.3,pp.725–735,2013.
[22] M. Zakrzewski, A. Singh, E. Yavari, X. Gao, O. Boric-Lubecke,
J. Vanhala, and K. Palovuori, “Quadrature imbalance compensation
withellipse-fittingmethodsformicrowaveradarphysiologicalsensing,”
IEEEtransactionsonmicrowavetheoryandtechniques,vol.62,no.6,
pp.1400–1408,2014.
[23] N. Ticaud, S. Kohler, P. Jarrige, L. Duvillaret, G. Gaborit, R. P.
O’Connor, D. Arnaud-Cormos, and P. Leveque, “Specific absorption
rateassessmentusingsimultaneouselectricfieldandtemperaturemea-
surements,” IEEE Antennasand WirelessPropagation Letters, vol.11,
pp.252–255,2012.
[24] C. Li, Y. Xiao, and J. Lin, “Design guidelines for radio frequency
non-contact vital sign detection,” in 2007 29th Annual International
ConferenceoftheIEEEEngineeringinMedicineandBiologySociety,
pp.1651–1654,IEEE,2007.