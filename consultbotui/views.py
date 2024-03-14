from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from consultbotui.models import Schedules
from .forms import ScheduleForm
from django.views.generic import ListView
from django.shortcuts import render
from .models import Event
from django.http import JsonResponse

class ScheduleCreateView(CreateView):
    model = Schedules
    form_class = ScheduleForm
    success_url = reverse_lazy('schedule_list')  # Укажите URL для перенаправления после создания


class ScheduleUpdateView(UpdateView):
    model = Schedules
    form_class = ScheduleForm
    success_url = reverse_lazy('schedule_list')  # Укажите URL для перенаправления после обновления


class ScheduleListView(ListView):
    model = Schedules
    template_name = 'schedule_list.html'  # Обновленный путь к шаблону

#For TUI Calendar https://ui.toast.com
def calendar_view(request):
    # Отображение страницы календаря
    return render(request, 'calendar.html')


def events_api(request):
    # API для получения событий календаря
    events = Event.objects.all().values('id', 'title', 'start_date', 'end_date', 'description')
    # Подготавливаем данные для соответствия формату, требуемому TUI Calendar
    events_data = [{
        'id': event['id'],
        'title': event['title'],
        'start': event['start_date'],
        'end': event['end_date'],
        'description': event['description']
    } for event in events]
    return JsonResponse(events_data, safe=False)
