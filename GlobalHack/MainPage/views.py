from django.shortcuts import render
# Create your views here.                                                                 
from django.conf.urls import url
from django.http import HttpResponse, HttpRequest
# Create your views here.                                                                   
from rssfeed.models import Item
from rssfeed.feeds import ShelterFeed
import feedparser 


def index(request):
    return render(request, 'MainPage/index.html', {})
def home(request):
    feed = feedparser.parse(ShelterFeed().__call__(request).content)
    feed = feed['entries']
    return render(request,'MainPage/home-page.html',context = { 'entries' : feed })



