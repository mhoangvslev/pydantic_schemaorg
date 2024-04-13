from __future__ import annotations

from datetime import date
from datetime import datetime
from datetime import time
from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from pydantic.v1 import Field
from pydantic.v1 import StrictBool

from pydantic2_schemaorg.Thing import Thing


class Event(Thing):
    """An event happening at a certain time and location, such as a concert, lecture, or festival."
     "Ticketing information may be added via the [[offers]] property. Repeated events may"
     "be structured as separate Event objects.

    See: https://schema.org/Event
    Model depth: 2
    """

    type_: str = Field(default="Event", alias="@type", const=True)
    superEvent: list[Event | str] | Event | str | None = Field(
        default=None,
        description="An event that this event is a part of. For example, a collection of individual music performances"
        "might each have a music festival as their superEvent.",
    )
    performers: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="The main performer or performers of the event&#x2014;for example, a presenter, musician,"
        "or actor.",
    )
    funding: list[Grant | str] | Grant | str | None = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
        "See also [[ownershipFundingInfo]].",
    )
    isAccessibleForFree: None | (
        list[StrictBool | Boolean | str] | StrictBool | Boolean | str
    ) = Field(
        default=None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    about: list[Thing | str] | Thing | str | None = Field(
        default=None,
        description="The subject matter of the content.",
    )
    director: list[Person | str] | Person | str | None = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors"
        "can be associated with individual items or with a series, episode, clip.",
    )
    sponsor: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
        "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    doorTime: None | (
        list[datetime | DateTime | time | Time | str]
        | datetime
        | DateTime
        | time
        | Time
        | str
    ) = Field(
        default=None,
        description="The time admission will commence.",
    )
    inLanguage: None | (list[str | Text | Language] | str | Text | Language) = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language"
        "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
        "[[availableLanguage]].",
    )
    offers: None | (list[Offer | Demand | str] | Offer | Demand | str) = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
        "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
        "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
        "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
        "of common types, it can be used in others. In that case, using a second type, such as Product"
        "or a subtype of Product, can clarify the nature of the offer.",
    )
    maximumAttendeeCapacity: None | (
        list[int | Integer | str] | int | Integer | str
    ) = Field(
        default=None,
        description="The total number of individuals that may attend an event or venue.",
    )
    audience: list[Audience | str] | Audience | str | None = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    eventSchedule: None | (list[Schedule | str] | Schedule | str) = Field(
        default=None,
        description="Associates an [[Event]] with a [[Schedule]]. There are circumstances where it is preferable"
        "to share a schedule for a series of repeating events rather than data on the individual"
        "events themselves. For example, a website or application might prefer to publish a schedule"
        "for a weekly gym class rather than provide data on every event. A schedule could be processed"
        "by applications to add forthcoming events to a calendar. An [[Event]] that is associated"
        "with a [[Schedule]] using this property should not have [[startDate]] or [[endDate]]"
        "properties. These are instead defined within the associated [[Schedule]], this avoids"
        "any ambiguity for clients using the data. The property might have repeated values to"
        "specify different schedules, e.g. for different months or seasons.",
    )
    subEvent: list[Event | str] | Event | str | None = Field(
        default=None,
        description="An Event that is part of this event. For example, a conference event includes many presentations,"
        "each of which is a subEvent of the conference.",
    )
    attendees: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="A person attending the event.",
    )
    actor: list[Person | str] | Person | str | None = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated"
        "with individual items or with a series, episode, clip.",
    )
    typicalAgeRange: list[str | Text] | str | Text | None = Field(
        default=None,
        description="The typical expected age range, e.g. '7-9', '11-'.",
    )
    aggregateRating: None | (
        list[AggregateRating | str] | AggregateRating | str
    ) = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    duration: list[Duration | str] | Duration | str | None = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    maximumPhysicalAttendeeCapacity: None | (
        list[int | Integer | str] | int | Integer | str
    ) = Field(
        default=None,
        description="The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]]"
        "is [[OfflineEventAttendanceMode]] (or the offline aspects, in the case of a [[MixedEventAttendanceMode]]).",
    )
    funder: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
        "contribution.",
    )
    eventAttendanceMode: None | (
        list[EventAttendanceModeEnumeration | str]
        | EventAttendanceModeEnumeration
        | str
    ) = Field(
        default=None,
        description="The eventAttendanceMode of an event indicates whether it occurs online, offline, or"
        "a mix.",
    )
    subEvents: list[Event | str] | Event | str | None = Field(
        default=None,
        description="Events that are a part of this event. For example, a conference event includes many presentations,"
        "each subEvents of the conference.",
    )
    maximumVirtualAttendeeCapacity: None | (
        list[int | Integer | str] | int | Integer | str
    ) = Field(
        default=None,
        description="The maximum virtual attendee capacity of an [[Event]] whose [[eventAttendanceMode]]"
        "is [[OnlineEventAttendanceMode]] (or the online aspects, in the case of a [[MixedEventAttendanceMode]]).",
    )
    attendee: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="A person or organization attending the event.",
    )
    startDate: None | (
        list[datetime | DateTime | date | Date | str]
        | datetime
        | DateTime
        | date
        | Date
        | str
    ) = Field(
        default=None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    keywords: None | (
        list[AnyUrl | URL | str | Text | DefinedTerm]
        | AnyUrl
        | URL
        | str
        | Text
        | DefinedTerm
    ) = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
        "are typically delimited by commas, or by repeating the property.",
    )
    location: None | (
        list[str | Text | VirtualLocation | PostalAddress | Place]
        | str
        | Text
        | VirtualLocation
        | PostalAddress
        | Place
    ) = Field(
        default=None,
        description="The location of, for example, where an event is happening, where an organization is located,"
        "or where an action takes place.",
    )
    review: list[Review | str] | Review | str | None = Field(
        default=None,
        description="A review of the item.",
    )
    composer: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="The person or organization who wrote a composition, or who is the composer of a work performed"
        "at some event.",
    )
    previousStartDate: None | (list[date | Date | str] | date | Date | str) = Field(
        default=None,
        description="Used in conjunction with eventStatus for rescheduled or cancelled events. This property"
        "contains the previously scheduled start date. For rescheduled events, the startDate"
        "property should be used for the newly scheduled start date. In the (rare) case of an event"
        "that has been postponed and rescheduled multiple times, this field may be repeated.",
    )
    recordedIn: None | (list[CreativeWork | str] | CreativeWork | str) = Field(
        default=None,
        description="The CreativeWork that captured all or part of this Event.",
    )
    performer: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="A performer at the event&#x2014;for example, a presenter, musician, musical group"
        "or actor.",
    )
    endDate: None | (
        list[datetime | DateTime | date | Date | str]
        | datetime
        | DateTime
        | date
        | Date
        | str
    ) = Field(
        default=None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    translator: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="Organization or person who adapts a creative work to different languages, regional"
        "differences and technical requirements of a target market, or that translates during"
        "some event.",
    )
    contributor: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="A secondary contributor to the CreativeWork or Event.",
    )
    remainingAttendeeCapacity: None | (
        list[int | Integer | str] | int | Integer | str
    ) = Field(
        default=None,
        description="The number of attendee places for an event that remain unallocated.",
    )
    workFeatured: None | (list[CreativeWork | str] | CreativeWork | str) = Field(
        default=None,
        description="A work featured in some event, e.g. exhibited in an ExhibitionEvent. Specific subproperties"
        "are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent).",
    )
    workPerformed: None | (list[CreativeWork | str] | CreativeWork | str) = Field(
        default=None,
        description="A work performed in some event, for example a play performed in a TheaterEvent.",
    )
    organizer: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="An organizer of an Event.",
    )
    eventStatus: None | (list[EventStatusType | str] | EventStatusType | str) = Field(
        default=None,
        description="An eventStatus of an event represents its status; particularly useful when an event"
        "is cancelled or rescheduled.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Grant import Grant
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.Thing import Thing
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Time import Time
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Language import Language
    from pydantic2_schemaorg.Offer import Offer
    from pydantic2_schemaorg.Demand import Demand
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.Audience import Audience
    from pydantic2_schemaorg.Schedule import Schedule
    from pydantic2_schemaorg.AggregateRating import AggregateRating
    from pydantic2_schemaorg.Duration import Duration
    from pydantic2_schemaorg.EventAttendanceModeEnumeration import (
        EventAttendanceModeEnumeration,
    )
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.DefinedTerm import DefinedTerm
    from pydantic2_schemaorg.VirtualLocation import VirtualLocation
    from pydantic2_schemaorg.PostalAddress import PostalAddress
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.Review import Review
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.EventStatusType import EventStatusType
