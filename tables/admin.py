from django.contrib import admin

# Register your models here.
from .models import CtrlObject, Instrument, DigitalInput, Alarm, Drive

admin.site.register(CtrlObject)

admin.site.register(Instrument)
admin.site.register(DigitalInput)
admin.site.register(Drive)

admin.site.register(Alarm)
