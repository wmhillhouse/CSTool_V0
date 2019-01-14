from django.db import models
import django_tables2 as tables


# Create your models here.
class Instrument(models.Model):
    tag = models.CharField(unique=True, max_length=200)
    description = models.CharField(max_length=200)
    config = models.BooleanField(default=False)
    fat = models.BooleanField(default=False)
    sat = models.BooleanField(default=False)
    # doc_ref = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.tag


class InstrumentTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', orderable=True)

    class Meta:
        model = Instrument
        # sequence = ('id', '...')
        template_name = 'django_tables2/bootstrap.html'


# Create your models here.
class Drive(models.Model):
    tag = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.tag
