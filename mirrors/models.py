from __future__ import unicode_literals

from django.db import models

class Mirror(models.Model):
    basepath = models.CharField(max_length=100)
    weight = models.IntegerField()
    region = models.CharField(max_length=100)
    available = models.BooleanField(default=False)

