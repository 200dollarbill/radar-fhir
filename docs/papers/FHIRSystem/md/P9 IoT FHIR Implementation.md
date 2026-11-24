Article
HL7 FHIR-Based Open-Source Framework for Real-Time
Biomedical Signal Acquisition and IoMT Interoperability

Felix-Constantin Adochiei 1,2,3
George Serit,an 1

and Gladiola-Gabriela Petroiu 5,*

, Florian-Alexandru T, oi 1, Ioana-Raluca Adochiei 2,3,4

, Florin Ciprian Argatu 1

,

1 Department of Measurements, Electrical Apparatus, and Static Converters (DMAECS), National University of
Science and Technology POLITEHNICA Bucharest, 313 Splaiul Independentei, District 6, 060042 Bucharest,
Romania; felix.adochiei@upb.ro (F.-C.A.); florian.toi@stud.fim.upb.ro (F.-A.T, .); florin.argatu@upb.ro (F.C.A.);
george.seritan@upb.ro (G.S.)

2 Academy of Romanian Scientists, Ilfov 3, 050044 Bucharest, Romania; ioana.adochiei@mta.ro
3

Emil Palade Center of Excellence for Young Researchers, Academy of Romanian Scientists, Ilfov 3,
050044 Bucharest, Romania

4 Department of Integrated Aviation Systems and Mechanics, Military Technical Academy “Ferdinand I”, 39–49

5

George Cos, buc Blvd., District 5, 050141 Bucharest, Romania
Faculty of Medical Bioengineering, Grigore T. Popa University of Medicine and Pharmacy of Ias, i, 9-13
Kogalniceanu Str., 700454 Ias, i, Romania
* Correspondence: gladiola.petroiu@umfiasi.ro

Abstract

This study presents the design and validation of an open-source framework for biomedical
signal acquisition and interoperable data exchange based on the Health Level Seven—Fast
Healthcare Interoperability Resources (HL7 FHIR) standard. The proposed system enables
secure, wireless transmission of physiological data from distributed sensing nodes toward a
locally hosted monitoring platform. The hardware architecture integrates ESP32-WROOM-
32 microcontrollers for multi-parameter acquisition, the MQTT protocol for low-latency
communication, and a Home Assistant (Nabu Casa, San Diego, CA, USA)–InfluxDB (In-
fluxData, San Francisco, CA, USA)–Grafana (Grafana Labs, New York, NY, USA) stack
for real-time visualization. The novelty of this work lies in the full-stack implementation
of HL7 FHIR Observations within a reproducible, open-source environment, ensuring
semantic interoperability without reliance on proprietary middleware or cloud services. A
case study involving multi-sensor acquisition of electrocardiographic (ECG), photoplethys-
mographic (PPG), temperature, and oxygen saturation signals was conducted to evaluate
system performance. Validation results confirmed consistent end-to-end data flow, sub-
second latency, zero packet loss, and accurate semantic preservation across all processing
stages. These findings demonstrate the feasibility of implementing standardized, open,
and scalable biomedical Internet of Medical Things (IoMT) systems using non-proprietary
components. The proposed framework provides a reproducible foundation for future
telemedicine and continuous patient-monitoring applications, aligning with FAIR data
principles and the ongoing digital transformation of healthcare.

Keywords: HL7 FHIR; interoperability; internet of medical things (IoMT); biomedical
signal acquisition; ESP32; MQTT; open-source framework; home assistant; InfluxDB;
Grafana; telemedicine

Academic Editor: Jesús

B. Alonso-Hernández

Received: 24 October 2025

Revised: 28 November 2025

Accepted: 29 November 2025

Published: 3 December 2025

Citation: Adochiei, F.-C.; T, oi, F.-A.;

Adochiei, I.-R.; Argatu, F.C.; Serit,an,

G.; Petroiu, G.-G. HL7 FHIR-Based

Open-Source Framework for

Real-Time Biomedical Signal

Acquisition and IoMT Interoperability.

Appl. Sci. 2025, 15, 12803. https://

doi.org/10.3390/app152312803

Correction Statement: This article has

been republished with a minor change.

The change does not affect the scientific

content of the article and further details

are available within the backmatter of

the website version of this article.

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Appl. Sci. 2025, 15, 12803

https://doi.org/10.3390/app152312803

Appl. Sci. 2025, 15, 12803

2 of 19

1. Introduction

The increasing digitalization of healthcare systems has led to exponential growth in
the volume and complexity of biomedical data, underscoring the need for interoperability
among heterogeneous medical devices and software platforms [1,2]. Modern hospital
infrastructure integrates equipment from multiple vendors, each with proprietary data
formats and communication protocols. This lack of interoperability can hinder clinical
decision-making, especially in time-critical scenarios.

Health Level Seven (HL7) standards provide a well-established framework for the
structured exchange of medical information between electronic systems [3,4]. The tran-
sition from the traditional HL7 v2.x architecture to the Fast Healthcare Interoperability
Resources (FHIR) model introduces a RESTful, web-based approach supporting modern
data formats such as JSON and XML [5]. FHIR’s RESTful design and modular resources
have been extensively analyzed by Bender and Sartipi [6], confirming its suitability for
lightweight interoperability. FHIR enables flexible, scalable communication between de-
vices and healthcare information systems, facilitating seamless integration of physiological
monitoring data, laboratory results, and patient records [7]. Expanded technical documen-
tation on developer-oriented FHIR implementation is provided in Grieve’s foundational
work [8]. This standard also enables semantic interoperability, allowing different systems
to interpret biomedical information consistently and independently of vendor-specific
implementations. Semantic harmonization across heterogeneous systems has been a cen-
tral objective in modern health informatics [9]. Broader methodological perspectives on
semantic interoperability have been synthesized in recent reviews [10].

Recent advances in the Internet of Medical Things (IoMT) have further expanded
this vision by connecting sensors, edge devices, and cloud infrastructure to enable contin-
uous acquisition and analysis of physiological parameters [11,12]. The multilayer IoMT
architecture—comprising perception, network, and application layers—has been systemati-
cally defined in several high-impact surveys [13]. Additional systematic reviews highlight
the rapid expansion of IoMT architectures and their clinical applicability [14].

Within IoMT architectures, the perception layer captures raw biomedical signals, the
network layer ensures wireless communication via Wi-Fi, Bluetooth Low Energy (BLE), or
ZigBee, and the application layer manages storage, visualization, and analytics through
databases and artificial intelligence methods [15,16]. Such integration aligns with the FAIR
(Findable, Accessible, Interoperable, Reusable) principles outlined in Wilkinson et al. [17],
which emphasize semantic interoperability and structured metadata across biomedical
data ecosystems. These requirements have been clarified in recent analyses of FAIR im-
plementation pathways [18]. Moreover, the growing demand for remote monitoring and
telemedicine—accelerated by the post-pandemic digitalization of healthcare—underscores
the need for open, interoperable biomedical data frameworks.

Several case studies have explored IoMT-based acquisition platforms for specific phys-
iological parameters, particularly blood pressure estimation from PPG signals [19] and
secure telemetry pipelines for biomedical monitoring [20]; FAIR-aligned data-management
frameworks relevant to interoperable medical ecosystems are discussed in [17]. MQTT-
based secure telemetry systems for real-time biomedical monitoring have been explored
in recent implementations. However, most of these implementations rely on proprietary
middleware or commercial cloud infrastructures, which hinder reproducibility and cost-
effective deployment. The present case study was therefore selected to demonstrate
that a fully open-source stack, built entirely from off-the-shelf components, can achieve
comparable real-time performance and semantic interoperability without dependence on
closed ecosystems.

Appl. Sci. 2025, 15, 12803

3 of 19

Despite these technological advances, most hospital networks still rely on wired con-
nections and proprietary middleware, which limits scalability and reproducibility [21].
Existing implementations of IoMT-based acquisition systems using MQTT transport and
HL7 FHIR encoding have been documented in several interoperability-focused stud-
ies [7,11,12,15], highlighting both architectural patterns and integration constraints across
heterogeneous healthcare infrastructures. Such limitations restrict flexibility, interoperabil-
ity, and validation across diverse environments.

The present study addresses these challenges by designing and validating a low-
cost, fully open-source biomedical data-acquisition system compliant with the HL7 FHIR
standards [22]. The proposed solution enables secure, wireless transmission of physiolog-
ical data, full semantic interoperability, and real-time visualization within a distributed
monitoring framework [23,24]. The ESP32 microcontroller was selected for its dual-core
architecture, integrated Wi-Fi and Bluetooth connectivity, and widespread adoption in
biomedical and educational research, providing a cost-effective and flexible foundation
for IoMT prototyping. Its originality lies in implementing a complete end-to-end data
integration chain—from sensor acquisition to open-source visualization—based entirely on
standardized protocols and open technologies [25].

In comparison with widely adopted interoperability frameworks—SMART on
FHIR [7], HAPI FHIR servers [26], and Open mHealth ecosystems [27]—the present work
provides an entirely on-premise, MQTT-based implementation that achieves real-time
acquisition and HL7 FHIR-compliant encoding using only open-source components. Prac-
tical deployment considerations for HAPI FHIR servers have been reported in large-scale
clinical integration studies [28]. Recent mobile health applications illustrate hybrid Open
mHealth–FHIR pipelines for distributed sensing [29].

Unlike these frameworks, which typically rely on cloud services or heavyweight
middleware, the proposed architecture emphasizes local deployment, lightweight transport,
and reproducibility for laboratory-scale IoMT prototyping. This comparative positioning
clarifies the contribution of the present framework relative to existing SMART-on-FHIR,
HAPI FHIR, and Open mHealth pipelines.

The main contributions of this study are: (1) the development of a dual-node biomedi-
cal data acquisition system using HL7 FHIR; (2) its integration within an open-source IoT
environment for end-to-end interoperability; and (3) validation of real-time data flow with
sub-second latency.

This paper is organized as follows: Section 2 presents the system architecture and
implementation details; Section 3 describes the case study and validation results; Section 4
discusses the system-level implications; and Section 5 concludes with perspectives for
future research.

2. Materials and Methods
2.1. System Architecture

The proposed system was designed as an integrated hardware–software framework
for real-time biomedical signal acquisition and wireless data transfer, fully compliant with
HL7 FHIR communication standards. Its architecture (Figure 1) consists of three functional
layers: acquisition, communication, and visualization.

At the acquisition level, an ESP32-WROOM-32 microcontroller (Espressif Systems,
Shanghai, China) was selected due to its dual-core architecture, embedded Wi-Fi/BLE
interfaces, and compatibility with open-source firmware development environments [16].
The device operates as a local gateway, decoding physiological data from connected medical
modules and converting them into standardized HL7 FHIR “Observation” resources.

Appl. Sci. 2025, 15, 12803

4 of 19

Figure 1. Architecture of the system for HL7 FHIR file reception, decoding, and transmission across
the acquisition, communication, and visualization layers.

The communication layer relies on the MQTT protocol for low-latency telemetry
and lightweight message transport, using a Mosquitto MQTT Broker (Eclipse Founda-
tion, Ottawa, ON, Canada) configured with TLS encryption and credential-based authen-
tication [25]. Authentication is achieved through username–password credentials and
TLS-based encryption, ensuring secure interoperability among system components [12].

At the visualization layer, time-series data are stored in InfluxDB and rendered through
Grafana dashboards, providing high-resolution monitoring and advanced analytical capa-
bilities for real-time physiological tracking [15,30].

The overall data flow—from sensor acquisition through MQTT transmission to
database storage and visualization—is illustrated in Figure 1, which presents a three-
layer architecture connecting the biomedical acquisition front-end to the open-source
analytics environment.

2.2. HL7 FHIR Data Structure and Processing

The transmitted data follow the FHIR Observation resource model, selected for its
structured representation of physiological signals and compatibility with RESTful com-
munication. Each Observation entity includes metadata such as patient identifiers, device
references, acquisition timestamps, and structured waveform descriptors, in accordance
with the official HL7 FHIR specification [31].

For electrocardiographic (ECG) monitoring, the valueSampledData element was
used to encode waveform samples as JSON numerical sequences, along with attributes
such as the sampling period, scaling factor, and physical units. The following con-
version formula was applied for transforming raw integer values into corresponding
physiological quantities:

VECG = (Vraw − Voffset) × Fscale

where Vraw represents the digitized input value, Voffset the reference origin, and Fscale the
conversion factor specified in the HL7 resource structure. In our AD8232 configuration,
Voffset = 2048 (12-bit ADC midpoint), Fscale = 0.00047 mV/LSB, corresponding to the AD8232
ECG analog front-end (Analog Devices, Wilmington, MA, USA) gain of 110 and the ESP32
ADC reference of 3.3 V.

This approach ensures compatibility with standards-compliant monitoring systems. It
enables future integration of multiple physiological parameters—such as oxygen saturation,
respiratory rate, or body temperature—using the same FHIR data schema.

The electrode placement used for single-lead ECG acquisition is illustrated in
Figure 2, corresponding to a standard Lead II configuration commonly adopted in low-cost
wearable systems.

 Appl. Sci. 2025, 15, 12803

5 of 19

Figure 2. Electrode placement configuration for Lead II ECG acquisition. Color coding: red—right
arm (RA); yellow—left arm (LA); green—left leg (LL) reference electrode.

The signal acquisition and message-generation processes were mapped into a logical
workflow in which raw analog data are converted into HL7 FHIR Observations and
transmitted to the integration platform. This logical flow will be detailed in the case
study section (Figures 3 and 4).

Figure 3. Vital-sign acquisition and monitoring module, illustrating the main sensing and processing
blocks (ESP-wroom-32).

Figure 4. Assembled hardware for the vital-sign acquisition and monitoring module.

   Appl. Sci. 2025, 15, 12803

6 of 19

A representative HL7 FHIR Observation JSON excerpt, illustrating the encoding of
waveform and scalar elements in the valueSampledData structure and the use of standard-
ized UCUM units, is provided in the Supplementary Materials to support reproducibility.
ECG signals were mapped to waveform categories defined in IEEE 11073-10101-2004 [32],
the reference standard that formalizes nomenclature for physiological waveforms and
underpins the mapping used in FHIR Waveform profiles.

The implemented acquisition and monitoring module is shown in Figure 3, which

presents the logical structure of the multi-sensor front-end.

The assembled hardware implementation is shown in Figure 4, corresponding to the

prototype used in validation.

2.3. Software Implementation

The system firmware was developed using MicroPython v1.20.0 (MicroPython Foun-
dation, Cambridge, UK) and deployed through the Thonny IDE v4.1.2 (University of
Tartu, Tartu, Estonia). The data-publishing process was managed through a Python-based
interface implemented in the Spyder IDE v5.5.1 (Spyder Project/Quansight, Austin, TX,
USA), which serializes and transmits selected FHIR files via MQTT to the ESP32 node.
Upon receiving the message, the microcontroller decodes the JSON payload, extracts
the signal parameters, and repackages the processed data for transmission to the Home
Assistant server.

The ESP32 node runs MicroPython firmware supporting wireless connectivity and
local JSON parsing, while the middleware stack—comprising Mosquitto, Home Assistant,
InfluxDB, and Grafana—handles message routing, persistence, and visualization. The
containerized setup in VMware (VMware Inc., Palo Alto, CA, USA) ensures reproducibility
and isolation during experimental validation.

2.4. Data Security and Interoperability

To ensure compliance with healthcare data protection requirements, several security
mechanisms were implemented: TLS encryption for all MQTT transactions; token-based
authentication between clients and the broker; and local data storage on the InfluxDB
server, minimizing external dependencies and ensuring GDPR compliance.

In this implementation, heart rate was encoded using LOINC 8867-4, oxygen saturation
using LOINC 59408-5, and temperature using LOINC 8310-5. UCUM units ‘%’, ‘degC’, and
‘ms’ were used accordingly. These standardized codes ensure semantic interoperability
with FHIR-compliant clinical systems.

Physiological measurements were transmitted as individual FHIR Observations at

each acquisition cycle; session-level Bundles were not generated in this prototype.

TLS 1.2 encryption and SHA-256-based authentication were configured within the

Mosquitto broker, ensuring the confidentiality and integrity of all transmitted payloads.

Furthermore, interoperability across hardware and software layers was validated by
maintaining the HL7 FHIR format end-to-end—from data generation at the acquisition
layer to visualization in Grafana—demonstrating that each component correctly preserved
data integrity, metadata, and temporal synchronization.

The validation also confirmed that HL7-compliant JSON structures remained seman-
tically intact after decoding, storage, and retrieval, ensuring full compliance with the
standard throughout the data path.

Additional security considerations are required to address the needs of biomedical
IoMT deployments fully. In accordance with best practices, the system shall explicitly
define its threat model, including potential adversarial actions such as eavesdropping,
message tampering, credential replay, and broker impersonation.

Appl. Sci. 2025, 15, 12803

7 of 19

Furthermore, MQTT topic-level Access Control Lists (ACLs), TLS cipher suite specifi-
cations, secure key provisioning methods, and certificate lifecycle management (issuance,
rotation, and revocation) should be formally documented. Mutual authentication mecha-
nisms and device-attestation strategies are recommended for clinical-grade environments.
A hybrid validation and security model for MQTT-based biomedical telemetry—
emphasizing device attestation, certificate rotation, and threat-mitigation strategies—has
been presented in [20]. This framework provides a relevant conceptual basis for improving
certificate lifecycle management and secure onboarding within clinical IoMT deployments.
These additions align the proposed architecture with contemporary cybersecurity
models in medical informatics, such as the hybrid validation framework, and strengthen
the system’s suitability for healthcare applications.

In this prototype, MQTT communication used TLS 1.2 with username/password
authentication, but did not implement mutual TLS or device attestation. Topic-level
ACLs were configured on the Mosquitto broker to restrict publish/subscribe privileges.
No identifiable patient data were transmitted, and all subjects were represented using
anonymised dummy identifiers.

A minimal security-hardening checklist, including TLS enforcement, credential ro-
tation, pseudonymisation rules, and broker-level ACL configuration, is provided in the
Supplementary Materials. Secure key provisioning and device-attestation mechanisms
were not implemented in this prototype and remain subjects for future extensions toward
clinical-grade deployments [33].

2.5. Validation Environment and Configuration

The validation process was conducted in a controlled environment simulating a real-
time patient-monitoring scenario. An HL7 FHIR “Observation” file containing three-lead
ECG data was selected as the test input. The system was deployed on a VMware virtual
machine running Home Assistant, InfluxDB, and Grafana.

Wireless communication between the acquisition node and the virtual server was
established via a local Wi-Fi network, with latency and data loss monitored across multiple
transfer cycles. The experiment confirmed stable communication and real-time visualiza-
tion of the ECG waveform with minimal delay.

To support reproducibility, key configuration snippets and MQTT connection pa-
rameters are summarized in the Supplementary Materials. Validation metrics—including
end-to-end latency, sampling-rate stability, and packet loss—were monitored across ten
acquisition sessions, as detailed in Section 3.4.

The detailed implementation of the acquisition hardware, firmware structure, and

experimental validation is presented in Section 3.

A public repository will be released in a future version; at this stage, only the
firmware structure and configuration parameters are provided to maintain prototype-
level reproducibility.

3. Case Study: Implementation and Validation
3.1. Experimental Setup

The experimental validation was performed on a multi-sensor module for vital-sign
monitoring centered on the ESP32-WROOM-32 development board, which managed HL7
FHIR message assembly, reception, decoding, and wireless transmission. The sensing front-
end integrated four biomedical transducers: AD8232 for electrocardiogram (ECG) signal
acquisition, GY-MAX30102 optical biosensor (Analog Devices/Maxim Integrated, San
Jose, CA, USA) for photoplethysmography (PPG), heart rate (HR), and oxygen saturation
(SpO2), and DHT11 temperature–humidity sensor (Aosong Electronics, Guangzhou, China)

Appl. Sci. 2025, 15, 12803

8 of 19

for body temperature and humidity measurement. Similar ESP32-centered biomedical
acquisition systems have been reported in low-cost sensing studies [34].

The DHT11 module was included as a low-cost demonstrator of the acquisition
pipeline [21]. ECG acquisition was performed using the AD8232 analog front-end opti-
mized for biopotential measurements [23]. Photoplethysmographic signals, heart rate, and
SpO2 were obtained using the GY-MAX30102 optical biosensing module [24]. Given that
no certified clinical thermometer was available during the experiments, a formal Bland–
Altman agreement analysis could not be performed within this prototype. Consequently,
the present work focuses on demonstrating the acquisition and interoperability aspects of
the temperature channel rather than its clinical accuracy.

The hardware configuration of the experimental setup is summarized in Table 1, while
Figures 3 and 4 present the electronic schematic created in Fritzing and the corresponding
assembled prototype.

Table 1. Hardware components used in the experimental setup.

Component

ESP32-
WROOM-32

DHT11

AD8232

GY-MAX30102

Functionality/Role

Quantity

Programming for vital sign acquisition; reception,
decoding, and transmission of the HL7 FHIR file.
Measurement of temperature and humidity; simulation
of a body temperature sensor.
Acquisition of the ECG signal.
Measurement of heart rate; measurement of blood
oxygen saturation (SpO2); acquisition of the PPG signal.

3

1

1

1

The physical implementation of the acquisition module is illustrated in Figure 4,
showing both the wiring diagram and the assembled hardware prototype. The system
architecture ensures proper isolation between analog and digital circuits, minimizing
interference and providing stable signal conditioning for biomedical measurements.

The integration platform was executed locally on a VMware Workstation 17 Player
instance running Ubuntu 22.04 LTS (Canonical Ltd., London, UK), hosting Home Assistant
as the middleware layer with Mosquitto (MQTT broker), InfluxDB (time-series database),
and Grafana (data visualization tool). All modules communicate within a local Wi-Fi
network, ensuring sub-second transmission latency and complete control over data flow.
The integration platform was hosted locally on VMware, as illustrated in Figure 5.

Figure 5. Launching the Home Assistant system in VMware for data acquisition and visualization.

 Appl. Sci. 2025, 15, 12803

9 of 19

The ECG signals were acquired using medical-grade Ag/AgCl disposable electrodes
with solid hydrogel, connected via a shielded 3.5 mm TRS cable to the AD8232 amplifier.
The technical characteristics of the electrodes are provided in Table 2. To minimize inter-
ference, the acquisition laptop remained disconnected from the AC power supply during
all tests.

Table 2. Characteristics of the ECG electrodes.

Size
Thickness

35 mm
1 mm

All sensors and modules were calibrated for synchronized operation, ensuring consis-
tent sampling across all acquisition channels. The HL7 FHIR file structure implemented in
the firmware maintained timestamped entries for each signal, enabling complete interoper-
ability testing across the hardware, MQTT transport, and visualization layers.

3.2. HL7 FHIR Observation Structure and Data Flow

The developed system employs a unified HL7 FHIR Observation resource to repre-
sent all acquired physiological parameters in a structured and semantically interoperable
format. Continuous biosignals—such as electrocardiographic (ECG), photoplethysmo-
graphic (PPG), and temperature time-series—were encoded using the valueSampledData
element, which stores numerical sequences together with their metadata: origin, scaling
factor, sampling period, and physical units [31]. Similar FHIR-based waveform-encoding
workflows have been demonstrated in recent biomedical informatics studies [35,36], con-
firming the feasibility of integrating IEEE 11073 metadata with HL7 FHIR for multi-sensor
physiological time-series.

Scalar physiological quantities, such as blood oxygen saturation (SpO2) and heart
rate (BPM), were represented by the valueQuantity structure, allowing each Observation
to encapsulate both waveform and scalar components in a consistent schema. This dual
representation ensures compatibility with standard-compliant medical record systems and
enables automatic data parsing across heterogeneous platforms.

Each Observation instance includes mandatory metadata fields—identifier, device
reference, acquisition timestamp, and component list—ensuring traceability from the sensor
level to the visualization layer. The hierarchical structure of the message maintains semantic
integrity across all transmission stages, supporting real-time clinical interpretation and
subsequent integration into electronic health record (EHR) systems.

The data generation and integration flow—from multi-sensor capture, local format-
ting into HL7 FHIR JSON, MQTT publication, to real-time visualization in Grafana—is
illustrated in Figure 6.

Figure 6. Acquisition system and HL7 FHIR Observation file generation flow.

Appl. Sci. 2025, 15, 12803

10 of 19

Representative HL7 FHIR Observation components are shown in Figure 7, illustrat-
ing temperature (10 samples) and ECG SampledData encoding (300 samples) within the
valueSampledData structure. These examples confirm the correct encoding of time-series
data with explicit temporal metadata and the use of valueQuantity for scalar indicators,
validating full compliance with HL7 FHIR standards.

Figure 7. Representative HL7 FHIR Observation components: (a) Temperature Reading (10 samples
at 0.5 Hz); (b) ECG signal segment (300 samples acquired at 100 Hz).

The ECG sequence corresponds to a 3-s window, while temperature values are repre-
sented as scalar entries within the same Observation structure. During experimental runs,
the ESP32 nodes performed synchronized sampling (ECG at 100 Hz; temperature at 0.5 Hz;
optical PPG buffers over 300 samples per cycle) and published their outputs to dedicated
MQTT topics—waveform data (ECG/PPG) under fhir/ecg and fhir/ppg, and scalar val-
ues (SpO2, BPM, temperature) under fhir/spo2, fhir/bpm, and fhir/temp. The uniform
timestamp alignment maintained within the generated HL7 messages ensured accurate
correlation between physiological parameters and reproducible cross-channel analysis.

3.3. Integration in the Open-Source Platform

Following deployment of the acquisition module, the ESP32 nodes communicated
wirelessly through the Mosquitto MQTT broker, enabling bidirectional data exchange be-
tween the hardware layer and the integration platform. Upon startup, each node published
HL7 FHIR Observation payloads under predefined topics and simultaneously subscribed
to control channels for configuration or synchronization commands. The topic hierarchy—
structured as fhir/ecg, fhir/ppg, fhir/spo2, fhir/bpm, and fhir/temp—allowed selective
message routing and modular scalability across multiple nodes.

The Home Assistant environment served as middleware, automatically registering
each MQTT topic as a virtual sensor entity. Sensor metadata, units, and data types were
defined within the configuration.YAML file, ensuring persistent identification of all chan-
nels. The broker configuration was secured using TLS 1.2 encryption and SHA-256-based
authentication, providing confidentiality and message integrity during transmission.

At the data management layer, InfluxDB was employed as a time-series database
optimized for biomedical telemetry. The decoded physiological values received via MQTT
were continuously written to dedicated measurement tables. InfluxDB’s high-resolution
timestamping (sub-millisecond precision) ensured accurate temporal alignment across
ECG, PPG, and scalar channels, facilitating subsequent correlation and analysis.

Visualization and human–machine interaction were handled through Grafana, which
accessed the InfluxDB database via an HTTP API connection. Multiple dashboards were
designed to display both waveform and scalar data. Time-varying graphs were configured
for ECG and PPG signals, while numeric panels displayed instantaneous physiological
parameters, including body temperature, heart rate, and oxygen saturation.

Incoming physiological parameters at the MQTT broker are displayed in Figure 8,
where physiological parameters are published under their respective MQTT topics of the

  (a) (b) Appl. Sci. 2025, 15, 12803

11 of 19

fhir/# type. Grafana dashboards offering real-time visualization of waveform and scalar
parameters are shown in Figure 9.

Figure 8. Reception of physiological data on MQTT Topics of the “fhir/#” type.

Figure 9. Graphical interface of the Grafana module and representation of the acquired vital parameters.

A preliminary visual inspection of the acquired ECG and PPG waveforms indicated
stable morphology and acceptable baseline drift. The broader signal-quality assessment—
limited to indicative considerations regarding signal-to-noise characteristics and qualitative
comparison with clinically reported ranges—is presented methodologically rather than
numerically, as no certified comparators were available during acquisition. These method-
ological aspects and their limitations are discussed conceptually in this subsection.

To extend portability and field accessibility, the same Home Assistant–Grafana envi-
ronment was deployed on mobile devices (Android) using the Home Assistant Companion
application. This configuration enabled clinicians to monitor physiological data streams in
real time from any location within the secure network domain, whether local or remote.
Mobile visualization through the Home Assistant Companion application is illustrated
in Figure 10.

  Appl. Sci. 2025, 15, 12803

12 of 19

Figure 10. Panels for monitoring biomedical data transmitted via the HL7 FHIR mobile interface on
mobile devices.

From an architectural standpoint, the integration demonstrates that a fully open-source
stack—comprising MQTT transport, Home Assistant orchestration, InfluxDB storage, and
Grafana visualization—can sustain continuous biomedical data acquisition with sub-second
end-to-end latency. The system preserves semantic interoperability because all parameters
are encoded in the HL7 FHIR Observation format throughout the pipeline. Furthermore,
local hosting within VMware minimizes dependency on external clouds and ensures
complete data sovereignty and GDPR compliance.

The complete communication and visualization workflow validated the feasibility
of interoperable IoMT infrastructures for medical research, teaching laboratories, and
clinical prototyping. The quantitative results of this validation are detailed in Section 3.4
(Validation Results).

  Appl. Sci. 2025, 15, 12803

13 of 19

3.4. Validation Results

The validation campaign was conducted to evaluate the reliability, latency, and se-
mantic integrity of the complete acquisition and data integration chain—from biosignal
capture at the ESP32 nodes to visualization in Grafana. Each session included simultaneous
acquisition from both nodes under stable network conditions (Wi-Fi 2.4 GHz, nominal
throughput 150 Mbps), with all components synchronized to a standard Network Time
Protocol (NTP) source.

The unified HL7 FHIR Observation was generated in two successive stages to reflect
the dual-node configuration: (i) the first ESP32 node contributed temperature (10 samples)
and ECG (300 samples), while (ii) the second node appended PPG (300 samples), SpO2
(10 readings), and BPM (10 readings).

Representative excerpts of the resulting Observation and the corresponding channel
segments were previously shown in Figure 7, confirming proper hierarchical encoding via
the valueSampledData and valueQuantity structures.

Timestamps were instrumented at four conceptual measurement points in the acqui-
sition chain—(i) at the ESP32 publisher, (ii) upon broker reception, (iii) at InfluxDB write
completion, and (iv) at data ingestion by Grafana—to define the methodological basis for
latency estimation. The reported end-to-end latency excludes visualization-rendering time.
Visualization-rendering time in Grafana was explicitly excluded from all latency
estimates. Because the ESP32 nodes lacked timestamp-level hardware logging and the
dataset was limited, no statistically meaningful confidence interval estimation or latency
distribution analysis could be performed in this prototype. The methodological framework
and associated limitations are discussed conceptually in this subsection.

3.4.1. Qualitative Validation

End-to-end tests verified the system’s ability to maintain the semantic consistency of
HL7 FHIR JSON payloads across all transmission layers. The following criteria were used
for qualitative validation:

1.

2.

3.

Integrity check—No structural deviation of FHIR components was observed after
multiple serialization/deserialization cycles.
Temporal alignment—All waveform channels (ECG, PPG, temperature) remained
synchronized within ±5 ms across dual nodes.
Visualization consistency—The same numerical values recorded in InfluxDB were ac-
curately rendered in Grafana panels, confirming the fidelity of the end-to-end pipeline.

No packet loss was detected in any of the ten repeated test runs. The observed delay
from publication to visualization remained below one second, consistent with bedside
monitoring requirements for telemetry-grade IoMT systems.

Both ESP32 nodes were synchronized to a local NTP server (chrony on Ubuntu 22.04,
update interval 60 s), which maintained a drift of approximately ±5 ms over 60 s windows.

3.4.2. Quantitative Performance Analysis

To complement the qualitative findings, a quantitative performance assessment was
conducted across 10 consecutive acquisition cycles (60 s each). Key parameters—latency,
packet loss, ECG sampling rate, per-message throughput, and CPU utilization—were
recorded and averaged.

The results, summarized in Table 3, confirm near real-time responsiveness and demon-

strate that the system can operate continuously without degradation or data loss.

Appl. Sci. 2025, 15, 12803

14 of 19

Table 3. Quantitative performance indicators are measured during system validation.

Parameter

Latency (end-to-end)

Packet loss

Sampling rate ECG

Throughput (per message)

CPU load (ESP32)

Mean

0.84

0

100

2.4

41

Std. Dev.

Unit

0.07

–

–

–

6

s

%

Hz

kB

%

The results show that message throughput and CPU utilization remain well within
the ESP32 microcontroller’s operational envelope, with sufficient processing margin for
additional sensors or data-processing tasks. The consistent ECG sampling rate confirms
the timing precision of the valueSampledData structure and validates that the HL7 FHIR
format introduces negligible overhead in real-time transmission scenarios.

A complete multi-node scalability assessment under variable network contention is

left for future work and is discussed in Section 4.3.

3.4.3. End-to-End System Visualization

Figure 11 offers an integrated overview of the complete data path, combining the ac-
quisition and HL7 FHIR encoding workflow (Figure 6) with the local open-source platform
architecture (Figure 5).

Figure 11. End-to-end architecture of the biomedical acquisition system based on HL7 FHIR
interoperability.

The architecture demonstrates seamless interoperability among all layers: ESP32
nodes for signal acquisition, Mosquitto for MQTT transport, Home Assistant for message
orchestration, InfluxDB for time-series storage, and Grafana for real-time visualization.

Data from the ESP32 nodes are encoded into HL7 FHIR Observation messages, pub-
lished via the MQTT broker (Mosquitto), and processed by Home Assistant integrated
with InfluxDB and Grafana. The platform operates locally within a VMware instance to
minimize latency and ensure complete control over data privacy and access.

3.4.4. Summary of Validation Findings

1.

The experimental validation confirmed that:

•

•

•
•

The system ensures complete semantic consistency of physiological data across
all layers of the architecture through the standardized HL7 FHIR format.
End-to-end latency is sub-second, suitable for clinical and educational telemoni-
toring contexts;
Packet loss is effectively null, even under continuous streaming conditions;
Computational load remains below 50%, enabling scalability to additional
biomedical modalities.

Appl. Sci. 2025, 15, 12803

15 of 19

2.

These findings demonstrate that the proposed configuration can serve as a benchmark
architecture for reproducible, open-source implementations of biomedical Internet of
Things (IoMT) systems adhering to FAIR data principles.

4. Discussion

The validation results confirm that the proposed open-source architecture—comprising
ESP32-based acquisition nodes, an MQTT transport layer, and a Home Assistant–InfluxDB–
Grafana integration stack—achieves real-time, interoperable, and secure biomedical data
exchange using the HL7 FHIR standard.

The overall data flow, summarized in Figure 11, illustrates the interoperability of all
layers, from sensor-level acquisition and HL7 encoding to storage and visualization. Each
message retains its semantic structure and metadata throughout the entire transmission
pipeline, ensuring data integrity and traceability—a key requirement in medical telemetry
and clinical informatics [11,12,15,16,25,30,37].

In contrast to proprietary middleware or vendor-locked cloud gateways, the proposed
framework demonstrates that fully open-source implementations can achieve comparable
performance while providing significantly greater transparency. This is particularly relevant
for healthcare research environments, where reproducibility, auditability, and compliance
with data-protection regulations are essential. The observed end-to-end latency below 1s
and zero packet loss confirm that the system meets the responsiveness criteria for bedside
or continuous patient monitoring.

From a systems engineering perspective, three technical aspects stand out:

1.

2.

3.

Semantic interoperability through HL7 FHIR. The dual use of valueSampledData
for waveform signals and valueQuantity for scalar indicators provides a flexible yet
compact encoding scheme. This structure eliminates the need for custom parsers while
preserving machine-readability and self-description of physiological data, facilitating
downstream analytics and cross-platform data fusion.
Localized data orchestration and security. Hosting all services within a VMware-
based environment ensures independence from external cloud infrastructures, min-
imizing cybersecurity and privacy risks. The combination of TLS 1.2 encryption,
SHA-256 authentication, and local database storage enables compliance with GDPR
and ISO/IEC 27001 [38] principles for medical data protection.
Scalability and modularity. The MQTT topic hierarchy (fhir/#) allows seamless
addition of new biosignal nodes or measurement modalities (e.g., respiration rate,
non-invasive blood pressure) without modifying the existing system architecture. The
average CPU load below 50% further indicates sufficient computational headroom for
embedded preprocessing or adaptive filtering directly on the ESP32 nodes.

4.1. Implications for Deployment

The architecture aligns with the emerging paradigm of edge–cloud medical computing,
where preliminary filtering, feature extraction, or data quality evaluation occur near the
sensors before transmission to centralized hospital middleware or research repositories.
Such hybrid configurations enable distributed decision-support systems that combine
near-real-time monitoring with long-term clinical analytics. The proposed stack can thus
be deployed in applications including:

•
•
•

remote patient monitoring in telemedicine or home-care settings,
rapid prototyping of decision-support tools for teaching laboratories,
experimental platforms for EHR integration using HL7 FHIR RESTful APIs.

Appl. Sci. 2025, 15, 12803

16 of 19

Exclusively relying on open-source components promotes reproducibility and trans-
parency, facilitating independent validation of the architecture and its adaptation to a
variety of biomedical contexts.

4.2. Limitations

While the results validate the interoperability and latency performance, certain limita-
tions must be acknowledged. Experiments were performed in a controlled environment,
free of motion artifacts and external electromagnetic interference. Real-world hospital de-
ployments may introduce additional variability due to Wi-Fi congestion, sensor detachment,
or ambient noise.

Furthermore, although the security model was robust at the transport layer (TLS 1.2),
it lacked certificate lifecycle management, device attestation, and mutual authentication,
which are critical in clinical environments. Finally, the quantitative assessment focused on
latency and packet loss, while other metrics such as temporal jitter, timestamp drift, and
end-to-end synchronization errors remain subjects for future investigation.

4.3. Future Work

Future research directions include:

1.

Clinical-grade validation involving human participants and certified reference de-
vices to assess medical accuracy under diverse physiological conditions.

2. Multi-node scalability studies under variable network load and interference, to

3.

4.

evaluate performance in high-density IoMT deployments.
Integration of embedded intelligence at the edge—using on-board anomaly detection
or adaptive data quality assessment—before HL7 message generation.
EHR and cloud interoperability testing via HL7 FHIR REST APIs, to demonstrate
automated order/result exchange and inter-institutional data portability.

The open-source architecture of the implementation supports reproducibility and
reusability by other researchers, in line with the FAIR data principles (Findable, Accessible,
Interoperable, and Reusable) promoted in modern digital medicine.

Although multi-node evaluation was not performed experimentally, a throughput
analysis indicates that Mosquitto can sustain ≥300 messages/s under QoS0 on a 2.4 GHz
Wi-Fi LAN, and InfluxDB can handle >10k writes/min. With 5–10 ESP32 nodes sampling
at the tested rates, CPU and broker load remain well within system limits.

4.4. Summary of Contributions

The study demonstrates that open-hardware platforms (e.g., ESP32), combined with
standardized interoperability frameworks (e.g., HL7 FHIR) and open-source software
layers—including Mosquitto MQTT v2.0.15 (Eclipse Foundation, Ottawa, ON, Canada),
Home Assistant v2024.6 (Nabu Casa, San Diego, CA, USA), InfluxDB v2.7 (InfluxData, San
Francisco, CA, USA), and Grafana v10.2 (Grafana Labs, New York, NY, USA)—can achieve
medical-grade data acquisition with low latency, full semantic traceability, and compliance
with data-protection requirements.

5. Conclusions

This work presented the design, implementation, and validation of a fully open-source
framework for biomedical signal acquisition and interoperable data integration based on
the HL7 FHIR standard. The system—built around ESP32-WROOM-32 sensing nodes,
MQTT communication, and an open-source Home Assistant–InfluxDB–Grafana platform—
achieved reliable, real-time, and secure exchange of physiological data encoded in
FHIR Observations.

Appl. Sci. 2025, 15, 12803

17 of 19

The case study conducted on a multi-sensor vital-sign monitoring module was selected
as a representative and reproducible experimental configuration. It provides a concrete
validation scenario in which heterogeneous biosignals (ECG, PPG, temperature, SpO2, and
heart rate) are acquired, encoded, transmitted, and visualized through a standardized,
end-to-end pipeline. This choice was justified by its high relevance to clinical monitoring
contexts and its ability to test the complete interoperability chain—from edge acquisition
to human–machine visualization—under realistic operational constraints. The successful
integration of this setup demonstrates the feasibility of implementing semantically interop-
erable IoMT systems using only open-source components and non-proprietary middleware,
thus ensuring transparency, reproducibility, and accessibility for research and education.

Experimental validation confirmed semantic integrity, zero packet loss, and sub-
second latency, satisfying the performance requirements for bedside and telemedicine
monitoring. Quantitative measurements also showed sufficient processing headroom
for additional biosensors and edge-level signal processing, both of which are crucial for
scalable healthcare deployments.

From an engineering standpoint, the presented architecture bridges the gap between
academic IoMT prototypes and clinically applicable, interoperable infrastructures, provid-
ing a reference implementation that can be extended toward hospital-grade environments
or embedded clinical research networks.

Overall, this study contributes to advancing FAIR-aligned, open, and interoperable
digital health ecosystems, reinforcing the role of standardized HL7 FHIR data structures in
developing transparent, secure, and reusable biomedical information systems.

Supplementary Materials: The following supporting information can be downloaded at: https:
//www.mdpi.com/article/10.3390/app152312803/s1, The file Supplementary.docx contains the
detailed security-validation checklist and configuration items required for IoMT systems, including:
TLS required (p. 1); Disable anonymous login (pp. 1–2); Password rotation (p. 2); ACL example
(“sensor1/pub”, “dashboard/sub”) (pp. 2–4); Pseudonymisation rule (p. 4); NTP sync requirement
(pp. 4–5); HL7 FHIR reference file and generated Observation structures (pp. 5–6); Limitations
(pp. 7–8); Timestamp propagation (p. 8); Conclusions of the supplementary analysis (pp. 8–9);
Additionally, the Supplementary Materials include the full YAML MQTT configuration for Home
Assistant, MicroPython publishing scripts, and the representative HL7 FHIR waveform samples used
in the validation experiments.

Author Contributions: Conceptualization, F.-C.A., I.-R.A. and F.C.A.; methodology, I.-R.A.; software,
F.-A.T, .; validation, F.-C.A., F.-A.T, . and G.S.; formal analysis, G.-G.P.; investigation, F.C.A.; resources,
G.-G.P.; data curation, G.S. and F.C.A.; writing—original draft preparation, F.-A.T, . and I.-R.A.;
writing—review and editing, I.-R.A.; visualization, F.C.A.; supervision, F.-C.A., G.-G.P. and I.-R.A.;
project administration, F.-C.A.; funding acquisition, G.-G.P. All authors have read and agreed to the
published version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Data are not publicly available due to system configuration and
infrastructure protection requirements related to the deployed IoMT architecture; data may be
made available for academic and non-commercial research purposes upon reasonable request to the
corresponding author.

Acknowledgments: The study was carried out in the Energy Quality Laboratory of the Faculty of
Electrical Engineering at the National University of Science and Technology ‘Politehnica’ Bucharest.

Conflicts of Interest: The authors declare no conflicts of interest.

Appl. Sci. 2025, 15, 12803

References

18 of 19

1.

Dolin, R.H.; Alschuler, L.; Beebe, C.; Biron, P.V.; Boyer, S.L.; Essin, D.; Kimber, E.; Lincoln, T.; Mattison, J.E. The HL7 Clinical
Document Architecture. J. Am. Med. Inform. Assoc. 2001, 8, 552–569. [CrossRef]

3.

2. Hurrell, M.J.; Monk, T.G.; Nicol, A.; Norton, A.N.; Reich, D.L.; Walsh, J.L. Implementation of a standards-based anaesthesia
record compliant with the Health Level 7 (HL7) clinical document architecture (CDA). J. Clin. Monit. Comput. 2012, 26, 295–304.
[CrossRef]
Osamika, D.; Adelusi, B.S.; Kelvin-Agwu, M.T.C.; Mustapha, A.Y.; Forkuo, A.Y.; Ikhalea, N. A Critical Review of Health Data
Interoperability Standards: FHIR, HL7, and Beyond. WSN (World Sci. News) 2025, 203, 194–233.
Dolin, R.H.; Alschuler, L. Approaching semantic interoperability in Health Level Seven. J. Am. Med. Inform. Assoc. 2011, 18,
99–103. [CrossRef]
Tabari, P.; Costagliola, G.; De Rosa, M.; Boeker, M. State-of-the-Art Fast Healthcare Interoperability Resources (FHIR)-Based Data
Model and Structure Implementations: Systematic Scoping Review. JMIR Med. Inform. 2024, 12, e58445. [CrossRef] [PubMed]
Bender, D.; Sartipi, K. HL7 FHIR: An Agile and RESTful approach to healthcare information exchange. In Proceedings of the 26th
IEEE International Symposium on Computer-Based Medical Systems (CBMS), Porto, Portugal, 20–22 June 2013; pp. 326–331.

5.

6.

4.

7. Mandel, J.C.; Kreda, D.A.; Mandl, K.D.; Kohane, I.S.; Ramoni, R.B. SMART on FHIR: A standards-based, interoperable apps

8.

platform for electronic health records. J. Am. Med. Inform. Assoc. 2016, 23, 899–908. [CrossRef]
Benson, T.; Grieve, G. Principles of Health Interoperability: SNOMED CT, HL7 and FHIR, 3rd ed.; Springer: Cham, Switzerland, 2016.
[CrossRef]

9. Martínez-Costa, C.; Menárguez-Tortosa, M.; Fernández-Breis, J.T. An approach for the semantic interoperability of ISO EN 13606

and OpenEHR archetypes. J. Biomed. Inform. 2015, 53, 197–210. [CrossRef]

10. Eichelberg, M.; Aden, T.; Riesmeier, J.; Dogac, A.; Laleci, G.B. A survey and analysis of electronic healthcare record standards.

Comput. Stand. Interfaces 2005, 27, 307–318. [CrossRef]

11. Mukhiya, S.K.; Rabbiab, F.; Punax, V.K.I.; Rutle, A.; Lamo, Y. A GraphQL approach to healthcare information exchange with HL7

FHIR. Procedia Comput. Sci. 2019, 160, 338–345. [CrossRef]

12. Lamprinakos, G.; Kouroubali, A.; Lazou, A.; Katehakis, D.G. Using FHIR to develop a healthcare mobile application. In
Proceedings of the 2014 4th International Conference on Wireless Mobile Communication and Healthcare—Transforming
Healthcare Through Innovations in Mobile and Wireless Technologies (MOBIHEALTH), Athens, Greece, 3–5 November 2014.
[CrossRef]
Islam, S.M.R.; Kwak, D.; Kabir, M.H.; Hossain, M.; Kwak, K.-S. The Internet of Things for Health Care: A Comprehensive Survey.
IEEE Access 2015, 3, 678–708. [CrossRef]

13.

14. Dang, L.M.; Piran, M.J.; Han, D.; Min, K.; Moon, H. A survey on Internet of Things and cloud computing for healthcare. Electronics

2019, 8, 768. [CrossRef]

15. El-Sappagh, S.; Ali, F.; Hendawi, A.; Jang, J.H.; Kwak, K.S. A mobile health monitoring-and-treatment system based on integration

of the SSN sensor ontology and the HL7 FHIR standard. BMC Med. Inform. Decis. Mak. 2019, 19, 97. [CrossRef]

16. Espressif Systems. ESP32-WROOM-32; Datasheet Version 3.5; Espressif Systems: Shanghai, China, 2025; Available online:

https://device.report/espressif-systems-shanghai/esp-wroom-32 (accessed on 4 March 2025).

17. Wilkinson, M.; Dumontier, M.; Aalbersberg, I.; Appleton, G.; Axton, M.; Baak, A.; Blomberg, N.; Boiten, J.-W.; da Silva Santos,
L.B.; Bourne, P.E.; et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci. Data 2016, 3, 160018.
[CrossRef]

18. Mons, B.; Neylon, C.; Velterop, J.; Dumontier, M.; da Silva Santos, L.O.B.; Wilkinson, M.D. Cloudy, increasingly FAIR; revisiting

the FAIR Data guiding principles. Sci. Data 2017, 4, 170065. [CrossRef]

19. Mousavi, S.S.; Firouzmand, M.; Charmi, M.; Hemmati, M.; Moghadam, M.; Ghorbani, Y. Blood pressure estimation from
appropriate and inappropriate PPG signals using A whole-based method. Biomed. Signal Process. Control 2019, 47, 196–206.
[CrossRef]
Segarra, C.; Dalsgaard, P.; Saliou, V. MQT-TZ: Secure MQTT Broker for Biomedical Signal Processing on the Edge. Stud. Health
Technol. Inform. 2020, 272, 261–268. [CrossRef]

20.

21. Aosong Electronics Co., Ltd. DHT 11 Humidity & Temperature Sensor; Aosong Electronics Co., Ltd.: Guangzhou, China, 2017.
22. HL7-FHIR] HL7 International. HL7® FHIR® Specification (Release 4); HL7 International: Ann Arbor, MI, USA, 2019; Available

online: https://www.hl7.org/ (accessed on 4 March 2025).

23. Analog Devices,

Inc.

Single-Lead, Heart Rate Monitor Front End AD8232. March 2012.

Available online:

https://www.analog.com/en/products/ad8232.html (accessed on 15 March 2025).

24. Maxim Integrated. MAX30102—High-Sensitivity Pulse Oximeter and Heart-Rate Sensor for Wearable Health. San Jose. October
2018. Available online: https://www.analog.com/media/en/technical-documentation/data-sheets/max30102.pdf (accessed on
1 November 2024).

Appl. Sci. 2025, 15, 12803

19 of 19

25.

Stanford-Clark, A.; Truong, H.L. MQTT For Sensor Networks (MQTT-SN) Protocol Specification Version 1.2, 14 November 2013; OASIS
Open, OASIS Message Queuing Telemetry Transport (MQTT) Technical Committee: Woburn, MA, USA, 2013; p. 28.

26. HAPI FHIR. HAPI FHIR Documentation—Server Framework. Available online: https://hapifhir.io/ (accessed on 17

October 2024).

27. Estrin, D.; Sim, I. Open mHealth Architecture: An Engine for Health Care Innovation. Science 2010, 330, 759–760. [CrossRef]
28.

Jayathissa, P.; Wickramasinghe, N. HAPI-FHIR Server Implementation to Enhancing Interoperability among Primary Care Health
Information Systems in Sri Lanka: Review of the Technical Use Case. arXiv 2024, arXiv:2402.02838. [CrossRef]
Falkenhein, I.; Bernhardt, B.; Gradwohl, S.; Brandl, M.; Hussein, R.; Hanke, S. Wearable Device Health Data Mapping to Open
mHealth and FHIR Data Formats. In Healthcare Transformation with Informatics and Artificial Intelligence; IOS Press: Amsterdam,
The Netherlands, 2023; Volume 305, pp. 341–344. [CrossRef]

29.

30. Mannes, J. InfluxData Closes $16 Million Series B Led by Battery Ventures to Organize IOT Data. TechCrunch, 21 September 2016.
Available online:
31. HL7 International.

FHIR Release 4 (R4)—Observation Resource and SampledData Datatype.

32.

https://www.hl7.org/fhir/ (accessed on 26 March 2025).
IEEE 11073-10101-2004; Health Informatics—Point-of-Care Medical Device Communication—Part 10101: Nomenclature. IEEE
Standards Association: New York, NY, USA, 2004.

33. Pelekoudas-Oikonomou, F.; Zachos, G.; Papaioannou, M.; de Ree, M. Blockchain-Based Security Mechanisms for IoMT Edge

Networks in IoMT-Based Healthcare Monitoring Systems. Sensors 2022, 22, 2449. [CrossRef]

34. Mishra, S.; Mahesh, C.M.N.; Shukla, S.; Ravula, S.; Chaudhary, S.; Ranjan, P. Low-Cost IoT-Based Remote Health Monitoring

System. Int. Res. J. Eng. Technol. 2019, 6, 7984, E-ISSN: 2395-0056.

35. Lee, S.; Do, H. Comparison and Analysis of ISO/IEEE 11073, IHE PCD-01, and HL7 FHIR Messages for Personal Health Devices.

Healthc. Inform. Res. 2018, 24, 46–55. [CrossRef]

36. Bikia, V.; Schmiedmayer, P.; Zahedivash, A.; Aalami, L.; Rao, A.; Ravi, V.; Turk, M.; Ceresnak, S.R.; Aalami, O. Spezi Data Pipeline:

Streamlining FHIR-based Interoperable Digital Health Data Workflows. arXiv 2025, arXiv:2509.14296. [CrossRef]

37. MQTT. FAQ. Available online: https://mqtt.org/faq/ (accessed on 4 March 2025).
38.

ISO/IEC 27001:2022; Information Security, Cybersecurity and Privacy Protection—Information Security Management Systems—
Requirements. ISO/IEC: Geneva, Switzerland, 2022.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

