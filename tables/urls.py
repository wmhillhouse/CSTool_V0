from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # url(r'^$', views.instruments, name='instruments'),
    path('', views.instruments, name='instruments'),
    path('instruments/<int:my_id>/', views.instrument_details, name='instrument_details')
]