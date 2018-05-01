from django.conf.urls import url

from .views import (
    UserCreateAPIView,
    UserStaffAdminCreateAPIView,
    UserDetailAPIView,
    UserLoginAPIView,
    UserDeleteAPIView,
    UserChangePasswordAPIView,
)

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^registeradmin/$', UserStaffAdminCreateAPIView.as_view(), name='adminregister'),
    # url(r'^(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<username>[a-z A-Z]+)/$', UserDetailAPIView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/delete/$', UserDeleteAPIView.as_view(), name='delete'),
    url(r'^(?P<username>[a-z A-Z]+)/delete/$', UserDeleteAPIView.as_view(), name='delete'),
    url(r'^(?P<username>[a-z A-Z]+)/ChangePassword/$', UserChangePasswordAPIView.as_view(), name='changepassword'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
]
