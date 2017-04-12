from django.conf.urls import url,include
from django.contrib import admin
from .views import logout,LoginView,DashboardView,ShowView,Create,Edit,edit_password,edit_client

app_name = 'client'

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^Create/$', Create.as_view(), name='create'),
    url(r'^show/(?P<username_url>\w+)/$', ShowView.as_view(), name='show'),
    url(r'^edit/$', edit_client, name='edit'),
    url(r'^edit_password/$', edit_password, name='edit_password'),
    ]