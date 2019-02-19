from django.contrib import admin
from . import models
from .models import *
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin


class IndexTagAdmin(admin.ModelAdmin):
    search_fields = ['tag', 'description']
    list_filter = ['table']
    list_display = ['table', 'tag', 'description']


class DocumentAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['tag', 'description', 'revision']
    exclude = ['index_tag']


class DocumentSectionInLine(admin.TabularInline):
    model = DocumentSection

    list_display = ['tag', 'description']
    exclude = ['assigned_document', 'index_tag']


class DocumentSectionAdmin(MPTTModelAdmin):

    mptt_level_indent = 50

    inlines = [
        DocumentSectionInLine,
    ]

    list_filter = ['assigned_document']
    list_display = ['tag', 'description', 'order', 'assigned_document']
    list_editable = ['order']


class DocumentEntryAdmin(MPTTModelAdmin):

    search_fields = ['text']
    # list_filter = ['assigned_section']
    # list_display = ['assigned_section', 'id']


class DocumentTextAdmin(admin.ModelAdmin):

    search_fields = ['text']
    # list_filter = ['assigned_section']
    # list_display = ['assigned_section', 'id']


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


admin.site.register(IndexTag, IndexTagAdmin)

admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentSection, DocumentSectionAdmin)

admin.site.register(DocumentText, DocumentTextAdmin)

admin.site.register(DocumentEntry, DocumentEntryAdmin)

# admin.site.register(models.CtrlObject, CtrlObjectAdmin)

admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(DigitalIO, DigitalIOAdmin)
admin.site.register(AnalogIO, AnalogIOAdmin)

admin.site.register(Drive)

admin.site.register(Alarm)
