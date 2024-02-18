from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class EntryPoint(SchemaOrgBase):
    """An entry point, within some Web-based protocol.

    See: https://schema.org/EntryPoint
    Model depth: 3
    """
    type_: str = Field(default="EntryPoint", alias='@type')
    
    encodingType: Union[List[str], str] = Field(
        default=None,
        description="The supported encoding type(s) for an EntryPoint request.",union_mode="smart"
    )
    
    contentType: Union[List[str], str] = Field(
        default=None,
        description="The supported content type(s) for an EntryPoint response.",union_mode="smart"
    )
    
    actionPlatform: Union[List[str], str] = Field(
        default=None,
        description="The high level platform(s) where the Action can be performed for the given URL. To specify"
     "a specific application or operating system instance, use actionApplication.",union_mode="smart"
    )
    
    urlTemplate: Union[List[str], str] = Field(
        default=None,
        description="An url template (RFC6570) that will be used to construct the target of the execution of"
     "the action.",union_mode="smart"
    )
    
    application: Union[List[str], str] = Field(
        default=None,
        description="An application that can complete the request.",union_mode="smart"
    )
    
    actionApplication: Union[List[str], str] = Field(
        default=None,
        description="An application that can complete the request.",union_mode="smart"
    )
    
    httpMethod: Union[List[str], str] = Field(
        default=None,
        description="An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint."
     "Values are capitalized strings as used in HTTP.",union_mode="smart"
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
    from pydantic_schemaorg import Text, SoftwareApplication, URL, DigitalPlatformEnumeration, AnyUrl
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
