from django.http import HttpResponse
from django.shortcuts import render
import json
from django.conf import settings
import os


# Create your views here.


def index(request):
    f = open(os.path.join(settings.BASE_DIR, 'static/json/infos.json'), 'r')

    return render(request, "cv/index.html", json.load(f))
