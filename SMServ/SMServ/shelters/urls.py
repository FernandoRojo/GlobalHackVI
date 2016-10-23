from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.inbound_sms, name='index'),
]
