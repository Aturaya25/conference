from functools import update_wrapper

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View

from .models import Presentation, Schedule, Room, UserProfile


class PresentationAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'presentation_name', 'presentation_author']


admin.site.register(Presentation, PresentationAdmin)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room', 'places', 'free_places', 'busy')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('room', 'author', 'presentation', 'start_date', 'end_date', 'status')
    fields = ['room', 'author', 'presentation', 'status', ('start_date', 'end_date')]


#admin.site.register(UserProfile)


class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fk_name = 'user'


class UserProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserProfileAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)


