#coding=utf8
from flask import Blueprint, Flask
from flask import g, url_for

#
# def add_subdomain_to_global(endpoint, values):
#     g.subdomain = values.pop('subdomain', None)
#
#
# def add_subdomain_to_url_params(endpoint, values):
#     if not 'subdomain' in values:
#         values['subdomain'] = g.subdomain
#
#
# def add_subdomain_support(app):
#     app.url_value_preprocessor(add_subdomain_to_global)
#     app.url_defaults(add_subdomain_to_url_params)
#
#
# blueprint = Blueprint('app',
#                       __name__,
#                       static_folder='static',
#                       template_folder='templates')

#add_subdomain_support(blueprint)


# @blueprint.context_processor
# def context_processor():
#     static_path_h5_2 = url_for('%s.static' % blueprint.name, filename='/')
#     return dict(static_path_h5_2=static_path_h5_2)

#
# from . import views

app = Flask(__name__)
from . import views
