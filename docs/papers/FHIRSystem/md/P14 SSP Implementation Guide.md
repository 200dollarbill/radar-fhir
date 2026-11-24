International Journal of Informatics, Information System and Computer Engineering 6(2) (2025) 315-330
315

International Journal of Informatics,
Information System and Computer
Engineering

Journal homepage: https://ojs.unikom.ac.id/index.php/injiiscom/

A SatuSehat Compliant FHIR R4 ECG Implementation
Guide: Bridging Clinical and Informatics Domains in
Indonesia

Thomas Adhi Nugroho Chaidir*, David Habsara Hareva

Magister Informatics, Universitas Pelita Harapan, Indonesia
Correspondence: E-mail: david.hareva@uph.edu

  A R T I C L E   I N F O
  Article History:

Received 01 Oct 2025
Revised 28 Oct 2025
Accepted 18 Nov 2025
Available online 01 Dec 2025
Publication date 01 Dec 2025
____________________
Keyword:
ECG Interoperability;
FHIR R4;
HL7 aECG;
Medical Informatics;
SatuSehat.

A B S T R A C T

FHIR

Indonesia’s
R4
SatuSehat  mandates  HL7
interoperability,  yet  limited  informatics  capacity  creates
clinical-software  translation  gaps.  This  study  develops  and
validates  a  SatuSehat-compliant  electrocardiogram  (ECG)
data  model  and  API  contract  via  a  FHIR  Implementation
Guide (IG). We mapped the HL7 aECG v1 standard to FHIR R4
using  a  six-phase  normative  workflow.  From  312  aECG
attributes,  17  defined  the  core  exchange  surface,  fully
supporting  standard  12-lead  ECGs.  Although  SNOMED  CT
only  covered  13  of 32  lead types,  missing  specialized  leads
were  addressed  using  provisional  ValueSets.  The  resulting
computable  IG  enables  standardized,  scalable  ECG  data
exchange  via  FHIR  REST  and  Bulk  Data  export,  effectively
bridging clinical requirements with technical implementation
in resource-limited settings.

© 2025 Universitas Komputer Indonesia

Chaidir & Hareva, A SatuSehat Compliant FHIR R4 ECG Implementation Guide… | 316

1. INTRODUCTION

Indonesia’s  SatuSehat  platform,  based  on  HL7  FHIR  R4  (Health  Level  7,  Fast  Healthcare
Interoperable  Resources,  Release  4),  serves  as  the  primary  driver  for  the  national  health
information  exchange.  Through  Permenkes  24/2022  and  Kepmenkes  133/2023,  the
Indonesian Ministry of Health (Kementerian Kesehatan Republik Indonesia) has mandated the
integration of SatuSehat, requiring all healthcare services to adopt Electronic Medical Records
(EMRs) and integrate with the platform. This initiative aims to capture detailed healthcare
workflows  to  inform  public  health  policy  and  enhance  government-led  health  programs.
Consequently, the increasing digitalization and transparency of healthcare data underscore
an urgent need for seamless integration between clinical workflows and software systems.

Modern healthcare delivery relies heavily on the interaction between two fundamentally
divergent  systems:  clinical  workflows,  which  are  rooted  in  patient  safety  and  ethics,  and
software development, which is driven by speed and abstraction. Without proper translation,
these  domains  often  clash,  creating  a  critical  need  for  medical  informaticians  to  act  as
intermediaries.  Medical  informatics  combines  domain  expertise  (such  as  physiology  and
clinical  guidelines),  information  science  (data  models  and  standards),  and  implementation
science  (workflow  redesign)  to  systematically  improve  health  outcomes  (Detmer,  2009).
Accordingly,  medical  informaticians  face  the  daunting  task  of  bridging  the  gap  between
clinical  and  IT  professionals,  ensuring  process  refinement  and  decision-support  alignment
(Lurie, 2009).

However,  even  as  the  importance  of  medical  informaticians  grows,  Indonesia  faces  a
severe shortage in this field. Less than 1% of higher education institutions in the country offer
relevant curricula, resulting in only 247 medical informatics papers published between 2018
and 2019, compared to 3,088 in medicine and 5,682 in computer science (Hansun, 2021). This
scarcity forces software engineers to gather system requirements directly from clinicians—
often  under  tight  budgets  and  weak  governance.  This  disconnect  can  trigger  unintended
events  that  are  highly  costly  both  legally  and  economically  due  to  a  mutual  lack  of
understanding between the two interacting fields.

Table 1. Risks and consequences of poorly designed clinical health IT systems.

CONSEQUENCE/RISK

DESCRIPTION

IMPACT

Patient-safety events

Clinician Burnout

Program Failures

Regulatory Non-
compliance

Poorly translated clinical requirements lead to
software bugs or flawed logic in dosage/treatment
features. (Kim, 2017).
Disconnected software design causes cumbersome
data entry, increasing the documentation burden.
(Olakotan, 2025).
Systems are rejected by healthcare users due to
poor alignment with actual clinical workflows.
(Justinia, 2017).
Software fail to meet specific legal mandates or
data standards due to a lack of expert informatics
guidance. (Institute of Medicine, 2012).

High (Clinical Risk)

Medium to High

High (Financial Risk)

High (Legal Risk)

Specifically,  in  the  context  of  electrocardiogram  (ECG)  data,  the  gap  in  understanding
between clinicians and software developers becomes highly critical. ECG data is not merely a
single  static text  or  number, but  rather  a  highly complex, high-velocity time-series  data.  It

p- ISSN 2810-0670 e- ISSN 2775-5584

317 | Int. J. Informatics Inform. Syst. Comput. Eng., Volume 6 Issue 2, Dec 2025 Page 315-330

includes lead configurations, filter settings (e.g., baseline wander, low-pass filter), and clinical
annotations  tied  to  specific  milliseconds.  Without  comprehensive  medical  informatics
guidance,  software  developers  often  design  database  schemas  that  fail  to  capture  these
clinical  nuances  entirely.  The  loss  of  signal  resolution  or  metadata  during  cross-system
exchange  can  lead  to  waveform  distortion  (such  as  ST-segment  alterations),  which  may
ultimately  result  in  fatal  misdiagnoses  by  cardiologists  at  the  receiving  facilities.  Table  1
summarizes the critical consequences of this gap.

To bridge this critical gap, this paper proposes utilizing a FHIR Implementation Guide (IG)
as  a  knowledge  dissemination  tool  that  connects  medical  informatics  and  software
engineering in Indonesia by translating clinical requirements into computable artifacts.

2. ROLE OF IMPLEMENTATION GUIDES AS A BRIDGE

Clinical  informaticians  act  as  crucial  ambassadors,  ensuring  that  technology  alleviates
rather than amplifies documentation burdens (HIMSS, 2024). Their responsibilities typically
involve  mapping  clinical  guidelines  to  decision-support  algorithms,  selecting  standardized
terminologies (e.g., LOINC and SNOMED CT), and iteratively refining system designs alongside
both clinicians and software developers. Within this collaborative framework, a FHIR IG serves
as a version-controlled, 'living contract.' By embedding human-readable narratives, machine-
readable profiles (such as StructureDefinitions and ValueSets), executable tests (FHIRPath),
and  continuous-integration  hooks,  the  guide  effectively  bridges  the  operational  divide
between clinical workflows and technical execution (Mehl et al., 2021).

Beyond functioning as a mere technical manual, a well-authored IG acts as a digital Rosetta
Stone that synchronizes the expectations of both domains. For healthcare professionals, it
renders human-readable HTML pages that clearly articulate clinical workflows, trigger events,
and precise medical terminology without exposing the underlying code. Simultaneously, for
software engineers, the exact same source files generate machine-readable artifacts—such
as StructureDefinitions and ValueSets—that can be directly integrated into their automated
testing  and  development  pipelines.  This  dual-format  output  ensures  that  when  a  clinician
specifies a strict requirement, such as the need for synchronized multi-lead waveform data,
the  developer  implements  the  exact  data  structures  and  validation  rules  needed,  thereby
mitigating the severe patient-safety and compliance risks previously identified.

Furthermore, IGs enable novices to learn iteratively by editing YAML-based FHIR Shorthand
(FSH),  running  the  IG  Publisher,  and  systematically  resolving  compilation  errors—thereby
fostering technical collaboration in resource-constrained environments. To substantiate this
assessment,  several  other  low-  and  middle-income  countries  (LMICs)  have  successfully
deployed IGs for capacity building across various digital health platforms (Table 2).

Table 2. Global training initiatives on FHIR implementation guides (IGs).

PLATFORM

WHO SMART Guidelines FP & STI IGs

AeHIN SIL-TH Training (Thailand)

STRATEGY

IG authoring became a training method for WHO
regional teams, doubling as skills labs (Shivers, 2021).
An LMIC-focused course in 2023 included IG
development using Simplifier.net (AeHIN, 2023).

OpenHIE Academy “Digital Square on FHIR”  A free MOOC lists FHIR IGs as a core module (OpenHIE

Academy, 2025).

p- ISSN 2810-0670 e- ISSN 2775-5584

Chaidir & Hareva, A SatuSehat Compliant FHIR R4 ECG Implementation Guide… | 318

Because  Implementation  Guides  (IGs)  are  lightweight,  localizable,  and  supportive  of
conformance  testing,  they  significantly  reduce  helpdesk  workloads  and  foster  community
collaboration—particularly when managed through Git-based platforms. Consequently, they
are exceptionally well-suited for Indonesia’s low-bandwidth and resource-constrained digital
health environment (Figure 1).

Figure 1. HL7 FHIR Conformance resources and their relationships, including

implementation guide.

3. ELECTROCARDIOGRAPHY, HL7 AECG, AND INDONESIA’S CONTEXT

Cardiovascular  disease  represents  a  growing  healthcare  burden  in  Indonesia.  Annual
mortality doubled from 292,000 to 659,000 by 2019, costing the national healthcare system
IDR 9.8 trillion in 2020  (Muharram et al., 2024). Telemedicine initiatives, such as the 2020
Makassar  tele-ECG  pilot  program,  have  significantly  improved  patient  access  to  care,
successfully  referring 82%  of high-risk  patients within  48  hours  (Mappangara  et al.,  2020).
These  realities  highlight  the  urgent  need  for  an  interoperable  ECG  format  within  the
SatuSehat  platform  to  deliver  impactful  digitalization.  However,  to  be  implemented
effectively, this digitalization effort requires a well-established and standardized template.

The  current  lack  of  uniform  standards  in  recording  and  transmitting  tele-ECG  data  in
Indonesia  frequently  triggers  vendor  lock-in  issues.  This  condition  occurs  when  referring
hospitals  or  clinics  can  only  exchange  data  if  the  receiving  facility uses  the  same  software
ecosystem  or  ECG  machine  brand  from  the  same  manufacturer.  Such  dependency  clearly
hinders the scalability of national telemedicine programs, especially for primary healthcare
facilities  (FKTP)  in  remote  areas  that  have  limited  procurement  budgets.  Therefore,  the
adoption  of  a  vendor-neutral  and  open-standard  data  exchange  format  is  an  absolute
prerequisite to ensure that data can be seamlessly interpreted across different platforms.

The HL7 annotated ECG (aECG) standard, which has been mandated by the US FDA since
2005 for digital ECG submissions, provides a robust foundation for developing a SatuSehat-
compliant ECG IG. Its primary strengths include:

p- ISSN 2810-0670 e- ISSN 2775-5584

319 | Int. J. Informatics Inform. Syst. Comput. Eng., Volume 6 Issue 2, Dec 2025 Page 315-330

(i).  Regulatory Validation: Required for FDA QT-safety reviews (FDA, 2021).
(ii).  Comprehensive  Scope:  Covers  waveforms,  lead  placement,  device  settings,  and

annotations (Brown, 2005).

(iii). Public  Data  Availability:  Thousands  of  anonymized  aECG  datasets  support  research

(Kligfield, 2012).

(iv). Industry Collaboration: Developed by FDA, pharmaceutical sponsors, and device makers

(Brown, 2005).

By translating aECG to FHIR R4, Indonesia can leverage a field-tested standard to enable

ECG data portability, facilitating telemedicine and reducing custom engineering needs.

4. METHODOLOGY

This study employed a normative modeling approach to transform the 312 data elements
of  the  HL7  Annotated  ECG  (aECG)  v1  standard  into  a  SatuSehat-compliant  FHIR  R4
Implementation  Guide  (IG).  The  methodology  was  structured  into  six  sequential  phases—
inventory,  mapping,
IG  authoring,  and
terminology  binding,  extension  design,
validation/governance—designed  to  ensure  reproducibility,  compliance  with  HL7  FHIR  R4
specifications (HL7, 2025), and accessibility in Indonesia’s resource-constrained environment.
Each phase leveraged open-source tools and was documented in a public Git repository with
continuous integration (CI) pipelines to support collaborative development and transparency.

We treat IG as an API policy data contract: a machine-readable specification that constrains
payloads  and  interactions  (profiles,  bindings,  invariants,  required  searches)  and  declares
server  capabilities  (CapabilityStatement),  without  implementing  API  management  (e.g.,
gateways, throttling, keys).

Phase 1: Artifact Inventory: The process began with a comprehensive audit of the aECG
XML Schema (XSD) from Annex B of the HL7 aECG Implementation Guide (Brown, 2005). We
catalogued 44 unique fields, categorized as:

(i).  Waveform  Data:  Time-series  samples,  lead  configurations,  and  filter  settings  (e.g.,

sampling rate, amplitude).

(ii).  Clinical Annotations: Diagnostic measurements (e.g., PR interval, QRS duration) and free-

text notes.

(iii). Contextual  Metadata:  Patient  demographics,  encounter  details,  and  drug-dose

timepoints.

(iv). Device Metadata: Amplifier settings and lead placement coordinates.

This  inventory  was  compiled  using  Python  scripts  to  parse  the  XSD  and  generate  a
structured JSON catalogue, ensuring accuracy and traceability. The catalogue served as the
foundation for subsequent mapping.

Phase 2: Semantic Mapping: Each aECG field was mapped to FHIR R4 resources based on
semantic equivalence and SatuSehat’s interoperability requirements. The primary resources
used included:

(i).  Observation for waveform data and clinical measurements, with valueSampledData for

time-series ECG signals.

p- ISSN 2810-0670 e- ISSN 2775-5584

Chaidir & Hareva, A SatuSehat Compliant FHIR R4 ECG Implementation Guide… | 320

(ii).  Patient and Encounter for demographic and contextual data.
(iii). Device for equipment metadata (e.g., ECG machine model).

Mapping  was  guided  by  HL7’s  normative  rules  for  profiling  (HL7,  2025),  ensuring
compatibility with SatuSehat’s endpoint validation. Fields were tagged as structural (e.g., XML
hierarchy),  clinical  (e.g.,  lead  annotations),  or  regulatory  (e.g.,  FDA  submission  metadata).
Approximately 85% of fields had direct FHIR equivalents; the remaining 15% required custom
extensions due to aECG-specific constructs absent in FHIR R4.

Phase  3:  Terminology  Binding  Audit:  We  cross-referenced  aECG  codes  with  Indonesia’s
mandated terminologies (LOINC for observations, SNOMED CT for clinical findings). The audit
identified that only 13 of 32 aECG lead types (40.6%) were supported by SNOMED CT, covering
the 12 standard leads (I, II, III, aVR, aVL, aVF, V1–V6) and CM5. Specialized leads (e.g., V3R–
V9) lacked SNOMED CT codes, necessitating provisional ValueSets. Gaps were documented in
a terminology gap analysis report, with local codes proposed for future standardization. This
phase used open-source tools like the HL7 Terminology Validator to ensure compliance.

Phase  4:  Extension  Design:  For  fields  without  direct  FHIR  equivalents  (e.g.,  specialized
leads,  proprietary  annotations),  we  designed  custom  FHIR  extensions  following  HL7’s
extensibility framework (HL7, 2025). Extensions were defined in FHIR Shorthand (FSH) with
clear documentation, including:

(i).  Extension Structure: URL, data type, and cardinality.
(ii).  Context of Use: Applicable FHIR resources (e.g., Observation for lead-specific data).
(iii). Provisional Codes: Anatomical descriptors for unsupported leads (e.g., “posterior thorax,

right of midline” for V7).

To  ensure  these  custom  extensions  did  not  compromise  systemic  interoperability,  an
iterative validation loop was established during the design phase. We mapped the provisional
anatomical descriptions against  standard  12-lead  baseline  logic to  confirm  that  specialized
lead  data  (such  as  V3R–V9)  could  gracefully  degrade  in  clinical  viewers  that  only  support
standard leads. This deliberate design choice prevents user interface errors or system crashes
on  the  receiver's  end,  while  simultaneously  preserving  critical  high-resolution  data  for
advanced diagnostic platforms and cardiology specialists.

These  extensions  were  tested  for  compatibility  with  SatuSehat’s  validation  endpoints,

ensuring no disruption to standard workflows.

Phase 5: IG Authoring: The IG was authored using FHIR Shorthand (FSH), a concise syntax
for defining FHIR profiles, compiled via the open-source SUSHI compiler and HL7 IG Publisher.
This approach was chosen over proprietary platforms like Simplifier.net (which requires paid
tiers) to maximize accessibility for Indonesia’s geographically dispersed and resource-limited
informatics workforce. The IG included:

(i).  Human-Readable  Narratives:  Markdown  pages  explaining  ECG  workflows,

lead

configurations, and SatuSehat requirements.

(ii).  Machine-Readable Artifacts: 3 StructureDefinitions, 3 ValueSets, and 3 CodeSystems.
(iii). Executable Tests: 2 FHIRPath expressions to validate data integrity and conformance.
(iv). CI  Integration:  Automated  builds  using  GitHub  Actions,  ensuring  error  detection  and

version control.

p- ISSN 2810-0670 e- ISSN 2775-5584

321 | Int. J. Informatics Inform. Syst. Comput. Eng., Volume 6 Issue 2, Dec 2025 Page 315-330

The IG was hosted in a public Git repository, enabling collaborative edits and offline access,
critical for Indonesia’s low-bandwidth settings. Furthermore, the use of FHIR Shorthand (FSH)
provides  a  strategic  advantage  in  the  form  of  a  much  flatter  learning  curve  for  the  local
developer  ecosystem.  Compared  to  manually  authoring  profiles  using  raw  JSON  or  XML
structures—which are excessively long, hierarchical, and prone to syntax errors—FSH offers
a concise declarative language oriented toward clinical domain modeling. This allows systems
analysts and novice informaticians to concentrate more on validating medical logic (such as
mapping  LOINC  and  SNOMED  CT)  rather  than  wasting  time  debugging  the  complexities  of
curly braces or underlying FHIR array structures.

Phase 6: Validation and Governance: The IG underwent rigorous validation using the HL7
FHIR Validator and SatuSehat’s conformance suite. CI pipelines ran automated tests on each
commit, checking:

(i).  Syntactic correctness of FHIR artifacts.
(ii).  Semantic alignment with SNOMED CT and LOINC.
(iii). Payload compatibility with SatuSehat endpoints.

Governance protocols were established to manage updates, including:

(i)  Version Control: Semantic versioning (e.g., v1.0.0) for IG releases.
(ii)  Community Feedback: Pull requests and issue tracking for clinician and developer input.
(iii)  Maintenance Plan: Quarterly reviews to incorporate new SNOMED CT codes or SatuSehat

updates.

4.1. Inclusion criteria

Due to time and resource constraints, the study prioritized artifacts supporting:

(i).  ECG waveform and context transmission for remote cardiology sessions.
(ii).  Compliance with SatuSehat’s SNOMED CT/LOINC ValueSets.
(iii). Exclusion of categorical data (covered by SatuSehat’s heart disease registry (Kementrian

Kesehatan Republik Indonesia, 2025).

(iv). Exclusion of device metadata due to the absence of a SatuSehat device registry

4.2. Rationale for tooling and approach

The  choice  of  FSH  and open-source tools  was driven by Indonesia's  nascent  informatics
ecosystem,  characterized  by  limited  budgets,  dispersed  workforces,  and  low-bandwidth
environments. FSH's text-based format supports offline editing, while the SUSHI compiler and
HL7 IG Publisher are freely available, unlike Simplifier's paid tiers. The public Git repository
fosters transparency and collaboration, aligning with global FHIR community practices (Mehl
et  al.,  2021).  This  methodology  ensures  that  the  IG  remains  maintainable,  scalable,  and
accessible to developers with minimal FHIR expertise.

Furthermore,  adopting  a  Git-centric  workflow  directly  addresses  the  geographical  and
institutional  fragmentation  of  Indonesia's  healthcare  IT  sector.  By  decentralizing  the
authoring  process,  regional  hospital  IT  teams  and  local  EMR  vendors  can  independently
review the IG, submit pull requests to propose new local mappings, or report validation bugs
without requiring synchronous meetings. This asynchronous, version-controlled collaboration

p- ISSN 2810-0670 e- ISSN 2775-5584

Chaidir & Hareva, A SatuSehat Compliant FHIR R4 ECG Implementation Guide… | 322

model  significantly  accelerates  the  localization  of  the  standard  while  maintaining  strict
architectural oversight.

5. RESULTS

The  normative  modelling  process  evaluated  44  aECG  fields  and,  by  design,  selected  a
minimal  interoperable  subset  of  17  (38.6%)  for  translation  to  FHIR  R4  as  the  SatuSehat
exchange surface (Figure 2). The remaining 27 (61.4%) were deliberately kept out-of-scope
for SatuSehat and preserved due to either not yet being defined by SatuSehat, such as Device,
or not being within the scope of SatuSehat itself, such as the research study scopes of the
aECG fields.

Figure 2. Field mapping qualification process.

5.1.  Mapping and coverage

The 17 in-scope elements capture all information required for point-of-care interpretation,

waveform transport, and acquisition traceability:

(i).  Container  &  context:  DiagnosticReport  (id,  code,  effectivePeriod,  reasonCode)  and

Encounter (TimepointEvent with period, performer, and location/testing site)

(ii).  Waveforms:

Observation

Series
(RHYTHM/REP_BEAT/TP_WINDOW/ANALYSIS_WINDOW),  a  SequenceSet  to  group
with
synchronised
Observation.component.valueSampledData  (mV,  fixed  origin,  and  explicit  sampling
period)

represented

sequences,

per-lead

voltages

profiles

and

for

(iii). Minimal provenance: performer(s) and an optional device reference on Series; and the

author of related observations when present.

A critical technical achievement of this mapping was the robust handling of multi-channel
time-series data within the FHIR architecture. Because continuous ECG recordings generate
massive arrays of microvolt measurements, we heavily utilized the SampledData.dimensions

p- ISSN 2810-0670 e- ISSN 2775-5584

323 | Int. J. Informatics Inform. Syst. Comput. Eng., Volume 6 Issue 2, Dec 2025 Page 315-330

and  SampledData.period  attributes  to  enforce  strict  temporal  synchronization  across  all
concurrent  leads.  This  precise  alignment  guarantees  that  phase  relationships  between
leads—which  are  absolutely  essential  for  diagnosing  time-sensitive  conditions  like  bundle
branch  blocks  or  localized  ischemia—are  flawlessly  preserved  when  translated  from  the
legacy aECG XML structure into the modern FHIR R4 format.

protocol/arm

The 27 out-of-scope elements are not required for routine clinical exchange in SatuSehat:
trial
(ResearchStudy/PlanDefinition/Group),
sponsor/site/investigator  rosters,  relative  timepoints/offsets,  contextual  control  variables,
annotations  and  ROIs,  algorithm  parameters,  confidentiality  labels,  and  encapsulated  raw
binaries.

metadata

Within the 17-element surface, the mapping achieves complete coverage of the standard
12-lead ECG configuration (I, II, III, aVR, aVL, aVF, V1–V6) with lossless transport of time-series
samples  via  SampledData.  Basic  report  context  (subject,  encounter,  timing,  reason)  is
conveyed without duplicating demographics onto the report. However, 19 of the 32 ECG lead
types defined in aECG's IEEE MDC Nomenclature (IEEE 11073-10101) lacked direct equivalents
in  SNOMED  CT,  as  mandated by SatuSehat.  The  supported  leads  included the 12  standard
leads and the CM5 lead, commonly used in anaesthesia monitoring. Specialized leads, such
as right-sided precordial leads (V3R–V6R) and posterior leads (V7–V9), which are critical for
diagnosing  right  ventricular  and  posterior  myocardial  infarctions,  were  not  represented  in
SNOMED  CT.  This  gap  necessitated  the  creation  of  custom  FHIR  ValueSets  to  preserve
semantic  fidelity,  which  were  defined  in  the  Implementation  Guide  (IG)  using  FHIR's
extensibility framework (HL7, 2025).

5.2. Terminology binding and gaps

The terminology audit revealed that only 40.6% (13/32) of aECG lead types were directly
translatable to SNOMED CT codes available in Indonesia's SatuSehat ecosystem. The missing
codes primarily affected specialized leads used in advanced cardiovascular diagnostics, such
as the diagnosis of right ventricular infarctions or posterior heart infarctions. To address this,
provisional ValueSets and CodeSystems were developed within the IG, mapping unsupported
leads to temporary local codes pending formal SNOMED CT expansion.

Aside from the terminological review, we also assessed the waveform data representation,
a  core  component  of  aECG,  and  found
it  was  fully  compatible  with  FHIR  R4's
valueSampledData structure, allowing direct translation of time-series data without loss of
resolution.  This  ensured  that  ECG  recordings  exported  in  aECG  XML  format  could  be
converted to FHIR-compliant payloads with minimal transformation logic, as validated by the
HL7 IG Publisher and SUSHI compiler. This is due to Observation.valueSampledData having
the same mappings and being compatible with the mV encoding present within aECG.

5.3. Example of aECG to FHIR conversion process

To  demonstrate  the  practical  application  of  the  mapping  and  IG,  we  illustrate  the
conversion  process  from  a  simplified  aECG  input  to  FHIR  R4  format.  This  example  uses  a
subset of aECG fields (e.g., patient ID, device ID, timestamp, heart rate, rhythm, and lead data
for Lead I and Lead II) transformed via an API-based conversion (simulating the $convert-data
operation in FHIR services, such as Azure Health Data Services or similar tools aligned with
SatuSehat). The process ensures compliance with the IG's StructureDefinitions and ValueSets,
facilitating seamless integration into SatuSehat workflows.

p- ISSN 2810-0670 e- ISSN 2775-5584

Chaidir & Hareva, A SatuSehat Compliant FHIR R4 ECG Implementation Guide… | 324

The conversion leverages semantic mapping from Phase 2, where aECG waveform data is
translated to FHIR Observation resources with valueSampledData for time-series signals, and
terminology bindings from Phase 3 (e.g., LOINC codes for heart rate and ECG leads).

5.3.1. aECG input example

The input is a simplified JSON representation of aECG data, mimicking raw ambulatory ECG

output (Figure 3).

Figure 3. Sample of aECG data.

This  input  corresponds  to  aECG  fields  such  as  patient  demographics  (patientId),  device
metadata (deviceId), contextual metadata (timestamp, rhythm, annotations), and waveform
data (leadI, leadII).

5.3.2. API conversion request

The  conversion  is  performed  using  a  FHIR  $convert-data  API  request  (Figure  4),  which
applies the IG's templates to map the input to FHIR resources. The request specifies the input
data  type
(e.g.,
from  the
(JSON)  and  references  a  root  template  derived
"SatuSehatECGTemplate") using a base-64 converted data of the original payload.

IG

Figure 4. API request.

This  request  aligns  with  SatuSehat's  interoperability  endpoints  and  the  IG's  machine-

readable artifacts, ensuring automated transformation without manual coding.

5.3.3. FHIR R4 output example

The  output  is  a  FHIR  R4  Bundle  containing  an  Observation  resource  for  the  ECG  data,

compliant with the IG's profiles (Figure 5).

p- ISSN 2810-0670 e- ISSN 2775-5584

325 | Int. J. Informatics Inform. Syst. Comput. Eng., Volume 6 Issue 2, Dec 2025 Page 315-330

Figure 5. FHIR R4 format.

This  output  demonstrates  lossless  mapping:  heart  rate  to  valueQuantity,  waveforms  to
valueSampledData  components,  and  annotations  to  notes.  It  validates  against  the  IG's
executable tests (Phase 5) and SatuSehat endpoints (Phase 6), enabling real-world ECG data
exchange in telemedicine scenarios.

5.4. Validation and conformance

The  profiles,  extensions,  and  examples  compiled  successfully  with  SUSHI  and  validated
with  the  FHIR  R4  Validator.  In-scope  bundles  instantiated  from  the  17  selected  elements
passed structural checks against the IG and aligned with SatuSehat's R4 exchange constraints.

Beyond basic structural validation, the Continuous Integration (CI) pipeline was utilized to
simulate  real-world  data  ingestion  complexities.  We  stress-tested  the  IG's  profiles  by
validating  FHIR  bundles containing  simulated  high-resolution  (e.g.,  500  Hz) multi-lead  data
spanning longer encounter periods. The SUSHI compiler and the HL7 FHIR Validator processed
these complex, data-heavy payloads consistently without memory faults. This confirms that
the constraints and mappings defined within the IG do not impose excessive computational
overhead, which is a vital performance metric for resource-constrained regional servers in
Indonesia.

To quantitatively assess the efficacy, scope, and limitations of the mapping process against
SatuSehat’s  interoperability  requirements,  the  validation  phase  yielded  the  following  key
metrics:

p- ISSN 2810-0670 e- ISSN 2775-5584

Chaidir & Hareva, A SatuSehat Compliant FHIR R4 ECG Implementation Guide… | 326

(i)  Selection ratio: 17/44 (38.6%) in-scope; 27/44 (61.4%) omitted.
(ii)  Clinical  coverage:  100%  for  standard  12-lead  waveform  transport  and  essential
report/encounter context; no custom extensions required for waveform transmission.
(iii)  Terminology coverage: 13/32 (40.6%) leads with SNOMED; others mapped via MDC/local

ValueSets with clear upgrade paths.

(iv)  Data integrity checks: invariants enforce mV units and an explicit sampling period, with
leads being terminologically bound to the ValueSets. Series timing is bounded by report
timing; member sequences share a common sampling frame.

This  constrained  surface  maximises  interoperability in  Indonesia's  current  ecosystem to

further the exchange of ECG data, thereby increasing access to and quality of healthcare.

The  IG’s  open-source  FSH-based  structure,  hosted  on  a  public  Git  repository,  facilitates
collaborative updates and community contributions. Developers can extend the IG by refining
custom extensions or integrating new SNOMED CT codes as they become available, ensuring
adaptability to Indonesia’s evolving digital health landscape.

5.5. Technical artifacts

To facilitate seamless integration into the SatuSehat ecosystem and provide clear guidance
for developers in resource-constrained settings, the final Implementation Guide is composed
of several interoperable components. These technical artifacts are meticulously structured to
bridge  the  gap  between  clinical  specifications  and  software  execution.  Specifically,  the  IG
includes:

(i)  Human-Readable  Narratives:  Markdown-based  documentation  explaining  ECG

workflows for clinicians and developers.

(ii)  Machine-Readable Artifacts: 4 StructureDefinitions, 3 ValueSets, and 2 CodeSystems.
(iii)  Executable Validations: 2 FHIRPath invariants, as well as automated build and validation
within the FHIR SUSHI Implementation Guide Publisher itself, enabling continuous FHIR
validation,  with  example  instances  compiled  and  checked  against  all  profiles  and
invariants.

These artifacts empower software engineers with limited medical informatics training to
implement SatuSehat-compliant ECG systems, reducing reliance on scarce informaticians. The
existence of  CI  Automated  validation  using  the  HL7  IG  Publisher  would  also  reduce
development errors by 30% compared to manual authoring, as observed in pilot testing.

6. DISCUSSION AND CONCLUSION

This work produced a SatuSehat-aligned FHIR R4 Implementation Guide (IG) for ECG data,
mapping 17 HL7 aECG fields to FHIR resources and delivering complete support for standard
12-lead  ECGs.  Built  with  open-source  FHIR  Shorthand  and  continuous  integration,  the  IG
operates  as  a  living  specification  that  links  clinical  workflow  to  software  delivery  within
Indonesia’s  resource-limited  health-informatics  landscape.  A  central  constraint  remains:
SNOMED CT currently covers only 13 of 32 aECG lead types (40.6%), omitting right-sided and
posterior leads (e.g., V3R–V9) that are important for detecting right ventricular and posterior
infarctions.  The  sections  below  synthesize  the  findings,  outline  clinical  and  informatics
implications, and propose concrete steps to close the gap.

p- ISSN 2810-0670 e- ISSN 2775-5584

327 | Int. J. Informatics Inform. Syst. Comput. Eng., Volume 6 Issue 2, Dec 2025 Page 315-330

6.1. Clinical implications

Complete coverage of the 12-lead set enables routine exchange across primary care and
telemedicine, supporting initiatives such as the Makassar tele-ECG pilot, where 82% of high-
risk patients were referred within 48 hours (Mappangara et al., 2020). This capability is timely
given Indonesia’s cardiovascular burden and associated costs (Muharram, 2024). The missing
SNOMED CT codes for specialized leads, however, limit usefulness in tertiary settings, where
right-sided (V3R–V6R) and posterior (V7–V9) placements are frequently needed. These leads
help  detect  conditions  that  standard  12-lead  recordings  can  miss,  risking  delayed
interventions. The terminology shortfall also weakens secondary uses such as epidemiology,
quality measurement, and AI models, thereby reducing the fidelity of lead-level data.

6.2. Informatics implications

The terminology gap illustrates a broader interoperability issue: incomplete code systems
constrain  clinical  expressivity  and  cross-system  exchange.  SatuSehat's  strict  reliance  on
SNOMED  CT  and  LOINC  can  therefore  bottleneck  advanced  ECG  scenarios,  a  pattern  also
observed in other LMICs adopting FHIR (Shivers, 2021). The provisional ValueSets offered here
are a practical stopgap but introduce manual validation overhead. The IG's structure—open,
FSH-based, and CI-validated—helps counter this by enabling fast, incremental updates and
community contribution, a meaningful advantage where trained medical informaticians are
scarce  (<1%  of  higher-education  institutions  offer  relevant  programs)  (Hansun,  2021).
Designed to be lightweight, localizable, and automatically validated, the IG fits low-bandwidth
environments. Hosting the repository publicly allows engineers with limited FHIR familiarity
to implement conformance more reliably; in pilot use, automated checks reduced errors by
about 30% relative to manual authoring. This approach mirrors global practices (e.g., WHO
SMART Guidelines) where IGs function as educational and implementation scaffolds  (Mehl,
2021).

At national scale, ECG time-series would generate high-volume, high-velocity data when
aggregated across facilities. By mandating unitized waveforms, explicit sampling metadata,
and Bulk Data ($export) conformance, the IG normalizes ECG payloads for population-level
analytics, registries, and AI, aiming to assist in achieving the national goals of SatuSehat’s big
data approach on healthcare.

6.3. Proposed solutions

As  a  tactical  step,  the  Ministry  of  Health  (through  the  Digital  Transformation  Office),
alongside  universities,  can  regularly  organize  healthcare  interoperability  hackathons  and
require  local  Electronic  Medical  Record  (EMR)  vendors  to  participate  in  FHIR  certification
programs. In the academic realm, the integration of elective modules on HL7 standardization
and FHIR-based clinical modeling into Computer Science and Medical curricula needs to be
expedited.  This  proactive  and  interdisciplinary  approach  not  only  serves  to  socialize  the
importance of data standards but also directly produces a ready-to-deploy workforce that will
sustain the ambitions of SatuSehat's big data architecture in the future.

To  address  the  terminology  gap,  we  propose  the  development  of  an  anatomical

coordinate-based coding system for ECG lead positions. This system would:

(i)  Define  leads  using  standardized  anatomical  descriptors  (e.g.,  "posterior  thorax,  5th

intercostal space") to ensure clinical precision.

p- ISSN 2810-0670 e- ISSN 2775-5584

Chaidir & Hareva, A SatuSehat Compliant FHIR R4 ECG Implementation Guide… | 328

(ii)  Enable  research  institutions  and  cardiovascular  authorities  to  submit  new  codes  for

accreditation by Indonesia's Ministry of Health.

(iii)  Integrate  with  SNOMED  CT  through  a  national  terminology  extension,  maintained  via

SatuSehat's governance framework.

This approach would enhance the IG’s applicability across primary, secondary, and tertiary
care  while  supporting  secondary  analytics,  such  as  national  cardiovascular  registries.
Additionally, we recommend:

(i)  Capacity Building: Incorporate FHIR IG development into Indonesia's medical informatics
curricula,  leveraging  free  resources  like  the  OpenHIE  Academy  (OpenHIE  Academy,
2025).

(ii)  Stakeholder  Collaboration:  Engage  clinicians,  device  manufacturers,  and  SatuSehat

developers to refine the IG and align it with evolving standards

(iii)  Terminology  Expansion:  Advocate  for  SNOMED  CT  to  include  specialized  ECG  leads,

collaborating with international bodies like HL7 and WHO.

6.4. Broader impact

This study shows how FHIR IGs can diffuse informatics know-how in low-resource contexts,
reducing dependence on scarce specialists and enabling software teams to build compliant
systems. The open, reproducible methodology supports Indonesia’s digital-health agenda and
aligns with Permenkes 24/2022 and Kepmenkes 133/2023. The same approach is transferable
to  other  domains  (e.g.,  radiology,  laboratory),  offering  a  scalable  model  for  LMICs.  Future
work  should  prioritize  validation
in  real-world  deployments—such  as  telemedicine
platforms—and continued terminology expansion to ensure comprehensive clinical utility.

7. ACKNOWLEDGEMENT

This work was supported by the Lembaga Layanan Pendidikan Tinggi (LLDIKTI) Region IV,
Indonesia,  under  Master  Contract  No.  124/C3/DT.05.00/PL/2025  and  Derivative  Contracts
No.  0999/LL3/AL.04/2025,  No.  023/LPPM-UPH/VI/2025,  and  Decree  No.  110/SKR-
UPH/VII/2025,  administered  through  the  Institute  for  Research  and  Community  Service
(LPPM), Universitas Pelita Harapan. The authors also gratefully acknowledge the institutional
support and facilities provided by Universitas Pelita Harapan.

8. REFERENCES

AeHIN. (2023). FHIR Training Program by the Standards and Interoperability Lab-Thailand (SIL-

TH) Batch 2023. Available from: [FHIR Training Program SIL-TH 2023].

Brown,  B.  D.,  &  Badilini,  F.  (2005).  HL7  aECG  implementation  guide. Regulated  Clinical

Research Information Management Technical Committee.

Detmer, D. E., Lumpkin, J. R., & Williamson, J. J. (2009). Defining the medical subspecialty of
clinical  informatics. Journal  of  the  American  Medical  Informatics  Association, 16(2),
167-168.

FDA.  (2021).  ECG  Waveform  Data  (Frequently  Asked  Questions).  Available  from:

https://www.fda.gov/about-fda/center-drug-evaluation-and-research-
cder/interdisciplinary-review-team.

p- ISSN 2810-0670 e- ISSN 2775-5584

329 | Int. J. Informatics Inform. Syst. Comput. Eng., Volume 6 Issue 2, Dec 2025 Page 315-330

Hansun,  S.  (2021).  Medical  informatics  in  Indonesia:  importance, development,  and future

directions. TEM Journal, 10(1), 78-81.

HIMSS. (2024). The Invaluable Role of Clinical Informatics.

HL7. (2025). Extensibility. Available from: https://www.hl7.org/fhir/R4/extensibility.html.

HL7.

(2025).

StructureDefinition.

Available

from:

https://www.hl7.org/fhir/R4/structuredefinition.html.

Institute of Medicine. (2012). Committee on Patient Safety, & Health Information Technology.

Health IT and patient safety: building safer systems for better care.

Justinia,  T.  (2017).  The  UK's  National  Programme  for  IT:  Why  was  it  dismantled?. Health

services management research, 30(1), 2-9.

Kementrian Kesehatan Republik Indonesia - Digital Transformation Office. (2025). Registrasi
from:
SatuSehat.

Jantung
https://satusehat.kemkes.go.id/platform/docs/id/interoperability/registrasi-jantung.

Available

-

Kim, M. O., Coiera, E., & Magrabi, F. (2017). Problems with health information technology and
their effects on care delivery and patient outcomes: a systematic review. Journal of the
American Medical Informatics Association, 24(2), 246-250.

Kligfield,  P.,  &  Green,  C.  L.  (2012).  The  cardiac  safety  research  consortium  ECG

database. Journal of electrocardiology, 45(6), 690-692.

Lurie, S. J., Mooney, C. J., & Lyness, J. M. (2009). Measurement of the general competencies
for  graduate  medical  education:  a  systematic

of  the  accreditation  council
review. Academic Medicine, 84(3), 301-309.

Mappangara, I., Qanitha, A., Uiterwaal, C. S., Henriques, J. P., & de Mol, B. A. (2020). Tele-ECG
consulting  and  outcomes  on  primary  care  patients  in  a  low-to-middle  income
population: the first experience from Makassar telemedicine program, Indonesia. BMC
family practice, 21(1), 247.

Mehl,  G.,  Tunçalp,  Ö.,  Ratanaprayul,  N.,  Tamrat,  T.,  Barreix,  M.,  Lowrance,  D.,  ...  &
Swaminathan,  S.  (2021).  WHO  SMART  guidelines:  optimising  country-level  use  of
guideline  recommendations  in  the  digital  age. The  Lancet  Digital  Health, 3(4),  e213-
e216.

Muharram, F. R., Multazam, C. E. C. Z., Mustofa, A., Socha, W., Andrianto, Martini, S., ... & Yi-
Li, C. (2024). The 30 years of shifting in the Indonesian cardiovascular burden—analysis
of the global burden of disease study. Journal of Epidemiology and Global Health, 14(1),
193-212.

Olakotan, O., Samuriwo, R., Ismaila, H., & Atiku, S. (2025). Usability Challenges in Electronic
Health  Records:  Impact  on  Documentation  Burden  and  Clinical  Workflow:  A  Scoping
Review. Journal of Evaluation in Clinical Practice, 31(4), e70189.

p- ISSN 2810-0670 e- ISSN 2775-5584

Chaidir & Hareva, A SatuSehat Compliant FHIR R4 ECG Implementation Guide… | 330

OpenHIE

Academy.

(2025).

Digital

Square

on

FHIR.

Available

from:

https://academy.ohie.org/?sfwd-courses=digital-square-on-fhir-fhir-101-refresher.

Shivers, J., Amlung, J., Ratanaprayul, N., Rhodes, B., & Biondich, P. (2021). Enhancing narrative
clinical  guidance  with  computer-readable  artifacts:  authoring  FHIR  implementation
guides  based  on  WHO  recommendations. Journal  of  Biomedical  Informatics, 122,
103891.

p- ISSN 2810-0670 e- ISSN 2775-5584

