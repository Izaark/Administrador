from django.conf.urls import url
from django.contrib import admin
from .views import CreateProjectClass

app_name = 'project'

urlpatterns = [
    url(r'^create/$', CreateProjectClass.as_view(), name='create'),

]