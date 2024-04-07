from django.urls import path
from OVS import views 

urlpatterns = [
    path("", views.home, name="home"),
]