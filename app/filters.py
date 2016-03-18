# -*- coding: utf-8 -*-
from app import app


def init_filters(application):
    application.jinja_env.filters['datetimefilter'] = datetimefilter


@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M:%S'):
    """convert a datetime to a different format."""
    return value.strftime(format)
