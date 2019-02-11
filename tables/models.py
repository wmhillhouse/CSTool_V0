from django.db import models
from .constants import *
from django.apps import apps


# Tags - A unique identifier for all items that are searchable and utilise referencing
class IndexTag(models.Model):

    table = models.CharField(max_length=32)
    tag = models.CharField(max_length=TAG_TEXT_LEN)

    def __str__(self):
        return self.table + '.' + self.tag

    class Meta:
        unique_together = ('table', 'tag')


# Custom Database Object - All database objects
class CustomDatabaseObject(models.Model):
    class Meta:
        verbose_name_plural = 'Custom Database Objects'

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='')
    index_tag = models.OneToOneField(IndexTag, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

    # Defines custom index name
    def get_index(self):
        return str(self.tag)

    # New save method
    def save(self, *args, **kwargs):

        # Automatically create index tag on save - this will fail if a unique tag has not been created
        self.index_tag, created = IndexTag.objects.update_or_create(
            tag=self.get_index(),
            defaults={
                'tag': self.tag,
                'table': self._meta.object_name})

        # Save the model
        super(CustomDatabaseObject, self).save(*args, **kwargs)

    class Meta:
        abstract = True

# Links a tag name to a related reference
# class Reference(models.Model):
#
#     tag1 = models.ManyToManyField(Tag, related_name='tag')
#     tag2 = models.ManyToManyField(Tag, related_name='reference')


class Document (CustomDatabaseObject):

    revision = models.FloatField(default=-1.0)


class DocumentSection (CustomDatabaseObject):
    class Meta:
            verbose_name_plural = 'Document Sections'

    assigned_document = models.ForeignKey(Document, on_delete=models.CASCADE)
    assigned_section = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    hierarchy = models.PositiveSmallIntegerField(choices=HIERARCHY)
    order = models.PositiveIntegerField(blank=True, null=True)
    section_number = models.CharField(max_length=32, blank=True, null=True)

    # Defines custom index name
    def get_index(self):
        return str(self.assigned_document) + '.' + self.tag

    # New save method
    # # Modify normal index tag creation to have a custom string as part of the tag
    # def save(self, *args, **kwargs):
    #
    #     # Automatically create index tag on save - this will fail if a unique tag has not been created
    #     self.index_tag = IndexTag.objects.create(
    #         tag=str(self.assigned_document) + '.' + self.tag,
    #         table=self._meta.object_name
    #     )
    #
    #     # A horrendously convoluted way to get a generic variable for this model class
    #     this_model = apps.get_model('tables', self.__class__.__name__)
    #
    #     # Save the model
    #     super(this_model, self).save(*args, **kwargs)


class DocumentEntry (models.Model):
    class Meta:
            verbose_name_plural = 'Document Entries'

    assigned_section = models.ForeignKey(DocumentSection, on_delete=models.CASCADE)
    text = models.TextField(max_length=DOC_TEXT_LEN, blank=True, default='')
    order = models.PositiveIntegerField(unique=True,auto_created=True)


# Control Object
class CtrlObject(models.Model):
    class Meta:
        verbose_name_plural = 'Control Objects'

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='')
    type = models.CharField(max_length=32, choices=CTRL_OBJ_TYPE)

    def __str__(self):
        return self.tag


class Instrument(CustomDatabaseObject):

    io_allocation = models.CharField(max_length=TAG_TEXT_LEN, blank=True, default='')
    cabinet = models.CharField(max_length=TAG_TEXT_LEN, blank=True, default='')
    pid_doc = models.CharField(max_length=DOC_TEXT_LEN, blank=True, default='')
    schematic_doc = models.CharField(max_length=DOC_TEXT_LEN, blank=True, default='')
    termination_doc = models.CharField(max_length=DOC_TEXT_LEN, blank=True, default='')


class DigitalIO (CustomDatabaseObject):
    class Meta:
            verbose_name_plural = 'Digital IO'

    type = models.CharField(max_length=32, choices=IO_TYPE)
    on_description = models.CharField(max_length=100, default='On')
    off_description = models.CharField(max_length=100, default='Off')


# class AnalogIO (Instrument):
#     class Meta:
#             verbose_name_plural = 'Digital IO'
#
#     type = models.CharField(max_length=32, choices=IO_TYPE)


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


class Events(models.Model):


    type = models.CharField(max_length=200, choices=EVENT_TYPES, default='ON')
    alarm_enable = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=ALARM_PRIORITIES, default=4)





# Create your models here.
class Drive(models.Model):
    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)

    def __str__(self):
        return self.tag
