from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', views.PostDetail, name='post_detail'),
    re_path(r'^new/', views.CreatePageView.as_view(), name='post_new'),
    re_path(r'^like/$', views.like_post, name='like_post')
]
