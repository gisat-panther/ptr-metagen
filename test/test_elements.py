import pytest

from metagen.utils import prepare_data_for_leaf
from metagen.metadata import View, Application


def test_stac_attribute_in_leaf():
    app = Application(name='test', nameInternal='test')
    assert hasattr(app, '_input_pars')


def test_exlude_stac_attribute_from_leaf():
    app = Application(name='test', nameInternal='test')
    dict = app.dict()
    assert hasattr(app, '_input_pars')
    assert dict.get('__input_pars') == None