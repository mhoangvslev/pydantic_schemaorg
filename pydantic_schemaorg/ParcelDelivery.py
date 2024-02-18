from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import List, Optional, Union
from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class ParcelDelivery(SchemaOrgBase):
    """The delivery of a parcel either via the postal service or a commercial service.

    See: https://schema.org/ParcelDelivery
    Model depth: 3
    """
    type_: str = Field(default="ParcelDelivery", alias='@type')
    
    trackingUrl: Union[List[str], str] = Field(
        default=None,
        description="Tracking url for the parcel delivery.",union_mode="smart"
    )
    
    deliveryStatus: Union[List[str], str] = Field(
        default=None,
        description="New entry added as the package passes through each leg of its journey (from shipment to"
     "final delivery).",union_mode="smart"
    )
    
    trackingNumber: Union[List[str], str] = Field(
        default=None,
        description="Shipper tracking number.",union_mode="smart"
    )
    
    hasDeliveryMethod: Union[List[str], str] = Field(
        default=None,
        description="Method used for delivery or shipping.",union_mode="smart"
    )
    
    provider: Union[List[str], str] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",union_mode="smart"
    )
    
    carrier: Union[List[str], str] = Field(
        default=None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",union_mode="smart"
    )
    
    originAddress: Union[List[str], str] = Field(
        default=None,
        description="Shipper's address.",union_mode="smart"
    )
    
    itemShipped: Union[List[str], str] = Field(
        default=None,
        description="Item(s) being shipped.",union_mode="smart"
    )
    
    deliveryAddress: Union[List[str], str] = Field(
        default=None,
        description="Destination address.",union_mode="smart"
    )
    
    expectedArrivalUntil: Union[List[str], str] = Field(
        default=None,
        description="The latest date the package may arrive.",union_mode="smart"
    )
    
    expectedArrivalFrom: Union[List[str], str] = Field(
        default=None,
        description="The earliest date the package may arrive.",union_mode="smart"
    )
    
    partOfOrder: Union[List[str], str] = Field(
        default=None,
        description="The overall order the items in this delivery were included in.",union_mode="smart"
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
    from pydantic_schemaorg import date, Organization, Product, datetime, DeliveryMethod, DateTime, DeliveryEvent, Date, Person, Text, Order, URL, AnyUrl, PostalAddress
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
