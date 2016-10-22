from django.conf.urls import url
from .feeds import ShelterFeed
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rss', ShelterFeed()),
    url(r'^viewfeed', views.viewfeed, { 'rss' : ShelterFeed() }, name = 'viewfeed'),
    url(r'^item/(?P<postid>\w+)/', views.post, name = 'rssitem'),
]
