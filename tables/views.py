from django.shortcuts import render

from .models import CtrlObject, Instrument, Alarm, CtrlObjectTypes, AlarmTypes

from django.core import serializers


# # All Control Objects
# def ctrl_objects(request):
#
#     data = serializers.serialize("python", CtrlObject.objects.all())
#
#     context = {
#         'data': data,
#     }
#
#     return render(request, 'tables/all.html', context)


# Creates a table of instruments
def instruments(request):

    data = serializers.serialize("python", Instrument.objects.all())

    context = {
        'data': data,
    }

    return render(request, 'tables/instruments.html', context)


# Creates a detailed view of an instrument and the relevant linked information
def instrument_details(request, tag):

    try:
        details = serializers.serialize("python", Instrument.objects.filter(tag=tag).all())
    except Instrument.DoesNotExist:
        details = None

    try:
        # alarms = serializers.serialize("python", Alarm.objects.filter(refObject=tag).all())
        alarms = Alarm.objects.all().filter(refObject=tag)  # .values('tag', 'description')
    except Instrument.DoesNotExist:
        alarms = None

    context = {
        'details': details,
        'alarms': alarms
    }

    return render(request, 'tables/instrument_details.html', context)

