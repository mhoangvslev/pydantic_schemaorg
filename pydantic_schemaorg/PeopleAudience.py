from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union
from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class PeopleAudience(SchemaOrgBase):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    See: https://schema.org/PeopleAudience
    Model depth: 4
    """
    type_: str = Field(default="PeopleAudience", alias='@type')
    
    suggestedMaxAge: Union[List[str], str] = Field(
        default=None,
        description="Maximum recommended age in years for the audience or user.",union_mode="smart"
    )
    
    requiredMinAge: Union[List[str], str] = Field(
        default=None,
        description="Audiences defined by a person's minimum age.",union_mode="smart"
    )
    
    requiredGender: Union[List[str], str] = Field(
        default=None,
        description="Audiences defined by a person's gender.",union_mode="smart"
    )
    
    healthCondition: Union[List[str], str] = Field(
        default=None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",union_mode="smart"
    )
    
    suggestedMeasurement: Union[List[str], str] = Field(
        default=None,
        description="A suggested range of body measurements for the intended audience or person, for example"
     "inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size"
     "chart for wearable products.",union_mode="smart"
    )
    
    suggestedMinAge: Union[List[str], str] = Field(
        default=None,
        description="Minimum recommended age in years for the audience or user.",union_mode="smart"
    )
    
    suggestedGender: Union[List[str], str] = Field(
        default=None,
        description="The suggested gender of the intended person or audience, for example \"male\", \"female\","
     "or \"unisex\".",union_mode="smart"
    )
    
    suggestedAge: Union[List[str], str] = Field(
        default=None,
        description="The age or age range for the intended audience or person, for example 3-12 months for infants,"
     "1-5 years for toddlers.",union_mode="smart"
    )
    
    requiredMaxAge: Union[List[str], str] = Field(
        default=None,
        description="Audiences defined by a person's maximum age.",union_mode="smart"
    )
    
    audienceType: Union[List[str], str] = Field(
        default=None,
        description="The target group associated with a given audience (e.g. veterans, car owners, musicians,"
     "etc.).",union_mode="smart"
    )
    
    geographicArea: Union[List[str], str] = Field(
        default=None,
        description="The geographic area associated with the audience.",union_mode="smart"
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
    from pydantic_schemaorg import StrictInt, StrictFloat, QuantitativeValue, int, Text, GenderType, Integer, MedicalCondition, Number
    from pydantic_schemaorg import Text, AdministrativeArea
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
