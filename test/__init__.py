
# if __name__ == '__main__':
#     from pathlib import Path
#     import json
#     from datetime import datetime
#     fld = Path('C:\michal\gisat\projects\WorldWater\portal\\new data')
#     imgs_fld = fld / 'data'
#
#     gen = Generator()
#
#     appkey = 'esaWorldWater'
#     app = Application(name=appkey, nameInternal=appkey)
#
#     places_names = ['colombia', 'gabon', 'greenland', 'mexico', 'zambia']
#
#     for place_name in places_names:
#         Place(applicationKey=app, nameInternal=f'place_{place_name}', nameDisplay=place_name.capitalize(),
#               geometry=fld /'geometrie' / f'{place_name}.geojson')
#
#     Period(applicationKey=app, nameInternal=f'period_2019_2020', nameDisplay='2019-2020', start='2019', end='2020')
#     Period(applicationKey=app, nameInternal=f'period_2019', nameDisplay='2019', period='2019')
#     Period(applicationKey=app, nameInternal=f'period_2020', nameDisplay='2020', period='2020')
#
#     for month in range(1, 13):
#         for year in [2019, 2020]:
#             date = datetime(year=year, month=month, day=1).strftime("%Y-%m")
#
#
#             Period(applicationKey=app, nameInternal=f'period_{date}', nameDisplay=f'{str(month)}',
#                    period=f'{date}')
#
#     layer_names = [
#         'water_frequency',
#         'maximum_extent',
#         'minimum_extent',
#         'water_classification',
#         'water_seasonality',
#         'water_presence',
#         'change_water_frequency',
#         'change_maximum_extent',
#         'change_minimum_extent',
#         'change_water_classification',
#         'change_water_presence',
#         'water_level']
#
#     for layer_name in layer_names:
#         LayerTemplate(applicationKey=app, nameInternal=f'layertemplate_{layer_name}',
#                       nameDisplay=' '.join(layer_name.split('_')))
#
#     attributes_names = [('Water level', 'wl', 'numeric'), ('Water level standard deviation', 'wlsd', 'numeric'),
#                         ('data', 'data', 'bool')]
#
#     for display, name, typ in attributes_names:
#         Attribute(applicationKey=app, nameInternal=f'attribute_{name}', nameDisplay=display, type=typ, unit='m')
#
#
#     # datasources
#     url = 'https://ptr.gisat.cz/mapserver/?map=/srv/msmaps/'
#     for item in imgs_fld.iterdir():
#         if item.suffix == '.tif':
#             name = item.name.removesuffix('.tif')
#             wms = SpatialWMS(nameInternal=f'spatialwms_{name}', url=f'{url}{name}.map', layers=name,
#                        configuration={"source": f"layerstorage/{name}.tif"})
#
#             if name.__contains__('water_frequency') and name.__contains__('-'):
#                 place, year, _, _ = name.split('_')
#                 period1, period2 = year.split('-')
#                 RelationSpatial(nameInternal=f'relationspatial_{name}',
#                                 periodKey=gen.get_element_by_nameInternal(f'period_{period2}'),
#                                 placeKey=gen.get_element_by_nameInternal(f'place_{place.lower()}'),
#                                 spatialDataSourceKey=wms,
#                                 layerTemplateKey=gen.get_element_by_nameInternal(f'layertemplate_change_water_frequency'),
#                                 applicationKey=app)
#             elif not name.__contains__('change'):
#                 place, year, first, second = name.split('_')
#                 try:
#                     date = datetime.strptime(year, "%Y%m").strftime("%Y-%m")
#                 except ValueError:
#                     date = datetime.strptime(year, "%Y").strftime("%Y")
#
#                 RelationSpatial(nameInternal=f'relationspatial_{name}',
#                                 periodKey=gen.get_element_by_nameInternal(f'period_{date}'),
#                                 placeKey=gen.get_element_by_nameInternal(f'place_{place.lower()}'),
#                                 spatialDataSourceKey=wms,
#                                 layerTemplateKey=gen.get_element_by_nameInternal(f'layertemplate_{first}_{second}'),
#                                 applicationKey=app)
#             elif name.__contains__('change'):
#                 place, year, change, first, second = name.split('_')
#                 period1, period2 = year.split('-')
#                 if name.__contains__('change_water_presence'):
#                     date = datetime.strptime(period2, "%Y%m").strftime("%Y-%m")
#                     RelationSpatial(nameInternal=f'relationspatial_{name}',
#                                     periodKey=gen.get_element_by_nameInternal(f'period_{date}'),
#                                     placeKey=gen.get_element_by_nameInternal(f'place_{place.lower()}'),
#                                     spatialDataSourceKey=wms,
#                                     layerTemplateKey=gen.get_element_by_nameInternal(f'layertemplate_change_water_presence'),
#                                     applicationKey=app)
#                 else:
#                     RelationSpatial(nameInternal=f'relationspatial_{name}',
#                                     periodKey=gen.get_element_by_nameInternal(f'period_{period2}'),
#                                     placeKey=gen.get_element_by_nameInternal(f'place_{place.lower()}'),
#                                     spatialDataSourceKey=wms,
#                                     layerTemplateKey=gen.get_element_by_nameInternal(f'layertemplate_{change}_{first}_{second}'),
#                                     applicationKey=app)
#
#
#
#         #altimetric
#     alt_fld = Path('C:\michal\gisat\projects\WorldWater\microapp\data\\review\\altimetric\martin')
#     water_level_layerTemplate = gen.get_element_by_nameInternal(f'layertemplate_water_level')
#
#     i = 1
#     for folder in alt_fld.iterdir():
#         if folder.is_dir() and (place_name := folder.name.split('_')[2]) != 'denmark':
#             place = gen.get_element_by_nameInternal(f'place_{place_name}')
#             spatia_attr = SpatialAttribute(nameInternal=f'spatialattribute_{folder.name.replace("pt1", "data")}',
#                                            tableName=folder.name, columnName='data', fidColumnName='fid')
#             atribute_relation = RelationAttribute(nameInternal=f'relationattribute_{place_name}_water_level_',
#                                                   placeKey=place,
#                                                   layerTemplateKey=water_level_layerTemplate ,
#                                                   applicationKey=app,
#                                                   attributeDataSourceKey=spatia_attr,
#                                                   attributeKey=gen.get_element_by_nameInternal(f'attribute_data'))
#
#             spatial_vector = SpatialVector(nameInternal=f'spatialvector_{place_name}_ts',
#                                            tableName=f'ww_ts_{place_name}_pt1',
#                                            fidColumnName='fid',
#                                            geometryColumnName='geom')
#
#             spatial_rel = RelationSpatial(nameInternal=f'spatialrelation_{place_name}_water_level',
#                                           spatialDataSourceKey=spatial_vector,
#                                           layerTemplateKey=water_level_layerTemplate ,
#                                           applicationKey=app,
#                                           placeKey=place)
#
#             for data_file in folder.iterdir():
#                 with open(data_file, 'r') as file:
#                     data = json.load(file)
#                     print(data_file.name)
#                     for k, v in data[0].items():
#                         if k != 'fid':
#                             saptial_attribute = SpatialAttribute(nameInternal=f'spatialattribute{k}',
#                                                                  tableName=data_file.name.removesuffix('.json'),
#                                                                  columnName=k,
#                                                                  fidColumnName='fid')
#
#                             i += 1
#                             print(i)
#                             date = datetime.strptime(k[:6], '%y%m%d')
#                             period = Period(applicationKey=app,
#                                             nameInternal=f'period_{date.strftime("%Y_%m_%d")}',
#                                             nameDisplay=date.strftime('%Y-%m-%d'),
#                                             period=date.strftime('%Y-%m-%d'))
#
#                             if k.endswith('wl'):
#                                 atribute_relation = RelationAttribute(
#                                     nameInternal=f'attributerelation_{place_name}_{date.strftime("%Y_%m_%d")}_'
#                                                  f'water_level',
#                                     periodKey=period,
#                                     placeKey=place,
#                                     layerTemplateKey=water_level_layerTemplate,
#                                     applicationKey=app,
#                                     attributeDataSourceKey=saptial_attribute,
#                                     attributeKey=gen.get_element_by_nameInternal(f'attribute_wl'))
#
#
#                             elif k.endswith('wlsd'):
#                                 atribute_relation = RelationAttribute(
#                                     nameInternal=f'attributerelation_{place_name}_{date.strftime("%Y_%m_%d")}_'
#                                                  f'water_level',
#                                     periodKey=period,
#                                     placeKey=place,
#                                     layerTemplateKey=water_level_layerTemplate,
#                                     applicationKey=app,
#                                     attributeDataSourceKey=saptial_attribute,
#                                     attributeKey=gen.get_element_by_nameInternal(f'attribute_wlsd'))
#
#
#
#
#
