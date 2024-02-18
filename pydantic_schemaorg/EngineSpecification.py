from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class EngineSpecification(SchemaOrgBase):
    """Information about the engine of the vehicle. A vehicle can have multiple engines represented"
     "by multiple engine specification entities.

    See: https://schema.org/EngineSpecification
    Model depth: 4
    """
    type_: str = Field(default="EngineSpecification", alias='@type')
    
    enginePower: Union[List[str], str] = Field(
        default=None,
        description="The power of the vehicle's engine. Typical unit code(s): KWT for kilowatt, BHP for brake"
     "horsepower, N12 for metric horsepower (PS, with 1 PS = 735,49875 W) * Note 1: There are"
     "many different ways of measuring an engine's power. For an overview, see [http://en.wikipedia.org/wiki/Horsepower#Engine\_power\_test\_codes](http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes)."
     "* Note 2: You can link to information about how the given value has been determined using"
     "the [[valueReference]] property. * Note 3: You can use [[minValue]] and [[maxValue]]"
     "to indicate ranges.",union_mode="smart"
    )
    
    engineType: Union[List[str], str] = Field(
        default=None,
        description="The type of engine or engines powering the vehicle.",union_mode="smart"
    )
    
    fuelType: Union[List[str], str] = Field(
        default=None,
        description="The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only"
     "one engine, this property can be attached directly to the vehicle.",union_mode="smart"
    )
    
    engineDisplacement: Union[List[str], str] = Field(
        default=None,
        description="The volume swept by all of the pistons inside the cylinders of an internal combustion"
     "engine in a single movement. Typical unit code(s): CMQ for cubic centimeter, LTR for"
     "liters, INQ for cubic inches * Note 1: You can link to information about how the given value"
     "has been determined using the [[valueReference]] property. * Note 2: You can use [[minValue]]"
     "and [[maxValue]] to indicate ranges.",union_mode="smart"
    )
    
    torque: Union[List[str], str] = Field(
        default=None,
        description="The torque (turning force) of the vehicle's engine. Typical unit code(s): NU for newton"
     "metre (N m), F17 for pound-force per foot, or F48 for pound-force per inch * Note 1: You"
     "can link to information about how the given value has been determined (e.g. reference"
     "RPM) using the [[valueReference]] property. * Note 2: You can use [[minValue]] and [[maxValue]]"
     "to indicate ranges.",union_mode="smart"
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
    from pydantic_schemaorg import Text, URL, QualitativeValue, QuantitativeValue, AnyUrl
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
