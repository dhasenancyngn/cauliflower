from cauliflower import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, unique=True, nullable=False)
    oem = db.Column(db.String)
    wiki = db.Column(db.String)
    imagepath = db.Column(db.String)

    def __init__(self, model, oem='unknown', wiki=None, imagepath='/static/no-image.png'):
        self.model = model
        self.oem = oem
        self.wiki = wiki
        self.imagepath = imagepath

    @staticmethod
    def get_dict_by_model(model):
        device = db.session.query(Device).filter_by(model=model).first()
        return {'model': device.model, 'oem': device.oem, 'wiki': device.wiki, 'imagepath': device.imagepath}

    @staticmethod
    def get_dict():
        devices = db.session.query(Device).all()
        return [{'model': x.model, 'oem': x.oem, 'wiki': x.wiki, 'imagepath': x.imagepath} for x in devices]