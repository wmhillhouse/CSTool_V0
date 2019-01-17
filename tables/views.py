from django.shortcuts import render

from .models import Instrument, Alarm
# from .models import InstrumentTable

from django.core import serializers


# Create your views here.

# Creates a table of instruments
def instruments(request):

    # Table 2
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
        alarms = Alarm.objects.all().filter(refObject=tag).values('tag', 'description')
    except Instrument.DoesNotExist:
        details = None

    context = {
        'details': details,
        'alarms': alarms
    }

    return render(request, 'tables/instrument_details.html', context)

