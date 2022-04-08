import pytest
import json

from metagen.base import prepare_data_for_leaf, Generator
from metagen.elements import View


def open_json(path: str):
    with open(path, 'r', encoding='utf8') as file:
        return json.load(file)


def test_element_view_model():
    view_obj = prepare_data_for_leaf(open_json('view_element_example.json'))
    assert View.__wrapped__.parse_obj(view_obj)


