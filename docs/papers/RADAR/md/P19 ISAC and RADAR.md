2026 IEEE 23rd Consumer Communications & Networking Conference (CCNC)
| AI-Enhanced |     |     |     |     | CW  | Radar |     | for Vital    | Sign |     | Monitoring |     |     |
| ----------- | --- | --- | --- | --- | --- | ----- | --- | ------------ | ---- | --- | ---------- | --- | --- |
|             |     |     |     |     | in  | ISAC  |     | Applications |      |     |            |     |     |
06366311.6202.97056CNCC/9011.01 :IOD | EEEI 6202© 00.13$/62/6-3769-5133-8-979 | )CNCC( ecnerefnoC gnikrowteN & snoitacinummoC remusnoC dr32 EEEI 6202 1st Woo-Jin Kim 2nd EunSung Jang 3rd Jae-Woo Park
Department of Electrical Engineering Department of AI Convergence Network Department of Electrical Engineering
|     |     | Ajou | University |     |     |     | Ajou | University |     |     | Ajou | University |     |
| --- | --- | ---- | ---------- | --- | --- | --- | ---- | ---------- | --- | --- | ---- | ---------- | --- |
Suwon 16499, Republic of Korea Suwon 16499, Republic of Korea Suwon 16499, Republic of Korea
kwj58383834@ajou.ac.kr jangstar@ajou.ac.kr woodenrain@ajou.ac.kr
|     | 4th | Minjun | Cho |     |     |     | 5th Sang-Jun | Park |     | 6th | Jeong-Wook |     | Kim |
| --- | --- | ------ | --- | --- | --- | --- | ------------ | ---- | --- | --- | ---------- | --- | --- |
Department of Electrical Engineering Department of Electrical Engineering Department of Electrical Engineering
|     | Ajou | University |     |     |     |     | Ajou | University |     |     | Ajou University |     |     |
| --- | ---- | ---------- | --- | --- | --- | --- | ---- | ---------- | --- | --- | --------------- | --- | --- |
Suwon 16499, Republic of Korea Suwon 16499, Republic of Korea Suwon 16499, Republic of Korea
minjun235@ajou.ac.kr pkparc@ajou.ac.kr jeongwookkim@ajou.ac.kr
| Abstract—This   |           | paper     | presents    |                     | a lightweight, |              | free-running |     |     |     |     |     |     |
| --------------- | --------- | --------- | ----------- | ------------------- | -------------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- |
| Continuous      | Wave      | (CW)      | radar       | system              | for            | non-contact  | vital        |     |     |     |     |     |     |
| sign monitoring |           | with      | enhanced    | sensing             | accuracy       | through      | deep         |     |     |     |     |     |     |
| learning-based  |           | frequency | correction. |                     | Unlike         | conventional | radar        |     |     |     |     |     |     |
| systems         | requiring | complex   |             | Frequency-Modulated |                |              | Continuous   |     |     |     |     |     |     |
Wave(FMCW)architecturesorhardware-levelstabilization,the
proposedsystemadoptsalow-costCWradarconfigurationwith
| audio       | waveform | acquisition, |     | enabling | compact  | deployment    |           | and |     |     |     |     |     |
| ----------- | -------- | ------------ | --- | -------- | -------- | ------------- | --------- | --- | --- | --- | --- | --- | --- |
| scalable    | data     | processing.  | To  | address  | the      | inherent      | frequency |     |     |     |     |     |     |
| instability | of       | free-running |     | systems, | a neural | network-based |           |     |     |     |     |     |     |
correctionschemeisemployed.Amongseveralcandidatemodels
| evaluated,      | Bidirectional     |             | Long            | Short-Term  | Memory             |                   | (Bi-LSTM)    |     |     |     |     |     |     |
| --------------- | ----------------- | ----------- | --------------- | ----------- | ------------------ | ----------------- | ------------ | --- | --- | --- | --- | --- | --- |
| model           | was selected      | for         | its superior    |             | accuracy           | and computational |              |     |     |     |     |     |     |
| efficiency.     | Experimental      |             | results         | demonstrate |                    | that              | the proposed |     |     |     |     |     |     |
| system          | achieves          | over        | 97%             | accuracy    | in respiration     |                   | and heart    |     |     |     |     |     |     |
| rate frequency  |                   | estimation, |                 | with low    | power              | consumption       |              | and |     |     |     |     |     |
| compact         | size.             | These       | characteristics |             | make               | the system        | suitable     |     |     |     |     |     |     |
| for integration |                   | as a        | sensing         | block       | within block-level |                   | Integrated   |     |     |     |     |     |     |
| Sensing         | and Communication |             |                 | (ISAC)      | architectures,     |                   | particularly |     |     |     |     |     |     |
inhealthcareapplicationswhereprecisephysiologicalmonitoring
is critical.
| Index | Terms—Free |     | running | CW  | radar, Deep | learning | based |     |     |     |     |     |     |
| ----- | ---------- | --- | ------- | --- | ----------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
Fig.1. ConceptoftheproposedCWradar-basedvitalsignmonitoringsystem
| frequency | correction, |     | Bi-LSTM, | ISAC, | Vital | sign monitoring |     |     |     |     |     |     |     |
| --------- | ----------- | --- | -------- | ----- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- |
withAI-basedcorrectionforISACapplications.
I. INTRODUCTION
|     |            |         |     |                   |     |     |        | have been widely | used | due to | their ability |     | to extract range |
| --- | ---------- | ------- | --- | ----------------- | --- | --- | ------ | ---------------- | ---- | ------ | ------------- | --- | ---------------- |
| An  | Integrated | Sensing |     | and Communication |     |     | (ISAC) | has              |      |        |               |     |                  |
gained considerable attention as a key enabling technology and Doppler information simultaneously [5], [6]. However,
for 6G, as emphasized in the IMT-2030 vision. ISAC aims FMCWsystemstypicallyrequirecomplexarchitectures,high-
|          |               |     |     |             |                 |     |        | speed analog-to-digital |     | converters | (ADCs), | and | Phase-Locked |
| -------- | ------------- | --- | --- | ----------- | --------------- | --- | ------ | ----------------------- | --- | ---------- | ------- | --- | ------------ |
| to merge | communication |     |     | and sensing | functionalities |     | within |                         |     |            |         |     |              |
a shared hardware and spectrum framework, enabling the Loop(PLL)basedsynchronization,whichhinderlow-costand
|     |     |     |     |     |     |     |     | compact integration, | especially |     | for sensing-only |     | modules in |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ---------- | --- | ---------------- | --- | ---------- |
developmentofcompact,multifunctionaldevices[1],[2].This
convergence is particularly important in emerging applica- modular ISAC architectures [7]. Several recent studies have
tions such as autonomous driving, smart manufacturing, and attemptedtoaddressthesechallengesthroughwaveform-level
orPhysical-level(PHY-level)integrationofradarandcommu-
| healthcare, | where | efficient |     | data exchange |     | and real-time | envi- |     |     |     |     |     |     |
| ----------- | ----- | --------- | --- | ------------- | --- | ------------- | ----- | --- | --- | --- | --- | --- | --- |
ronmental awareness must co-exist [3]. In healthcare-related nication blocks [8], [9]. Nevertheless, most still assume ideal
|            |          |     |                 |     |         |                  |     | hardware environments |     | or tightly | synchronized |     | components, |
| ---------- | -------- | --- | --------------- | --- | ------- | ---------------- | --- | --------------------- | --- | ---------- | ------------ | --- | ----------- |
| scenarios, | accurate |     | and non-contact |     | sensing | of physiological |     |                       |     |            |              |     |             |
signals such as respiration and heart rate is crucial, as it which limits practical deployment in scenarios demanding
enables continuous monitoring, early diagnosis, and elderly modularity, low power, and simplicity [10], [11].
care [4]. Radar-based solutions, particularly FMCW radars, To overcome these limitations, this paper proposes a
Authorized licensed use limited to: Institut Teknologi Sepuluh Nopember. Downloaded on March 31,2026 at 17:06:09 UTC from IEEE Xplore.  Restrictions apply.
979-8-3315-9673-6/26/$31.00 ©2026 IEEE

2026 IEEE 23rd Consumer Communications & Networking Conference (CCNC)
Fig.2. ConceptoftheproposedCWradar-basedvitalsignmonitoringsystemusingGRU-basedfrequencycorrection.
lightweight, free-running CW radar system for vital sign TABLEI
monitoring [12]. Instead of relying on PLL or hardware- SYSTEMPARAMETERSFORVITALSIGNMONITORING
| level frequency |     | stability, | the | system | utilizes | audio-domain |     |     |     |           |     |       |     |     |
| --------------- | --- | ---------- | --- | ------ | -------- | ------------ | --- | --- | --- | --------- | --- | ----- | --- | --- |
|                 |     |            |     |        |          |              |     |     |     | Parameter |     | Value |     |     |
signal acquisition combined with deep learning-based fre- CenterFrequency(fc) 24.125GHz
|        |             |               |     |                  |     |      |        |     |                       | Bandwidth(BW) |     | 0.25GHz |     |     |
| ------ | ----------- | ------------- | --- | ---------------- | --- | ---- | ------ | --- | --------------------- | ------------- | --- | ------- | --- | --- |
| quency | correction. | Specifically, |     | a Bi-directional |     | Long | Short- |     |                       |               |     |         |     |     |
|        |             |               |     |                  |     |      |        |     | SamplingFrequency(fs) |               |     | 44.1kHz |     |     |
TermMemory(Bi-LSTM)networkisemployedtocompensate
|               |     |             |             |     |              |     |           |     |     | Distance(R0)  |     | 1m      |     |     |
| ------------- | --- | ----------- | ----------- | --- | ------------ | --- | --------- | --- | --- | ------------- | --- | ------- | --- | --- |
| for frequency |     | instability | and improve |     | the accuracy |     | of respi- |     |     |               |     |         |     |     |
|               |     |             |             |     |              |     |           |     |     | Wavelength(λ) |     | 0.0124m |     |     |
ration and heart rate estimation [13]. As shown in Fig. 1, TimeWindowforFFT 10s
| the proposed |           | system consists |               | of two | functionally | separated  |     |     |     |     |     |     |     |     |
| ------------ | --------- | --------------- | ------------- | ------ | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| blocks:      | a sensing | block           | that performs |        | CW signal    | processing |     |     |     |     |     |     |     |     |
and AI-based correction, and a communication block that B. CW Radar-Based Vital Sign Monitoring Algorithm
modulatesandtransmitstheencodeddata.Bothblockssharea
|     |     |     |     |     |     |     |     | CW  | radar estimates | physiological |     | motion | by analyzing |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | --- | ------ | ------------ | --- |
singleantennausingtime-divisionmultiplexing(TDM),which
|                  |     |           |         |         |     |              |     | the phase | variation | of the | received | baseband | signal. | The |
| ---------------- | --- | --------- | ------- | ------- | --- | ------------ | --- | --------- | --------- | ------ | -------- | -------- | ------- | --- |
| allows alternate |     | operation | between | sensing | and | transmission |     |           |           |        |          |          |         |     |
displacementofthesubject’schestduetorespirationandheart
| without | additional | RF  | chains. | This | modular | and | compact |                 |     |     |     |     |     |     |
| ------- | ---------- | --- | ------- | ---- | ------- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- |
|         |            |     |         |      |         |     |         | rate is modeled | as: |     |     |     |     |     |
designenablesthesystemtoactasareusablesensingmodule
| in block-level |     | ISAC frameworks |     | [14]. |     |     |     |     |     |        |         |     |     |     |
| -------------- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | ------ | ------- | --- | --- | --- |
|                |     |                 |     |       |     |     |     |     |     | R(t)=R | +∆R(t), |     |     | (1) |
0
II. CWRADAR-BASEDVITALSIGNMONITORINGSYSTEM where R is the nominal distance to the target and ∆R(t) is
0
WITHAI-BASEDCORRECTIONDESIGN thetime-varyingdisplacementduetobreathingandheartrate.
2R(t),
|           |        |     |     |     |     |     |     | The round-trip | delay     | is expressed |     | as τ = | where | c is |
| --------- | ------ | --- | --- | --- | --- | --- | --- | -------------- | --------- | ------------ | --- | ------ | ----- | ---- |
| A. System | Design |     |     |     |     |     |     |                |           |              |     | c      |       |      |
|           |        |     |     |     |     |     |     | the speed      | of light. |              |     |        |       |      |
Fig. 2 illustrates the overall system architecture of the The transmitted and received CW signals are represented
| proposed | CW  | radar-based | vital | sign | monitoring |     | solution, |     |     |     |     |     |     |     |
| -------- | --- | ----------- | ----- | ---- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
by:
which integrates radar signal acquisition, motion extraction, s (t)=Acos(2πf t) (2)
|               |     |           |             |     |              |     |        |     |     | TX  |     | c   |     |     |
| ------------- | --- | --------- | ----------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| and GRU-based |     | frequency | correction. |     | The proposed |     | system |     |     |     |     |     |     |     |
(t)=A′cos(2πf
consistsofafree-runningCWradarfront-end,adigitalsignal s RX c (t−τ)) (3)
| processing | module, | and | an AI-based |     | correction | stage. | The |     |     |     |     |     |     |     |
| ---------- | ------- | --- | ----------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
radar acquires the baseband I-channel signal generated by After mixing and low-pass filtering, the Intermediate Fre-
|               |     |            |             |     |           |      |          | quency | (IF) signal | is obtained | as: |     |     |     |
| ------------- | --- | ---------- | ----------- | --- | --------- | ---- | -------- | ------ | ----------- | ----------- | --- | --- | --- | --- |
| chest motion, | and | an initial | respiration |     | and heart | rate | estimate |        |             |             |     |     |     |     |
isobtainedthroughanFFT-basedmethod.Theseestimatesare (cid:18) (cid:19)
4π
|              |     |             |            |     |         |     |         | s (t)=Acos |     | R(t) |     |     |     |     |
| ------------ | --- | ----------- | ---------- | --- | ------- | --- | ------- | ---------- | --- | ---- | --- | --- | --- | --- |
| then refined | by  | the Bi-LSTM | correction |     | network | to  | compen- | IF         |     |      |     |     |     |     |
λ
| sate for | frequency | drift | and noise. | This | modular | architecture |     |     |     |     |     |             |     |          |
| -------- | --------- | ----- | ---------- | ---- | ------- | ------------ | --- | --- | --- | --- | --- | ----------- | --- | -------- |
|          |           |       |            |      |         |              |     |     |     |     |     | (cid:18) 4π |     | (cid:19) |
enablescompactimplementationandsupportsintegrationwith
|                    |     |         |     |     |     |     |     |     |     |     | =Acos | (R +∆R(t)) |     | (4) |
| ------------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | --- |
|                    |     |         |     |     |     |     |     |     |     |     |       | λ 0        |     |     |
| ISAC communication |     | blocks. |     |     |     |     |     |     |     |     |       |            |     |     |
Authorized licensed use limited to: Institut Teknologi Sepuluh Nopember. Downloaded on March 31,2026 at 17:06:09 UTC from IEEE Xplore.  Restrictions apply.

2026 IEEE 23rd Consumer Communications & Networking Conference (CCNC)
where λ is the wavelength. The variation ∆R(t) includes
both low-frequency respiratory motion and higher-frequency
heart rate-induced vibrations. Thus, s (t) captures vital sign
IF
information through the time-varying phase.
Table I outlines the target system parameters and oper-
ational conditions for the proposed CW radar-based vital
sign monitoring. These parameters were selected based on
theoretical calculations and practical hardware limitations to
meettherequirementsofshort-range,non-contactdetectionof
respiration and heart rate.
In this work, only the I signal is captured and used in
all signal processing steps. The signal is segmented into 10-
second windows and subjected to Fast Fourier Transform
(FFT) to extract dominant frequency components. Respiration
is typically found from 0.2 to 0.5 Hz, while the heart rate
component lies from 1.0 to 1.8 Hz. Peak frequency detection
is performed within each band to estimate the respective vital
signs. To improve robustness, the extracted frequencies are
Fig.3. Bi-LSTMandLSTMArchitecture
aligned with sensor-derived ground truth data and averaged
across time windows.
TABLEII
TheseFFT-basedestimatesserveasinputstothesubsequent DEEPLEARNINGPARAMETERSFORVITALSIGNESTIMATION
AI-based correction stage, which compensates for estimation
Parameter Value
errors, as described in Section D.
Epoch 10000
In the proposed ISAC node, the communication path pack- BatchSize 16
agesthecorrectedvital-signparameters(respirationrate,heart NumberofHiddenUnits 50
rate, and quality flags) and transmits them through the same
RF front-end using TDM. The sensing/communication duty
cyclecanbeconfigured(e.g.,90%sensingand10%uplinkper long-term temporal dependencies and smooth out anomalies
cycle) to balance latency and power. Because the antenna and or noise in the radar measurements.
RFchainareshared,hardwareredundancyisminimizedwhile As shown in Fig. 3, each LSTM unit maintains an internal
periodic uplink reporting remains feasible without modifying memorycellc andanoutputhiddenstateh ,whichallowitto
t t
the radar front-end. carry information across time and update its state selectively.
At time t, given the current input x and the previous hidden
t
C. Deep Learning-Based Vital Sign Correction stateh (withpreviouscellstatec ),theLSTMcomputes
t−1 t−1
hree gate activations, namely the input i , forget f , and
CW radar vital sign signals exhibit temporal patterns that t t
outputo gates,aswellasacandidatecellstatec˜,asfollows:
span many time steps. To exploit these long-range depen- t t
dencies and correct any distortions, we employ a Bi-LSTM
i =σ(W [h , x ]+b ) (5)
t i t−1 t i
network as a temporal correction module in our pipeline. As
shown in Fig. 3, the Bi-LSTM comprises two LSTM layers,
f =σ(W [h , x ]+b ) (6)
t f t−1 t f
where one processes the input sequence from t = 1 to T
(forward in time) and the other from t = T down to 1
o =σ(W [h , x ]+b ) (7)
t o t−1 t o
(backward in time). The sequence of input feature vectors
over T time steps is denoted as {x ,x ,...,x }. The for-
1 2 T c˜ =tanh(W [h , x ]+b ) (8)
t c t−1 t c
ward LSTM processes this sequence to produce hidden states
→− →− →−
h 1 , h 2 ,..., h T , whereas the ←− backwar ←− d LSTM (processing where [h t−1 ,x t ] denotes the concatenation of h t−1 and x t ;
thesequenceinreverse)yields h
T
,..., h
1
.Ateachtimestep W
i
,W
f
,W
o
,W
c
∈ Rnh×(nh+nx) are the trainable weight
t, the forward and backward hidden vectors
→−
are c
←
o
−
ncatenated matrices, b
i
,b
f
,b
o
,b
c
∈ Rnh are the corresponding bias
to form a bidirectional representation h =[ h , h ], which vectors, n is the number of hidden units, and n is the
t t t h x
encodes context from both past and future around time t. inputfeaturedimension.Thegatevectorsi ,f ,o ∈[0,1] are
t t t
This context-rich vector is then passed to subsequent layers computed using the sigmoid activation σ, while the candidate
to estimate a corrected vital sign signal. In our design, the memory content c˜ is generated using the hyperbolic tangent.
t
Bi-LSTM outputs a refined sequence yˆ = [yˆ ,yˆ ,...,yˆ ] Thesegatesmodulatehowinformationflowsthroughthecell:
1 2 T
of the same length T, where each yˆ is the corrected vital f controls the fraction of prior cell memory c to retain
t t t−1
sign estimate at time t. By leveraging information from both (forgetting the rest), i governs how much new information
t
preceding and upcoming samples, the Bi-LSTM can model c˜ to write to the cell, and o determines how much of the
t t
Authorized licensed use limited to: Institut Teknologi Sepuluh Nopember. Downloaded on March 31,2026 at 17:06:09 UTC from IEEE Xplore. Restrictions apply.

2026 IEEE 23rd Consumer Communications & Networking Conference (CCNC)
updatedcellstateisrevealedasthenewhiddenstate.Thecell
| state and | hidden  | state        | are then | updated | as:             |     |      |       |     |     |     |     |
| --------- | ------- | ------------ | -------- | ------- | --------------- | --- | ---- | ----- | --- | --- | --- | --- |
|           |         | c =f         | ⊙c       | +i      | ⊙c˜             |     |      | (9)   |     |     |     |     |
|           |         | t            | t        | t−1     | t               | t   |      |       |     |     |     |     |
|           |         | h            | =o       | ⊙tanh(c | )               |     |      |       |     |     |     |     |
|           |         |              | t t      |         | t               |     |      | (10)  |     |     |     |     |
| where ⊙   | denotes | element-wise |          |         | multiplication. |     | This | gated |     |     |     |     |
memoryarchitectureenableseachLSTMcelltopreservelong-
terminformationwhiledynamicallyincorporatingnewinputs,
| effectively      | mitigating  |           | vanishing-gradient |                |            | issues.  | By chaining     |          |     |     |     |     |
| ---------------- | ----------- | --------- | ------------------ | -------------- | ---------- | -------- | --------------- | -------- | --- | --- | --- | --- |
| (and potentially |             | stacking) | such               | LSTM           | cells      | in       | a bidirectional |          |     |     |     |     |
| fashion,         | the network |           | can capture        |                | complex    | temporal |                 | patterns |     |     |     |     |
| in the           | vital sign  | data      | and                | learn          | to correct |          | distortions     | or       |     |     |     |     |
| motion           | artifacts   | over      | time.              | The overall    |            | Bi-LSTM  | correction      |          |     |     |     |     |
| architecture     | and         | the LSTM  |                    | cell mechanism |            | are      | summarized      |          |     |     |     |     |
in Fig. 3.
TableIIsummarizesthekeytraininghyperparametersofour Fig.4. ExperimentalsetupincludingCWradar,ECGsensor,respirationbelt,
andcontrolPC.
| deep learning-based |              | vital                 | sign     | correction     |     | model,     | including | the     |     |     |     |     |
| ------------------- | ------------ | --------------------- | -------- | -------------- | --- | ---------- | --------- | ------- | --- | --- | --- | --- |
| batch size,         | number       | of                    | training | epochs,        | and | number     | of        | hidden  |     |     |     |     |
| units. Each         | of           | these hyperparameters |          |                | was | determined |           | through |     |     |     |     |
| iterative           | experimental |                       | tuning   | and validation |     | to ensure  |           | optimal |     |     |     |     |
performance.Weincrementallyadjustedtheirvaluesandeval-
| uated the | model’s           | accuracy |      | and stability |     | on a | validation | set, |     |     |     |     |
| --------- | ----------------- | -------- | ---- | ------------- | --- | ---- | ---------- | ---- | --- | --- | --- | --- |
| selecting | the configuration |          | that | yielded       | the | best | results.   | This |     |     |     |     |
empiricaltuningprocessensuredthatthefinalhyperparameter
| settings          | provided | a balance |     | between     | training |            | efficiency | and |     |     |     |     |
| ----------------- | -------- | --------- | --- | ----------- | -------- | ---------- | ---------- | --- | --- | --- | --- | --- |
| model complexity, |          | resulting |     | in a robust |          | vital sign | correction |     |     |     |     |     |
model.
|            | III. IMPLEMENTATIONANDEXPERIMENT |     |              |              |       |                 |         |     |     |     |     |     |
| ---------- | -------------------------------- | --- | ------------ | ------------ | ----- | --------------- | ------- | --- | --- | --- | --- | --- |
| Fig. 4     | shows                            | the | experimental |              | setup | for radar-based |         | vi- |     |     |     |     |
| tal sign   | monitoring.                      | In  | the          | experiments, |       | the CW          | radar   | was |     |     |     |     |
| positioned | approximately                    |     | 1            | m in         | front | of the          | subject | at  |     |     |     |     |
chest height. The subject was instructed to remain still and (a) (b)
breathenormallythroughouttherecording.Eachsessionlasted
|     |     |     |     |     |     |     |     |     | Fig.5. Photographsoftheimplementedradarsystem:(a)Radarcontrolboard, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- |
approximately 5 minutes, long enough to capture multiple (b)RFbeamK-LC1Amodule.
| respiration | and      | heart | rate cycles. |     |             |     |              |     |     |     |     |     |
| ----------- | -------- | ----- | ------------ | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- |
| To obtain   | accurate |       | ground-truth |     | references, |     | two synchro- |     |     |     |     |     |
nized reference sensors were used during data collection. to a PC for further processing. This hardware setup allows
A respiration belt was placed around the subject’s chest to high-resolution, non- contact detection of chest movement
monitorthebreathingpattern,andanECGsensorwasattached associated with respiration and heart rate and serves as the
to the fingertip to measure the heart rate. input to the FFT-based and AI correction stages described in
|     |     |     |     |     |     |     |     |     | later sections. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- |
Theoutputsfrombothsensorsweretime-synchronizedwith
the radar data and served as ground-truth labels for both In addition to the controlled laboratory experiments, the
validation and training of the deep learning-based correction proposed CW radar system was also deployed and tested
model. This multi-sensor configuration ensured high-fidelity during a public exhibition, where multiple participants with
reference values for both respiration and heart rate. different physical conditions were monitored in real time.
|        |             |     |       |          |          |     |      |        | The exhibition | tests verified | that the radar | and AI correction |
| ------ | ----------- | --- | ----- | -------- | -------- | --- | ---- | ------ | -------------- | -------------- | -------------- | ----------------- |
| Fig. 5 | illustrates | the | radar | hardware | platform |     | used | in our |                |                |                |                   |
experiments. The system consists of an RFbeam K-LC1A pipeline maintained stable performance under diverse subject
24 GHz CW radar module integrated with an ST-100 starter conditionsandenvironmentalvariability,suchasdifferentpos-
kit board. The K-LC1A module provides a single-channel tures, slight movements, and varying ambient settings. These
analog I signal as the baseband output, corresponding to field results demonstrate that the proposed sensing system
canoperaterobustlyinreal-world,multi-personenvironments,
| the in-phase | component |     | of  | the reflected |     | wave. | This | signal |     |     |     |     |
| ------------ | --------- | --- | --- | ------------- | --- | ----- | ---- | ------ | --- | --- | --- | --- |
is amplified and digitized by the ST-100 board’s built-in confirming its practicality and reliability beyond controlled
ADC, which operates at an audio-band sampling frequency laboratory conditions.
of 44.1 kHz. The digitized signal is transmitted via USB Quantitatively, the proposed method achieves extremely
Authorized licensed use limited to: Institut Teknologi Sepuluh Nopember. Downloaded on March 31,2026 at 17:06:09 UTC from IEEE Xplore.  Restrictions apply.

2026 IEEE 23rd Consumer Communications & Networking Conference (CCNC)
TABLEIII
COMPARISONOFRADAR-BASEDVITALSIGNMONITORINGMETHODS
Frequency
|     | Ref. |     |     |     |     | TargetSignal. |     | CorrectionMethod. |     |     | RadarType. |     | Accuracy.(%) |     |     |
| --- | ---- | --- | --- | --- | --- | ------------- | --- | ----------------- | --- | --- | ---------- | --- | ------------ | --- | --- |
Band.(GHz)
|     | [15] |     |     | 24  |                 | HeartRate |     |     | Bi-GRU |     | CW   |     | 94.99          |     |     |
| --- | ---- | --- | --- | --- | --------------- | --------- | --- | --- | ------ | --- | ---- | --- | -------------- | --- | --- |
|     | [16] |     |     | 24  |                 | HeartRate |     |     | ANN    |     | CW   |     | 85             |     |     |
|     | [17] |     |     | 24  |                 | HeartRate |     |     | BSS    |     | CW   |     | 95.8           |     |     |
|     |      |     |     |     |                 | HeartRate |     |     |        |     |      |     | Respiration:89 |     |     |
|     | [18] |     |     | 61  |                 |           |     |     | Bi-GRU |     | CW   |     |                |     |     |
|     |      |     |     |     | RespirationRate |           |     |     |        |     |      |     | Heartrate:97   |     |     |
|     | [19] |     |     | 77  |                 | HeartRate |     |     | ANN    |     | FMCW |     | 88             |     |     |
Respiration:97.5
|     | This |     |     |     |                 | HeartRate |     |     |         |                |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --------------- | --------- | --- | --- | ------- | -------------- | --- | --- | --- | --- | --- |
|     | Work |     |     | 24  | RespirationRate |           |     |     | Bi-LSTM | CW(WithoutPLL) |     |     |     |     |     |
HeartRate:97.8
highaccuracyincomparisontothegroundtruth.Thecorrected
| respiration | frequency |     | reaches | an  | accuracy | of  | about | 97.5% |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ------- | --- | -------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
relativetothereference,whilethecorrectedheartrateachieves
| about 97.8% |       | accuracy. | In practical |     | terms,    | this      | corresponds | to      |     |     |     |     |     |     |     |
| ----------- | ----- | --------- | ------------ | --- | --------- | --------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| only a      | minor | deviation | between      |     | the radar | estimates |             | and the |     |     |     |     |     |     |     |
sensor measurements.
| For instance,    |             | the mean         | absolute         |        | error         | of the             | respiration  | rate     |     |     |     |     |     |     |     |
| ---------------- | ----------- | ---------------- | ---------------- | ------ | ------------- | ------------------ | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| after correction |             | is on            | the              | order  | of a few      | tenths             | of           | a breath |     |     |     |     |     |     |     |
| per minute,      | and         | the              | root-mean-square |        |               | error (RMSE)       |              | is like- |     |     |     |     |     |     |     |
| wise low,        | remaining   |                  | well             | under  | 1 breath/min. |                    | The heart    | rate     |     |     |     |     |     |     |     |
| estimation       | error       | is               | similarly        | small, | with          | a root-mean-square |              |          |     |     |     |     |     |     |     |
| error (RMSE)     |             | of approximately |                  |        | 2 beats       | per                | minute       | (BPM)    |     |     |     |     |     |     |     |
| or less.         | These       | error            | margins          | are    | negligible    | in                 | the context  | of       |     |     |     |     |     |     |     |
| normal           | respiratory | and              | cardiac          | rate   | variability,  |                    | underscoring |          |     |     |     |     |     |     |     |
| that the         | corrected   | radar            | outputs          | can    | reliably      | replicate          |              | the true |     |     |     |     |     |     |     |
vital signs. The near-98% accuracy also suggests a strong (a) Respiration rate
correlationbetweenthecorrectedradarmeasurementsandthe
groundtruth,withthecorrelationcoefficientapproachingunity
atR≈0.98,confirmingthattheBi-LSTMmodelsuccessfully
| generalizes   | across            | the               | test     | data.        |              |               |                |          |     |     |     |     |     |     |     |
| ------------- | ----------------- | ----------------- | -------- | ------------ | ------------ | ------------- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| As shown      |                   | in Fig.           | 6, the   | proposed     |              | Bi-LSTM       | correction     |          |     |     |     |     |     |     |     |
| model         | significantly     |                   | improves | the          | accuracy     | of            | vital          | sign es- |     |     |     |     |     |     |     |
| timates       | from              | the CW            | radar.   | In           | the          | bar graph     | of             | Fig. 6,  |     |     |     |     |     |     |     |
| the corrected |                   | radar-derived     |          | respiration  |              | and heart     | rate           | values   |     |     |     |     |     |     |     |
| closely       | match             | the ground        | truth    | measurements |              |               | from reference |          |     |     |     |     |     |     |     |
| sensors.      | The               | bars representing |          | the          | AI-corrected |               | estimates      | are      |     |     |     |     |     |     |     |
| nearly        | indistinguishable |                   | from     | those        | of           | the reference |                | for both |     |     |     |     |     |     |     |
respirationandheartrate,indicatingthatthemodeleffectively
| compensates      |            | for measurement |        | errors     | in          | the       | radar, including |         |     |     |     |           |      |     |     |
| ---------------- | ---------- | --------------- | ------ | ---------- | ----------- | --------- | ---------------- | ------- | --- | --- | --- | --------- | ---- | --- | --- |
| frequency        | drift      | and             | noise. | The        | respiration | frequency |                  | output  |     |     |     |           |      |     |     |
| after correction |            | tracks          | the    | true value | within      |           | a small          | margin, |     |     |     |           |      |     |     |
| and similarly    |            | the corrected   |        | heart      | rate        | aligns    | almost           | exactly |     |     |     |           |      |     |     |
| with the         | reference. |                 |        |            |             |           |                  |         |     |     |     | (b) Heart | rate |     |     |
Table III compares the performance of our approach with Fig. 6. Frequency comparison of radar-estimated, ground-truth, and AI-
existing works in the literature. The proposed Bi-LSTM cor- correctedvitalsignfrequenciesfor(a)respirationrateand(b)heartrate.
| rection         | outperforms |       | or matches       |     | the state-of-the-art |        |             | methods |     |     |     |     |     |     |     |
| --------------- | ----------- | ----- | ---------------- | --- | -------------------- | ------ | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| for contactless |             | vital | sign monitoring. |     | Prior                | non-AI | calibration |         |     |     |     |     |     |     |     |
techniquestypicallyachievedaccuraciesrangingfrom90%to
|     |     |     |     |     |     |     |     |     | sulted | in larger | errors, such | as  | several BPM | for heart | rate or |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------------ | --- | ----------- | --------- | ------- |
95%, and earlier neural network approaches reported accura- a few breaths per minute for respiration, and struggled with
| cies in | the mid-90% |     | range. |     |     |     |     |     |            |        |                 |     |         |               |      |
| ------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | ---------- | ------ | --------------- | --- | ------- | ------------- | ---- |
|         |             |     |        |     |     |     |     |     | oscillator | drift. | Recent AI-based |     | methods | have improved | per- |
In contrast, our model’s accuracy, ranging from about 97% formance, with some works reporting heart rate errors from 3
to 98% for both respiration and heart rate, is notably higher. to5BPMorcorrelationaround0.95,butourBi-LSTMfurther
For example, conventional peak-detection methods often re- reduces the error up to 2 BPM and pushes the correlation
Authorized licensed use limited to: Institut Teknologi Sepuluh Nopember. Downloaded on March 31,2026 at 17:06:09 UTC from IEEE Xplore.  Restrictions apply.

2026 IEEE 23rd Consumer Communications & Networking Conference (CCNC)
closer to 0.98. In terms of respiration, previous studies have Development of the signal processing and reconfiguable
shown mean errors of about 1 breath/min or more, whereas ASIC, and supported by National Research Foundation of
our approach brings the error below 0.5 breaths/min. As Korea (NRF) granted by the Korea government (MSIT) under
summarized in Table III, our corrected radar system achieves GrantNo.RS-2025-02303435,andalsosupportedbyNational
the highest accuracy among the compared methods. These Research Foundation of Korea (NRF) granted by the Korea
results demonstrate that leveraging a bidirectional LSTM for government (MSIT) under Grant No. RS-2025-24535709.
error correction provides a significant performance gain. The
model’sabilitytoincorporatetemporalcontextfrombothpast
REFERENCES
and future signal patterns enables more precise adjustments,
resultinginvitalsignreadingsthatrivalthefidelityofcontact [1] F.Adib,H.Mao,Z.Kabelac,D.Katabi,andR.C.Miller,“Smarthomes
thatmonitorbreathingandheartrate,”inProc.33rdAnnu.ACMConf.
sensors. Overall, the evaluation confirms that the proposed
HumanFactorsinComput.Syst.(CHI),Seoul,SouthKorea,Apr.2015,
AI-based correction approach offers superior reliability and pp.837–846.
accuracy in vital sign monitoring, marking an improvement [2] C. Li, V. M. Lubecke, O. Boric-Lubecke, and J. Lin, “A review on
recent advances in Doppler radar sensors for noncontact healthcare
over existing literature and validating the effectiveness of the
monitoring,” IEEE Trans. Microw. Theory Techn., vol. 61, no. 5, pp.
Bi-LSTM correction framework. 2046–2060,May.2013.
[3] M.Mercuri,J.P.Goossens,F.Horlin,andF.Naessens,“Jointestimation
IV. CONCLUSION ofrespirationandheartrateusingasingle-channelradar,”IEEETrans.
Biomed.CircuitsSyst.,vol.14,no.5,pp.1042–1051,Oct.2020.
In this work, we presented a lightweight, free-running CW [4] D.B.Le,H.Lin,F.Fioranelli,andQ.H.Abbasi,“Vitalsignmonitoring
radar system for non-contact vital sign monitoring, enhanced using frequency comb continuous wave radar and machine learning,”
IEEESens.J.,vol.21,no.10,pp.12230–12239,May.2021.
by a deep learning-based correction mechanism using a Bi-
[5] Y. Yang, Y. Li, and C. Li, “Wavelet transform-based micro-Doppler
LSTM network. Unlike conventional FMCW systems that signaturesforvitalsigndetectionwithaDopplerradar,”IEEEAntennas
rely on complex synchronization hardware such as PLLs, the WirelessPropag.Lett.,vol.16,pp.1040–1043,2017.
[6] F.AdibandD.Katabi,“SeethroughwallswithWi-Fi,”inProc.ACM
proposedradaroperateswithoutaPLLandemploysAI-based
SIGCOMM,HongKong,China,Aug.2013,pp.75–86.
correction to compensate for frequency instability. [7] T.Zhao,S.Tang,L.Lin,Q.Pu,andX.Zhang,“PIRate:Humansensing
Experimental results confirm that the Bi-LSTM model usingmmWaveradar,”Proc.ACMInteract.Mob.WearableUbiquitous
Technol.,vol.3,no.3,pp.1–23,Sep.2019.
significantly improves the accuracy of respiration and heart
[8] S.Tang,Q.Pu,S.Gollakota,andD.Wetherall,“Sleepingandbreathing
rate estimation, achieving accuracies of 97.5% and 97.8%, with Wi-Fi,” in Proc. 11th USENIX Conf. Netw. Syst. Design Imple-
respectively. These results verify that the proposed system ment.(NSDI),Seattle,WA,USA,Apr.2014,pp.349–362.
[9] Y.Wang,K.Wu,andL.M.Ni,“WiFall:Device-freefalldetectionby
maintainshighaccuracyevenwithoutPLL-basedstabilization.
wireless networks,” IEEE Trans. Mobile Comput., vol. 16, no. 2, pp.
Thesystem’scompactdesign,lowpowerconsumption,and 581–594,Feb.2017.
high accuracy make it well suited for integration into block- [10] T.Liu,W.Ma,X.He,andC.Li,“Contactlessheartrateandbreathing
rate monitoring with Doppler radar: Signal processing advances and
level ISAC architectures, particularly in healthcare applica-
future directions,” IEEE Signal Process. Mag., vol. 37, no. 4, pp. 81–
tionsrequiringcontinuousandunobtrusivemonitoring.Future 94,Jul.2020.
work will focus on expanding the dataset to include diverse [11] S. Iyer, L. Zhao, M. P. Mohan, J. Jimeno, M. Y. Siyal, A. Alphones,
and M. F. Karim, “mm-Wave radar-based vital signs monitoring and
subjectsandenvironments,aswellasextendingtheframework
arrhythmia detection using machine learning,” Sensors, vol. 22, no. 9,
toward multi-person monitoring and activity recognition. p.3106,Apr.2022.
Despiteitseffectiveness,theproposedsystemstillhassome [12] B.S.S.Charan,A.C.H.Chow,D.H.Werner,andB.M.Hochwald,
“Neuralnetworkaidedinterferencecancellationforvitalsignsmonitor-
limitations. The current CW radar configuration is optimized
ingusingmulti-antennaradar,”IEEETrans.Biomed.CircuitsSyst.,vol.
for respiration and heart rate estimation, but cannot extract 17,no.1,pp.153–166,Feb.2023.
directionalmotionorvelocityinformation.Infuturework,we [13] R. Wu, S. F. Tedde, P. M. Sarro, G. C. Cardinali, and A. Annoni,
“BreathingandheartratedetectionusingaCMOS-integratedRFradar
plan to integrate a communication module with the sensing
transceiver,”IEEESens.J.,vol.20,no.15,pp.8667–8675,Aug.2020.
block to realize a fully functional ISAC system and explore [14] Y. Kim and H. Ling, “Human activity classification based on micro-
joint radar–communication resource allocation. Doppler signatures using a support vector machine,” IEEE Trans.
Geosci.RemoteSens.,vol.47,no.5,pp.1328–1337,May.2009.
Beyond sensing, the proposed node supports a lightweight
[15] M.YavariandA.M.Eltawil,“Aself-interference-cancelingfull-duplex
communicationpaththatsharestheRFchainviatime-division front-end for Internet-of-Things applications,” IEEE Trans. Microw.
multiplexing (TDM). The corrected vital-sign parameters are TheoryTechn.,vol.66,no.4,pp.2056–2071,Apr.2018.
[16] L. Li, D. Liu, Y. Zhang, and J. Lu, “Millimeter-wave radar human
packetized and periodically uplinked with a configurable duty
detection based on attention U-Net,” IEEE Sens. J., vol. 22, no. 12,
cycle,enablinglow-powerreal-timereportingwithoutaltering pp.11495–11504,Jun.2022.
the radar front-end. This shared-hardware design aligns with [17] A. I. A. Mohd Ali, S. K. Sharma, S. Chien, J. K. Tan, M. F. Karim,
andA.Alphones,“FMCWradar-basedhumanpresencedetectionusing
ISAC principles and provides a practical bridge toward fully
recurrentneuralnetworks,”IEEESens.J.,vol.22,no.13,pp.13158–
integrated sensing and communication systems. 13166,Jul.2022.
[18] A. Va, T. Shimizu, G. Jain, and R. W. Heath, “Millimeter wave beam
ACKNOWLEDGMENT training: A survey,” IEEE Commun. Surveys Tuts., vol. 20, no. 2, pp.
1374–1393,2ndQuart.,2018.
This work was supported by Korea Planning & Evaluation [19] F.Adib,Z.Kabelac,andD.Katabi,“Multi-personlocalizationviaRF
InstituteofIndustrialTechnology(KEIT)grantedbytheKorea bodyreflections,”inProc.USENIXConf.Netw.Syst.Des.Implement.
(NSDI),Apr.2015,pp.279–292.
government (MOTIE) under Grant No. RS-2024-00446223,
Authorized licensed use limited to: Institut Teknologi Sepuluh Nopember. Downloaded on March 31,2026 at 17:06:09 UTC from IEEE Xplore. Restrictions apply.
