from django.db import models
# Create your models here.


# Control Object
class CtrlObject(models.Model):
    class Meta:
        verbose_name_plural = "Control Objects"

    tag = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=200)
    # CtrlObjectType = models.ForeignKey(CtrlObjectType, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag


class CtrlObjectTypes(models.Model):
    class Meta:
        verbose_name_plural = "Control Object Types"

    id = models.PositiveSmallIntegerField(primary_key=True)
    type = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.tag


class Instrument(models.Model):
    tag = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=200)
    io_allocation = models.CharField(max_length=100, default='')
    config = models.BooleanField(default=False)
    # doc_ref = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.tag


class Alarm(models.Model):
    tag = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=200)
    type = models.PositiveSmallIntegerField()
    priority = models.PositiveSmallIntegerField()
    refObject = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class AlarmTypes(models.Model):
    class Meta:
        verbose_name_plural = "Alarm Types"

    id = models.PositiveSmallIntegerField(primary_key=True)
    type = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.tag


# Create your models here.
class Drive(models.Model):
    tag = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.tag
