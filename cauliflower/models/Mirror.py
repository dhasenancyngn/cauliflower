from cauliflower import db

class Mirror(object):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    weight = db.Column(db.String)
    available = db.Column(db.Boolean)
