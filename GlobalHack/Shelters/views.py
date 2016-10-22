
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import ShelterForm
from .models import MakeShelter
# Create your views here.
import feedparser

def index(request):
    return render(request, 'rssfeed/index.html');
def Map(request):
    return render(request, 'Shelters/heatmap.html');

def NewShelter(request):
    if request.method == 'POST':
        form = ShelterForm(request.POST)
        if form.is_valid() and MakeShelter(form.data):
            return HttpResponse("Thanks");
    else:
        form = ShelterForm();
    return render(request, 'Shelters/NewShelter.html', {'form': form})


