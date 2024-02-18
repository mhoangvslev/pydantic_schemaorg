from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class ContactPoint(SchemaOrgBase):
    """A contact point&#x2014;for example, a Customer Complaints department.

    See: https://schema.org/ContactPoint
    Model depth: 4
    """
    type_: str = Field(default="ContactPoint", alias='@type')
    
    contactType: Union[List[str], str] = Field(
        default=None,
        description="A person or organization can have different contact points, for different purposes."
     "For example, a sales contact point, a PR contact point and so on. This property is used"
     "to specify the kind of contact point.",union_mode="smart"
    )
    
    telephone: Union[List[str], str] = Field(
        default=None,
        description="The telephone number.",union_mode="smart"
    )
    
    contactOption: Union[List[str], str] = Field(
        default=None,
        description="An option available on this contact point (e.g. a toll-free number or support for hearing-impaired"
     "callers).",union_mode="smart"
    )
    
    email: Union[List[str], str] = Field(
        default=None,
        description="Email address.",union_mode="smart"
    )
    
    productSupported: Union[List[str], str] = Field(
        default=None,
        description="The product or service this support contact point is related to (such as product support"
     "for a particular product line). This can be a specific product or product line (e.g. \"iPhone\")"
     "or a general category of products or services (e.g. \"smartphones\").",union_mode="smart"
    )
    
    faxNumber: Union[List[str], str] = Field(
        default=None,
        description="The fax number.",union_mode="smart"
    )
    
    serviceArea: Union[List[str], str] = Field(
        default=None,
        description="The geographic area where the service is provided.",union_mode="smart"
    )
    
    availableLanguage: Union[List[str], str] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]].",union_mode="smart"
    )
    
    hoursAvailable: Union[List[str], str] = Field(
        default=None,
        description="The hours during which this service or contact is available.",union_mode="smart"
    )
    
    areaServed: Union[List[str], str] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",union_mode="smart"
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
    from pydantic_schemaorg import Language, Product, GeoShape, ContactPointOption, Text, OpeningHoursSpecification, Place, AdministrativeArea
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
