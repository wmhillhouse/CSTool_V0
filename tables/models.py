from django.db import models
import django_tables2 as tables
# Create your models here.


# Control Object
# class CtrlObject(models.Model):
#     tag = models.CharField(unique=True, max_length=100)
#     description = models.CharField(max_length=200)
#     type = models.ForeignKey(CtrlObjectType, on_delete=models.CASCADE)
#
# class CtrlObjectType(models.Model):
#     id = models.PositiveSmallIntegerField(primary_key=True)
#     type = models.CharField(unique=True, max_length=32)


class Instrument(models.Model):
    tag = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=200)
    config = models.BooleanField(default=False)
    fat = models.BooleanField(default=False)
    sat = models.BooleanField(default=False)
    # doc_ref = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.tag


class Alarm(models.Model):
    tag = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=200)
    type = models.PositiveSmallIntegerField()
    priority = models.PositiveSmallIntegerField()
    refObject = models.CharField(max_length=100)


class AlarmTypes(models.Model):
    class Meta:
        verbose_name_plural = "Alarm Types"

    id = models.PositiveSmallIntegerField(primary_key=True)
    type = models.CharField(unique=True, max_length=32)


# Create your models here.
class Drive(models.Model):
    tag = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.tag
