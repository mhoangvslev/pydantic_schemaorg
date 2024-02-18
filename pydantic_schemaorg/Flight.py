from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import datetime
from datetime import datetime, time
from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class Flight(SchemaOrgBase):
    """An airline flight.

    See: https://schema.org/Flight
    Model depth: 4
    """
    type_: str = Field(default="Flight", alias='@type')
    
    departureGate: Union[List[str], str] = Field(
        default=None,
        description="Identifier of the flight's departure gate.",union_mode="smart"
    )
    
    mealService: Union[List[str], str] = Field(
        default=None,
        description="Description of the meals that will be provided or available for purchase.",union_mode="smart"
    )
    
    estimatedFlightDuration: Union[List[str], str] = Field(
        default=None,
        description="The estimated time the flight will take.",union_mode="smart"
    )
    
    seller: Union[List[str], str] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",union_mode="smart"
    )
    
    arrivalAirport: Union[List[str], str] = Field(
        default=None,
        description="The airport where the flight terminates.",union_mode="smart"
    )
    
    carrier: Union[List[str], str] = Field(
        default=None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",union_mode="smart"
    )
    
    boardingPolicy: Union[List[str], str] = Field(
        default=None,
        description="The type of boarding policy used by the airline (e.g. zone-based or group-based).",union_mode="smart"
    )
    
    departureAirport: Union[List[str], str] = Field(
        default=None,
        description="The airport where the flight originates.",union_mode="smart"
    )
    
    webCheckinTime: Union[List[str], str] = Field(
        default=None,
        description="The time when a passenger can check into the flight online.",union_mode="smart"
    )
    
    flightDistance: Union[List[str], str] = Field(
        default=None,
        description="The distance of the flight.",union_mode="smart"
    )
    
    departureTerminal: Union[List[str], str] = Field(
        default=None,
        description="Identifier of the flight's departure terminal.",union_mode="smart"
    )
    
    flightNumber: Union[List[str], str] = Field(
        default=None,
        description="The unique identifier for a flight including the airline IATA code. For example, if describing"
     "United flight 110, where the IATA code for United is 'UA', the flightNumber is 'UA110'.",union_mode="smart"
    )
    
    arrivalTerminal: Union[List[str], str] = Field(
        default=None,
        description="Identifier of the flight's arrival terminal.",union_mode="smart"
    )
    
    aircraft: Union[List[str], str] = Field(
        default=None,
        description="The kind of aircraft (e.g., \"Boeing 747\").",union_mode="smart"
    )
    
    arrivalGate: Union[List[str], str] = Field(
        default=None,
        description="Identifier of the flight's arrival gate.",union_mode="smart"
    )
    
    departureTime: Union[List[str], str] = Field(
        default=None,
        description="The expected departure time.",union_mode="smart"
    )
    
    tripOrigin: Union[List[str], str] = Field(
        default=None,
        description="The location of origin of the trip, prior to any destination(s).",union_mode="smart"
    )
    
    offers: Union[List[str], str] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",union_mode="smart"
    )
    
    itinerary: Union[List[str], str] = Field(
        default=None,
        description="Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is"
     "important use [[ItemList]] to specify that order (see examples).",union_mode="smart"
    )
    
    provider: Union[List[str], str] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",union_mode="smart"
    )
    
    arrivalTime: Union[List[str], str] = Field(
        default=None,
        description="The expected arrival time.",union_mode="smart"
    )
    
    partOfTrip: Union[List[str], str] = Field(
        default=None,
        description="Identifies that this [[Trip]] is a subTrip of another Trip. For example Day 1, Day 2, etc."
     "of a multi-day trip.",union_mode="smart"
    )
    
    subTrip: Union[List[str], str] = Field(
        default=None,
        description="Identifies a [[Trip]] that is a subTrip of this Trip. For example Day 1, Day 2, etc. of a"
     "multi-day trip.",union_mode="smart"
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
    from pydantic_schemaorg import Organization, Distance, datetime, Vehicle, DateTime, Person, Text, BoardingPolicyType, Airport, Duration
    from pydantic_schemaorg import Organization, datetime, Trip, DateTime, Demand, Offer, Time, Person, time, Place, ItemList
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
