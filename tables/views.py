from django.shortcuts import render

from .models import CtrlObject, Instrument, Alarm, Drive

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

    # Query all fields for all instruments and store in an ordered structure
    data = serializers.serialize("python", Instrument.objects.all())

    context = {
        'title': "Instruments",
        'address': "instruments",
        'data': data,
    }

    return render(request, 'tables/general_table.html', context)


# Creates a detailed view of an instrument and the relevant linked information
def instrument_details(request, tag):

    # Query all fields for specified instrument and store in an ordered structure
    data = serializers.serialize("python", Instrument.objects.all().filter(tag=tag))

    # Query all alrams allocated to specified instrument
    alarms = Alarm.objects.all().filter(refObject=tag)

    context = {
        'title': "Instrument Details",
        'tag': tag,
        'data': data,
        'alarms': alarms
    }

    return render(request, 'tables/instrument_details.html', context)


# Creates a table of instruments
def drives(request):

    # Query all fields for all drives and store in an ordered structure
    data = serializers.serialize("python", Drive.objects.all())

    context = {
        'title': "Drives",
        'address': "drives",
        'data': data,
    }

    return render(request, 'tables/general_table.html', context)


# Creates a detailed view of an instrument and the relevant linked information
def actuator_details(request, tag):

    # Query all fields for specified drive and store in an ordered structure
    data = serializers.serialize("python", Drive.objects.filter(tag=tag).all())

    # Query all alarms allocated to specified drive
    alarms = Alarm.objects.all().filter(refObject=tag)

    # Query all interlocks allocated to specified drive
    interlocks = Alarm.objects.all().filter(refObject=tag)

    context = {
        'title': "Drive Details",
        'tag': tag,
        'data': data,
        'alarms': alarms,
        'interlocks': interlocks,
    }

    return render(request, 'tables/actuator_details.html', context)
