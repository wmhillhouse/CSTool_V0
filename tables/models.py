from django.db import models
from .constants import *


# Control Object
class CtrlObject(models.Model):
    class Meta:
        verbose_name_plural = "Control Objects"

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='')
    type = models.CharField(max_length=32, choices=CTRL_OBJ_TYPE)

    def __str__(self):
        return self.tag


class Instrument(models.Model):
    tag = models.ForeignKey(CtrlObject, on_delete=models.CASCADE)
    io_allocation = models.CharField(max_length=TAG_TEXT_LEN, blank=True, default='')
    cabinet = models.CharField(max_length=TAG_TEXT_LEN, blank=True, default='')
    pid_doc = models.CharField(max_length=DOC_TEXT_LEN, blank=True, default='')
    schematic_doc = models.CharField(max_length=DOC_TEXT_LEN, blank=True, default='')
    termination_doc = models.CharField(max_length=DOC_TEXT_LEN, blank=True, default='')


class DigitalIO (models.Model):
    class Meta:
            verbose_name_plural = 'Digital IO'

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='')
    type = models.CharField(max_length=32, choices=DIGITAL_IO_TYPE, default='DI')
    on_description = models.CharField(max_length=100, default='On')
    off_description = models.CharField(max_length=100, default='Off')


# class Digital_IO(models.Model):
#     class Meta:
#         verbose_name_plural = "Digital IO"
#
#     tag = models.ForeignKey(CtrlObject, on_delete=models.CASCADE)
#
#     on_description = models.CharField(max_length=100, default="On")
#     off_description = models.CharField(max_length=100, default="Off")
#
#     def __str__(self):
#         return self.tag


# class Analog_Input(models.Model):
#     class Meta:
#         verbose_name_plural = "Analog IO"
#     tag = models.CharField(unique=True, max_length=100)
#
#     hysteresis = models.FloatField(verbose_name="Hysteresis", default=1.0)
#     hh_sp = models.FloatField(verbose_name='High High Setpoint', default=95.0)
#     h_sp = models.FloatField(verbose_name='High Setpoint', default=90.0)
#     l_sp = models.FloatField(verbose_name='Low Setpoint', default=10.0)
#     ll_sp = models.FloatField(verbose_name='Low Low Setpoint', default=5.0)


class Alarm(models.Model):

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='')
    type = models.CharField(max_length=SHORT_TEXT_LEN, choices=ALARM_TYPES, default='D')
    priority = models.PositiveSmallIntegerField(choices=ALARM_PRIORITIES, default=4)
    refObject = models.CharField(max_length=TAG_TEXT_LEN, blank=True, default='')

    def __str__(self):
        return self.tag


# class Events(models.Model):
#     EVENT_TYPE = (
#         ('ON', 'On'),
#         ('OFF', 'Off'),
#         ('HH', 'High High'),
#         ('H', 'High'),
#         ('L', 'Low'),
#         ('LL', 'Low Low')
#     )
#
#     ALARM_PRIORITIES = (
#         (1, 'Critical'),
#         (2, 'High'),
#         (3, 'Medium'),
#         (4, 'Low')
#     )
#
#     tag = models.CharField(unique=True, max_length=100)
#     description = models.CharField(max_length=200)
#     refObject = models.CharField(max_length=100)
#     logic = models.CharField(max_length=32, choices=EVENT_TYPE, default='ON')
#     alarm_enable = models.BooleanField(default=False)
#     priority = models.PositiveSmallIntegerField(choices=ALARM_PRIORITIES, default=4)


# Reference Lists
class Reference(models.Model):

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    description = models.CharField(max_length=DESC_TEXT_LEN,
                                   blank=True,
                                   default='')
    type = models.CharField(max_length=32,
                            choices=OBJ_TYPE)

    def __str__(self):
        return self.tag


# Create your models here.
class Drive(models.Model):
    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)

    def __str__(self):
        return self.tag
