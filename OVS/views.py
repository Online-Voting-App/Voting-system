from django.shortcuts import HttpResponse
def home (request):
    return HttpResponse("Hello,django")

# Create your views here.