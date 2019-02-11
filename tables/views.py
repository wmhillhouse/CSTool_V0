from .constants import *

from django.shortcuts import render

from .models import *

from django.core import serializers

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# from .forms import CtrlObjectForm


from django.views.generic import TemplateView

from django.apps import apps

# Libraries for Login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required


# User login
def user_login(request):

    # Proceed if the request method is POST
    if request.method == 'POST':
        # Get username and password from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check user authentication
        user = authenticate(username=username, password=password)

        # If user exists - authentication is successful
        if user:

            # If the user is active - log the user in and return the user to the login page
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('tables:user_login'))

            # If the user is not active - notify the user
            else:
                return HttpResponse("Account not active.")

        # If user does not exist - notify the user
        else:
            return HttpResponse("Invalid login details.")

    # If request is not the POST request, send an empty request
    else:
        return render(request, 'tables/login.html', {})


# User logout
@login_required(login_url=LOGIN_URL)
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('tables:user_login'))


# Creates a generic list of items
@login_required(login_url=LOGIN_URL)
def generic_list(request, table_name):

    # Get the table from the name of the table
    table = apps.get_model('tables', table_name)

    # Query all fields for all instruments and store in an ordered structure
    data = serializers.serialize("python", table.objects.all())

    context = {
        'title': table._meta.object_name,
        'address': table._meta.model_name,
        'data': data,
    }

    return render(request, 'tables/general_table.html', context)


# Creates a table of documents
@login_required(login_url=LOGIN_URL)
def document_list(request):

    # Query all fields for all instruments and store in an ordered structure
    data = serializers.serialize("python", Document.objects.all())

    context = {
        'title': "Documents",
        'address': "documents",
        'data': data,
    }

    return render(request, 'tables/general_table.html', context)


# Creates a table of instruments
@login_required(login_url=LOGIN_URL)
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
@login_required(login_url=LOGIN_URL)
def details(request, tag):

    test = CtrlObject.objects.filter(tag=tag)
    test('type')


    # Query all fields for specified instrument and store in an ordered structure
    data = serializers.serialize("python", Instrument.objects.all().filter(tag=tag))

    # Query all alarms allocated to specified instrument
    alarms = Alarm.objects.all().filter(refObject=tag)

    context = {
        'title': "Instrument Details",
        'tag': tag,
        'data': data,
        'alarms': alarms,
    }

    return render(request, 'tables/instrument_details.html', context)


# Creates a detailed view of an instrument and the relevant linked information
@login_required(login_url=LOGIN_URL)
def instrument_details(request, tag):

    # Query all fields for specified instrument and store in an ordered structure
    data = serializers.serialize("python", Instrument.objects.all().filter(tag=tag))

    # Query all alarms allocated to specified instrument
    alarms = Alarm.objects.all().filter(refObject=tag)

    context = {
        'title': "Instrument Details",
        'tag': tag,
        'data': data,
        'alarms': alarms,
    }

    return render(request, 'tables/instrument_details.html', context)


# Creates a table of instruments
@login_required(login_url=LOGIN_URL)
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
@login_required(login_url=LOGIN_URL)
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


from django.views.generic import    (View, TemplateView,
                                     ListView, DetailView,
                                     CreateView, UpdateView,
                                     DeleteView)
from . import models
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string


class AlarmListView(ListView):
    model = models.Alarm


# @login_required(login_url=LOGIN_URL)
# @permission_required('tables.alarm.can_add_drive')
class AlarmCreate(CreateView):
    model = Alarm
    fields = '__all__'

    success_url = reverse_lazy('tables:alarm-create')
