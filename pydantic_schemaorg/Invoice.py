from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class Invoice(SchemaOrgBase):
    """A statement of the money due for goods or services; a bill.

    See: https://schema.org/Invoice
    Model depth: 3
    """
    type_: str = Field(default="Invoice", alias='@type')
    
    accountId: Union[List[str], str] = Field(
        default=None,
        description="The identifier for the account the payment will be applied to.",union_mode="smart"
    )
    
    confirmationNumber: Union[List[str], str] = Field(
        default=None,
        description="A number that confirms the given order or payment has been received.",union_mode="smart"
    )
    
    category: Union[List[str], str] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",union_mode="smart"
    )
    
    paymentDueDate: Union[List[str], str] = Field(
        default=None,
        description="The date that payment is due.",union_mode="smart"
    )
    
    billingPeriod: Union[List[str], str] = Field(
        default=None,
        description="The time interval used to compute the invoice.",union_mode="smart"
    )
    
    paymentDue: Union[List[str], str] = Field(
        default=None,
        description="The date that payment is due.",union_mode="smart"
    )
    
    provider: Union[List[str], str] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",union_mode="smart"
    )
    
    paymentMethodId: Union[List[str], str] = Field(
        default=None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",union_mode="smart"
    )
    
    minimumPaymentDue: Union[List[str], str] = Field(
        default=None,
        description="The minimum payment required at this time.",union_mode="smart"
    )
    
    referencesOrder: Union[List[str], str] = Field(
        default=None,
        description="The Order(s) related to this Invoice. One or more Orders may be combined into a single"
     "Invoice.",union_mode="smart"
    )
    
    paymentStatus: Union[List[str], str] = Field(
        default=None,
        description="The status of payment; whether the invoice has been paid or not.",union_mode="smart"
    )
    
    paymentMethod: Union[List[str], str] = Field(
        default=None,
        description="The name of the credit card or other method of payment for the order.",union_mode="smart"
    )
    
    broker: Union[List[str], str] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",union_mode="smart"
    )
    
    scheduledPaymentDate: Union[List[str], str] = Field(
        default=None,
        description="The date the invoice is scheduled to be paid.",union_mode="smart"
    )
    
    customer: Union[List[str], str] = Field(
        default=None,
        description="Party placing the order or paying the invoice.",union_mode="smart"
    )
    
    totalPaymentDue: Union[List[str], str] = Field(
        default=None,
        description="The total amount due.",union_mode="smart"
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
    from pydantic_schemaorg import Organization, datetime, DateTime, PriceSpecification, PaymentStatusType, Thing, PhysicalActivityCategory, Date, Person, Order, URL, CategoryCode, Duration, date, MonetaryAmount, Text, PaymentMethod, AnyUrl
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
