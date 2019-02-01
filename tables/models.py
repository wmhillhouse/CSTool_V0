from django.db import models
# Create your models here.


# Control Object
class CtrlObject(models.Model):
    class Meta:
        verbose_name_plural = "Control Objects"

    CTRL_OBJ_TYPE = (
        ('DI', 'Digital Input'),
        ('DO', 'Digital Output'),
        ('AI', 'Analog Input'),
        ('AO', 'Analog Output'),
        ('DRiVE', 'Drive'),
        ('VALVE', 'Valve'),
    )

    tag = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=200, blank=True, default='')
    type = models.CharField(max_length=32, choices=CTRL_OBJ_TYPE)

    def __str__(self):
        return self.tag


class DigitalInput (models.Model):
    class Meta:
            verbose_name_plural = 'Digital Inputs'

    tag = models.ForeignKey(CtrlObject, on_delete=models.CASCADE)
    on_description = models.CharField(max_length=100, default='On')
    off_description = models.CharField(max_length=100, default='Off')


class Instrument(models.Model):

    tag = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=200)
    io_allocation = models.CharField(max_length=100, blank=True, default='')

    # doc_ref = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.tag


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
    ALARM_TYPES = (
        ('D',   'Digital'),
        ('HH',  'High High'),
        ('H',   'High'),
        ('L',   'Low'),
        ('LL',  'Low Low')
    )

    ALARM_PRIORITIES = (
        (1, 'Critical'),
        (2, 'High'),
        (3, 'Medium'),
        (4, 'Low')
    )

    tag = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=32, choices=ALARM_TYPES, default='D')
    priority = models.PositiveSmallIntegerField(choices=ALARM_PRIORITIES, default=4)
    refObject = models.ForeignKey(CtrlObject, on_delete=models.CASCADE)

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


# Create your models here.
class Drive(models.Model):
    tag = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.tag
