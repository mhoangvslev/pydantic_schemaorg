from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl
from datetime import date
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class Patient(SchemaOrgBase):
    """A patient is any person recipient of health care services.

    See: https://schema.org/Patient
    Model depth: 3
    """
    type_: str = Field(default="Patient", alias='@type')
    
    healthCondition: Union[List[str], str] = Field(
        default=None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",union_mode="smart"
    )
    
    drug: Union[List[str], str] = Field(
        default=None,
        description="Specifying a drug or medicine used in a medication procedure.",union_mode="smart"
    )
    
    diagnosis: Union[List[str], str] = Field(
        default=None,
        description="One or more alternative conditions considered in the differential diagnosis process"
     "as output of a diagnosis process.",union_mode="smart"
    )
    
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
    
    funding: Union[List[str], str] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",union_mode="smart"
    )
    
    memberOf: Union[List[str], str] = Field(
        default=None,
        description="An Organization (or ProgramMembership) to which this Person or Organization belongs.",union_mode="smart"
    )
    
    gender: Union[List[str], str] = Field(
        default=None,
        description="Gender of something, typically a [[Person]], but possibly also fictional characters,"
     "animals, etc. While http://schema.org/Male and http://schema.org/Female may be"
     "used, text strings are also acceptable for people who do not identify as a binary gender."
     "The [[gender]] property can also be used in an extended sense to cover e.g. the gender"
     "of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities."
     "A mixed-gender [[SportsTeam]] can be indicated with a text value of \"Mixed\".",union_mode="smart"
    )
    
    height: Union[List[str], str] = Field(
        default=None,
        description="The height of the item.",union_mode="smart"
    )
    
    deathPlace: Union[List[str], str] = Field(
        default=None,
        description="The place where the person died.",union_mode="smart"
    )
    
    makesOffer: Union[List[str], str] = Field(
        default=None,
        description="A pointer to products or services offered by the organization or person.",union_mode="smart"
    )
    
    telephone: Union[List[str], str] = Field(
        default=None,
        description="The telephone number.",union_mode="smart"
    )
    
    sponsor: Union[List[str], str] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",union_mode="smart"
    )
    
    owns: Union[List[str], str] = Field(
        default=None,
        description="Products owned by the organization or person.",union_mode="smart"
    )
    
    hasOfferCatalog: Union[List[str], str] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",union_mode="smart"
    )
    
    homeLocation: Union[List[str], str] = Field(
        default=None,
        description="A contact location for a person's residence.",union_mode="smart"
    )
    
    workLocation: Union[List[str], str] = Field(
        default=None,
        description="A contact location for a person's place of work.",union_mode="smart"
    )
    
    globalLocationNumber: Union[List[str], str] = Field(
        default=None,
        description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred"
     "to as International Location Number or ILN) of the respective organization, person,"
     "or place. The GLN is a 13-digit number used to identify parties and physical locations.",union_mode="smart"
    )
    
    naics: Union[List[str], str] = Field(
        default=None,
        description="The North American Industry Classification System (NAICS) code for a particular organization"
     "or business person.",union_mode="smart"
    )
    
    honorificSuffix: Union[List[str], str] = Field(
        default=None,
        description="An honorific suffix following a Person's name such as M.D./PhD/MSCSW.",union_mode="smart"
    )
    
    email: Union[List[str], str] = Field(
        default=None,
        description="Email address.",union_mode="smart"
    )
    
    spouse: Union[List[str], str] = Field(
        default=None,
        description="The person's spouse.",union_mode="smart"
    )
    
    weight: Union[List[str], str] = Field(
        default=None,
        description="The weight of the product or person.",union_mode="smart"
    )
    
    vatID: Union[List[str], str] = Field(
        default=None,
        description="The Value-added Tax ID of the organization or person.",union_mode="smart"
    )
    
    colleague: Union[List[str], str] = Field(
        default=None,
        description="A colleague of the person.",union_mode="smart"
    )
    
    taxID: Union[List[str], str] = Field(
        default=None,
        description="The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in"
     "Spain.",union_mode="smart"
    )
    
    familyName: Union[List[str], str] = Field(
        default=None,
        description="Family name. In the U.S., the last name of a Person.",union_mode="smart"
    )
    
    faxNumber: Union[List[str], str] = Field(
        default=None,
        description="The fax number.",union_mode="smart"
    )
    
    knowsAbout: Union[List[str], str] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that"
     "is known about - suggesting possible expertise but not implying it. We do not distinguish"
     "skill levels here, or relate this to educational content, events, objectives or [[JobPosting]]"
     "descriptions.",union_mode="smart"
    )
    
    honorificPrefix: Union[List[str], str] = Field(
        default=None,
        description="An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.",union_mode="smart"
    )
    
    birthDate: Union[List[str], str] = Field(
        default=None,
        description="Date of birth.",union_mode="smart"
    )
    
    brand: Union[List[str], str] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",union_mode="smart"
    )
    
    jobTitle: Union[List[str], str] = Field(
        default=None,
        description="The job title of the person (for example, Financial Manager).",union_mode="smart"
    )
    
    follows: Union[List[str], str] = Field(
        default=None,
        description="The most generic uni-directional social relation.",union_mode="smart"
    )
    
    interactionStatistic: Union[List[str], str] = Field(
        default=None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",union_mode="smart"
    )
    
    contactPoints: Union[List[str], str] = Field(
        default=None,
        description="A contact point for a person or organization.",union_mode="smart"
    )
    
    birthPlace: Union[List[str], str] = Field(
        default=None,
        description="The place where the person was born.",union_mode="smart"
    )
    
    awards: Union[List[str], str] = Field(
        default=None,
        description="Awards won by or for this item.",union_mode="smart"
    )
    
    funder: Union[List[str], str] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",union_mode="smart"
    )
    
    parents: Union[List[str], str] = Field(
        default=None,
        description="A parents of the person.",union_mode="smart"
    )
    
    parent: Union[List[str], str] = Field(
        default=None,
        description="A parent of this person.",union_mode="smart"
    )
    
    performerIn: Union[List[str], str] = Field(
        default=None,
        description="Event that this person is a performer or participant in.",union_mode="smart"
    )
    
    additionalName: Union[List[str], str] = Field(
        default=None,
        description="An additional name for a Person, can be used for a middle name.",union_mode="smart"
    )
    
    worksFor: Union[List[str], str] = Field(
        default=None,
        description="Organizations that the person works for.",union_mode="smart"
    )
    
    agentInteractionStatistic: Union[List[str], str] = Field(
        default=None,
        description="The number of completed interactions for this entity, in a particular role (the 'agent'),"
     "in a particular action (indicated in the statistic), and in a particular context (i.e."
     "interactionService).",union_mode="smart"
    )
    
    colleagues: Union[List[str], str] = Field(
        default=None,
        description="A colleague of the person.",union_mode="smart"
    )
    
    nationality: Union[List[str], str] = Field(
        default=None,
        description="Nationality of the person.",union_mode="smart"
    )
    
    seeks: Union[List[str], str] = Field(
        default=None,
        description="A pointer to products or services sought by the organization or person (demand).",union_mode="smart"
    )
    
    hasCredential: Union[List[str], str] = Field(
        default=None,
        description="A credential awarded to the Person or Organization.",union_mode="smart"
    )
    
    address: Union[List[str], str] = Field(
        default=None,
        description="Physical address of the item.",union_mode="smart"
    )
    
    contactPoint: Union[List[str], str] = Field(
        default=None,
        description="A contact point for a person or organization.",union_mode="smart"
    )
    
    knowsLanguage: Union[List[str], str] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a known language."
     "We do not distinguish skill levels or reading/writing/speaking/signing here. Use"
     "language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).",union_mode="smart"
    )
    
    knows: Union[List[str], str] = Field(
        default=None,
        description="The most generic bi-directional social/work relation.",union_mode="smart"
    )
    
    hasPOS: Union[List[str], str] = Field(
        default=None,
        description="Points-of-Sales operated by the organization or person.",union_mode="smart"
    )
    
    relatedTo: Union[List[str], str] = Field(
        default=None,
        description="The most generic familial relation.",union_mode="smart"
    )
    
    hasOccupation: Union[List[str], str] = Field(
        default=None,
        description="The Person's occupation. For past professions, use Role for expressing dates.",union_mode="smart"
    )
    
    alumniOf: Union[List[str], str] = Field(
        default=None,
        description="An organization that the person is an alumni of.",union_mode="smart"
    )
    
    netWorth: Union[List[str], str] = Field(
        default=None,
        description="The total financial value of the person as calculated by subtracting assets from liabilities.",union_mode="smart"
    )
    
    callSign: Union[List[str], str] = Field(
        default=None,
        description="A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting"
     "and radio communications to identify people, radio and TV stations, or vehicles.",union_mode="smart"
    )
    
    isicV4: Union[List[str], str] = Field(
        default=None,
        description="The International Standard of Industrial Classification of All Economic Activities"
     "(ISIC), Revision 4 code for a particular organization, business person, or place.",union_mode="smart"
    )
    
    affiliation: Union[List[str], str] = Field(
        default=None,
        description="An organization that this person is affiliated with. For example, a school/university,"
     "a club, or a team.",union_mode="smart"
    )
    
    deathDate: Union[List[str], str] = Field(
        default=None,
        description="Date of death.",union_mode="smart"
    )
    
    duns: Union[List[str], str] = Field(
        default=None,
        description="The Dun & Bradstreet DUNS number for identifying an organization or business person.",union_mode="smart"
    )
    
    award: Union[List[str], str] = Field(
        default=None,
        description="An award won by or for this item.",union_mode="smart"
    )
    
    publishingPrinciples: Union[List[str], str] = Field(
        default=None,
        description="The publishingPrinciples property indicates (typically via [[URL]]) a document describing"
     "the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]]"
     "writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity"
     "policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles"
     "are those of the party primarily responsible for the creation of the [[CreativeWork]]."
     "While such policies are most typically expressed in natural language, sometimes related"
     "information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.",union_mode="smart"
    )
    
    sibling: Union[List[str], str] = Field(
        default=None,
        description="A sibling of the person.",union_mode="smart"
    )
    
    children: Union[List[str], str] = Field(
        default=None,
        description="A child of the person.",union_mode="smart"
    )
    
    givenName: Union[List[str], str] = Field(
        default=None,
        description="Given name. In the U.S., the first name of a Person.",union_mode="smart"
    )
    
    siblings: Union[List[str], str] = Field(
        default=None,
        description="A sibling of the person.",union_mode="smart"
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg import Drug, MedicalCondition
    from pydantic_schemaorg import StrictInt, StrictFloat, QuantitativeValue, int, Text, GenderType, Integer, MedicalCondition, Number
    from pydantic_schemaorg import Text, AdministrativeArea
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
    from pydantic_schemaorg import Text, AdministrativeArea
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
    from pydantic_schemaorg import Language, ContactPoint, Grant, Organization, Product, Demand, PriceSpecification, Offer, Thing, Date, Person, URL, Brand, Place, ProgramMembership, DefinedTerm, PostalAddress, date, InteractionCounter, Distance, Event, MonetaryAmount, OwnershipInfo, QuantitativeValue, Country, EducationalOrganization, Text, Occupation, OfferCatalog, GenderType, EducationalOccupationalCredential, CreativeWork, AnyUrl
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
