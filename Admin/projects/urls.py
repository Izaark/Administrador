from django.conf.urls import url
from django.contrib import admin
from .views import CreateProjectClass,ListClass, ShowClass,edit

app_name = 'project'

urlpatterns = [
    url(r'^create/$', CreateProjectClass.as_view(), name='create'),
    url(r'^my/projects/$', ListClass.as_view(), name='name_projects'),
    url(r'^show/(?P<slug>[\w-]+)/$', ShowClass.as_view(), name='show'),
    url(r'^edit/(?P<slug>[\w-]+)/$', edit, name='edit'),


]