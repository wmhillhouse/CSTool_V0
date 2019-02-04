from django.shortcuts import render

from .models import CtrlObject, Instrument, Alarm, Drive

from django.core import serializers

from django.http import HttpResponseRedirect
from django.shortcuts import render

# from .forms import CtrlObjectForm
from django.views.generic import TemplateView


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



# from tables.forms import Create

# def create(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = Create(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = Create()
#
#     return render(request, 'tables/create.html', {'form': form})


# from tables.forms import CtrlObjectForm


# class CtrlObject(TemplateView):
#     template_name = 'tables/all.html'
#
#     def get_all(self, request):
#         form = CtrlObjectForm()
#
#         # Query all fields for all drives and store in an ordered structure
#         data = serializers.serialize("python", CtrlObject.objects.all())
#
#         args = {
#             'title': "All",
#             'address': "all",
#             'data': data
#         }
#
#         return render(request, self.template_name, args)
#
#     def get_details(self, request, tag):
#         # Query all fields for specified drive and store in an ordered structure
#         data = serializers.serialize("python", CtrlObject.objects.filter(tag=tag).all())
#
#         # Query all alarms allocated to specified drive
#         alarms = Alarm.objects.all().filter(refObject=tag)
#
#         # Query all interlocks allocated to specified drive
#         interlocks = Alarm.objects.all().filter(refObject=tag)
#
#         args = {
#             'title': "Control Object Details",
#             'tag': tag,
#             'data': data,
#             'alarms': alarms,
#             'interlocks': interlocks,
#         }
#
#         return render(request, 'tables/details.html', args)
#
#     def create(self, request):
#         form = CtrlObjectForm(request.POST)
#         # if form.is_valid():
#         ctrl_object = form.save(commit=False)
#         ctrl_object.save
#
#         tag = form.cleaned_data['tag']
#         description = form.cleaned_data['description']
#         type = form.cleaned_data['type']
#
#         args = {
#             'form': form,
#             'tag': tag,
#             'description': description,
#             'type': type
#         }
#
#         return render(request, 'tables/create.html', args)

from django.views.generic.edit import CreateView


class AlarmCreate(CreateView):
    model = Alarm
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'table/alarm.html', {'alarm': self.object})

    # fields = ['tag',
    #           'description']