from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config, TEMPLATE_DIR, STATIC_DIR

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from yacut import api_views, cli_commands, error_handlers, views
db.create_all()