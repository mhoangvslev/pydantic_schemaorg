from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class PropertyValueSpecification(SchemaOrgBase):
    """A Property value specification.

    See: https://schema.org/PropertyValueSpecification
    Model depth: 3
    """
    type_: str = Field(default="PropertyValueSpecification", alias='@type')
    
    valueMinLength: Union[List[str], str] = Field(
        default=None,
        description="Specifies the minimum allowed range for number of characters in a literal value.",union_mode="smart"
    )
    
    valueMaxLength: Union[List[str], str] = Field(
        default=None,
        description="Specifies the allowed range for number of characters in a literal value.",union_mode="smart"
    )
    
    valuePattern: Union[List[str], str] = Field(
        default=None,
        description="Specifies a regular expression for testing literal values according to the HTML spec.",union_mode="smart"
    )
    
    valueRequired: Union[List[str], str] = Field(
        default=None,
        description="Whether the property must be filled in to complete the action. Default is false.",union_mode="smart"
    )
    
    valueName: Union[List[str], str] = Field(
        default=None,
        description="Indicates the name of the PropertyValueSpecification to be used in URL templates and"
     "form encoding in a manner analogous to HTML's input@name.",union_mode="smart"
    )
    
    minValue: Union[List[str], str] = Field(
        default=None,
        description="The lower value of some characteristic or property.",union_mode="smart"
    )
    
    multipleValues: Union[List[str], str] = Field(
        default=None,
        description="Whether multiple values are allowed for the property. Default is false.",union_mode="smart"
    )
    
    defaultValue: Union[List[str], str] = Field(
        default=None,
        description="The default value of the input. For properties that expect a literal, the default is a"
     "literal value, for properties that expect an object, it's an ID reference to one of the"
     "current values.",union_mode="smart"
    )
    
    maxValue: Union[List[str], str] = Field(
        default=None,
        description="The upper value of some characteristic or property.",union_mode="smart"
    )
    
    readonlyValue: Union[List[str], str] = Field(
        default=None,
        description="Whether or not a property is mutable. Default is false. Specifying this for a property"
     "that also has a value makes it act similar to a \"hidden\" input in an HTML form.",union_mode="smart"
    )
    
    stepValue: Union[List[str], str] = Field(
        default=None,
        description="The stepValue attribute indicates the granularity that is expected (and required)"
     "of the value in a PropertyValueSpecification.",union_mode="smart"
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
    from pydantic_schemaorg import Text, StrictBool, Boolean, Thing, Number, StrictInt, StrictFloat
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
