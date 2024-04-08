import re
from django.utils.timezone import datetime
from django.shortcuts import HttpResponse
def home (request):
    return HttpResponse("Hello,django")
def launch (request, name):
    now= datetime.now()
    formatted_now = now.strftime("%A,%d %B,%Y at %X")
# Create your views here.

