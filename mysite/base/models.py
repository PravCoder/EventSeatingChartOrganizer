from django.db import models



class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    date =  models.CharField(max_length=200, null=True)
    info = models.CharField(max_length=200, null=True)
    # pre_registered_guests = Man

