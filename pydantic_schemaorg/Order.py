from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class Order(SchemaOrgBase):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line"
     "items, each represented by an Offer that has been accepted by the customer.

    See: https://schema.org/Order
    Model depth: 3
    """
    type_: str = Field(default="Order", alias='@type')
    
    discountCurrency: Union[List[str], str] = Field(
        default=None,
        description="The currency of the discount. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",union_mode="smart"
    )
    
    orderDelivery: Union[List[str], str] = Field(
        default=None,
        description="The delivery of the parcel related to this order or order item.",union_mode="smart"
    )
    
    orderNumber: Union[List[str], str] = Field(
        default=None,
        description="The identifier of the transaction.",union_mode="smart"
    )
    
    confirmationNumber: Union[List[str], str] = Field(
        default=None,
        description="A number that confirms the given order or payment has been received.",union_mode="smart"
    )
    
    paymentUrl: Union[List[str], str] = Field(
        default=None,
        description="The URL for sending a payment.",union_mode="smart"
    )
    
    paymentDueDate: Union[List[str], str] = Field(
        default=None,
        description="The date that payment is due.",union_mode="smart"
    )
    
    orderDate: Union[List[str], str] = Field(
        default=None,
        description="Date order was placed.",union_mode="smart"
    )
    
    seller: Union[List[str], str] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",union_mode="smart"
    )
    
    acceptedOffer: Union[List[str], str] = Field(
        default=None,
        description="The offer(s) -- e.g., product, quantity and price combinations -- included in the order.",union_mode="smart"
    )
    
    paymentDue: Union[List[str], str] = Field(
        default=None,
        description="The date that payment is due.",union_mode="smart"
    )
    
    discount: Union[List[str], str] = Field(
        default=None,
        description="Any discount applied (to an Order).",union_mode="smart"
    )
    
    paymentMethodId: Union[List[str], str] = Field(
        default=None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",union_mode="smart"
    )
    
    orderedItem: Union[List[str], str] = Field(
        default=None,
        description="The item ordered.",union_mode="smart"
    )
    
    paymentMethod: Union[List[str], str] = Field(
        default=None,
        description="The name of the credit card or other method of payment for the order.",union_mode="smart"
    )
    
    billingAddress: Union[List[str], str] = Field(
        default=None,
        description="The billing address for the order.",union_mode="smart"
    )
    
    broker: Union[List[str], str] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",union_mode="smart"
    )
    
    customer: Union[List[str], str] = Field(
        default=None,
        description="Party placing the order or paying the invoice.",union_mode="smart"
    )
    
    isGift: Union[List[str], str] = Field(
        default=None,
        description="Indicates whether the offer was accepted as a gift for someone other than the buyer.",union_mode="smart"
    )
    
    orderStatus: Union[List[str], str] = Field(
        default=None,
        description="The current status of the order.",union_mode="smart"
    )
    
    partOfInvoice: Union[List[str], str] = Field(
        default=None,
        description="The order is being paid as part of the referenced Invoice.",union_mode="smart"
    )
    
    discountCode: Union[List[str], str] = Field(
        default=None,
        description="Code used to redeem a discount.",union_mode="smart"
    )
    
    merchant: Union[List[str], str] = Field(
        default=None,
        description="'merchant' is an out-dated term for 'seller'.",union_mode="smart"
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
    from pydantic_schemaorg import OrderItem, Organization, Product, datetime, DateTime, Offer, Date, Service, Person, URL, ParcelDelivery, StrictInt, StrictFloat, PostalAddress, date, Boolean, OrderStatus, Invoice, Text, StrictBool, PaymentMethod, AnyUrl, Number
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
