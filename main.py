from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, InputRequired, Email, Length
from flask_bootstrap import Bootstrap




class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template("index.html")


def verify_admin(form):
    email = form.email.data
    password = form.password.data
    if email == "admin@email.com" and password == "12345678":
        return True
    else:
        return False

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        check = verify_admin(login_form)
        print(check)
        if check:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)