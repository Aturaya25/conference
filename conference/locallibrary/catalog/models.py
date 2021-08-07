import uuid
import os

from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.utils import timezone
import json


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_STATUS = (
        ('Admin', 'Admin'),
        ('Presenter', 'Presenter'),
        ('Listener', 'Listener'),
    )
    role = models.CharField(max_length=100, choices=ROLE_STATUS, blank=True, default='Listener', help_text='User role')


class Presentation(models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, help_text="Unique ID for presentation")
    created_date = models.DateField('Created date', null=True, blank=True, auto_now_add=True)
    presentation_author = models.CharField('Author', max_length=200)
    presentation_name = models.CharField('Presentation name', max_length=200)

    def __str__(self):
        return '%s, %s, %s' % (self.created_date, self.presentation_name, self.presentation_author)

    def get_absolute_url(self):
        return reverse('presentation-detail', args=[str(self.id)])

    class Meta:
        permissions = (("can_add_presentation", "Add presentation"),)


class Room(models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, help_text="Unique ID for room")
    room = models.CharField('Room', max_length=10)
    places = models.IntegerField('Places', default=30)
    free_places = models.IntegerField('Free places', default=30)
    busy = models.BooleanField('Busy', default=False)

    def __str__(self):
        return '%s' % self.room

    def get_absolute_url(self):
        return reverse('room-detail', args=[str(self.id)])

    def add_lstener_in_json(self, listener):
        with open(os.path.join('catalog/', 'register.json'), 'r') as reg:
            data = json.load(reg)
            reg_listener = {"listener": listener}
            data.append(reg_listener)
            with open(os.path.join('catalog/', 'register.json'), 'w') as outfile:
                json.dump(data, outfile)
        return True

    def delete_listener_in_json(self, listener):
        with open(os.path.join('catalog/', 'register.json'), 'r') as reg:
            data = json.load(reg)
        for i in range(len(data)):
            if data[i]['listener'] == listener:
                data.pop(i)
                break
        with open(os.path.join('catalog/', 'register.json'), 'w') as outfile:
            json.dump(data, outfile)

    def check_listener(self, listener):
        with open(os.path.join('catalog/', 'register.json'), 'r') as reg:
            flag = False
            data = json.load(reg)
            for i in range(len(data)):
                if not data[i]['listener'] == listener:
                    continue
                else:
                    flag = True
                    break
        return flag


class Schedule(models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, help_text="Unique ID for schedule")
    room = models.ForeignKey('Room', Room)
    presentation = models.ForeignKey('Presentation', Presentation, null=True)
    start_date = models.DateTimeField('Start date', null=True, blank=True)
    end_date = models.DateTimeField('End date', null=True, blank=True)
    author = models.CharField('Author', max_length=200)
    SCHEDULE_STATUS = (
        ('Completed', 'Completed'),
        ('Started', 'Started'),
        ('Finish', 'Finish'),
    )
    status = models.CharField('status', max_length=100, choices=SCHEDULE_STATUS, blank=True, default='Completed')

    def check_status(self):
        if self.start_date <= timezone.now() <= self.end_date:
            self.status = 'Started'
        elif self.end_date < timezone.now():
            self.status = 'Finish'
        else:
            self.status = 'Completed'
        return self.status

    def __str__(self):
        return '%s, %s, %s' % (self.room, self.author, self.presentation)

    def get_absolute_url(self):
        return reverse('schedule-detail', args=[str(self.id)])

    def active(self):
        now = timezone.now()
        if self.start_date < now < self.end_date:
            self.room.busy = True
        else:
            self.room.busy = False

    def all_listener(self):
        with open(os.path.join('catalog/', 'register.json'), 'r') as reg:
            data = json.load(reg)
            return len(data)
