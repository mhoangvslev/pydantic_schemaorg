from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class Reservation(SchemaOrgBase):
    """Describes a reservation for travel, dining or an event. Some reservations require tickets."
     "Note: This type is for information about actual reservations, e.g. in confirmation"
     "emails or HTML pages with individual confirmations of reservations. For offers of tickets,"
     "restaurant reservations, flights, or rental cars, use [[Offer]].

    See: https://schema.org/Reservation
    Model depth: 3
    """
    type_: str = Field(default="Reservation", alias='@type')
    
    bookingTime: Union[List[str], str] = Field(
        default=None,
        description="The date and time the reservation was booked.",union_mode="smart"
    )
    
    priceCurrency: Union[List[str], str] = Field(
        default=None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
     "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",union_mode="smart"
    )
    
    modifiedTime: Union[List[str], str] = Field(
        default=None,
        description="The date and time the reservation was modified.",union_mode="smart"
    )
    
    bookingAgent: Union[List[str], str] = Field(
        default=None,
        description="'bookingAgent' is an out-dated term indicating a 'broker' that serves as a booking agent.",union_mode="smart"
    )
    
    reservationId: Union[List[str], str] = Field(
        default=None,
        description="A unique identifier for the reservation.",union_mode="smart"
    )
    
    underName: Union[List[str], str] = Field(
        default=None,
        description="The person or organization the reservation or ticket is for.",union_mode="smart"
    )
    
    reservationStatus: Union[List[str], str] = Field(
        default=None,
        description="The current status of the reservation.",union_mode="smart"
    )
    
    provider: Union[List[str], str] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",union_mode="smart"
    )
    
    reservedTicket: Union[List[str], str] = Field(
        default=None,
        description="A ticket associated with the reservation.",union_mode="smart"
    )
    
    programMembershipUsed: Union[List[str], str] = Field(
        default=None,
        description="Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the"
     "reservation.",union_mode="smart"
    )
    
    broker: Union[List[str], str] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",union_mode="smart"
    )
    
    reservationFor: Union[List[str], str] = Field(
        default=None,
        description="The thing -- flight, event, restaurant, etc. being reserved.",union_mode="smart"
    )
    
    totalPrice: Union[List[str], str] = Field(
        default=None,
        description="The total price for the reservation or ticket, including applicable taxes, shipping,"
     "etc. Usage guidelines: * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030)"
     "to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use"
     "'.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid"
     "using these symbols as a readability separator.",union_mode="smart"
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
    from pydantic_schemaorg import Organization, StrictInt, StrictFloat, datetime, DateTime, PriceSpecification, Ticket, Thing, Person, Text, ProgramMembership, ReservationStatusType, Number
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
