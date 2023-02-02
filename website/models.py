from . import db

class Girldata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image_id = db.Column(db.String(50))
    elo = db.Column(db.Float)
    pos_votes = db.Column(db.Float)
    neg_votes = db.Column(db.Float)
