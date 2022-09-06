from flask import Flask, render_template
from lorem import sentence, word
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "false"

db = SQLAlchemy(app)


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(120))
    city = db.Column(db.String(120))
    street = db.Column(db.String(120))
    shortDescription = db.Column(db.String(1024), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    dimension = db.Column(db.String(8))
    icon = db.Column(db.String(50))
    color = db.Column(db.String(50))

    def __repr__(self):
        return "<Product %r>" % self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route("/")
def index():
    listings = Listing.query.all()
    return render_template("index.html", listings=listings)

@app.route("/l/<path:path>")
def l(path):
    listing = Listing.query.filter_by(slug=path).first()
    return render_template("index.html", listing=listing)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
