from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_babel import Babel
from flask_login import LoginManager
from werkzeug.utils import import_string
from myapp.pygments_ext import PygmentsExtension 

mail = Mail()
db = SQLAlchemy()
babel = Babel()
login_manager = LoginManager()

blueprints = [
  'myapp.main:main',
  'myapp.admin:admin',
  'myapp.api:api'
]

def create_app(config):
  app = Flask(__name__)
  app.config.from_object(config)
  app.jinja_env.add_extension(PygmentsExtension)

  # Load extensions
  mail.init_app(app)
  db.init_app(app)
  babel.init_app(app)
  login_manager.init_app(app)

  # Load blueprints
  for bp_name in blueprints:
    bp = import_string(bp_name)
    app.register_blueprint(bp)
  return app
