from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

migrate.init_app(app, db, render_as_batch=True)

CORS(app, resources={r"/api/clients/*": {"origins": "http://localhost:3000"}})

from app.routes import tracker
app.register_blueprint(tracker, url_prefix="/api/clients")

