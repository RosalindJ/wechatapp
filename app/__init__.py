# -*- coding: utf-8 -*-
import os
import sys
from flask import Flask

from werkzeug.contrib.fixers import ProxyFix
from werkzeug.routing import BaseConverter

app = Flask(__name__, instance_relative_config=True)
# configure
config = os.environ.get('APP_CONFIG', 'config.development')
app.config.from_object(config)
app.config.from_pyfile('config.py')

# register our blueprints

from .home import blueprint as home_blueprint
#app.url_map.default_subdomain = home_blueprint.name
app.register_blueprint(home_blueprint)#, subdomain=home_blueprint.name)
from .wechat import blueprint as wechat_blueprint
app.register_blueprint(wechat_blueprint)#, subdomain=wechat_blueprint.name)


# proxy
app.wsgi_app = ProxyFix(app.wsgi_app)


class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]

# url path 支持正则表达式
app.url_map.converters['regex'] = RegexConverter
#数据库初始化
from .models import db
db.init_app(app)
# 缓存初始化# debug toolbar 初始化# bootstrap 框架初始化
from app.extensions import (cache, assets_env, debug_toolbar, bootstrap)
cache.init_app(app)
debug_toolbar.init_app(app)
bootstrap.init_app(app)

# 过滤器初始化
from app import filters
filters.init_filters(app)
