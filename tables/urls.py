from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.instruments, name='instruments'),
    path('instruments/<str:tag>/', views.instrument_details, name='instrument_details')
]