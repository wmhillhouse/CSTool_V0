from django.contrib import admin
from . import models


class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag', 'description']
    list_display = ['tag', 'description', 'type']


class DocumentAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['tag', 'description']


class DocumentSectionAdmin(admin.ModelAdmin):

    search_fields = ['assigned_document']
    list_display = ['assigned_document', 'order', 'section_number', 'description']


class CtrlObjectAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['tag', 'description']


class DigitalIOAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['tag', 'description']


admin.site.register(models.Tag, TagAdmin)

admin.site.register(models.Document, DocumentAdmin)
admin.site.register(models.DocumentSection, DocumentSectionAdmin)
admin.site.register(models.DocumentEntry)

admin.site.register(models.CtrlObject, CtrlObjectAdmin)

admin.site.register(models.Instrument)
admin.site.register(models.DigitalIO, DigitalIOAdmin)

admin.site.register(models.Drive)

admin.site.register(models.Alarm)
