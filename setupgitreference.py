#!/usr/bin/env python3
# -*- coding: utf8 -*-


import kaptan


config = kaptan.Kaptan()
config.import_config({
    'environment': 'DEV',
    'redis_uri': 'redis://localhost:6379/0',
    'debug': False,
    'pagination': {
        'per_page': 10,
        'limit': 20,
        }
    })

print(config.get("pagination.limit"))
