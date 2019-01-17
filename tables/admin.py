from django.contrib import admin

# Register your models here.
from .models import Instrument, Alarm, Drive, AlarmTypes

admin.site.register(Instrument)
admin.site.register(Drive)

admin.site.register(Alarm)
admin.site.register(AlarmTypes)
