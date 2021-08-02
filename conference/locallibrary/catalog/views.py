
from django.shortcuts import render
from django.views import generic

import datetime

from .models import Presentation, Schedule, Room, UserProfile
from .forms import UserRegistrationForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    num_room = Room.objects.all().count()
    num_free_room = Room.objects.filter(busy=False).count()
    num_presentation = Presentation.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_room': num_room, 'num_presentation': num_presentation, 'num_free_room': num_free_room},
    )


class ScheduleListViews(generic.ListView):
    model = Schedule
    paginate_by = 10


class ScheduleDetailViews(generic.DetailView):
    model = Schedule


class PresentationViews(generic.ListView):
    model = Presentation


class PresentationDetailViews(generic.DetailView):
    model = Presentation


class RoomViews(generic.ListView):
    model = Room


class RoomDetailViews(generic.DetailView):
    model = Room


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'catalog/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'catalog/register.html', {'user_form': user_form})


class ScheduleCreate(CreateView):
    model = Schedule
    fields = ['room', 'presentation', 'start_date', 'end_date', 'author']
    initial = {'start_date': datetime.date.today()}


class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['room', 'presentation', 'start_date', 'end_date']


class ScheduleDelete(DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule')


class PresentationCreate(CreateView):
    model = Presentation
    fields = ['presentation_author', 'presentation_name']


class PresentationUpdate(UpdateView):
    model = Presentation
    fields = ['presentation_name', 'presentation_author']


class PresentationDelete(DeleteView):
    model = Presentation
    success_url = reverse_lazy('presentation')
