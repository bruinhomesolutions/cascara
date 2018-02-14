from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.graph, name='graph'),
    url(r'^api/value_over_time', views.value_over_time, name='value_over_time'),
]