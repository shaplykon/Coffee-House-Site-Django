from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^coffee/$', views.CoffeeView.as_view(), name='coffee'),
    re_path(r'^coffee/(?P<id>\d+)/$', views.detail_coffee, name='detail_coffee'),
    re_path(r'^dessert/(?P<id>\d+)/$', views.detail_dessert, name='detail_dessert'),
    re_path(r'^tea/(?P<id>\d+)/$', views.detail_tea, name='detail_tea'),
    re_path(r'tea/$', views.TeaView.as_view(), name='tea'),
    re_path(r'desserts/$', views.DessertsView.as_view(), name='desserts'),
    re_path(r'favourites/$', views.favourites, name='favourites')
]
