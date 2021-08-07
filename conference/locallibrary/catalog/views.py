from django.contrib.auth.models import Group
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
import datetime

from .models import Presentation, Schedule, Room
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


def register_listener(request):
    listener = request.user.username
    if not Room.check_listener(request, listener):
        if Room.add_lstener_in_json(request, listener):
            status = 'Successfully registration'
            return render(
                request,
                'catalog/register_listener.html',
                context={'status': status}
            )
        else:
            status = ' No free places'
            return render(
                request,
                'catalog/register_listener.html',
                context={'status': status}
            )
    else:
        Room.delete_listener_in_json(request, listener)
        status = 'Successfully unsubscrible'
        return render(
                request,
                'catalog/register_listener.html',
                context={'status': status}
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
            new_user.groups.add(Group.objects.get(name='listener'))
            return render(request, 'catalog/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'catalog/register.html', {'user_form': user_form})


def refresh_page(request):
    if request.is_ajax():
        now = timezone.now()
        status = Schedule.check_status(request)
        context = {
            status
        }
        return render(request, "schedule_detail.html", context)


class ScheduleCreate(CreateView):
    model = Schedule
    fields = ['room', 'presentation', 'start_date', 'end_date', 'author']
    initial = {'start_date': datetime.date.today(),
               'end_date': datetime.date.today()}


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
