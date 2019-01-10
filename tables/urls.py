from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.instruments, name='instruments'),
    # url(r'/instruments/(?P<id>\d+)/$', views.instrument_details, name='instrument_details')
]