from django.shortcuts import render
from .models import *

major_tables = {"Aero/Mech":3,"Archi/Civil":3,"Elec":1,"Indus":1,"Env":1,"Bio":4,"Chem":3,"CS":3,"Deans/Chairmen/IndustryFriends":2}
max_constants = {"student":2, "professor":1, "mentor":1, "seats":8}

def home(request):
    all_events = Event.objects.all()
    context = {"all_events":all_events}
    return render(request, "base/home.html", context)

def view_event(request, pk):
    

    event = Event.objects.get(id=str(pk))
    if request.method == "POST":
        if request.POST.get("guest-register"):
            name = request.POST.get("name")
            email = request.POST.get("email")
            major = request.POST.get("major")
            person_type = request.POST.get("person-type")

            guest = Guest.objects.create(name=name, email=email, major=major, person_type=person_type)
            event.guests.add(guest)
            event.save()
            guest.save()

    context = {"event":event}
    return render(request, "base/view_event.html", context)

def create_event(request):
    if request.method == "POST":
        title = request.POST.get("event-title")
        info = request.POST.get("event-info")
        date = request.POST.get("event-date")
        event = Event.objects.create(title=title, info=info, date=date)
        c = SeatingChart.objects.create()
        c.save()
        event.chart = c
        event.save()
        event.chart.init_tables(major_tables, event)
        event.save()

    context = {}
    return render(request, "base/create_event.html", context)


"""
TODO:
- Editting for fornt desk person.

Write some HTML and CSS to view the seating chart of the event in which each table is displayed with the table name and
and each person seated at that table is displayed with their name, major, and person_type for that table, also display hte max_seats and seats avalible for each table.
Make it look clean adn easy to read. 
"""