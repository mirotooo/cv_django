from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.


def index(request):
    f = open('cv/json/infos.json', 'r')

    return render(request, "cv/index.html", json.load(f))
