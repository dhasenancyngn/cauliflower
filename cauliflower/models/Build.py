from cauliflower import db
from datetime import datetime
from cauliflower.models.Device import Device
class Build(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.Integer, db.ForeignKey('device.id'))
    artifacts = db.relationship('Artifact', backref='build_artifact', lazy='joined')

    build_number = db.Column(db.Integer, unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    date_updated = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now, nullable=False)
    channel = db.Column(db.String, nullable=False)

    def __init__(self, model, build_number, channel):
        self.model = model
        self.build_number = build_number
        self.channel = channel

    @staticmethod
    def get_dict_by_model(model):
        q = db.session.query(Build).join(Device).filter_by(model=model)
        builds = []

        for build in q.all():
            builds.append({
                "model": str(build.model),
                "channel": str(build.channel),
                "artifacts" : [
                    {
                        'type': str(x.type),
                        'path': str(x.path),
                        'size': int(x.size),
                        'md5': str(x.md5) if isinstance(x.md5, str) else None,
                        'sha1': str(x.sha1) if isinstance(x.sha1, str) else None,
                        'sha256': str(x.sha256) if isinstance(x.sha256, str) else None
                    } for x in build.artifacts
                ],
                'build_number': int(build.build_number),
                'date_created': build.date_created,
                'date_updated': build.date_updated
            })
        return builds


class Artifact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    build = db.Column(db.Integer, db.ForeignKey('build.id'))

    type = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    md5 = db.Column(db.String)
    sha1 = db.column(db.String)
    sha256 = db.column(db.String)

    def __init__(self, build, _type, path, size, md5=None, sha1=None, sha256=None):
        self.type = _type
        self.path = path
        self.md5 = md5
        self.size = size
        self.sha1 = sha1
        self.sha256 = sha256

