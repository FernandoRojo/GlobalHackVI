from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Map$', views.Map, name = 'Map'),
    url(r'^NewShelter$', views.NewShelter, name = 'NewShelter'),
    url(r'^heatdata$', views.heatdata),
]
