from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import cauliflower.local_config as config

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from cauliflower.models import Device
from cauliflower.blueprints.api import api
from cauliflower.blueprints.web import web
app.register_blueprint(api)
app.register_blueprint(web)