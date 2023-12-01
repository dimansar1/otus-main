from os import getenv

from flask import Flask
from flask import request
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for

from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
# from flask_login import LoginManager

from models import db, User
from views.videos import videos_app
from views.forms.users import UserForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.register_blueprint(videos_app)

config_class_name = getenv("CONFIG_CLASS", "DevelopmentConfig")
config_object = f"config.{config_class_name}"
app.config.from_object(config_object)

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)

# login_manager = LoginManager(app)

@app.get("/", endpoint="index")
def hello_root():
    return render_template("index.html")

@app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    # form = UserForm()
    # if request.method == "GET":
    #     return render_template("login.html", form=form)
    
    # if not form.validate_on_submit():
    #     return render_template("login.html", form=form), 400

    # user = User(username=form.data["username"], email=form.data["email"], password=form.data["password"])
    # db.session.add(user)
    # db.session.commit()
    # flash(f"Created user {user.username!r}", category="primary")
    return render_template("login.html")
    # return redirect(url)

@app.route("/register/", methods=["GET", "POST"], endpoint="register")
def register():
    form = UserForm()
    if request.method == "POST":
        if len(request.form['username']) > 4 and len(request.form['email']) > 4 \
            and len(request.form['password']) > 4 and request.form['password'] == request.form['password2']:
            hash = generate_password_hash(form.data['password'])
            res = User(form.data['username'], form.data['email'], hash)
            if res:
                flash("You have successfully registered", "success")
                db.session.add(res)
                db.session.commit()
                return redirect(url_for('login'))
            else:
                flash("Error when adding to the database", "error")
        else:
            flash("The fields are filled in incorrectly", "error")
 
    return render_template("register.html", form=form)