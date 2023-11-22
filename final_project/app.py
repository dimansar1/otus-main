from os import getenv

from flask import Flask
from flask import request
from flask import render_template

from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from models import db
from views.videos import videos_app

app = Flask(__name__)
app.register_blueprint(videos_app)

config_class_name = getenv("CONFIG_CLASS", "DevelopmentConfig")
config_object = f"config.{config_class_name}"
app.config.from_object(config_object)

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)


@app.get("/", endpoint="index")
def hello_root():
    return render_template("index.html")
