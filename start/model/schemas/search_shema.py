search = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "original_query": {
            "type": "string"
        },
        "suggestion": {
            "type": "null"
        },
        "status": {
            "type": "string"
        },
        "meta": {
            "type": "object",
            "properties": {
                "items_count": {
                    "type": "integer"
                },
                "items_limit": {
                    "type": "integer"
                },
                "items_offset": {
                    "type": "integer"
                }
            },
            "required": [
                "items_count",
                "items_limit",
                "items_offset"
            ]
        },
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "_cls": {
                        "type": "string"
                    },
                    "_id": {
                        "type": "string"
                    },
                    "uid": {
                        "type": "string"
                    },
                    "alias": {
                        "type": "string"
                    },
                    "background": {
                        "type": "object",
                        "properties": {
                            "image_1x": {
                                "type": "string"
                            },
                            "image_15x": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "image_1x",
                            "image_15x"
                        ]
                    },
                    "badges": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "alias": {
                                    "type": "string"
                                },
                                "image_1x": {
                                    "type": [
                                        "string",
                                        "null"
                                    ]
                                },
                                "text": {
                                    "type": "string"
                                },
                                "text_right": {
                                    "type": "string"
                                },
                                "text_color": {
                                    "type": "string"
                                },
                                "text_color_right": {
                                    "type": "string"
                                },
                                "background_color": {
                                    "type": "string"
                                },
                                "background_color_right": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                },
                                "size": {
                                    "type": "string"
                                },
                                "structure": {
                                    "type": "string"
                                },
                                "under_logo_position": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "id",
                                "name",
                                "alias",
                                "text",
                                "text_right",
                                "text_color",
                                "text_color_right",
                                "background_color",
                                "background_color_right",
                                "type",
                                "size",
                                "structure",
                                "under_logo_position"
                            ]
                        }
                    },
                    "banner": {
                        "type": "object",
                        "properties": {
                            "image_1x": {
                                "type": "null"
                            },
                            "image_15x": {
                                "type": "null"
                            }
                        },
                    },
                    "description": {
                        "type": "string"
                    },
                    "download_options": {
                        "type": "string"
                    },
                    "downloadable": {
                        "type": "boolean"
                    },
                    "drm_encrypted": {
                        "type": "boolean"
                    },
                    "duration": {
                        "type": "integer"
                    },
                    "enabled_for_partner": {
                        "type": "boolean"
                    },
                    "for_kids": {
                        "type": "boolean"
                    },
                    "genres": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "title",
                                "slug"
                            ]
                        }
                    },
                    "genres_string": {
                        "type": "string"
                    },
                    "horizontal": {
                        "type": "object",
                        "properties": {
                            "image_1x": {
                                "type": "string"
                            },
                            "image_15x": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "image_1x",
                            "image_15x"
                        ]
                    },
                    "hot_content": {
                        "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                        "type": "boolean"
                    },
                    "is_premier": {
                        "type": "boolean"
                    },
                    "in_subscription": {
                        "type": "boolean"
                    },
                    "is_disabled": {
                        "type": "boolean"
                    },
                    "is_free": {
                        "type": "boolean"
                    },
                    "is_preview": {
                        "type": "boolean"
                    },
                    "is_top250": {
                        "type": "boolean"
                    },
                    "is_4k": {
                        "type": "boolean"
                    },
                    "is_51": {
                        "type": "boolean"
                    },
                    "logotype": {
                        "type": "object",
                        "properties": {
                            "image_1x": {
                                "type": "string"
                            },
                            "image_15x": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "image_1x",
                            "image_15x"
                        ]
                    },
                    "meta": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "_id": {
                                    "type": "string"
                                },
                                "uid": {
                                    "type": "string"
                                },
                                "alias": {
                                    "type": "string"
                                },
                                "number": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "episodes_count": {
                                    "type": "integer"
                                },
                                "episodes_uids": {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "episodes_titles": {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "rating_age": {
                                    "type": "string"
                                },
                                "special": {
                                    "type": "boolean"
                                },
                                "play_last_season": {
                                    "type": "boolean"
                                },
                                "is_premier": {
                                    "type": "boolean"
                                },
                                "downloadable": {
                                    "type": "boolean"
                                },
                                "drm_encrypted": {
                                    "type": "boolean"
                                },
                                "enabled_for_partner": {
                                    "type": "boolean"
                                },
                                "for_kids": {
                                    "type": "boolean"
                                },
                                "hot_content": {
                                    "type": "boolean"
                                },
                                "in_subscription": {
                                    "type": "boolean"
                                },
                                "is_disabled": {
                                    "type": "boolean"
                                },
                                "is_free": {
                                    "type": "boolean"
                                },
                                "is_maxmind_proxy_enabled": {
                                    "type": "boolean"
                                },
                                "is_preview": {
                                    "type": "boolean"
                                },
                                "is_top250": {
                                    "type": "boolean"
                                },
                                "premium": {
                                    "type": "boolean"
                                },
                                "standart": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "_id",
                                "uid",
                                "alias",
                                "number",
                                "title",
                                "episodes_count",
                                "episodes_uids",
                                "episodes_titles",
                                "rating_age",
                                "special",
                                "play_last_season",
                                "is_premier",
                                "downloadable",
                                "drm_encrypted",
                                "enabled_for_partner",
                                "for_kids",
                                "hot_content",
                                "in_subscription",
                                "is_disabled",
                                "is_free",
                                "is_maxmind_proxy_enabled",
                                "is_preview",
                                "is_top250",
                                "premium",
                                "standart"
                            ]
                        }
                    },
                    "packshot": {
                        "type": "object",
                        "properties": {
                            "image_1x": {
                                "type": "string"
                            },
                            "image_15x": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "image_1x",
                            "image_15x"
                        ]
                    },
                    "play_last_season": {
                        "type": "boolean"
                    },
                    "playback_options": {
                        "type": "string"
                    },
                    "premium": {
                        "type": "boolean"
                    },
                    "quote": {
                        "type": "object",
                        "properties": {
                            "source": {
                                "type": "string"
                            },
                            "text": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "source",
                            "text"
                        ]
                    },
                    "quote_source": {
                        "type": "string"
                    },
                    "rating_age": {
                        "type": "string"
                    },
                    "release_date": {
                        "type": "integer"
                    },
                    "slug": {
                        "type": "string"
                    },
                    "special": {
                        "type": "boolean"
                    },
                    "standard": {
                        "type": "boolean"
                    },
                    "summary": {
                        "type": "string"
                    },
                    "subtitle": {
                        "type": "string"
                    },
                    "thumbnail": {
                        "type": "object",
                        "properties": {
                            "image_1x": {
                                "type": "null"
                            },
                            "image_15x": {
                                "type": [
                                    "string",
                                    "null"
                                ]
                            }
                        },
                    },
                    "title": {
                        "type": "string"
                    },
                    "title_original": {
                        "type": "string"
                    },
                    "trailer_src": {
                        "type": "string"
                    },
                    "vertical": {
                        "type": "object",
                        "properties": {
                            "image_1x": {
                                "type": "string"
                            },
                            "image_15x": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "image_1x",
                            "image_15x"
                        ]
                    },
                    "video_cover": {
                        "type": "string"
                    },
                    "web_url": {
                        "type": "string"
                    },
                    "year": {
                        "type": "integer"
                    },
                    "rating_start": {
                        "type": "number"
                    },
                    "subscriptions": {
                        "type": "array"
                    }
                },
                "required": [
                    "_cls",
                    "_id",
                    "uid",
                    "alias",
                    "background",
                    "badges",
                    "banner",
                    "description",
                    "download_options",
                    "downloadable",
                    "drm_encrypted",
                    "duration",
                    "enabled_for_partner",
                    "for_kids",
                    "genres",
                    "genres_string",
                    "horizontal",
                    "hot_content",
                    "is_maxmind_proxy_enabled",
                    "is_premier",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_preview",
                    "is_top250",
                    "is_4k",
                    "is_51",
                    "logotype",
                    "meta",
                    "packshot",
                    "play_last_season",
                    "playback_options",
                    "premium",
                    "quote",
                    "quote_source",
                    "rating_age",
                    "release_date",
                    "slug",
                    "special",
                    "standard",
                    "summary",
                    "subtitle",
                    "thumbnail",
                    "title",
                    "title_original",
                    "trailer_src",
                    "vertical",
                    "video_cover",
                    "web_url",
                    "year",
                    "rating_start",
                    "subscriptions"
                ]
            }
        }
    },
    "required": [
        "original_query",
        "status",
        "meta",
        "items"
    ]
}