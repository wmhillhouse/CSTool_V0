from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # path('', views.login, name='login'),
    url(r'^$', views.login, name='login'),
]