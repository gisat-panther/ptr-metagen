import pytest

from metagen.utils import prepare_data_for_leaf
from metagen.metadata import View, Application
from test.fixtures import VIEW, TAG_1, LAYER_TEMPLATE_1
from metagen.metadata import LayerTemplate, Tag

# def test_exlude_stac_attribute_from_leaf():
#     app = Application(name='test', nameInternal='test')
#     dict = app.dict()
#     assert pass