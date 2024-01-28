from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import os


app = Flask(__name__)


##SECRET KEY 
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_key_for_development')



##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///contact_list.db"
# Create the extension
db = SQLAlchemy()
# initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String, nullable=False)
    message = db.Column(db.String(500), nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()



# Define WTForms Form
# First, you define a WTForms form that corresponds to your Lead model. 
# This form will be used for input validation and CSRF protection.
class LeadForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(max=250)], render_kw={"placeholder": "Nombre"})
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max=250)], render_kw={"placeholder": "Apellido"})
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=250)], render_kw={"placeholder": "Email"})
    phone = StringField('Phone', validators=[DataRequired()], render_kw={"placeholder": "Teléfono"})
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)], render_kw={"placeholder": "Mensaje"})
    submit = SubmitField('Enviar')



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    form = LeadForm()
    if form.validate_on_submit():
        new_lead = Lead(
            firstname = form.firstname.data,
            lastname = form.lastname.data,
            email = form.email.data,
            phone = form.phone.data,
            message = form.message.data
        )
        db.session.add(new_lead)
        db.session.commit()
        flash('Lead submitted successfully!', 'success')
                
        return redirect(url_for("home"))
    return render_template("contacto.html", form=form)


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/acerca")
def acerca():
    return render_template("acerca.html")


@app.route("/articlea")
def articlea():
    return render_template("articlea.html")


@app.route("/articleb")
def articleb():
    return render_template("articleb.html")


@app.route("/articlec")
def articlec():
    return render_template("articlec.html")


@app.route("/articled")
def articled():
    return render_template("articled.html")




if __name__ == "__main__":
    app.run(debug=True)

