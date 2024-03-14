from django.contrib import admin
from django.urls import path, include
from consultbotui.views import calendar_view, events_api  # Импортируйте events_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', include('consultbotui.urls')),  # Обновлено для корректного включения
    path('calendar/', calendar_view, name='calendar'),  # Путь к представлению календаря
    path('api/events/', events_api, name='events_api'),  # Добавьте эту строку для доступа к API
]
