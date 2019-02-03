from django import forms
from .constants import *
from tables.models import CtrlObject, Alarm


# class Create(forms.Form):
#     tag = forms.CharField(label='Tag', max_length=TAG_TEXT_LEN)
#     description = forms.CharField(label='Description', max_length=DESC_TEXT_LEN)
#     type = forms.CharField(label='Type', max_length=TAG_TEXT_LEN)
#
#
# class CreateForm(forms.ModelForm):
#     tag = forms.CharField(label='Tag', max_length=TAG_TEXT_LEN)
#     description = forms.CharField(label='Description', max_length=DESC_TEXT_LEN)
#     type = forms.CharField(label='Type', max_length=TAG_TEXT_LEN)
#
#     class Meta:
#         model = CtrlObject
#         fields = ('tag',
#                   'description',
#                   'type')
#
#
# class CtrlObjectForm(forms.ModelForm):
#     class Meta:
#         model = CtrlObject
#         fields = ['tag',
#                   'description',
#                   'type']

#
# class AlarmForm(forms.ModelForm):
#     class Meta:
#         model = Alarm
#         fields = '__all__'
