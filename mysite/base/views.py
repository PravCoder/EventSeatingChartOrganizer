from django.shortcuts import render
from .models import *

major_tables = {"Aero/Mech":3,"Archi/Civil":3,"Elec":1,"Indus":1,"Env":1,"Bio":4,"Chem":3,"CS":3,"Deans/Chairmen/IndustryFriends":2}
max_constants = {"student":2, "professor":1, "mentor":1, "seats":4}

def home(request):
    all_events = Event.objects.all()
    context = {"all_events":all_events}
    return render(request, "base/home.html", context)

def view_event(request, pk):

    event = Event.objects.get(id=str(pk))
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("guest-register") == "Submitted":
            print("GUEST REGISTER")
            name = request.POST.get("name")
            email = request.POST.get("email")
            major = request.POST.get("major")
            person_type = request.POST.get("person-type")

            guest = Guest.objects.create(name=name, email=email, major=major, person_type=person_type)
            event.guests.add(guest)
            event.save()
            guest.save()

            assigned_table = event.chart.assign_guest(guest, max_constants)

            event.save()
            guest.save()

        if request.POST.get("add-table") == "Submitted":
            print("ADD TABLE")
            table_name = request.POST.get("table-name")
            max_seats = int(request.POST.get("max-seats"))
            max_prof = int(request.POST.get("prof-num"))
            max_students = int(request.POST.get("student-num"))
            max_mentors = int(request.POST.get("mentor-num"))
            table_ids = [table.num_id for table in event.chart.tables.all() ]
            if len(table_ids) > 0:
                new_table = Table.objects.create(label=table_name,max_seats=max_seats,max_prof=max_prof,max_students=max_students,max_mentors=max_mentors,num_id=max(table_ids)+1)
            else:
                new_table = Table.objects.create(label=table_name,max_seats=max_seats,max_prof=max_prof,max_students=max_students,max_mentors=max_mentors,num_id=1)
            event.chart.tables.add(new_table)

            new_table.save()
            event.save()
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
        # event.chart.init_tables(major_tables, event)   # testing add tables
        event.save()

    context = {}
    return render(request, "base/create_event.html", context)


""" 
TODO:
- Editting for frnot desk person.
- User can type different types of people
- Error messages for edge cases for 
- only show avalible major tables

NOTE:
- in add table form table name as to match id of table major_tables = {"Aero/Mech":3,"Archi/Civil":3,"Elec":1,"Indus":1,"Env":1,"Bio":4,"Chem":3,"CS":3,"Deans/Chairmen/IndustryFriends":2}

Presentation:
When a guest arrives unregistered they scan a QR code which redirects them to this webpage.
This is the form the guests have to fill out to RSVP/pre-register. This is also the form that the guests did not RSVP and they arrive at the event. 
We have allocated a certain number of tables for each major. And we have a pre-defined number of students, prof, and mentors at each table. 
And when a guest submits a form we add them to the avalible table, an avalible table for a guest is a table that matches their major and if there is space
for that type of person at that table.


"""