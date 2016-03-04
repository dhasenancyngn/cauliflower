from . import web
from cauliflower.models import Device, Build
from flask import render_template_string, render_template
@web.route('/')
def front():
    devices = Device.get_dict()
    return render_template("base.html", devices=Device.get_dict())


@web.route('/<string:model>')
def device(model):
    builds = Build.get_dict_by_model(model)
    print(builds)
    from pprint import pprint; pprint(builds)
    return render_template("device.html", devices=Device.get_dict(), builds=Build.get_dict_by_model(model))