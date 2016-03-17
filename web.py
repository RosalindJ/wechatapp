# -*- coding: utf-8 -*-
import os
import sys
import flask

sys.path.insert(0, os.path.realpath(os.path.join(
    os.path.dirname(__file__), '../../')))

from flask_debugtoolbar import DebugToolbarExtension

from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]


app = flask.Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

app.config.from_object(__name__)

app.config['TESTING'] = True
app.config['WEIXIN_TOKEN'] = 'fjgirieuwkx245223341jdnff'
app.config['WEIXIN_EXPIRES_IN'] = 2000
app.config['WEIXIN_APP_ID'] = 'wx753cb1f1a5681082'
app.config['WEIXIN_APP_SECRET'] = '10e6312977c6daa0ef68d55bb0ba172b'

from models import db
db.init_app(app)

import views

app.add_url_rule('/', view_func=views.web_index)
#app.add_url_rule('/rates/<int:pid>', view_func=views.rates)
#app.add_url_rule('/deal/<int:pid>', view_func=views.deal)
#app.add_url_rule('/detail/<int:pid>', view_func=views.detail)
#app.add_url_rule('/get_data', view_func=views.get_data)
app.add_url_rule('/presell', view_func=views.presell, methods=['GET', 'POST'])
#app.add_url_rule('/h5/1', view_func=views.h5_1, methods=['GET'])
#app.add_url_rule('/h5/2', view_func=views.h5_2, methods=['GET'])

DebugToolbarExtension(app)

import flask_weixin
weixin = flask_weixin.Weixin(app)

import knife

#app.add_url_rule('/weixin', view_func=weixin.view_func)
app.add_url_rule('/weixin', view_func=knife.do, methods=['GET', 'POST'])
app.add_url_rule('/oauth', view_func=knife.oauth, methods=['GET', 'POST'])


def test():
    result = weixin.jsapi_signature(flask.request.url)
    return flask.render_template('h5/2/index.html', ati=result)


app.add_url_rule('/share/<path:template>', view_func=knife.share)

#import gevent.wsgi
#import werkzeug.serving

#@werkzeug.serving.run_with_reloader
#def runServer():
#    app.debug = False
#
#    ws = gevent.wsgi.WSGIServer(('', 8000), app)
#    ws.serve_forever()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    #runServer()
