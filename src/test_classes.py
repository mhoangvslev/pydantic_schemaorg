import importlib
import inspect
import json
import os
import re
from collections.abc import Iterator
from typing import Union

import pytest
import requests
from requests import Response

dir = os.path.dirname(__file__)
dir = f"{dir}/../pydantic2_schemaorg"
files = os.listdir(f"{dir}")


def get_modules_in_package(dir_name: str, package_name: str):
    files = os.listdir(dir_name)
    for file in files:
        if file not in ["__init__.py", "__pycache__"]:
            if file[-3:] != ".py":
                continue
            file_name = file[:-3]
            module_name = package_name + "." + file_name
            for _name, cls in inspect.getmembers(
                importlib.import_module(module_name), inspect.isclass
            ):
                if cls.__module__ == module_name:
                    yield cls


def get_all_examples() -> Iterator[Union[list, dict]]:
    schema_org_request: Response = requests.get(
        "https://schema.org/version/latest/schemaorg-all-examples.txt"
    )
    content = schema_org_request.text
    matches = re.findall(
        r'<script type\="application/ld\+json">(?P<json_ld>.*?)</script>',
        content,
        flags=re.DOTALL | re.M,
    )
    for match in matches:
        m = match
        m = m.replace("\n", "")
        b = json.loads(m)
        yield b


for example in get_all_examples():
    if isinstance(example, dict) and not isinstance(example.get("@type"), list):
        type_ = example.get("@type", "").split(":")[-1]
        if not type_:
            print(f"Not a type: {type_}")
            continue
        try:
            mod = __import__(f"pydantic2_schemaorg.{type_}", fromlist=[f"{type_}"])
            class_ = getattr(mod, f"{type_}")
            model = class_.__call__(**example)
            print(f"Success for {type_}", model.json())
        except Exception as e:
            print(f"Exception for type {type_}", e)


schema_classes = get_modules_in_package(dir, "pydantic2_schemaorg")


@pytest.mark.parametrize("schema_class", schema_classes)
def test_classes(schema_class):
    schema_class._update_all_fields()
    assert schema_class.__call__() is not None
