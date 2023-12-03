from os import getenv, path

from flask import Flask
from flask import request
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import send_from_directory

from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from models import db
from views.videos import videos_app

from models import db, Video

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
    videos: list[Video] = Video.query.order_by(Video.id).all()
    return render_template("index.html", videos=videos)

@app.route('/upload/<name>')
def download(name):
    return send_from_directory(path.join(app.root_path, 'upload'), name)
