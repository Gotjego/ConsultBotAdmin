from django.urls import path
from .views import ScheduleListView, ScheduleCreateView, ScheduleUpdateView, calendar_view, events_api

urlpatterns = [
    path('', ScheduleListView.as_view(), name='schedule_list'),
    path('new/', ScheduleCreateView.as_view(), name='schedule_new'),
    path('edit/<int:pk>/', ScheduleUpdateView.as_view(), name='schedule_edit'),
    path('calendar/', calendar_view, name='calendar'),  # Отображение календаря
    path('api/events/', events_api, name='events_api'),  # API для событий
]