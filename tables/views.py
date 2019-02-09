from django.shortcuts import render

from .models import CtrlObject, Instrument, Alarm, Drive

from django.core import serializers

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# from .forms import CtrlObjectForm
from django.views.generic import TemplateView


# Libraries for Login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('tables:user_login'))
            else:
                return HttpResponse("Account not active.")
        else:
            return HttpResponse("Invalid login details.")
    else:
        return render(request, 'tables/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('tables:user_login'))


# Creates a table of instruments
@login_required
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
@login_required
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


from django.views.generic import    (View, TemplateView,
                                     ListView, DetailView,
                                     CreateView, UpdateView,
                                     DeleteView)
from . import models
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string


class AlarmListView(ListView):
    model = models.Alarm


class AlarmCreate(CreateView):
    model = Alarm
    fields = '__all__'

    success_url = reverse_lazy('tables:alarm-create')

    # def dispatch(self, *args, **kwargs):
    #     self.tag = kwargs['pk']
    #     return super(AlarmCreate, self).dispatch(*args, **kwargs)

    # def form_valid(self, form):
    #     form.save()
    #     alarm = Alarm.objects.get(tag=self.tag)
    #     return HttpResponse(render_to_string('tables/modal_form_success.html', {'alarm': alarm}))

    # def form_valid(self, form):
    #     self.object = form.save()
    #     return render(self.request, 'http://localhost:8000/admin/tables/alarm', {'alarm': self.object})

    # def get_initial(self):
    #     tag = get_object_or_404(Tag, slug=self.kwargs.get('tag'))
    #     return {
    #         'tag': tag,
    #     }

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['cpf'] = self.args[0]
    #     return initial
