from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=200, null=True)
    email =  models.CharField(max_length=200, null=True)
    major =  models.CharField(max_length=200, null=True)
    person_type =  models.CharField(max_length=200, null=True)


class Table(models.Model):
    num_id = models.IntegerField(default=-1, null=True, blank=False)
    max_seats = models.IntegerField(default=-1, null=True, blank=False)
    label = models.CharField(max_length=200, null=True)
    seated_guests = models.ManyToManyField("Guest", related_name="seated_guests", blank=True)

    @property
    def get_guests(self):
        return len(list(self.seated_guests))
    @property
    def get_avalible(self):
        return self.max_seats-self.seated_guests.through.objects.count()
    
    def get_type_count(self, person_type):
        count = 0
        for guest in self.seated_guests.all():
            if guest.person_type ==  person_type:
                count += 1
        return count

class SeatingChart(models.Model):
    tables = models.ManyToManyField("Table", related_name="tables", blank=True)

    def init_tables(self, major_tables, event):
        cur_id = 1
        for major_name, num_tables in major_tables.items():
            for _ in range(num_tables):
                table = Table.objects.create(num_id=cur_id, max_seats=8, label=major_name)
                cur_id += 1
                event.chart.tables.add(table)
                event.save()
                table.save()

    def assign_guest(self, new_guest, max_constants):
        for table in self.tables.all():
            if table.label == new_guest.major:
                if table.get_type_count(new_guest.person_type) < max_constants[new_guest.person_type] and len(list(table.seated_guests.all())) < table.max_seats:
                    table.seated_guests.add(new_guest)
                    table.save()
                    new_guest.save()
                    return table
        return False


class Event(models.Model):

    title = models.CharField(max_length=200, null=True)
    date =  models.CharField(max_length=200, null=True)
    info = models.CharField(max_length=200, null=True)
    guests = models.ManyToManyField("Guest", related_name="guests", blank=True)
    chart = models.ForeignKey(SeatingChart, on_delete=models.SET_NULL,null=True, related_name="chart",blank=True)

