from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
from .models import Item
from .feeds import ShelterFeed

import feedparser

def index(request):
    return render(request, 'rssfeed/index.html');


def rss(request):
    return render(request, 'rssfeed/XML.xml')

def viewfeed(request,rss):
    feed = feedparser.parse(ShelterFeed().__call__(request).content)
    feed = feed['entries']
    return render(request,'rssfeed/feed.html',context = { 'entries' : feed })

def post(request, postid):
   mycomment = Item.objects.get(id = postid)
   text = '<strong>Shelter :</strong> %s <p>'%mycomment.Title
   text += '<strong>Comment :</strong> %s <p>'%mycomment.description
   return HttpResponse(text)
