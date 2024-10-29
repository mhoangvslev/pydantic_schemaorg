from pydantic2_schemaorg.ScholarlyArticle import ScholarlyArticle


scholarly_article = ScholarlyArticle(
    url="https://github.com/blurry-dev/pydantic2_schemaorg",
    sameAs="https://github.com/blurry-dev/pydantic2_schemaorg",
    copyrightNotice="Free to use under the MIT license",
    dateCreated="2024-10",
)
print(scholarly_article.json())
