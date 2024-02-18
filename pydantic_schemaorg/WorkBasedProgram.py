from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class WorkBasedProgram(SchemaOrgBase):
    """A program with both an educational and employment component. Typically based at a workplace"
     "and structured around work-based learning, with the aim of instilling competencies"
     "related to an occupation. WorkBasedProgram is used to distinguish programs such as"
     "apprenticeships from school, college or other classroom based educational programs.

    See: https://schema.org/WorkBasedProgram
    Model depth: 4
    """
    type_: str = Field(default="WorkBasedProgram", alias='@type')
    
    occupationalCategory: Union[List[str], str] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",union_mode="smart"
    )
    
    trainingSalary: Union[List[str], str] = Field(
        default=None,
        description="The estimated salary earned while in the program.",union_mode="smart"
    )
    
    timeToComplete: Union[List[str], str] = Field(
        default=None,
        description="The expected length of time to complete the program if attending full-time.",union_mode="smart"
    )
    
    termsPerYear: Union[List[str], str] = Field(
        default=None,
        description="The number of times terms of study are offered per year. Semesters and quarters are common"
     "units for term. For example, if the student can only take 2 semesters for the program in"
     "one year, then termsPerYear should be 2.",union_mode="smart"
    )
    
    programType: Union[List[str], str] = Field(
        default=None,
        description="The type of educational or occupational program. For example, classroom, internship,"
     "alternance, etc.",union_mode="smart"
    )
    
    typicalCreditsPerTerm: Union[List[str], str] = Field(
        default=None,
        description="The number of credits or units a full-time student would be expected to take in 1 term however"
     "'term' is defined by the institution.",union_mode="smart"
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
    
    dayOfWeek: Union[List[str], str] = Field(
        default=None,
        description="The day of the week for which these opening hours are valid.",union_mode="smart"
    )
    
    timeOfDay: Union[List[str], str] = Field(
        default=None,
        description="The time of day the program normally runs. For example, \"evenings\".",union_mode="smart"
    )
    
    hasCourse: Union[List[str], str] = Field(
        default=None,
        description="A course or class that is one of the learning opportunities that constitute an educational"
     "/ occupational program. No information is implied about whether the course is mandatory"
     "or optional; no guarantee is implied about whether the course will be available to everyone"
     "on the program.",union_mode="smart"
    )
    
    programPrerequisites: Union[List[str], str] = Field(
        default=None,
        description="Prerequisites for enrolling in the program.",union_mode="smart"
    )
    
    educationalCredentialAwarded: Union[List[str], str] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other educational"
     "credential awarded as a consequence of successful completion of this course or program.",union_mode="smart"
    )
    
    provider: Union[List[str], str] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",union_mode="smart"
    )
    
    numberOfCredits: Union[List[str], str] = Field(
        default=None,
        description="The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.",union_mode="smart"
    )
    
    termDuration: Union[List[str], str] = Field(
        default=None,
        description="The amount of time in a term as defined by the institution. A term is a length of time where"
     "students take one or more classes. Semesters and quarters are common units for term.",union_mode="smart"
    )
    
    startDate: Union[List[str], str] = Field(
        default=None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",union_mode="smart"
    )
    
    salaryUponCompletion: Union[List[str], str] = Field(
        default=None,
        description="The expected salary upon completing the training.",union_mode="smart"
    )
    
    maximumEnrollment: Union[List[str], str] = Field(
        default=None,
        description="The maximum number of students who may be enrolled in the program.",union_mode="smart"
    )
    
    applicationDeadline: Union[List[str], str] = Field(
        default=None,
        description="The date at which the program stops collecting applications for the next enrollment"
     "cycle.",union_mode="smart"
    )
    
    applicationStartDate: Union[List[str], str] = Field(
        default=None,
        description="The date at which the program begins collecting applications for the next enrollment"
     "cycle.",union_mode="smart"
    )
    
    occupationalCredentialAwarded: Union[List[str], str] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other occupational"
     "credential awarded as a consequence of successful completion of this course or program.",union_mode="smart"
    )
    
    endDate: Union[List[str], str] = Field(
        default=None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",union_mode="smart"
    )
    
    educationalProgramMode: Union[List[str], str] = Field(
        default=None,
        description="Similar to courseMode, the medium or means of delivery of the program as a whole. The value"
     "may either be a text label (e.g. \"online\", \"onsite\" or \"blended\"; \"synchronous\""
     "or \"asynchronous\"; \"full-time\" or \"part-time\") or a URL reference to a term from"
     "a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous"
     ").",union_mode="smart"
    )
    
    financialAidEligible: Union[List[str], str] = Field(
        default=None,
        description="A financial aid type or program which students may use to pay for tuition or fees associated"
     "with the program.",union_mode="smart"
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
    from pydantic_schemaorg import Text, MonetaryAmountDistribution, CategoryCode
    from pydantic_schemaorg import Organization, datetime, DateTime, Demand, Offer, Date, Person, MonetaryAmountDistribution, URL, CategoryCode, Integer, DefinedTerm, StructuredValue, Duration, Number, StrictInt, StrictFloat, date, DayOfWeek, int, Text, EducationalOccupationalCredential, AlignmentObject, AnyUrl, Course
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
