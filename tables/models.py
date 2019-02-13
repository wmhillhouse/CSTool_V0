from django.db import models
from .constants import *
from django.apps import apps
from model_utils import FieldTracker


# Tags - A unique identifier for all items that are searchable and utilise referencing
class IndexTag(models.Model):

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    table = models.CharField(max_length=32)

    def __str__(self):
        return self.tag


# Custom Database Object - All database objects
class CustomDatabaseObject(models.Model):
    class Meta:
        verbose_name_plural = 'Custom Database Objects'

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='')
    index_tag = models.OneToOneField(IndexTag, blank=True, null=True, on_delete=models.CASCADE)

    # Revision TBA
    # revision = models.FloatField(default=-1.0)

    # Field tracker .... I'm sure this will be used as part of Revision
    tracker = FieldTracker()

    def __str__(self):
        return self.tag

    # Generates index tag automatically
    def create_index(self):
        return self.tag

    # Function to allow child instances to automatically generate tag without modifying the parent save method
    def create_tag(self):
        return self.tag

    # Function to allow child instances to automatically generate description without modifying the parent save method
    def create_description(self):
        return self.description

    def parent_save(self):
        # No change - child to redefine if auto generation is desired
        self.tag = self.create_tag()
        self.description = self.create_description()

        # Automatically create index tag on save
        self.index_tag, created = IndexTag.objects.update_or_create(
            tag=self.index_tag,
            defaults={
                'tag': self.create_index(),
                'table': self._meta.object_name})

    # New save method
    def save(self, *args, **kwargs):
        # Parent save
        self.parent_save()

        # Save the model
        super(CustomDatabaseObject, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Document (CustomDatabaseObject):

    revision = models.FloatField(default=-1.0)


class DocumentSection (CustomDatabaseObject):
    class Meta:
            verbose_name_plural = 'Document Sections'

    section_number = models.CharField(max_length=32, null=True)
    assigned_document = models.ForeignKey(Document, on_delete=models.CASCADE)
    assigned_section = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    hierarchy = models.PositiveSmallIntegerField(choices=HIERARCHY)
    # order = models.PositiveIntegerField(blank=True, null=True)

    # Defines custom index name
    def create_index(self):
        return str(self.assigned_document) + '.' + self.tag

    # Defines the tag as the section number
    def create_tag(self):
        return self.section_number

    def create_description(self):
        if self.description == '':
            return "I'm a goddamn document section"
        else:
            return self.description


class DocumentEntry (CustomDatabaseObject):
    class Meta:
            verbose_name_plural = 'Document Entries'

    # Overwrites parent object fields
    tag = models.CharField(max_length=TAG_TEXT_LEN, editable=False, blank=True)
    description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='')

    assigned_document = models.ForeignKey(Document, on_delete=models.CASCADE)
    assigned_section = models.ForeignKey(DocumentSection, on_delete=models.CASCADE)
    text = models.TextField(max_length=DOC_TEXT_LEN, blank=True, default='')

    # order = models.PositiveIntegerField(unique=True, auto_created=True)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    def create_tag(self):
        return str(self.id)


# Control Object
class CtrlObject(models.Model):
    class Meta:
        verbose_name_plural = 'Control Objects'

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='')
    type = models.CharField(max_length=32, choices=CTRL_OBJ_TYPE)

    # Control Object Methods....
    # .... Can't remember what this needs ...


class Instrument(CustomDatabaseObject):

    io_allocation = models.CharField(max_length=TAG_TEXT_LEN, verbose_name='IO Allocation', blank=True, default='')
    cabinet = models.CharField(max_length=TAG_TEXT_LEN, blank=True, default='')
    pid_doc = models.CharField(max_length=DOC_TEXT_LEN, verbose_name='P&ID', blank=True, default='')
    schematic_doc = models.CharField(max_length=DOC_TEXT_LEN, verbose_name='Schematic', blank=True, default='')
    termination_doc = models.CharField(max_length=DOC_TEXT_LEN, verbose_name='Termination', blank=True, default='')
    datasheet = models.CharField(max_length=DOC_TEXT_LEN, verbose_name='Termination', blank=True, default='')
    # type = type = models.CharField(max_length=32, choices=IO_TYPE, default='DI')


class DigitalInput (Instrument):
    type = models.CharField(max_length=32, choices=IO_TYPE, default='DI')
    on_description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='On')
    off_description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='Off')

    # Set Instrument IO Type to DI..?


class DigitalOutput (Instrument):
    type = models.CharField(max_length=32, choices=IO_TYPE, default='DO')
    on_description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='On')
    off_description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='Off')


class AnalogInput (Instrument):

    type = models.CharField(max_length=32, choices=IO_TYPE, default='AI')
    range = models.CharField(max_length=32, blank=True, default='0-100')
    units = models.CharField(max_length=32, blank=True, default='')
    hh_sp = models.FloatField(verbose_name='High High Setpoint', blank=True, default=95.0)
    h_sp = models.FloatField(verbose_name='High Setpoint', blank=True, default=90.0)
    l_sp = models.FloatField(verbose_name='Low Setpoint', blank=True, default=10.0)
    ll_sp = models.FloatField(verbose_name='Low Low Setpoint', blank=True, default=5.0)
    hysteresis = models.FloatField(verbose_name="Hysteresis", blank=True, default=1.0)


class AnalogOutput (Instrument):

    type = models.CharField(max_length=32, choices=IO_TYPE, default='AO')
    range = models.CharField(max_length=32, blank=True, default='0-100')
    units = models.CharField(max_length=32, blank=True, default='')


##########################################################################################
# Unsure about the following models
##########################################################################################


# Links a tag name to a related reference
# class Reference(models.Model):
#
#     tag1 = models.ManyToManyField(Tag, related_name='tag')
#     tag2 = models.ManyToManyField(Tag, related_name='reference')


class DigitalIO (CustomDatabaseObject):
    class Meta:
            verbose_name_plural = 'Digital IO'

    type = models.CharField(max_length=32, choices=IO_TYPE, default='INPUT')
    on_description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='On')
    off_description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='Off')


class AnalogIO (Instrument):
    class Meta:
            verbose_name_plural = 'Analog IO'

    type = models.CharField(max_length=32, choices=IO_TYPE, default='INPUT')
    range = models.CharField(max_length=32, blank=True, default='0-100')
    units = models.CharField(max_length=32, blank=True, default='')
    hh_sp = models.FloatField(verbose_name='High High Setpoint', blank=True, default=95.0)
    h_sp = models.FloatField(verbose_name='High Setpoint', blank=True, default=90.0)
    l_sp = models.FloatField(verbose_name='Low Setpoint', blank=True, default=10.0)
    ll_sp = models.FloatField(verbose_name='Low Low Setpoint', blank=True, default=5.0)
    hysteresis = models.FloatField(verbose_name="Hysteresis", blank=True, default=1.0)


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################


class Alarm(models.Model):

    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)
    description = models.CharField(max_length=DESC_TEXT_LEN, blank=True, default='')
    type = models.CharField(max_length=SHORT_TEXT_LEN, choices=ALARM_TYPES, default='D')
    priority = models.PositiveSmallIntegerField(choices=ALARM_PRIORITIES, default=4)
    refObject = models.CharField(max_length=TAG_TEXT_LEN, blank=True, default='')

    def __str__(self):
        return self.tag


class Logic(CustomDatabaseObject):

    type = models.CharField(max_length=200, choices=LOGIC_SUFFIX, default='ON')
    alarm_enable = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=ALARM_PRIORITIES, default=4)


class Drive(models.Model):
    tag = models.CharField(unique=True, max_length=TAG_TEXT_LEN)

    def __str__(self):
        return self.tag
