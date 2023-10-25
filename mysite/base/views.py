from django.shortcuts import render
from .models import *

def home(request):
    all_events = Event.objects.all()
    context = {"all_events":all_events}
    return render(request, "base/home.html", context)

def view_event(request, pk):
    event = Event.objects.get(id=str(pk))

    context = {"event":event}
    return render(request, "base/view_event.html", context)

def create_event(request):
    if request.method == "POST":
        title = request.POST.get("event-title")
        info = request.POST.get("event-info")
        date = request.POST.get("event-date")
        event = Event.objects.create(title=title, info=info, date=date)
        event.save()

    context = {}
    return render(request, "base/create_event.html", context)