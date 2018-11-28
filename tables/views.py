from django.shortcuts import render

from .models import Instrument


# Create your views here.
def index(request):

    instruments = Instrument.objects.all()[:10]

    context = {
        'title': 'Instruments',
        'instruments': instruments
    }

    return render(request, 'tables/index.html', context)


def instruments(request, id):

    instrument = Instrument.objects.get(id=id)
    context = {
        'instrument': instrument,
    }
    return render(request, 'tables/instruments.html', context)
