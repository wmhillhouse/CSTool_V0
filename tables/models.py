from django.db import models


# Create your models here.
class Instrument(models.Model):
    tag = models.CharField(unique=True, max_length=200)
    description = models.CharField(max_length=200)
    # doc_ref = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.tag


# Create your models here.
class Drive(models.Model):
    tag = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.tag
