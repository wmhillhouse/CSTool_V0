from django.shortcuts import render

from .models import CtrlObject, Instrument, Alarm, CtrlObjectTypes, AlarmTypes, Drive

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
        'title': "Instruments",
        'address': "instruments",
        'data': data,
    }

    return render(request, 'tables/general_table.html', context)


# Creates a detailed view of an instrument and the relevant linked information
def instrument_details(request, tag):

    try:
        details = serializers.serialize("python", Instrument.objects.filter(tag=tag).all())
    except Instrument.DoesNotExist:
        details = None

    try:
        alarms = Alarm.objects.all().filter(refObject=tag)
    except Instrument.DoesNotExist:
        alarms = None

    context = {
        'details': details,
        'alarms': alarms
    }

    return render(request, 'tables/instrument_details.html', context)


# Creates a table of instruments
def drives(request):

    data = serializers.serialize("python", Drive.objects.all())

    context = {
        'title': "Drives",
        'address': "drives",
        'data': data,
    }

    return render(request, 'tables/general_table.html', context)


# Creates a detailed view of an instrument and the relevant linked information
def actuator_details(request, tag):

    try:
        data = serializers.serialize("python", Drive.objects.filter(tag=tag).all())
    except Drive.DoesNotExist:
        data = None

    try:
        alarms = Alarm.objects.all().filter(refObject=tag)
    except Drive.DoesNotExist:
        alarms = None

    try:
        interlocks = Alarm.objects.all().filter(refObject=tag)
    except Drive.DoesNotExist:
        interlocks = None

    context = {
        'data': data,
        'alarms': alarms,
        'interlocks': interlocks,
    }

    return render(request, 'tables/actuator_details.html', context)
