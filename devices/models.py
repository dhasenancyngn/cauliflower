from django.db import models


class Device(models.Model):
    # TODO: Decide on extra attributes to use, info about the model?
    #       Grouping by Manufacturer? Maintainers?
    model = models.CharField(max_length=50)
