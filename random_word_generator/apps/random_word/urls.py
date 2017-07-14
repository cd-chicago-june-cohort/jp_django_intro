from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate', views.gen_num),
    url(r'^reset', views.reset_attempts)
]