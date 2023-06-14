from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


class Mouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mouseName = db.Column(db.String(150), unique=True)
    mouseImg = db.Column(db.String(150), unique=True)
    mouseCat = db.Column(db.String(150))
    mouseSubCat = db.Column(db.String(150))
    powerType = db.Column(db.String(150))