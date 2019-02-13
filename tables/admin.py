from django.contrib import admin
from . import models


class IndexTagAdmin(admin.ModelAdmin):
    search_fields = ['tag']
    list_filter = ['table']
    list_display = ['table', 'tag']


class DocumentAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['index_tag', 'tag', 'description']
    exclude = ['index_tag']


class DocumentSectionAdmin(admin.ModelAdmin):

    search_fields = ['assigned_document']
    list_display = ['index_tag', 'assigned_document', 'section_number', 'description']
    exclude = ['index_tag']


class DocumentEntryAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['index_tag', 'tag', 'description']
    exclude = ['index_tag']


class InstrumentAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['tag', 'description']
    exclude = ['index_tag']


class DigitalIOAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['tag', 'description']
    exclude = ['index_tag']


class AnalogIOAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['tag', 'description']
    exclude = ['index_tag']


admin.site.register(models.IndexTag, IndexTagAdmin)

admin.site.register(models.Document, DocumentAdmin)
admin.site.register(models.DocumentSection, DocumentSectionAdmin)
admin.site.register(models.DocumentEntry, DocumentEntryAdmin)

# admin.site.register(models.CtrlObject, CtrlObjectAdmin)

admin.site.register(models.Instrument, InstrumentAdmin)
admin.site.register(models.DigitalIO, DigitalIOAdmin)
admin.site.register(models.AnalogIO, AnalogIOAdmin)

admin.site.register(models.Drive)

admin.site.register(models.Alarm)
