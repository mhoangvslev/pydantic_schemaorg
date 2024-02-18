from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class BankAccount(SchemaOrgBase):
    """A product or service offered by a bank whereby one may deposit, withdraw or transfer money"
     "and in some cases be paid interest.

    See: https://schema.org/BankAccount
    Model depth: 5
    """
    type_: str = Field(default="BankAccount", alias='@type')
    
    accountMinimumInflow: Union[List[str], str] = Field(
        default=None,
        description="A minimum amount that has to be paid in every month.",union_mode="smart"
    )
    
    bankAccountType: Union[List[str], str] = Field(
        default=None,
        description="The type of a bank account.",union_mode="smart"
    )
    
    accountOverdraftLimit: Union[List[str], str] = Field(
        default=None,
        description="An overdraft is an extension of credit from a lending institution when an account reaches"
     "zero. An overdraft allows the individual to continue withdrawing money even if the account"
     "has no funds in it. Basically the bank allows people to borrow a set amount of money.",union_mode="smart"
    )
    
    annualPercentageRate: Union[List[str], str] = Field(
        default=None,
        description="The annual rate that is charged for borrowing (or made by investing), expressed as a single"
     "percentage number that represents the actual yearly cost of funds over the term of a loan."
     "This includes any fees or additional costs associated with the transaction.",union_mode="smart"
    )
    
    feesAndCommissionsSpecification: Union[List[str], str] = Field(
        default=None,
        description="Description of fees, commissions, and other terms applied either to a class of financial"
     "product, or by a financial service organization.",union_mode="smart"
    )
    
    interestRate: Union[List[str], str] = Field(
        default=None,
        description="The interest rate, charged or paid, applicable to the financial product. Note: This"
     "is different from the calculated annualPercentageRate.",union_mode="smart"
    )
    
    produces: Union[List[str], str] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",union_mode="smart"
    )
    
    category: Union[List[str], str] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",union_mode="smart"
    )
    
    hasOfferCatalog: Union[List[str], str] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",union_mode="smart"
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
    
    audience: Union[List[str], str] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",union_mode="smart"
    )
    
    serviceOutput: Union[List[str], str] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",union_mode="smart"
    )
    
    provider: Union[List[str], str] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",union_mode="smart"
    )
    
    brand: Union[List[str], str] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",union_mode="smart"
    )
    
    isRelatedTo: Union[List[str], str] = Field(
        default=None,
        description="A pointer to another, somehow related product (or multiple products).",union_mode="smart"
    )
    
    aggregateRating: Union[List[str], str] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",union_mode="smart"
    )
    
    serviceArea: Union[List[str], str] = Field(
        default=None,
        description="The geographic area where the service is provided.",union_mode="smart"
    )
    
    serviceType: Union[List[str], str] = Field(
        default=None,
        description="The type of service being offered, e.g. veterans' benefits, emergency relief, etc.",union_mode="smart"
    )
    
    providerMobility: Union[List[str], str] = Field(
        default=None,
        description="Indicates the mobility of a provided service (e.g. 'static', 'dynamic').",union_mode="smart"
    )
    
    review: Union[List[str], str] = Field(
        default=None,
        description="A review of the item.",union_mode="smart"
    )
    
    broker: Union[List[str], str] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",union_mode="smart"
    )
    
    termsOfService: Union[List[str], str] = Field(
        default=None,
        description="Human-readable terms of service documentation.",union_mode="smart"
    )
    
    serviceAudience: Union[List[str], str] = Field(
        default=None,
        description="The audience eligible for this service.",union_mode="smart"
    )
    
    hoursAvailable: Union[List[str], str] = Field(
        default=None,
        description="The hours during which this service or contact is available.",union_mode="smart"
    )
    
    areaServed: Union[List[str], str] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",union_mode="smart"
    )
    
    availableChannel: Union[List[str], str] = Field(
        default=None,
        description="A means of accessing the service (e.g. a phone bank, a web site, a location, etc.).",union_mode="smart"
    )
    
    award: Union[List[str], str] = Field(
        default=None,
        description="An award won by or for this item.",union_mode="smart"
    )
    
    slogan: Union[List[str], str] = Field(
        default=None,
        description="A slogan or motto associated with the item.",union_mode="smart"
    )
    
    logo: Union[List[str], str] = Field(
        default=None,
        description="An associated logo.",union_mode="smart"
    )
    
    isSimilarTo: Union[List[str], str] = Field(
        default=None,
        description="A pointer to another, functionally similar product (or multiple products).",union_mode="smart"
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
    from pydantic_schemaorg import Text, URL, MonetaryAmount, AnyUrl
    from pydantic_schemaorg import Text, URL, AnyUrl, QuantitativeValue, Number, StrictInt, StrictFloat
    from pydantic_schemaorg import Audience, Organization, Product, GeoShape, Demand, Offer, Thing, PhysicalActivityCategory, Person, Service, URL, CategoryCode, OpeningHoursSpecification, Brand, Place, ServiceChannel, AdministrativeArea, GovernmentBenefitsType, Review, Text, OfferCatalog, AggregateRating, ImageObject, AnyUrl
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
