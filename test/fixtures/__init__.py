# TODO: change fictures calling ad distribution

LAYER_TEMPLATE_1 = {
                "key": "0fed6c38-9f3e-4aed-b0c3-9ec220a0b83e",
                "data": {
                    "applicationKey": "esaUtepVisat",
                    "nameInternal": "layertemplate_WSF_2019_(100m)",
                    "nameDisplay": "WSF 2019 (100m)"
                }
            }


MAP_DEFINITION = {
        "key": "map-1",
        "data": {
            "view": {},
            "layers": []
        },
        "name": None
    }


MAP = {
    "map-1": MAP_DEFINITION
}

MAPSET_1 = {
                "key": "map-set-1",
                "data": {
                    "backgroundLayer": {
                        "key": "cartoDB_LightNoLabels",
                        "type": "wmts",
                        "options": {
                            "url": "https://{s}.basemaps.cartocdn.com/rastertiles/light_nolabels/{z}/{x}/{y}{r}.png"
                        }
                    },
                    "view": {
                        "center": {
                            "lat": 45.77,
                            "lon": 14.77
                        },
                        "boxRange": 2103667
                    },
                    "viewLimits": {

                    }
                },
                "maps": [
                    "map-1"
                ],
                "sync": {
                    "roll": True,
                    "tilt": True,
                    "range": True,
                    "center": True,
                    "heading": True,
                    "boxRange": True
                },
                "activeMapKey": "map-1"
            }

MAPSETS = {
            "map-set-1": MAPSET_1
        }

TIME_LAYER_1 = {
                    "legend": {
                        "layerTemplateKey": "0fed6c38-9f3e-4aed-b0c3-9ec220a0b83e"
                    },
                    "items": [
                        {
                            "mapZIndex": 1,
                            "periods": {
                                "filter": {
                                    "layerTemplateKey": "0fed6c38-9f3e-4aed-b0c3-9ec220a0b83e"
                                },
                                "filterByActive": {
                                    "application": True
                                }
                            },
                            "layerState": {
                                "layerTemplateKey": "0fed6c38-9f3e-4aed-b0c3-9ec220a0b83e",
                                "filterByActive": {
                                    "application": True
                                }
                            }
                        }
                    ]
                }

TIME_LAYER_2 = {
                    "legend": {
                        "layerTemplateKey": "a0c8d936-2e52-4c31-8c55-ffefb1fed8c0"
                    },
                    "items": [
                        {
                            "mapZIndex": 2,
                            "periods": {
                                "filter": {
                                    "layerTemplateKey": "a0c8d936-2e52-4c31-8c55-ffefb1fed8c0"
                                },
                                "filterByActive": {
                                    "application": True
                                }
                            },
                            "layerState": {
                                "layerTemplateKey": "a0c8d936-2e52-4c31-8c55-ffefb1fed8c0",
                                "filterByActive": {
                                    "application": True
                                }
                            }
                        }
                    ]
                }

TIME_LAYER_3 = {
                    "legend": {
                        "layerTemplateKey": "10b5b8ca-794d-40d2-961a-a8878cb9ec09"
                    },
                    "items": [
                        {
                            "mapZIndex": 3,
                            "periods": {
                                "filter": {
                                    "layerTemplateKey": "10b5b8ca-794d-40d2-961a-a8878cb9ec09"
                                },
                                "filterByActive": {
                                    "application": True
                                }
                            },
                            "layerState": {
                                "layerTemplateKey": "10b5b8ca-794d-40d2-961a-a8878cb9ec09",
                                "filterByActive": {
                                    "application": True
                                }
                            }
                        }
                    ]
                }

TIME_LAYER_4 = {
                    "legend": {
                        "layerTemplateKey": "ebc4a4df-8677-4eb0-9635-bb79c8e13d1a"
                    },
                    "items": [
                        {
                            "mapZIndex": 4,
                            "periods": {
                                "filter": {
                                    "layerTemplateKey": "ebc4a4df-8677-4eb0-9635-bb79c8e13d1a"
                                },
                                "filterByActive": {
                                    "application": True
                                }
                            },
                            "layerState": {
                                "layerTemplateKey": "ebc4a4df-8677-4eb0-9635-bb79c8e13d1a",
                                "filterByActive": {
                                    "application": True
                                }
                            }
                        }
                    ]
                }

TIME_LAYER_5 = {
                    "legend": {
                        "layerTemplateKey": "0ed19a9b-af0b-4209-ae79-f53f6d8ef350"
                    },
                    "items": [
                        {
                            "mapZIndex": 5,
                            "periods": {
                                "filter": {
                                    "layerTemplateKey": "0ed19a9b-af0b-4209-ae79-f53f6d8ef350"
                                },
                                "filterByActive": {
                                    "application": True
                                }
                            },
                            "layerState": {
                                "layerTemplateKey": "0ed19a9b-af0b-4209-ae79-f53f6d8ef350",
                                "filterByActive": {
                                    "application": True
                                }
                            }
                        }
                    ]
                }



TIMELINE = {
            "timelinePeriod": {
                "start": "2014-01-02",
                "end": "2021-01-01"
            },
            "timelineLayers": [TIME_LAYER_1, TIME_LAYER_2, TIME_LAYER_3, TIME_LAYER_4, TIME_LAYER_5]
}

MAPS = {
        "maps": MAP,
        "sets": MAPSETS,
        "activeSetKey": "map-set"
    }

STATE = {
    "maps": MAPS,
    "components": {
        "View": {
            "longDescription": "The World Settlement Footprint provides a knowledge base that can support researchers, governmental bodies and other stakeholders such as urban planners to better understand how urbanisation is taking place and, concurrently, put in place sustainable urban development strategies for well-informed policy decisions at local and national levels. This dataset presents resampled version of WSF 2019 on resulutions 100m, 250m, 500m, 1km, and 10km. Each pixel corresponding to ground percent surface covered by settlements."
        },
        "Timeline": TIMELINE
    }
}

VIEW = {
    "key": "6c581b24-de76-42bf-a606-cfed0fe1bd3a",
    "data": {
        "nameInternal": "wsf-resampled",
        "nameDisplay": "WSF 2019 Resampled",
        "description": "The World Settlement Footprint 2019 resampled on the resolution of 100m, 250m, 500m, 1km, and 10km. Each pixel corresponding to ground percent surface covered by settlements ",
        "state": STATE,
        "applicationKey": "esaUtepVisat",
        "tagKeys": [
            "478e5d14-d564-43d4-b982-978db868b1f0",
            "5ec6b453-046e-4f72-94b3-5f4146fe6224",
            "8fd34a09-bc19-4d97-9d4e-749ac2e8d735",
            "5474a30d-e5f1-4c67-bd12-6174be976893",
            "e08ded4a-9f1c-4aa2-bed7-e5620af10c33"
        ]
    }
}

TAG_1 = {
                "key":"478e5d14-d564-43d4-b982-978db868b1f0",
                "data":{
                    "nameInternal":"tag-isDataset",
                    "nameDisplay":"Dataset",
                    "tagKeys":[
                        "c26c5124-87a1-4d58-b5c8-7cd4777ffbfe"
                    ]
                }
            }