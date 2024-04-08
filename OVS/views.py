import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.shortcuts import HttpResponse
def home (request):
    return HttpResponse("Hello,django")
def launch(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
# Create your views here.

