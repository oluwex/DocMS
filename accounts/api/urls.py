from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserStaffAdminCreateAPIView,
    UserDetailAPIView,
    UserLoginAPIView,
    UserDeleteAPIView,
)

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^registeradmin/$', UserStaffAdminCreateAPIView.as_view(), name='adminregister'),
    url(r'^(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', UserDeleteAPIView.as_view(), name='delete'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
]
