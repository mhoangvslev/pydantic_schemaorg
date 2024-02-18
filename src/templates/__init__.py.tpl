# __all__= ['SchemaOrgBase','{{all_classes | map(attribute='valid_name')|join('\', \'')}}']
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
{%- for schemaorg_type in all_classes | map(attribute='valid_name') %}
from pydantic_schemaorg.{{schemaorg_type}} import {{schemaorg_type}}
{%- endfor %}
