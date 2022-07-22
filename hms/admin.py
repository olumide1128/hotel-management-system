from django.contrib import admin
from .models import Employee, Room, Guest, Reservation, Checkins
# Register your models here.

admin.site.register(Employee)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Checkins)