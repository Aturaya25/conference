import uuid

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


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


class Schedule(models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, help_text="Unique ID for schedule")
    room = models.ForeignKey('Room', Room)
    presentation = models.ForeignKey('Presentation', Presentation, null=True)
    start_date = models.DateTimeField('Start date', null=True, blank=True)
    end_date = models.DateTimeField('End date', null=True, blank=True)
    author = models.CharField('Author', max_length=200)

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

