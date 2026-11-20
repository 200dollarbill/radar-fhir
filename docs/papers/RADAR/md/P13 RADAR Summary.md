BiomedicalSignalProcessingandControl75(2022)103597
Contents lists available at ScienceDirect
Biomedical Signal Processing and Control
journal homepage: www.elsevier.com/locate/bspc
A medical radar system for non-contact vital sign monitoring and clinical
☆
performance evaluation in hospitalized older patients
Hoang Thi Yena, Masaki Kurosawaa, Tetsuo Kirimotoa, Yukiya Hakozakib, Takemi Matsuib,
Guanghao Suna,*
aThe University of Electro-Communications, Tokyo, Japan
bTokyo Metropolitan University, Tokyo, Japan
A R T I C L E I N F O A B S T R A C T
Keywords: Medical radar plays an important role in non-contact vital sign monitoring. However, radar is sensitive and
24 GHz radar susceptible to noise that deteriorates signal quality, making its application unstable in medical practice settings.
Vital signs Previous studies have focused on detecting vital signs from radar output, but mainly used high-quality signals in
Signal quality
laboratory settings. Therefore, signal quality evaluation to maintain good-quality signals for processing is crucial
Cheyne-Stokes respiration
for radar applications. This paper presents a vital sign monitoring system using medical radar that automatically
Sleep apnea
evaluates signal quality to eliminate unsatisfactory signals using the support-vector machine and to extract
heartbeat and respiration signals using the singular value decomposition method. To evaluate the system per-
formance, we tested it on 10 healthy subjects and compared the obtained vital signs with those measured using a
contact-type ECG device and a respiration belt. Two evaluation steps were conducted. First, we measured 10
subjects for evaluating the signal quality in a laboratory setting. The results showed that the accuracy for each
subject archive was 93.2%–100%. Second, we extracted vital signs including respiration rate (RR) and the heart
rate (HR) following signal quality classification. The results showed RR and HR deviation from 0 to 1 bpm, and
0 to 4 bpm, respectively. Moreover, the system was applied in a real medical practice setting for continuously
monitoring the bedside of hospitalized older patients at a hospital.
1. Introduction proposed by Lee and Lin to measure the movement of the peripheral
artery wall in relation to the pressure pulse wave and to extract clinical
Vital signs are a group of medical signs that include respiration rate features from the signal [8]. Many studies have suggested the use of a 24
(RR), heart rate (HR), blood pressure (BP), and body temperature (BT). GHz CW radar to monitor vital signs at home, resulting in high efficiency
These signs indicate the status of physical and psychological stress level and cost savings, as compared to monitoring at the hospital [9,10].
[1,2]. Changes in RR and HR in people at risk of cardiopulmonary arrest However, this medical radar has the problem of sensitivity to noise,
and healthy subjects are more substantial than changes in other vital and the signal quality is reduced by even slight body movements. Pre-
signs such as BP and BT [3]. RR and HR are significantly related to and vious studies have shown that the vital sign detection algorithm may not
can help diagnose lung and cardiovascular diseases [4–6]. When be accurate in the presence of body movements in the signal. A
monitoring these vital signs by the traditional method, many electrodes mismatch between the RR and HR extracted from radar and reference
or terminals are placed on the body of the patients, which makes them signals occurs when there is a body movement [11]. However, the
uncomfortable. Furthermore, the traditional method is unsuitable for literature on signal quality evaluation is scarce. In [12], assessed signals
patients with skin abrasions and for long-term monitoring. The non- were taken from Internet databases, which were collected from iPhone
contact method has the potential to meet these requirements with the applications and digital stethoscopes. Training signals were divided into
use of radar to monitor cardiac volume changes. It was first published in three groups: bad, good, and excellent, and support-vector machine
1972 by Johnson and Guy [7]. A continuous-wave (CW) radar was (SVM) were used as the training model. The authors in [13] used 24 GHz
☆ This research was funded by the JSPS KAKENHI Grant-in-Aid for Scientific Research (B) under Grant 19H02385.
* Corresponding author.
E-mail address: guanghao.sun@uec.ac.jp (G. Sun).
https://doi.org/10.1016/j.bspc.2022.103597
Received 25 November 2021; Received in revised form 4 February 2022; Accepted 20 February 2022
Availableonline25February2022
1746-8094/©2022ElsevierLtd.Allrightsreserved.

H.T. Yen et al. B i o m e d i c a l S i g n a l P r o c e s s i n g a n d C o n t r ol75(2022)103597
radar to classify heart sound signal quality using six-port interferometers channel signals with the detailed inference in [23] are
based on ensemble classifiers but not vital signs. In [14], vital sign ( )
4πs(t) 4πd
quality assessment was based on autocorrelation and spectrum analysis, B I (t)=A r .cos λ (cid:0) λ 0(cid:0) θ (1)
with an impulse radio ultra-wideband (IR-UWB) radar signal as input.
( )
To avoid body movements, another study attempted to collect high- 4πs(t) 4πd
quality signals from patients after they lied motionless in bed for 5 B Q (t)=A r .sin λ (cid:0) λ 0(cid:0) θ (2)
min [15]. For signals without body movements, vital sign peaks were
detected using Doppler radar signals [9,10,16–18]. Paper [19] extracted where θ =(4πvt0 )/λ, s(t)is the equation for the body wall movement
RR and HR used 24 GHz radar with a short signal window, but required and λ is the wavelength of the transmitted signal from the radar. Without
high-quality signal as input. Previous studies used high-quality radar
loss of generality, I and Q channel signals can be rewritten as
signals to diagnose diseases related to cardiopulmonary diseases. Res- ( )
p p i a r t a ie to n r t y s fo ab r n 2 o 4 r h m [ a 2 li 0 t ] ie . s B y w d e e r t e e c d t i i a n g g n R o - s p e e d a k a s s , h p e n a e r u t m ra o t n e i v a a r b i y a b m ili o ty n i ( t H or R in V g ) I(t)=B I (t)/A r =cos 4π λ s(t) (cid:0) 4π λ d 0(cid:0) θ (3)
was estimated, with the input was without body movement [21]. By ( )
4πs(t) 4πd
observing the trend of HRV using 24 GHz radar Doppler signals, disease Q(t)=B Q (t)/A r =sin λ (cid:0) λ 0(cid:0) θ (4)
related to heart failure was detected [22].
In this study, a 24 GHz CW radar is used, and the above-mentioned
The I and Q signals can be represented on a trigonometric circle
problems are solved in two steps. First, we perform signal quality clas-
(Fig. 2b). After dividing the corresponding side of (4) by (3), the equa-
sification based on the SVM algorithm with the extraction of eight well-
tion of the body surface movement at any time t is given as Eq. (5).
suited features. Signals are classified into two groups: high- and low- ( )
q ra u n a d li o ty m , i m n ov w e h m ic e h n ts lo w an -q d u a h l i i g ty h -q s u ig a n li a t l y s s a i r g e n a o ls b ta w in it e h d o u a t s b h o a d v y i n r g a n b d o o d m y s(t)= 4 λ π .arctan Q I( ( t t ) ) +d 0 + 4 λ π .θ (5)
movements. Next, for the group of high-quality signals, we use the filter From Eq. (5), if we call s0 =d0 +(λ.θ/4π)as the starting point, x as
and singular value decomposition (SVD) algorithm combining single the displacement, and α =arctan∠(Q(t),I(t)), then x can be written as
vectors to obtain RR and HR. With the RR and HR extraction, the results
show that the vital sign peaks are significantly clearer than those in the x= λ .α (6)
conventional method and without harmonic peaks. The methods in each 4π
step are described in Section 2. Section 3 demonstrates the evaluation of Eq. (6) means that the displacement x=λ/2 corresponds to a circle.
the algorithms based on healthy subject signals and their clinical If the displacement of the object is greater than λ/2, the Doppler fre-
application. Finally, discussions and conclusions are given in Section 4. quency can be observed on the signal, and the channels I and Q are al-
ways balanced in amplitude. However, the displacement of the body
2. Method wall from the back side is always less than 2 mm [24,25] while
λ/2≃6.2mm. Therefore, the signals can be imbalanced. The object-to-
In this section, the solution to the radar problem is given, from radar distances are chosen to obtain balanced signals between the I
assessing the signal quality that can obtain the qualified signal. Subse- and Q channels. The optimal distance was taken by previous work [26],
quently, from the high-quality signal, RR and HR are extracted. Fig. 1 however that paper used one channel and transmitted double-sideband.
shows a schematic of the system with the processing steps. The following In this paper, we used 2 channels of 24 GHz and gave the optimal dis-
subsections demonstrate in detail the processing. tance from radar to object to obtain amplitude balanced signals.
When a balanced distance is represented on the unit circle, it lies on
2.1. Principle of the vital sign measurement using radar the bisectors of the four quadrants, as shown in Fig. 2b. The distance is
expressed by Eq. (7).
The structure of the CW 24 GHz Doppler radar (New Japan Radio,
NJR4262) is shown in Fig. 2a. The baseband signals including I and Q
Fig. 1. Complete vital sign monitoring system based on a 24 GHz radar.
2

H.T. Yen et al. B i o m e d i c a l S i g n a l P r o c e s s i n g a n d C o n t r ol75(2022)103597
Fig. 2. Structure of the 24 GHz radar and the balanced position.
λ λ λ amplitude of body random motion is normally greater than that of the
d b = 16 +k 8 (cid:0) 4π α 0 , k∈Z (7) body wall due to vital signs. Therefore, when the distance from the body
to the radar is fixed, random body movements produce a larger ampli-
where α 0 is arctan∠(Q(t),I(t))at distance n.λ/2(n∈Z)with the easiest tude in the radar signal, as shown in Fig. 4a. Therefore, the amplitudes of
visualization at n = 0. In Eq. (7), the component λ/16 stands for the two signal channels I and Q were chosen as the extracted characteristics.
position of the first quadrant bisector, and k.λ/8 shows that when the Second, because the displacement due to vital signs when measuring
distance increases or decreases by a multiple of λ/8, the signal will be from the back side is small, the demodulation output from the arctan-
balanced, as shown in Fig. 2c. The component λ.α 0 /4π is the phase angle gent (arctan(Q(t)/I(t))) is uniformly variable. However, the displace-
of distance n.λ/2(n∈Z). Especially at multiples of distance λ/4, the ment due to the body random movement is mostly greater than half of
phase angle demodulation of the two channels will repeat. the wavelength; therefore, the demodulated arctangent will rise and fall
for a segment of the signal, as shown in Fig. 4b.
In addition, for the signal without a body random movement, the
2.2. Signal quality assessment using support vector machine
center frequency in a signal segment will be the rate of breathing, fol-
lowed by the frequency of the HR, and noise but with low power.
For the signal quality assessment, the length of a sample as 10240 ms
However, for the signal with the body random movement, the frequency
was taken. In detail, each sample on each channel includes 1024 sam-
of the movement will prevail; therefore, the frequency is different from
pling points with a 100 Hz sampling frequency. Hereinafter, each sample
the frequency of vital signs, as shown in Fig. 4c. The definition of the
includes 1024 sampling points of the I channel and 1024 sampling
features is illustrated in Fig. 4. The features are then fed to the Quadratic
points of the Q channel. The diagram of the signal quality assessment
SVM training model with a K-fold of 5, Box Constraint of 1, Kernel Scale
can be demonstrated as Fig. 3. Based on the radar principle, eight fea-
is “auto” and output of 2 classes: low-quality samples are labeled as “1”
tures were extracted for each sample to input the classification model.
and high-quality samples are labeled as “(cid:0) 1”. By setting the model
Radar principle reveals that the radar output signal at a determined
training parameters, the hyperplane separating two classes is found
distance and without body random movement, amplitude, phase dif-
[27,28]. Then the weights are saved and the test sample is input.
ference between the two channels, and center frequency of the signal are
within a certain range.
First, radar works based on the Doppler effect, and the radar output
reflects the displacement of the body surface when measured. The
Fig. 3. Block diagram of the signal quality assessment system.
3

H.T. Yen et al. B i o m e d i c a l S i g n a l P r o c e s s i n g a n d C o n t r ol75(2022)103597
Fig. 4. Eight features extracted from radar signal. a) Based on amplitude; b) Based on arctangent; c) Based on frequency; for the high-quality sample (left side) and
the low-quality sample (right side).
4

H.T. Yen et al.                                                                                                                                                                          B  i o  m   e d  i c a  l  S  i g n  a  l  P r  o c  e s  s i n  g  a  n  d   C  o n  t r  ol75(2022)103597
2.3. Vital sign extraction with singular value decomposition
By using the 24 GHz radar, the body wall motion due to vital signs is
smaller than half of the wavelength, and one peak of the radar signal
corresponds to one peak of respiration [23]. Therefore, respiration peaks
can be extracted by enveloping raw high-quality signals, so MATLAB’s
envelope function is used.
To determine the HR, two steps are implemented as follows. First, a
band-pass filter with a pass frequency range of 0.7–3 Hz is used. In this
range, the main component frequency is the HR, but harmonic. Next,
based on SVD, a single frequency contained in the signal is separated. By
combining vectors and singular values, the component frequencies
contained in the signal are separated [29]. Therefore, the heartbeat can
be determined without harmonics; specifically, a window of 512 sam-
pling points is used to obtain one sample for extraction. A total of 512
sampling points are [x(1),x(2),...,x(512)], and they are spread in a
matrix, as in (8).
| ⎡      |                   | ⎤      |      |
| ------ | ----------------- | ------ | ---- |
| x(1)   | x(2) ... x(257)   |        |      |
| ⎢ x(   | ) x( ) . . . x(2  | 8)⎥    |      |
| X= ⎢ 2 | 3                 | 5 ⎥    |      |
| ⎣ .. . | .. . . . .        | .. . ⎦ | (8)  |
| x(256) | x(257) ... x(512) |        |      |
Next, the SVD algorithm is implemented according to (9).
| [U,D,V]=svd(X)                      |                                                             |                                      | (9)   |
| ----------------------------------- | ----------------------------------------------------------- | ------------------------------------ | ----- |
| where the left orthonormal U=(u1    |                                                             | ,u2 ,...,un ) with uj is the column  |       |
| vector, the right orthonormal V=(v1 |                                                             | ,v2 ,...,vm ) with vj is the column  |       |
| vector, and σ                       | j is the singular value. Thus, u1 and u2 are the first and  |                                      |       |
second columns in matrix U ; v1 and v2 are the first and second columns
| in matrix V, σ | 1 and σ |     |     |
| -------------- | ------- | --- | --- |
2 are the first and second non-zero singular values
in D. Subsequently, H
12 is calculated as in (10).
| H 12 =σ 1 u 1 vT | +σ 2 u 2 vT |     | (10)  |
| ---------------- | ----------- | --- | ----- |
1 2
| H 12 has the same size as X. By averaging each anti-diagonal of H |                                                |     | 12,  |
| ----------------------------------------------------------------- | ---------------------------------------------- | --- | ---- |
| we obtain a row vector H                                          | 1 of size [1 ×512] that matches the length of  |     |      |
the signal sample under consideration. Continuing to slide the sample
window to the next signal sample, the next row vector is obtained. This
process is repeated until the end of the data. Redrawing the results, it can
be seen that the signal clearly shows peaks corresponding to the R peak
of the ECG wave. The HR extraction process is shown in Fig. 5.
2.4. Experiment and data description
We created datasets in our laboratory to measure the vital signs of
healthy individuals. We performed measurements on 10 healthy in-
dividuals, including 3 females and 7 males (age: 19–32 years, height:  Fig. 5. Algorithm diagram to determine heart beat.
160–179 cm, and weight: 53–75 kg). Being different from the approach
and measurement method of the previous paper which measured vital  the posture and position, they themselves had to move up and down, left
sign from the chest when subject sit on the chair [19], our paper practice  and right. Therefore, for the first 5 min, the signal included body
measuring from the back when the person was lying in bed. Healthies  movements. Afterwards, they were asked to keep still to obtain good-
subjects were asked to lie in a bed with the radar attached to the bottom,  quality data. The measurement setup is shown in Fig. 6.
and the distance from the radar to the upper surface of the bed was 20  For the clinical data, after evaluating the system on the healthy in-
cm. When measuring the signal, they wore contact measuring devices,  dividuals, we applied the proposed method to inpatient data. We applied
including an ECG device (BIOPAC ECG100C) and a respiration belt  the signal assessment and the vital sign extraction to patient data from
(NIHON KOHDEN, SR-601S, Japan) to obtain the reference signal. The  the Yokohama Hospital, Japan, with one week of data processing for a
patient presenting with Cheyne-Stokes respiration and a patient with
experiment protocol was designed to create training and testing datasets
symptoms of sleep apnea. The results showed that both patients had
with ground-truth labeling, respectively. To obtain the datasets with
ground-truth labeling, we both control the time that the subject lies on  abnormalities in RR and HR before and during the disease symptoms.
the bed performing the body movement, and the time of lying motion- This study was approved by the Ethics Committee of the Yokohama
less. Each individual was required to take 2 measurements, one mea- Hospital and the Committee on Human Research of the Faculty of Sys-
surement to collect data for training, and one measurement to collect  tem Design, Tokyo Metropolitan University, and the Ethics Committee
data for testing. The training session lasted 20 min, during which there  of the University of Electro-Communications. All participants provided
was a period with movement (labeled as low-quality “1”) and without  written informed consent.
| movement (labeled as high-quality “(cid:0) |     | 1”). The testing dataset mea- |     |
| ------------------------------------------ | --- | ----------------------------- | --- |
surement time was 10 min. In the beginning, owing to the adjustment of
5

H.T. Yen et al.                                                                                                                                                                          B  i o  m   e d  i c a  l  S  i g n  a  l  P r  o c  e s  s i n  g  a  n  d   C  o n  t r  ol75(2022)103597
this study, we find the peaks of respiration by taking the envelope, thus
ignoring the effect of the HR, by using the envelope function in MATLAB
2020. An example of this result is shown in Fig. 7.
The results of RR in 5 min for 10 healthy individuals are shown in
Table 2. From Table 2, we can see that the difference in RR (subtraction
of the referenced RR from the proposed RR) between the reference and
proposed method ranges from 0 to 3 bpm, only 1 min out of the total 50
min of survey is 3 bpm, and the difference is mainly from 0 to 1 bpm (47
of 50 min of survey), as in Fig. 8a. The correspondence of the RR results
between the reference and the proposed method is shown by the scatter
plot and the correlation coefficient, as shown in Fig. 8b.
For the heartbeat signal, the signal segment after being classified into
the high-quality group was passed through a filter with the pass fre-
quency range of 0.7–3 Hz and then, taken at intervals of 5120 ms. Each
segment of 5120 ms signal was spread out into a matrix, which was fed
Fig. 6. Setup to measure healthy individuals.   into the SVD algorithm. Subsequently, the first and second orders were
taken. By combining the single value, a matrix of the same size as the
3. Results  spread matrix of the signal was obtained. By averaging the anti-diagonal
of the resulting matrix, we obtained a signal with clear heartbeat peaks.
The results using the filter only and using combined filter and SVD, are
3.1. Evaluation on the healthy individuals in the laboratory
shown in Fig. 9. When using filter in frequency range 0.7–3 Hz, signal
still contains noise harmonic, so when executing “findpeaks” function in
For the signal quality classification of healthy individuals, we per-
MATLAB, the number of peaks after band-pass filter is larger than the
formed signal measurements of 10 healthy individuals. First, the in-
one of the ECG, and therefore inaccurate. However, after using SVD to
dividuals were asked to move until their chest position coincided with
process, the peak of the heart beat is clearer and more accurate. The
the position where the radar was located below. At these time intervals,
reason is that, with high-quality signal, in the range of 0.7–3 Hz, the
the system obtained low-quality signals. Once they were positioned on
the chest wall directly above the radar and their body remained sta- frequency of the heart beat dominates with largest power, so it is located
tionary, the received signal was of good quality.  in the first and the second order, while the harmonics are located in the
We measured and labeled 60 min of low-quality signals and 60 min
of high-quality signals. Each signal sample was 1024 sampling points
(10240 ms), and the signal samples were passed through the pre-
processing block to extract eight features (as shown in Fig. 3). The
samples with eight features were then trained using the Quadratic SVM
that could obtain 100% validation accuracy. After training, we per-
formed testing with a new dataset of 10 min long. The results showed
that the algorithm with the extracted features can eliminate low-quality
signals. The results of the testing with 10 healthy individuals are given in
Table 1. For the laboratory data, we have the reference device. Hence,
we can compare the proposed method results with the reference results
in terms of evaluation accuracy according to Eq. (11). The results are
from 93.2% to 100%, as shown in Table 1, where Ncor is the number of
| samples with the correct decision and Ntotal  |     | is the total number of  |     |     |     |     |
| --------------------------------------------- | --- | ----------------------- | --- | --- | --- | --- |
samples.
N
Acc= cor.100%
(11)
N total
After being classified into a group of high-quality signals, the signals
were sent to the vital sign extraction. As for the breath rate, in our
previous article, we have confirmed that radar measurement results in a  Fig. 7. Signal segment with the RR correspondence of the reference and pro-
| peak of the breathing rate cause a peak in the radar signal. Therefore, in  |     |     | posed method.  |     |     |     |
| --------------------------------------------------------------------------- | --- | --- | -------------- | --- | --- | --- |
Table 1
Result of signal quality assessment, the measurement of 10 healthy subjects within 10 min, the length of each sample is 10.24 s (1024 sampling points at 100 Hz).
Subject  Number of  Reference  Proposed method  Number of wrong  Accuracy
| samples        |                         |                        |                         |                        | decisions  | (%)    |
| -------------- | ----------------------- | ---------------------- | ----------------------- | ---------------------- | ---------- | ------ |
|                | Number of high-quality  | Number of low-quality  | Number of high-quality  | Number of low-quality  |            |        |
|                | samples                 | samples                | samples                 | samples                |            |        |
| Subject 1  59  | 49                      | 10                     | 48                      | 11                     | 1          | 98.3   |
| Subject 2  59  | 51                      | 8                      | 51                      | 8                      | 0          | 100    |
| Subject 3  59  | 39                      | 20                     | 35                      | 24                     | 4          | 93.2   |
| Subject 4  59  | 45                      | 14                     | 45                      | 14                     | 0          | 100    |
| Subject 5  59  | 42                      | 17                     | 40                      | 19                     | 4          | 93.2   |
| Subject 6  59  | 53                      | 6                      | 53                      | 6                      | 0          | 100    |
| Subject 7  59  | 48                      | 11                     | 48                      | 11                     | 2          | 96.6   |
| Subject 8  59  | 54                      | 5                      | 54                      | 5                      | 2          | 96.6   |
| Subject 9  59  | 52                      | 7                      | 53                      | 6                      | 1          | 98.3   |
| Subject10  59  | 45                      | 14                     | 45                      | 14                     | 2          | 96.6   |
6

H.T. Yen et al. B i o m e d i c a l S i g n a l P r o c e s s i n g a n d C o n t r ol75(2022)103597
Table 2 higher order. Using SVD is essentially separate heart rate frequency.
Result of RR extraction compare with the reference signals, the measurement of Therefore, the peaks of the signal after processing using SVD have
10 healthy subjects with 5 min high-quality signal. clearer and more accurate. The results of extracting HR of 10 healthy
Subject Method Respiration Rate (bpm) individuals in 5 min high-quality signals are shown in Table 3.
From Table 3, we can see that the difference in HR between the
Minute Minute Minute Minute Minute
1 2 3 4 5 reference and proposed method ranges from 0 to 7 bpm. Only 2 min out
of the total 50 min of survey is 7 bpm, and the difference is mainly from
Subject Resp 15 16 15 18 15
0 to 4 bpm (38 of 50 min), especially bias from 0 to 1 bpm with 22 of 50
1 (Reference)
Radar 15 16 15 17 16 min, as shown in Fig. 10a. The scatter plot and correlation between HR
(proposed) measured by ECG (reference) and HR by proposed method are given in
Subject Resp 15 17 15 12 15 Fig. 10b. With this result, it proves that the proposed method is effective
2 (Reference)
to detect vital signs. However, it should be emphasized that, the accu-
Radar 16 17 15 12 14
(proposed) racy of the signal quality assessment is very important, it determines the
Subject Resp 18 15 15 14 15 accuracy of the vital sign detection stage. If at stage 1, signal quality is
3 (Reference) misclassified, then breathing rate and heart rate are also wrong, leading
Radar 15 16 14 14 15 to incorrect diagnosis of disease.
(proposed)
Subject Resp 17 18 18 16 16
4 (Reference)
3.2. Signal quality assessment and vital sign extraction for clinical data
Radar 18 18 18 16 17
(proposed)
Subject Resp 16 15 16 14 16 In this subsection, we illustrate the use of the proposed system in
5 (Reference) clinical applications. For signal quality classification, we performed
Radar 15 15 15 15 15
signal classification on a dataset received from the hospital. The dataset
(proposed)
Subject Resp 12 12 13 12 13 contains measurement data of the elderly. By observing and labeling 250
6 (Reference) samples of bad quality and 250 samples of good quality from measure-
Radar 12 13 12 13 12 ment files (2 h data), 1024 sampling points for one sample, we per-
(proposed)
formed training with a K-fold of 5. That is, 500 signal samples were
Subject Resp 17 18 18 18 17
divided into two parts: 400 training samples and 100 testing samples.
7 (Reference)
Radar 18 18 18 18 18 The procedure was repeated five times with a variable test set. The re-
(proposed) sults show that the data was classified with a validation accuracy of
Subject Resp 20 22 20 20 19 99.1% for the training model using SVM, with the notice that the
8 (Reference)
training data was not included in the testing data. The training dataset
Radar 21 22 20 19 20
(proposed) also was trained with different Machine Learning algorithms, the results
Subject Resp 15 15 15 16 15 for Tree Decision, Logistic Regression and Fine KNN were 98.2%, 94.5%
9 (Reference) and 95.5%, respectively. This proves that the extracted features are
Radar 15 15 15 15 13
more suitable for the SVM model.
(proposed)
After training, we applied the model to assess the signals of two
Subject Resp 14 14 14 15 14
10 (Reference) patients. Two patients had data of 7 days and 24 h (24 measurement
Radar 15 12 13 14 14 data files) per day. The results of one-hour data testing of Patient 1 are
(proposed) plotted in Fig. 11. By such signal quality classification, the sleep quality
of the elderly is evaluated when the classification is performed on the set
of data collected during night sleep hours. It must be emphasized that
inferences about sleep quality as measured by the ratio of low-quality
signal to total signal length are made when the signal is not affected
Fig. 8. The result of RR detection: a) Histogram of the RR difference between the reference and proposed methods; b) Scatter plot with correlation between RR by
reference and RR by proposed method.
7

H.T. Yen et al. B i o m e d i c a l S i g n a l P r o c e s s i n g a n d C o n t r ol75(2022)103597
Fig. 9. Segment of the signal after extracting heartbeat.
by surrounding activities such as the arrival of doctors and nurses.
Table 3
Specifically, Fig. 11 shows that in one-hour signal, there is 32.66% low-
Result of HR extraction compare with the reference signals, the measurement of
quality signal. If in this one hour, all low-quality signal is due to
10 healthy subjects with 5 min high-quality signal.
movement of the patient, we can conclude that patient’s movement rate
Subject Method Heart Rate (bpm) in one hour is 32.66 %. However, if the T* interval is due to the nurse
Minute Minute Minute Minute Minute going to the patient’s bed to check patient at night. In this case, if we
1 2 3 4 5 take the percentage 32.66% to evaluate the patient’s movement rate in
Subject ECG 62 61 62 62 60 one hour, it will be incorrect. The time interval T* is 164 s (16 samples).
1 (Reference) Therefore, to be precise, in one-hour, low-quality signal rate is 32.66%
Radar 68 68 61 63 59 including the patient’s movement rate of 27.92 %.
(proposed)
After being classified into the high-quality signal group, the RR and
Subject ECG 57 57 58 56 58
2 (Reference) the HR were extracted. We intensively analyzed the RR and HR of the
Radar 56 57 58 55 57 two patients in the time period, including the risk of Cheyne-Stokes
(proposed) respiration (CSR) and sleep apnea. We focused on assessing the abnor-
Subject ECG 67 63 57 56 55
mality of the RR and HR in 7 days of Patient 1 from January 5 (2017) to
3 (Reference)
January 11 (2017) and Patient 2 from January 17 (2020) to January 23
Radar 60 59 62 55 57
(proposed) (2020).
Subject ECG 62 63 63 62 63 Each day, the RR and HR of the patients were calculated 24 times (24
4 (Reference) h) from high-quality radar signals. The RR and the HR for each day are
Radar 62 63 59 58 60
plotted in a box chart in Fig. 12. As can be observed, for patient 1, from
(proposed)
Subject ECG 60 62 60 62 60 January 5 to January 8, the RR and the HR linearly increased, and the
5 (Reference) mean HR reached a peak on January 8. Owing to this abnormality, it was
Radar 63 55 65 60 55 desirable to examine the raw signal more closely before and after
(proposed)
January 8. As an alert, the raw signal from the radar on January 8 was
Subject ECG 60 64 61 62 63
distinctive, the respiratory amplitude changed, and the patient was
6 (Reference)
Radar 58 61 65 62 61 diagnosed with CSR. Meanwhile, before CSR pathogenesis, the raw
(proposed) signal from the radar has a stable amplitude, as shown in Fig. 13.
Subject ECG 58 59 59 58 57 For Patient 2, the mean HR and the absolute HR showed an abnormal
7 (Reference)
increase on January 19. At 11 am on January 19, the heart rate suddenly
Radar 58 59 60 62 57
(proposed) increased to 85 bpm, whereas the mean HR of this patient was
Subject ECG 58 60 58 61 59 approximately 60 bpm. Upon close examination of the raw data, we
8 (Reference) found that the patient stopped breathing 15 times per hour. The longest
Radar 58 55 54 67 64
duration of apnea was 66 s (from 2505 s to 2571 s), as shown in Fig. 14.
(proposed)
The patient was alerted that apnea occurred, and the breathing rate
Subject ECG 54 54 52 50 49
9 (Reference) increased after apnea occurred. In the following days, medical inter-
Radar 53 54 54 49 53 vention was needed for the signs of the disease to achieve remission.
(proposed) About sleep apnea, as we know, when stop breathing, heart rate also
Subject ECG 82 83 82 87 82
tends to drop that make the body is deprived of oxygen. Then, invol-
10 (Reference)
Radar 76 77 81 86 82 untary reflexes cause awake at the end of that period of stop breathing.
(proposed) When this occurs, heart rate tends to accelerate quickly and blood
pressure goes up [30,31]. Our paper also gave a result of heart rate in-
crease when sleep apnea occur.
In addition, every day the nurses in hospital would check the heart
rate and temperature of the patients 3 times per day. The results of
8

H.T. Yen et al. B i o m e d i c a l S i g n a l P r o c e s s i n g a n d C o n t r ol75(2022)103597
Fig. 10. a) The result of HR detection: Histogram of the HR difference between ECG and proposed methods; b) Scatterplot with correlation between HR by ECG and
HR by proposed method.
Fig. 11. Example of the signal quality classification result with one-hour measurement of inpatient in Yokohama Hospital, Japan.
nurses’ daily check recorded an increase in abnormal heart rate on of the algorithm with different sample lengths, and the decision in the
January 7 and January 8, 2017 for patients with CSR and on January 19, paper was an optimal trade-off for accuracy and sample length. Heart
2020 for patients with sleep apnea syndrome, which made a consistency beat detection with 512 sampling points was suitable for SVM with 1024
with our results. sampling points because two computation times of the second stage
would complete for one sample of the first stage.
4. Discussion and conclusion It is important to monitor the RR and the HR to give an alert when
there is an abnormality. Moreover, this monitoring is non-contact,
In this paper, we presented a two-stage system, as shown in Fig. 15. making it suitable for inpatients because they have to be in the hospi-
The first stage was the evaluation of the radar signal quality. The second tal for a long time. In addition, in the period when Covid-19 is still
stage was to monitor RR and HR to detect abnormalities in patients. spreading strongly, the urgency of using non-contact devices is even
We evaluated the accuracy of the algorithm by processing data higher. It would be great if we could have contactless patient moni-
collected from healthy individuals in our laboratory. The evaluation on toring, which could replace the daily RR and HR measurements of nurses
healthy individuals signal showed the quite high accuracy. During in the hospital. Previous studies have focused on detecting vital signs
measurements, we did not need to wait until the subject was completely based on high-quality signals in the laboratory. However, in real ap-
motionless. Instead, we recorded data intervals in which the measured plications, the signal measured in the hospital is not as stable as in the
person had random body movements. The signal containing the body laboratory but includes random body movements. Therefore, high-
movements was then discarded, and the high-quality signal was retained quality signal separation before vital sign extraction is essential. The
to extract the RR and the HR. This study also investigated the accuracy results of RR and HR analysis of the two patients showed that, when
9

H.T. Yen et al. B i o m e d i c a l S i g n a l P r o c e s s i n g a n d C o n t r ol75(2022)103597
Fig. 12. Trend of 24 h RR and HR for two patients diagnosed with CSR (a) and sleep apnea (b).
Fig. 13. Respiratory amplitude of Patient 1 during CSR (a) and before CSR pathogenesis (b).
Fig. 14. Segment of stop-breathing signal from Patient 2 with sleep apnea.
patients have CSR, the RR and HR increase significantly. Meanwhile, assessment, if the low-quality signal cannot be eliminated, the accuracy
patients with sleep apnea often stop breathing, the HR increases, and the of the vital sign detection will be greatly reduced. On the other hand, the
RR tends to increase after each apnea. extracted features in this paper mainly carry information of breathing
There are some problems that we should discuss more after doing the rate rather than heart rate, so our next plan is to continue improving the
research. On the one hand, the peak detection of the vital signs requires quality of the classification system based on the information of heart rate
a high-quality signal, so this stage will be very dependent on the first shown on radar signal. In addition, the system calculated only HR, that
step which is the signal quality classification. In the step of signal quality is, the total beats in each minute, not yet calculated HRV. Furthermore,
10

H.T. Yen et al. B i o m e d i c a l S i g n a l P r o c e s s i n g a n d C o n t r ol75(2022)103597
Fig. 15. Block diagram of signal processing: a) Signal quality assessment. b) Vital signs extraction.
the system includes many steps so consists of many calculations. How- related to the intensity of constant work rate exercise in copd, Chest 128 (2) (2005)
ever, in this study, the authors have focused on omitting the signal with
651–656.
[6] P. Gagnon, J.S. Bussi`eres, F. Ribeiro, S.L. Gagnon, D. Saey, N. Gagn´e,
low quality and found out the vital signs for clinical signals, has not S. Provencher, F. Maltais, Influences of spinal anesthesia on exercise tolerance in
taken account the complexity of the algorithm. Therefore, it is necessary patients with chronic obstructive pulmonary disease, Am. J. Respir. Crit. Care Med.
for the next plan to evaluate the computational cost, thereby reducing 186 (7) (2012) 606–615.
[7] C.C. Johnson, A.W. Guy, Nonionizing electromagnetic wave effects in biological
the complexity of the system to implement the algorithm on real devices materials and systems, Proc. IEEE 60 (6) (1972) 692–718.
using in hospitals. [8] J.Y. Lee, J.C. Lin, A microcprocessor-based noninvasive arterial pulse wave
In conclusion, the novelty of the proposed system is quality classi- analyzer, IEEE Trans. Biomed. Eng. BME-32 (6) (1985) 451–455.
[9] G. Sun, S. Gotoh, Z. Zhao, S. Kim, S. Suzuki, N. Imamoglu, W. Yu, T. Matsui, Vital-
fication of radar signals based on the feature differences between signals
cube: A non-contact vital sign monitoring system using medical radar for
with and without body random movements and extraction of RR and HR ubiquitous home healthcare, J. Med. Imag. Health Inf. 4 (6) (2014) 863–867.
with clear peaks. This study has the potential in the complicated Covid- [10] G. Sun, T. Matsui, Y. Watai, S. Kim, T. Kirimoto, S. Suzuki, Y. Hakozaki, Vital-
scope: design and evaluation of a smart vital sign monitor for simultaneous
19 situation to non-contact monitor inpatients with CSR and sleep apnea
measurement of pulse rate, respiratory rate, and body temperature for patient
through the detection of abnormalities in 24 h RR and HR trends. monitoring, J. Sens. 2018 (2018) 1–7.
[11] S. Kang, Y. Lee, Y.-H. Lim, H.-K. Park, S.H. Cho, S.H. Cho, Validation of noncontact
cardiorespiratory monitoring using impulse-radio ultra-wideband radar against
CRediT authorship contribution statement
nocturnal polysomnography, Sleep Breath 24 (3) (2020) 841–848.
[12] H. Tang, M. Wang, Y. Hu, B. Guo, T. Li, P. Zhou, Automated signal quality
Hoang Thi Yen: Data curation, Formal analysis, Investigation, assessment for heart sound signal by novel features and evaluation in open public
Methodology, Software, Validation, Visualization, Writing – original datasets, Biomed. Res. Int. 2021 (2021) 1–15.
[13] K. Shi, S. Schellenberger, F. Michler, T. Steigleder, A. Malessa, F. Lurz, C. Ostgathe,
draft, Conceptualization. Masaki Kurosawa: Conceptualization. Tet- R. Weigel, A. Koelpin, Automatic signal quality index determination of radar-
suo Kirimoto: Conceptualization. Yukiya Hakozaki: Conceptualiza- recorded heart sound signals using ensemble classification”, IEEE Trans. Biomed.
tion. Takemi Matsui: Conceptualization. Guanghao Sun: Funding Eng. 67 (3) (2020) 773–785.
[14] Y. Lee, J.W. Choi, S.H. Cho, Vital sign quality assessment based on ir-uwb radar
acquisition, Project administration, Resources, Supervision, Writing –
sensor, in: 2017 International Conference on Information and Communication
review & editing, Conceptualization. Technology Convergence (ICTC), 2017, pp. 896–900.
[15] J.-Y. Park, Y. Lee, Y.-W. Choi, R. Heo, H.-K. Park, S.-H. Cho, S.H. Cho, Y.-H. Lim,
Preclinical evaluation of a noncontact simultaneous monitoring method for
Declaration of Competing Interest
respiration and carotid pulsation using impulse-radio ultra-wideband radar, Sci.
Rep. 9 (1) (2019) 1–12.
The authors declare that they have no known competing financial [16] J.-Y. Kim, J.-H. Park, S.-Y. Jang, J.-R. Yang, Peak detection algorithm for vital sign
detection using doppler radar sensors, Sensors 19 (7) (2019) 1575.
interests or personal relationships that could have appeared to influence [17] N. Maleˇsevi´c, V. Petrovi´c, M. Beli´c, C. Antfolk, V. Mihajlovi´c, M. Jankovi´c,
the work reported in this paper. Contactless real-time heartbeat detection via 24 ghz continuous-wave doppler
radar using artificial neural networks, Sensors 20 (8) (2020) 2351.
[18] W.-K. Liu, H.-P. Fu, Z.-K. Yang, A doppler radar vital sign detection system using
References
concurrent dual-band hybrid down conversion architecture, IEICE Electronics
Express 190 (665) (2019) 16–20.
[1] A. Coca, R.J. Roberge, W.J. Williams, D.P. Landsittel, J.B. Powell, A. Palmiero, [19] Y. Xu, Q. Li, Z. Tang, Accurate and contactless vital sign detection in short time
Physiological monitoring in firefighter ensembles: Wearable plethysmographic window with 24 ghz doppler radar, J. Sens. 2021 (2021).
sensor vest versus standard equipment, J. Occupational Environ. Hygiene 7 (2) [20] G. Sun, M. Okada, R. Nakamura, T. Matsuo, T. Kirimoto, Y. Hakozaki, T. Matsui,
(2009) 109–114. Twenty-four-hour continuous and remote monitoring of respiratory rate using a
[2] R. Paradiso, T. Faetti, S. Werner, Wearable monitoring systems for psychological medical radar system for the early detection of pneumonia in symptomatic elderly
and physiological state assessment in a naturalistic environment, in: 2011 Annual bedridden hospitalized patients, Clin. Case Rep. 7 (1) (2019) 83–86.
International Conference of the IEEE Engineering in Medicine and Biology Society, [21] K. Edanami, Y. Yao, H. T. Yen, M. Kurosawa, T. Kirimoto, Y. Hakozaki, T. Matsui,
IEEE, 2011, pp. 2250–2253. and G. Sun, Design and evaluation of digital filters for non-contact measuring of
[3] T.J. Hodgetts, G. Kenward, I.G. Vlachonikolis, S. Payne, N. Castle, The hrv using medical radar and its application in bedside patient monitoring system,
identification of risk factors for cardiac arrest and formulation of activation criteria in: 2021 43rd Annual International Conference of the IEEE Engineering in
to alert a medical emergency team, Resuscitation 54 (2) (2002) 125–131. Medicine & Biology Society (EMBC), IEEE, 2021, pp. 6962–6965.
[4] W. H. Organization, et al., Health topics: cardiovascular disease, Fact Sheet. [22] Y. Otake, T. Kobayashi, Y. Hakozaki, and T. Matsui, Non-contact heart rate
Available online: http://www.who.int/cardiovascular_diseases/en/ (accessed on variability monitoring using doppler radars located beneath bed mattress: a case
11 December 2020), 2019. report, Eur. Heart J.-Case Rep. 5(8) (2021) ytab273.
[5] L. Puente-Maestu, J.G. de Pedro, Y. Martínez-Abad, J.M.R. de On˜a, D. Llorente, J.
M. Cubillo, Dyspnea, entilatory pattern, and changes in dynamic hyperinflation
11

H.T. Yen et al. B i o m e d i c a l S i g n a l P r o c e s s i n g a n d C o n t r ol75(2022)103597
[23] H. T. Yen, M. Kurosawa, T. Kirimoto, K. Edanami, and G. Sun, Proof-of-principle [27] D.A. Pisner, D.M. Schnyer, “Support vector machine”, in Machine Learning, Elsevier
experiment on 24 ghz medical radar for non-contact vital signs measurement, in: (2020) 101–121.
2021 43rd Annual International Conference of the IEEE Engineering in Medicine [28] W.S. Noble, What is a support vector machine? Nat. Biotechnol. 24 (12) (2006)
Biology Society (EMBC), 2021, pp. 6884–6884. 1565–1567.
[24] A. De Groote, M. Wantier, G. Ch´eron, M. Estenne, M. Paiva, Chest wall motion [29] X. Zhao, B. Ye, Separation of single frequency component using singular value
during tidal breathing, J. Appl. Physiol. 83 (5) (1997) 1531–1537. decomposition, Circuits Syst. Signal Process. 38 (1) (2019) 191–217.
[25] D. Wang, S. Yoo, S.H. Cho, Experimental comparison of ir-uwb radar and fmcw [30] S.M. Series, Obstructive sleep apnea and heart disease, Am. J. Respir. Crit. Care
radar for vital signs, Sensors 20 (22) (2020) 6695. Med. 188 (2013) P1–P2.
[26] Y. Xiao, J. Lin, O. Boric-Lubecke, M. Lubecke, Frequency-tuning technique for [31] N. Vitulano, A. Di Marco Berardino, A. Re, G. Riccioni, F. Perna, F. Mormile, S.
remote detection of heartbeat and respiration using lowpower double-sideband Valente, and F. Bellocci, Obstructive sleep apnea and heart disease: the biomarkers
transmission in the ka-band, IEEE Trans. Microw. Theory Tech. 54 (5) (2006) point of view, Front. Biosci. (Scholar edition) 5 (2013) 588–599.
2023–2032.
12