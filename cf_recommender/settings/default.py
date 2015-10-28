# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

DEFAULT_SETTINGS = {
            # redis
            'expire': 3600 * 24 * 30,
            'redis': {
                'host': 'localhost',
                'port': 6379,
                'db': 12
            },
            # recommendation engine settings
            'recommendation_count': 5,
            'recommendation': {
                'update_interval_sec': 60,
                'search_depth': 500,
                'max_history': 1000,
            },
        }
