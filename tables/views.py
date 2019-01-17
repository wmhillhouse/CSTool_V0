from django.shortcuts import render

from .models import Instrument
from .models import InstrumentTable

from django.core import serializers


# Create your views here.
def instruments(request):

    # Table 1
    instrument_table = Instrument.objects.all()

    # Table 2
    data = serializers.serialize("python", Instrument.objects.all())

    # Table 3
    data2 = InstrumentTable(Instrument.objects.all())

    context = {
        'title': 'Instruments',
        'instrument_table': instrument_table,
        'data': data,
        'data2': data2
    }

    return render(request, 'tables/instruments.html', context)


def instrument_details(request, my_id):

    # instrument = Instrument.objects.get(id=my_id)

    context = {
        'instrument': my_id,
    }
    return render(request, 'tables/instrument_details.html', context)

