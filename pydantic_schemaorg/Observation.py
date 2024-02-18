from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from datetime import datetime
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class Observation(SchemaOrgBase):
    """Instances of the class [[Observation]] are used to specify observations about an entity"
     "at a particular time. The principal properties of an [[Observation]] are [[observationAbout]],"
     "[[measuredProperty]], [[statType]], [[value] and [[observationDate]] and [[measuredProperty]]."
     "Some but not all Observations represent a [[QuantitativeValue]]. Quantitative observations"
     "can be about a [[StatisticalVariable]], which is an abstract specification about which"
     "we can make observations that are grounded at a particular location and time. Observations"
     "can also encode a subset of simple RDF-like statements (its observationAbout, a StatisticalVariable,"
     "defining the measuredPoperty; its observationAbout property indicating the entity"
     "the statement is about, and [[value]] ) In the context of a quantitative knowledge graph,"
     "typical properties could include [[measuredProperty]], [[observationAbout]],"
     "[[observationDate]], [[value]], [[unitCode]], [[unitText]], [[measurementMethod]].

    See: https://schema.org/Observation
    Model depth: 3
    """
    type_: str = Field(default="Observation", alias='@type')
    
    measurementQualifier: Union[List[str], str] = Field(
        default=None,
        description="Provides additional qualification to an observation. For example, a GDP observation"
     "measures the Nominal value.",union_mode="smart"
    )
    
    measurementMethod: Union[List[str], str] = Field(
        default=None,
        description="A subproperty of [[measurementTechnique]] that can be used for specifying specific"
     "methods, in particular via [[MeasurementMethodEnum]].",union_mode="smart"
    )
    
    observationAbout: Union[List[str], str] = Field(
        default=None,
        description="The [[observationAbout]] property identifies an entity, often a [[Place]], associated"
     "with an [[Observation]].",union_mode="smart"
    )
    
    observationPeriod: Union[List[str], str] = Field(
        default=None,
        description="The length of time an Observation took place over. The format follows `P[0-9]*[Y|M|D|h|m|s]`."
     "For example, P1Y is Period 1 Year, P3M is Period 3 Months, P3h is Period 3 hours.",union_mode="smart"
    )
    
    variableMeasured: Union[List[str], str] = Field(
        default=None,
        description="The variableMeasured property can indicate (repeated as necessary) the variables"
     "that are measured in some dataset, either described as text or as pairs of identifier"
     "and description using PropertyValue, or more explicitly as a [[StatisticalVariable]].",union_mode="smart"
    )
    
    measurementTechnique: Union[List[str], str] = Field(
        default=None,
        description="A technique, method or technology used in an [[Observation]], [[StatisticalVariable]]"
     "or [[Dataset]] (or [[DataDownload]], [[DataCatalog]]), corresponding to the method"
     "used for measuring the corresponding variable(s) (for datasets, described using [[variableMeasured]];"
     "for [[Observation]], a [[StatisticalVariable]]). Often but not necessarily each"
     "[[variableMeasured]] will have an explicit representation as (or mapping to) an property"
     "such as those defined in Schema.org, or other RDF vocabularies and \"knowledge graphs\"."
     "In that case the subproperty of [[variableMeasured]] called [[measuredProperty]]"
     "is applicable. The [[measurementTechnique]] property helps when extra clarification"
     "is needed about how a [[measuredProperty]] was measured. This is oriented towards scientific"
     "and scholarly dataset publication but may have broader applicability; it is not intended"
     "as a full representation of measurement, but can often serve as a high level summary for"
     "dataset discovery. For example, if [[variableMeasured]] is: molecule concentration,"
     "[[measurementTechnique]] could be: \"mass spectrometry\" or \"nmr spectroscopy\""
     "or \"colorimetry\" or \"immunofluorescence\". If the [[variableMeasured]] is \"depression"
     "rating\", the [[measurementTechnique]] could be \"Zung Scale\" or \"HAM-D\" or \"Beck"
     "Depression Inventory\". If there are several [[variableMeasured]] properties recorded"
     "for some given data object, use a [[PropertyValue]] for each [[variableMeasured]]"
     "and attach the corresponding [[measurementTechnique]]. The value can also be from"
     "an enumeration, organized as a [[MeasurementMetholdEnumeration]].",union_mode="smart"
    )
    
    observationDate: Union[List[str], str] = Field(
        default=None,
        description="The observationDate of an [[Observation]].",union_mode="smart"
    )
    
    measuredProperty: Union[List[str], str] = Field(
        default=None,
        description="The measuredProperty of an [[Observation]], typically via its [[StatisticalVariable]]."
     "There are various kinds of applicable [[Property]]: a schema.org property, a property"
     "from other RDF-compatible systems, e.g. W3C RDF Data Cube, Data Commons, Wikidata,"
     "or schema.org extensions such as [GS1's](https://www.gs1.org/voc/?show=properties).",union_mode="smart"
    )
    
    measurementDenominator: Union[List[str], str] = Field(
        default=None,
        description="Identifies the denominator variable when an observation represents a ratio or percentage.",union_mode="smart"
    )
    
    marginOfError: Union[List[str], str] = Field(
        default=None,
        description="A [[marginOfError]] for an [[Observation]].",union_mode="smart"
    )
    
    unitText: Union[List[str], str] = Field(
        default=None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard"
     "unit code for <a href='unitCode'>unitCode</a>.",union_mode="smart"
    )
    
    unitCode: Union[List[str], str] = Field(
        default=None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL."
     "Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",union_mode="smart"
    )
    
    additionalProperty: Union[List[str], str] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g."
     "a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. http://schema.org/width, http://schema.org/color,"
     "http://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",union_mode="smart"
    )
    
    value: Union[List[str], str] = Field(
        default=None,
        description="The value of a [[QuantitativeValue]] (including [[Observation]]) or property value"
     "node. * For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for"
     "values is 'Number'. * For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean',"
     "or 'StructuredValue'. * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030)"
     "to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use"
     "'.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid"
     "using these symbols as a readability separator.",union_mode="smart"
    )
    
    valueReference: Union[List[str], str] = Field(
        default=None,
        description="A secondary value that provides additional information on the original value, e.g."
     "a reference temperature or a type of measurement.",union_mode="smart"
    )
    
    minValue: Union[List[str], str] = Field(
        default=None,
        description="The lower value of some characteristic or property.",union_mode="smart"
    )
    
    maxValue: Union[List[str], str] = Field(
        default=None,
        description="The upper value of some characteristic or property.",union_mode="smart"
    )
    
    subjectOf: Union[List[str], str] = Field(
        default=None,
        description="A CreativeWork or Event about this Thing.",union_mode="smart"
    )
    
    mainEntityOfPage: Union[List[str], str] = Field(
        default=None,
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being"
     "described. See [background notes](/docs/datamodel.html#mainEntityBackground)"
     "for details.",union_mode="smart"
    )
    
    identifier: Union[List[str], str] = Field(
        default=None,
        description="The identifier property represents any kind of identifier for any kind of [[Thing]],"
     "such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for"
     "representing many of these, either as textual strings or as URL (URI) links. See [background"
     "notes](/docs/datamodel.html#identifierBg) for more details.",union_mode="smart"
    )
    
    image: Union[List[str], str] = Field(
        default=None,
        description="An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].",union_mode="smart"
    )
    
    name: Union[List[str], str] = Field(
        default=None,
        description="The name of the item.",union_mode="smart"
    )
    
    url: Union[List[str], str] = Field(
        default=None,
        description="URL of the item.",union_mode="smart"
    )
    
    sameAs: Union[List[str], str] = Field(
        default=None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the"
     "URL of the item's Wikipedia page, Wikidata entry, or official website.",union_mode="smart"
    )
    
    disambiguatingDescription: Union[List[str], str] = Field(
        default=None,
        description="A sub property of description. A short description of the item used to disambiguate from"
     "other, similar items. Information from other properties (in particular, name) may"
     "be necessary for the description to be useful for disambiguation.",union_mode="smart"
    )
    
    alternateName: Union[List[str], str] = Field(
        default=None,
        description="An alias for the item.",union_mode="smart"
    )
    
    description: Union[List[str], str] = Field(
        default=None,
        description="A description of the item.",union_mode="smart"
    )
    
    potentialAction: Union[List[str], str] = Field(
        default=None,
        description="Indicates a potential Action, which describes an idealized action in which this thing"
     "would play an 'object' role.",union_mode="smart"
    )
    
    additionalType: Union[List[str], str] = Field(
        default=None,
        description="An additional type for the item, typically used for adding more specific types from external"
     "vocabularies in microdata syntax. This is a relationship between something and a class"
     "that the thing is in. Typically the value is a URI-identified RDF class, and in this case"
     "corresponds to the use of rdf:type in RDF. Text values can be used sparingly, for cases"
     "where useful information can be added without their being an appropriate schema to reference."
     "In the case of text values, the class label should follow the schema.org <a href=\"http://schema.org/docs/styleguide.html\">style"
     "guide</a>.",union_mode="smart"
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg import StatisticalVariable, datetime, Property, DateTime, QuantitativeValue, Thing, PropertyValue, Enumeration, Text, URL, Place, DefinedTerm, MeasurementMethodEnum, AnyUrl
    from pydantic_schemaorg import Boolean, QualitativeValue, QuantitativeValue, PropertyValue, Text, StrictBool, MeasurementTypeEnumeration, URL, Number, Enumeration, DefinedTerm, StructuredValue, AnyUrl, StrictInt, StrictFloat
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
