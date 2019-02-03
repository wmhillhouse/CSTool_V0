from django.contrib import admin
from . import models


class CtrlObjectAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']

    list_display = ['tag', 'description']


class DigitalIOAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']

    list_display = ['tag', 'description']


admin.site.register(models.CtrlObject, CtrlObjectAdmin)
admin.site.register(models.Instrument)
admin.site.register(models.DigitalIO, DigitalIOAdmin)

admin.site.register(models.Drive)

admin.site.register(models.Alarm)
