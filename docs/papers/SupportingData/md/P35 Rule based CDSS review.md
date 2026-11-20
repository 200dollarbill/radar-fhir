Health and Technology (2022) 12:713–727
https://doi.org/10.1007/s12553-022-00672-9

REVIEW PAPER

A systematic review of technologies and standards used
in the development of rule‑based clinical decision support systems

Petros Papadopoulos1

 · Mario Soflano2

 · Yaelle Chaudy1 · Wilson Adejo1 · Thomas M. Connolly3

Received: 26 November 2021 / Accepted: 19 April 2022
© The Author(s) 2022

/ Published online: 27 May 2022

Abstract
A Clinical Decision Support System (CDSS) is a technology platform that uses medical knowledge with clinical data to pro-
vide customised advice for an individual patient's care. CDSSs use rules to encapsulate expert knowledge and rules engines
to infer logic by evaluating rules according to a patient's specific information and related medical facts. However, CDSSs
are by nature complex with a plethora of different technologies, standards and methods used to implement them and it can
be difficult for practitioners to determine an appropriate solution for a specific scenario. This study's main goal is to provide
a better understanding of different technical aspects of a CDSS, identify gaps in CDSS development and ultimately provide
some guidelines to assist their translation into practice. We focus on issues related to knowledge representation including
use of clinical ontologies, interoperability with EHRs, technology standards, CDSS architecture and mobile/cloud access.
This study performs a systematic literature review of rule-based CDSSs that discuss the underlying technologies used and
have evaluated clinical outcomes. From a search that yielded an initial set of 1731 papers, only 15 included an evaluation
of clinical outcomes. This study has found that a large majority of papers did not include any form of evaluation and, for
many that did include an evaluation, the methodology was not sufficiently rigorous to provide statistically significant results.
From the 15 papers shortlisted, there were no RCT or quasi-experimental studies, only 6 used ontologies to represent domain
knowledge, only 2 integrated with an EHR system, only 5 supported mobile use and only 3 used recognised healthcare tech-
nology standards (and all these were HL7 standards). Based on these findings, the paper provides some recommendations
for future CDSS development.

Keywords  Clinical Decision Support · Rules engines · Interoperability · Technology Standards · Ontologies

1  Introduction

Various definitions exist for a CDSS, for example, a CDSS
is “an active knowledge system that generates case specific
advice, based on two or more items of patient data” [1] or
“an active intelligent system capable of assisting the medi-
cal professionals by making specific recommendations and
decisions based on the analysis of patient specific informa-
tion and related medical facts” [2]. From a system architec-
ture perspective, a CDSS implementation as a diagnostic
tool is essentially an expert system built to present helpful

 *  Petros Papadopoulos

petros.papadopoulos@gmail.com

1  Computer and Information Sciences, University

of Strathclyde, Glasgow, UK

2  School of Computing, Engineering and Built Environment,

Glasgow Caledonian University, Glasgow, UK

3  Glasgow, UK

information  and  advice  to  the  clinician/physician  at  the
point-of-care. The main responsibilities of a CDSS are to
support decision making, improve the overall patient qual-
ity of service and increase patient diagnostic and prognostic
capabilities to the best available level, eliminate unneces-
sary mistakes and cost, and increase productivity [3]. The
expanding medical knowledge, patient information, diagnos-
tics, diseases and treatment methods, by necessity, is becom-
ing a science of information [2].

Expert systems consist of two main parts: the knowl-
edge base and rules, and the Inference Engine [4]. The
Inference Engine evaluates given parameters with exist-
ing knowledge and rules to deduct new knowledge about
a specific case and aid the clinician’s decision-making
process, usually at point-of-care. The inference mecha-
nism (the mechanism that comes to a conclusion based
on the knowledge base) can be achieved using a diverse
range of techniques including but not limited to: Bayesian

Vol.:(0123456789)1 3
714

Health and Technology (2022) 12:713–727

networks, neural networks, genetic algorithms, rule-based
systems (expert systems), decision trees (logical condi-
tions), casual probabilistic networks (statistical modeling),
data mining, natural language processing, case-based rea-
soning, and supervised/unsupervised training [1].

The area of CDSSs can be confusing with a plethora
of different technologies, standards and methods used to
implement them. Thus, it can be difficult for practitioners
to determine an appropriate solution for a specific sce-
nario. This study’s main goal is to allow an in-depth, better
understanding of different technical aspects of a CDSS
and ultimately provide some guidance to suitable solutions
that should be of interest to software developers of CDSSs
and also health practitioners involved in commissioning
or development.

This study will perform a systematic literature review
of the technologies used to develop rule-based CDSSs,
focusing on papers that contain a clinical evaluation of the
CDSS and discuss technical aspects of the implementation
of the rules engine, including how knowledge has been
represented and used. In addition, the paper examines the
standards used to develop CDSSs and their integration/
interoperability with Electronic Health Record (EHR) sys-
tems. The next section provides background information
on CDSSs, the third section discusses the research ques-
tions this paper attempts to answer and the methodology
used to review the literature and the fourth section dis-
cusses the findings. The final section provides conclusions
and recommendations from the study.

2   Background

2.1   Clinical decision support

CDSSs fall under two main categories with regards to
how they capture medical knowledge [5–7] that have dif-
ferent approaches on how to infer clinical knowledge (see
Fig. 1):

Fig. 1   Knowledge Capturing Approaches

•  Knowledge Based

Work-flow driven, use logical flows that contain state-
ments referencing and manipulating medical data;
Rule-based reasoning, capture knowledge in the form
of IF–THEN statements and forward chaining, until
a conclusion is reached;
Probabilistic reasoning, use Bayesian networks and graph-
ical representations that capture the relationship between
disease and symptoms with conditional probabilities.

•  Non-Knowledge Based

Machine Learning (ML), learn or train on large data-
sets of clinical data.

•  Artificial Neural Networks
•  Genetic Algorithms
•  Support Vector Machines.

Knowledge-based systems, also known as expert systems
or rule-based systems, use an extensive clinical knowledge
base  containing  subject-specific  knowledge  taken  from
the medical literature, or from one or more experts. Non-
knowledge based systems, also known as case-based systems,
use machine learning (ML) to look for patterns in clinical
assessment data to suggest a diagnostic probability. They are
described as non-knowledge based, as the system does not
actually have any knowledge prior to a ML algorithm process
taking place.

Non-knowledge approaches are very important to the future
of CDSSs as they simplify the knowledge acquisition and
maintenance process, a process that is time consuming and
requires considerable human effort [2]. This type of system
will be more widely used in the future when “big data” applica-
tions are widely used in healthcare to provide potentially more
accuracy in diagnosing disease than the average clinician [5].
The Watson Health system developed by IBM uses natural
language processing and information mining tools to provide
clinical guidance [8]. Although this type of system can solve
complex decision-making problems, they require large sets of
labeled data in order to train their algorithms and generally
do not provide the rationale behind the decisions made [8]. A
detailed survey of machine learning in CDSSs can be found
in [9].

This literature review focuses on knowledge-based CDSSs
and examples of such systems are discussed in the Analysis
section. Knowledge-based CDSSs are composed of three
basic architectural parts, namely the Medical Knowledge
Base, the Electronic Health Record, and the Inference Mecha-
nism (reasoning) [2], although the EHR may be a separate
system. We briefly discuss these components below.

1 3Health and Technology (2022) 12:713–727

2.2   Electronic health record (EHR)

The EHR stores a collection of patient health data in a secure
digital form. These records are shared through a network
and include information such as medical history, allergies,
immunization status, lab results, and personal statistics. The
EHR should accurately capture the most up-to-date health
status and history of a patient. Standards have been devel-
oped to define how EHR data should be structured, semanti-
cally described, and communicated. These standards include
HL7 (v2, v3, and FHIR), openEHR, ASTM E1384, CEN’s
TC 251, and ISO TC 215. EHRs also often rely on medical
terminologies such as SNOMED CT (SCT), LOINC, ICD,
RxNorm, and UMLS. We discuss standards and terminolo-
gies in the following sections.

2.3   Clinical rules engines languages and standards

Rule-based systems are characterized by their high degree
of agility to cater for constantly changing circumstances.
Rule-based systems are made up from a rule-base (usually
decomposed into rule-sets) and an inference engine that
operates on the rules. Imperative for this system paradigm
approach to work and be easier to maintain is that although
the rules collectively should behave as part of the program,
they should be stored as data [10].

One of the first CDSSs called MYCIN was developed
in the early 1970s at the University of Stanford. Develop-
ers accepted that straightforward algorithms of statistical
approaches were unsuitable for healthcare with the underly-
ing knowledge not well understood and disagreement even
between clinical experts on how best to treat a patient. The
nature of these types of problems led the researchers to use
interaction rules to capture knowledge about organisms that
can cause infections and the antibiotics appropriate to treat
them [5, 11].

Rule-based systems are used to develop CDSSs because
of their flexibility and agility, an advantageous approach
when working with clinical knowledge that is changing
constantly with new discoveries from studies. Furthermore,
clinicians are not always confident of the rules that should
apply to a specific situation [11]. Rule-based systems essen-
tially capture knowledge with conditions in logical systems,
similar to first-order logic. The rule is specified in the form
of IF–THEN clauses including logical functions and opera-
tions, and can be developed in various rule languages or
formats [12].

There are now several rules engines that are used widely
in diverse domains such as SEBASTIAN, Jess, Jena, CLIPS,
OpenCDS,  and  iLog  [13].  System  for  Evidence-Based
Advice through Simultaneous Transaction with an Intel-
ligent Agent across a Network (SEBASTIAN) is a CDSS
framework that uses web services, with a write once use

715

everywhere  medical  knowledge  language.  The  SEBAS-
TIAN framework also includes a rules engine. Jess is a Java-
based rules engine that provides rule-based programming
for expert systems based on the Rete algorithm for logic
inference. Jess is a superset of the CLIPS object-oriented
language for implementing expert systems. Jena, a seman-
tic web framework for Java, can extract and write data to
Resource Description Framework (RDF) graphs that repre-
sent an abstract model. Jena also supports the Web Ontology
Language (OWL). OpenCDS is an open-source, standards-
based framework that provides tools and resources to imple-
ment a CDSS. C Language Integrated Production System
(CLIPS) is an object-oriented language that can be used to
build expert systems. iLog is a business rules management
system with a rule represented by a statement of logic that
is used to make a business decision.

In  CDSS,  there  are  some  major  healthcare  standards
regarding Clinical Guideline Representation, Patient Infor-
mation and Medical Terminology as identified in [13] that
will be discussed in the following subsections.

2.3.1   Clinical guidelines

A key part of a CDSS is representing clinical knowledge.
This subsection discusses the use of clinical guidelines to
represent clinical knowledge. GLIF (Guideline Interchange
Format) is a computer-interpretable guidelines (CIGs) lan-
guage for modeling and executing clinical practice guide-
lines (CPGs). GLIF supports sharing of CIGs across dif-
ferent medical institutions and platforms. GLIF defines an
ontology for representing guidelines, as well as a medical
ontology for representing medical data and concepts. In
GLIF3, guidelines can be encoded at three levels: a con-
ceptual flowchart, a computable specification that can be
verified for logical consistency and completeness, and an
implementable specification for inclusion into particular
organizational information systems [14].

NewGUIDE  is  a  guideline  representation  formalism
developed at the University of Pavia. In NewGUIDE the
guideline is hierarchically structured in “pages” representing
different abstraction levels: the first (high level) page is nor-
mally composed by a flowchart of non-atomic tasks, whose
expansion is described in inner pages. The main features
of NewGUIDE are: the capability to represent sequential,
parallel and iterative paths, the possibility of running ana-
lytic-decision models when decisional tasks are not associ-
ated with specific rules, the use of a terminology server to
define the guideline task names, and finally the possibility of
generating a Petri net written in WPDL (Workflow Process
Definition Language) for guideline simulation purposes [15].
SAGE clinical guidelines representation is a standards-
based, shareable and interoperable active environment using
HL7, medical terminologies (eg. LOINC, SNOMED) and

1 3716

Health and Technology (2022) 12:713–727

virtual medical record standards. Asbru is a task-specific
and intention-based plan representation language to embody
clinical guidelines and protocols as time-oriented skeletal
plans. Skeletal plans provide a powerful way to reuse exist-
ing domain-specific procedural knowledge, while leaving
room  for  execution-time  flexibility  to  achieve  particu-
lar goals. Proforma is a formal knowledge representation
method for the development and execution of clinical guide-
lines. Proforma employs a process description language that
is based on a logical model of decision making and plan
enactment, the description language is a task-based formal-
ism that uses plans, decisions, enquiries and actions. There
are software suites of authoring, verification and testing
tools and can support web or standalone execution [16].

2.3.2   Patient information

The HL7 Virtual Medical Record (vMR) v3 standard speci-
fies a data model for representing clinical data relevant to a
CDSS. The purpose of the vMR is to provide a simple and
intuitive representation of data that can be used across CDSS
implementations and to address the issues of interoperability
between organizations and systems.

The HL7 Clinical Document Architecture (CDA) is an
XML-based markup standard intended to specify the encoding,
structure, and semantics of clinical documents for exchange.
The HL7 Continuity of Care Document (CCD) specification,
an XML-based markup standard intended to specify the encod-
ing, structure, and semantics of a patient summary clinical
document for exchange, is a constraint on the CDA standard.
The HL7 Fast Healthcare Interoperability Resources (FHIR)
is a standard data format that aims to simplify EHR-based data
sharing. The FHIR standard is designed to address the tech-
nical (understanding the data) and semantic (exchanging the
correct data) complexity for data exchange in eHealth.

Another interoperability standard is openEHR, an open
specification in eHealth that describes the management, stor-
age, retrieval and exchange of health data in EHRs, main-
tained by the openEHR Foundation. The atomic entity of
openEHR is an archetype – a reusable data element and group
definitions that can be reused in various clinical contexts, sim-
ilar to a FHIR resource. However, FHIR does not require a
specific language, whereas openEHR archetypes are designed
using the Archetype Definition Language (ADL) [17].

2.3.3   Medical terminology

There are a number of standard medical terminologies used
in CDSS systems including:

•  Logical Observation Identifiers Names and Codes (LOINC),
a universal standard for identifying medical laboratory
observations and has expanded to include nursing diagnosis,
outcomes classification, nursing interventions and patient
care datasets.

•  SNOMED Clinical Terms (CT), a collection of medical
terminology that includes terms, codes, synonyms and
definitions used in clinical documentation and reporting.
•  The ICD (International Classification of Diseases, Tenth
Revision, Clinical Modification), a system used by clini-
cians and other healthcare providers to classify and code
all diagnoses, symptoms and procedures recorded in con-
junction with hospital care in the U.S. It provides a level
of detail that is necessary for diagnostic specificity and
morbidity classification in the U.S.

•  RxNorm, provides normalized names for clinical drugs
and links its names to many of the drug vocabularies com-
monly used in pharmacy management and drug interaction
software. By providing links between these vocabularies,
RxNorm can mediate messages between systems not using
the same software and vocabulary.

2.4   Ontologies

The  plethora  of  medical  standards  and  the  freedom  to
loosely follow each standard by vendors has resulted in the
requirement for a common unified medical knowledge rep-
resentation approach that will make integration and informa-
tion exchange easier. In health informatics, ontologies offer
a formal description of health-related domain information
and provide a vocabulary for biomedical entities that address
the unified medical knowledge representation problem [2,
18, 19]. Ontologies facilitate standardisation, flexibility for
change, and therefore promote sharing and reusability of
medical knowledge between CDSS systems implemented
in different technology and standards [2, 20].

An ontology is part of artificial intelligence that focuses
on conceptualizations of objects / knowledge. It encom-
passes a “representation, formal naming, and definition of
the categories, properties, and relations between the con-
cepts, data, and entities that substantiate one, many, or all
domains” [21]. Ontologies generally appear as a taxonomical
tree of conceptualizations, from very general and domain-
independent at the top levels to increasingly domain-specific
further down the hierarchy and they construct a vocabulary
that represents knowledge by classifying and verifying ter-
minologies [22]. As a domain-independent knowledge repre-
sentation, an ontology is flexible and dynamic in expanding,
managing and integrating knowledge from different sources
as well as adapting it to the user’s needs and allows easier
knowledge sharing between domain applications. However,

1 3Health and Technology (2022) 12:713–727

717

there is a large number of ontological languages, which
poses a challenge for ontological editors when integrating
different ontological languages. It may also be difficult to
turn specialist knowledge into an ontology particularly when
the knowledge including its relationships are not clearly
understood/defined or open to contradictions and misinter-
pretations or if there is a lack of agreement about synonymy
when representing knowledge [23].

Ontologies are used in CDSSs to express complex struc-
tures and objects with complicated interconnections and still
maintain flexibility and compatibility with other systems.
Semantic reasoners are software that provide a higher level
of abstraction from the ontology layer and can infer logical
outcomes from a set of axioms. Thus, the inference engine
usually relies on rules that are expressed in an ontology lan-
guage. Although ontologies can be time consuming to develop
they provide key support for exchange of information.

Amongst many ontology languages, the most commonly
used ones are RDF, RDF Schema, OIL, DAML + OIL and
OWL (OWL, OWL-DL, OWL Lite) with the main difference
between them being the level of control on every concept.

OWL extends RDF to allow more complex relationships
between RDF classes and provide more precise constraints.
An ontology could be created without using an editor, how-
ever, there are ontology editors such as Protégé and Ontoterm
that provide an interface and visualiser for non-technical
users. A review of semantic web and rule-based inference
engines is conducted in [12, 24, 25] and some prototypes
have been developed to enable easier knowledge and rule
capturing (eg. [18]). Clinical knowledge can be inferred using
established rule languages such as RuleML and SWRL.

There are existing medical ontologies available online
such as SNOMED CT and LOINC, and there are also ontolo-
gies that are domain-specific, for example, in diabetes, there
is Diabetes Mellitus Treatment Ontology (DMTO), for cardi-
ovascular there is Cardiovascular Disease Ontology (CVDO)
and  for  stroke  there  is  Stroke  Ontology  (STO-DRAFT/
CVAO).

3.  Have the CDSSs been integrated with the organizational

EHR?

4.  How has knowledge been represented in rules-based

CDSSs?

These research questions are designed to help capture
theoretical aspects of CDSSs technologies and standards
and the extent to which they are used in implementations of
CDSSs, i.e. trying to identify evidence of gaps in theory and
practice. For this reason this study only includes papers on
CDSSs that discuss the underlying technologies used, how
knowledge has been represented, and have been evaluated.

3.2   Systematic literature review

A systematic literature review of the most relevant databases
with the following search terms was performed (adjusted to
each database’s querying method):

(“Clinical Decision Support” OR “Diagnostic Deci-
sion Support” OR “e-health”) AND (“rules engine” OR
“inference engine” OR
“calculator” OR “business rule” OR “rule based”)

The search was limited to the time period 2007–2019
in seven of the most relevant research databases, namely:
Science Direct, Association Computing Machinery (ACM)
digital library, Springer, BioMed, PubMed, Emerald, and
Institute of Electrical and Electronics Engineering (IEEE)
Explore. The application of the search terms on each of
these databases yielded 1731 results (see Table 1) and by
looking at the title, abstract, and a quick overview of the
paper to ensure it discussed technical aspects of the imple-
mentation of the CDSS, including how knowledge had been
represented and used, this reduced the total to 341 possibly
relevant papers (see Fig. 2 for selection process). A thorough
review of the 341 possible relevant articles was then further
reduced to 114 relevant papers that were then further filtered
to 15 works that included some form of rigorous evaluation

3   Research methodology

Table 1   Search Results by Database

3.1   Research questions

Database

Search Results

Relevant Papers

Selected
Papers

In this work the focus is on rule-based CDSSs and the aim is
to answer the following research questions using a system-
atic review of the literature:

1.  How have the rules-based CDSSs been evaluated in terms

of clinical outcomes?

2.  What architectures, technologies and standards have

been used to develop rules-based CDSSs?

IEEE
ACM
BioMed
PubMed
Springer
Science Direct
Emerald
Total

20
19
101
68
1455
52
16
1731

16
11
40
29
207
33
5
341

0
0
1
1
10
3
0
15

1 3718

Health and Technology (2022) 12:713–727

that  accounts  for  chance  agreements  [26].  The  IRR  was
measured on a subset of the papers found, five papers from
each reviewer were selected at random to be reviewed by oth-
ers. Based on the 5 reviewers, 25 papers and 95 decisions, a
Krippendorff’s alpha of 0.742 was computed which can be
accepted as satisfactory [27]. The average pairwise agree-
ment was 78.7%.

4   Analysis

This section addresses each of the research questions set out
above based on the 15 papers that matched the original cri-
teria. The subsequent section discusses the overall findings
from the systematic literature review.

4.1   Evaluation

This  section  addresses  RQ1: How  have  the  rules-based
CDSSs been evaluated in terms of clinical outcomes? 15
papers were found that evaluated clinical outcomes covering
a range of medical areas including diabetes, cardiovascular,
respiratory, drug use, paediatrics, triage, health examina-
tions, intensive care, poisoning diagnosis, hepatitis, periph-
eral neuropathy, and lab tests.

4.1.1   Diabetes

There were three papers that covered diabetes [19, 28, 29].
Sherimon  &  Krishnan  [19]  discussed  OntoDiabetic,  an
ontology-based CDSS to assess risk factors and provide
appropriate treatment suggestions for diabetic patients. To
evaluate the system, a case study was conducted with 250
patients with risk of overt cardiovascular disease (CVD),
diabetic nephropathy and hypertension in primary health
centres in Oman. Risk assessment of the diabetic patients in
five different parameters (smoking, alcohol, physical, sexual
and cardiac) was conducted using OntoDiabetic and com-
pared with manual risk assessment by clinicians. Of the 250
patients, 123 were general diabetic patients having fewer
complications and the risk of these 123 patients was on aver-
age 74% efficient in risk assessment. The remaining 127
patients had one of three complications, overt CVD, diabetic
nephropathy and hypertension. 52 patients with overt CVD
were assessed with 83% accuracy; 34 diabetic nephropathy
cases were 79% accurate and 41 patients with hypertension
were diagnosed by the system with 85% accuracy.

Hussain et al. [28] discussed the development of a cloud-
based CDSS using a range of diverse inputs, such as sensors,
user profile information, social media, clinical knowledge
bases,  and  medical  experts  to  generate  standards-based
personalized  recommendations  for  diabetes.  Input  was
converted into a standard interface following HL7 vMR

Fig. 2   Literature Survey Selection Process

of the system. This study is based upon those 15 papers (see
Table 1 for breakdown of results by database).

Springer had the most results because the search terms
could not be applied to the title and abstract only and the
search returned papers that had the search terms present on
the full text. The number of relevant papers seems more
pertinent for Springer once the filtering and review processes
were finished.

The papers were distributed between 5 reviewers. The
reviewers were given a list of rules as inclusion criteria and
the relevant information that should be extracted from the
paper, if present. Inclusion criteria included all papers that
used a rule-based approach in the health domain, includ-
ing  studies  and  reviews.  Some  of  the  information  to  be
extracted was the medical area of the work, how the logic
was integrated in the tool/study, how the Knowledge was
represented and acquired, functionality of the used technol-
ogy, system architecture, platform security and privacy and
relevant accreditation, validation and evaluation of the study,
hard coded logic, using an existing engine rule engine, rules
engine language, logic editor. This information helped to
form a useful and comprehensive view of the field of rules
engines in the CDSS domain that to the best of knowledge
of the authors has not been done before to this extent.

3.3   Inter‑rater reliability

Inter-rater reliability (IRR) was performed and computed
using Krippendorff’s alpha, a well-regarded, flexible measure

1 3Health and Technology (2022) 12:713–727

719

standards and submitted to the CDSS to generate recommen-
dations. The system was evaluated with test data from 100
patients at Saint Mary’s Hospital in Korea: 20 with type-1
diabetes, 40 with type-2 diabetes mellitus, and 40 with sus-
picions for diabetes but no specific diagnosis. The system
generally performed well with three patients identified as
suspicious for type-1 diabetes, who had not been diagnosed
with diabetes. Two patients diagnosed with type-1 diabetes
were placed in the type-2 category, although this was due to
the patients having comorbidities that were not handled in
the MLMs (Medical Logic Modules).

Serhani et al. [29] proposed an adaptive CDSS for patients
with diabetes linked to an intelligent continuous monitor-
ing scheme that handled semi continuous data streams from
smart sensors monitoring blood sugar (BS) and blood pres-
sure (BP). The system was evaluated using 13,650 read-
ings related to BS and BP for 70 patients over a period of
6 months. The system was able to provide advice on lifestyle
and exercise, food intake and medication based on different
combinations of BS and BP readings.

4.1.2   Other clinical domains

The remaining selected papers were for a range of different
clinical domains. Sorenson et al. [30] discussed the use of
a frame-based knowledge representation to construct a bed-
side CDSS for ventilator weaning. The validation consisted
of comparing the CDSS protocol with that of the paper-
based system. A set of more than 2,000 recommendations
were generated for every possible combination of variable
values from the Acute Respiratory Distress Syndrome Net-
work ventilation and oxygenation protocols for maintenance
of mechanical ventilation. All were reviewed by a physi-
cian and respiratory therapist familiar with the protocols.
Separately, the testing and clinical implementation of the
weaning protocol was successfully tested with eight patients.
178 instructions were generated by the system and 80% of
these were accepted by the clinicians and many of the rejec-
tions were mainly unavoidable. The computerized wean-
ing protocol was subsequently integrated into the clinical
environment.

The mobile CDSS GenSupport for congenital clubfoot
treatment [3] supported the registration of patient informa-
tion, supervised the treatment process, and provided advice
during treatment. For the clinical evaluation of the CDSS, a
dataset containing full treatment history of 17 patients with
congenital clubfoot was used. The system provided the same
treatment recommendations as performed by the clinician
on 5 of the 17 patients. For the other patients, the system
advised performing a tenotomy either before (7 of 17) or
after (5 of 17) it was actually performed by the clinician.
With the 7 cases, tenotomy was not performed according
to the recommendations from the Ponseti expert group and

the clinicians provided a sub-optimal treatment. With the
5 cases, the clinicians performed tenotomy earlier than the
CDSS recommended and the clinicians’ actions were most
likely based on factors not documented in the patient data
available in the evaluation.

Kumar et al. [31] proposed a hybrid approach of case-
based reasoning (CBR) and rule-based reasoning (RBR) to
build a CDSS for ICU, as an alternative to a purely rule-
based system. The CDSS was developed by taking a CBR
system and augmenting it with RBR functionality. The sys-
tem was evaluated with real data from six ICU domains from
a hospital in India, populated with five tagged cases that
were very close to an old patient case. The relevance of the
retrieved cases given a test case where retrieval effective-
ness was defined in terms of precision and recall rates was
examined. Similar results were obtained for all the domains
with a maximum precision of 0.85, recall of 0.62, optimum
threshold of 0.335 and k of 0.25, demonstrating the efficacy
of the proposed approach.

Batista-Navarro et al. [32] developed a CDSS to provide
timely information to clinicians about poisoning. The CDSS
accepted signs and symptoms observed from a patient as
input and presented a list of possible poisoning types with
the corresponding management procedures that may be con-
sidered in making the final diagnosis. The CDSS was vali-
dated using 50 test cases, each test case consisting of patient
symptoms and the expected poisoning type. The symptoms
for each test case were entered into the CDSS and 96% of
these cases were given the expected result.

Kunhimangalam  et  al.  [33]  aimed  to  show  that  fuzzy
CDSSs for peripheral neuropathy improve diagnostic and pre-
dictive medical opinions. To evaluate the fuzzy CDSS, 104
NCS (Nerve Conduction Studies) data from Kannur Medical
College in India were tested with normal cases and differ-
ent peripheral neuropathy cases. Comparing the fuzzy CDSS
output with that of a domain expert, the CDSS showed an
accuracy of 93.26%.

Zhang et al. [34] developed a knowledge translation plat-
form as part of a CDSS in DaYi hospital in China in 2013.
As part of the evaluation, a case study related to medication
prescribing was tested. During a 13-month period, 9,596
alerts were detected from 2,667,016 medical orders and
8,609 (89.7%) of the alerts were revised by physicians dem-
onstrating observable behaviour change. The authors con-
cluded that the knowledge translation platform successfully
assisted in translating evidence-based rules into observable
clinician behaviour changes.

Zhang et al. [35] developed a CDSS that supported the
sharing  of  knowledge  among  heterogeneous  healthcare
information systems. The knowledge base consisted of inde-
pendent and reusable knowledge modules (KMs) to meet
core CDSS needs. A semantic web service framework was
developed to identify, access, and leverage these KMs across

1 3720

Health and Technology (2022) 12:713–727

CDSS applications and care settings. The system was vali-
dated with two distinct CDSS applications at different hos-
pitals in China: a clinical pathway management system with
298 patients and a mobile-based emergency triage system
for trauma care in mass casualty incidents with 148 patients.
For both cases, the knowledge base was instantiated with
relevant domain knowledge mainly from standard CPGs and
real patient data from the collaborating hospitals. Domain
experts performed each CDSS task in two modes, i.e., using
their own expertise and using the CDSS and the CDSS had
an overall accuracy of 98.66% and completeness of 96.98%.
Karim et al. [36] developed a Belief Rule-Based Expert
System (BRBES) that can suspect bronchiolitis under uncer-
tainty with increased accuracy. To demonstrate the appli-
cability of the system, data on the signs and symptoms of
200 patients with bronchiolitis (runny nose, fever, feeding,
respiratory distress and wheezing) was collected from a hos-
pital in Bangladesh. The diagnosis of the BRBES system
was compared with that of an expert and was found to be
more reliable based on pathology.

The UbiTriagem CDSS for triage based on web semantics
and ubiquitous computing [37] was evaluated using 30 sce-
narios that already had a correctly documented triage. The
automatic triage assessment from UbiTriagem was correct in
93.3% of the cases and, after adjustments in the underlying
model, in 100% of the cases.

Mohammadhassanzadeh et al. [38] implemented a CDSS
with plausible reasoning mechanisms that applied patterns
from human thought processes, such as generalization, simi-
larity and interpolation. The authors investigated the effi-
ciency of the CDSS loaded with a hepatitis dataset dealing
with different degrees of missing data using two metrics:
(i) Coverage—the ratio of the number of answered queries
(either correct or incorrect) to the total number of queries
and (ii) Correctness – the percentage of answered queries
that were correct. A medical expert used the CDSS to diag-
nose the possibility of survival for each patient. For each
incomplete justification (i.e., for which the system has no
answer), inductive and analogical reasoning was applied to
supplement deductive reasoning with plausible inferences.
Using their best judgment and medical experience, the medi-
cal expert then confirmed or refuted the justifications. The
results showed that plausibly inferred knowledge extended
the coverage of the knowledge base by, on average, 2%,
7%, 12%, and 16% for datasets with, respectively, 5%, 10%,
15%, and 20% of missing values. The authors posit that this
expansion in the knowledge base coverage allowed complex
disease diagnostic queries to be solved that were previously
unresolvable, without losing the correctness of the answers.
Kopanitsa & Semenov [39] developed a first order predicates-
based CDSS to analyze laboratory test results and deliver reports
in natural language to patients. To evaluate the accuracy of the

system, 1,000 randomly generated reports were created in a way
that allowed validation of all 89 decision support algorithms.
The reports were given to two pathology experts to review inde-
pendently and the experts only disagreed with two reports. The
decision support system has been implemented in the Helix lab-
oratory service in Saint-Petersburg, Russia and was in commer-
cial production in 2018 generating about 20,000 reports a day.
Kuo & Fuh [40] created a CDSS (HEALS) to assist cli-
nicians to improve the quality of health examinations. To
evaluate the effectiveness of the system, eight residents of a
Taiwanese hospital with less than two years of clinical experi-
ence were given a set of relevant questions with four to seven
possible answers divided into three levels of correctness —
completely correct, partially correct, and least correct. For each
question, to reduce bias only one or two answers qualified as
completely correct and the others as partially correct or least
correct. Two senior physicians with more than 10 years expe-
rience in health examination validated the questions/answers.
An 18% improvement was achieved using the HEALS CDSS.

4.2   CDSS architectures, technologies and standards

This section addresses RQ2: What architectures, technolo-
gies and standards have been used to develop rules-based
CDSSs? and RQ3: Have the CDSSs been integrated with the
organizational EHR?

4.2.1   CDSS architectures

Velickovski et al. [7] identified different software architec-
tural models used in CDSSs. The main factors that contrib-
ute to the selection of a model are the time and resources
available, the level of integration with other health systems,
and level and ease of reuse of software components. Accord-
ing to the study, there are four different architectural models
with similar technology characteristics to develop a CDSS:

•  The Standalone Model, no integration to an external

Health Information System (HIS) or EHR;

•  The Integrated Model, CDSS is tightly coupled to the HIS

or EHR;

•  The Standard-Based Model, CDSS is separated from the
HIS/EHR and interoperability is achieved through the use
of computer-interpretable guidelines (CIGs);

•  The Service-Oriented Model, again the CDSS is sepa-
rated from the HIS/EHR, but is integrated using service-
based interfaces. The interfaces encode the clinical data
and recommendations using ontologies and vocabular-
ies. Here, standardization is based on the data transferred
between the HIS and CDSS instead of the clinical rules
executed by the CDSS as in standard-based systems.

1 3Health and Technology (2022) 12:713–727

721

Due to the growing support for mHealth, we were also
particularly interested in CDSS support for mobile/handheld
devices and use of the cloud. The majority of papers were
Standalone, however, five were Service-Oriented [28, 34,
35, 37, 38]. In addition, five of the selected papers supported
mobile/handheld device access [3, 28, 29, 35, 37]. Only one
used the cloud [28].

4.2.2   CDSS technologies

A range of rules/inference engines were used in the selected
papers. Some researchers developed their own engines [30,
31, 33, 36, 38, 39]. Other researchers used existing technolo-
gies; for example:

•  The reasoning engine Pellet was used by [35, 37].
•  An inference engine based on ANTLR (ANother Tool
for Language Recognition) was used to develop a CDSS
rules engine for drug use [34].

•  The Eval3RulesEngine developed for mobiles based on

the external library Eval3 was used by [3].

•  Jess, a rule engine and scripting environment written
entirely in Java, was used by [29]. Rules were specified
using Common LISP (CLISP) type syntax and readings
are inferred using Jess engine to generate advice for dia-
betes.

•  HL7 Arden syntax was used to develop the rules for a
cloud-based CDSS for diabetes [28]. Each diabetes rule
was represented as an individual MLM and converted
into a compiled C# class for execution by the Knowledge
Inference Engine. Each MLM had a counterpart C# class.
•  CLIPS (C Language Integrated Production System), a
rule-based programming language for creating expert
systems, was used to develop a CDSS rules engine for
poisoning diagnosis [32].

4.2.3   CDSS standards

•  HL7 CDA (Clinical Document Architecture), an exchange

model for clinical documents, was used by [28].

Surprisingly, no papers used HL7 FHIR.

4.2.4   EHR integration

This  subsection  addresses  RQ3:  Have  the  CDSSs  been
integrated with the organizational EHR? Without having
to duplicate patient data, which can lead to errors, ideally
CDSSs should be integrated with an EHR system. However,
only 2 of the selected papers were integrated with an EHR:

•  The cloud-based CDSS for diabetes [28] was integrated
with the EHR at St Mary’s Hospital in Korea by convert-
ing data from HL7 CDA to HL7 vMR format using the
adapter interoperability engine (ARIEN).

•  The CDSS to check drug prescribing [34] was integrated

with the EHR at DaYi Hospital in China.

4.3   CDSS knowledge representation

This subsection addresses RQ4: How has knowledge been
represented in rules-based CDSSs? From the papers identi-
fied, clinical knowledge representation were implemented in
a range of ways. Ontology was the most common knowledge
representation method identified in 6 of the selected papers.
An ontology is normally used to represent:

•  Domain knowledge including diagnostic knowledge that
defines diagnostic rules and/or drug use rules [19, 28, 34,
35, 37, 38]

•  Clinical guidelines including recommended care proto-

cols for clinical problems [19, 34, 37, 38]

•  Patient semantic profile including patient details entered
by patients or clinicians [19, 28, 35, 38] and patient activ-
ities [28].

Only a small number of papers adopted standards and these
tended to be HL7 standards:

•  HL7 Arden Syntax, a formalism for clinical knowledge rep-
resentation, and HL7 GELLO, to build queries to extract
and manipulate data from medical data, was used to build
a cloud-based CDSS for diabetes [28].

•  HL7 InfoButton, a standard mechanism for CDSSs to
request context-specific clinical knowledge from online
resources, was used for the drug use CDSS [34].

•  HL7 vMR (Virtual Medical Record) is a data model for
representing the data that is analyzed and/or produced
by a CDSS engine. HL7 vMR was used by [35] for their
shareable CDSS system and for the cloud-based CDSS
for diabetes [28].

From the papers identified, no papers used existing ontolo-
gies such as those listed in the Background section earlier and
instead created bespoke ontologies to represent the knowledge
they required. Zhang et al. [34] developed a unified ontology
containing diagnostic knowledge, treatment knowledge and
pharmaceutical knowledge. [38] used an ontology to repre-
sent patient data in different formats and databases, explicit
medical knowledge (available texts, journals, and clinical
guidelines) and tacit medical knowledge and experiences of
domain experts. Kuo and Fuh [40] created a custom health
examination ontology to represent health examination data
such as physical examination results and lab data. Sherimon
and Krishnan [19] developed the Diabetic Patient Clinical
Analysis Ontology to represent all the information required to
analyze patient information, compute risk scores and suggest

1 3722

Health and Technology (2022) 12:713–727

treatment procedures according to given clinical guidelines.
Hussain et al. [28] used an ontology to represent data from
sensors and information retrieved from social media, activity
history, user profile information, clinical data, expert knowl-
edge, and expert recommendations. The Knowledge Reposi-
tory also contained clinical information using HL7 Arden
Syntax. Wunsch et al. [37] created a custom ontology based
on the Manchester Triage System protocol and Zhang et al.
[35] created custom ontologies of real-time patient data and
semantic domain knowledge base containing static CDSS
knowledge and executable CDSS rules.

OWL was the most used ontology language identified
in this study [19, 28, 35, 37, 38] while one paper did not
explicitly specify what ontology language was used [34].
Protégé was used by [35, 37] to create their ontologies and
Arden syntax was used by [28] to represent expert knowl-
edge and recommendations.

In terms of knowledge repository, a range of technolo-
gies were used. Hussain et al. [28] used Windows Azure
and SQL Azure while Wunch et al. [37] and Kuo and Fuh
[40] used a MySQL database. Zhang et al. [34] employed
Microsoft’s Entity Framework to generate a knowledge base
schema from an ontology model, which was then stored
in a SQL server database. When parsing the ontologies,
Wunch et al. [37] and Kuo and Fuh [40] created a custom
module written in Java and Zhang et al. [35] used Apache
Jena while the other papers did not provide specific details,
which may indicate the parsing was part of their bespoke
inference engine.

Apart from the use of ontologies, XML and Common
LISP (CLISP) were also used for knowledge representation.
Chen and Skjelvik [3] represented the guidelines for clubfoot
treatment in a decision tree implemented in XML. Kumar
et al. [31] used XML as their rule base format. Serhani et al.
[29] used CLISP to implement their rules for Jess inference
engine.

Other methods were also used for knowledge representa-
tion. Kunhimangalam et al. [33] implemented knowledge as
fuzzy rules. Karim et al. [36] used knowledge representa-
tion based around fuzzy logic to represent different types of
uncertain data related to the signs and symptoms of bronchi-
olitis, which was then converted into conventional IF–THEN
rules. Batista-Navarro et al. [32] adopted knowledge from
Algorithms of Common Poisonings Part 1 and represented
the knowledge as rules stored as CLIPS files in the file sys-
tem. Kopanitsa and Semenov [39] developed a knowledge
representation language based on the first order predicate
logic. Sorenson et al. [30] used a frame to represent knowl-
edge where a frame included a list of findings necessary to
make a decision or carry out an action, and a logic or math-
ematical statement to determine its output.

5   Discussion

5.1   Evaluation

Addressing RQ1: How have the rules-based CDSSs been
evaluated in terms of clinical outcomes? One of the key
criteria for the selected papers in this review was that they
had to contain an evaluation of clinical outcomes. No RCT
or quasi-experimental studies were identified and many
of the papers only contained small-scale evaluations. No
papers examined the costs of system implementation or
carried out any form of cost/benefit analysis.

In terms of clinical outcomes, some papers used real-time
patient data while others used test data, either based on exist-
ing patient data, published test datasets or randomly generated
data. Surprisingly many of the patient studies were relatively
small. The largest study was for the OntoDiabetic CDSS [19],
which was evaluated with 250 patients with risk of CVD, dia-
betic nephropathy and hypertension. Other real-time patient
studies included the cloud-based CDSS [28] that was evalu-
ated with test data from 100 patients: 20 with type-1 diabe-
tes, 40 with type-2 diabetes mellitus, and 40 with suspicions
for diabetes but no specific diagnosis; the adaptive CDSS for
patients with diabetes linked to an intelligent continuous mon-
itoring scheme [29] evaluated using 13,650 readings related to
BS and BP for 70 patients over a period of 6 months; and the
frame-based CDSS for ventilator weaning [30] was evaluated
with eight patients.

Studies that used test patient data for evaluation included
the belief rule-based CDSS for bronchiolitis [36] which
used data from 200 patients with bronchiolitis and com-
pared with that of an expert; the fuzzy CDSS for diagnos-
tic and predictive medical opinions, which used a dataset
of 104 nerve studies and the output compared with that
of  a  domain  expert;  the  CDSS  for  poisoning  diagnosis
[32] which used 50 test cases, each test case consisting
of patient symptoms and the expected poisoning type; the
mobile CDSS for congenital clubfoot treatment [3] which
used a dataset containing treatment history of 17 patients
with congenital clubfoot; the CDSS for ICU that adopted
CBR and RBR [31], which used real data from six ICU
domains using five tagged cases that were very close to an
old patient case; and the CDSS using plausible reasoning
mechanisms [38], which used a hepatitis dataset dealing
with different degrees of missing data, although no indica-
tion was given on the size of the dataset.

Other studies used other datasets including the knowl-
edge translation platform for medication prescribing [34],
which examined the number of alerts raised by the system
and how many prescriptions were modified based on the
alert; the UbiTriagem CDSS for triage [37], which used 30

1 3Health and Technology (2022) 12:713–727

723

scenarios that already had a correctly documented triage;
and the CDSS to analyze laboratory test results [39], which
randomly generated 1,000 reports and asked two pathology
experts to independently verify the reports.

5.2   CDSS standards

Addressing RQ2: What architectures, technologies and stand-
ards have been used to develop rules-based CDSSs? In terms
of architectures, while there are various models proposed
the majority of papers were Standalone and only five were
Service-Oriented. None of the included papers used the Inte-
grated or Standards-based model. Standards are very impor-
tant in the development of systems generally and can lead
to faster development times, enhanced reliability, enhanced
security and can result in safer software. In particular, despite
three decades of development CDSSs still suffer from inter-
operability issues. Many CDSSs exist as standalone systems
or as systems that cannot communicate effectively with other
systems [41]. Interoperability standards, such as FHIR, are
continuously being developed and improved. These standards
are already being utilized in commercial EHR systems and
government agencies and medical organizations are support-
ing and some even mandating the use of these interoperability
standards in health systems [42].

From the review it is clear that health standards are not
widely adopted, with the exception of HL7. Only 3 of the
15 selected papers used recognised CDSS standards [28, 34,
35]. All the standards used were from HL7 including Arden,
GELLO, InfoButton, vMR and CDA. None of the selected
papers used FHIR or openEHR. This lack of use of interop-
erability supports the view of other researchers (eg. [41]).

The cloud also offers a solution to interoperability and
cloud  systems  tend  to  conform  to  an  open  architecture,
newer standards, and more flexible connectivity to other sys-
tems. Only one of the 15 selected papers [28] used the cloud.

5.3   Mobile

It is argued that mHealth is changing the way healthcare can
be delivered beyond the use of apps for medicine, health and
fitness and well-being of patients to use of remote monitoring
and consultation, telemedicine and patient management and
in our case clinical decision support. This change is driven
by increased mobile device penetration and capabilities along
with growing clinician and patient demand [48]. A mHealth-
based CDSS offers the potential to reduce medical errors and
improve the quality and efficiency of healthcare [49]. Several
exploratory studies have been conducted on the use of mobile
devices to deliver eHealth content and some had positive out-
comes. But one of the issues with this approach is that the
majority of mobile applications on Google Play and the Apple
Store are not following any health guidelines and are usually

not evidence based [50]. A review in 2014 suggested actual
application of such systems to date has been limited [51].
We were interested to determine whether the landscape had
changed and more mobile CDSSs were being developed and
more evidence of their usefulness was available. In this review,
5 of the 15 selected papers supported mobile/handheld device
access ([3, 28, 29, 35, 37]) and, as noted previously, none of
these evaluations used RCT or quasi-experimental methodolo-
gies so like the 2014 review, evidence remains limited.

5.4   EHR integration

Addressing RQ3: Have the CDSSs been integrated with the
organizational EHR? CDSSs that have been integrated into
EHR platforms have been shown to enhance the quality of
clinical care and improve patient outcomes and their accept-
ance by clinicians can be significantly improved if they are
well integrated with the EHRs [43–46]. The integration of
these systems also allows previous patient data to be accessed
by the CDSS for its own inferencing needs and to save any
data the CDSS may generate to be saved back into the EHR.
This helps in avoiding redundant data entry and errors due
to missing or incorrect data being entered. The integration
between the two systems also has several other advantages
such as single log on and consistent user interfaces [47].
Despite these benefits, only 2 of the 15 selected papers devel-
oped a CDSS that integrated with an EHR.

5.5   Knowledge representation

Addressing RQ4: How has knowledge been represented in
rules-based CDSSs? Although the use of ontologies has been
identified to have the potential to improve flexibility and reus-
ability of knowledge, only 6 papers in the review actually
used an ontology and others used alternatives such as XML,,
CLISP, HL7 vMR format and first order predicate logic. There
is no clear justification in the papers discussed as to why such
an approach was taken, however, perhaps the knowledge to
be stored was sufficiently simple that an ontology was not
needed. There is also no clear justification on why creating a
bespoke ontology to fit the domain was preferred compared
to using existing ontologies. Our assumption is the choice
may be due to personal preference by the programmers or
knowledge engineers. Knowledge representation using OWL
was the most commonly used ontology language identified
in this study while Prot´eg´e was the only ontology editor
used by the studies for its user-friendly capabilities in creating
and visualizing ontologies. To store the knowledge, relational
databases such as MySQL and SQL Server are commonly
used for its security compared to XML. When parsing ontolo-
gies, the papers indicated the most common approach was
to hardcode it into the CDSS followed by creating a custom
module usually written in Java and using Apache Jena.

1 3724

6   Conclusions

Rule-based systems are extensively used in CDSSs possibly
due to the flexibility they offer for a system that is under con-
stant change. The increase in generated information, together
with the increase in evidence-based studies makes it very chal-
lenging to continue building systems manually. The flexibility
and moderate time for health experts to develop a CDSS is
certainly one of the main reasons why rule-based systems are
so widely used in smaller studies (usually IF–THEN rules),
this is further supported by the fact that from the 341 possible
relevant papers that were fully reviewed 114 were relevant
and composed of primarily small studies, but when looking
at rigorous evaluation, only 15 of those papers were in fact
shortlisted and included in this study.

There were a number of interesting findings from this
study. From the 15 papers shortlisted, there were no RCT
or quasi-experimental studies and many of the papers only
contained small-scale evaluations. No papers examined the
costs of system implementation or carried out any form of
cost/benefit analysis. Despite the fact that ontologies provide
many advantages for representing domain knowledge, only 6
of the shortlisted papers used ontologies to represent domain
knowledge. Given the obvious advantages to integrating the
CDSS with the EHR system, only 2 of the papers described
CDSSs that integrated with an EHR system and in general
interoperability was not addressed. Technology standards are
very important in the development of systems and can lead
to faster development times, enhanced reliability, enhanced
security and can result in safer software, however, only 3 of
the shortlisted papers used recognised healthcare technology
standards (and all these were HL7 standards).

Finally, as mHealth is changing the way healthcare is
delivered, driven by increased mobile device penetration and
capabilities along with growing clinician and patient demand,
and an mHealth-based CDSS offers the potential to reduce
medical errors and improve the quality and efficiency of
healthcare, only 5 of the shortlisted papers supported mobile
use. This point has also been noted by other researchers; for
example, [49]. Moreover, given that the cloud does not only
provide on-demand services but also offers high availabil-
ity, reliability, vast scalability, a cheaper environment for
computing, and we are seeing a move in healthcare to trans-
form and shift IT structure towards the cloud, we might have
expected to see more CDSSs using the cloud, however, out of
the 15 selected papers only 1 paper used the cloud.

There were several relatively new non-knowledge based
approaches briefly discussed in this paper that may address
some of the complexities involved in decision making in
healthcare. The automation of rule generation from analyz-
ing a vast volume of evidence-based research and the cor-
relation to each patients’ health history can provide a more

Health and Technology (2022) 12:713–727

enriched diagnostic/prognostic tool for the future. With the
increase in evidence-based clinical trials and in some cases
the automatic translation to clinical knowledge it is possible
that scalable nonknowledge based approaches may be better
suited to tackle the increased complexity.

Recommendations arising from these findings suggest the

following (see Fig. 3):

•  At the outset of the development of the CDSS, a meth-
odology has to be produced for how the system will be
evaluated to demonstrate that the CDSS is effective and
provides clear clinical benefits and cost benefits.

•  Interoperability has to be addressed from the start of the
development to ensure that the CDSS integrates with the
EHR as well as other healthcare information systems.
•  The adoption of relevant healthcare technology stand-
ards should underpin the development of the CDSS to
enhance reliability, enhance security and provide safer
software among other benefits.

•  Ontologies facilitate standardization, flexibility for change,
and promote sharing and reusability of medical knowledge
between CDSS systems and their use should be considered
in the development of a CDSS. The adoption of relevant
publicly available ontologies should be considered first
before any new ontologies are created.

•  Consideration should be given to mobile usage given
increased  mobile  device  penetration  and  capabilities
along with growing clinician and patient demand.

•  Consideration should be given to whether the cloud pro-

vides any suitable services for the CDSS.

•  As well as the use of traditional knowledge-based approaches
to CDSS development, consideration should be given to the
use of non knowledge based approaches where this may be
more appropriate.

While these recommendations are not novel the find-
ings from this review suggest these recommendations are
not being addressed in the development of CDSSs. It is
difficult to gauge from the papers why this might be the
case but possible reasons may be the additional costs of
addressing  interoperability  or  using  recognised  CDSS
standards; initial developments may only be prototypes
to prove the underlying concept with a more extensive
implementation  to  follow  if  the  business  case  can  be
made; experimental studies can be difficult to undertake
and require careful planning and approval from a range of
different parties and may be considered beyond the scope
of the project; projects may not have the appropriate staff
for development or evaluation (eg [52, 53].).

In terms of limitations of the study, the review is based on
a limited number of electronic databases and the inclusion
of additional databases may identify further relevant papers.

1 3Health and Technology (2022) 12:713–727

725

Fig. 3   Rule Based CDSS Rec-
ommendations

In addition, the majority of the work reviewed consisted of
projects that were academic oriented, open sourced, ven-
dor agnostic. This implies that commercial systems that are
closed sourced have not been captured in this study. This may
provide some explanation as one of the factors to the limited
use of standards found and interoperability in this study.

Funding  Not applicable.

Data availability  Not applicable.

Code availability  Not applicable.

Declarations

Ethics approval  Not applicable.

Consent to participate  Not applicable.

Consent for publication  Not applicable.

Conflicts of interest  Not applicable.

Open Access  This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source,
provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article are
included in the article's Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in
the article's Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will

need to obtain permission directly from the copyright holder. To view a
copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

References

  1.  Garcia  EV,  Klein  JL,  Taylor  AT.  Clinical  decision  support
systems  in  myocardial  perfusion  imaging.  J  Nucl  Cardiol.
2014;21:427–39.

  2.  Aleksovska-Stojkovska, L, Loskovska, S. Clinical decision sup-
port systems: Medical knowledge acquisition and representation
methods. In: Electro/Information Technology (EIT), 2010 IEEE
Int Conf on IEEE. 2010. p. 1–6.

  3.  Chen, W, Skjelvik, D. A mobile clinical decision support system

for clubfoot treatment. Artif Intell Med. 2009:181–185.
  4.  S´eroussi B, Beux PL, Venot A. Medical diagnostic decision sup-
port. Medical Informatics, e-Health. Springer. 2014. p. 141–166.
  5.  Berner ES, Lande ES. Overview of clinical decision support sys-
tems. Clinical decision support systems: Springer; 2016. p. 1–17.
  6.  Kim J-K, Lee J-S, Park J-S, Lim J-S, Lee J-S, Jung J-S. Adap-
tive mining prediction model for content recommendation to
coronary heart disease patients. Clust Comput. 2014;17:881–91.
  7.  Velickovski  F,  Ceccaroni  L,  Roca  J,  Burgos  F,  Galdiz  JB,
Marina N, Lluch-Ariet M. Clinical decision support systems
(cdss) for preventive management of copd patients, J Transl
Med. 2014;12 S9. https:// doi. org/ 10. 1186/ 1479- 5876- 12- S2- S9.
  8.  Lobach DF, Johns EB, Halpenny B, Saunders TA, Brzozowski
J, Fiol GD, Berry DL, Braun IM, Finn K, Wolfe J, Abrahm
JL, Cooley ME. Increasing complexity in rule-based clinical
decision support: The symptom assessment and management
intervention, JMIR Med Inform. 2016;4 e36. doi:v4i4e36[pii].
  9.  Peiffer-Smadja N, Rawson T, Ahmad R, Buchard A, Georgiou P,
Lescure F-X, Birgand G, Holmes A. Machine learning for clini-
cal decision support in infectious diseases: a narrative review of
current applications. Clin Microbiol Infect. 2020;26:584–595.
https:// doi. org/ 10. 1016/j. cmi. 2019. 09. 009.

1 3726

Health and Technology (2022) 12:713–727

 10.  Nadkarni  PM.  Infrastructure  for  complex  clinical  decision
support: Rule engines. Metadata-driven software systems in
biomedicine. Springer. 2011. p. 143–155.

 11.  Musen MA, Middleton B, Greenes RA. Clinical decision-support
systems. Biomedical informatics: Springer; 2014. p. 643–74.
 12.  Rattanasawad T, Saikaew KR, Buranarach M, Supnithi T. A
review and comparison of rule languages and rule-based infer-
ence engines for the semantic web. In: Computer Science and
Engineering Conference (ICSEC), 2013 Int IEEE. 2013. p. 1–6.
 13.  Loya SR, Kawamoto K, Chatwin C, Huser V. Service oriented
architecture for clinical decision support: a systematic review
and future directions, J Med Syst. 2014;38(12).

 14.  Boxwala AA, Peleg M, Tu S, Ogunyemi O, Zeng QT, Wang
D, Patel VL, Greenes RA, Shortliffe EH. Glif3: a representa-
tion format for sharable computer-interpretable clinical practice
guidelines. J Biomed Inform. 2004;37:47–161.

 15.  Ciccarese P, Kumar A, Quaglini S. New-guide: a new approach
to representing clinical practice guidelines. Adv Clin Knowl
Manag. 2002:15–18.

 16.  Sutton DR, Fox J. The syntax and semantics of the pro forma guide-
line modeling language. J Am Med Inform Assoc. 2003;10:433–43.
 17.  Saripalle R, Runyan C, Russell M. Using hl7 fhir to achieve inter-
operability in patient health record. J Biomed Inform. 2019;94.

 18.  Alharbi RF, Berri J, El-Masri S. Ontology based clinical decision
support system for diabetes diagnostic. In: Sci Inf Conf (SAI),
2015. IEEE. 2015. p. 597–602.

 19.  Sherimon P, Krishnan R. Ontodiabetic: an ontology-based clini-
cal decision support system for diabetic patients. Arab J Sci Eng.
2016;41:1145–60.

 20.  Chiarugi F, Colantonio S, Emmanouilidou D, Martinelli M, Moroni
D, Salvetti O. Decision support in heart failure through processing
of electro and echocardiograms. Artif Intell Med. 2010;50:95–104.
 21.  Gressling T. 88 ontologies and inferencing. In: Data Science in

Chemistry. De Gruyter. 2020. p. 429–435.

 22.  Chandrasekaran B, Josephson JR, Benjamins VR. What are ontol-
ogies, and why do we need them? IEEE Intelligent Systems and
their applications. 1999;14:20–6.

 23.  Durán-Muñoz I, Bautista-Zambrana MR. Applying ontologies
to terminology: Advantages and disadvantages. Hermes-J Lang
Commun Business. 2013. p. 65–77.

 24.  Douali N, Vanel JM, Roo JD, Jaulent M-C. New semantic web
rules and new medical reasoning framework. In: Instrumentation
and Measurement Technology Conference (I2MTC), 2013 IEEE
Int. IEEE. 2013. p. 1332–1335.

 25.  Kashyap V, Hongsermeier T. Can semantic web technologies
enable translational medicine? Semantic Web. 2007. p. 249–279.
 26.  Lombard M, Snyder-Duch J, Bracken CC. Content analysis in
mass communication: Assessment and reporting of intercoder
reliability. Hum Commun Res. 2002;28:587–604.

 27.  Krippendorff K. Content analysis: An introduction to its meth-

odology. SAGE. 2013.

 28.  Hussain M, Khattak A, Khan W, Fatima I, Amin M, Pervez Z,
Batool R, Saleem M, Afzal M, Faheem M. Cloud-based smart
cdss for chronic diseases. Heal Technol. 2013;3:153–75.

 29.  Serhani MA, Benharref A, Nujum AR. An adaptive expert system
for automated advices generation-based semi-continuous m-health
monitoring. In: International Conference on Brain Informatics and
Health. Springer. 2014. p. 388–399.

 30.  Sorenson D, Grissom C, Carpenter L, Austin A, Sward K, Napoli
L, Warner HR, Morris AHRCR. in Critical Care Investigators,
A frame-based representation for a bedside ventilator weaning
protocol. J Biomed Inform. 2008;41:461–8.

 31.  Kumar KA, Singh Y, Sanyal S. Hybrid approach using case-
based  reasoning  and  rule-based  reasoning  for  domain  inde-
pendent  clinical  decision  support  in  icu.  Expert  Syst  Appl.
2009;36:65–71.

 32.  Batista-Navarro RTB, Bandojo DA, Gatapia MJK, Santos RNC,
Marcelo AB, Panganiban LCR, Naval PC. Esp: An expert sys-
tem for poisoning diagnosis and management. Inform Health Soc
Care. 2010;35:53–63.

 33.  Kunhimangalam R, Ovallath S, Joseph PK. A clinical decision
support system with an integrated emr for diagnosis of peripheral
neuropathy. J Med Syst. 2014;38.

 34.  Zhang Y, Li H, Duan H, Zhao Y. Mobilizing clinical decision
support to facilitate knowledge translation: a case study in China.
Comput Biol Med. 2015;60:40–50.

 35.  Zhang Y-F, Gou L, Tian Y, Li T-C, Zhang M, Li J-S. Design and
development of a sharable clinical decision support system based
on a semantic web service framework. J Med Syst. 2016;40:118.
 36.  Karim R, Hossain MS, Khalid MS, Mustafa R, Bhuiyan TA. A
belief rule-based expert system to assess bronchiolitis suspicion
from signs and symptoms under uncertainty. In: Proceedings of
SAI Intelligent Systems Conference, Springer. 2016. p. 331–343.
 37.  Wunsch G, da Costa CA, Righi RR. A semantic-based model for
triage patients in emergency departments. J Med Syst. 2017;41:65.
 38.  Mohammadhassanzadeh H, Woensel WV, Abidi SR, Abidi SSR.
Semantics-based plausible reasoning to extend the knowledge
coverage of medical knowledge bases for improved clinical deci-
sion support. BioData mining. 2017;10:7.

 39.  Kopanitsa G, Semenov I. Patient facing decision support system
for interpretation of laboratory test results. BMC Med Inform
Decis Mak. 2018;18:68.

 40.  Kuo KL, Fuh CS. A health examination system integrated with
clinical decision support system. J Med Syst. 2010;34:829–42.
 41.  Sutton RT, Pincock D, Baumgart DC, Sadowski DC, Fedorak RN,
Kroeker KI. An overview of clinical decision support systems: benefits,
risks, and strategies for success. NPJ digital medicine. 2020;3:1–10.

 42.  European Commission. Recommendation on a European electronic
health record exchange format. 2019. https:// digit al- strat egy. ec. europa.
eu/ en/ libra ry/ recom menda tion- europ ean- elect ronic- health- record-
excha nge- format (last accessed 28.03.2022).

 43.  Wulff A. Haarbrandt B, Tute E, Marschollek M, Beerbaum P,
Jack T. An interoperable clinical decision-support system for early
detection of sirs in pediatric intensive care using openehr, Artifi-
cial intelligence in medicine. 2018;89:10–23.

 44.  Adel E, El-Sappagh S, Barakat S, Elmogy M. Distributed elec-
tronic health record based on semantic interoperability using
fuzzy ontology: a survey. Int J Comput Appl. 2018;40:223–41.

 45.  Garcelon N, Burgun A, Salomon R, Neuraz A. Electronic health
records for the diagnosis of rare diseases. Kidney Int. 2020;97:676–86.
 46.  Ndlovu K, Mars M, Scott RE. Interoperability frameworks linking
mhealth applications to electronic record systems. BMC Health
Serv Res. 2021;21:1–10.

 47.  Shah H, Krishnan G, Williams P, Vogler A, Allard RD, Interop-
erability NPM, integration considerations for a process-oriented
clinical decision support system, in,. IEEE World Congress on
Services. IEEE. 2011;2011:437–42.

 48.  Paglialonga A, Patel AA, Pinto E, Mugambi D, Keshavjee K. The
healthcare system perspective in mhealth, in: m Health Current
and Future Applications, Springer. 2019. p. 127–142.

 49.  Timotijevic L, Hodgkins CE, Banks A, Rusconi P, Egan B, Peacock
M, Seiss E, Touray MM, Gage H, Pellicano C, Spalletta G. Designing
a mhealth clinical decision support system for parkinson’s disease: a
theoretically grounded user needs approach. BMC Med Inform Decis
Mak. 2020;20:1–21.

 50.  Eckhoff RP, Kizakevich PN, Bakalov V, Zhang Y, Bryant SP,
Hobbs MA. A platform to build mobile health apps: The per-
sonal health intervention toolkit (phit). JMIR Mhealth Uhealth.
2015;3:46. https:// doi. org/ 10. 2196/ mheal th. 4202.

 51.  Jones SS, Rudin RS, Perry T, Shekelle PG. Health information
technology: an updated systematic review with a focus on mean-
ingful use. Ann Intern Med. 2014;160:48–54.

1 3Health and Technology (2022) 12:713–727

727

 52.  Greaves F, Joshi I, Campbell M, Roberts S, Patel N, Powell J.
What is an appropriate level of evidence for a digital health inter-
vention? The Lancet. 2018;392(10165):2665–7.

 53.  Greenhalgh T, Wherton J, Papoutsi C, Lynch J, Hughes G, Hinder
S, Fahy N, Procter R, Shaw S. Beyond adoption: a new frame-
work for theorizing and evaluating nonadoption, abandonment,
and challenges to the scale-up, spread, and sustainability of health
and care technologies. J Med Internet Res. 2017;19(11).

Publisher's  Note  Springer  Nature  remains  neutral  with  regard  to
jurisdictional claims in published maps and institutional affiliations.

To be used for all articles, including articles with biological applications.

1 3
