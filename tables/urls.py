from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

# Application Name
app_name = 'tables'

urlpatterns = [
    # Administration Links
    url(r'^home/$', views.user_login, name='user_login'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    # List view links'
    path('<str:table_name>', views.generic_list, name='list'),
    # path('documents', views.document_list, name='document-list'),
    # path('instruments2', views.instruments, name='instrument-list'),
    # path('drives2', views.drives, name='drive-list'),
    # path('alarms2', views.AlarmListView.as_view(), name='alarm-list'),
    # Details view links
    path('<str:table_name>/<str:tag>', views.generic_details, name='details'),
    path('instruments/<str:tag>/', views.instrument_details, name='instrument-details'),
    path('drives/<str:tag>/', views.actuator_details, name='actuator-details'),
    # Create view links
    path('alarm/create',  login_required(views.AlarmCreate.as_view()), name='alarm-create')
]