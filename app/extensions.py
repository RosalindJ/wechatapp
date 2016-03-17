from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension
#from flask.ext.login import LoginManager
from flask_assets import Environment
from flask_bootstrap import Bootstrap

#from appname.models import User

# Setup flask cache
cache = Cache()

# init flask assets
assets_env = Environment()

# init debug_toolbar
debug_toolbar = DebugToolbarExtension()

# init bootstrap
bootstrap = Bootstrap()
