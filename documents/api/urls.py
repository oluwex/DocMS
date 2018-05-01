from django.conf.urls import url

from .views import DocumentUploadView

urlpatterns = [
    url(r'^upload/$', DocumentUploadView.as_view(), name='upload_doc'),
]