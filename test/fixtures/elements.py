import pytest

from metagen.metadata import Application, Configuration, Scope, Place, Period, LayerTemplate, Attribute, SpatialWMS, \
    RelationSpatial, SpatialAttribute, SpatialWMTS, SpatialVector, Style, Case, RelationAttribute, Tag


@pytest.fixture(autouse=True)
def layer_template_1a():
    return LayerTemplate(applicationKey='app', nameInternal=f'lt', nameDisplay='lt')


@pytest.fixture(autouse=True)
def layer_template_1b():
    return LayerTemplate(applicationKey='app', nameInternal=f'lt', nameDisplay='lt')


@pytest.fixture(autouse=True)
def application_1a():
    return Application(name='app', nameInternal='application_name_interna', description='bla', color='bla')


@pytest.fixture(autouse=True)
def configuration_1a():
    return Configuration(applicationKey='app', nameInternal='test_configuration', data={
        "tags": {"isFilterCategory": "48457f40-ba47-49f5-8c19-a8fdf8ddf82f"},
        "configByApplicationStoryKey": {"ap01-surface-dynamics": {
                "viewKey": "4fc16bc5-ee6d-4007-aa65-f26d553de790",
                "scopeKey": "045fb1db-bf01-4b97-a7f7-a1d6c7ab7fc9"
            }
        }
    })


@pytest.fixture(autouse=True)
def scope_1a():
    return Scope(applicationKey='app', nameInternal='test_scope', nameDisplay='test_scope',
                 description='test scope',
                 tagKeys=["28aa1d23-ac24-4bf3-a605-da62ef1dfd67", "2fba3fcd-7c91-4333-b755-610d984b7f14"],
                 configuration={
                     "image": {
                         "key": "ap01",
                         "alt": "ap01_preview"
                     }})


@pytest.fixture(autouse=True)
def scope_1b():
    return Scope(applicationKey='app', nameInternal='test_scope', nameDisplay='test_scope',
                 description='test scope',
                 tagKeys=["2fba3fcd-7c91-4333-b755-610d984b7f14","28aa1d23-ac24-4bf3-a605-da62ef1dfd67"],
                 configuration={
                     "image": {
                         "key": "ap01",
                         "alt": "ap01_preview"
                     }})


@pytest.fixture(autouse=True)
def place_1a(scope_1a, application_1a):
    return Place(applicationKey=application_1a, scopeKey=scope_1a, nameInternal='test_place', nameDisplay='test_place',
                 description='test_place', geometry={"type": "Point", "coordinates": [13.4, 52.52]})


@pytest.fixture(autouse=True)
def period_1a(application_1a, scope_1a):
    return Period(applicationKey=application_1a, scopeKey=scope_1a, nameInternal='test_period', nameDisplay='test_period',
                  description='bla', start='2017', end='2018')


@pytest.fixture(autouse=True)
def attribute_1a(application_1a):
    return Attribute(applicationKey=application_1a, nameInternal='test_attribute', nameDisplay='test_attribute',
                     description='bla', type='numeric', unit='°C', valueType='test', color='black')


@pytest.fixture(autouse=True)
def spatial_wms_1a():
    return SpatialWMS(nameInternal='test_spatial_wms', url='http://foo.bar', layers='layer', configuration={},
                      params={})


@pytest.fixture(autouse=True)
def case_1a(application_1a):
    return Case(applicationKey=application_1a, nameInternal='test case', nameDisplay='test_case', description='bla')


@pytest.fixture(autouse=True)
def relation_spatial_1a(scope_1a, place_1a, period_1a, spatial_wms_1a, layer_template_1a, application_1a, case_1a):
    return RelationSpatial(nameInternal='test_rel_spatial', scopeKey=scope_1a, periodKey=period_1a, placeKey=place_1a,
                           spatialDataSourceKey=spatial_wms_1a, layerTemplateKey=layer_template_1a,
                           applicationKey=application_1a, caseKey=case_1a)


@pytest.fixture(autouse=True)
def spatial_attribute_1a():
    return SpatialAttribute(nameInternal='spatila_attribute', attribution='text',tableName='table', columnName='column')


@pytest.fixture(autouse=True)
def spatial_wmts_1a():
    return SpatialWMTS(nameInternal='test_wmts', urls=['http://foo.bar'])


@pytest.fixture(autouse=True)
def spatial_vector_1a():
    return SpatialVector(nameInternal='test_spatial_vector', layerName='layer', tableName='table')


@pytest.fixture(autouse=True)
def style_1a():
    return Style(nameInternal='test_style', nameDisplay='test style', description='test style',
                 definition={"rules": []})


@pytest.fixture(autouse=True)
def tag_1a():
    return Tag(nameInternal='test_tag', nameDisplay='test_tag', description='test tag', color='black',
               tagKeys=["48457f40-ba47-49f5-8c19-a8fdf8ddf82f"])


@pytest.fixture(autouse=True)
def relation_attribute_1a(scope_1a, period_1a, place_1a, spatial_attribute_1a, attribute_1a, application_1a,
                       layer_template_1a, case_1a):
    return RelationAttribute(nameInternal='test', scopeKey=scope_1a, periodKey=period_1a, placeKey=place_1a,
                             attributeDataSourceKey=spatial_attribute_1a, attributeKey=attribute_1a,
                             applicationKey=application_1a, layerTemplateKey=layer_template_1a,caseKey=case_1a)

