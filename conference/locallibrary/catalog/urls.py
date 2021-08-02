from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^schedule/$', views.ScheduleListViews.as_view(), name='schedule'),
    path(r'^schedule/(?P<pk>\d+)$', views.ScheduleDetailViews.as_view(), name='schedule-detail'),
    url(r'^presentation/$', views.PresentationViews.as_view(), name='presentation'),
    path(r'^presentation/(?P<pk>\d+)$', views.PresentationDetailViews.as_view(), name='presentation-detail'),
    path(r'^room/(?P<pk>\d+)$', views.RoomDetailViews.as_view(), name='room-detail'),
    url(r'^room/$', views.RoomViews.as_view(), name='room'),
    url(r'^register/$', views.register, name='register'),
]

urlpatterns += [
    url(r'^schedule/create/$', views.ScheduleCreate.as_view(), name='schedule_create'),
    path(r'^schedule/(?P<pk>\d+)$/update/$', views.ScheduleUpdate.as_view(), name='schedule_update'),
    path(r'^schedule/(?P<pk>\d+)$/delete/$', views.ScheduleDelete.as_view(), name='schedule_delete'),
]
urlpatterns += [
    url(r'^presentation/create/$', views.PresentationCreate.as_view(), name='presentation_create'),
    path(r'^presentation/(?P<pk>\d+)$/update/$', views.PresentationUpdate.as_view(), name='presentation_update'),
    path(r'^presentation/(?P<pk>\d+)$/delete/$', views.PresentationDelete.as_view(), name='presentation_delete'),
]
#urlpatterns += path('registerListener/', views.registerListener, name='registerListener')
