trailer = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "_cls": {
            "type": "string"
        },
        "_id": {
            "type": "string"
        },
        "additional_content": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "uid": {
                        "type": "string"
                    },
                    "video_src": {
                        "type": "string"
                    },
                    "announcement": {
                        "type": "boolean"
                    },
                    "restrictions": {
                        "type": "array"
                    },
                    "start_id": {
                        "type": "integer"
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
                    }
                },
                "required": [
                    "description",
                    "title",
                    "uid",
                    "video_src",
                    "announcement",
                    "restrictions",
                    "start_id",
                    "packshot"
                ]
            }
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
            "type": "array"
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
        "budget": {
            "type": "string"
        },
        "cast": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "alias": {
                        "type": "string"
                    },
                    "character": {
                        "type": "object",
                        "properties": {
                            "biography": {
                                "type": "string"
                            },
                            "main_character": {
                                "type": "boolean"
                            },
                            "name": {
                                "type": "string"
                            },
                            "photo": {
                                "type": "null"
                            },
                            "photo_app_section": {
                                "type": "null"
                            },
                            "start_id": {
                                "type": "integer"
                            },
                            "weight": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            }
                        },
                        "required": [
                            "biography",
                            "main_character",
                            "name",
                            "start_id"
                        ]
                    },
                    "filmography": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "photo": {
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
                    }
                },
                "required": [
                    "alias",
                    "character",
                    "filmography",
                    "name",
                    "photo"
                ]
            }
        },
        "color": {
            "type": "object",
            "properties": {
                "back_color_1": {
                    "type": "string"
                },
                "back_color_2": {
                    "type": "string"
                },
                "font_color": {
                    "type": "string"
                }
            },
            "required": [
                "back_color_1",
                "back_color_2",
                "font_color"
            ]
        },
        "composers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "alias": {
                        "type": "string"
                    },
                    "character": {
                        "type": "object",
                        "properties": {
                            "photo": {
                                "type": "null"
                            },
                            "photo_app_section": {
                                "type": "null"
                            }
                        },
                    },
                    "filmography": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "photo": {
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
                    }
                },
                "required": [
                    "alias",
                    "character",
                    "filmography",
                    "name",
                    "photo"
                ]
            }
        },
        "description": {
            "type": "string"
        },
        "directors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "alias": {
                        "type": "string"
                    },
                    "character": {
                        "type": "object",
                        "properties": {
                            "photo": {
                                "type": "null"
                            },
                            "photo_app_section": {
                                "type": "null"
                            }
                        },
                    },
                    "filmography": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "photo": {
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
                    }
                },
                "required": [
                    "alias",
                    "character",
                    "filmography",
                    "name",
                    "photo"
                ]
            }
        },
        "display": {
            "type": "boolean"
        },
        "downloadable": {
            "type": "boolean"
        },
        "duration": {
            "type": "integer"
        },
        "duration_minutes": {
            "type": "string"
        },
        "enabled_for_partner": {
            "type": "boolean"
        },
        "facts": {
            "type": "array"
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
        "hashtags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "alias": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "text_color": {
                        "type": "string"
                    },
                    "url": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "alias",
                    "title",
                    "text_color",
                    "url"
                ]
            }
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
        "horizontal_poster": {
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
        "in_subscription": {
            "type": "boolean"
        },
        "is_4k": {
            "type": "boolean"
        },
        "is_51": {
            "type": "boolean"
        },
        "is_disabled": {
            "type": "boolean"
        },
        "is_free": {
            "type": "boolean"
        },
        "is_premier": {
            "type": "boolean"
        },
        "is_preview": {
            "type": "boolean"
        },
        "items": {
            "type": "array"
        },
        "items_total": {
            "type": "integer"
        },
        "kinopoisk_id": {
            "type": "string"
        },
        "locales": {
            "type": "array",
            "items": {
                "type": "string"
            }
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
        "operators": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "alias": {
                        "type": "string"
                    },
                    "character": {
                        "type": "object",
                        "properties": {
                            "photo": {
                                "type": "null"
                            },
                            "photo_app_section": {
                                "type": "null"
                            }
                        },
                    },
                    "filmography": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "photo": {
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
                    }
                },
                "required": [
                    "alias",
                    "character",
                    "filmography",
                    "name",
                    "photo"
                ]
            }
        },
        "origin_countries": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    }
                },
                "required": [
                    "code",
                    "title"
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
        "producers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "alias": {
                        "type": "string"
                    },
                    "character": {
                        "type": "object",
                        "properties": {
                            "photo": {
                                "type": "null"
                            },
                            "photo_app_section": {
                                "type": "null"
                            }
                        },
                    },
                    "filmography": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "photo": {
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
                    }
                },
                "required": [
                    "alias",
                    "character",
                    "filmography",
                    "name",
                    "photo"
                ]
            }
        },
        "promo_content": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string"
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
                    "restrictions": {
                        "type": "array"
                    },
                    "title": {
                        "type": "string"
                    },
                    "start_id": {
                        "type": "integer"
                    },
                    "uid": {
                        "type": "string"
                    },
                    "video_src": {
                        "type": "string"
                    }
                },
                "required": [
                    "description",
                    "packshot",
                    "restrictions",
                    "title",
                    "start_id",
                    "uid",
                    "video_src"
                ]
            }
        },
        "publish": {
            "type": "string"
        },
        "quote": {
            "type": "string"
        },
        "quote_source": {
            "type": "string"
        },
        "rating_age": {
            "type": "string"
        },
        "rating_imdb": {
            "type": "number"
        },
        "rating_kp": {
            "type": "number"
        },
        "rating_start": {
            "type": "number"
        },
        "release_date": {
            "type": "integer"
        },
        "release_year_end": {
            "type": "null"
        },
        "release_year_start": {
            "type": "integer"
        },
        "restrictions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    }
                },
                "required": [
                    "id"
                ]
            }
        },
        "seo": {
            "type": "object",
            "properties": {
                "long_description": {
                    "type": "string"
                },
                "short_description": {
                    "type": "string"
                },
                "subject": {
                    "type": "string"
                }
            },
            "required": [
                "long_description",
                "short_description",
                "subject"
            ]
        },
        "slug": {
            "type": "string"
        },
        "similar": {
            "type": "string"
        },
        "special": {
            "type": "boolean"
        },
        "special_description": {
            "type": "object",
            "properties": {
                "paragraph_1": {
                    "type": "string"
                },
                "paragraph_2": {
                    "type": "string"
                },
                "paragraph_3": {
                    "type": "string"
                },
                "paragraph_4": {
                    "type": "string"
                }
            },
            "required": [
                "paragraph_1",
                "paragraph_2",
                "paragraph_3",
                "paragraph_4"
            ]
        },
        "standard": {
            "type": "boolean"
        },
        "start_release_date": {
            "type": "string"
        },
        "subtitle": {
            "type": "string"
        },
        "subscriptions": {
            "type": "array"
        },
        "thumbnail": {
            "type": "object",
            "properties": {
                "image_1x": {
                    "type": "null"
                },
                "image_15x": {
                    "type": "string"
                }
            },
            "required": [
                "image_15x"
            ]
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
        "uid": {
            "type": "string"
        },
        "unavailable_by_geo": {
            "type": "boolean"
        },
        "unpublish": {
            "type": "integer"
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
        "vertical_poster": {
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
        "web_url": {
            "type": "string"
        },
        "weight": {
            "type": "null"
        },
        "writers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "alias": {
                        "type": "string"
                    },
                    "character": {
                        "type": "object",
                        "properties": {
                            "photo": {
                                "type": "null"
                            },
                            "photo_app_section": {
                                "type": "null"
                            }
                        },
                    },
                    "filmography": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "photo": {
                        "type": "object",
                        "properties": {
                            "image_1x": {
                                "type": [
                                    "string",
                                    "null"
                                ]
                            },
                            "image_15x": {
                                "type": [
                                    "string",
                                    "null"
                                ]
                            }
                        },
                    }
                },
                "required": [
                    "alias",
                    "character",
                    "filmography",
                    "name",
                    "photo"
                ]
            }
        },
        "year": {
            "type": "integer"
        }
    },
    "required": [
        "_cls",
        "_id",
        "additional_content",
        "alias",
        "background",
        "badges",
        "banner",
        "budget",
        "cast",
        "color",
        "composers",
        "description",
        "directors",
        "display",
        "downloadable",
        "duration",
        "duration_minutes",
        "enabled_for_partner",
        "facts",
        "for_kids",
        "genres",
        "hashtags",
        "horizontal",
        "horizontal_poster",
        "in_subscription",
        "is_4k",
        "is_51",
        "is_disabled",
        "is_free",
        "is_premier",
        "is_preview",
        "items",
        "items_total",
        "kinopoisk_id",
        "locales",
        "logotype",
        "operators",
        "origin_countries",
        "packshot",
        "play_last_season",
        "playback_options",
        "producers",
        "promo_content",
        "publish",
        "quote",
        "quote_source",
        "rating_age",
        "rating_imdb",
        "rating_kp",
        "rating_start",
        "release_date",
        "release_year_start",
        "restrictions",
        "seo",
        "slug",
        "similar",
        "special",
        "special_description",
        "standard",
        "start_release_date",
        "subtitle",
        "subscriptions",
        "thumbnail",
        "title",
        "title_original",
        "trailer_src",
        "uid",
        "unavailable_by_geo",
        "unpublish",
        "vertical",
        "vertical_poster",
        "web_url",
        "writers",
        "year"
    ]
}