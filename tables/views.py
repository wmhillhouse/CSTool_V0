from django.shortcuts import render

from .models import Instrument

from django.core import serializers


# Create your views here.
def instruments(request):

    instrument_table = Instrument.objects.all()

    data = serializers.serialize("python", Instrument.objects.all())

    context = {
        'title': 'Instruments',
        'instrument_table': instrument_table,
        'data': data
    }

    return render(request, 'tables/instruments.html', context)


# def instrument_details(request, id):
#
#     instrument = Instrument.objects.get(id=id)
#     context = {
#         'instrument': instrument,
#     }
#     return render(request, 'tables/instruments/details.html', context)
