from django.conf.urls import url
from . import views
from tables.views import CtrlObject
from django.urls import path

urlpatterns = [
    # path('all', CtrlObject.as_view(), name='general_table'),
    path('instruments', views.instruments, name='instruments'),
    path('drives', views.drives, name='drives'),
    path('instruments/<str:tag>/', views.instrument_details, name='instrument_details'),
    path('drives/<str:tag>/', views.actuator_details, name='actuator_details'),
    # path('create', views.create, name='create')
    path('alarm/create',  views.AlarmCreate.as_view(), name='alarm-create')
]