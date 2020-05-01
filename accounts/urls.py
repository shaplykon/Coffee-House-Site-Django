from django.contrib.auth.views import LogoutView
from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    re_path(r'^register/$', register_form, name='register'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^account/$', account_view, name='account'),
    re_path(r'^avatar/$', change_avatar, name='avatar'),
    re_path(r'^save-changes/$', save_changes, name='save_changes'),
    re_path(r'^upload-picture/$', change_avatar, name='upload_picture'),
    path('', include('django.contrib.auth.urls'))
]
