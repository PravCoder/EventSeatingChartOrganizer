from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("view-event/<str:pk>", views.view_event, name="view-event"),

     path("create-event/", views.create_event, name="create-event")
    
]