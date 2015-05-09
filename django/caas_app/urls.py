from django.conf.urls import patterns, url
from caas_app import views

urlpatters = patterns('',
    url(r'^$', views.index, name='index')
)
