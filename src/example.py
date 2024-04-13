from pydantic2_schemaorg.ScholarlyArticle import ScholarlyArticle


scholarly_article = ScholarlyArticle(
    url="https://github.com/blurry-dev/pydantic2-schemaorg/pydantic2_schemaorg",
    sameAs="https://github.com/blurry-dev/pydantic2-schemaorg/pydantic2_schemaorg",
    copyrightNotice="Free to use under the MIT license",
    dateCreated="2021-11",
)
print(scholarly_article.json())
