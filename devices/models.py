from django.db import models
from django.conf import settings

class Device(models.Model):
    # TODO: Decide on extra attributes to use, info about the model?
    #       Grouping by Manufacturer? Maintainers?
    model = models.CharField(max_length=50)
    image = models.FileField(upload_to=settings.IMAGE_PATH, default='noimage.png')



