from __future__ import unicode_literals

from django.db import models
from devices.models import Device
# Create your models here.
class Stats(models.Model):
    device_hash = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    model = models.ForeignKey(Device)
    version = models.CharField(max_length=256)
