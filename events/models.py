from django.db import models

from contacts.models import Contact, Address

""" Event system tables """


class Venue(models.Model):
    name = models.TextField(blank=False)
    address = models.ForeignKey(Address)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', 'address')


class EventType(models.Model):
    abbrev = models.CharField(max_length=6)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    table = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Event(models.Model):
    type = models.ForeignKey(EventType)
    description = models.TextField(blank=True)
    start = models.DateTimeField(blank=True)
    end = models.DateTimeField(blank=True)
    notes = models.TextField(blank=True, null=True)
    contacts = models.ManyToManyField(Contact)
    venues = models.ManyToManyField(Venue)

    def __str__(self):
        result = self.description
        if self.start:
            result += self.start.strftime("%Y %b")
        return result

    class Meta:
        ordering = ('-start', 'description')

