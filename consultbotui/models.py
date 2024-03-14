from django.db import models


class Accommodations(models.Model):
    note = models.CharField(max_length=25, blank=True, null=True)
    subcategory = models.ForeignKey('Subcategories', models.DO_NOTHING)
    duration = models.TimeField()
    break_time = models.TimeField()
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accommodations'


class Appointments(models.Model):
    created = models.DateTimeField(blank=True, null=True)
    schedule = models.ForeignKey('Schedules', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    accomodation = models.ForeignKey(Accommodations, models.DO_NOTHING)
    datetime = models.DateTimeField()
    communication_type = models.CharField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'
        unique_together = (('schedule', 'datetime'),)


class Schedules(models.Model):
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    note = models.CharField(max_length=25, blank=True, null=True)
    markup = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedules'
        unique_together = (('start_dt', 'end_dt'),)


class Services(models.Model):
    title = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'services'


class Subcategories(models.Model):
    title = models.CharField(unique=True, max_length=30)
    service = models.ForeignKey(Services, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'subcategories'


class Users(models.Model):
    telegram_id = models.BigIntegerField(blank=True, null=True)
    telegram_chat_id = models.BigIntegerField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    is_admin = models.BooleanField(blank=True, null=True)
    password = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('username', 'phone', 'telegram_id'),)

#For TUI Calendar https://ui.toast.com

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
