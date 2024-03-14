from django.contrib import admin
from consultbotui.models import Accommodations, Appointments, Schedules, Services, Subcategories, Users
from .models import Event


# Регистрация моделей для отображения в административной панели
admin.site.register(Accommodations)
admin.site.register(Appointments)
admin.site.register(Services)
admin.site.register(Subcategories)
admin.site.register(Users)
admin.site.register(Event)

@admin.register(Schedules)
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('start_dt', 'end_dt', 'note', 'markup')



