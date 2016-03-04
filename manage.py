__author__ = 'zifnab'
from flask_script import Manager, Server
from cauliflower import app, db
from flask_migrate import MigrateCommand
import cauliflower.local_config as config

app.config.from_object(config.Development)
app.debug = True

manager=Manager(app)

manager.add_command('runserver', Server(host=app.config.get('HOST', '0.0.0.0'), port=app.config.get('PORT', 5000),
                                        use_debugger=True, use_reloader=True))
manager.add_command('db', MigrateCommand)

@manager.command
def print_routes():
    for rule in app.url_map.iter_rules():
        print(rule)

@manager.command
def init_data():
    #TODO - Move all of these to API calls
    from cauliflower.models import Device, Build, Artifact
    for model in ['mako', 'hammerhead', 'shamu', 'angular']:
        device = Device(model, 'google', 'http://wiki.cyanogenmod.org/w/{0}'.format(model), '{0}.png'.format(model))
        db.session.add(device)

    for i in [1, 2, 3, 4, 5]:
        model = db.session.query(Device).filter_by(model='mako').first()
        build = Build(model=model.id, build_number=i, channel="NIGHTLY")
        recovery = Artifact(build=build.id, _type="recovery", path="/recovery.img", size=123456789, md5="md5", sha1="sha1", sha256="sha256")
        rom = Artifact(build=build.id, _type="build", path="/cm-XXX.img", size=12345678901, md5="md5", sha1="sha1", sha256="sha256")
        manifest = Artifact(build=build.id, _type="manifest", path="/manifest.xml", size=1234567890, md5="md5", sha1="sha1", sha256="sha256")
        build.artifacts = [recovery, rom, manifest]
        db.session.add(recovery)
        db.session.add(rom)
        db.session.add(manifest)
        db.session.add(build)
    db.session.commit()

@manager.command
def clear_database():
    from cauliflower.models.Device import Device
    Device.query.delete()

if __name__ == '__main__':
    manager.run()
