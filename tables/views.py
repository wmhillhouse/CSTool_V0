from django.shortcuts import render

from .models import Instrument


# Create your views here.
def instruments(request):

    instrument_table = Instrument.objects.all()

    context = {
        'title': 'Instruments',
        'instrument_table': instrument_table
    }

    return render(request, 'tables/instruments.html', context)


# def instrument_details(request, id):
#
#     instrument = Instrument.objects.get(id=id)
#     context = {
#         'instrument': instrument,
#     }
#     return render(request, 'tables/instruments/details.html', context)
