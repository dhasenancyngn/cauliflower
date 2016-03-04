from flask import jsonify

from cauliflower.blueprints.api import api
from cauliflower.models import Device

@api.route('/api/v1/devices', methods=('GET',))
def devices():

    return jsonify(**{'devices': Device.get_dict()})