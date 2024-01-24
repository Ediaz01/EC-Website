from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


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



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        new_lead = Lead(
            firstname = request.form["firstname"],
            lastname = request.form["lastname"],
            email = request.form["email"],
            phone = request.form["phone"],
            message = request.form["message"]
        )
        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("contacto.html")


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

