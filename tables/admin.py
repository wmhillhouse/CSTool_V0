from django.contrib import admin

# Register your models here.
from .models import Instrument, Drive

admin.site.register(Instrument)
admin.site.register(Drive)
