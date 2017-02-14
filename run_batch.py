from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from myapp import create_app
import config

release_app = create_app(config.release)
debug_app = create_app(app.debug)

app = DispatcherMiddleware(release_app, {'/test': debug_app})

run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)