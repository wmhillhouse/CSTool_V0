from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tables/(?P<id>\d+)/$', views.instruments, name='instruments')
]