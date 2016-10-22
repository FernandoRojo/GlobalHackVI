from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    context = {'login':login}
    return render(request, 'registration/base.html', context)

def logout(request):
    return render(request, 'registration/base.html')
