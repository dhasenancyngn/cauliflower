from __future__ import unicode_literals

from django.db import models
from devices.models import Device
from recoveries.models import Recovery

class Build(models.Model):
    # TODO: Decide on extra attributes to use, info about the model?
    #       Grouping by Manufacturer? Maintainers?
    device = models.ForeignKey(Device)
    recovery = models.ForeignKey(Recovery)
    path = models.CharField(max_length=100)
    size = models.IntegerField()
    md5sum = models.CharField(max_length=32, blank=True)
    sha1sum = models.CharField(max_length=40, blank=True)
    sha512 = models.CharField(max_length=128)
    build_number = models.IntegerField()
    fingerprint = models.CharField(max_length=256)
    description = models.CharField(max_length=4096, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
