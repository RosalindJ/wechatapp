#coding=utf8
from flask import Blueprint
from flask import g

blueprint = Blueprint('home',
                      __name__)
from . import views
