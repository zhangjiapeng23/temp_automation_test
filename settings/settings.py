'''
    Temp base settings
'''
import logging

DEBUG = FALSE

# project host
PROJECT_HOST = ''

MIDDLEWARE = {
    "mysql": {
        "host": "",
        "username": "",
        "password": "",
        "port": None
    },
    "redis": {
        "host": "",
        "password": "",
        "port": None
    }
}

APPS = [
    {
        "name": "",
        "namespace": "",
        "deployment": "",
        "path": {
            "api_name": "/xxx/xxx",
        }
    }
]

# 终端日志等级
SH_LOG_LEVEL = logging.INFO
# 文本日志等级
FH_LOG_LEVEL = logging.DEBUG

