from django.urls import HttpResponse
from OVS import views 

urlpatterns = [
    path("", views.home, name="home"),
]