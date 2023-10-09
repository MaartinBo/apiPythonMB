API_HOSTS = {
    "test": "http://yourInternaliIp:port/site/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}

WOO_API_HOSTS = {
    "test": "http://yourInternaliIp:port/site",
    "dev": "",
    "prod": ""
}
DB_HOST = {
    'machine1': {
        "test": {"host": "127.0.0.1",
                 "database": "testsite",
                 "table_prefix": "wp_",
                 "socket": None,
                 "port": 8889
                 },
        "dev": {
            "host": "",
            "database": "",
            "table_prefix": "",
            "socket": None,
            "port": ""
        },
        "prod": {
            "host": "",
            "database": "",
            "table_prefix": "",
            "socket": None,
            "port": ""
        },
    },
    'docker': {
        "test": {
            "host": "host.docker.internal",
            "database": "testsite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 8889
        },
    }
    }
