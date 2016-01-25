from __future__ import unicode_literals

from django.db import models

class Recovery(models.Model):
    path = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sha1sum = models.CharField(max_length=40, blank=True)
    sha512 = models.CharField(max_length=128)
