from django.contrib import admin
from . import models
from .models import *
from mptt.admin import DraggableMPTTAdmin


class IndexTagAdmin(admin.ModelAdmin):
    search_fields = ['tag']
    list_filter = ['table']
    list_display = ['table', 'tag']


class DocumentAdmin(admin.ModelAdmin):

    search_fields = ['tag', 'description']
    list_display = ['tag', 'description', 'revision']
    exclude = ['index_tag']


# class DocumentSectionAdmin(admin.ModelAdmin):
#
#     search_fields = ['assigned_document']
#     list_display = ['index_tag', 'assigned_document', 'section_number', 'description']
#     exclude = ['index_tag']


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

############################################################


class DocumentSectionAdmin(DraggableMPTTAdmin):
    # search_fields = ['tag', 'description']
    list_filter = ['assigned_document']
    # list_display = ['assigned_document', 'indented_title', 'tag', 'description']
    # exclude = ['index_tag']


admin.site.register(DocumentSection, DocumentSectionAdmin)

###


admin.site.register(IndexTag, IndexTagAdmin)

admin.site.register(Document, DocumentAdmin)
# admin.site.register(DocumentSection, DocumentSectionAdmin)
admin.site.register(DocumentEntry, DocumentEntryAdmin)

# admin.site.register(models.CtrlObject, CtrlObjectAdmin)

admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(DigitalIO, DigitalIOAdmin)
admin.site.register(AnalogIO, AnalogIOAdmin)

admin.site.register(Drive)

admin.site.register(Alarm)
