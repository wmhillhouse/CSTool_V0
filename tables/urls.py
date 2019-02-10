from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

# Application Name
app_name = 'tables'

urlpatterns = [
    # Administration Links
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    # List view links'
    path('documents', views.document_list, name='document-list'),
    path('instruments', views.instruments, name='instrument-list'),
    path('drives', views.drives, name='drive-list'),
    path('alarms', views.AlarmListView.as_view(), name='alarm-list'),
    # Details view links
    path('instruments/<str:tag>/', views.instrument_details, name='instrument-details'),
    path('drives/<str:tag>/', views.actuator_details, name='actuator-details'),
    # Create view links
    path('alarm/create',  login_required(views.AlarmCreate.as_view()), name='alarm-create')
]