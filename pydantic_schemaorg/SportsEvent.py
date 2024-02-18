from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from datetime import date, datetime, time
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class SportsEvent(SchemaOrgBase):
    """Event type: Sports event.

    See: https://schema.org/SportsEvent
    Model depth: 3
    """
    type_: str = Field(default="SportsEvent", alias='@type')
    
    homeTeam: Union[List[str], str] = Field(
        default=None,
        description="The home team in a sports event.",union_mode="smart"
    )
    
    sport: Union[List[str], str] = Field(
        default=None,
        description="A type of sport (e.g. Baseball).",union_mode="smart"
    )
    
    competitor: Union[List[str], str] = Field(
        default=None,
        description="A competitor in a sports event.",union_mode="smart"
    )
    
    awayTeam: Union[List[str], str] = Field(
        default=None,
        description="The away team in a sports event.",union_mode="smart"
    )
    
    superEvent: Union[List[str], str] = Field(
        default=None,
        description="An event that this event is a part of. For example, a collection of individual music performances"
     "might each have a music festival as their superEvent.",union_mode="smart"
    )
    
    performers: Union[List[str], str] = Field(
        default=None,
        description="The main performer or performers of the event&#x2014;for example, a presenter, musician,"
     "or actor.",union_mode="smart"
    )
    
    funding: Union[List[str], str] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",union_mode="smart"
    )
    
    isAccessibleForFree: Union[List[str], str] = Field(
        default=None,
        description="A flag to signal that the item, event, or place is accessible for free.",union_mode="smart"
    )
    
    about: Union[List[str], str] = Field(
        default=None,
        description="The subject matter of the content.",union_mode="smart"
    )
    
    director: Union[List[str], str] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",union_mode="smart"
    )
    
    sponsor: Union[List[str], str] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",union_mode="smart"
    )
    
    doorTime: Union[List[str], str] = Field(
        default=None,
        description="The time admission will commence.",union_mode="smart"
    )
    
    inLanguage: Union[List[str], str] = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",union_mode="smart"
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
    
    maximumAttendeeCapacity: Union[List[str], str] = Field(
        default=None,
        description="The total number of individuals that may attend an event or venue.",union_mode="smart"
    )
    
    audience: Union[List[str], str] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",union_mode="smart"
    )
    
    eventSchedule: Union[List[str], str] = Field(
        default=None,
        description="Associates an [[Event]] with a [[Schedule]]. There are circumstances where it is preferable"
     "to share a schedule for a series of repeating events rather than data on the individual"
     "events themselves. For example, a website or application might prefer to publish a schedule"
     "for a weekly gym class rather than provide data on every event. A schedule could be processed"
     "by applications to add forthcoming events to a calendar. An [[Event]] that is associated"
     "with a [[Schedule]] using this property should not have [[startDate]] or [[endDate]]"
     "properties. These are instead defined within the associated [[Schedule]], this avoids"
     "any ambiguity for clients using the data. The property might have repeated values to"
     "specify different schedules, e.g. for different months or seasons.",union_mode="smart"
    )
    
    subEvent: Union[List[str], str] = Field(
        default=None,
        description="An Event that is part of this event. For example, a conference event includes many presentations,"
     "each of which is a subEvent of the conference.",union_mode="smart"
    )
    
    attendees: Union[List[str], str] = Field(
        default=None,
        description="A person attending the event.",union_mode="smart"
    )
    
    actor: Union[List[str], str] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",union_mode="smart"
    )
    
    typicalAgeRange: Union[List[str], str] = Field(
        default=None,
        description="The typical expected age range, e.g. '7-9', '11-'.",union_mode="smart"
    )
    
    aggregateRating: Union[List[str], str] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",union_mode="smart"
    )
    
    duration: Union[List[str], str] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",union_mode="smart"
    )
    
    maximumPhysicalAttendeeCapacity: Union[List[str], str] = Field(
        default=None,
        description="The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]]"
     "is [[OfflineEventAttendanceMode]] (or the offline aspects, in the case of a [[MixedEventAttendanceMode]]).",union_mode="smart"
    )
    
    funder: Union[List[str], str] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",union_mode="smart"
    )
    
    eventAttendanceMode: Union[List[str], str] = Field(
        default=None,
        description="The eventAttendanceMode of an event indicates whether it occurs online, offline, or"
     "a mix.",union_mode="smart"
    )
    
    subEvents: Union[List[str], str] = Field(
        default=None,
        description="Events that are a part of this event. For example, a conference event includes many presentations,"
     "each subEvents of the conference.",union_mode="smart"
    )
    
    maximumVirtualAttendeeCapacity: Union[List[str], str] = Field(
        default=None,
        description="The maximum virtual attendee capacity of an [[Event]] whose [[eventAttendanceMode]]"
     "is [[OnlineEventAttendanceMode]] (or the online aspects, in the case of a [[MixedEventAttendanceMode]]).",union_mode="smart"
    )
    
    attendee: Union[List[str], str] = Field(
        default=None,
        description="A person or organization attending the event.",union_mode="smart"
    )
    
    startDate: Union[List[str], str] = Field(
        default=None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",union_mode="smart"
    )
    
    keywords: Union[List[str], str] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
     "are typically delimited by commas, or by repeating the property.",union_mode="smart"
    )
    
    location: Union[List[str], str] = Field(
        default=None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",union_mode="smart"
    )
    
    review: Union[List[str], str] = Field(
        default=None,
        description="A review of the item.",union_mode="smart"
    )
    
    composer: Union[List[str], str] = Field(
        default=None,
        description="The person or organization who wrote a composition, or who is the composer of a work performed"
     "at some event.",union_mode="smart"
    )
    
    previousStartDate: Union[List[str], str] = Field(
        default=None,
        description="Used in conjunction with eventStatus for rescheduled or cancelled events. This property"
     "contains the previously scheduled start date. For rescheduled events, the startDate"
     "property should be used for the newly scheduled start date. In the (rare) case of an event"
     "that has been postponed and rescheduled multiple times, this field may be repeated.",union_mode="smart"
    )
    
    recordedIn: Union[List[str], str] = Field(
        default=None,
        description="The CreativeWork that captured all or part of this Event.",union_mode="smart"
    )
    
    performer: Union[List[str], str] = Field(
        default=None,
        description="A performer at the event&#x2014;for example, a presenter, musician, musical group"
     "or actor.",union_mode="smart"
    )
    
    endDate: Union[List[str], str] = Field(
        default=None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",union_mode="smart"
    )
    
    translator: Union[List[str], str] = Field(
        default=None,
        description="Organization or person who adapts a creative work to different languages, regional"
     "differences and technical requirements of a target market, or that translates during"
     "some event.",union_mode="smart"
    )
    
    contributor: Union[List[str], str] = Field(
        default=None,
        description="A secondary contributor to the CreativeWork or Event.",union_mode="smart"
    )
    
    remainingAttendeeCapacity: Union[List[str], str] = Field(
        default=None,
        description="The number of attendee places for an event that remain unallocated.",union_mode="smart"
    )
    
    workFeatured: Union[List[str], str] = Field(
        default=None,
        description="A work featured in some event, e.g. exhibited in an ExhibitionEvent. Specific subproperties"
     "are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent).",union_mode="smart"
    )
    
    workPerformed: Union[List[str], str] = Field(
        default=None,
        description="A work performed in some event, for example a play performed in a TheaterEvent.",union_mode="smart"
    )
    
    organizer: Union[List[str], str] = Field(
        default=None,
        description="An organizer of an Event.",union_mode="smart"
    )
    
    eventStatus: Union[List[str], str] = Field(
        default=None,
        description="An eventStatus of an event represents its status; particularly useful when an event"
     "is cancelled or rescheduled.",union_mode="smart"
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
    from pydantic_schemaorg import Text, URL, AnyUrl, Person, SportsTeam
    from pydantic_schemaorg import Language, EventAttendanceModeEnumeration, Organization, Grant, datetime, Audience, DateTime, Demand, Thing, Time, Offer, Person, Date, URL, time, Integer, DefinedTerm, Place, Duration, PostalAddress, date, Event, Boolean, Review, int, EventStatusType, Text, StrictBool, Schedule, VirtualLocation, AggregateRating, CreativeWork, AnyUrl
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
