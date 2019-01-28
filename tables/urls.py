from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    #path('', views.ctrlobject, name='ctrlobject'),
    path('', views.instruments, name='instruments'),
    path('drives', views.drives, name='drives'),
    path('instruments/<str:tag>/', views.instrument_details, name='instrument_details'),
    path('drives/<str:tag>/', views.actuator_details, name='actuator_details')

]