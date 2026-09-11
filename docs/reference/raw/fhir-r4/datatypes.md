---
id: datatypes
title: Data Types
source_url: https://hl7.org/fhir/R4/datatypes.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:18Z'
sha256: c886eaf9091361c162586d90232dbb27f780fb9b6ed0ac2a99b4b2c71ee5c7da
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/datatypes.html) [R4B](http://hl7.org/fhir/R4B/datatypes.html) **R4** [R3](http://hl7.org/fhir/STU3/datatypes.html) [R2](http://hl7.org/fhir/DSTU2/datatypes.html)

- [Data Types](#)
- [Examples](datatypes-examples.html)
- [Detailed Descriptions](datatypes-definitions.html)
- [Mappings](datatypes-mappings.html)
- [Profiles and Extensions](datatypes-extras.html)
- [R3 Conversions](datatypes-version-maps.html)

# 2.24.0 Data Types

|  |  |  |
| --- | --- | --- |
| [FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): Normative | [Standards Status](versions.html#std-process): [Partially Normative](versions.html#std-process) |

|  |  |
| --- | --- |
|  | This page has been approved as part of an [ANSI](https://www.ansi.org/)  standard. See the [Infrastructure](ansi-infrastructure.html) Package for further details. |

The FHIR specification defines a set of data types that are used for the
resource elements. There are four categories of data types:

1. Simple / primitive types, which are single elements with a primitive value ([below](#primitive))
2. General-purpose complex types, which are re-usable clusters of elements ([below](#complex))
3. Metadata types: A set of types for use with metadata resources
4. Special purpose data types - defined elsewhere in the specification for specific usages

This page describes the general-purpose data types (categories 1 and 2).

**Data Types Summary**.

Legend: see [Standards Status Colors](versions.html#std-process)

**Primitive Types**

**General-Purpose Data types**

**Metadata Types**

**Special Purpose Data types**

A [limited set](extensibility.html#list) of these data types may
appear in extensions. All data types (including primitives) may have
extensions, but only the following data types may include [Modifier Extensions](extensibility.html#modifier):

- [Timing](datatypes.html#timing)
- [Dosage](dosage.html#Dosage)
- [ElementDefinition](elementdefinition.html#ElementDefinition)

## 2.24.0.1 Primitive Types

The following table describes the primitive types that are used in this specification. Primitive types are those with only a value, and no additional elements as children (though, like
all types, they have [extensions](extensibility.html)). See also the [Examples](datatypes-examples.html#primitives).

|  |  |  |  |
| --- | --- | --- | --- |
| **Primitive Types** | | | |
| FHIR Name | Value Domain | XML Representation | JSON representation |
| boolean | true | false | xs:boolean, except that **0 and 1 are not valid values** | JSON boolean (true or false) |
|  | Regex: `true|false` | | |
| integer | A signed integer in the range −2,147,483,648..2,147,483,647 (32-bit; for larger values, use decimal) | xs:int, except that **leading 0 digits are not allowed** | JSON number (with no decimal point) |
|  | Regex: `[0]|[-+]?[1-9][0-9]*` | | |
| string | A sequence of Unicode characters | xs:string | JSON String |
|  | Note that strings SHALL NOT exceed 1MB (1024\*1024 characters) in size. Strings SHOULD not contain Unicode character points below 32, except for u0009 (horizontal tab), u0010 (carriage return) and u0013 (line feed). Leading and Trailing whitespace is allowed, but SHOULD be [removed when using the XML format](xml.html#whitespace). Note: This means that a string that consists only of whitespace could be trimmed to nothing, which would be treated as an invalid element value. Therefore strings SHOULD always contain non-whitespace content | | |
|  | This data type can be [bound](terminologies.html#string) to a [ValueSet](valueset.html) | | |
|  | Regex: `[ \r\n\t\S]+` (see notes below) | | |
| decimal | Rational numbers that have a decimal representation. See below about the precision of the number | union of xs:decimal and xs:double (see below for limitations) | A JSON number (see below for limitations) |
|  | Regex: `-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?` | | |
| uri | A Uniform Resource Identifier Reference ([RFC 3986](http://tools.ietf.org/html/rfc3986) ). Note: URIs are case sensitive. For UUID (urn:uuid:53fefa32-fcbb-4ff8-8a92-55ee120877b7) use all lowercase | xs:anyURI | A JSON string - a URI |
|  | Regex: `\S*` (This regex is very permissive, but URIs must be valid. Implementers are welcome to use more specific regex statements for a URI in specific contexts) | | |
|  | URIs can be absolute or relative, and may have an optional fragment identifier  This data type can be [bound](terminologies.html#string) to a [ValueSet](valueset.html) | | |
| url | A Uniform Resource Locator ([RFC 1738](http://tools.ietf.org/html/rfc1738) ). Note URLs are accessed directly using the specified protocol. Common URL protocols are `http{s}:`, `ftp:`, `mailto:` and `mllp:`, though many others are defined | xs:anyURI | A JSON string - a URL |
| canonical | A URI that refers to a [resource by its canonical URL](references.html#canonical) ([resources with a `url` property](references.html#canonical-list)). The `canonical` type differs from a `uri` in that it has special meaning in this specification, and in that it may have a version appended, separated by a vertical bar (|). Note that the type `canonical` is not used for the actual canonical URLs that are the target of these references, but for the URIs that refer to them, and may have the version suffix in them. Like other URIs, elements of type `canonical` may also have #fragment references | xs:anyURI | A JSON string - a canonical URL |
| base64Binary | A stream of bytes, base64 encoded ([RFC 4648](http://tools.ietf.org/html/rfc4648) ) | xs:base64Binary | A JSON string - base64 content |
|  | Regex: `(\s*([0-9a-zA-Z\+\=]){4}\s*)+` | | |
|  | There is no specified upper limit to the size of a binary, but systems will have to impose some implementation based limit to the size they support. This should be clearly documented, though there is no computable for this at this time | | |
| instant | An instant in time in the format YYYY-MM-DDThh:mm:ss.sss+zz:zz (e.g. 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z). The time SHALL specified at least to the second and SHALL include a time zone. Note: This is intended for when precisely observed times are required (typically system logs etc.), and not human-reported times - for those, use date or dateTime (which can be as precise as `instant`, but is not required to be). `instant` is a more constrained dateTime | xs:dateTime | A JSON string - an xs:dateTime |
|  | Note: This type is for system times, not human times (see date and dateTime below). | | |
|  | Regex: `([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))` | | |
| date | A date, or partial date (e.g. just year or year + month) as used in human communication. The format is YYYY, YYYY-MM, or YYYY-MM-DD, e.g. 2018, 1973-06, or 1905-08-23. **There SHALL be no time zone**. Dates SHALL be valid dates | union of xs:date, xs:gYearMonth, xs:gYear | A JSON string - a union of xs:date, xs:gYearMonth, xs:gYear |
|  | Regex: `([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1]))?)?` | | |
| dateTime | A date, date-time or partial date (e.g. just year or year + month) as used in human communication. The format is YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDThh:mm:ss+zz:zz, e.g. 2018, 1973-06, 1905-08-23, 2015-02-07T13:28:17-05:00 or 2017-01-01T00:00:00.000Z. If hours and minutes are specified, a time zone SHALL be populated. Seconds must be provided due to schema type constraints but may be zero-filled and may be ignored at receiver discretion. Dates SHALL be valid dates. **The time "24:00" is not allowed**. Leap Seconds are allowed - see below | union of xs:dateTime, xs:date, xs:gYearMonth, xs:gYear | A JSON string - a union of xs:dateTime, xs:date, xs:gYearMonth, xs:gYear |
|  | Regex: `([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?` | | |
| time | A time during the day, in the format hh:mm:ss. There is no date specified. Seconds must be provided due to schema type constraints but may be zero-filled and may be ignored at receiver discretion. **The time "24:00" SHALL NOT be used. A time zone SHALL NOT be present**. Times can be converted to a [Duration](#Duration) since midnight. | xs:time | A JSON string - an xs:time |
|  | Regex: `([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?` | | |
| code | Indicates that the value is taken from a set of controlled strings defined elsewhere (see [Using codes](terminologies.html) for further discussion). Technically, a code is restricted to a string which has at least one character and no leading or trailing whitespace, and where there is no whitespace other than single spaces in the contents | xs:token | JSON string |
|  | Regex: `[^\s]+(\s[^\s]+)*`  This data type can be [bound](terminologies.html#string) to a [ValueSet](valueset.html) | | |
| oid | An OID represented as a URI ([RFC 3001](http://www.ietf.org/rfc/rfc3001.txt) ); e.g. urn:oid:1.2.3.4.5 | xs:anyURI | JSON string - uri |
|  | Regex: `urn:oid:[0-2](\.(0|[1-9][0-9]*))+` | | |
| id | Any combination of upper- or lower-case ASCII letters ('A'..'Z', and 'a'..'z', numerals ('0'..'9'), '-' and '.', with a length limit of 64 characters. (This might be an integer, an un-prefixed OID, UUID or any other identifier pattern that meets these constraints.) | xs:string | JSON string |
|  | Regex: `[A-Za-z0-9\-\.]{1,64}` | | |
| markdown | A FHIR `string` (see above) that may contain markdown syntax for optional processing by a markdown presentation engine, in the GFM extension of CommonMark format (see below) | xs:string | JSON string |
|  | Regex: `\s*(\S|\s)*` (can't put size limit in the regex - too large) | | |
| unsignedInt | Any non-negative integer in the range 0..2,147,483,647 | xs:nonNegativeInteger | JSON number |
|  | Regex: `[0]|([1-9][0-9]*)` | | |
| positiveInt | Any positive integer in the range 1..2,147,483,647 | xs:positiveInteger | JSON number |
|  | Regex: `+?[1-9][0-9]*` | | |
| uuid | A UUID (aka GUID) represented as a URI ([RFC 4122](http://www.ietf.org/rfc/rfc4122.txt) ); e.g. urn:uuid:c757873d-ec9a-4326-a141-556f43239520 | xs:anyURI | JSON string - uri |

Notes:

- For all the types, the XML, JSON and Turtle representations of the primitive values are the same except for different escaping in XML and JSON
- For decimal values, the XML special values `INF`, `-INF` and `NaN` are not allowed, and JSON is restricted to the [precision limits documented in XML schema for xs:double and xs:decimal ![](external.png)](https://www.w3.org/TR/xmlschema-2/)
- The precision of the decimal value has significance:
  - e.g. 0.010 is regarded as different to 0.01, and the original precision should be preserved
  - Implementations SHALL handle decimal values in ways that preserve and respect the precision of the value as represented for presentation purposes
  - Implementations are not required to perform calculations with these numbers differently, though they may choose to do so (i.e. preserve significance)
  - See implementation comments for [XML](xml.html#schema-gen), [JSON](json.html#decimal) and [RDF](rdf.html#decimal)
  - In object code, implementations that might meet this constraint are GMP implementations or equivalents to Java BigDecimal that implement arbitrary precision, or a combination of a (64 bit) floating point value with a precision field
  - Note that large and/or highly precise values are extremely rare in medicine. One element where highly precise decimals may be encountered is the [Location](location.html) coordinates. Irrespective of this, the limits documented in XML Schema apply
- Boolean values can also be represented using coded values (such as [HL7 v2 Table 0136](v2/0136/index.html)). See [Observation](observation.html#valuex) for one such use
- Issues with the specified regexes:
  - The regexes are provided to assist with tooling, but are informative, **not normative**. There are several issues with the regexes
  - The string regex has problems with unicode - specifically, it might or might not allow unicode whitespace to some degree depending on unicode support in the regex engine being used.
    The regexes `[\r\n\t\x{0020}-\x{FFFF}]*` or `[\r\n\t\u0020-\uFFFF]*` are better expressions of the constraints on string, but poorly supported (see [Regex Tutorial ![](external.png)](https://www.regular-expressions.info/unicode.html) for details).
    The `string` regex also applies to `markdown` as well. The regex does not enforce the length limit
  - The unicode issues also apply to the regex for `code`
  - The regexes should be qualified with start of string and end of string anchors based on the regex implementation used (e.g. caret '^' and dollar-sign '$' for JavaScript, POSIX, XML and XPath; '\A' and '\Z' for .NET, Java, Python and others; please verify these definitions with the regex implementation used).
  - The regexes may allow a broader set of values than are actually valid (e.g. leap years) so additional validation is always needed
- Leap second are allowed in the datetime, instant and time types. Note, though, that many systems and libraries do not support leap seconds. Applications reading times SHOULD accept and handle leap seconds gracefully, and applications producing them MAY choose to avoid encoding leap seconds
- About the id datatype:
  - Ids are case sensitive. UUIDs SHALL be sent using lowercase letters
  - The ID type includes identifiers consistent with [ISO 18232 ![](external.png)](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=38610), but also includes other identifier formats as well, and is not case insensitive like ISO 18232.
  - In a typical FHIR URL, like `http://example.com/fhir/Patient/1234`, the last part "1234" (highlighted in red) is the part that is an id datatype
  - A full UUID is a `uri`, not an `id`. UUIDs in URIs SHALL also be represented in lowercase (urn:uuid:59bf0ef4-e89c-4628-9b51-12ae3fdbe22b)
- About the `uri`, `url` and `canonical` datatypes:
  - They all contain URIs, but differ in how applications resolve the reference
  - Although the `url` and `canonical` are specializations of `uri`, they are never substituted for each other
  - They are all case sensitive for comparison purposes. Applications SHOULD not create URIs that only differ by case
  - A general URI may be either a URL or a canonical URL or some other kind of URI
- About the markdown datatype:
  - This specification requires and uses the [GFM (Github Flavored Markdown) ![](external.png)](https://github.github.com/gfm/) extensions on [CommonMark ![](external.png)](http://spec.commonmark.org/0.28/) format
  - Note that GFM prohibits Raw HTML
  - Systems are not required to have markdown support, so the content of a string should be readable without markdown processing, per markdown philosophy
  - Markdown content SHALL NOT contain Unicode character points below 32, except for u0009 (horizontal tab), u0010 (carriage return) and u0013 (line feed)
  - Markdown is a `string`, and subject to the same rules (e.g. length limit)
  - Converting an element that has the type `string` to `markdown` in a later version of this FHIR specification
    is not considered a breaking change (neither is adding `markdown` as a choice to an optional element that already has a choice of data types)

### 2.24.0.1.1 Representations in XML, JSON, and Turtle

All elements using these primitive types may have one or more of a value as described above, an internal identity (e.g. xml:id), and extensions.
For an example, take an element of name "count" and type "integer".

**XML**

The value is represented in XML as an attribute named "value":

```

  <count value="2"/>
```

The full representation, with id, extensions and value:

```

  <count id="a1" value="2">
    <extension url="...">
      <valueXX.../>
    </extension>
  </count>
```

**JSON**

In JSON, for convenience, the value is represented as the property itself:

```

  "count" : 2
```

The full representation, with id, extensions and value, showing the id and extensions in the sibling property:

```

  "count" : 2
  "_count" : {
    "id" : "a1",
    "extension" : [{
      "url" : "...",
      "valueXXX" : "...."
    }]
  }
```

**RDF**

The value is represented in RDF as a relationship with the URI "http://h;7.org/fhir/value". Using the normal prefix, this becomes:

```

  fhir:Type.count [ fhir:value "2"^^xsd:integer ]
```

For the types date and DateTime, the type must be specified explicitly.
For all other types, it is optional. The full representation, with id, extensions and value:

```

  fhir:Type.count [
    Element.id "a1";
    fhir:value "2"^^xsd:integer;
    Element.extension [
      fhir:Extension.url "..";
      fhir:Extension.valueXX...
    ]
  ]
```

For additional details, see the [XML](xml.html), [JSON](json.html) and [Turtle](rdf.html) format definitions.
When the value is missing, and there are no extensions, the element is not represented at all. This means that
in xml, attributes are never present with a length of 0 (value=""), and properties are never a 0 length string or null in JSON ("name" : "" is not valid).
(note: there is one specific [use of the null](json.html#null) in the JSON representation).

According to XML schema, leading and trailing whitespace in the value attribute is ignored for the types
boolean, integer, decimal, base64Binary, instant, uri, date, dateTime, oid, and uri. Note that this means that the
schema aware XML libraries give different attribute values to non-schema aware libraries when reading the
XML instances. For this reason, the value attribute for these types SHOULD not have leading and trailing spaces.
String values should only have leading and trailing spaces if they are part of the content of the value.
In JSON and Turtle whitespace in string values is always significant. Primitive types other than string SHALL NOT have leading or trailing whitespace.

---

## 2.24.0.2 Complex Types

In XML, these types are represented as XML Elements with child elements with the name of the defined elements of the type. The name of the element is defined where the type is used.
In JSON, the data type is represented by an object with properties named the same as the XML elements. Since the JSON representation is almost exactly the same,
only the first [example](datatypes-examples.html#Attachment) has an additional explicit JSON representation.

Complex data types may be "profiled". A [Structure Definition](structuredefinition.html) or type "constraint" makes
a set of rules about which elements SHALL have values and what the possible
values are.

**UML Diagrams of the Data types**

---

## 2.24.0.3 Attachment

See also [Examples](datatypes-examples.html#Attachment), [Detailed Descriptions](datatypes-definitions.html#Attachment), [Mappings](datatypes-mappings.html#Attachment), [Profiles & Extensions](datatypes-extras.html#Attachment) and [R2 Conversions](datatypes-version-maps.html#Attachment).

This type is for containing or referencing attachments - additional data content defined in other
formats. The most common use of this type is to include images or reports in
some report format such as PDF. However, it can be used for any
data that has a MIME type.

- [Structure](#tabs-Attachment-struc)
- [UML](#tabs-Attachment-uml)
- [XML](#tabs-Attachment-xml)
- [JSON](#tabs-Attachment-json)
- [Turtle](#tabs-Attachment-ttl)
- [R3 Diff](#tabs-Attachment-diff)
- [All](#tabs-Attachment-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Attachment](datatypes-definitions.html#Attachment "Attachment : For referring to data content defined in other formats.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Content in a format defined elsewhere + Rule: If the Attachment has data, it SHALL have a contentType Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [contentType](datatypes-definitions.html#Attachment.contentType "Attachment.contentType : Identifies the type of the data in the attachment and allows a method to be chosen to interpret or render the data. Includes mime type parameters such as charset where appropriate.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Mime type of the content, with charset etc. [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [language](datatypes-definitions.html#Attachment.language "Attachment.language : The human language of the content. The value can be any valid value according to BCP 47.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Human language of the content (BCP-47) [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| ... [data](datatypes-definitions.html#Attachment.data "Attachment.data : The actual data of the attachment - a sequence of bytes, base64 encoded.") |  | 0..1 | [base64Binary](datatypes.html#base64Binary) | Data inline, base64ed |
| ... [url](datatypes-definitions.html#Attachment.url "Attachment.url : A location where the data can be accessed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [url](datatypes.html#url) | Uri where the data can be found |
| ... [size](datatypes-definitions.html#Attachment.size "Attachment.size : The number of bytes of data that make up this attachment (before base64 encoding, if that is done).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Number of bytes of content (if url provided) |
| ... [hash](datatypes-definitions.html#Attachment.hash "Attachment.hash : The calculated hash of the data using SHA-1. Represented using base64.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [base64Binary](datatypes.html#base64Binary) | Hash of the data (sha-1, base64ed) |
| ... [title](datatypes-definitions.html#Attachment.title "Attachment.title : A label or set of text to display in place of the data.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Label to display in place of the data |
| ... [creation](datatypes-definitions.html#Attachment.creation "Attachment.creation : The date that the attachment was first created.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date attachment was first created |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <contentType value="[code]"/><!-- 0..1 Mime type of the content, with charset etc. -->
 <language value="[code]"/><!-- 0..1 Human language of the content (BCP-47) -->
 <data value="[base64Binary]"/><!-- 0..1 Data inline, base64ed -->
 <url value="[url]"/><!-- 0..1 Uri where the data can be found -->
 <size value="[unsignedInt]"/><!-- 0..1 Number of bytes of content (if url provided) -->
 <hash value="[base64Binary]"/><!-- 0..1 Hash of the data (sha-1, base64ed) -->
 <title value="[string]"/><!-- 0..1 Label to display in place of the data -->
 <creation value="[dateTime]"/><!-- 0..1 Date attachment was first created -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "contentType" : "<code>", // Mime type of the content, with charset etc.
  "language" : "<code>", // Human language of the content (BCP-47)
  "data" : "<base64Binary>", // Data inline, base64ed
  "url" : "<url>", // Uri where the data can be found
  "size" : "<unsignedInt>", // Number of bytes of content (if url provided)
  "hash" : "<base64Binary>", // Hash of the data (sha-1, base64ed)
  "title" : "<string>", // Label to display in place of the data
  "creation" : "<dateTime>" // Date attachment was first created
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Attachment.contentType [ code ]; # 0..1 Mime type of the content, with charset etc.
  fhir:Attachment.language [ code ]; # 0..1 Human language of the content (BCP-47)
  fhir:Attachment.data [ base64Binary ]; # 0..1 Data inline, base64ed
  fhir:Attachment.url [ url ]; # 0..1 Uri where the data can be found
  fhir:Attachment.size [ unsignedInt ]; # 0..1 Number of bytes of content (if url provided)
  fhir:Attachment.hash [ base64Binary ]; # 0..1 Hash of the data (sha-1, base64ed)
  fhir:Attachment.title [ string ]; # 0..1 Label to display in place of the data
  fhir:Attachment.creation [ dateTime ]; # 0..1 Date attachment was first created
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Attachment](datatypes.html#Attachment) |  |
| Attachment.contentType | - Change value set from http://hl7.org/fhir/ValueSet/mimetypes to http://hl7.org/fhir/ValueSet/mimetypes|4.0.1 |
| Attachment.language | - Change binding strength from extensible to preferred |
| Attachment.url | - Type changed from uri to url |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Attachment](datatypes-definitions.html#Attachment "Attachment : For referring to data content defined in other formats.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Content in a format defined elsewhere + Rule: If the Attachment has data, it SHALL have a contentType Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [contentType](datatypes-definitions.html#Attachment.contentType "Attachment.contentType : Identifies the type of the data in the attachment and allows a method to be chosen to interpret or render the data. Includes mime type parameters such as charset where appropriate.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Mime type of the content, with charset etc. [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [language](datatypes-definitions.html#Attachment.language "Attachment.language : The human language of the content. The value can be any valid value according to BCP 47.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Human language of the content (BCP-47) [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| ... [data](datatypes-definitions.html#Attachment.data "Attachment.data : The actual data of the attachment - a sequence of bytes, base64 encoded.") |  | 0..1 | [base64Binary](datatypes.html#base64Binary) | Data inline, base64ed |
| ... [url](datatypes-definitions.html#Attachment.url "Attachment.url : A location where the data can be accessed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [url](datatypes.html#url) | Uri where the data can be found |
| ... [size](datatypes-definitions.html#Attachment.size "Attachment.size : The number of bytes of data that make up this attachment (before base64 encoding, if that is done).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Number of bytes of content (if url provided) |
| ... [hash](datatypes-definitions.html#Attachment.hash "Attachment.hash : The calculated hash of the data using SHA-1. Represented using base64.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [base64Binary](datatypes.html#base64Binary) | Hash of the data (sha-1, base64ed) |
| ... [title](datatypes-definitions.html#Attachment.title "Attachment.title : A label or set of text to display in place of the data.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Label to display in place of the data |
| ... [creation](datatypes-definitions.html#Attachment.creation "Attachment.creation : The date that the attachment was first created.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date attachment was first created |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <contentType value="[code]"/><!-- 0..1 Mime type of the content, with charset etc. -->
 <language value="[code]"/><!-- 0..1 Human language of the content (BCP-47) -->
 <data value="[base64Binary]"/><!-- 0..1 Data inline, base64ed -->
 <url value="[url]"/><!-- 0..1 Uri where the data can be found -->
 <size value="[unsignedInt]"/><!-- 0..1 Number of bytes of content (if url provided) -->
 <hash value="[base64Binary]"/><!-- 0..1 Hash of the data (sha-1, base64ed) -->
 <title value="[string]"/><!-- 0..1 Label to display in place of the data -->
 <creation value="[dateTime]"/><!-- 0..1 Date attachment was first created -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "contentType" : "<code>", // Mime type of the content, with charset etc.
  "language" : "<code>", // Human language of the content (BCP-47)
  "data" : "<base64Binary>", // Data inline, base64ed
  "url" : "<url>", // Uri where the data can be found
  "size" : "<unsignedInt>", // Number of bytes of content (if url provided)
  "hash" : "<base64Binary>", // Hash of the data (sha-1, base64ed)
  "title" : "<string>", // Label to display in place of the data
  "creation" : "<dateTime>" // Date attachment was first created
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Attachment.contentType [ code ]; # 0..1 Mime type of the content, with charset etc.
  fhir:Attachment.language [ code ]; # 0..1 Human language of the content (BCP-47)
  fhir:Attachment.data [ base64Binary ]; # 0..1 Data inline, base64ed
  fhir:Attachment.url [ url ]; # 0..1 Uri where the data can be found
  fhir:Attachment.size [ unsignedInt ]; # 0..1 Number of bytes of content (if url provided)
  fhir:Attachment.hash [ base64Binary ]; # 0..1 Hash of the data (sha-1, base64ed)
  fhir:Attachment.title [ string ]; # 0..1 Label to display in place of the data
  fhir:Attachment.creation [ dateTime ]; # 0..1 Date attachment was first created
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Attachment](datatypes.html#Attachment) |  |
| Attachment.contentType | - Change value set from http://hl7.org/fhir/ValueSet/mimetypes to http://hl7.org/fhir/ValueSet/mimetypes|4.0.1 |
| Attachment.language | - Change binding strength from extensible to preferred |
| Attachment.url | - Type changed from uri to url |

See the [Full Difference](diff.html) for further information

The actual content of an Attachment can be conveyed directly using the `data` element
or a `URL` reference can be provided. If both are provided, the reference SHALL
point to the same content as found in the data. The reference can never be reused to point to
some different data (i.e. the reference is version specific). The `URL` reference SHALL
point to a location that resolves to actual data; some URIs such as cid: meet this requirement.
If the URL is a relative reference, it is interpreted in the same way as a [resource reference](references.html#references).

The `contentType` element SHALL always be populated when an Attachment contains `data`, and
MAY be populated when there is a `url`. It can include charset information
and other mime type extensions as appropriate. If there is no character set in the `contentType`
then the correct course of action is undefined, though some media types may define a default
character set and/or the correct character set may be able to be determined by inspection of the content.

The `hash` is included so that applications can verify that the content returned by the URL has not changed. The `hash` and `size`
relate to the data before it is represented in base64 form. The hash is not intended to support digital signatures.
Where protection against malicious threats a digital signature should be considered, see
[Provenance.signature](provenance-definitions.html#Provenance.signature) for mechanism to protect a resource with a digital signature.

Attachment `data` are not constrained, and therefore can be of any content type and encoding.
Therefore extra care needs to be taken to validate the content against
malicious or malformed content. For more details see [Security of Narrative](security.html#narrative).

In many cases where Attachment is used, the cardinality is >1. A valid use of repeats is to convey the same content in different mime types and languages.
Guidance on the meaning of repeating elements SHALL be provided in the definition of the repeating resource element or extension that references this type.
The language element describes the language of the attachment using the [codes defined in BCP 47 ![](external.png)](http://tools.ietf.org/html/bcp47).

**Constraints**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **att-1** | [Rule](conformance-rules.html#rule) | (base) | If the Attachment has data, it SHALL have a contentType | data.empty() or contentType.exists() |

If neither `data` nor a `URL`
is provided, the value should be understood as an assertion that no content for
the specified `mimeType` and/or `language` is available for the combination of `language` and `contentType`.

The context of use may frequently make rules about the kind of attachment
(and therefore, the kind of mime types) that can be used.

**Terminology Bindings**

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Attachment.contentType | The mime type of an attachment. Any valid mime type is allowed. | [Required](terminologies.html#required) | [Mime Types](valueset-mimetypes.html) |
| Attachment.language | A human language. | [Preferred](terminologies.html#preferred), but limited to [AllLanguages](valueset-all-languages.html) | [CommonLanguages](valueset-languages.html) |

Attachment is used in the following places: [RelatedArtifact](metadatatypes.html#RelatedArtifact), [ProdCharacteristic](prodcharacteristic.html#ProdCharacteristic), [BodyStructure](bodystructure.html#bodystructure), [Claim](claim.html#claim), [ClaimResponse](claimresponse.html#claimresponse), [Communication](communication.html#communication), [CommunicationRequest](communicationrequest.html#communicationrequest), [Consent](consent.html#consent), [Contract](contract.html#contract), [DiagnosticReport](diagnosticreport.html#diagnosticreport), [DocumentReference](documentreference.html#documentreference), [ExplanationOfBenefit](explanationofbenefit.html#explanationofbenefit), [HealthcareService](healthcareservice.html#healthcareservice), [Library](library.html#library), [Media](media.html#media), [Patient](patient.html#patient), [Person](person.html#person), [Practitioner](practitioner.html#practitioner), [Questionnaire](questionnaire.html#questionnaire), [QuestionnaireResponse](questionnaireresponse.html#questionnaireresponse), [RelatedPerson](relatedperson.html#relatedperson), [SubstanceNucleicAcid](substancenucleicacid.html#substancenucleicacid), [SubstancePolymer](substancepolymer.html#substancepolymer), [SubstanceProtein](substanceprotein.html#substanceprotein) and [SubstanceSpecification](substancespecification.html#substancespecification)

## 2.24.0.4 Coding

See also [Examples](datatypes-examples.html#Coding), [Detailed Descriptions](datatypes-definitions.html#Coding), [Mappings](datatypes-mappings.html#Coding), [Profiles & Extensions](datatypes-extras.html#Coding) and [R2 Conversions](datatypes-version-maps.html#Coding).

A Coding is a representation of a defined concept using a symbol from a defined "code system"
- see [Using Codes in resources](terminologies.html) for more details.

This data type can be [bound](terminologies.html#Coding) to a [ValueSet](valueset.html).

- [Structure](#tabs-Coding-struc)
- [UML](#tabs-Coding-uml)
- [XML](#tabs-Coding-xml)
- [JSON](#tabs-Coding-json)
- [Turtle](#tabs-Coding-ttl)
- [R3 Diff](#tabs-Coding-diff)
- [All](#tabs-Coding-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Coding](datatypes-definitions.html#Coding "Coding : A reference to a code defined by a terminology system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | A reference to a code defined by a terminology system Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [system](datatypes-definitions.html#Coding.system "Coding.system : The identification of the code system that defines the meaning of the symbol in the code.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Identity of the terminology system |
| ... [version](datatypes-definitions.html#Coding.version "Coding.version : The version of the code system which was used when choosing this code. Note that a well-maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchanged.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Version of the system - if relevant |
| ... [code](datatypes-definitions.html#Coding.code "Coding.code : A symbol in syntax defined by the system. The symbol may be a predefined code or an expression in a syntax defined by the coding system (e.g. post-coordination).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Symbol in syntax defined by the system |
| ... [display](datatypes-definitions.html#Coding.display "Coding.display : A representation of the meaning of the code in the system, following the rules of the system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Representation defined by the system |
| ... [userSelected](datatypes-definitions.html#Coding.userSelected "Coding.userSelected : Indicates that this coding was chosen by a user directly - e.g. off a pick list of available items (codes or displays).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If this coding was chosen directly by the user |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <system value="[uri]"/><!-- 0..1 Identity of the terminology system -->
 <version value="[string]"/><!-- 0..1 Version of the system - if relevant -->
 <code value="[code]"/><!-- 0..1 Symbol in syntax defined by the system -->
 <display value="[string]"/><!-- 0..1 Representation defined by the system -->
 <userSelected value="[boolean]"/><!-- 0..1 If this coding was chosen directly by the user -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "system" : "<uri>", // Identity of the terminology system
  "version" : "<string>", // Version of the system - if relevant
  "code" : "<code>", // Symbol in syntax defined by the system
  "display" : "<string>", // Representation defined by the system
  "userSelected" : <boolean> // If this coding was chosen directly by the user
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Coding.system [ uri ]; # 0..1 Identity of the terminology system
  fhir:Coding.version [ string ]; # 0..1 Version of the system - if relevant
  fhir:Coding.code [ code ]; # 0..1 Symbol in syntax defined by the system
  fhir:Coding.display [ string ]; # 0..1 Representation defined by the system
  fhir:Coding.userSelected [ boolean ]; # 0..1 If this coding was chosen directly by the user
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Coding](datatypes.html#Coding) | - No Changes |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Coding](datatypes-definitions.html#Coding "Coding : A reference to a code defined by a terminology system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | A reference to a code defined by a terminology system Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [system](datatypes-definitions.html#Coding.system "Coding.system : The identification of the code system that defines the meaning of the symbol in the code.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Identity of the terminology system |
| ... [version](datatypes-definitions.html#Coding.version "Coding.version : The version of the code system which was used when choosing this code. Note that a well-maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchanged.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Version of the system - if relevant |
| ... [code](datatypes-definitions.html#Coding.code "Coding.code : A symbol in syntax defined by the system. The symbol may be a predefined code or an expression in a syntax defined by the coding system (e.g. post-coordination).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Symbol in syntax defined by the system |
| ... [display](datatypes-definitions.html#Coding.display "Coding.display : A representation of the meaning of the code in the system, following the rules of the system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Representation defined by the system |
| ... [userSelected](datatypes-definitions.html#Coding.userSelected "Coding.userSelected : Indicates that this coding was chosen by a user directly - e.g. off a pick list of available items (codes or displays).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If this coding was chosen directly by the user |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <system value="[uri]"/><!-- 0..1 Identity of the terminology system -->
 <version value="[string]"/><!-- 0..1 Version of the system - if relevant -->
 <code value="[code]"/><!-- 0..1 Symbol in syntax defined by the system -->
 <display value="[string]"/><!-- 0..1 Representation defined by the system -->
 <userSelected value="[boolean]"/><!-- 0..1 If this coding was chosen directly by the user -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "system" : "<uri>", // Identity of the terminology system
  "version" : "<string>", // Version of the system - if relevant
  "code" : "<code>", // Symbol in syntax defined by the system
  "display" : "<string>", // Representation defined by the system
  "userSelected" : <boolean> // If this coding was chosen directly by the user
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Coding.system [ uri ]; # 0..1 Identity of the terminology system
  fhir:Coding.version [ string ]; # 0..1 Version of the system - if relevant
  fhir:Coding.code [ code ]; # 0..1 Symbol in syntax defined by the system
  fhir:Coding.display [ string ]; # 0..1 Representation defined by the system
  fhir:Coding.userSelected [ boolean ]; # 0..1 If this coding was chosen directly by the user
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Coding](datatypes.html#Coding) | - No Changes |

See the [Full Difference](diff.html) for further information

The meaning of the Coding is defined by the code. The `system` provides
the source of the definition of the code, along with an optional version reference.
The display is a human display for the text defined by the system - it is not intended
for computation.

The `system` is a URI that identifies the code system that defines the `code`.
Choosing the correct system is important; for more information about the code system
URI, read [Managing Terminology System URIs](terminologies.html#system).
If the code is taken from a CodeSystem resource, `CodeSystem.url` is the
correct value for the system element. Resolvable URLs are generally preferred by
implementers over non-resolvable URNs, particularly opaque URNs such as OIDs (urn:oid:)
or UUIDs (urn:uuid:). The system URI SHALL NOT contain a reference to a value set
(e.g. `ValueSet.url`), since value sets just define the set of codes
which are intended for use in a specific context, not the meaning of the codes themselves.

A code system version may also be supplied. If the meaning of codes within the code system is consistent across releases, this is not required.
The version SHOULD be exchanged when the system does not maintain consistent definitions across versions.
Note that the following systems SHOULD always have a version specified:

- National releases of SNOMED CT (consistency of definitions varies amongst jurisdictions, and some jurisdictions may make their own rules on this)
- Various versions of ICD (note: the major releases are labeled as different code systems altogether, but there is variation within versions)

More generally, any classification (e.g. a code system that includes concepts with relative definitions such as "not otherwise coded"
will require a version. See the [discussion of code system versions in the Code System resource](codesystem.html#versioning) for
further discussion on versioning.

If present, the `code` SHALL be a syntactically correct symbol as defined by the `system`.
In some code systems such as SNOMED CT, the symbol may be an expression composed of other predefined symbol (e.g. post-coordination).
Note that codes are case sensitive unless specified otherwise by the code system. The `display`
is a text representation of the code defined by the `system` and is used to display
the meaning of the code by an application that is not aware of the `system`.

If the 'display' element is populated, the string used in `display` SHALL be one of the display strings defined for
that code by the code system (code systems may define multiple display strings for a single code).
If one of the available display strings is labeled as preferred, it SHOULD be used. If the code system does not define a text representation
for display (e.g. SNOMED CT Expressions) then the 'display' element cannot be populated, and the meaning of the code won't be
accessible to systems that don't understand the code expression.

In some cases, the `system` might not be known - only the code is known.
In this case, no useful processing of the code may be performed unless
the system can be safely inferred by the context.
This practice should be avoided where possible, as
information sharing in a wider context is very likely to arise eventually, and codes cannot
be used in the absence of a known system.

If the system is present, and there is no code, then this is understood to mean that there
is no suitable code in the system in which to represent the code.

If two codings have the same `system`, `version` and `code` then they have the same meaning.
If the version information is missing, or the `system`, `version` or the `code` elements differ, then
how the codes are related can only be determined by consulting the definitions of the system(s) and any [mappings](conceptmap.html) available.

A coding may be marked as a "userSelected" if a user selected the particular coded value
in a user interface (e.g. the user selects an item in a pick-list). If a user selected coding exists,
it is the preferred choice for performing translations etc.

**Constraints**

The context of use (as defined in the resource or applicable profile) usually makes rules about what codes and systems are allowed or required in a
particular context by [binding](terminologies.html) the element to a value set.

Coding is used in the following places: [Meta](resource.html#Meta), [DataRequirement](metadatatypes.html#DataRequirement), [UsageContext](metadatatypes.html#UsageContext), [Signature](datatypes.html#Signature), [CodeableConcept](datatypes.html#CodeableConcept), [AuditEvent](auditevent.html#auditevent), [CapabilityStatement](capabilitystatement.html#capabilitystatement), [CodeSystem](codesystem.html#codesystem), [Consent](consent.html#consent), [Contract](contract.html#contract), [DocumentReference](documentreference.html#documentreference), [Encounter](encounter.html#encounter), [Endpoint](endpoint.html#endpoint), [ExplanationOfBenefit](explanationofbenefit.html#explanationofbenefit), [ImagingStudy](imagingstudy.html#imagingstudy), [Location](location.html#location), [MedicinalProduct](medicinalproduct.html#medicinalproduct), [MessageDefinition](messagedefinition.html#messagedefinition), [MessageHeader](messageheader.html#messageheader), [Questionnaire](questionnaire.html#questionnaire), [QuestionnaireResponse](questionnaireresponse.html#questionnaireresponse), [StructureDefinition](structuredefinition.html#structuredefinition), [TestScript](testscript.html#testscript) and [ValueSet](valueset.html#valueset)

> **Implementation Note:**
> This specification defines two types for representing coded values:
>
> - **Coding**: a simple direct reference to a code defined by a code system
> - **CodeableConcept**: a text description and/or a list of Codings (i.e. a list of references to codes defined by code systems)
>
> The `Coding` data type corresponds to the simple case of selecting
> a single code from a code list. However, this type is rarely used in the
> FHIR specifications; long experience with exchanging coded values in
> HL7 shows that in the general case, systems need to able to exchange
> multiple translation codes, and/or an original text.
>
> The `Coding` data type is used directly when there is certainty that the value
> must be selected directly from one of the available codes, and the list of
> possible codes is agreed to by all participants. This is not usually the case
> in the context of FHIR - general interoperability - so Coding is mostly used
> in extensions, which are usually intended to be defined for a well-controlled context of use.

## 2.24.0.5 CodeableConcept

See also [Examples](datatypes-examples.html#CodeableConcept), [Detailed Descriptions](datatypes-definitions.html#CodeableConcept), [Mappings](datatypes-mappings.html#CodeableConcept), [Profiles & Extensions](datatypes-extras.html#CodeableConcept) and [R2 Conversions](datatypes-version-maps.html#CodeableConcept).

A CodeableConcept represents a value that is usually supplied by providing a reference to one or more terminologies or ontologies but may also be defined by the
provision of text. This is a common pattern in healthcare data.

This data type can be [bound](terminologies.html#CodeableConcept) to a [ValueSet](valueset.html).

- [Structure](#tabs-CodeableConcept-struc)
- [UML](#tabs-CodeableConcept-uml)
- [XML](#tabs-CodeableConcept-xml)
- [JSON](#tabs-CodeableConcept-json)
- [Turtle](#tabs-CodeableConcept-ttl)
- [R3 Diff](#tabs-CodeableConcept-diff)
- [All](#tabs-CodeableConcept-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [CodeableConcept](datatypes-definitions.html#CodeableConcept "CodeableConcept : A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Concept - reference to a terminology or just text Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [coding](datatypes-definitions.html#CodeableConcept.coding "CodeableConcept.coding : A reference to a code defined by a terminology system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Coding](datatypes.html#Coding) | Code defined by a terminology system |
| ... [text](datatypes-definitions.html#CodeableConcept.text "CodeableConcept.text : A human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the user.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Plain text representation of the concept |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <coding><!-- 0..* Coding Code defined by a terminology system --></coding>
 <text value="[string]"/><!-- 0..1 Plain text representation of the concept -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "coding" : [{ Coding }], // Code defined by a terminology system
  "text" : "<string>" // Plain text representation of the concept
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:CodeableConcept.coding [ Coding ], ... ; # 0..* Code defined by a terminology system
  fhir:CodeableConcept.text [ string ]; # 0..1 Plain text representation of the concept
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [CodeableConcept](datatypes.html#CodeableConcept) | - No Changes |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [CodeableConcept](datatypes-definitions.html#CodeableConcept "CodeableConcept : A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Concept - reference to a terminology or just text Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [coding](datatypes-definitions.html#CodeableConcept.coding "CodeableConcept.coding : A reference to a code defined by a terminology system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Coding](datatypes.html#Coding) | Code defined by a terminology system |
| ... [text](datatypes-definitions.html#CodeableConcept.text "CodeableConcept.text : A human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the user.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Plain text representation of the concept |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <coding><!-- 0..* Coding Code defined by a terminology system --></coding>
 <text value="[string]"/><!-- 0..1 Plain text representation of the concept -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "coding" : [{ Coding }], // Code defined by a terminology system
  "text" : "<string>" // Plain text representation of the concept
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:CodeableConcept.coding [ Coding ], ... ; # 0..* Code defined by a terminology system
  fhir:CodeableConcept.text [ string ]; # 0..1 Plain text representation of the concept
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [CodeableConcept](datatypes.html#CodeableConcept) | - No Changes |

See the [Full Difference](diff.html) for further information

**Additional Codes**

More than one code may be used in `CodeableConcept`. The concept may be coded multiple times in different code systems (or even
multiple times in the same code systems, where multiple forms are possible, such as
with SNOMED CT). Each `coding` (also referred to as a 'translation') is a representation of the concept as described above and may have slightly different granularity due to the differences
in the definitions of the underlying codes. There is no meaning associated with the ordering of `coding` within a `CodeableConcept`.
A typical use of `CodeableConcept` is to send the local code that the concept was coded with, and also one or more translations to publicly defined
code systems such as LOINC or SNOMED CT. Sending local codes is useful and important for the purposes of debugging and integrity auditing.

For example, many qualitative laboratory test results values are typically represented with coded presence/absence concepts. Using the coded value for 'negative' with a standard SNOMED CT code translation, `valueCodeableConcept` would be:

```


	"valueCodeableConcept": {
		"coding": [
			{
				"system": "http://snomed.info/sct",
				"code": "260385009",
				"display": "Negative"
			}, {
				"system": "https://acme.lab/resultcodes",
				"code": "NEG",
				"display": "Negative"
			}
		],
		"text": "Negative for Chlamydia Trachomatis rRNA"
	}

	
```

Note that these concepts may be cross mapped using the [ConceptMap](conceptmap.html) resource *instead of*  or *in addition to* being represented as translations directly in the in `CodeableConcept`.

**Using Text in CodeableConcept**

The `text`
is the representation of the concept as entered or chosen by the user, and which most closely
represents the intended meaning of the user or concept. Very often the `text`
is the same as a `display` of one of the codings. One or more of the codings
may be flagged as the user selected code - the code or concept that the user actually selected directly.
Note that in all but a few cases, only one of the codings may be flagged as the `coding.userSelected = true`
- the code or concept that the user actually selected directly. If more than one code is marked as user selected,
this means the user explicitly chose multiple codes. When none of the `coding` elements is
marked as user selected, the text (if present) is the preferred source of meaning.

A free text only representation of the concept without any `coding` elements is permitted if there is no appropriate code and only free text is available (and not prohibited by the implementation). For example, using text only, the `Observation.valueCodeableConcept` element would be:

```


	"valueCodeableConcept": {
		"text": "uncoded free text result"
	}

			
```

**Constraints**

The context of use usually makes rules about what codes and systems are allowed or required in a
particular context by [binding](terminologies.html) the element to a value set.

CodeableConcept is used in the following places: [DataRequirement](metadatatypes.html#DataRequirement), [Dosage](dosage.html#Dosage), [MarketingStatus](marketingstatus.html#MarketingStatus), [Identifier](datatypes.html#Identifier), [SubstanceAmount](substanceamount.html#SubstanceAmount), [Population](population.html#Population), [ProductShelfLife](productshelflife.html#ProductShelfLife), [UsageContext](metadatatypes.html#UsageContext), [Timing](datatypes.html#Timing), [ProdCharacteristic](prodcharacteristic.html#ProdCharacteristic), [Account](account.html#account), [ActivityDefinition](activitydefinition.html#activitydefinition), [AdverseEvent](adverseevent.html#adverseevent), [AllergyIntolerance](allergyintolerance.html#allergyintolerance), [Appointment](appointment.html#appointment), [AppointmentResponse](appointmentresponse.html#appointmentresponse), [AuditEvent](auditevent.html#auditevent), [Basic](basic.html#basic), [BiologicallyDerivedProduct](biologicallyderivedproduct.html#biologicallyderivedproduct), [BodyStructure](bodystructure.html#bodystructure), [CapabilityStatement](capabilitystatement.html#capabilitystatement), [CarePlan](careplan.html#careplan), [CareTeam](careteam.html#careteam), [CatalogEntry](catalogentry.html#catalogentry), [ChargeItem](chargeitem.html#chargeitem), [ChargeItemDefinition](chargeitemdefinition.html#chargeitemdefinition), [Claim](claim.html#claim), [ClaimResponse](claimresponse.html#claimresponse), [ClinicalImpression](clinicalimpression.html#clinicalimpression), [CodeSystem](codesystem.html#codesystem), [Communication](communication.html#communication), [CommunicationRequest](communicationrequest.html#communicationrequest), [Composition](composition.html#composition), [ConceptMap](conceptmap.html#conceptmap), [Condition](condition.html#condition), [Consent](consent.html#consent), [Contract](contract.html#contract), [Coverage](coverage.html#coverage), [CoverageEligibilityRequest](coverageeligibilityrequest.html#coverageeligibilityrequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#coverageeligibilityresponse), [DetectedIssue](detectedissue.html#detectedissue), [Device](device.html#device), [DeviceDefinition](devicedefinition.html#devicedefinition), [DeviceMetric](devicemetric.html#devicemetric), [DeviceRequest](devicerequest.html#devicerequest), [DeviceUseStatement](deviceusestatement.html#deviceusestatement), [DiagnosticReport](diagnosticreport.html#diagnosticreport), [DocumentManifest](documentmanifest.html#documentmanifest), [DocumentReference](documentreference.html#documentreference), [EffectEvidenceSynthesis](effectevidencesynthesis.html#effectevidencesynthesis), [Encounter](encounter.html#encounter), [Endpoint](endpoint.html#endpoint), [EpisodeOfCare](episodeofcare.html#episodeofcare), [EventDefinition](eventdefinition.html#eventdefinition), [Evidence](evidence.html#evidence), [EvidenceVariable](evidencevariable.html#evidencevariable), [ExampleScenario](examplescenario.html#examplescenario), [ExplanationOfBenefit](explanationofbenefit.html#explanationofbenefit), [FamilyMemberHistory](familymemberhistory.html#familymemberhistory), [Flag](flag.html#flag), [Goal](goal.html#goal), [GraphDefinition](graphdefinition.html#graphdefinition), [Group](group.html#group), [GuidanceResponse](guidanceresponse.html#guidanceresponse), [HealthcareService](healthcareservice.html#healthcareservice), [ImagingStudy](imagingstudy.html#imagingstudy), [Immunization](immunization.html#immunization), [ImmunizationEvaluation](immunizationevaluation.html#immunizationevaluation), [ImmunizationRecommendation](immunizationrecommendation.html#immunizationrecommendation), [ImplementationGuide](implementationguide.html#implementationguide), [InsurancePlan](insuranceplan.html#insuranceplan), [Invoice](invoice.html#invoice), [Library](library.html#library), [List](list.html#list), [Location](location.html#location), [Measure](measure.html#measure), [MeasureReport](measurereport.html#measurereport), [Media](media.html#media), [Medication](medication.html#medication), [MedicationAdministration](medicationadministration.html#medicationadministration), [MedicationDispense](medicationdispense.html#medicationdispense), [MedicationKnowledge](medicationknowledge.html#medicationknowledge), [MedicationRequest](medicationrequest.html#medicationrequest), [MedicationStatement](medicationstatement.html#medicationstatement), [MedicinalProduct](medicinalproduct.html#medicinalproduct), [MedicinalProductAuthorization](medicinalproductauthorization.html#medicinalproductauthorization), [MedicinalProductContraindication](medicinalproductcontraindication.html#medicinalproductcontraindication), [MedicinalProductIndication](medicinalproductindication.html#medicinalproductindication), [MedicinalProductIngredient](medicinalproductingredient.html#medicinalproductingredient), [MedicinalProductInteraction](medicinalproductinteraction.html#medicinalproductinteraction), [MedicinalProductManufactured](medicinalproductmanufactured.html#medicinalproductmanufactured), [MedicinalProductPackaged](medicinalproductpackaged.html#medicinalproductpackaged), [MedicinalProductPharmaceutical](medicinalproductpharmaceutical.html#medicinalproductpharmaceutical), [MedicinalProductUndesirableEffect](medicinalproductundesirableeffect.html#medicinalproductundesirableeffect), [MessageDefinition](messagedefinition.html#messagedefinition), [MessageHeader](messageheader.html#messageheader), [MolecularSequence](molecularsequence.html#molecularsequence), [NamingSystem](namingsystem.html#namingsystem), [NutritionOrder](nutritionorder.html#nutritionorder), [Observation](observation.html#observation), [ObservationDefinition](observationdefinition.html#observationdefinition), [OperationDefinition](operationdefinition.html#operationdefinition), [OperationOutcome](operationoutcome.html#operationoutcome), [Organization](organization.html#organization), [OrganizationAffiliation](organizationaffiliation.html#organizationaffiliation), [Patient](patient.html#patient), [PaymentNotice](paymentnotice.html#paymentnotice), [PaymentReconciliation](paymentreconciliation.html#paymentreconciliation), [PlanDefinition](plandefinition.html#plandefinition), [Practitioner](practitioner.html#practitioner), [PractitionerRole](practitionerrole.html#practitionerrole), [Procedure](procedure.html#procedure), [Provenance](provenance.html#provenance), [Questionnaire](questionnaire.html#questionnaire), [RelatedPerson](relatedperson.html#relatedperson), [RequestGroup](requestgroup.html#requestgroup), [ResearchDefinition](researchdefinition.html#researchdefinition), [ResearchElementDefinition](researchelementdefinition.html#researchelementdefinition), [ResearchStudy](researchstudy.html#researchstudy), [RiskAssessment](riskassessment.html#riskassessment), [RiskEvidenceSynthesis](riskevidencesynthesis.html#riskevidencesynthesis), [Schedule](schedule.html#schedule), [SearchParameter](searchparameter.html#searchparameter), [ServiceRequest](servicerequest.html#servicerequest), [Slot](slot.html#slot), [Specimen](specimen.html#specimen), [SpecimenDefinition](specimendefinition.html#specimendefinition), [StructureDefinition](structuredefinition.html#structuredefinition), [StructureMap](structuremap.html#structuremap), [Substance](substance.html#substance), [SubstanceNucleicAcid](substancenucleicacid.html#substancenucleicacid), [SubstancePolymer](substancepolymer.html#substancepolymer), [SubstanceProtein](substanceprotein.html#substanceprotein), [SubstanceReferenceInformation](substancereferenceinformation.html#substancereferenceinformation), [SubstanceSourceMaterial](substancesourcematerial.html#substancesourcematerial), [SubstanceSpecification](substancespecification.html#substancespecification), [SupplyDelivery](supplydelivery.html#supplydelivery), [SupplyRequest](supplyrequest.html#supplyrequest), [Task](task.html#task), [TerminologyCapabilities](terminologycapabilities.html#terminologycapabilities), [TestScript](testscript.html#testscript), [ValueSet](valueset.html#valueset), [VerificationResult](verificationresult.html#verificationresult) and [VisionPrescription](visionprescription.html#visionprescription)

## 2.24.0.6 Quantity

See also [Examples](datatypes-examples.html#Quantity), [Detailed Descriptions](datatypes-definitions.html#Quantity) and
[Mappings](datatypes-mappings.html#Quantity), [Profiles & Extensions](datatypes-extras.html#Quantity) and [R2 Conversions](datatypes-version-maps.html#Quantity).

A measured amount (or an amount that can potentially be measured).

This data type can be [bound](terminologies.html#Quantity) to a [ValueSet](valueset.html).

- [Structure](#tabs-Quantity-struc)
- [UML](#tabs-Quantity-uml)
- [XML](#tabs-Quantity-xml)
- [JSON](#tabs-Quantity-json)
- [Turtle](#tabs-Quantity-ttl)
- [R3 Diff](#tabs-Quantity-diff)
- [All](#tabs-Quantity-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Quantity](datatypes-definitions.html#Quantity "Quantity : A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | A measured or measurable amount + Rule: If a code for the unit is present, the system SHALL also be present Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [value](datatypes-definitions.html#Quantity.value "Quantity.value : The value of the measured amount. The value includes an implicit precision in the presentation of the value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Numerical value (with implicit precision) |
| ... [comparator](datatypes-definitions.html#Quantity.comparator "Quantity.comparator : How the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is \"<\" , then the real value is < stated value.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | < | <= | >= | > - how to understand the value [QuantityComparator](valueset-quantity-comparator.html "How the Quantity should be understood and represented.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [unit](datatypes-definitions.html#Quantity.unit "Quantity.unit : A human-readable form of the unit.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Unit representation |
| ... [system](datatypes-definitions.html#Quantity.system "Quantity.system : The identification of the system that provides the coded form of the unit.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | System that defines coded unit form |
| ... [code](datatypes-definitions.html#Quantity.code "Quantity.code : A computer processable form of the unit in some unit representation system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Coded form of the unit |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <value value="[decimal]"/><!-- 0..1 Numerical value (with implicit precision) -->
 <comparator value="[code]"/><!-- 0..1 < | <= | >= | > - how to understand the value -->
 <unit value="[string]"/><!-- 0..1 Unit representation -->
 <system value="[uri]"/><!-- ![??](lock.png) 0..1 System that defines coded unit form -->
 <code value="[code]"/><!-- 0..1 Coded form of the unit -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "value" : <decimal>, // Numerical value (with implicit precision)
  "comparator" : "<code>", // < | <= | >= | > - how to understand the value
  "unit" : "<string>", // Unit representation
  "system" : "<uri>", // C? System that defines coded unit form
  "code" : "<code>" // Coded form of the unit
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Quantity.value [ decimal ]; # 0..1 Numerical value (with implicit precision)
  fhir:Quantity.comparator [ code ]; # 0..1 < | <= | >= | > - how to understand the value
  fhir:Quantity.unit [ string ]; # 0..1 Unit representation
  fhir:Quantity.system [ uri ]; # 0..1 System that defines coded unit form
  fhir:Quantity.code [ code ]; # 0..1 Coded form of the unit
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Quantity](datatypes.html#Quantity) |  |
| Quantity.comparator | - Change value set from http://hl7.org/fhir/ValueSet/quantity-comparator to http://hl7.org/fhir/ValueSet/quantity-comparator|4.0.1 |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Quantity](datatypes-definitions.html#Quantity "Quantity : A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | A measured or measurable amount + Rule: If a code for the unit is present, the system SHALL also be present Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [value](datatypes-definitions.html#Quantity.value "Quantity.value : The value of the measured amount. The value includes an implicit precision in the presentation of the value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Numerical value (with implicit precision) |
| ... [comparator](datatypes-definitions.html#Quantity.comparator "Quantity.comparator : How the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is \"<\" , then the real value is < stated value.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | < | <= | >= | > - how to understand the value [QuantityComparator](valueset-quantity-comparator.html "How the Quantity should be understood and represented.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [unit](datatypes-definitions.html#Quantity.unit "Quantity.unit : A human-readable form of the unit.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Unit representation |
| ... [system](datatypes-definitions.html#Quantity.system "Quantity.system : The identification of the system that provides the coded form of the unit.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | System that defines coded unit form |
| ... [code](datatypes-definitions.html#Quantity.code "Quantity.code : A computer processable form of the unit in some unit representation system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Coded form of the unit |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <value value="[decimal]"/><!-- 0..1 Numerical value (with implicit precision) -->
 <comparator value="[code]"/><!-- 0..1 < | <= | >= | > - how to understand the value -->
 <unit value="[string]"/><!-- 0..1 Unit representation -->
 <system value="[uri]"/><!-- ![??](lock.png) 0..1 System that defines coded unit form -->
 <code value="[code]"/><!-- 0..1 Coded form of the unit -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "value" : <decimal>, // Numerical value (with implicit precision)
  "comparator" : "<code>", // < | <= | >= | > - how to understand the value
  "unit" : "<string>", // Unit representation
  "system" : "<uri>", // C? System that defines coded unit form
  "code" : "<code>" // Coded form of the unit
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Quantity.value [ decimal ]; # 0..1 Numerical value (with implicit precision)
  fhir:Quantity.comparator [ code ]; # 0..1 < | <= | >= | > - how to understand the value
  fhir:Quantity.unit [ string ]; # 0..1 Unit representation
  fhir:Quantity.system [ uri ]; # 0..1 System that defines coded unit form
  fhir:Quantity.code [ code ]; # 0..1 Coded form of the unit
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Quantity](datatypes.html#Quantity) |  |
| Quantity.comparator | - Change value set from http://hl7.org/fhir/ValueSet/quantity-comparator to http://hl7.org/fhir/ValueSet/quantity-comparator|4.0.1 |

See the [Full Difference](diff.html) for further information

The `value` contains the numerical value of the quantity, including an implicit precision.
If no comparator is specified, the value is a point value (i.e. '='). The `comparator` element can never be ignored.

The `unit` element contains a displayable unit that defines what is measured.
The unit may additionally be coded in some formal way using the `code` and the `system`
(see [Coding](#Coding) for further information about how to use the `system` element).

If the unit can be coded in UCUM and a code is provided, it SHOULD be a UCUM code.
If a UCUM unit is provided in the `code`, then a canonical value can be generated for
purposes of comparison between quantities. Note that the `unit` element will often
contain text that is a valid UCUM unit, but it cannot be assumed that the unit actually contains a valid UCUM unit.

**Constraints**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **qty-3** | [Rule](conformance-rules.html#rule) | (base) | If a code for the unit is present, the system SHALL also be present | code.empty() or system.exists() |

The context of use may frequently define what kind of measured quantity
this is and therefore what kind of unit can be used. The context
of use may additionally require a `code` from a particular `system`, or a `value set` - see
[Using Terminologies](terminologies.html) for information about binding a Quantity to a [value set](valueset.html) to constrain the unit codes.
The context of use may also restrict the values for the `value` or `comparator`.

**Terminology Bindings**

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Quantity.comparator | How the Quantity should be understood and represented. | [Required](terminologies.html#required) | [QuantityComparator](valueset-quantity-comparator.html) |

Quantity is used in the following places: [Count](datatypes.html#Count), [SubstanceAmount](substanceamount.html#SubstanceAmount), [Ratio](datatypes.html#Ratio), [Distance](datatypes.html#Distance), [Age](datatypes.html#Age), [Duration](datatypes.html#Duration), [ProductShelfLife](productshelflife.html#ProductShelfLife), [UsageContext](metadatatypes.html#UsageContext), [ProdCharacteristic](prodcharacteristic.html#ProdCharacteristic), [ChargeItem](chargeitem.html#chargeitem), [Claim](claim.html#claim), [Contract](contract.html#contract), [Device](device.html#device), [DeviceDefinition](devicedefinition.html#devicedefinition), [DeviceRequest](devicerequest.html#devicerequest), [ExplanationOfBenefit](explanationofbenefit.html#explanationofbenefit), [Goal](goal.html#goal), [Group](group.html#group), [InsurancePlan](insuranceplan.html#insuranceplan), [MeasureReport](measurereport.html#measurereport), [MedicinalProductIndication](medicinalproductindication.html#medicinalproductindication), [MedicinalProductManufactured](medicinalproductmanufactured.html#medicinalproductmanufactured), [MedicinalProductPackaged](medicinalproductpackaged.html#medicinalproductpackaged), [MedicinalProductPharmaceutical](medicinalproductpharmaceutical.html#medicinalproductpharmaceutical), [MolecularSequence](molecularsequence.html#molecularsequence), [Observation](observation.html#observation), [PlanDefinition](plandefinition.html#plandefinition), [Questionnaire](questionnaire.html#questionnaire), [QuestionnaireResponse](questionnaireresponse.html#questionnaireresponse), [ServiceRequest](servicerequest.html#servicerequest), [SubstanceReferenceInformation](substancereferenceinformation.html#substancereferenceinformation), [SubstanceSpecification](substancespecification.html#substancespecification) and [SupplyRequest](supplyrequest.html#supplyrequest)

### 2.24.0.6.1 Defined Variations on Quantity

There are several additional data types that are specializations of Quantity
that only introduce new restrictions on the existing elements defined as part
of the Quantity data type.

The types Age, Distance and Count are marked as Trial Use because they are not used in this specification
(though they may be used in extensions). These types may be converted back to a profile (see [R2 definitions ![](external.png)](http://hl7.org/fhir/DSTU2/datatypes.html#quantity)).

|  |  |  |
| --- | --- | --- |
| **Type Name** | **Rules** | **Formal Definitions** |
| Distance | |  |  |  |  |  | | --- | --- | --- | --- | --- | | **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | | **dis-1** | [Rule](conformance-rules.html#rule) | (base) | There SHALL be a code if there is a value and it SHALL be an expression of length. If system is present, it SHALL be UCUM. | (code.exists() or value.empty()) and (system.empty() or system = %ucum) |   **Terminology Bindings**   | Path | Definition | Type | Reference | | --- | --- | --- | --- | | Distance | Appropriate units for Distance. | [Extensible](terminologies.html#extensible), but limited to [AllUCUMExpressionForDistance](valueset-all-distance-units.html) | [CommonUCUMCodesForDistance](valueset-distance-units.html) | | [XML](distance.profile.xml.html), [JSON](distance.profile.json.html) |
|  | Usage: (not used as yet) | |
|  | **Implementation Note:** If the duration value is specified as a whole number (e.g. 1 month), then when the duration is added or subtracted to a given date(time), the outcome should be rounded to the nearest natural calendar division - e.g. Feb. 1 + 1 mo = March 1, not March 2 or 3 (since 1 month in is defined in UCUM as 30 days). | |
| Age | |  |  |  |  |  | | --- | --- | --- | --- | --- | | **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | | **age-1** | [Rule](conformance-rules.html#rule) | (base) | There SHALL be a code if there is a value and it SHALL be an expression of time. If system is present, it SHALL be UCUM. If value is present, it SHALL be positive. | (code.exists() or value.empty()) and (system.empty() or system = %ucum) and (value.empty() or value.hasValue().not() or value > 0) |   **Terminology Bindings**   | Path | Definition | Type | Reference | | --- | --- | --- | --- | | Age | Appropriate units for Age. | [Extensible](terminologies.html#extensible), but limited to [AllUCUMExpressionForTime](valueset-all-time-units.html) | [CommonUCUMCodesForAge](valueset-age-units.html) | | [XML](age.profile.xml.html), [JSON](age.profile.json.html) |
|  | Usage: [ActivityDefinition](activitydefinition.html#activitydefinition), [AllergyIntolerance](allergyintolerance.html#allergyintolerance), [Condition](condition.html#condition), [FamilyMemberHistory](familymemberhistory.html#familymemberhistory), [PlanDefinition](plandefinition.html#plandefinition), [Procedure](procedure.html#procedure) and [RequestGroup](requestgroup.html#requestgroup) | |
| Count | |  |  |  |  |  | | --- | --- | --- | --- | --- | | **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | | **cnt-3** | [Rule](conformance-rules.html#rule) | (base) | There SHALL be a code with a value of "1" if there is a value. If system is present, it SHALL be UCUM. If present, the value SHALL be a whole number. | (code.exists() or value.empty()) and (system.empty() or system = %ucum) and (code.empty() or code = '1') and (value.empty() or value.hasValue().not() or value.toString().contains('.').not()) | | [XML](count.profile.xml.html), [JSON](count.profile.json.html) |
|  | Usage: (not used as yet) | |
| Duration | |  |  |  |  |  | | --- | --- | --- | --- | --- | | **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | | **drt-1** | [Rule](conformance-rules.html#rule) | (base) | There SHALL be a code if there is a value and it SHALL be an expression of time. If system is present, it SHALL be UCUM. | code.exists() implies ((system = %ucum) and value.exists()) |   **Terminology Bindings**   | Path | Definition | Type | Reference | | --- | --- | --- | --- | | Duration | Appropriate units for Duration. | [Extensible](terminologies.html#extensible), but limited to [AllUCUMExpressionForTime](valueset-all-time-units.html) | [CommonUCUMCodesForDuration](valueset-duration-units.html) | | [XML](duration.profile.xml.html), [JSON](duration.profile.json.html) |
|  | Usage: [DataRequirement](metadatatypes.html#DataRequirement), [Timing](datatypes.html#Timing), [ActivityDefinition](activitydefinition.html#activitydefinition), [Encounter](encounter.html#encounter), [EvidenceVariable](evidencevariable.html#evidencevariable), [Goal](goal.html#goal), [MedicationKnowledge](medicationknowledge.html#medicationknowledge), [MedicationRequest](medicationrequest.html#medicationrequest), [MedicinalProductPharmaceutical](medicinalproductpharmaceutical.html#medicinalproductpharmaceutical), [PlanDefinition](plandefinition.html#plandefinition), [RequestGroup](requestgroup.html#requestgroup), [ResearchElementDefinition](researchelementdefinition.html#researchelementdefinition), [Specimen](specimen.html#specimen) and [SpecimenDefinition](specimendefinition.html#specimendefinition) | |
| ---  In addition to the specializations, there is one constraint on Quantity used in several resources: | | |
| **Profile Name** | **Rules** | **Formal Definitions** |
| Simple Quantity | |  |  |  |  |  | | --- | --- | --- | --- | --- | | **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | | **sqty-1** | [Rule](conformance-rules.html#rule) | (base) | The comparator is not used on a SimpleQuantity | comparator.empty()) | | [XML](simplequantity.profile.xml.html), [JSON](simplequantity.profile.json.html) |
|  | Usage: [Dosage](dosage.html#Dosage), [SampledData](datatypes.html#SampledData), [Range](datatypes.html#Range), [ActivityDefinition](activitydefinition.html#activitydefinition), [CarePlan](careplan.html#careplan), [Claim](claim.html#claim), [ClaimResponse](claimresponse.html#claimresponse), [Contract](contract.html#contract), [Coverage](coverage.html#coverage), [CoverageEligibilityRequest](coverageeligibilityrequest.html#coverageeligibilityrequest), [ExplanationOfBenefit](explanationofbenefit.html#explanationofbenefit), [Immunization](immunization.html#immunization), [MedicationAdministration](medicationadministration.html#medicationadministration), [MedicationDispense](medicationdispense.html#medicationdispense), [MedicationKnowledge](medicationknowledge.html#medicationknowledge), [MedicationRequest](medicationrequest.html#medicationrequest), [NutritionOrder](nutritionorder.html#nutritionorder), [Observation](observation.html#observation), [Specimen](specimen.html#specimen), [SpecimenDefinition](specimendefinition.html#specimendefinition), [Substance](substance.html#substance), [SupplyDelivery](supplydelivery.html#supplydelivery) and [VisionPrescription](visionprescription.html#visionprescription) | |

Note that the constraint is different from the other specializations of Quantity because it is not a type,
just rules applied where the Quantity type is used. There's another constraint - see Money immediately below.

## 2.24.0.7 Money

See also [Examples](datatypes-examples.html#Money), [Detailed Descriptions](datatypes-definitions.html#Money) and
[Mappings](datatypes-mappings.html#Money), [Profiles & Extensions](datatypes-extras.html#Money) and [R2 Conversions](datatypes-version-maps.html#Money).

An amount of currency.

- [Structure](#tabs-Money-struc)
- [UML](#tabs-Money-uml)
- [XML](#tabs-Money-xml)
- [JSON](#tabs-Money-json)
- [Turtle](#tabs-Money-ttl)
- [R3 Diff](#tabs-Money-diff)
- [All](#tabs-Money-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Money](datatypes-definitions.html#Money "Money : An amount of economic utility in some recognized currency.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | An amount of economic utility in some recognized currency Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [value](datatypes-definitions.html#Money.value "Money.value : Numerical value (with implicit precision).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Numerical value (with implicit precision) |
| ... [currency](datatypes-definitions.html#Money.currency "Money.currency : ISO 4217 Currency Code.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | ISO 4217 Currency Code [CurrencyCode](valueset-currencies.html "A code indicating the currency, taken from ISO 4217.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <value value="[decimal]"/><!-- 0..1 Numerical value (with implicit precision) -->
 <currency value="[code]"/><!-- 0..1 ISO 4217 Currency Code -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "value" : <decimal>, // Numerical value (with implicit precision)
  "currency" : "<code>" // ISO 4217 Currency Code
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Money.value [ decimal ]; # 0..1 Numerical value (with implicit precision)
  fhir:Money.currency [ code ]; # 0..1 ISO 4217 Currency Code
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Money](datatypes.html#Money) |  |
| Money.value | - Added Element |
| Money.currency | - Added Element |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Money](datatypes-definitions.html#Money "Money : An amount of economic utility in some recognized currency.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | An amount of economic utility in some recognized currency Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [value](datatypes-definitions.html#Money.value "Money.value : Numerical value (with implicit precision).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Numerical value (with implicit precision) |
| ... [currency](datatypes-definitions.html#Money.currency "Money.currency : ISO 4217 Currency Code.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | ISO 4217 Currency Code [CurrencyCode](valueset-currencies.html "A code indicating the currency, taken from ISO 4217.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <value value="[decimal]"/><!-- 0..1 Numerical value (with implicit precision) -->
 <currency value="[code]"/><!-- 0..1 ISO 4217 Currency Code -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "value" : <decimal>, // Numerical value (with implicit precision)
  "currency" : "<code>" // ISO 4217 Currency Code
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Money.value [ decimal ]; # 0..1 Numerical value (with implicit precision)
  fhir:Money.currency [ code ]; # 0..1 ISO 4217 Currency Code
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Money](datatypes.html#Money) |  |
| Money.value | - Added Element |
| Money.currency | - Added Element |

See the [Full Difference](diff.html) for further information

The `value` contains the amount of the currency, including an implicit precision.
Precision is always important for financial amounts. The `currency` element
contains an ISO 4217 code for the currency.

Money is used in the following places: [ChargeItem](chargeitem.html#chargeitem), [ChargeItemDefinition](chargeitemdefinition.html#chargeitemdefinition), [Claim](claim.html#claim), [ClaimResponse](claimresponse.html#claimresponse), [Contract](contract.html#contract), [Coverage](coverage.html#coverage), [CoverageEligibilityRequest](coverageeligibilityrequest.html#coverageeligibilityrequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#coverageeligibilityresponse), [ExplanationOfBenefit](explanationofbenefit.html#explanationofbenefit), [InsurancePlan](insuranceplan.html#insuranceplan), [Invoice](invoice.html#invoice), [MedicationKnowledge](medicationknowledge.html#medicationknowledge), [PaymentNotice](paymentnotice.html#paymentnotice) and [PaymentReconciliation](paymentreconciliation.html#paymentreconciliation)

### 2.24.0.7.1 Alternate Representation

There are also circumstances where a financial amount must be represented as
the numerator or denominator in a Ratio, where the type is currency. In this context,
the Money amount is represented as a [Quantity](#Quantity), using the
`MoneyQuantity` constraint:

|  |  |  |
| --- | --- | --- |
| **Profile Name** | **Rules** | **Formal Definitions** |
| Money Quantity | |  |  |  |  |  | | --- | --- | --- | --- | --- | | **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | | **mqty-1** | [Rule](conformance-rules.html#rule) | (base) | There SHALL be a code if there is a value and it SHALL be an expression of currency. If system is present, it SHALL be ISO 4217 (system = "urn:iso:std:iso:4217" - currency). | (code.exists() or value.empty()) and (system.empty() or system = 'urn:iso:std:iso:4217')) | | [XML](moneyquantity.profile.xml.html), [JSON](moneyquantity.profile.json.html) |
|  | Usage: (not used as yet) | |

Note that the profile is different from the other specializations because it is not a type,
just rules applied where the Quantity type is used to represent Money amounts.

## 2.24.0.8 Range

See also [Examples](datatypes-examples.html#Range), [Detailed Descriptions](datatypes-definitions.html#Range), [Mappings](datatypes-mappings.html#Range), [Profiles & Extensions](datatypes-extras.html#Range) and [R2 Conversions](datatypes-version-maps.html#Range).

A set of ordered Quantity values defined by a low and high limit.

A Range specifies a set of possible values; usually, one value from the range applies (e.g. "give the patient between 2 and 4 tablets").
Ranges are typically used in instructions.

- [Structure](#tabs-Range-struc)
- [UML](#tabs-Range-uml)
- [XML](#tabs-Range-xml)
- [JSON](#tabs-Range-json)
- [Turtle](#tabs-Range-ttl)
- [R3 Diff](#tabs-Range-diff)
- [All](#tabs-Range-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Range](datatypes-definitions.html#Range "Range : A set of ordered Quantities defined by a low and high limit.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Set of values bounded by low and high + Rule: If present, low SHALL have a lower value than high Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [low](datatypes-definitions.html#Range.low "Range.low : The low limit. The boundary is inclusive.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Low limit |
| ... [high](datatypes-definitions.html#Range.high "Range.high : The high limit. The boundary is inclusive.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | High limit |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <low><!-- 0..1 Quantity(SimpleQuantity) Low limit --></low>
 <high><!-- 0..1 Quantity(SimpleQuantity) High limit --></high>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "low" : { Quantity(SimpleQuantity) }, // Low limit
  "high" : { Quantity(SimpleQuantity) } // High limit
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Range.low [ Quantity(SimpleQuantity) ]; # 0..1 Low limit
  fhir:Range.high [ Quantity(SimpleQuantity) ]; # 0..1 High limit
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Range](datatypes.html#Range) | - No Changes |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Range](datatypes-definitions.html#Range "Range : A set of ordered Quantities defined by a low and high limit.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Set of values bounded by low and high + Rule: If present, low SHALL have a lower value than high Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [low](datatypes-definitions.html#Range.low "Range.low : The low limit. The boundary is inclusive.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Low limit |
| ... [high](datatypes-definitions.html#Range.high "Range.high : The high limit. The boundary is inclusive.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | High limit |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <low><!-- 0..1 Quantity(SimpleQuantity) Low limit --></low>
 <high><!-- 0..1 Quantity(SimpleQuantity) High limit --></high>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "low" : { Quantity(SimpleQuantity) }, // Low limit
  "high" : { Quantity(SimpleQuantity) } // High limit
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Range.low [ Quantity(SimpleQuantity) ]; # 0..1 Low limit
  fhir:Range.high [ Quantity(SimpleQuantity) ]; # 0..1 High limit
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Range](datatypes.html#Range) | - No Changes |

See the [Full Difference](diff.html) for further information

The `unit` and `code`/`system` elements of the `low` or `high` elements SHALL match.
If the `low` or `high` elements are missing, the meaning
is that the low or high boundaries are not known and therefore neither is the complete range.

The `comparator` flag on the `low` or `high` elements cannot be present. Note that the Range type should not be
used to represent out of range measurements: A quantity type with the comparator element should be used instead.

The low and the high values are inclusive and are assumed to have arbitrarily high precision; e.g. the range 1.5 to 2.5
includes 1.50, and 2.50 but not 1.49 or 2.51.

**Constraints**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **rng-2** | [Rule](conformance-rules.html#rule) | (base) | If present, low SHALL have a lower value than high | low.empty() or high.empty() or (low <= high) |

Range is used in the following places: [Dosage](dosage.html#Dosage), [SubstanceAmount](substanceamount.html#SubstanceAmount), [Population](population.html#Population), [UsageContext](metadatatypes.html#UsageContext), [Timing](datatypes.html#Timing), [ActivityDefinition](activitydefinition.html#activitydefinition), [AllergyIntolerance](allergyintolerance.html#allergyintolerance), [Condition](condition.html#condition), [DeviceRequest](devicerequest.html#devicerequest), [FamilyMemberHistory](familymemberhistory.html#familymemberhistory), [Goal](goal.html#goal), [Group](group.html#group), [Observation](observation.html#observation), [ObservationDefinition](observationdefinition.html#observationdefinition), [PlanDefinition](plandefinition.html#plandefinition), [Procedure](procedure.html#procedure), [RequestGroup](requestgroup.html#requestgroup), [RiskAssessment](riskassessment.html#riskassessment), [ServiceRequest](servicerequest.html#servicerequest), [SpecimenDefinition](specimendefinition.html#specimendefinition), [SubstanceReferenceInformation](substancereferenceinformation.html#substancereferenceinformation), [SubstanceSpecification](substancespecification.html#substancespecification) and [SupplyRequest](supplyrequest.html#supplyrequest)

## 2.24.0.9 Ratio

See also [Examples](datatypes-examples.html#Ratio), [Detailed Descriptions](datatypes-definitions.html#Ratio), [Mappings](datatypes-mappings.html#Ratio), [Profiles & Extensions](datatypes-extras.html#Ratio) and [R2 Conversions](datatypes-version-maps.html#Ratio).

A relationship between two Quantity values expressed as a numerator and a denominator.

The Ratio datatype should only be used to express a relationship of two numbers if the
relationship cannot be suitably expressed using a Quantity and a common unit. Where
the denominator value is known to be fixed to "1", Quantity should be used instead
of Ratio.

- [Structure](#tabs-Ratio-struc)
- [UML](#tabs-Ratio-uml)
- [XML](#tabs-Ratio-xml)
- [JSON](#tabs-Ratio-json)
- [Turtle](#tabs-Ratio-ttl)
- [R3 Diff](#tabs-Ratio-diff)
- [All](#tabs-Ratio-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Ratio](datatypes-definitions.html#Ratio "Ratio : A relationship of two Quantity values - expressed as a numerator and a denominator.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | A ratio of two Quantity values - a numerator and a denominator + Rule: Numerator and denominator SHALL both be present, or both are absent. If both are absent, there SHALL be some extension present Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [numerator](datatypes-definitions.html#Ratio.numerator "Ratio.numerator : The value of the numerator.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Quantity](datatypes.html#Quantity) | Numerator value |
| ... [denominator](datatypes-definitions.html#Ratio.denominator "Ratio.denominator : The value of the denominator.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Quantity](datatypes.html#Quantity) | Denominator value |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <numerator><!-- 0..1 Quantity Numerator value --></numerator>
 <denominator><!-- 0..1 Quantity Denominator value --></denominator>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "numerator" : { Quantity }, // Numerator value
  "denominator" : { Quantity } // Denominator value
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Ratio.numerator [ Quantity ]; # 0..1 Numerator value
  fhir:Ratio.denominator [ Quantity ]; # 0..1 Denominator value
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Ratio](datatypes.html#Ratio) | - No Changes |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Ratio](datatypes-definitions.html#Ratio "Ratio : A relationship of two Quantity values - expressed as a numerator and a denominator.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | A ratio of two Quantity values - a numerator and a denominator + Rule: Numerator and denominator SHALL both be present, or both are absent. If both are absent, there SHALL be some extension present Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [numerator](datatypes-definitions.html#Ratio.numerator "Ratio.numerator : The value of the numerator.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Quantity](datatypes.html#Quantity) | Numerator value |
| ... [denominator](datatypes-definitions.html#Ratio.denominator "Ratio.denominator : The value of the denominator.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Quantity](datatypes.html#Quantity) | Denominator value |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <numerator><!-- 0..1 Quantity Numerator value --></numerator>
 <denominator><!-- 0..1 Quantity Denominator value --></denominator>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "numerator" : { Quantity }, // Numerator value
  "denominator" : { Quantity } // Denominator value
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Ratio.numerator [ Quantity ]; # 0..1 Numerator value
  fhir:Ratio.denominator [ Quantity ]; # 0..1 Denominator value
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Ratio](datatypes.html#Ratio) | - No Changes |

See the [Full Difference](diff.html) for further information

Examples where a Quantity is typically used are rates, densities, concentrations.
Examples where a Ratio is used are: titers (e.g. 1:128); concentration ratios where
the denominator is significant (e.g. 5mg/10mL); observed frequencies (e.g. 2 repetitions/8 hr),
and where the numerator or denominator is an amount of a currency (no UCUM code for $ etc.).

Common factors in the numerator and denominator are not automatically cancelled out. Ratios are not
simply "structured numbers" - for example, blood pressure measurements (e.g. "120/60") are not ratios.

A proper ratio has both a numerator and a denominator; however, these are not mandatory in order
to allow an invalid ratio with an extension with further information.

**Constraints**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **rat-1** | [Rule](conformance-rules.html#rule) | (base) | Numerator and denominator SHALL both be present, or both are absent. If both are absent, there SHALL be some extension present | (numerator.empty() xor denominator.exists()) and (numerator.exists() or extension.exists()) |

The context of use may require particular types of Quantity for the numerator or denominator.

Ratio is used in the following places: [Dosage](dosage.html#Dosage), [Goal](goal.html#goal), [Medication](medication.html#medication), [MedicationAdministration](medicationadministration.html#medicationadministration), [MedicationKnowledge](medicationknowledge.html#medicationknowledge), [MedicinalProductIngredient](medicinalproductingredient.html#medicinalproductingredient), [MedicinalProductPharmaceutical](medicinalproductpharmaceutical.html#medicinalproductpharmaceutical), [NutritionOrder](nutritionorder.html#nutritionorder), [Observation](observation.html#observation), [ServiceRequest](servicerequest.html#servicerequest), [Substance](substance.html#substance) and [SubstanceSpecification](substancespecification.html#substancespecification)

## 2.24.0.10 Period

See also [Examples](datatypes-examples.html#Period), [Detailed Descriptions](datatypes-definitions.html#Period), [Mappings](datatypes-mappings.html#Period), [Profiles & Extensions](datatypes-extras.html#Period) and [R2 Conversions](datatypes-version-maps.html#Period).

A time period defined by a start and end date/time.

A period specifies a range of times. The context
of use will specify whether the entire range applies (e.g. "the patient
was an inpatient of the hospital for this time range") or one value
from the period applies (e.g. "give to the patient between 2 and 4 pm on 24-Jun 2013").

- [Structure](#tabs-Period-struc)
- [UML](#tabs-Period-uml)
- [XML](#tabs-Period-xml)
- [JSON](#tabs-Period-json)
- [Turtle](#tabs-Period-ttl)
- [R3 Diff](#tabs-Period-diff)
- [All](#tabs-Period-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Period](datatypes-definitions.html#Period "Period : A time period defined by a start and end date and optionally time.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Time range defined by start and end date/time + Rule: If present, start SHALL have a lower value than end Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [start](datatypes-definitions.html#Period.start "Period.start : The start of the period. The boundary is inclusive.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [dateTime](datatypes.html#dateTime) | Starting time with inclusive boundary |
| ... [end](datatypes-definitions.html#Period.end "Period.end : The end of the period. If the end of the period is missing, it means no end was known or planned at the time the instance was created. The start may be in the past, and the end date in the future, which means that period is expected/planned to end at that time.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [dateTime](datatypes.html#dateTime) | End time with inclusive boundary, if not ongoing |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <start value="[dateTime]"/><!-- ![??](lock.png) 0..1 Starting time with inclusive boundary -->
 <end value="[dateTime]"/><!-- ![??](lock.png) 0..1 End time with inclusive boundary, if not ongoing -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "start" : "<dateTime>", // C? Starting time with inclusive boundary
  "end" : "<dateTime>" // C? End time with inclusive boundary, if not ongoing
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Period.start [ dateTime ]; # 0..1 Starting time with inclusive boundary
  fhir:Period.end [ dateTime ]; # 0..1 End time with inclusive boundary, if not ongoing
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Period](datatypes.html#Period) | - No Changes |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Period](datatypes-definitions.html#Period "Period : A time period defined by a start and end date and optionally time.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Time range defined by start and end date/time + Rule: If present, start SHALL have a lower value than end Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [start](datatypes-definitions.html#Period.start "Period.start : The start of the period. The boundary is inclusive.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [dateTime](datatypes.html#dateTime) | Starting time with inclusive boundary |
| ... [end](datatypes-definitions.html#Period.end "Period.end : The end of the period. If the end of the period is missing, it means no end was known or planned at the time the instance was created. The start may be in the past, and the end date in the future, which means that period is expected/planned to end at that time.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [dateTime](datatypes.html#dateTime) | End time with inclusive boundary, if not ongoing |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <start value="[dateTime]"/><!-- ![??](lock.png) 0..1 Starting time with inclusive boundary -->
 <end value="[dateTime]"/><!-- ![??](lock.png) 0..1 End time with inclusive boundary, if not ongoing -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "start" : "<dateTime>", // C? Starting time with inclusive boundary
  "end" : "<dateTime>" // C? End time with inclusive boundary, if not ongoing
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Period.start [ dateTime ]; # 0..1 Starting time with inclusive boundary
  fhir:Period.end [ dateTime ]; # 0..1 End time with inclusive boundary, if not ongoing
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Period](datatypes.html#Period) | - No Changes |

See the [Full Difference](diff.html) for further information

If the `start` element is missing, the start of the period is not
known. If the `end` element is missing, it means that the period is ongoing,
or the start may be in the past, and the end date in the future, which means that period
is expected/planned to end at the specified time

The end value includes any matching date/time. For example, the period
2011-05-23 to 2011-05-27 includes all the times from the start of the 23rd May through to
the end of the 27th of May.

Period is used in the following places: [Address](datatypes.html#Address), [DataRequirement](metadatatypes.html#DataRequirement), [HumanName](datatypes.html#HumanName), [ContactPoint](datatypes.html#ContactPoint), [MarketingStatus](marketingstatus.html#MarketingStatus), [Identifier](datatypes.html#Identifier), [Timing](datatypes.html#Timing), [Account](account.html#account), [ActivityDefinition](activitydefinition.html#activitydefinition), [AllergyIntolerance](allergyintolerance.html#allergyintolerance), [Appointment](appointment.html#appointment), [AuditEvent](auditevent.html#auditevent), [BiologicallyDerivedProduct](biologicallyderivedproduct.html#biologicallyderivedproduct), [CarePlan](careplan.html#careplan), [CareTeam](careteam.html#careteam), [CatalogEntry](catalogentry.html#catalogentry), [ChargeItem](chargeitem.html#chargeitem), [ChargeItemDefinition](chargeitemdefinition.html#chargeitemdefinition), [Claim](claim.html#claim), [ClaimResponse](claimresponse.html#claimresponse), [ClinicalImpression](clinicalimpression.html#clinicalimpression), [CommunicationRequest](communicationrequest.html#communicationrequest), [Composition](composition.html#composition), [Condition](condition.html#condition), [Consent](consent.html#consent), [Contract](contract.html#contract), [Coverage](coverage.html#coverage), [CoverageEligibilityRequest](coverageeligibilityrequest.html#coverageeligibilityrequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#coverageeligibilityresponse), [DetectedIssue](detectedissue.html#detectedissue), [DeviceRequest](devicerequest.html#devicerequest), [DeviceUseStatement](deviceusestatement.html#deviceusestatement), [DiagnosticReport](diagnosticreport.html#diagnosticreport), [DocumentReference](documentreference.html#documentreference), [EffectEvidenceSynthesis](effectevidencesynthesis.html#effectevidencesynthesis), [Encounter](encounter.html#encounter), [Endpoint](endpoint.html#endpoint), [EpisodeOfCare](episodeofcare.html#episodeofcare), [EventDefinition](eventdefinition.html#eventdefinition), [Evidence](evidence.html#evidence), [EvidenceVariable](evidencevariable.html#evidencevariable), [ExplanationOfBenefit](explanationofbenefit.html#explanationofbenefit), [FamilyMemberHistory](familymemberhistory.html#familymemberhistory), [Flag](flag.html#flag), [Group](group.html#group), [HealthcareService](healthcareservice.html#healthcareservice), [InsurancePlan](insuranceplan.html#insuranceplan), [Library](library.html#library), [Measure](measure.html#measure), [MeasureReport](measurereport.html#measurereport), [Media](media.html#media), [MedicationAdministration](medicationadministration.html#medicationadministration), [MedicationRequest](medicationrequest.html#medicationrequest), [MedicationStatement](medicationstatement.html#medicationstatement), [MedicinalProductAuthorization](medicinalproductauthorization.html#medicinalproductauthorization), [NamingSystem](namingsystem.html#namingsystem), [Observation](observation.html#observation), [OrganizationAffiliation](organizationaffiliation.html#organizationaffiliation), [Patient](patient.html#patient), [PaymentReconciliation](paymentreconciliation.html#paymentreconciliation), [PlanDefinition](plandefinition.html#plandefinition), [Practitioner](practitioner.html#practitioner), [PractitionerRole](practitionerrole.html#practitionerrole), [Procedure](procedure.html#procedure), [Provenance](provenance.html#provenance), [Questionnaire](questionnaire.html#questionnaire), [RelatedPerson](relatedperson.html#relatedperson), [RequestGroup](requestgroup.html#requestgroup), [ResearchDefinition](researchdefinition.html#researchdefinition), [ResearchElementDefinition](researchelementdefinition.html#researchelementdefinition), [ResearchStudy](researchstudy.html#researchstudy), [ResearchSubject](researchsubject.html#researchsubject), [RiskAssessment](riskassessment.html#riskassessment), [RiskEvidenceSynthesis](riskevidencesynthesis.html#riskevidencesynthesis), [Schedule](schedule.html#schedule), [ServiceRequest](servicerequest.html#servicerequest), [Specimen](specimen.html#specimen), [SupplyDelivery](supplydelivery.html#supplydelivery), [SupplyRequest](supplyrequest.html#supplyrequest) and [Task](task.html#task)

## 2.24.0.11 SampledData

Normative Candidate Note: This DataType is not normative - it is still undergoing Trial Use while more experience is gathered.

See also [Examples](datatypes-examples.html#SampledData), [Detailed Descriptions](datatypes-definitions.html#SampledData), [Mappings](datatypes-mappings.html#SampledData), [Profiles & Extensions](datatypes-extras.html#SampledData) and [R2 Conversions](datatypes-version-maps.html#SampledData).

Data that comes from a series of measurements taken by a device, which may have upper and lower limits. The data type also supports more than one dimension in the data.

A SampledData provides a concise way to handle the data produced by devices that sample a particular physical state at a high frequency. A typical
use for this is for the output of an ECG or EKG device. The data type includes a series of raw decimal values (which are mostly simple integers), along with adjustments for scale and
factor. These are interpreted such that

```

original measured value[i] = SampledData.data[i] * SampledData.scaleFactor + SampledData.origin.value
```

- [Structure](#tabs-SampledData-struc)
- [UML](#tabs-SampledData-uml)
- [XML](#tabs-SampledData-xml)
- [JSON](#tabs-SampledData-json)
- [Turtle](#tabs-SampledData-ttl)
- [R3 Diff](#tabs-SampledData-diff)
- [All](#tabs-SampledData-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [SampledData](datatypes-definitions.html#SampledData "SampledData : A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [Element](element.html) | A series of measurements taken by a device Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [origin](datatypes-definitions.html#SampledData.origin "SampledData.origin : The base quantity that a measured value of zero represents. In addition, this provides the units of the entire measurement series.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Zero value and units |
| ... [period](datatypes-definitions.html#SampledData.period "SampledData.period : The length of time between sampling times, measured in milliseconds.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [decimal](datatypes.html#decimal) | Number of milliseconds between samples |
| ... [factor](datatypes-definitions.html#SampledData.factor "SampledData.factor : A correction factor that is applied to the sampled data points before they are added to the origin.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Multiply data by this before adding to origin |
| ... [lowerLimit](datatypes-definitions.html#SampledData.lowerLimit "SampledData.lowerLimit : The lower limit of detection of the measured points. This is needed if any of the data points have the value \"L\" (lower than detection limit).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Lower limit of detection |
| ... [upperLimit](datatypes-definitions.html#SampledData.upperLimit "SampledData.upperLimit : The upper limit of detection of the measured points. This is needed if any of the data points have the value \"U\" (higher than detection limit).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Upper limit of detection |
| ... [dimensions](datatypes-definitions.html#SampledData.dimensions "SampledData.dimensions : The number of sample points at each time point. If this value is greater than one, then the dimensions will be interlaced - all the sample points for a point in time will be recorded at once.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [positiveInt](datatypes.html#positiveInt) | Number of sample points at each time point |
| ... [data](datatypes-definitions.html#SampledData.data "SampledData.data : A series of data points which are decimal values separated by a single space (character u20). The special values \"E\" (error), \"L\" (below detection limit) and \"U\" (above detection limit) can also be used in place of a decimal value.") |  | 0..1 | [string](datatypes.html#string) | Decimal values with spaces, or "E" | "U" | "L" |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <origin><!-- 1..1 Quantity(SimpleQuantity) Zero value and units --></origin>
 <period value="[decimal]"/><!-- 1..1 Number of milliseconds between samples -->
 <factor value="[decimal]"/><!-- 0..1 Multiply data by this before adding to origin -->
 <lowerLimit value="[decimal]"/><!-- 0..1 Lower limit of detection -->
 <upperLimit value="[decimal]"/><!-- 0..1 Upper limit of detection -->
 <dimensions value="[positiveInt]"/><!-- 1..1 Number of sample points at each time point -->
 <data value="[string]"/><!-- 0..1 Decimal values with spaces, or "E" | "U" | "L" -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "origin" : { Quantity(SimpleQuantity) }, // R!  Zero value and units
  "period" : <decimal>, // R!  Number of milliseconds between samples
  "factor" : <decimal>, // Multiply data by this before adding to origin
  "lowerLimit" : <decimal>, // Lower limit of detection
  "upperLimit" : <decimal>, // Upper limit of detection
  "dimensions" : "<positiveInt>", // R!  Number of sample points at each time point
  "data" : "<string>" // Decimal values with spaces, or "E" | "U" | "L"
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:SampledData.origin [ Quantity(SimpleQuantity) ]; # 1..1 Zero value and units
  fhir:SampledData.period [ decimal ]; # 1..1 Number of milliseconds between samples
  fhir:SampledData.factor [ decimal ]; # 0..1 Multiply data by this before adding to origin
  fhir:SampledData.lowerLimit [ decimal ]; # 0..1 Lower limit of detection
  fhir:SampledData.upperLimit [ decimal ]; # 0..1 Upper limit of detection
  fhir:SampledData.dimensions [ positiveInt ]; # 1..1 Number of sample points at each time point
  fhir:SampledData.data [ string ]; # 0..1 Decimal values with spaces, or "E" | "U" | "L"
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [SampledData](datatypes.html#SampledData) |  |
| SampledData.factor | - Default Value "1" removed |
| SampledData.data | - Min Cardinality changed from 1 to 0 |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [SampledData](datatypes-definitions.html#SampledData "SampledData : A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [Element](element.html) | A series of measurements taken by a device Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [origin](datatypes-definitions.html#SampledData.origin "SampledData.origin : The base quantity that a measured value of zero represents. In addition, this provides the units of the entire measurement series.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Zero value and units |
| ... [period](datatypes-definitions.html#SampledData.period "SampledData.period : The length of time between sampling times, measured in milliseconds.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [decimal](datatypes.html#decimal) | Number of milliseconds between samples |
| ... [factor](datatypes-definitions.html#SampledData.factor "SampledData.factor : A correction factor that is applied to the sampled data points before they are added to the origin.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Multiply data by this before adding to origin |
| ... [lowerLimit](datatypes-definitions.html#SampledData.lowerLimit "SampledData.lowerLimit : The lower limit of detection of the measured points. This is needed if any of the data points have the value \"L\" (lower than detection limit).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Lower limit of detection |
| ... [upperLimit](datatypes-definitions.html#SampledData.upperLimit "SampledData.upperLimit : The upper limit of detection of the measured points. This is needed if any of the data points have the value \"U\" (higher than detection limit).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Upper limit of detection |
| ... [dimensions](datatypes-definitions.html#SampledData.dimensions "SampledData.dimensions : The number of sample points at each time point. If this value is greater than one, then the dimensions will be interlaced - all the sample points for a point in time will be recorded at once.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [positiveInt](datatypes.html#positiveInt) | Number of sample points at each time point |
| ... [data](datatypes-definitions.html#SampledData.data "SampledData.data : A series of data points which are decimal values separated by a single space (character u20). The special values \"E\" (error), \"L\" (below detection limit) and \"U\" (above detection limit) can also be used in place of a decimal value.") |  | 0..1 | [string](datatypes.html#string) | Decimal values with spaces, or "E" | "U" | "L" |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <origin><!-- 1..1 Quantity(SimpleQuantity) Zero value and units --></origin>
 <period value="[decimal]"/><!-- 1..1 Number of milliseconds between samples -->
 <factor value="[decimal]"/><!-- 0..1 Multiply data by this before adding to origin -->
 <lowerLimit value="[decimal]"/><!-- 0..1 Lower limit of detection -->
 <upperLimit value="[decimal]"/><!-- 0..1 Upper limit of detection -->
 <dimensions value="[positiveInt]"/><!-- 1..1 Number of sample points at each time point -->
 <data value="[string]"/><!-- 0..1 Decimal values with spaces, or "E" | "U" | "L" -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "origin" : { Quantity(SimpleQuantity) }, // R!  Zero value and units
  "period" : <decimal>, // R!  Number of milliseconds between samples
  "factor" : <decimal>, // Multiply data by this before adding to origin
  "lowerLimit" : <decimal>, // Lower limit of detection
  "upperLimit" : <decimal>, // Upper limit of detection
  "dimensions" : "<positiveInt>", // R!  Number of sample points at each time point
  "data" : "<string>" // Decimal values with spaces, or "E" | "U" | "L"
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:SampledData.origin [ Quantity(SimpleQuantity) ]; # 1..1 Zero value and units
  fhir:SampledData.period [ decimal ]; # 1..1 Number of milliseconds between samples
  fhir:SampledData.factor [ decimal ]; # 0..1 Multiply data by this before adding to origin
  fhir:SampledData.lowerLimit [ decimal ]; # 0..1 Lower limit of detection
  fhir:SampledData.upperLimit [ decimal ]; # 0..1 Upper limit of detection
  fhir:SampledData.dimensions [ positiveInt ]; # 1..1 Number of sample points at each time point
  fhir:SampledData.data [ string ]; # 0..1 Decimal values with spaces, or "E" | "U" | "L"
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [SampledData](datatypes.html#SampledData) |  |
| SampledData.factor | - Default Value "1" removed |
| SampledData.data | - Min Cardinality changed from 1 to 0 |

See the [Full Difference](diff.html) for further information

The digits are a set of decimal values separated by a single space (Unicode character u20).
In addition to decimal values, the special values "E" (error), "L" (below detection limit)
and "U" (above detection limit) can also be used. If there is more than one dimension, the
different dimensions are interlaced - all the data points for a particular time are
represented together.

SampledData is used in the following places: [Observation](observation.html#observation)

## 2.24.0.12 Identifier

See also [Examples](datatypes-examples.html#Identifier), [Detailed Descriptions](datatypes-definitions.html#Identifier), [Mappings](datatypes-mappings.html#Identifier), [Profiles & Extensions](datatypes-extras.html#Identifier) and [R2 Conversions](datatypes-version-maps.html#Identifier).

A numeric or alphanumeric string that is associated with a single object or entity within a given system.
Typically, identifiers are used to connect content in resources to external content available in other frameworks or protocols.
Identifiers are associated with objects and may be changed or retired due to human or system process and
errors.

- [Structure](#tabs-Identifier-struc)
- [UML](#tabs-Identifier-uml)
- [XML](#tabs-Identifier-xml)
- [JSON](#tabs-Identifier-json)
- [Turtle](#tabs-Identifier-ttl)
- [R3 Diff](#tabs-Identifier-diff)
- [All](#tabs-Identifier-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Identifier](datatypes-definitions.html#Identifier "Identifier : An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business identifiers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | An identifier intended for computation Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [use](datatypes-definitions.html#Identifier.use "Identifier.use : The purpose of this identifier.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | usual | official | temp | secondary | old (If known) [IdentifierUse](valueset-identifier-use.html "Identifies the purpose for this identifier, if known .") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [type](datatypes-definitions.html#Identifier.type "Identifier.type : A coded type for the identifier that can be used to determine which identifier to use for a specific purpose.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Description of identifier [IdentifierType](valueset-identifier-type.html "A coded type for an identifier that can be used to determine which identifier to use for a specific purpose.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [system](datatypes-definitions.html#Identifier.system "Identifier.system : Establishes the namespace for the value - that is, a URL that describes a set values that are unique.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | The namespace for the identifier value |
| ... [value](datatypes-definitions.html#Identifier.value "Identifier.value : The portion of the identifier typically relevant to the user and which is unique within the context of the system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | The value that is unique |
| ... [period](datatypes-definitions.html#Identifier.period "Identifier.period : Time period during which identifier is/was valid for use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Time period when id is/was valid for use |
| ... [assigner](datatypes-definitions.html#Identifier.assigner "Identifier.assigner : Organization that issued/manages the identifier.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that issued id (may be just text) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <use value="[code]"/><!-- 0..1 usual | official | temp | secondary | old (If known) -->
 <type><!-- 0..1 CodeableConcept Description of identifier --></type>
 <system value="[uri]"/><!-- 0..1 The namespace for the identifier value -->
 <value value="[string]"/><!-- 0..1 The value that is unique -->
 <period><!-- 0..1 Period Time period when id is/was valid for use --></period>
 <assigner><!-- 0..1 Reference(Organization) Organization that issued id (may be just text) --></assigner>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "use" : "<code>", // usual | official | temp | secondary | old (If known)
  "type" : { CodeableConcept }, // Description of identifier
  "system" : "<uri>", // The namespace for the identifier value
  "value" : "<string>", // The value that is unique
  "period" : { Period }, // Time period when id is/was valid for use
  "assigner" : { Reference(Organization) } // Organization that issued id (may be just text)
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Identifier.use [ code ]; # 0..1 usual | official | temp | secondary | old (If known)
  fhir:Identifier.type [ CodeableConcept ]; # 0..1 Description of identifier
  fhir:Identifier.system [ uri ]; # 0..1 The namespace for the identifier value
  fhir:Identifier.value [ string ]; # 0..1 The value that is unique
  fhir:Identifier.period [ Period ]; # 0..1 Time period when id is/was valid for use
  fhir:Identifier.assigner [ Reference(Organization) ]; # 0..1 Organization that issued id (may be just text)
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Identifier](datatypes.html#Identifier) |  |
| Identifier.use | - Change value set from http://hl7.org/fhir/ValueSet/identifier-use to http://hl7.org/fhir/ValueSet/identifier-use|4.0.1 |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Identifier](datatypes-definitions.html#Identifier "Identifier : An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business identifiers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | An identifier intended for computation Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [use](datatypes-definitions.html#Identifier.use "Identifier.use : The purpose of this identifier.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | usual | official | temp | secondary | old (If known) [IdentifierUse](valueset-identifier-use.html "Identifies the purpose for this identifier, if known .") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [type](datatypes-definitions.html#Identifier.type "Identifier.type : A coded type for the identifier that can be used to determine which identifier to use for a specific purpose.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Description of identifier [IdentifierType](valueset-identifier-type.html "A coded type for an identifier that can be used to determine which identifier to use for a specific purpose.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [system](datatypes-definitions.html#Identifier.system "Identifier.system : Establishes the namespace for the value - that is, a URL that describes a set values that are unique.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | The namespace for the identifier value |
| ... [value](datatypes-definitions.html#Identifier.value "Identifier.value : The portion of the identifier typically relevant to the user and which is unique within the context of the system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | The value that is unique |
| ... [period](datatypes-definitions.html#Identifier.period "Identifier.period : Time period during which identifier is/was valid for use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Time period when id is/was valid for use |
| ... [assigner](datatypes-definitions.html#Identifier.assigner "Identifier.assigner : Organization that issued/manages the identifier.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that issued id (may be just text) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <use value="[code]"/><!-- 0..1 usual | official | temp | secondary | old (If known) -->
 <type><!-- 0..1 CodeableConcept Description of identifier --></type>
 <system value="[uri]"/><!-- 0..1 The namespace for the identifier value -->
 <value value="[string]"/><!-- 0..1 The value that is unique -->
 <period><!-- 0..1 Period Time period when id is/was valid for use --></period>
 <assigner><!-- 0..1 Reference(Organization) Organization that issued id (may be just text) --></assigner>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "use" : "<code>", // usual | official | temp | secondary | old (If known)
  "type" : { CodeableConcept }, // Description of identifier
  "system" : "<uri>", // The namespace for the identifier value
  "value" : "<string>", // The value that is unique
  "period" : { Period }, // Time period when id is/was valid for use
  "assigner" : { Reference(Organization) } // Organization that issued id (may be just text)
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Identifier.use [ code ]; # 0..1 usual | official | temp | secondary | old (If known)
  fhir:Identifier.type [ CodeableConcept ]; # 0..1 Description of identifier
  fhir:Identifier.system [ uri ]; # 0..1 The namespace for the identifier value
  fhir:Identifier.value [ string ]; # 0..1 The value that is unique
  fhir:Identifier.period [ Period ]; # 0..1 Time period when id is/was valid for use
  fhir:Identifier.assigner [ Reference(Organization) ]; # 0..1 Organization that issued id (may be just text)
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Identifier](datatypes.html#Identifier) |  |
| Identifier.use | - Change value set from http://hl7.org/fhir/ValueSet/identifier-use to http://hl7.org/fhir/ValueSet/identifier-use|4.0.1 |

See the [Full Difference](diff.html) for further information

The `value` SHALL be unique within the defined `system`
and have a consistent meaning wherever it appears. Identifier.system is always case sensitive. `Identifier.value` is
to be treated as case sensitive unless knowledge of the `Identifier.system` allows the processer to be confident
that non-case-sensitive processing is safe.

The `system` is a URI that defines a set of identifiers (i.e. how the `value` is made unique).
It might be a specific application or a recognized standard/specification for a set of identifiers
or a way of making identifiers unique.
FHIR defines [some useful or important system URIs directly](identifier-registry.html). Here are some
example identifier namespaces:

- `http://hl7.org/fhir/sid/us-ssn` for United States Social Security Number (SSN) values
- `http://ns.electronichealth.net.au/id/hi/ihi/1.0` for Australian Individual Healthcare Identifier (IHI) numbers
- `urn:ietf:rfc:3986` for when the value of the identifier is itself a globally unique URI

If the system is a URL, it SHOULD resolve. Resolution might be to a web page that describes the identifier
system and/or supports look-up of identifiers. Alternatively, it could be to a [NamingSystem](namingsystem.html) resource
instance. Resolvable URLs are generally preferred by implementers over non-resolvable URNs, particularly
opaque URNs such as OIDs (urn:oid:) or UUIDs (urn:uuid:). If used, OIDs and UUIDs may be registered in
the [HL7 OID registry ![](external.png)](http://hl7.org/oid) and SHOULD be registered if the content is shared
or exchanged across institutional boundaries.

It is up to the implementer organization to determine an appropriate URL or URN structure that will
avoid collisions and to manage that space (and the resolvability of URLs) over time.

Note that the scope of a given identifier system may extend beyond identifiers that might be captured
by a single resource. For example, some systems might draw all "order" identifiers from a single
namespace, though some might be used on [MedicationRequest](medicationrequest.html) while
others would appear on [ServiceRequest](servicerequest.html).

If the identifier value itself is naturally a globally unique URI (e.g. an OID, a UUID, or a URI with no trailing local part),
then the `system` SHALL be "`urn:ietf:rfc:3986`", and the URI is in the `value`
(OIDs and UUIDs using urn:oid: and urn:uuid: - see [note on the V3 mapping](datatypes-mappings.html#ii) and the [examples](datatypes-examples.html#Identifier)).
Naturally globally unique identifiers are those for which no [system has been assigned](identifier-registry.html) and where the value of the identifier is reasonably
expected to not be re-used. Typically, these are absolute URIs of some kind.

In some cases, the system might not be known - only the value is known (e.g. a simple device that scans a barcode),
or the system is known implicitly (simple exchange in a limited context, often driven by barcode readers).
In this case, no useful matching may be performed using the value unless the system can be safely inferred by the
context. Applications should provide a `system` wherever possible, as information sharing in a wider context
is very likely to arise eventually, and values without a system are inherently limited in use.

In addition to the `system` (which provides a uniqueness scope) and the `value`, identifiers may also have a
`type`, which may be useful when a system encounters identifiers with unknown system values.
Note, however, that the type of an identifier is not a well-controlled vocabulary with wide variations
in practice. The `type` deals only with general categories of identifiers and SHOULD not be
used for codes that correspond 1..1 with the Identifier.system. Some identifiers may fall into multiple
categories due to variations in common usage.

The `assigner` is used to indicate what registry/state/facility/etc. assigned the identifier.
As a [Reference](references.html), the assigner can include just a text description in the `display`.

**Constraints**

**Terminology Bindings**

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Identifier.use | Identifies the purpose for this identifier, if known . | [Required](terminologies.html#required) | [IdentifierUse](valueset-identifier-use.html) |
| Identifier.type | A coded type for an identifier that can be used to determine which identifier to use for a specific purpose. | [Extensible](terminologies.html#extensible) | [Identifier Type Codes](valueset-identifier-type.html) |

Identifier is used in the following places: [Reference](references.html#Reference), [ProductShelfLife](productshelflife.html#ProductShelfLife), [Account](account.html#account), [ActivityDefinition](activitydefinition.html#activitydefinition), [AdverseEvent](adverseevent.html#adverseevent), [AllergyIntolerance](allergyintolerance.html#allergyintolerance), [Appointment](appointment.html#appointment), [AppointmentResponse](appointmentresponse.html#appointmentresponse), [Basic](basic.html#basic), [BiologicallyDerivedProduct](biologicallyderivedproduct.html#biologicallyderivedproduct), [BodyStructure](bodystructure.html#bodystructure), [Bundle](bundle.html#bundle), [CarePlan](careplan.html#careplan), [CareTeam](careteam.html#careteam), [CatalogEntry](catalogentry.html#catalogentry), [ChargeItem](chargeitem.html#chargeitem), [ChargeItemDefinition](chargeitemdefinition.html#chargeitemdefinition), [Claim](claim.html#claim), [ClaimResponse](claimresponse.html#claimresponse), [ClinicalImpression](clinicalimpression.html#clinicalimpression), [CodeSystem](codesystem.html#codesystem), [Communication](communication.html#communication), [CommunicationRequest](communicationrequest.html#communicationrequest), [Composition](composition.html#composition), [ConceptMap](conceptmap.html#conceptmap), [Condition](condition.html#condition), [Consent](consent.html#consent), [Contract](contract.html#contract), [Coverage](coverage.html#coverage), [CoverageEligibilityRequest](coverageeligibilityrequest.html#coverageeligibilityrequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#coverageeligibilityresponse), [DetectedIssue](detectedissue.html#detectedissue), [Device](device.html#device), [DeviceDefinition](devicedefinition.html#devicedefinition), [DeviceMetric](devicemetric.html#devicemetric), [DeviceRequest](devicerequest.html#devicerequest), [DeviceUseStatement](deviceusestatement.html#deviceusestatement), [DiagnosticReport](diagnosticreport.html#diagnosticreport), [DocumentManifest](documentmanifest.html#documentmanifest), [DocumentReference](documentreference.html#documentreference), [EffectEvidenceSynthesis](effectevidencesynthesis.html#effectevidencesynthesis), [Encounter](encounter.html#encounter), [Endpoint](endpoint.html#endpoint), [EnrollmentRequest](enrollmentrequest.html#enrollmentrequest), [EnrollmentResponse](enrollmentresponse.html#enrollmentresponse), [EpisodeOfCare](episodeofcare.html#episodeofcare), [EventDefinition](eventdefinition.html#eventdefinition), [Evidence](evidence.html#evidence), [EvidenceVariable](evidencevariable.html#evidencevariable), [ExampleScenario](examplescenario.html#examplescenario), [ExplanationOfBenefit](explanationofbenefit.html#explanationofbenefit), [FamilyMemberHistory](familymemberhistory.html#familymemberhistory), [Flag](flag.html#flag), [Goal](goal.html#goal), [Group](group.html#group), [GuidanceResponse](guidanceresponse.html#guidanceresponse), [HealthcareService](healthcareservice.html#healthcareservice), [ImagingStudy](imagingstudy.html#imagingstudy), [Immunization](immunization.html#immunization), [ImmunizationEvaluation](immunizationevaluation.html#immunizationevaluation), [ImmunizationRecommendation](immunizationrecommendation.html#immunizationrecommendation), [InsurancePlan](insuranceplan.html#insuranceplan), [Invoice](invoice.html#invoice), [Library](library.html#library), [List](list.html#list), [Location](location.html#location), [Measure](measure.html#measure), [MeasureReport](measurereport.html#measurereport), [Media](media.html#media), [Medication](medication.html#medication), [MedicationAdministration](medicationadministration.html#medicationadministration), [MedicationDispense](medicationdispense.html#medicationdispense), [MedicationRequest](medicationrequest.html#medicationrequest), [MedicationStatement](medicationstatement.html#medicationstatement), [MedicinalProduct](medicinalproduct.html#medicinalproduct), [MedicinalProductAuthorization](medicinalproductauthorization.html#medicinalproductauthorization), [MedicinalProductIngredient](medicinalproductingredient.html#medicinalproductingredient), [MedicinalProductPackaged](medicinalproductpackaged.html#medicinalproductpackaged), [MedicinalProductPharmaceutical](medicinalproductpharmaceutical.html#medicinalproductpharmaceutical), [MessageDefinition](messagedefinition.html#messagedefinition), [MolecularSequence](molecularsequence.html#molecularsequence), [NutritionOrder](nutritionorder.html#nutritionorder), [Observation](observation.html#observation), [ObservationDefinition](observationdefinition.html#observationdefinition), [Organization](organization.html#organization), [OrganizationAffiliation](organizationaffiliation.html#organizationaffiliation), [Patient](patient.html#patient), [PaymentNotice](paymentnotice.html#paymentnotice), [PaymentReconciliation](paymentreconciliation.html#paymentreconciliation), [Person](person.html#person), [PlanDefinition](plandefinition.html#plandefinition), [Practitioner](practitioner.html#practitioner), [PractitionerRole](practitionerrole.html#practitionerrole), [Procedure](procedure.html#procedure), [Questionnaire](questionnaire.html#questionnaire), [QuestionnaireResponse](questionnaireresponse.html#questionnaireresponse), [RelatedPerson](relatedperson.html#relatedperson), [RequestGroup](requestgroup.html#requestgroup), [ResearchDefinition](researchdefinition.html#researchdefinition), [ResearchElementDefinition](researchelementdefinition.html#researchelementdefinition), [ResearchStudy](researchstudy.html#researchstudy), [ResearchSubject](researchsubject.html#researchsubject), [RiskAssessment](riskassessment.html#riskassessment), [RiskEvidenceSynthesis](riskevidencesynthesis.html#riskevidencesynthesis), [Schedule](schedule.html#schedule), [ServiceRequest](servicerequest.html#servicerequest), [Slot](slot.html#slot), [Specimen](specimen.html#specimen), [SpecimenDefinition](specimendefinition.html#specimendefinition), [StructureDefinition](structuredefinition.html#structuredefinition), [StructureMap](structuremap.html#structuremap), [Substance](substance.html#substance), [SubstanceNucleicAcid](substancenucleicacid.html#substancenucleicacid), [SubstanceProtein](substanceprotein.html#substanceprotein), [SubstanceReferenceInformation](substancereferenceinformation.html#substancereferenceinformation), [SubstanceSourceMaterial](substancesourcematerial.html#substancesourcematerial), [SubstanceSpecification](substancespecification.html#substancespecification), [SupplyDelivery](supplydelivery.html#supplydelivery), [SupplyRequest](supplyrequest.html#supplyrequest), [Task](task.html#task), [TestReport](testreport.html#testreport), [TestScript](testscript.html#testscript), [ValueSet](valueset.html#valueset) and [VisionPrescription](visionprescription.html#visionprescription)

## 2.24.0.13 HumanName

See also [Examples](datatypes-examples.html#HumanName), [Detailed Descriptions](datatypes-definitions.html#HumanName), [Mappings](datatypes-mappings.html#HumanName), [Profiles & Extensions](datatypes-extras.html#HumanName) and [R2 Conversions](datatypes-version-maps.html#HumanName).

A name of a human with text, parts and usage information.

Names may be changed or repudiated. People may have different names in different
contexts. Names may be divided into parts of different type that have variable
significance depending on context, though the division into parts is not always
significant. With personal names, the different parts might or might not be imbued with
some implicit meaning; various cultures associate different importance with the
name parts and the degree to which systems SHALL care about name parts around the
world varies widely.

- [Structure](#tabs-HumanName-struc)
- [UML](#tabs-HumanName-uml)
- [XML](#tabs-HumanName-xml)
- [JSON](#tabs-HumanName-json)
- [Turtle](#tabs-HumanName-ttl)
- [R3 Diff](#tabs-HumanName-diff)
- [All](#tabs-HumanName-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [HumanName](datatypes-definitions.html#HumanName "HumanName : A human's name with the ability to identify parts and usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Name of a human - parts and usage Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [use](datatypes-definitions.html#HumanName.use "HumanName.use : Identifies the purpose for this name.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | usual | official | temp | nickname | anonymous | old | maiden [NameUse](valueset-name-use.html "The use of a human name.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [text](datatypes-definitions.html#HumanName.text "HumanName.text : Specifies the entire name as it should be displayed e.g. on an application UI. This may be provided instead of or as well as the specific parts.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Text representation of the full name |
| ... [family](datatypes-definitions.html#HumanName.family "HumanName.family : The part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Family name (often called 'Surname') |
| ... [given](datatypes-definitions.html#HumanName.given "HumanName.given : Given name.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Given names (not always 'first'). Includes middle names This repeating element order: Given Names appear in the correct order for presenting the name |
| ... [prefix](datatypes-definitions.html#HumanName.prefix "HumanName.prefix : Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the name.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Parts that come before the name This repeating element order: Prefixes appear in the correct order for presenting the name |
| ... [suffix](datatypes-definitions.html#HumanName.suffix "HumanName.suffix : Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the name.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Parts that come after the name This repeating element order: Suffixes appear in the correct order for presenting the name |
| ... [period](datatypes-definitions.html#HumanName.period "HumanName.period : Indicates the period of time when this name was valid for the named person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Time period when name was/is in use |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <use value="[code]"/><!-- 0..1 usual | official | temp | nickname | anonymous | old | maiden -->
 <text value="[string]"/><!-- 0..1 Text representation of the full name -->
 <family value="[string]"/><!-- 0..1 Family name (often called 'Surname') -->
 <given value="[string]"/><!-- 0..* Given names (not always 'first'). Includes middle names -->
 <prefix value="[string]"/><!-- 0..* Parts that come before the name -->
 <suffix value="[string]"/><!-- 0..* Parts that come after the name -->
 <period><!-- 0..1 Period Time period when name was/is in use --></period>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "use" : "<code>", // usual | official | temp | nickname | anonymous | old | maiden
  "text" : "<string>", // Text representation of the full name
  "family" : "<string>", // Family name (often called 'Surname')
  "given" : ["<string>"], // Given names (not always 'first'). Includes middle names
  "prefix" : ["<string>"], // Parts that come before the name
  "suffix" : ["<string>"], // Parts that come after the name
  "period" : { Period } // Time period when name was/is in use
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:HumanName.use [ code ]; # 0..1 usual | official | temp | nickname | anonymous | old | maiden
  fhir:HumanName.text [ string ]; # 0..1 Text representation of the full name
  fhir:HumanName.family [ string ]; # 0..1 Family name (often called 'Surname')
  fhir:HumanName.given [ string ], ... ; # 0..* Given names (not always 'first'). Includes middle names
  fhir:HumanName.prefix [ string ], ... ; # 0..* Parts that come before the name
  fhir:HumanName.suffix [ string ], ... ; # 0..* Parts that come after the name
  fhir:HumanName.period [ Period ]; # 0..1 Time period when name was/is in use
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [HumanName](datatypes.html#HumanName) |  |
| HumanName.use | - Change value set from http://hl7.org/fhir/ValueSet/name-use to http://hl7.org/fhir/ValueSet/name-use|4.0.1 |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [HumanName](datatypes-definitions.html#HumanName "HumanName : A human's name with the ability to identify parts and usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Name of a human - parts and usage Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [use](datatypes-definitions.html#HumanName.use "HumanName.use : Identifies the purpose for this name.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | usual | official | temp | nickname | anonymous | old | maiden [NameUse](valueset-name-use.html "The use of a human name.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [text](datatypes-definitions.html#HumanName.text "HumanName.text : Specifies the entire name as it should be displayed e.g. on an application UI. This may be provided instead of or as well as the specific parts.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Text representation of the full name |
| ... [family](datatypes-definitions.html#HumanName.family "HumanName.family : The part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Family name (often called 'Surname') |
| ... [given](datatypes-definitions.html#HumanName.given "HumanName.given : Given name.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Given names (not always 'first'). Includes middle names This repeating element order: Given Names appear in the correct order for presenting the name |
| ... [prefix](datatypes-definitions.html#HumanName.prefix "HumanName.prefix : Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the name.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Parts that come before the name This repeating element order: Prefixes appear in the correct order for presenting the name |
| ... [suffix](datatypes-definitions.html#HumanName.suffix "HumanName.suffix : Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the name.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Parts that come after the name This repeating element order: Suffixes appear in the correct order for presenting the name |
| ... [period](datatypes-definitions.html#HumanName.period "HumanName.period : Indicates the period of time when this name was valid for the named person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Time period when name was/is in use |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <use value="[code]"/><!-- 0..1 usual | official | temp | nickname | anonymous | old | maiden -->
 <text value="[string]"/><!-- 0..1 Text representation of the full name -->
 <family value="[string]"/><!-- 0..1 Family name (often called 'Surname') -->
 <given value="[string]"/><!-- 0..* Given names (not always 'first'). Includes middle names -->
 <prefix value="[string]"/><!-- 0..* Parts that come before the name -->
 <suffix value="[string]"/><!-- 0..* Parts that come after the name -->
 <period><!-- 0..1 Period Time period when name was/is in use --></period>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "use" : "<code>", // usual | official | temp | nickname | anonymous | old | maiden
  "text" : "<string>", // Text representation of the full name
  "family" : "<string>", // Family name (often called 'Surname')
  "given" : ["<string>"], // Given names (not always 'first'). Includes middle names
  "prefix" : ["<string>"], // Parts that come before the name
  "suffix" : ["<string>"], // Parts that come after the name
  "period" : { Period } // Time period when name was/is in use
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:HumanName.use [ code ]; # 0..1 usual | official | temp | nickname | anonymous | old | maiden
  fhir:HumanName.text [ string ]; # 0..1 Text representation of the full name
  fhir:HumanName.family [ string ]; # 0..1 Family name (often called 'Surname')
  fhir:HumanName.given [ string ], ... ; # 0..* Given names (not always 'first'). Includes middle names
  fhir:HumanName.prefix [ string ], ... ; # 0..* Parts that come before the name
  fhir:HumanName.suffix [ string ], ... ; # 0..* Parts that come after the name
  fhir:HumanName.period [ Period ]; # 0..1 Time period when name was/is in use
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [HumanName](datatypes.html#HumanName) |  |
| HumanName.use | - Change value set from http://hl7.org/fhir/ValueSet/name-use to http://hl7.org/fhir/ValueSet/name-use|4.0.1 |

See the [Full Difference](diff.html) for further information

This table summarizes where common parts of a person's name are found.

|  |  |  |
| --- | --- | --- |
| **Name** | **Example** | **Destination / Comments** |
| Surname | Smith | Family Name |
| First name | John | Given Name |
| Title | Mr. | Prefix |
| Middle Name | Samuel | Subsequent Given Names |
| Patronymic | bin Osman | Family Name |
| Multiple family names | Carreño Quiñones | Family Name. See note below about decomposition of family name |
| Initials | Q. | Given Name as initial ("." recommended) |
| Nick Name | Jock | Given name, with Use = common |
| Qualifications | PhD | Suffix |
| Honorifics | Senior | Suffix |
| Voorvoegsel / Nobility | van Beethoven | Family Name. See note below about decomposition of family name |

For further information, including all [W3C International Examples ![](external.png)](http://www.w3.org/International/questions/qa-personal-names),
consult the [examples](datatypes-examples.html#HumanName). **Note: Implementers should read the name examples for a full
understanding of how name works.**

The multiple given parts and family name combine to form a single name.
Where a person has alternate names that may be used in place of each other (e.g. Nicknames, Aliases),
these are different instances of `HumanName`.

The text element specifies the entire name as it should be displayed e.g. in an application UI.
This may be provided instead of or as well as the specific parts. Applications updating a
name SHALL ensure that when both text and parts are present, no content is included in the
text that isn't found in a part. The correct order of assembly of the parts is culture
dependent: the order of the parts within a given part type has significance and SHALL be
observed. The appropriate order between family name and given names depends on culture and context of use.
Note that there is an [extension](extension-humanname-assembly-order.html) for the few times name
assembly order is not fixed by the culture.

The given name parts may contain whitespace, though generally they don't. Initials may be used in place of
the full name if that is all that is recorded. Systems that operate across cultures should
generally rely on the text form for presentation and use the parts for index/search functionality.
For this reason, applications SHOULD populate the text element for future robustness.

In some cultures (e.g. German, Dutch, Spanish, Portuguese), family names are complex and composed of
various parts that may need to be managed separately, e.g. they have differing significance
for searching. In these cases, the full family name is populated in `family`,
and a decomposition of the name can be provided using the `family` extensions
[own-name](extension-humanname-own-name.html),
[own-prefix](extension-humanname-own-prefix.html),
[partner-name](extension-humanname-partner-name.html),
[partner-prefix](extension-humanname-partner-prefix.html),
[fathers-family](extension-humanname-fathers-family.html) and
[mothers-family](extension-humanname-mothers-family.html).

For robust search, servers should search the parts of a family name independently.
E.g. Searching either Carreno or Quinones should match a family name of "Carreno Quinones".
HL7 affiliates, and others producing implementation guides, may make more specific recommendations about how search should work
in specific cultures or environments.

**Constraints**

**Terminology Bindings**

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| HumanName.use | The use of a human name. | [Required](terminologies.html#required) | [NameUse](valueset-name-use.html) |

HumanName is used in the following places: [InsurancePlan](insuranceplan.html#insuranceplan), [Organization](organization.html#organization), [Patient](patient.html#patient), [Person](person.html#person), [Practitioner](practitioner.html#practitioner) and [RelatedPerson](relatedperson.html#relatedperson)

## 2.24.0.14 Address

See also [Examples](datatypes-examples.html#Address), [Detailed Descriptions](datatypes-definitions.html#Address), [Mappings](datatypes-mappings.html#Address), [Profiles & Extensions](datatypes-extras.html#Address) and [R2 Conversions](datatypes-version-maps.html#Address).

An address expressed using postal conventions (as opposed to GPS or other location definition
formats). This data type may be used to convey addresses for use in delivering mail as well
as for visiting locations which might not be valid for mail delivery. There are a variety
of postal address formats defined around the world.

- [Structure](#tabs-Address-struc)
- [UML](#tabs-Address-uml)
- [XML](#tabs-Address-xml)
- [JSON](#tabs-Address-json)
- [Turtle](#tabs-Address-ttl)
- [R3 Diff](#tabs-Address-diff)
- [All](#tabs-Address-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Address](datatypes-definitions.html#Address "Address : An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | An address expressed using postal conventions (as opposed to GPS or other location definition formats) Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [use](datatypes-definitions.html#Address.use "Address.use : The purpose of this address.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | home | work | temp | old | billing - purpose of this address [AddressUse](valueset-address-use.html "The use of an address.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [type](datatypes-definitions.html#Address.type "Address.type : Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | postal | physical | both [AddressType](valueset-address-type.html "The type of an address (physical / postal).") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [text](datatypes-definitions.html#Address.text "Address.text : Specifies the entire address as it should be displayed e.g. on a postal label. This may be provided instead of or as well as the specific parts.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Text representation of the address |
| ... [line](datatypes-definitions.html#Address.line "Address.line : This component contains the house number, apartment number, street name, street direction,  P.O. Box number, delivery hints, and similar address information.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Street name, number, direction & P.O. Box etc. This repeating element order: The order in which lines should appear in an address label |
| ... [city](datatypes-definitions.html#Address.city "Address.city : The name of the city, town, suburb, village or other community or delivery center.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of city, town etc. |
| ... [district](datatypes-definitions.html#Address.district "Address.district : The name of the administrative area (county).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | District name (aka county) |
| ... [state](datatypes-definitions.html#Address.state "Address.state : Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Sub-unit of country (abbreviations ok) |
| ... [postalCode](datatypes-definitions.html#Address.postalCode "Address.postalCode : A postal code designating a region defined by the postal service.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Postal code for area |
| ... [country](datatypes-definitions.html#Address.country "Address.country : Country - a nation as commonly understood or generally accepted.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Country (e.g. can be ISO 3166 2 or 3 letter code) |
| ... [period](datatypes-definitions.html#Address.period "Address.period : Time period when address was/is in use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Time period when address was/is in use |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <use value="[code]"/><!-- 0..1 home | work | temp | old | billing - purpose of this address -->
 <type value="[code]"/><!-- 0..1 postal | physical | both -->
 <text value="[string]"/><!-- 0..1 Text representation of the address -->
 <line value="[string]"/><!-- 0..* Street name, number, direction & P.O. Box etc. -->
 <city value="[string]"/><!-- 0..1 Name of city, town etc. -->
 <district value="[string]"/><!-- 0..1 District name (aka county) -->
 <state value="[string]"/><!-- 0..1 Sub-unit of country (abbreviations ok) -->
 <postalCode value="[string]"/><!-- 0..1 Postal code for area -->
 <country value="[string]"/><!-- 0..1 Country (e.g. can be ISO 3166 2 or 3 letter code) -->
 <period><!-- 0..1 Period Time period when address was/is in use --></period>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "use" : "<code>", // home | work | temp | old | billing - purpose of this address
  "type" : "<code>", // postal | physical | both
  "text" : "<string>", // Text representation of the address
  "line" : ["<string>"], // Street name, number, direction & P.O. Box etc.
  "city" : "<string>", // Name of city, town etc.
  "district" : "<string>", // District name (aka county)
  "state" : "<string>", // Sub-unit of country (abbreviations ok)
  "postalCode" : "<string>", // Postal code for area
  "country" : "<string>", // Country (e.g. can be ISO 3166 2 or 3 letter code)
  "period" : { Period } // Time period when address was/is in use
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Address.use [ code ]; # 0..1 home | work | temp | old | billing - purpose of this address
  fhir:Address.type [ code ]; # 0..1 postal | physical | both
  fhir:Address.text [ string ]; # 0..1 Text representation of the address
  fhir:Address.line [ string ], ... ; # 0..* Street name, number, direction & P.O. Box etc.
  fhir:Address.city [ string ]; # 0..1 Name of city, town etc.
  fhir:Address.district [ string ]; # 0..1 District name (aka county)
  fhir:Address.state [ string ]; # 0..1 Sub-unit of country (abbreviations ok)
  fhir:Address.postalCode [ string ]; # 0..1 Postal code for area
  fhir:Address.country [ string ]; # 0..1 Country (e.g. can be ISO 3166 2 or 3 letter code)
  fhir:Address.period [ Period ]; # 0..1 Time period when address was/is in use
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Address](datatypes.html#Address) |  |
| Address.use | - Change value set from http://hl7.org/fhir/ValueSet/address-use to http://hl7.org/fhir/ValueSet/address-use|4.0.1 |
| Address.type | - Change value set from http://hl7.org/fhir/ValueSet/address-type to http://hl7.org/fhir/ValueSet/address-type|4.0.1 |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Address](datatypes-definitions.html#Address "Address : An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | An address expressed using postal conventions (as opposed to GPS or other location definition formats) Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [use](datatypes-definitions.html#Address.use "Address.use : The purpose of this address.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | home | work | temp | old | billing - purpose of this address [AddressUse](valueset-address-use.html "The use of an address.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [type](datatypes-definitions.html#Address.type "Address.type : Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | postal | physical | both [AddressType](valueset-address-type.html "The type of an address (physical / postal).") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [text](datatypes-definitions.html#Address.text "Address.text : Specifies the entire address as it should be displayed e.g. on a postal label. This may be provided instead of or as well as the specific parts.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Text representation of the address |
| ... [line](datatypes-definitions.html#Address.line "Address.line : This component contains the house number, apartment number, street name, street direction,  P.O. Box number, delivery hints, and similar address information.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Street name, number, direction & P.O. Box etc. This repeating element order: The order in which lines should appear in an address label |
| ... [city](datatypes-definitions.html#Address.city "Address.city : The name of the city, town, suburb, village or other community or delivery center.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of city, town etc. |
| ... [district](datatypes-definitions.html#Address.district "Address.district : The name of the administrative area (county).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | District name (aka county) |
| ... [state](datatypes-definitions.html#Address.state "Address.state : Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Sub-unit of country (abbreviations ok) |
| ... [postalCode](datatypes-definitions.html#Address.postalCode "Address.postalCode : A postal code designating a region defined by the postal service.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Postal code for area |
| ... [country](datatypes-definitions.html#Address.country "Address.country : Country - a nation as commonly understood or generally accepted.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Country (e.g. can be ISO 3166 2 or 3 letter code) |
| ... [period](datatypes-definitions.html#Address.period "Address.period : Time period when address was/is in use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Time period when address was/is in use |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <use value="[code]"/><!-- 0..1 home | work | temp | old | billing - purpose of this address -->
 <type value="[code]"/><!-- 0..1 postal | physical | both -->
 <text value="[string]"/><!-- 0..1 Text representation of the address -->
 <line value="[string]"/><!-- 0..* Street name, number, direction & P.O. Box etc. -->
 <city value="[string]"/><!-- 0..1 Name of city, town etc. -->
 <district value="[string]"/><!-- 0..1 District name (aka county) -->
 <state value="[string]"/><!-- 0..1 Sub-unit of country (abbreviations ok) -->
 <postalCode value="[string]"/><!-- 0..1 Postal code for area -->
 <country value="[string]"/><!-- 0..1 Country (e.g. can be ISO 3166 2 or 3 letter code) -->
 <period><!-- 0..1 Period Time period when address was/is in use --></period>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "use" : "<code>", // home | work | temp | old | billing - purpose of this address
  "type" : "<code>", // postal | physical | both
  "text" : "<string>", // Text representation of the address
  "line" : ["<string>"], // Street name, number, direction & P.O. Box etc.
  "city" : "<string>", // Name of city, town etc.
  "district" : "<string>", // District name (aka county)
  "state" : "<string>", // Sub-unit of country (abbreviations ok)
  "postalCode" : "<string>", // Postal code for area
  "country" : "<string>", // Country (e.g. can be ISO 3166 2 or 3 letter code)
  "period" : { Period } // Time period when address was/is in use
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Address.use [ code ]; # 0..1 home | work | temp | old | billing - purpose of this address
  fhir:Address.type [ code ]; # 0..1 postal | physical | both
  fhir:Address.text [ string ]; # 0..1 Text representation of the address
  fhir:Address.line [ string ], ... ; # 0..* Street name, number, direction & P.O. Box etc.
  fhir:Address.city [ string ]; # 0..1 Name of city, town etc.
  fhir:Address.district [ string ]; # 0..1 District name (aka county)
  fhir:Address.state [ string ]; # 0..1 Sub-unit of country (abbreviations ok)
  fhir:Address.postalCode [ string ]; # 0..1 Postal code for area
  fhir:Address.country [ string ]; # 0..1 Country (e.g. can be ISO 3166 2 or 3 letter code)
  fhir:Address.period [ Period ]; # 0..1 Time period when address was/is in use
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Address](datatypes.html#Address) |  |
| Address.use | - Change value set from http://hl7.org/fhir/ValueSet/address-use to http://hl7.org/fhir/ValueSet/address-use|4.0.1 |
| Address.type | - Change value set from http://hl7.org/fhir/ValueSet/address-type to http://hl7.org/fhir/ValueSet/address-type|4.0.1 |

See the [Full Difference](diff.html) for further information

The text element specifies the entire address as it should be displayed e.g. on a postal label. This may
be provided instead of or as well as the specific parts. Applications updating an address SHALL ensure that
when both text and parts are present, no content is included in the text that isn't found in a part.

**Constraints**

**Terminology Bindings**

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Address.use | The use of an address. | [Required](terminologies.html#required) | [AddressUse](valueset-address-use.html) |
| Address.type | The type of an address (physical / postal). | [Required](terminologies.html#required) | [AddressType](valueset-address-type.html) |

Address is used in the following places: [Claim](claim.html#claim), [ClaimResponse](claimresponse.html#claimresponse), [ExplanationOfBenefit](explanationofbenefit.html#explanationofbenefit), [InsurancePlan](insuranceplan.html#insuranceplan), [Location](location.html#location), [Organization](organization.html#organization), [Patient](patient.html#patient), [Person](person.html#person), [Practitioner](practitioner.html#practitioner) and [RelatedPerson](relatedperson.html#relatedperson)

## 2.24.0.15 ContactPoint

See also [Examples](datatypes-examples.html#ContactPoint), [Detailed Descriptions](datatypes-definitions.html#ContactPoint), [Mappings](datatypes-mappings.html#ContactPoint), [Profiles & Extensions](datatypes-extras.html#ContactPoint) and [R2 Conversions](datatypes-version-maps.html#ContactPoint).

Details for all kinds of technology-mediated contact points for a person or organization, including telephone, email, etc.

- [Structure](#tabs-ContactPoint-struc)
- [UML](#tabs-ContactPoint-uml)
- [XML](#tabs-ContactPoint-xml)
- [JSON](#tabs-ContactPoint-json)
- [Turtle](#tabs-ContactPoint-ttl)
- [R3 Diff](#tabs-ContactPoint-diff)
- [All](#tabs-ContactPoint-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [ContactPoint](datatypes-definitions.html#ContactPoint "ContactPoint : Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Details of a Technology mediated contact point (phone, fax, email, etc.) + Rule: A system is required if a value is provided. Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [system](datatypes-definitions.html#ContactPoint.system "ContactPoint.system : Telecommunications form for contact point - what communications system is required to make use of the contact.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [code](datatypes.html#code) | phone | fax | email | pager | url | sms | other [ContactPointSystem](valueset-contact-point-system.html "Telecommunications form for contact point.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [value](datatypes-definitions.html#ContactPoint.value "ContactPoint.value : The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | The actual contact point details |
| ... [use](datatypes-definitions.html#ContactPoint.use "ContactPoint.use : Identifies the purpose for the contact point.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | home | work | temp | old | mobile - purpose of this contact point [ContactPointUse](valueset-contact-point-use.html "Use of contact point.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [rank](datatypes-definitions.html#ContactPoint.rank "ContactPoint.rank : Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Specify preferred order of use (1 = highest) |
| ... [period](datatypes-definitions.html#ContactPoint.period "ContactPoint.period : Time period when the contact point was/is in use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Time period when the contact point was/is in use |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <system value="[code]"/><!-- ![??](lock.png) 0..1 phone | fax | email | pager | url | sms | other -->
 <value value="[string]"/><!-- 0..1 The actual contact point details -->
 <use value="[code]"/><!-- 0..1 home | work | temp | old | mobile - purpose of this contact point -->
 <rank value="[positiveInt]"/><!-- 0..1 Specify preferred order of use (1 = highest) -->
 <period><!-- 0..1 Period Time period when the contact point was/is in use --></period>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "system" : "<code>", // C? phone | fax | email | pager | url | sms | other
  "value" : "<string>", // The actual contact point details
  "use" : "<code>", // home | work | temp | old | mobile - purpose of this contact point
  "rank" : "<positiveInt>", // Specify preferred order of use (1 = highest)
  "period" : { Period } // Time period when the contact point was/is in use
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:ContactPoint.system [ code ]; # 0..1 phone | fax | email | pager | url | sms | other
  fhir:ContactPoint.value [ string ]; # 0..1 The actual contact point details
  fhir:ContactPoint.use [ code ]; # 0..1 home | work | temp | old | mobile - purpose of this contact point
  fhir:ContactPoint.rank [ positiveInt ]; # 0..1 Specify preferred order of use (1 = highest)
  fhir:ContactPoint.period [ Period ]; # 0..1 Time period when the contact point was/is in use
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [ContactPoint](datatypes.html#ContactPoint) |  |
| ContactPoint.system | - Change value set from http://hl7.org/fhir/ValueSet/contact-point-system to http://hl7.org/fhir/ValueSet/contact-point-system|4.0.1 |
| ContactPoint.use | - Change value set from http://hl7.org/fhir/ValueSet/contact-point-use to http://hl7.org/fhir/ValueSet/contact-point-use|4.0.1 |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [ContactPoint](datatypes-definitions.html#ContactPoint "ContactPoint : Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Details of a Technology mediated contact point (phone, fax, email, etc.) + Rule: A system is required if a value is provided. Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [system](datatypes-definitions.html#ContactPoint.system "ContactPoint.system : Telecommunications form for contact point - what communications system is required to make use of the contact.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [code](datatypes.html#code) | phone | fax | email | pager | url | sms | other [ContactPointSystem](valueset-contact-point-system.html "Telecommunications form for contact point.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [value](datatypes-definitions.html#ContactPoint.value "ContactPoint.value : The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | The actual contact point details |
| ... [use](datatypes-definitions.html#ContactPoint.use "ContactPoint.use : Identifies the purpose for the contact point.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | home | work | temp | old | mobile - purpose of this contact point [ContactPointUse](valueset-contact-point-use.html "Use of contact point.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [rank](datatypes-definitions.html#ContactPoint.rank "ContactPoint.rank : Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Specify preferred order of use (1 = highest) |
| ... [period](datatypes-definitions.html#ContactPoint.period "ContactPoint.period : Time period when the contact point was/is in use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Time period when the contact point was/is in use |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <system value="[code]"/><!-- ![??](lock.png) 0..1 phone | fax | email | pager | url | sms | other -->
 <value value="[string]"/><!-- 0..1 The actual contact point details -->
 <use value="[code]"/><!-- 0..1 home | work | temp | old | mobile - purpose of this contact point -->
 <rank value="[positiveInt]"/><!-- 0..1 Specify preferred order of use (1 = highest) -->
 <period><!-- 0..1 Period Time period when the contact point was/is in use --></period>
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "system" : "<code>", // C? phone | fax | email | pager | url | sms | other
  "value" : "<string>", // The actual contact point details
  "use" : "<code>", // home | work | temp | old | mobile - purpose of this contact point
  "rank" : "<positiveInt>", // Specify preferred order of use (1 = highest)
  "period" : { Period } // Time period when the contact point was/is in use
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:ContactPoint.system [ code ]; # 0..1 phone | fax | email | pager | url | sms | other
  fhir:ContactPoint.value [ string ]; # 0..1 The actual contact point details
  fhir:ContactPoint.use [ code ]; # 0..1 home | work | temp | old | mobile - purpose of this contact point
  fhir:ContactPoint.rank [ positiveInt ]; # 0..1 Specify preferred order of use (1 = highest)
  fhir:ContactPoint.period [ Period ]; # 0..1 Time period when the contact point was/is in use
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [ContactPoint](datatypes.html#ContactPoint) |  |
| ContactPoint.system | - Change value set from http://hl7.org/fhir/ValueSet/contact-point-system to http://hl7.org/fhir/ValueSet/contact-point-system|4.0.1 |
| ContactPoint.use | - Change value set from http://hl7.org/fhir/ValueSet/contact-point-use to http://hl7.org/fhir/ValueSet/contact-point-use|4.0.1 |

See the [Full Difference](diff.html) for further information

If capturing a phone, fax or similar contact point, the value should be a properly formatted telephone number according to
[ITU-T E.123 ![](external.png)](http://www.itu.int/rec/T-REC-E.123-200102-I/e).
However, this is frequently not possible due to legacy data and/or clerical practices when recording contact details.
For this reason, phone, fax, pager, and email addresses are not handled as formal URLs. For other kinds
of contact points, the `system` is "other" and the `value` SHOULD be a URL so that its use can be determined automatically. Typical
URL schemes used in the value are http{s}: for web addresses, and URL schemes for various kinds of messaging systems.
If the value is not a URL, then human interpretation will be required.

The `rank` element can be used to specify a preference for the order in which a set of contacts
is used. ContactPoints with lower rank values are more preferred than those with higher rank values. Note that `rank` does not necessarily
follow the order in which the contacts are represented in the instance.

**Constraints**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **cpt-2** | [Rule](conformance-rules.html#rule) | (base) | A system is required if a value is provided. | value.empty() or system.exists() |

**Terminology Bindings**

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| ContactPoint.system | Telecommunications form for contact point. | [Required](terminologies.html#required) | [ContactPointSystem](valueset-contact-point-system.html) |
| ContactPoint.use | Use of contact point. | [Required](terminologies.html#required) | [ContactPointUse](valueset-contact-point-use.html) |

ContactPoint is used in the following places: [ContactDetail](metadatatypes.html#ContactDetail), [CareTeam](careteam.html#careteam), [Device](device.html#device), [DeviceDefinition](devicedefinition.html#devicedefinition), [Endpoint](endpoint.html#endpoint), [HealthcareService](healthcareservice.html#healthcareservice), [InsurancePlan](insuranceplan.html#insuranceplan), [Location](location.html#location), [MessageHeader](messageheader.html#messageheader), [Organization](organization.html#organization), [OrganizationAffiliation](organizationaffiliation.html#organizationaffiliation), [Patient](patient.html#patient), [Person](person.html#person), [Practitioner](practitioner.html#practitioner), [PractitionerRole](practitionerrole.html#practitionerrole), [RelatedPerson](relatedperson.html#relatedperson) and [Subscription](subscription.html#subscription)

## 2.24.0.16 Timing

See also [Examples](datatypes-examples.html#Timing), [Detailed Descriptions](datatypes-definitions.html#Timing), [Mappings](datatypes-mappings.html#Timing), [Profiles & Extensions](datatypes-extras.html#Timing) and [R2 Conversions](datatypes-version-maps.html#Timing).

Describes the occurrence of an event that may occur multiple times. Timing schedules are used for
specifying when events are expected or requested to occur and may also be used to represent the
summary of a past or ongoing event. For simplicity, the definitions of Timing components are
expressed as 'future' events, but such components can also be used to describe historic or
ongoing events.

A Timing schedule can be a list of events and/or criteria for when the event happens, which
can be expressed in a structured form and/or as a code. When both event and a repeating
specification are provided, the list of events should be understood as an interpretation
of the information in the repeat structure.

Note: The Timing data type allows [modifier extensions](extensibility.html#modifier).

- [Structure](#tabs-Timing-struc)
- [UML](#tabs-Timing-uml)
- [XML](#tabs-Timing-xml)
- [JSON](#tabs-Timing-json)
- [Turtle](#tabs-Timing-ttl)
- [R3 Diff](#tabs-Timing-diff)
- [All](#tabs-Timing-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Timing](datatypes-definitions.html#Timing "Timing : Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [BackBoneElement](backboneelement.html) | A timing schedule that specifies an event that may occur multiple times Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](backboneelement.html#BackboneElement "May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [event](datatypes-definitions.html#Timing.event "Timing.event : Identifies specific times when the event occurs.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [dateTime](datatypes.html#dateTime) | When the event occurs |
| ... [repeat](datatypes-definitions.html#Timing.repeat "Timing.repeat : A set of rules that describe when the event is scheduled.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [Element](element.html) | When the event is to occur + Rule: if there's a duration, there needs to be duration units + Rule: if there's a period, there needs to be period units + Rule: duration SHALL be a non-negative value + Rule: period SHALL be a non-negative value + Rule: If there's a periodMax, there must be a period + Rule: If there's a durationMax, there must be a duration + Rule: If there's a countMax, there must be a count + Rule: If there's an offset, there must be a when (and not C, CM, CD, CV) + Rule: If there's a timeOfDay, there cannot be a when, or vice versa |
| .... [bounds[x]](datatypes-definitions.html#Timing.repeat.bounds_x_ "Timing.repeat.bounds[x] : Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Length/Range of lengths, or (Start and/or end) limits |
| ..... boundsDuration |  |  | [Duration](datatypes.html#Duration) |  |
| ..... boundsRange |  |  | [Range](datatypes.html#Range) |  |
| ..... boundsPeriod |  |  | [Period](datatypes.html#Period) |  |
| .... [count](datatypes-definitions.html#Timing.repeat.count "Timing.repeat.count : A total count of the desired number of repetitions across the duration of the entire timing specification. If countMax is present, this element indicates the lower bound of the allowed range of count values.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Number of times to repeat |
| .... [countMax](datatypes-definitions.html#Timing.repeat.countMax "Timing.repeat.countMax : If present, indicates that the count is a range - so to perform the action between [count] and [countMax] times.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Maximum number of times to repeat |
| .... [duration](datatypes-definitions.html#Timing.repeat.duration "Timing.repeat.duration : How long this thing happens for when it happens. If durationMax is present, this element indicates the lower bound of the allowed range of the duration.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | How long when it happens |
| .... [durationMax](datatypes-definitions.html#Timing.repeat.durationMax "Timing.repeat.durationMax : If present, indicates that the duration is a range - so to perform the action between [duration] and [durationMax] time length.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | How long when it happens (Max) |
| .... [durationUnit](datatypes-definitions.html#Timing.repeat.durationUnit "Timing.repeat.durationUnit : The units of time for the duration, in UCUM units.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | s | min | h | d | wk | mo | a - unit of time (UCUM) [UnitsOfTime](valueset-units-of-time.html "A unit of time (units from UCUM).") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [frequency](datatypes-definitions.html#Timing.repeat.frequency "Timing.repeat.frequency : The number of times to repeat the action within the specified period. If frequencyMax is present, this element indicates the lower bound of the allowed range of the frequency.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Event occurs frequency times per period |
| .... [frequencyMax](datatypes-definitions.html#Timing.repeat.frequencyMax "Timing.repeat.frequencyMax : If present, indicates that the frequency is a range - so to repeat between [frequency] and [frequencyMax] times within the period or period range.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Event occurs up to frequencyMax times per period |
| .... [period](datatypes-definitions.html#Timing.repeat.period "Timing.repeat.period : Indicates the duration of time over which repetitions are to occur; e.g. to express \"3 times per day\", 3 would be the frequency and \"1 day\" would be the period. If periodMax is present, this element indicates the lower bound of the allowed range of the period length.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Event occurs frequency times per period |
| .... [periodMax](datatypes-definitions.html#Timing.repeat.periodMax "Timing.repeat.periodMax : If present, indicates that the period is a range from [period] to [periodMax], allowing expressing concepts such as \"do this once every 3-5 days.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Upper limit of period (3-4 hours) |
| .... [periodUnit](datatypes-definitions.html#Timing.repeat.periodUnit "Timing.repeat.periodUnit : The units of time for the period in UCUM units.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | s | min | h | d | wk | mo | a - unit of time (UCUM) [UnitsOfTime](valueset-units-of-time.html "A unit of time (units from UCUM).") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [dayOfWeek](datatypes-definitions.html#Timing.repeat.dayOfWeek "Timing.repeat.dayOfWeek : If one or more days of week is provided, then the action happens only on the specified day(s).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [code](datatypes.html#code) | mon | tue | wed | thu | fri | sat | sun [DaysOfWeek](valueset-days-of-week.html) ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [timeOfDay](datatypes-definitions.html#Timing.repeat.timeOfDay "Timing.repeat.timeOfDay : Specified time of day for action to take place.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [time](datatypes.html#time) | Time of day for action |
| .... [when](datatypes-definitions.html#Timing.repeat.when "Timing.repeat.when : An approximate time period during the day, potentially linked to an event of daily living that indicates when the action should occur.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [code](datatypes.html#code) | Code for time period of occurrence [EventTiming](valueset-event-timing.html "Real world event relating to the schedule.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [offset](datatypes-definitions.html#Timing.repeat.offset "Timing.repeat.offset : The number of minutes from the event. If the event code does not indicate whether the minutes is before or after the event, then the offset is assumed to be after the event.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Minutes from event (before or after) |
| ... [code](datatypes-definitions.html#Timing.code "Timing.code : A code for the timing schedule (or just text in code.text). Some codes such as BID are ubiquitous, but many institutions define their own additional codes. If a code is provided, the code is understood to be a complete statement of whatever is specified in the structured timing data, and either the code or the data may be used to interpret the Timing, with the exception that .repeat.bounds still applies over the code (and is not contained in the code).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | BID | TID | QID | AM | PM | QD | QOD | + [TimingAbbreviation](valueset-timing-abbreviation.html "Code for a known / defined timing pattern.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Timing xmlns="http://hl7.org/fhir">
 <!-- from BackboneElement: extension, modifierExtension -->
 <event value="[dateTime]"/><!-- 0..* When the event occurs -->
 <repeat>  <!-- 0..1 When the event is to occur -->
  <bounds[x]><!-- 0..1 Duration|Range|Period Length/Range of lengths, or (Start and/or end) limits --></bounds[x]>
  <count value="[positiveInt]"/><!-- 0..1 Number of times to repeat -->
  <countMax value="[positiveInt]"/><!-- 0..1 Maximum number of times to repeat -->
  <duration value="[decimal]"/><!-- 0..1 How long when it happens -->
  <durationMax value="[decimal]"/><!-- 0..1 How long when it happens (Max) -->
  <durationUnit value="[code]"/><!-- 0..1 s | min | h | d | wk | mo | a - unit of time (UCUM) -->
  <frequency value="[positiveInt]"/><!-- 0..1 Event occurs frequency times per period -->
  <frequencyMax value="[positiveInt]"/><!-- 0..1 Event occurs up to frequencyMax times per period -->
  <period value="[decimal]"/><!-- 0..1 Event occurs frequency times per period -->
  <periodMax value="[decimal]"/><!-- 0..1 Upper limit of period (3-4 hours) -->
  <periodUnit value="[code]"/><!-- 0..1 s | min | h | d | wk | mo | a - unit of time (UCUM) -->
  <dayOfWeek value="[code]"/><!-- 0..* mon | tue | wed | thu | fri | sat | sun -->
  <timeOfDay value="[time]"/><!-- 0..* Time of day for action -->
  <when value="[code]"/><!-- 0..* Code for time period of occurrence -->
  <offset value="[unsignedInt]"/><!-- 0..1 Minutes from event (before or after) -->
 </repeat>
 <code><!-- 0..1 CodeableConcept BID | TID | QID | AM | PM | QD | QOD | + --></code>
</Timing>
```

**JSON Template**

```

{![doco](help.png)
  // from BackboneElement: extension, modifierExtension
  "event" : ["<dateTime>"], // When the event occurs
  "repeat" : { // When the event is to occur
    // bounds[x]: Length/Range of lengths, or (Start and/or end) limits. One of these 3:
    "boundsDuration" : { Duration },
    "boundsRange" : { Range },
    "boundsPeriod" : { Period },
    "count" : "<positiveInt>", // Number of times to repeat
    "countMax" : "<positiveInt>", // Maximum number of times to repeat
    "duration" : <decimal>, // How long when it happens
    "durationMax" : <decimal>, // How long when it happens (Max)
    "durationUnit" : "<code>", // s | min | h | d | wk | mo | a - unit of time (UCUM)
    "frequency" : "<positiveInt>", // Event occurs frequency times per period
    "frequencyMax" : "<positiveInt>", // Event occurs up to frequencyMax times per period
    "period" : <decimal>, // Event occurs frequency times per period
    "periodMax" : <decimal>, // Upper limit of period (3-4 hours)
    "periodUnit" : "<code>", // s | min | h | d | wk | mo | a - unit of time (UCUM)
    "dayOfWeek" : ["<code>"], // mon | tue | wed | thu | fri | sat | sun
    "timeOfDay" : ["<time>"], // Time of day for action
    "when" : ["<code>"], // Code for time period of occurrence
    "offset" : "<unsignedInt>" // Minutes from event (before or after)
  },
  "code" : { CodeableConcept } // BID | TID | QID | AM | PM | QD | QOD | +
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from BackboneElement: Element.extension, BackboneElement.modifierextension
  fhir:Timing.event [ dateTime ], ... ; # 0..* When the event occurs
  fhir:Timing.repeat [ # 0..1 When the event is to occur
    # Timing.repeat.bounds[x] : 0..1 Length/Range of lengths, or (Start and/or end) limits. One of these 3
      fhir:Timing.repeat.boundsDuration [ Duration ]
      fhir:Timing.repeat.boundsRange [ Range ]
      fhir:Timing.repeat.boundsPeriod [ Period ]
    fhir:Timing.repeat.count [ positiveInt ]; # 0..1 Number of times to repeat
    fhir:Timing.repeat.countMax [ positiveInt ]; # 0..1 Maximum number of times to repeat
    fhir:Timing.repeat.duration [ decimal ]; # 0..1 How long when it happens
    fhir:Timing.repeat.durationMax [ decimal ]; # 0..1 How long when it happens (Max)
    fhir:Timing.repeat.durationUnit [ code ]; # 0..1 s | min | h | d | wk | mo | a - unit of time (UCUM)
    fhir:Timing.repeat.frequency [ positiveInt ]; # 0..1 Event occurs frequency times per period
    fhir:Timing.repeat.frequencyMax [ positiveInt ]; # 0..1 Event occurs up to frequencyMax times per period
    fhir:Timing.repeat.period [ decimal ]; # 0..1 Event occurs frequency times per period
    fhir:Timing.repeat.periodMax [ decimal ]; # 0..1 Upper limit of period (3-4 hours)
    fhir:Timing.repeat.periodUnit [ code ]; # 0..1 s | min | h | d | wk | mo | a - unit of time (UCUM)
    fhir:Timing.repeat.dayOfWeek [ code ], ... ; # 0..* mon | tue | wed | thu | fri | sat | sun
    fhir:Timing.repeat.timeOfDay [ time ], ... ; # 0..* Time of day for action
    fhir:Timing.repeat.when [ code ], ... ; # 0..* Code for time period of occurrence
    fhir:Timing.repeat.offset [ unsignedInt ]; # 0..1 Minutes from event (before or after)
  ];
  fhir:Timing.code [ CodeableConcept ]; # 0..1 BID | TID | QID | AM | PM | QD | QOD | +
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Timing](datatypes.html#Timing) |  |
| Timing.repeat.count | - Type changed from integer to positiveInt |
| Timing.repeat.countMax | - Type changed from integer to positiveInt |
| Timing.repeat.durationUnit | - Change value set from http://hl7.org/fhir/ValueSet/units-of-time to http://hl7.org/fhir/ValueSet/units-of-time|4.0.1 |
| Timing.repeat.frequency | - Type changed from integer to positiveInt - Default Value "1" removed |
| Timing.repeat.frequencyMax | - Type changed from integer to positiveInt |
| Timing.repeat.periodUnit | - Change value set from http://hl7.org/fhir/ValueSet/units-of-time to http://hl7.org/fhir/ValueSet/units-of-time|4.0.1 |
| Timing.repeat.dayOfWeek | - Change value set from http://hl7.org/fhir/ValueSet/days-of-week to http://hl7.org/fhir/ValueSet/days-of-week|4.0.1 |
| Timing.repeat.when | - Change value set from http://hl7.org/fhir/ValueSet/event-timing to http://hl7.org/fhir/ValueSet/event-timing|4.0.1 |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Timing](datatypes-definitions.html#Timing "Timing : Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[N](versions.html#std-process "Standards Status = Normative") |  | [BackBoneElement](backboneelement.html) | A timing schedule that specifies an event that may occur multiple times Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](backboneelement.html#BackboneElement "May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [event](datatypes-definitions.html#Timing.event "Timing.event : Identifies specific times when the event occurs.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [dateTime](datatypes.html#dateTime) | When the event occurs |
| ... [repeat](datatypes-definitions.html#Timing.repeat "Timing.repeat : A set of rules that describe when the event is scheduled.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [Element](element.html) | When the event is to occur + Rule: if there's a duration, there needs to be duration units + Rule: if there's a period, there needs to be period units + Rule: duration SHALL be a non-negative value + Rule: period SHALL be a non-negative value + Rule: If there's a periodMax, there must be a period + Rule: If there's a durationMax, there must be a duration + Rule: If there's a countMax, there must be a count + Rule: If there's an offset, there must be a when (and not C, CM, CD, CV) + Rule: If there's a timeOfDay, there cannot be a when, or vice versa |
| .... [bounds[x]](datatypes-definitions.html#Timing.repeat.bounds_x_ "Timing.repeat.bounds[x] : Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Length/Range of lengths, or (Start and/or end) limits |
| ..... boundsDuration |  |  | [Duration](datatypes.html#Duration) |  |
| ..... boundsRange |  |  | [Range](datatypes.html#Range) |  |
| ..... boundsPeriod |  |  | [Period](datatypes.html#Period) |  |
| .... [count](datatypes-definitions.html#Timing.repeat.count "Timing.repeat.count : A total count of the desired number of repetitions across the duration of the entire timing specification. If countMax is present, this element indicates the lower bound of the allowed range of count values.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Number of times to repeat |
| .... [countMax](datatypes-definitions.html#Timing.repeat.countMax "Timing.repeat.countMax : If present, indicates that the count is a range - so to perform the action between [count] and [countMax] times.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Maximum number of times to repeat |
| .... [duration](datatypes-definitions.html#Timing.repeat.duration "Timing.repeat.duration : How long this thing happens for when it happens. If durationMax is present, this element indicates the lower bound of the allowed range of the duration.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | How long when it happens |
| .... [durationMax](datatypes-definitions.html#Timing.repeat.durationMax "Timing.repeat.durationMax : If present, indicates that the duration is a range - so to perform the action between [duration] and [durationMax] time length.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | How long when it happens (Max) |
| .... [durationUnit](datatypes-definitions.html#Timing.repeat.durationUnit "Timing.repeat.durationUnit : The units of time for the duration, in UCUM units.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | s | min | h | d | wk | mo | a - unit of time (UCUM) [UnitsOfTime](valueset-units-of-time.html "A unit of time (units from UCUM).") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [frequency](datatypes-definitions.html#Timing.repeat.frequency "Timing.repeat.frequency : The number of times to repeat the action within the specified period. If frequencyMax is present, this element indicates the lower bound of the allowed range of the frequency.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Event occurs frequency times per period |
| .... [frequencyMax](datatypes-definitions.html#Timing.repeat.frequencyMax "Timing.repeat.frequencyMax : If present, indicates that the frequency is a range - so to repeat between [frequency] and [frequencyMax] times within the period or period range.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Event occurs up to frequencyMax times per period |
| .... [period](datatypes-definitions.html#Timing.repeat.period "Timing.repeat.period : Indicates the duration of time over which repetitions are to occur; e.g. to express \"3 times per day\", 3 would be the frequency and \"1 day\" would be the period. If periodMax is present, this element indicates the lower bound of the allowed range of the period length.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Event occurs frequency times per period |
| .... [periodMax](datatypes-definitions.html#Timing.repeat.periodMax "Timing.repeat.periodMax : If present, indicates that the period is a range from [period] to [periodMax], allowing expressing concepts such as \"do this once every 3-5 days.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [decimal](datatypes.html#decimal) | Upper limit of period (3-4 hours) |
| .... [periodUnit](datatypes-definitions.html#Timing.repeat.periodUnit "Timing.repeat.periodUnit : The units of time for the period in UCUM units.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | s | min | h | d | wk | mo | a - unit of time (UCUM) [UnitsOfTime](valueset-units-of-time.html "A unit of time (units from UCUM).") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [dayOfWeek](datatypes-definitions.html#Timing.repeat.dayOfWeek "Timing.repeat.dayOfWeek : If one or more days of week is provided, then the action happens only on the specified day(s).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [code](datatypes.html#code) | mon | tue | wed | thu | fri | sat | sun [DaysOfWeek](valueset-days-of-week.html) ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [timeOfDay](datatypes-definitions.html#Timing.repeat.timeOfDay "Timing.repeat.timeOfDay : Specified time of day for action to take place.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [time](datatypes.html#time) | Time of day for action |
| .... [when](datatypes-definitions.html#Timing.repeat.when "Timing.repeat.when : An approximate time period during the day, potentially linked to an event of daily living that indicates when the action should occur.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [code](datatypes.html#code) | Code for time period of occurrence [EventTiming](valueset-event-timing.html "Real world event relating to the schedule.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [offset](datatypes-definitions.html#Timing.repeat.offset "Timing.repeat.offset : The number of minutes from the event. If the event code does not indicate whether the minutes is before or after the event, then the offset is assumed to be after the event.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Minutes from event (before or after) |
| ... [code](datatypes-definitions.html#Timing.code "Timing.code : A code for the timing schedule (or just text in code.text). Some codes such as BID are ubiquitous, but many institutions define their own additional codes. If a code is provided, the code is understood to be a complete statement of whatever is specified in the structured timing data, and either the code or the data may be used to interpret the Timing, with the exception that .repeat.bounds still applies over the code (and is not contained in the code).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | BID | TID | QID | AM | PM | QD | QOD | + [TimingAbbreviation](valueset-timing-abbreviation.html "Code for a known / defined timing pattern.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Timing xmlns="http://hl7.org/fhir">
 <!-- from BackboneElement: extension, modifierExtension -->
 <event value="[dateTime]"/><!-- 0..* When the event occurs -->
 <repeat>  <!-- 0..1 When the event is to occur -->
  <bounds[x]><!-- 0..1 Duration|Range|Period Length/Range of lengths, or (Start and/or end) limits --></bounds[x]>
  <count value="[positiveInt]"/><!-- 0..1 Number of times to repeat -->
  <countMax value="[positiveInt]"/><!-- 0..1 Maximum number of times to repeat -->
  <duration value="[decimal]"/><!-- 0..1 How long when it happens -->
  <durationMax value="[decimal]"/><!-- 0..1 How long when it happens (Max) -->
  <durationUnit value="[code]"/><!-- 0..1 s | min | h | d | wk | mo | a - unit of time (UCUM) -->
  <frequency value="[positiveInt]"/><!-- 0..1 Event occurs frequency times per period -->
  <frequencyMax value="[positiveInt]"/><!-- 0..1 Event occurs up to frequencyMax times per period -->
  <period value="[decimal]"/><!-- 0..1 Event occurs frequency times per period -->
  <periodMax value="[decimal]"/><!-- 0..1 Upper limit of period (3-4 hours) -->
  <periodUnit value="[code]"/><!-- 0..1 s | min | h | d | wk | mo | a - unit of time (UCUM) -->
  <dayOfWeek value="[code]"/><!-- 0..* mon | tue | wed | thu | fri | sat | sun -->
  <timeOfDay value="[time]"/><!-- 0..* Time of day for action -->
  <when value="[code]"/><!-- 0..* Code for time period of occurrence -->
  <offset value="[unsignedInt]"/><!-- 0..1 Minutes from event (before or after) -->
 </repeat>
 <code><!-- 0..1 CodeableConcept BID | TID | QID | AM | PM | QD | QOD | + --></code>
</Timing>
```

**JSON Template**

```

{![doco](help.png)
  // from BackboneElement: extension, modifierExtension
  "event" : ["<dateTime>"], // When the event occurs
  "repeat" : { // When the event is to occur
    // bounds[x]: Length/Range of lengths, or (Start and/or end) limits. One of these 3:
    "boundsDuration" : { Duration },
    "boundsRange" : { Range },
    "boundsPeriod" : { Period },
    "count" : "<positiveInt>", // Number of times to repeat
    "countMax" : "<positiveInt>", // Maximum number of times to repeat
    "duration" : <decimal>, // How long when it happens
    "durationMax" : <decimal>, // How long when it happens (Max)
    "durationUnit" : "<code>", // s | min | h | d | wk | mo | a - unit of time (UCUM)
    "frequency" : "<positiveInt>", // Event occurs frequency times per period
    "frequencyMax" : "<positiveInt>", // Event occurs up to frequencyMax times per period
    "period" : <decimal>, // Event occurs frequency times per period
    "periodMax" : <decimal>, // Upper limit of period (3-4 hours)
    "periodUnit" : "<code>", // s | min | h | d | wk | mo | a - unit of time (UCUM)
    "dayOfWeek" : ["<code>"], // mon | tue | wed | thu | fri | sat | sun
    "timeOfDay" : ["<time>"], // Time of day for action
    "when" : ["<code>"], // Code for time period of occurrence
    "offset" : "<unsignedInt>" // Minutes from event (before or after)
  },
  "code" : { CodeableConcept } // BID | TID | QID | AM | PM | QD | QOD | +
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from BackboneElement: Element.extension, BackboneElement.modifierextension
  fhir:Timing.event [ dateTime ], ... ; # 0..* When the event occurs
  fhir:Timing.repeat [ # 0..1 When the event is to occur
    # Timing.repeat.bounds[x] : 0..1 Length/Range of lengths, or (Start and/or end) limits. One of these 3
      fhir:Timing.repeat.boundsDuration [ Duration ]
      fhir:Timing.repeat.boundsRange [ Range ]
      fhir:Timing.repeat.boundsPeriod [ Period ]
    fhir:Timing.repeat.count [ positiveInt ]; # 0..1 Number of times to repeat
    fhir:Timing.repeat.countMax [ positiveInt ]; # 0..1 Maximum number of times to repeat
    fhir:Timing.repeat.duration [ decimal ]; # 0..1 How long when it happens
    fhir:Timing.repeat.durationMax [ decimal ]; # 0..1 How long when it happens (Max)
    fhir:Timing.repeat.durationUnit [ code ]; # 0..1 s | min | h | d | wk | mo | a - unit of time (UCUM)
    fhir:Timing.repeat.frequency [ positiveInt ]; # 0..1 Event occurs frequency times per period
    fhir:Timing.repeat.frequencyMax [ positiveInt ]; # 0..1 Event occurs up to frequencyMax times per period
    fhir:Timing.repeat.period [ decimal ]; # 0..1 Event occurs frequency times per period
    fhir:Timing.repeat.periodMax [ decimal ]; # 0..1 Upper limit of period (3-4 hours)
    fhir:Timing.repeat.periodUnit [ code ]; # 0..1 s | min | h | d | wk | mo | a - unit of time (UCUM)
    fhir:Timing.repeat.dayOfWeek [ code ], ... ; # 0..* mon | tue | wed | thu | fri | sat | sun
    fhir:Timing.repeat.timeOfDay [ time ], ... ; # 0..* Time of day for action
    fhir:Timing.repeat.when [ code ], ... ; # 0..* Code for time period of occurrence
    fhir:Timing.repeat.offset [ unsignedInt ]; # 0..1 Minutes from event (before or after)
  ];
  fhir:Timing.code [ CodeableConcept ]; # 0..1 BID | TID | QID | AM | PM | QD | QOD | +
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Timing](datatypes.html#Timing) |  |
| Timing.repeat.count | - Type changed from integer to positiveInt |
| Timing.repeat.countMax | - Type changed from integer to positiveInt |
| Timing.repeat.durationUnit | - Change value set from http://hl7.org/fhir/ValueSet/units-of-time to http://hl7.org/fhir/ValueSet/units-of-time|4.0.1 |
| Timing.repeat.frequency | - Type changed from integer to positiveInt - Default Value "1" removed |
| Timing.repeat.frequencyMax | - Type changed from integer to positiveInt |
| Timing.repeat.periodUnit | - Change value set from http://hl7.org/fhir/ValueSet/units-of-time to http://hl7.org/fhir/ValueSet/units-of-time|4.0.1 |
| Timing.repeat.dayOfWeek | - Change value set from http://hl7.org/fhir/ValueSet/days-of-week to http://hl7.org/fhir/ValueSet/days-of-week|4.0.1 |
| Timing.repeat.when | - Change value set from http://hl7.org/fhir/ValueSet/event-timing to http://hl7.org/fhir/ValueSet/event-timing|4.0.1 |

See the [Full Difference](diff.html) for further information

If the timing schedule has repeating criteria, the repeat can occur a given number of times per
the specified duration or in relation to some repeating real-world event. If no end condition is specified,
the schedule will terminate on some criteria that are expressed elsewhere.

This table summarizes some common uses of the Timing Data Type criteria.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **description** | **duration** | **durationUnit** | **frequency** | **frequencyMax** | **period** | **periodUnit** | **periodMax** | **Day of Week** | **Time Of Day** | **when** | **offset** | **bounds[x]** | **count** |
| Every 8 hours |  |  | 1 |  | 8 | h |  |  |  |  |  |  |  |
| Every 7 days |  |  | 1 |  | 7 | d |  |  |  |  |  |  |  |
| 3 times a day |  |  | 3 |  | 1 | d |  |  |  |  |  |  |  |
| 3-4 times a day |  |  | 3 | 4 | 1 | d |  |  |  |  |  |  |  |
| Every 4-6 hours |  |  | 1 |  | 4 | h | 6 |  |  |  |  |  |  |
| Every 21 days for 1 hour | 1 | hr | 1 |  | 21 | d |  |  |  |  |  |  |  |
| Three times a week for ½ hour | 0.5 | hr | 3 |  | 1 | wk |  |  |  |  |  |  |  |
| With breakfast |  |  |  |  |  |  |  |  |  | CM |  |  |  |
| For 5 minutes, 10 minutes before meals | 5 | min |  |  |  |  |  |  |  | AC | 10 |  |  |
| 1 tablet 3 times daily, 30 minutes before meals |  |  | 3 |  | 1 | d |  |  |  | AC | 30 |  |  |
| BID, 30 mins before meal, for next 10 days |  |  | 2 |  | 1 | d |  |  |  | AC | 30 | Duration = 10 days |  |
| TID, for 14 days |  |  | 3 |  | 1 | d |  |  |  |  |  | Duration = 14 days |  |
| BID, start on 7/1/2015 at 1:00 PM |  |  | 2 |  | 1 | d |  |  |  |  |  | Period.start = 2015-07-01T13:00:00 |  |
| Mon, Wed, Fri Morning |  |  | 1 |  | 1 | d |  | mon | wed | fri |  | MORN |  |  |  |
| Every day at 10am |  |  | 1 |  | 1 | d |  |  | 10:00 |  |  |  |  |
| Take once, at any time |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Take every second day, in the morning, until 20 have been taken |  |  | 1 |  | 2 | d |  |  |  | MORN |  |  | 20 |

Many systems avoid the complexity of the Timing structure by using a text field for timing instructions.
This maps to `Timing.code.text`. For example, the text instruction "take medication in
the morning on weekends and days off work' would be represented as:

```

  "timing": {
    "code" : {
      "text" : "Take medication in the morning on weekends and days off work"
    }    
  }
```

Note, though, that some systems include timing details in
something like 'Dosage instructions' which is wider than just Timing; those systems do not use the
Timing data type. Other systems use a set of 'common' codes - including, but usually not limited to,
widely understood acronyms such as "BID". If a `Timing.code` is
provided, the code is understood to be a complete statement of whatever is specified in the structured timing
data (except for `Timing.repeat.bounds`, which applies to the code), and either the code or the
data may be used to interpret the `Timing`. A structured timing specification SHOULD be provided whenever
possible, unless the code is BID, TID, QID, AM or PM, which have a ubiquitous meaning.

This table shows the relationship between the [codes provided as
part of the base specification](valueset-timing-abbreviation.html), and the structured data portions of the Timing type:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **description** | **duration** | **durationUnit** | **frequency** | **frequencyMax** | **period** | **periodUnit** | **periodMax** | **when** | **bounds[x]** |
| QOD |  |  | 1 |  | 2 | d |  |  |  |
| QD |  |  | 1 |  | 1 | d |  |  |  |
| BID |  |  | 2 |  | 1 | d |  |  |  |
| TID |  |  | 3 |  | 1 | d |  |  |  |
| QID |  |  | 4 |  | 1 | d |  |  |  |
| Q4H |  |  | 1 |  | 4 | h |  |  |  |
| Q6H |  |  | 1 |  | 6 | h |  |  |  |
| AM |  |  | 1 |  | 1 | d |  | MORN |  |
| PM |  |  | 1 |  | 1 | d |  | AFT or EVE |  |

These codes SHALL be understood as having the formal meanings documented in this table. Note that BID, etc. are defined as 'at institutionally specified times'.
For example, an institution may choose that BID is "always at 7am and 6pm". If it is inappropriate for this choice to be made, the code BID
should not be used. Instead, a distinct organization-specific code should be used in place of the HL7-defined BID code and/or a structured
representation should be used (in this case, `timeOfDay`).

**Constraints**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **tim-1** | [Rule](conformance-rules.html#rule) | Timing.repeat | if there's a duration, there needs to be duration units | duration.empty() or durationUnit.exists() |
| **tim-2** | [Rule](conformance-rules.html#rule) | Timing.repeat | if there's a period, there needs to be period units | period.empty() or periodUnit.exists() |
| **tim-4** | [Rule](conformance-rules.html#rule) | Timing.repeat | duration SHALL be a non-negative value | duration.exists() implies duration >= 0 |
| **tim-5** | [Rule](conformance-rules.html#rule) | Timing.repeat | period SHALL be a non-negative value | period.exists() implies period >= 0 |
| **tim-6** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's a periodMax, there must be a period | periodMax.empty() or period.exists() |
| **tim-7** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's a durationMax, there must be a duration | durationMax.empty() or duration.exists() |
| **tim-8** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's a countMax, there must be a count | countMax.empty() or count.exists() |
| **tim-9** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's an offset, there must be a when (and not C, CM, CD, CV) | offset.empty() or (when.exists() and ((when in ('C' | 'CM' | 'CD' | 'CV')).not())) |
| **tim-10** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's a timeOfDay, there cannot be a when, or vice versa | timeOfDay.empty() or when.empty() |

Note that these constraints still allow for nonsensical timing specifications such as "Once per day at 2:00 and 4:00" or "every 3 days on Friday".
Implementers must take care to ensure that their configuration and data collection designs do not lead to these non-interpretable timing specifications.
The elements `dayOfWeek`, `timeOfDay`, and `when` are particularly likely to be at issue here.

**Terminology Bindings**

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Timing.repeat.durationUnit Timing.repeat.periodUnit | A unit of time (units from UCUM). | [Required](terminologies.html#required) | [UnitsOfTime](valueset-units-of-time.html) |
| Timing.repeat.dayOfWeek |  | [Required](terminologies.html#required) | [DaysOfWeek](valueset-days-of-week.html) |
| Timing.repeat.when | Real world event relating to the schedule. | [Required](terminologies.html#required) | [EventTiming](valueset-event-timing.html) |
| Timing.code | Code for a known / defined timing pattern. | [Preferred](terminologies.html#preferred) | [TimingAbbreviation](valueset-timing-abbreviation.html) |

Timing is used in the following places: [Dosage](dosage.html#Dosage), [TriggerDefinition](metadatatypes.html#TriggerDefinition), [ActivityDefinition](activitydefinition.html#activitydefinition), [CarePlan](careplan.html#careplan), [ChargeItem](chargeitem.html#chargeitem), [Contract](contract.html#contract), [DeviceMetric](devicemetric.html#devicemetric), [DeviceRequest](devicerequest.html#devicerequest), [DeviceUseStatement](deviceusestatement.html#deviceusestatement), [EvidenceVariable](evidencevariable.html#evidencevariable), [NutritionOrder](nutritionorder.html#nutritionorder), [Observation](observation.html#observation), [PlanDefinition](plandefinition.html#plandefinition), [RequestGroup](requestgroup.html#requestgroup), [ResearchElementDefinition](researchelementdefinition.html#researchelementdefinition), [ServiceRequest](servicerequest.html#servicerequest), [SupplyDelivery](supplydelivery.html#supplydelivery), [SupplyRequest](supplyrequest.html#supplyrequest) and [VerificationResult](verificationresult.html#verificationresult)

## 2.24.0.17 Signature

Normative Candidate Note: This DataType is not normative - it is still undergoing Trial Use while more experience is gathered.

See also [Examples](datatypes-examples.html#Signature), [Detailed Descriptions](datatypes-definitions.html#Signature), [Mappings](datatypes-mappings.html#Signature), [Profiles & Extensions](datatypes-extras.html#Signature) and [R2 Conversions](datatypes-version-maps.html#Signature).

A Signature holds an electronic representation of a signature and its supporting context in a FHIR accessible form.
The signature may either be a cryptographic type (XML DigSig or a JWS), which is able to provide non-repudiation proof, or
it may be a graphical image that represents a signature or a signature process.

- [Structure](#tabs-Signature-struc)
- [UML](#tabs-Signature-uml)
- [XML](#tabs-Signature-xml)
- [JSON](#tabs-Signature-json)
- [Turtle](#tabs-Signature-ttl)
- [R3 Diff](#tabs-Signature-diff)
- [All](#tabs-Signature-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Signature](datatypes-definitions.html#Signature "Signature : A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [Element](element.html) | A Signature - XML DigSig, JWS, Graphical image of signature, etc. Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [type](datatypes-definitions.html#Signature.type "Signature.type : An indication of the reason that the entity signed this document. This may be explicitly included as part of the signature information and can be used when determining accountability for various actions concerning the document.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..\* | [Coding](datatypes.html#Coding) | Indication of the reason the entity signed the object(s) [Signature Type Codes](valueset-signature-type.html "An indication of the reason that an entity signed the object.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [when](datatypes-definitions.html#Signature.when "Signature.when : When the digital signature was signed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [instant](datatypes.html#instant) | When the signature was created |
| ... [who](datatypes-definitions.html#Signature.who "Signature.who : A reference to an application-usable description of the identity that signed  (e.g. the signature used their private key).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Patient](patient.html) | [Device](device.html) | [Organization](organization.html)) | Who signed |
| ... [onBehalfOf](datatypes-definitions.html#Signature.onBehalfOf "Signature.onBehalfOf : A reference to an application-usable description of the identity that is represented by the signature.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Patient](patient.html) | [Device](device.html) | [Organization](organization.html)) | The party represented |
| ... [targetFormat](datatypes-definitions.html#Signature.targetFormat "Signature.targetFormat : A mime type that indicates the technical format of the target resources signed by the signature.") |  | 0..1 | [code](datatypes.html#code) | The technical format of the signed resources [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [sigFormat](datatypes-definitions.html#Signature.sigFormat "Signature.sigFormat : A mime type that indicates the technical format of the signature. Important mime types are application/signature+xml for X ML DigSig, application/jose for JWS, and image/* for a graphical image of a signature, etc.") |  | 0..1 | [code](datatypes.html#code) | The technical format of the signature [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [data](datatypes-definitions.html#Signature.data "Signature.data : The base64 encoding of the Signature content. When signature is not recorded electronically this element would be empty.") |  | 0..1 | [base64Binary](datatypes.html#base64Binary) | The actual signature content (XML DigSig. JWS, picture, etc.) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <type><!-- 1..* Coding Indication of the reason the entity signed the object(s) --></type>
 <when value="[instant]"/><!-- 1..1 When the signature was created -->
 <who><!-- 1..1 Reference(Practitioner|PractitionerRole|RelatedPerson|Patient|
   Device|Organization) Who signed --></who>
 <onBehalfOf><!-- 0..1 Reference(Practitioner|PractitionerRole|RelatedPerson|
   Patient|Device|Organization) The party represented --></onBehalfOf>
 <targetFormat value="[code]"/><!-- 0..1 The technical format of the signed resources -->
 <sigFormat value="[code]"/><!-- 0..1 The technical format of the signature -->
 <data value="[base64Binary]"/><!-- 0..1 The actual signature content (XML DigSig. JWS, picture, etc.) -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "type" : [{ Coding }], // R!  Indication of the reason the entity signed the object(s)
  "when" : "<instant>", // R!  When the signature was created
  "who" : { Reference(Practitioner|PractitionerRole|RelatedPerson|Patient|
   Device|Organization) }, // R!  Who signed
  "onBehalfOf" : { Reference(Practitioner|PractitionerRole|RelatedPerson|
   Patient|Device|Organization) }, // The party represented
  "targetFormat" : "<code>", // The technical format of the signed resources
  "sigFormat" : "<code>", // The technical format of the signature
  "data" : "<base64Binary>" // The actual signature content (XML DigSig. JWS, picture, etc.)
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Signature.type [ Coding ], ... ; # 1..* Indication of the reason the entity signed the object(s)
  fhir:Signature.when [ instant ]; # 1..1 When the signature was created
  fhir:Signature.who [ Reference(Practitioner|PractitionerRole|RelatedPerson|Patient|Device|Organization) ]; # 1..1 Who signed
  fhir:Signature.onBehalfOf [ Reference(Practitioner|PractitionerRole|RelatedPerson|Patient|Device|Organization) ]; # 0..1 The party represented
  fhir:Signature.targetFormat [ code ]; # 0..1 The technical format of the signed resources
  fhir:Signature.sigFormat [ code ]; # 0..1 The technical format of the signature
  fhir:Signature.data [ base64Binary ]; # 0..1 The actual signature content (XML DigSig. JWS, picture, etc.)
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Signature](datatypes.html#Signature) |  |
| Signature.who | - Renamed from who[x] to who - Remove Type uri |
| Signature.onBehalfOf | - Renamed from onBehalfOf[x] to onBehalfOf - Remove Type uri |
| Signature.targetFormat | - Added Element |
| Signature.sigFormat | - Added Element |
| Signature.data | - Renamed from blob to data |
| Signature.contentType | - deleted |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Signature](datatypes-definitions.html#Signature "Signature : A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [Element](element.html) | A Signature - XML DigSig, JWS, Graphical image of signature, etc. Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [type](datatypes-definitions.html#Signature.type "Signature.type : An indication of the reason that the entity signed this document. This may be explicitly included as part of the signature information and can be used when determining accountability for various actions concerning the document.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..\* | [Coding](datatypes.html#Coding) | Indication of the reason the entity signed the object(s) [Signature Type Codes](valueset-signature-type.html "An indication of the reason that an entity signed the object.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [when](datatypes-definitions.html#Signature.when "Signature.when : When the digital signature was signed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [instant](datatypes.html#instant) | When the signature was created |
| ... [who](datatypes-definitions.html#Signature.who "Signature.who : A reference to an application-usable description of the identity that signed  (e.g. the signature used their private key).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Patient](patient.html) | [Device](device.html) | [Organization](organization.html)) | Who signed |
| ... [onBehalfOf](datatypes-definitions.html#Signature.onBehalfOf "Signature.onBehalfOf : A reference to an application-usable description of the identity that is represented by the signature.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Patient](patient.html) | [Device](device.html) | [Organization](organization.html)) | The party represented |
| ... [targetFormat](datatypes-definitions.html#Signature.targetFormat "Signature.targetFormat : A mime type that indicates the technical format of the target resources signed by the signature.") |  | 0..1 | [code](datatypes.html#code) | The technical format of the signed resources [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [sigFormat](datatypes-definitions.html#Signature.sigFormat "Signature.sigFormat : A mime type that indicates the technical format of the signature. Important mime types are application/signature+xml for X ML DigSig, application/jose for JWS, and image/* for a graphical image of a signature, etc.") |  | 0..1 | [code](datatypes.html#code) | The technical format of the signature [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [data](datatypes-definitions.html#Signature.data "Signature.data : The base64 encoding of the Signature content. When signature is not recorded electronically this element would be empty.") |  | 0..1 | [base64Binary](datatypes.html#base64Binary) | The actual signature content (XML DigSig. JWS, picture, etc.) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <type><!-- 1..* Coding Indication of the reason the entity signed the object(s) --></type>
 <when value="[instant]"/><!-- 1..1 When the signature was created -->
 <who><!-- 1..1 Reference(Practitioner|PractitionerRole|RelatedPerson|Patient|
   Device|Organization) Who signed --></who>
 <onBehalfOf><!-- 0..1 Reference(Practitioner|PractitionerRole|RelatedPerson|
   Patient|Device|Organization) The party represented --></onBehalfOf>
 <targetFormat value="[code]"/><!-- 0..1 The technical format of the signed resources -->
 <sigFormat value="[code]"/><!-- 0..1 The technical format of the signature -->
 <data value="[base64Binary]"/><!-- 0..1 The actual signature content (XML DigSig. JWS, picture, etc.) -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "type" : [{ Coding }], // R!  Indication of the reason the entity signed the object(s)
  "when" : "<instant>", // R!  When the signature was created
  "who" : { Reference(Practitioner|PractitionerRole|RelatedPerson|Patient|
   Device|Organization) }, // R!  Who signed
  "onBehalfOf" : { Reference(Practitioner|PractitionerRole|RelatedPerson|
   Patient|Device|Organization) }, // The party represented
  "targetFormat" : "<code>", // The technical format of the signed resources
  "sigFormat" : "<code>", // The technical format of the signature
  "data" : "<base64Binary>" // The actual signature content (XML DigSig. JWS, picture, etc.)
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Signature.type [ Coding ], ... ; # 1..* Indication of the reason the entity signed the object(s)
  fhir:Signature.when [ instant ]; # 1..1 When the signature was created
  fhir:Signature.who [ Reference(Practitioner|PractitionerRole|RelatedPerson|Patient|Device|Organization) ]; # 1..1 Who signed
  fhir:Signature.onBehalfOf [ Reference(Practitioner|PractitionerRole|RelatedPerson|Patient|Device|Organization) ]; # 0..1 The party represented
  fhir:Signature.targetFormat [ code ]; # 0..1 The technical format of the signed resources
  fhir:Signature.sigFormat [ code ]; # 0..1 The technical format of the signature
  fhir:Signature.data [ base64Binary ]; # 0..1 The actual signature content (XML DigSig. JWS, picture, etc.)
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Signature](datatypes.html#Signature) |  |
| Signature.who | - Renamed from who[x] to who - Remove Type uri |
| Signature.onBehalfOf | - Renamed from onBehalfOf[x] to onBehalfOf - Remove Type uri |
| Signature.targetFormat | - Added Element |
| Signature.sigFormat | - Added Element |
| Signature.data | - Renamed from blob to data |
| Signature.contentType | - deleted |

See the [Full Difference](diff.html) for further information

**Constraints**

Notes:

- One consequence of signing the document is that URLs, identifiers and internal references are frozen and
  cannot be changed. This might be a desired feature, but it may also cripple interoperability between closed
  ecosystems where [re-identification](managing.html) frequently occurs. For this reason, it is
  recommended that systems consider carefully the impact of any signature processes. The impact of signatures
  on [Document bundles](documents.html) and their related processes is the most well understood
  use of digital signatures.
- Note that following common normalization procedures in XML causes consecutive whitespace within
  attributes to be normalized. As a result, whitespace within [markdown](datatypes.html#markdown) can be changed without
  breaking a digital signature. For elements with a type of markdown, this means that, in some
  cases, whitespace manipulation that results in significantly different visual rendering (e.g. changing
  indentation levels, causing content to appear in separate paragraphs rather than part of a single
  paragraph, etc.) might not be detected as a signature-breaking change. If this would present an
  unacceptable risk, systems should use the [JSON signature](json.html#canonical) approach as it does not normalize whitespace.

### 2.24.0.17.1 XML Signature rules

When the signature is an XML Digital Signature (contentType = application/signature+xml), the following rules apply:

- The Signature.data is base64 encoded XML-Signature
- The XML-Signature is a [Detached ![](external.png)](http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/#def-SignatureDetached) Signature (where the content that is signed is separate from the signature itself)
- The Signature SHOULD conform to XAdES-X-L for support of Long Term signatures. The XAdES-X-L specification adds the timestamp of the signing, inclusion of the signing certificate, and statement of revocation
- When FHIR Resources are signed, the signature is across the [Canonical XML form](xml.html#canonical) of the resource(s)
- The Signature SHOULD use the hashing algorithm SHA-256. Signature validation policy will apply to the signature and determine acceptability
- The Signature SHALL include a "CommitmentTypeIndication" element for the Purpose(s) of Signature. The Purpose can be the action being attested to, or the role associated with the signature. The value shall come from ASTM E1762-95(2013). The `Signature.type` shall contain the same values as the CommitmentTypeIndication element.

There are three levels of signature verification:

1. Verifying that the Digital Signature block itself has integrity through verifying the signature across the XML-Signature.
2. Confirming that the signer was authentic, not revoked, and appropriate to the signature purpose.
3. Confirming that the signed content of interest is unmodified using the hash algorithm.

Deviations from these guidelines would need to be expressed in site policy and would be enumerated in the XML-Signature block.
For example, some environments may choose a different XAdES profile, hashing algorithm, policy identifier, or signature purpose vocabulary.

### 2.24.0.17.2 JSON Signature rules

When the signature is an JSON Digital Signature (contentType = application/jose), the following rules apply:

- The Signature.data is base64 encoded JWS-Signature [RFC 7515: JSON Web Signature (JWS) ![](external.png)](https://tools.ietf.org/html/rfc7515)
- The signature is a [Detached ![](external.png)](https://tools.ietf.org/html/rfc7515#appendix-F) Signature (where the content that is signed is separate from the signature itself)
- When FHIR Resources are signed, the signature is across the [Canonical JSON form](json.html#canonical) of the resource(s)
- The Signature SHOULD use the hashing algorithm SHA256. Signature validation policy will apply to the signature and determine acceptability
- The Signature SHALL include a "CommitmentTypeIndication" element for the Purpose(s) of Signature. The Purpose can be the action being attested to, or the role associated with the signature. The value shall come from ASTM E1762-95(2013). The `Signature.type` shall contain the same values as the CommitmentTypeIndication element.

There are three levels of signature verification:

1. Verifying that the Digital Signature block itself has integrity through verifying the signature across the JWS-Signature.
2. Confirming that the signer was authentic, not revoked, and appropriate to the signature purpose.
3. Confirming that the signed content of interest is unmodified using the hash algorithm.

Deviations from these guidelines would need to be expressed in site policy and would be enumerated in the JWS-Signature block.
For example, some environments may choose a different hashing algorithm, policy identifier, or signature purpose vocabulary.

Signature is used in the following places: [Bundle](bundle.html#bundle), [Contract](contract.html#contract), [Provenance](provenance.html#provenance) and [VerificationResult](verificationresult.html#verificationresult)

## 2.24.0.18 Annotation

See also [Examples](datatypes-examples.html#Annotation), [Detailed Descriptions](datatypes-definitions.html#Annotation), [Mappings](datatypes-mappings.html#Annotation), [Profiles & Extensions](datatypes-extras.html#Annotation) and [R2 Conversions](datatypes-version-maps.html#Annotation).

A text note which also contains information about who made the statement and when.

- [Structure](#tabs-Annotation-struc)
- [UML](#tabs-Annotation-uml)
- [XML](#tabs-Annotation-xml)
- [JSON](#tabs-Annotation-json)
- [Turtle](#tabs-Annotation-ttl)
- [R3 Diff](#tabs-Annotation-diff)
- [All](#tabs-Annotation-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Annotation](datatypes-definitions.html#Annotation "Annotation : A  text note which also  contains information about who made the statement and when.") | [N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Text node with attribution Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [author[x]](datatypes-definitions.html#Annotation.author_x_ "Annotation.author[x] : The individual responsible for making the annotation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Individual responsible for the annotation |
| .... authorReference |  |  | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) |  |
| .... authorString |  |  | [string](datatypes.html#string) |  |
| ... [time](datatypes-definitions.html#Annotation.time "Annotation.time : Indicates when this particular annotation was made.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | When the annotation was made |
| ... [text](datatypes-definitions.html#Annotation.text "Annotation.text : The text of the annotation in markdown format.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [markdown](datatypes.html#markdown) | The annotation - text content (as markdown) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <author[x]><!-- 0..1 Reference(Practitioner|Patient|RelatedPerson|Organization)|
   string Individual responsible for the annotation --></author[x]>
 <time value="[dateTime]"/><!-- 0..1 When the annotation was made -->
 <text value="[markdown]"/><!-- 1..1 The annotation  - text content (as markdown) -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  // author[x]: Individual responsible for the annotation. One of these 2:
  "authorReference" : { Reference(Practitioner|Patient|RelatedPerson|Organization) },
  "authorString" : "<string>",
  "time" : "<dateTime>", // When the annotation was made
  "text" : "<markdown>" // R!  The annotation  - text content (as markdown)
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  # Annotation.author[x] : 0..1 Individual responsible for the annotation. One of these 2
    fhir:Annotation.authorReference [ Reference(Practitioner|Patient|RelatedPerson|Organization) ]
    fhir:Annotation.authorString [ string ]
  fhir:Annotation.time [ dateTime ]; # 0..1 When the annotation was made
  fhir:Annotation.text [ markdown ]; # 1..1 The annotation  - text content (as markdown)
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Annotation](datatypes.html#Annotation) |  |
| Annotation.text | - Type changed from string to markdown |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Annotation](datatypes-definitions.html#Annotation "Annotation : A  text note which also  contains information about who made the statement and when.") | [N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Text node with attribution Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [author[x]](datatypes-definitions.html#Annotation.author_x_ "Annotation.author[x] : The individual responsible for making the annotation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Individual responsible for the annotation |
| .... authorReference |  |  | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) |  |
| .... authorString |  |  | [string](datatypes.html#string) |  |
| ... [time](datatypes-definitions.html#Annotation.time "Annotation.time : Indicates when this particular annotation was made.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | When the annotation was made |
| ... [text](datatypes-definitions.html#Annotation.text "Annotation.text : The text of the annotation in markdown format.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [markdown](datatypes.html#markdown) | The annotation - text content (as markdown) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <author[x]><!-- 0..1 Reference(Practitioner|Patient|RelatedPerson|Organization)|
   string Individual responsible for the annotation --></author[x]>
 <time value="[dateTime]"/><!-- 0..1 When the annotation was made -->
 <text value="[markdown]"/><!-- 1..1 The annotation  - text content (as markdown) -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  // author[x]: Individual responsible for the annotation. One of these 2:
  "authorReference" : { Reference(Practitioner|Patient|RelatedPerson|Organization) },
  "authorString" : "<string>",
  "time" : "<dateTime>", // When the annotation was made
  "text" : "<markdown>" // R!  The annotation  - text content (as markdown)
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  # Annotation.author[x] : 0..1 Individual responsible for the annotation. One of these 2
    fhir:Annotation.authorReference [ Reference(Practitioner|Patient|RelatedPerson|Organization) ]
    fhir:Annotation.authorString [ string ]
  fhir:Annotation.time [ dateTime ]; # 0..1 When the annotation was made
  fhir:Annotation.text [ markdown ]; # 1..1 The annotation  - text content (as markdown)
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Annotation](datatypes.html#Annotation) |  |
| Annotation.text | - Type changed from string to markdown |

See the [Full Difference](diff.html) for further information

Systems that do not have structured annotations simply communicate a single annotation with no author or time.

This element may need to be included in narrative because of the potential for modifying information.

Annotations **SHOULD NOT** be used to communicate "modifying" information that could be computable
(this is a SHOULD because enforcing user behavior is nearly impossible).

Annotation is used in the following places: [AllergyIntolerance](allergyintolerance.html#allergyintolerance), [CarePlan](careplan.html#careplan), [CareTeam](careteam.html#careteam), [ChargeItem](chargeitem.html#chargeitem), [ClinicalImpression](clinicalimpression.html#clinicalimpression), [Communication](communication.html#communication), [CommunicationRequest](communicationrequest.html#communicationrequest), [Condition](condition.html#condition), [Contract](contract.html#contract), [Device](device.html#device), [DeviceDefinition](devicedefinition.html#devicedefinition), [DeviceRequest](devicerequest.html#devicerequest), [DeviceUseStatement](deviceusestatement.html#deviceusestatement), [EffectEvidenceSynthesis](effectevidencesynthesis.html#effectevidencesynthesis), [Evidence](evidence.html#evidence), [EvidenceVariable](evidencevariable.html#evidencevariable), [FamilyMemberHistory](familymemberhistory.html#familymemberhistory), [Goal](goal.html#goal), [GuidanceResponse](guidanceresponse.html#guidanceresponse), [ImagingStudy](imagingstudy.html#imagingstudy), [Immunization](immunization.html#immunization), [Invoice](invoice.html#invoice), [List](list.html#list), [Media](media.html#media), [MedicationAdministration](medicationadministration.html#medicationadministration), [MedicationDispense](medicationdispense.html#medicationdispense), [MedicationRequest](medicationrequest.html#medicationrequest), [MedicationStatement](medicationstatement.html#medicationstatement), [NutritionOrder](nutritionorder.html#nutritionorder), [Observation](observation.html#observation), [Procedure](procedure.html#procedure), [RequestGroup](requestgroup.html#requestgroup), [ResearchStudy](researchstudy.html#researchstudy), [RiskAssessment](riskassessment.html#riskassessment), [RiskEvidenceSynthesis](riskevidencesynthesis.html#riskevidencesynthesis), [ServiceRequest](servicerequest.html#servicerequest), [Specimen](specimen.html#specimen), [Task](task.html#task) and [VisionPrescription](visionprescription.html#visionprescription)

## 2.24.0.19 Open Type Element

Some elements do not have a specified type. The type is represented by the wildcard symbol "\*". In these cases, the element type may be one of the following:

**Primitive Types**

- [base64Binary](datatypes.html#base64Binary)
- [boolean](datatypes.html#boolean)
- [canonical](datatypes.html#canonical)
- [code](datatypes.html#code)
- [date](datatypes.html#date)
- [dateTime](datatypes.html#dateTime)
- [decimal](datatypes.html#decimal)
- [id](datatypes.html#id)
- [instant](datatypes.html#instant)
- [integer](datatypes.html#integer)
- [markdown](datatypes.html#markdown)
- [oid](datatypes.html#oid)
- [positiveInt](datatypes.html#positiveInt)
- [string](datatypes.html#string)
- [time](datatypes.html#time)
- [unsignedInt](datatypes.html#unsignedInt)
- [uri](datatypes.html#uri)
- [url](datatypes.html#url)
- [uuid](datatypes.html#uuid)

**Data Types**

- [Address](datatypes.html#Address)
- [Age](datatypes.html#Age)
- [Annotation](datatypes.html#Annotation)
- [Attachment](datatypes.html#Attachment)
- [CodeableConcept](datatypes.html#CodeableConcept)
- [Coding](datatypes.html#Coding)
- [ContactPoint](datatypes.html#ContactPoint)
- [Count](datatypes.html#Count)
- [Distance](datatypes.html#Distance)
- [Duration](datatypes.html#Duration)
- [HumanName](datatypes.html#HumanName)
- [Identifier](datatypes.html#Identifier)
- [Money](datatypes.html#Money)
- [Period](datatypes.html#Period)
- [Quantity](datatypes.html#Quantity)
- [Range](datatypes.html#Range)
- [Ratio](datatypes.html#Ratio)
- [Reference](references.html#Reference)
- [SampledData](datatypes.html#SampledData)
- [Signature](datatypes.html#Signature)
- [Timing](datatypes.html#Timing)

**MetaDataTypes**

- [ContactDetail](metadatatypes.html#ContactDetail)
- [Contributor](metadatatypes.html#Contributor)
- [DataRequirement](metadatatypes.html#DataRequirement)
- [Expression](metadatatypes.html#Expression)
- [ParameterDefinition](metadatatypes.html#ParameterDefinition)
- [RelatedArtifact](metadatatypes.html#RelatedArtifact)
- [TriggerDefinition](metadatatypes.html#TriggerDefinition)
- [UsageContext](metadatatypes.html#UsageContext)

**Special Types**

- [Dosage](dosage.html#Dosage)
- [Meta](resource.html#Meta)

The element name ends with "[x]", and this is replaced with the Title cased name of the data type.

Open references are used in the following places: [Parameters](parameters.html#parameters), [StructureMap](structuremap.html#structuremap) and [Task](task.html#task)

## 2.24.0.20 Other Types

The following types are defined as part of the data types, but are documented elsewhere in the specification:

- **[Resource](resource.html#metadata)** - the conceptual base class for all resources
- **[Reference](references.html#Reference)** - for references from one resource to another
- **[Extension](extensibility.html)** - used to convey additional data in a resource
- **[Narrative](narrative.html#Narrative)** - conveys a human-readable representation of the content of a resource
