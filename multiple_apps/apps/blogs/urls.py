from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/new', views.new),
    url(r'^/create', views.create),
    url(r'^/numbers_route/(?P<parameter>\d+)$', views.show),
    url(r'^/numbers_route/(?P<parameter>\d+)/edit', views.edit),
    url(r'^/numbers_route/(?P<parameter>\d+)/delete', views.destroy),
    
    # url(r'^$', views.index),
]