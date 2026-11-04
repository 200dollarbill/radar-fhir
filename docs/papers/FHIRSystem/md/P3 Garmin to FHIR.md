TYPE Original Research
PUBLISHED 06 October 2025
DOI 10.3389/fdgth.2025.1636775
Streamlining wearable data
integration for EHDS: a case
EDITED BY study on advancing healthcare
Shameer Khader,
Sanofi, France
interoperability using Garmin
REVIEWED BY
Ana Corte-Real,
devices and FHIR
University of Coimbra, Portugal
Zarina Shameer,
AbbVie, United States
*CORRESPONDENCE Somayeh Abedian1,2*, Eugene Yesakov3, Stanislav Ostrovskiy3
Somayeh Abedian and Rada Hussein1
somayeh.abedian@lbg.ac.at
RECEIVED 28 May 2025 1Ludwig Boltzmann Institute for Digital Health and Prevention, Salzburg, Austria, 2Institute of Health
Policy, Management and Evaluation, Dalla Lana School of Public Health, University of Toronto,
ACCEPTED 20 August 2025
Toronto, ON, Canada, 3Edenlab, Innovative Digital Health Solutions, Tallinn, Estonia
PUBLISHED 06 October 2025
CITATION
Abedian S, Yesakov E, Ostrovskiy S and
Introduction: Patient-Generated Health Data (PGHD) collected through
Hussein R (2025) Streamlining wearable data
wearable devices such as smartwatches offers new opportunities for
integration for EHDS: a case study on
advancing healthcare interoperability using personalized care, chronic disease management, and preventive health.
Garmin devices and FHIR. Despite this potential, technical, regulatory, and interoperability challenges
Front. Digit. Health 7:1636775. still limit the integration of PGHD into healthcare systems, especially in
doi: 10.3389/fdgth.2025.1636775
relation to standards such as Fast Healthcare Interoperability Resources (FHIR)
COPYRIGHT and the European Health Data Space (EHDS).
© 2025 Abedian, Yesakov, Ostrovskiy and
Methods:This study used the Garmin Vívoactive 4 smartwatch to collect PGHD
Hussein. This is an open-access article
distributed under the terms of the Creative and integrate it into a FHIR server via the Fitrockr hub and API. The Kodjin FHIR
Commons Attribution License (CC BY). The server was deployed to enable standardized data storage and transfer. In
use, distribution or reproduction in other
parallel, data from the Modular Open Research Platform (MORE) were
forums is permitted, provided the original
author(s) and the copyright owner(s) are examined for compatibility with FHIR resources. The process included device
credited and that the original publication in enrolment, data collection, mapping to FHIR specifications, and evaluation of
this journal is cited, in accordance with
compliance with General Data Protection Regulation (GDPR) requirements.
accepted academic practice. No use,
distribution or reproduction is permitted Results: The prototype demonstrated that data from Garmin devices could be
which does not comply with these terms. securely collected, mapped, and transferred into a FHIR environment.
Integration through the Fitrockr hub ensured structured data formatting and
reliability. The analysis of PGHD from the MORE platform confirmed that
heterogeneous data types, including physiological measures and survey
responses, could be represented with appropriate FHIR resources. These
findings highlight the technical feasibility and scalability of PGHD integration.
Discussion: The results confirm that PGHD from wearable devices can be
standardized and transferred into healthcare systems in compliance with
international standards and European regulations. This approach contributes
to bridging the gap between personal health data and medical decision-
making, supporting the objectives of the EHDS and enabling further use of
PGHD in research and innovation.
KEYWORDS
Patient-Generated Health Data (PGHD), FHIR (Fast Healthcare Interoperability
Resources), healthcare interoperability, wearable devices, data integration
Frontiers in Digital Health 01 frontiersin.org

Abedian et al. 10.3389/fdgth.2025.1636775
1 Introduction studies using the Modular Open Research Platform (MORE).
MORE is a research infrastructure designed to support digital
The increasing frequency of wearable health devices grants new health studies. It consists of a web-based study management
chances and opportunities for integrating Patient-Generated Health application, which allows researchers to configure studies and
Data (PGHD) into clinical workflows. Wearable technologies, such specify the data to be collected, and a companion study app that
as Garmin smartwatches, generate continuous health metrics that helps guide and support participants throughout long-term
can provide valuable insights for personalized healthcare, studies. MORE facilitates data collection in real-world settings,
continuing disease management, and preventive care (1–5). Many enabling researchers to analyze PGHD, and it actually works as
research studies and systematic reviews display the effect of these a PGHD data hub (20, 21).
types of data in promoting wellness and helping disease We analyzed the collected data and mapped them to the FHIR
management in the clinical and health domains (6–8). standard (see Figure 1).
Despite PGHD’s potential, several technical, regulatory, and This paper summarizes the results of our prototyping in this
usability barriers hinder effective PGHD utilization in clinical or endeavor, utilizing FHIR in standardizing the PGHD in
medical decision making (9). alignment with the EHDS recommendations for the secondary
However, the researchers show some risks and challenges use of data in research and innovation (22).
related to legal validation, privacy, or data sharing, including The prototyping process included several key steps: collecting
counting this type of data in medical records as clinical data, data, configuring the FHIR server, operating the Fitrockr API,
and in addition, some barriers in interoperability between technical mapping PGHD from the Garmin device to FHIR
wearable devices and standards in the healthcare domain, such specifications, and developing the portal. Moreover, the evaluation
as Fast Healthcare Interoperability Resources (FHIR®) (10–13). and analysis of data elements from the MORE platform are needed
The FHIR standard has been recognized as a widely accepted for conformance compatibility with FHIR resources. Ultimately,
standard to facilitate structured health data exchange across the aim was to demonstrate a scalable method for incorporating
different systems, supporting the integration of PGHD into wearable health data from various sources into healthcare systems.
Electronic Health Records (EHRs) (14).
On the other hand, PGHD is vital to the European Health
2 Methods and materials
Data Space (EHDS), as it provides a more complete view of
patient health. Integrating data from devices and apps enables
personalized care and enhances research, ultimately improving This study follows a multi-step method to integrate wearable
healthcare outcomes. Thus, the EHDS regulation highlights the health data into the FHIR ecosystem as a case study. The
need for robust interoperability frameworks to allow the secure integration process involves several key workings: data collected
sharing and exchange of health data across countries (15). from Garmin Vívoactive 4 smartwatches via the Fitrockr API, data
Furthermore, the Digital Health Convener (DH-Convener) transformation into FHIR-compliant resources, and secure data
initiative, conceptualized by the Ludwig Boltzmann Institute for transfer to an FHIR repository. Figure 2illustrates overall workflow.
Digital Health and Prevention, aims to create interoperability Alongside this, because MORE is a platform for secondary use
and security as a service platform that integrates PGHD with and research of health data, we attempted to assess the
EHRs (16, 17) in alignment with the EHDS technical and compatibility of PGHD, which is integrated into the platform,
governance requirements for the secondary use of data. This using the FIHR standard, as an experimental study on the
study addresses a prototyping of the DH-Convener initiative for secondary use of data platform on health data.
PGHD interoperability. We selected one popular model of Consequently, we received a JSON output of the MORE platform
Garmin, Vívoactive 4. It is widely used in healthcare research and based on FHIR resources and the FHIR Implementation Guide
based on its ability and other potential to provide consistent (IG), we provided an analysis of the FHIR-compliant schema (23).
real-time data as a reliable process on various health metrics (18). Details of these processes are in the following.
Garmin Vívoactive 4 is also considered a practical alternative
to gold-standard ECG procedures for heart rate variability
measurements, with most markers in the same range (19). 2.1 Seamless integration: leveraging PGHD
These results support the consistency of Garmin Vívoactive 4 from Garmin device for FHIR
and its reliability in capturing accurate health data, making it a interoperability
valuable tool in healthcare research as well.
Thus, the DH-Convener prototype provides a PGHD This section outlines the process of integrating PGHD from
integration model using Garmin Vívoactive 4 smartwatches, the Garmin Vívoactive 4 into an FHIR server (similarly for
focusing on real-time data streams from a PGHD hub (collected transferring data to an FHIR-compatible health system),
by the Fitrockr platform) and based on the FHIR standard preparing the data for transfer to other healthcare systems or
(stored by the Edenlab FHIR server) in compliance with GDPR. EHRs. It includes connecting devices, collecting data, mapping
As Patient-Reported Outcomes and questionnaires are PGHD to FHIR standards, and deploying the FHIR server to
considered valuable PGHD resources, we also integrated the ensure seamless interoperability and maintain data integrity, as
Ecological Momentary Assessment (EMA) collected in research detailed in the following sections:.
Frontiers in Digital Health 02 frontiersin.org

Abedian et al. 10.3389/fdgth.2025.1636775
FIGURE 1
Integrating wearable data with DH-convener and PGHD solutions in healthcare interoperability standards. “Fitrockr” logo reproduced with permission
from https://www.fitrockr.com/, “MORE” app logo reproduced with permission from https://dhp.lbg.ac.at/more/?lang=en, “Edenlab” logo
reproduced with permission from https://edenlab.io/and “Open EHR” logo reproduced with permission from https://openehr.org/.
FIGURE 2
Integrating PGHD from Garmin into FHIR through data transformation layers.
Frontiers in Digital Health 03 frontiersin.org

Abedian et al. 10.3389/fdgth.2025.1636775
2.1.1 Device enrollment and data collection By utilizing the Fitrockr hub and its data dictionary, we
In this phase, we selected Garmin Vívoactive 4 smartwatches ensured that all PGHD was accurately formatted, stored, and
for their ability to track key PGHD, including heart rate, step prepared for smooth integration into the healthcare ecosystem.
count, sleep patterns, activity intensity, stress level, etc. The hub also played a vital role in maintaining the integrity
Once the Garmin Vívoactive 4 devices were enrolled, they and quality of the data throughout the intake process, ensuring
were set up to continuously track and record health metrics that it met the necessary standards for further analysis. If any
which are vital for monitoring an individual’s physical activity, errors occurred in the data, such as inconsistencies in format or
sleep quality, burning calories, body composition, and overall unusual values, the hub would identify and correct these issues
health. This setup involved adjusting the data sampling rates by using preprocessing and correction methods, such as fixing
and ensuring the devices could automatically sync with the incorrect values or aligning the data with the correct formats.
central system through the Garmin Connect tool, which ensured This process ensured that the data remained accurate and
a smooth and nonstop flow of data. ready for subsequent analysis, which in the next step involved
On the other hand, real-time monitoring was essential for mapping to FHIR standard resources. Additionally, users could
tracking important health measures. Therefore, the Garmin monitor and view their data through the Fitrockr dashboard,
Connect tool was used to configure the devices, making sure which demonstrated the integrated data on the hub. Figure 3
they were correctly set up to gather data while also ensuring illustrates a snapshot of the Fitrockr hub.
that the data synced accurately with the central system for
reliable and constant data transfer. 2.1.3 FHIR server deployment and API
configuration
The Kodjin FHIR server was selected to ensure standardized data
2.1.2 Integrating PGHD from garmin vívoactive 4 storage and retrieval. It was configured to support seamless processing
with FHIR compatibility of FHIR resources and enable secure management of our prototyping
Aligned to better management of data collection, the Fitrockr on PGHD. The Kodjin solution uses a low-code declarative approach,
hub was employed. The Fitrockr hub served as the central allowing for efficient integration with minimal coding. We used a
platform for data acquisition, where it securely gathered and cloud version of the Kodjin FHIR server in this study.
organized the data from the Garmin devices. This platform has To make the data ready for integration with the FHIR server,
been shown to enhance data integration by supporting various we used the secure Public Fitrockr API to access the collected
wearable technologies and ensuring secure data administration (24). PGHD from the Fitrockr hub and then mapped each data
The collected data was then prepared for integration with the element individually and created an FHIR bundle, ensuring it
FHIR server. A critical component of this process was using the was practical with the FHIR standard.
Fitrockr data dictionary, which provided a list of standardized Moreover, the Public Fitrockr API was used for its secure,
data elements for the PGHD from wearable tools (25). In other standardized access to Garmin data. Participants voluntarily
words, it provides a clear point of view on wearable health data, initiated data sharing via the study portal. Token-based
and then defining details of interoperability between different authentication and encrypted communication ensured GDPR-
systems will be easier. compliant, ethical use of PGHD in the research.
The Fitrockr data dictionary provides structured naming and
codification of PGHD variables derived from Garmin and other 2.1.4 PGHD mapping to FHIR resources
wearable devices. The codification primarily relies on vendor- In this step, we mapped the processed and collected data to
specific identifiers, using parameter names and structures defined FHIR profiles using the Edenlab transformation tool to ensure
in the Garmin Health API (25), which are then systematically seamless integration. In this process, key FHIR resource types
organized within Fitrockr’s internal data dictionary (26). This were used, including Patient for personal information like name,
enables structured extraction of key health metrics such as heart gender, birth date, and contact details, and Observation for
rate, step count, and sleep stages. However, the data dictionary capturing health-related data such as Heart Rate, stress data,
does not currently use clinical coding systems such as LOINC or respiration, steps, VO2 max, Pulse Ox, BBI data, etc.
SNOMED CT, limiting direct clinical interoperability. These resources were structured and linked appropriately,
The data dictionary is maintained and validated internally by allowing consistent and standardized data exchange, aligning
the Fitrockr team, who test its accuracy and reliability through with the FHIR framework for smooth interoperability and
various production-level integrations. While not externally integration into healthcare ecosystems.
certified, the data schema is stable and widely used in Fitrockr’s We utilized the Kodjin mapping tool to convert the Garmin
deployments for research and wellness analytics. Vívoactive 4 PGHD collected on the Fitrockr hub into
Although it is not officially integrated with the HealthData@EU appropriate FHIR resources as a Liquid.
framework, the Fitrockr dictionary, due to its structured formatting In fact, Liquid is a template language designed to work with
and FHIR mapping offers a model that could be adapted to align FHIR resources data mapping. It enables complex mappings and
with the interoperability goals defined by the TEHDAS offers flexibility for data processing tools. This facilitated unified
recommendations (22), especially in the context of secondary data mapping and ensured compatibility with the FHIR standard for
use and PGHD harmonization within EHDS. further integration into healthcare systems (27).
Frontiers in Digital Health 04 frontiersin.org

Abedian et al. 10.3389/fdgth.2025.1636775
FIGURE 3
Overview of the Fitrockr dashboard for data monitoring and transfer trends.
Some of the data we retrieved from the Fitrockr hub and mapped While this solution is specific to the research study, adopting
to FHIR resources is illustrated in Figure 4. In addition, to further GDPR-compliant practices is critical for larger-scale projects to
demonstrate the data transformation process, we have included a protect user privacy and ensure data security by consulting with
raw JSON sample from the MORE research platform and its GDPR experts to ensure that the solutions meet the European
mapped version in FHIR format in the Supplementary Material. regulation standards for data sharing, such as using short message
(SMS) on participants mobile phones to give their confirmation
before using related data.
2.1.5 Validation and compliance monitoring
At the same time, for verification and confirmation on the
In this prototype, we developed a portal to allow users to
successful transfer of data to the FHIR server, we developed a
control their data-sharing preferences. This web-based portal
quick dashboard that allows for retrieving and fetching PGHD
provides an option for them to exclude sensitive data, such as
based on FHIR identifiers such as Patient ID and Participant ID
demographic details or stress analysis, and send only selected
or Patient name, etc. Therefore, it serves as a tool and proof for
data to the server of their choice.
verification of the entire process in our work.
In this research-focused project, formal consent forms were
not applied, as the study did not involve clinical intervention or
treatment. Instead, we developed a participant-controlled portal 2.2 Evaluation of compatibility of research
that allowed individuals to fully access and review their wearable data from the MORE platform with FHIR
data collected through Fitrockr.
Data sharing only occurred when participants actively clicked We examined a subset of PGHD from the MORE research
a “Send to FHIR Server” button, indicating voluntary and platform, which houses data from wearables like Polar; In the
informed participation in the research. This design supports the second section of our study, we worked with extracted JSON data to
principle of active informed consent through action, ensuring assess its conformance with the FHIR standard rather than utilizing
transparency and autonomy. an API for direct data transmission (as we did in the first section of
To ensure privacy and compliance with the GDPR, the research when we employed an API to obtain data from the
pseudonymization was implemented during data transmission to Fitrockr hub). This compatibility assessment was used in two stages:.
the FHIR server, each participant was assigned a unique, non-
identifiable code that replaced direct identifiers in the server. In 2.2.1 Data extraction and preprocessing
the second part of the study, where we analyzed data exported We worked with a subset of JSON-formatted PGHD instead of
from the MORE platform, no direct transmission occurred. utilizing an API. The extracted data was reviewed to determine the
These datasets were already anonymized due to their research necessary transformations for mapping to FHIR resources.
nature, and no identifying information was included. As such, In our analysis of the MORE research platform, we identified
GDPR compliance was ensured through anonymization at source. that the research data is categorized into four key elements:
Frontiers in Digital Health 05 frontiersin.org

Abedian et al. 10.3389/fdgth.2025.1636775
FIGURE 4
Retrieving data from the Fitrockr hub and mapping it to FHIR resources.
• Heart Rate: Physiological data obtained from wearable devices. 3.1 Data collection and synchronization
• Acceleration: Motion data used for activity tracking like
walking, running, or sedentary behavior. The Garmin Vívoactive 4 devices successfully collected
• Survey Responses: User-reported questions and answers. continuous personal health data, including heart rate, step
• GPS Data: Location information linked to recorded activities. count, sleep patterns, activity levels, and stress data. The devices
were enrolled and configured to synchronize with the central
system using the Garmin Connect tool, ensuring reliable data
2.2.2 Mapping to FHIR resources transfer. Data synchronization was achieved with minimal
To align the data with FHIR standards, we mapped each data latency, allowing real-time tracking and continuous monitoring
type to the corresponding FHIR resources: of the patient’s health metrics. The devices provided highly
consistent data with minimal errors, validating their use in
• Heart rate, GPS data, and acceleration → FHIR Observation
clinical and research settings.
• Survey responses → FHIR QuestionnaireResponse
This transformation was implemented using the Kodjin Liquid
templates to structure the extracted JSON data into FHIR- 3.2 Fitrockr hub data integration
compliant formats.
The Fitrockr hub played a pivotal role in the secure
aggregation and preprocessing of data from the Garmin devices.
3 Results
Data quality was maintained by leveraging the Fitrockr data
dictionary, which ensured consistency and compatibility between
The integration of Garmin Vívoactive 4 smartwatches with an the various wearable technologies used in the study. Any
FHIR-compliant system through the Fitrockr hub has inconsistencies in the data, such as missing or outlier values,
demonstrated significant technical feasibility for real-time data were automatically flagged and corrected, maintaining data
acquisition, transformation, and interoperability with healthcare integrity for further analysis. This platform facilitated seamless
systems. This section presents the key outcomes from the data ingestion and ensured compliance with healthcare data
prototyping process. security protocols.
Frontiers in Digital Health 06 frontiersin.org

Abedian et al. 10.3389/fdgth.2025.1636775
3.3 Mapping data to FHIR resources 4 Discussion
Data transformation from Garmin PGHD into FHIR-compliant 4.1 Aspects of interoperability in the DH-
resources was successfully completed using the Kodjin FHIR server convener prototyping
and resource mapper. The key FHIR resources used for this process
included Patient, Observation, and Bundle. PGHD elements such as In this prototype, we used of Fitrockr solution to collect
heart rate, steps, sleep quality, and stress levels were mapped to PGHD streams from the Garmin Vívoactive 4. This ensures that
FHIR Observation resources, while personal details were assigned the data is disciplined in a standardized format and machine
to Patient resources. This ensured that data from various wearable readable to be transferred securely. To ensure consistency across
devices, including Garmin, could be easily integrated into any various FHIR-compliant systems and platforms, we align the
FHIR-compliant healthcare system, ensuring interoperability with Fitrockr data dictionary with FHIR resources like Observation,
existing EHR systems. Device, and Patient, PGHD that meet a suitable conversion into
a standardized format, and so they are interpreted across various
FHIR-compliant systems and platforms.
3.4 Data compliance and GDPR
In the data exchange and integration concept, as shown in the
considerations
picture, we examine how data flows fluently between wearable
devices, the FHIR cloud server, and structured health data
A crucial aspect of the prototyping phase was ensuring that repositories. The FHIR standard serves as the link between these
the collected PGHD adhered to data protection regulations, data sources, enabling smooth interoperability. This facilitates
specifically GDPR. A user-friendly portal was developed to allow live access to PGHD within clinical or medical workflows,
participants to control their data-sharing preferences, with the allowing healthcare providers to include wearable data in patient
ability to decline some items of sharing, such as sensitive data records and make informed medical decisions.
like stress levels or personal demographics. This ensured user Additionally, alongside the Fitrockr hub, we employed the
autonomy while maintaining compliance with European data MORE research platform for the secondary use of PGHD,
privacy laws. Furthermore, consultations with GDPR experts including Patient-Reported Outcome Measures (PROMs), Patient-
confirmed that the solution met the regulatory standards Reported Experience Measures (PREMs), questionnaires, and other
required for large-scale health data integration projects. personal health data that can be defined by researchers and
considered PGHD. We evaluated the compatibility of these data
types with FHIR resources and mapped them to ensure compliance
3.5 Evaluation of compatibility with MORE
with FHIR standards. In this case, we assess the compatibility of
platform data
the MORE platform’s JSON data set with FHIR standards.
As a cross-system interoperability, in addition to FHIR, DH-
The analysis of PGHD data from the MORE research platform Convener explores complementary standards like openEHR and
demonstrated that even non-API data could be mapped to FHIR OMOP for semantic interoperability and data representation. While
standards. We successfully transformed a subset of JSON- FHIR ensures the exchange of data between systems, openEHR’s
formatted data, including heart rate, acceleration, survey archetype-based modeling provides a framework for representing
responses, and GPS data, into FHIR-compatible formats using complex clinical and health data in a structured and meaningful way.
Kodjin Liquid templates. The DH-Convener initiative, by providing PGHD in FHIR,
This demonstrated the versatility of the FHIR standard in openEHR, and OMOP standards, aims to ensure that PGHD is
accommodating data from various sources, including wearables not only exchanged but also accurately represented and
not initially supported by FHIR-compliant APIs. The mapped interpreted across various health information systems (16).
data was categorized appropriately into Observation (for
physiological and physical activity data), Questionnaire Response
(for survey data), and other relevant FHIR resources.
4.2 EHDS and PGHD interoperability
3.6 Scalability and future integration With the EHDS’s entry into force on 26 March 2025 (28).
PGHD plays a crucial role in fulfilling the EHDS goals of
The scalability of the proposed solution was validated through empowering individuals and enriching healthcare insights. With
the integration of PGHD from various wearable devices into the PGHD interoperability, the EHDS can gain a more
FHIR ecosystem. The use of the Fitrockr hub, Kodjin server, and comprehensive understanding of a patient’s health status beyond
FHIR resources demonstrated that this method could be applied to traditional clinical settings.
other wearable technologies, ensuring that PGHD from different This inclusion facilitates personalized care, promotes
sources can be standardized and integrated into healthcare systems preventative measures, and enhances research capabilities,
seamlessly. This scalability is critical for the extensive approval of ultimately leading to improved patient outcomes and a more
wearable health data in clinical and research settings. holistic approach to healthcare delivery.
Frontiers in Digital Health 07 frontiersin.org

Abedian et al.                                                                                                                                                          10.3389/fdgth.2025.1636775
The  DH-Convener  aligns  with  these  objectives  by  Furthermore,  systems  for  managing  dynamic  consent  in
demonstrating how FHIR-standardized PGHD can be integrated  compliance  with  EHDS  and  GDPR  should  be  designed  to
into EHR. The lessons learned from this integration and PGHD  ensure  data  security  without  compromising  clinical  utility
interoperability  can  inform  the  implementation  of  the  EHDS  (34).  In  this  context,  emerging  technologies  such  as
national  Health  Data  Access  Bodies  (HDABs)  to  efficiently  blockchain offer promising models for secure and transparent
manage  and  process  diverse  data  sources  while  maintaining  data  sharing  while  maintaining  patient  consent  and
quality and consistency. Ultimately, the HDABs will regulate the  traceability.  Recent  researchs  are  exploring  the  disruptive
secondary use of PGHD for research and innovation, ensuring  potential of blockchain in managing health data compliance,
privacy  through  strict  rules  involving  pseudonymization  and  particularly under GDPR (35).
| anonymization.  | Access  requires  | HDAB  | permits,  | guaranteeing  |     |     |     |     |     |     |     |     |
| --------------- | ----------------- | ----- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
data is used ethically and legitimately.
| Furthermore,  | Fitrockr’s  | structured  | data  | acquisition  | and  |     |     |     |     |     |     |     |
| ------------- | ----------- | ----------- | ----- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
5 Conclusion
mapping practices provide valuable input for the development
| of  future  | PGHD  integration  | pipelines.  | In  | alignment  | with  |     |     |     |     |     |     |     |
| ----------- | ------------------ | ----------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
TEHDAS  recommendations  (22),  such  platforms  demonstrate  The integration of PGHD using FHIR standards marks a
significant step toward advancing patient-centered, data-driven
practical approaches for harmonizing and reusing non-clinical
PGHD within cross-border health data infrastructures governed  healthcare. Through the DH-Convener initiative, the importance
|     |     |     |     |     |     | of  interoperability,  |     | data  quality,  | regulatory  |     | compliance,  | and  |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --------------- | ----------- | --- | ------------ | ---- |
by the EHDS.
|     |     |     |     |     |     | clinical  applicability  |     | in  utilizing     | wearable  |             | data  for  | improved      |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | ----------------- | --------- | ----------- | ---------- | ------------- |
|     |     |     |     |     |     | health  outcomes         |     | is  underscored.  | As        | identified  | in         | this  study,  |
4.3 Future works and impact on healthcare  addressing the existing challenges by improving standardization,
systems strengthening regulatory frameworks, and leveraging AI-driven
|     |     |     |     |     |     | analytics  | will  be  | essential  to  | unlocking  | the  | full  | potential  of  |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | -------------- | ---------- | ---- | ----- | -------------- |
PGHD in the future of digital health.
According to this study and operational work within the DH-
Convener initiative, the following technical directions for future  The study applies the FAIR (Findable, Accessible, Interoperable,
and Reusable) principles to ensure that PGHD collected from
research and development are proposed:.
wearable devices are structured, standardized, and optimized for
secondary use. To achieve findability, we aligned the data with
4.3.1 Real-time data processing and AI-powered
clinical decision support well-defined metadata and standardized formats, allowing efficient
identification and retrieval. Accessibility was ensured by securely
The integration of real-time data processing frameworks for
PGHD, especially in the context of PREMs and PROMs, should  storing  the  data  while  maintaining  controlled  and  authorized
|     |     |     |     |     |     | access  for  | clinical  | and  research  | purposes.  | Mapping  |     | PGHD  to  |
| --- | --- | --- | --- | --- | --- | ------------ | --------- | -------------- | ---------- | -------- | --- | --------- |
be prioritized for future efforts. This involves leveraging machine
learning (ML) and artificial intelligence (AI) for live analysis of  FHIR resources significantly enhanced interoperability, allowing
|                                                              |               |           |                  |           |           | seamless       | data  exchange  | between      | diverse    |     | healthcare  | systems   |
| ------------------------------------------------------------ | ------------- | --------- | ---------------- | --------- | --------- | -------------- | --------------- | ------------ | ---------- | --- | ----------- | --------- |
| PGHD,  enabling                                              | actionable    | insights  | and  supporting  |           | Clinical  |                |                 |              |            |     |             |           |
| Decision Support Systems (CDSS) (29–31). These advancements  |               |           |                  |           |           | and platforms. |                 |              |            |     |             |           |
|                                                              |               |           |                  |           |           | Additionally,  |                 | integrating  | the  MORE  |     | research    | platform  |
| would  enhance                                               | personalized  | care      | and  precision   | medicine  | by        |                |                 |              |            |     |             |           |
utilizing  live  data  from  wearable  devices  to  optimize  care  supported  the  reusability  of  PGHD  for  secondary  analysis,
aiding applications such as patient-reported outcomes (PROMs)
decisions. Expanding AI-driven predictive analytics for clinical
outcomes will improve decision-making and treatment pathways,  and experience measures (PREMs).
offering more targeted and effective healthcare interventions (32).
4.3.2 Data security, privacy, and regulatory  Data availability statement
compliance for PGHD
Ensuring the security and privacy of sensitive health data is
The raw data supporting the conclusions of this article will be
crucial in the integration of PGHD into the healthcare system.
made available by the authors, without undue reservation.
Since wearable devices are not classified as medical devices, the
legal status and standards of PGHD are still under development,
requiring further research on their quality, authentication, and
authorization  processes.  The  EHDS  aims  to  establish  a  Ethics statement
harmonized framework for health data sharing while ensuring
strong data protection measures, particularly in compliance with  Ethical approval was not required for this study because it did
the GDPR and other European laws (33). not involve human participants, personal identifiable data, or any
Additionally,  future  work  should  emphasize  developing  intervention  that  could  impact  individuals.  The  studies  were
robust encryption and privacy-preserving technologies, such  conducted  in  accordance  with  the  local  legislation  and
as federated learning and especially homomorphic encryption,  institutional requirements. The participants provided their written
to  protect  PGHD  during  transmission  and  storage.  informed consent to participate in this study.
| Frontiers in Digital Health |     |     |     |     |     | 08  |     |     |     |     |     | frontiersin.org |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

Abedian et al. 10.3389/fdgth.2025.1636775
Author contributions Generative AI statement
SA: Investigation, Writing – review & editing, Supervision, The author(s) declare that no Generative AI was used in the
Conceptualization, Writing – original draft, Project administration, creation of this manuscript.
Data curation, Visualization, Methodology. EY: Conceptualization, Any alternative text (alt text) provided alongside figures in this
Writing – review & editing, Software. SO: Writing – review & article has been generated by Frontiers with the support of
editing, Software, Conceptualization. RH: Investigation, artificial intelligence and reasonable efforts have been made to
Conceptualization, Project administration, Writing – review & ensure accuracy, including review by the authors wherever
editing, Writing – original draft, Methodology, Supervision. possible. If you identify any issues, please contact us.
Funding
Publisher’s note
The author(s) declare that no financial support was received
All claims expressed in this article are solely those of the
for the research and/or publication of this article.
authors and do not necessarily represent those of their affiliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
Acknowledgments
claim that may be made by its manufacturer, is not guaranteed
or endorsed by the publisher.
The authors thank Prabath W. S. Jayathissa and Florian
Katsch, members of the research group, for their valuable
contributions to the study.
Supplementary material
Conflict of interest
The Supplementary Material for this article can be found
online at: https://www.frontiersin.org/articles/10.3389/fdgth.2025.
Authors EY and SO were employed by company Edenlab. 1636775/full#supplementary-material
The remaining authors declare that the research was conducted
in the absence of any commercial or financial relationships that
SUPPLEMENTARY MATERIAL 1
could be construed as a potential conflict of interest. FHIR transaction bundle generated from MORE platform sample.
References
1. Piwek L, Ellis DA, Andrews S, Joinson A. The rise of consumer health wearables: 10. Ayaz M, Pasha MF, Alzahrani MY, Budiarto R, Stiawan D. The fast health
promises and barriers. PLoS Med. (2016) 13(2):e1001953. doi: 10.1371/journal.pmed. interoperability resources (FHIR) standard: systematic literature review of
1001953 implementations, applications, challenges and opportunities. JMIR Med Inform.
(2021) 9(7):e21929. doi: 10.2196/21929
2. Jim HSL, Hoogland AI, Brownstein NC, Barata A, Dicker AP, Knoop H, et al.
Innovations in research and clinical care using patient-generated health data. CA 11. Canali S, Schiaffonati V, Aliverti A. Challenges and recommendations for
Cancer J Clin. (2020) 70(3):182–99. doi: 10.3322/caac.21608 wearable devices in digital health: data quality, interoperability, health equity,
3. Hughes A, Shandhi MMH, Master H, Dunn J, Brittain E. Wearable devices in fairness. PLOS Digit Health. (2022) 1(10):e0000104. doi: 10.1371/journal.pdig.
cardiovascular medicine. Circ Res. (2023) 132(5):652–70. doi: 10.1161/ 0000104
CIRCRESAHA.122.322389
12. Brönneke JB, Müller J, Mouratis K, Hagen J, Stern AD. Regulatory, legal, and
4. Yu S, Chen Z, Wu X. The impact of wearable devices on physical activity for market aspects of smart wearables for cardiac monitoring. Sensors (Basel). (2021)
chronic disease patients: findings from the 2019 health information national 21(14):4937. doi: 10.3390/s21144937
trends survey. Int J Environ Res Public Health. (2023) 20(1):887. doi: 10.3390/
13. Sifaoui A, Eastin MS. Whispers from the wrist”: wearable health monitoring
ijerph20010887
devices and privacy regulations in the U.S.: the loopholes, the challenges, and the
5. Hsueh PYS, Dey S, Das S, Wetter T. Making sense of patient-generated health opportunities. Cryptography. (2024) 8(2):26. doi: 10.3390/cryptography8020026
data for interpretable patient-centered care: the transition from “more” to “better”.
Stud Health Technol Inform. (2017) 245:113–7. doi: 10.3233/978-1-61499-830-3-113 14. Tiase VL, Hull W, McFarland MM, Sward KA, Del Fiol G, Staes C, et al.
Patient-generated health data and electronic health record integration: a scoping
6. Huhn S, Axt M, Gunga HC, Maggioni MA, Munga S, Obor D, et al. The impact review. JAMIA Open. (2020) 3(4):619–27. doi: 10.1093/jamiaopen/ooaa052
of wearable technologies in health research: scoping review. JMIR Mhealth Uhealth.
(2022) 10(1):e34384. doi: 10.2196/34384 15. ehds2pilot.eu. Data interoperability, quality and protection—EHDS2 Pilot
(2022). Available online at: https://ehds2pilot.eu/package/citizens/(Accessed July 4,
7. Guardado S, Karampela M, Isomursu M, Grundstrom C. Use of patient-
2024).
generated health data from consumer-grade devices by health care professionals in
the clinic: systematic review. J Med Internet Res. (2024) 26:e49320. doi: 10.2196/49320 16. Abedian S, Hanke S, Hussein R. Application of the openEHR reference model
for PGHD: a case study on the DH-convener initiative. Int J Med Inform. (2025)
8. Guardado Medina S, Isomursu M. The use of patient-generated health data from
193:105686. doi: 10.1016/j.ijmedinf.2024.105686
consumer-grade mobile devices in clinical workflows: protocol for a systematic
review. JMIR Res Protoc. (2023) 12:e39389. doi: 10.2196/39389 17. LBI for Digital Health and Prevention. Digital health (DH) convener. Available
online at: https://dhp.lbg.ac.at/digital-health-dh-convener/(Accessed July 10, 2024).
9. Cohen DJ, Keller SR, Hayes GR, Dorr DA, Ash JS, Sittig DF. Integrating patient-
generated health data into clinical care settings or clinical decision-making: lessons 18. Kader F, Bayramoglu B, Tayfur I. Evaluation of the performance and reliability
learned from project HealthDesign. JMIR Hum Factors. (2016) 3(2):e26. doi: 10. of a smartwatch capable of performing ECGs: a prospective observational study.
2196/humanfactors.5919 Heliyon. (2025) 11(1):e41682. doi: 10.1016/j.heliyon.2025.e41682
Frontiers in Digital Health 09 frontiersin.org

Abedian et al. 10.3389/fdgth.2025.1636775
19. Theurl F, Schreinlechner M, Sappler N, Toifl M, Dolejsi T, Hofer F, et al. (EU) 2024/2847 (2025). Available online at: https://health.ec.europa.eu/latest-
Smartwatch-derived heart rate variability: a head-to-head comparison with the gold updates/regulation-eu-2025327-european-health-data-space-and-amending-directive-
standard in cardiovascular disease. Eur Heart J Digit Health. (2023) 4(3):155–64. 201124eu-and-regulation-eu-2025-03-05_en(Accessed May 11, 2025).
doi: 10.1093/ehjdh/ztad022
29. Raclin T, Price A, Stave C, Lee E, Reddy B, Kim J, et al. Combining machine
20. Pakianathan PVS, Wurhofer D, Kumar D, Niebauer J, Smeddinck J. Multi- learning, patient-reported outcomes, and value-based health care: protocol for
stakeholder design for complex digital health systems: development of a modular scoping reviews. JMIR Res Protoc. (2022) 11(7):e36395. doi: 10.2196/36395
open research platform (MORE). Stud Health Technol Inform. (2023) 301:204–9.
30. Folkvord F, Carlson JI, Ottaviano M, Carvajal D, Gonzalez LH, van de Schoot
doi: 10.3233/SHTI230040
R, et al. Using patient-generated health data more efficient and effectively to facilitate
21. LBI for Digital Health and Prevention. MORE (Modular open research platform the implementation of value-based healthcare in the EU—innovation report. Comput
for digital health: An infrastructure to foster data-driven innovation). Available Struct Biotechnol J. (2024) 24:672–8. doi: 10.1016/j.csbj.2024.10.026
online at: https://dhp.lbg.ac.at/more/(Accessed March 21, 2025).
31. Terheyden JH, Pielka M, Schneider T, Holz FG, Sifa R. A new generation of
22. Estupiñán Romero F, Bernal-Delgado E, Comendeiro-Mälloe M, Doupi P, González- patient-reported outcome measures with large language models. J Patient Rep
García J, Mäkinen M, et al. TEHDAS—wP6—d6.2—recommendations to Enhance Outcomes. (2025) 9(1):34. doi: 10.1186/s41687-025-00867-4
Interoperability Within HealthData@EU. Geneva: Zenodo (2022). doi: 10.5281/zenodo.
32. Cruz Rivera S, Liu X, Hughes SE, Dunster H, Manna E, Denniston AK, et al.
10036412
Embedding patient-reported outcomes at the heart of artificial intelligence health-
23. HL7 organization. FHIR resource implementation guide (2025). Available care technologies. Lancet Digit Health. (2023) 5(3):e168–73. doi: 10.1016/S2589-
online at: https://www.hl7.org/fhir/implementationguide.html (Accessed May 02, 7500(22)00252-7
2025).
33. Council of the EU and the European Council. European Health Data Space:
24. Fitrockr Health Solutions platform. Wearable health data solutions for your projects Council adopts new regulation improving cross-border access to EU health data
(2025). Available online at: https://www.fitrockr.com/(Accessed May 03, 2025). (2025). Available online at: https://www.consilium.europa.eu/en/press/press-
releases/2025/01/21/european-health-data-space-council-adopts-new-regulation-
25. Garmin. Garmin health API (2025). Available online at: https://developer.
improving-cross-border-access-to-eu-health-data/?utm_source=chatgpt.com
garmin.com/health-api/overview/(Accessed May 05, 2025).
(Accessed May 13, 2025).
26. Fitrockr. Data dictionary (2025). Available online at: https://www.fitrockr.com/
34. Shin H, Ryu K, Kim JY, Lee S. Application of privacy protection technology to
help-center/data-dictionary/(Accessed May 07, 2025).
healthcare big data. Digital Health. (2024) 10:20552076241282242. doi: 10.1177/
27. Edenlab Health Solution. Kodjin data mapper (2025). Available online at: 20552076241282242
https://kodjin.com/mapper/(Accessed May 09, 2025).
35. Taraboanta D, Popescu GH. Reflections about blockchain in health data
28. Directorate-General for Health and Food Safety. Regulation (EU) 2025/327 on sharing: navigating a disruptive technology. Int J Environ Res Public Health. (2024)
the European Health Data Space and amending Directive 2011/24/EU and Regulation 21(2):230. doi: 10.3390/ijerph21020230
Frontiers in Digital Health 10 frontiersin.org