from django.contrib import admin
from .models import Employee, Room, Guest, Reservation, Checkins, Billing
# Register your models here.

admin.site.register(Employee)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Checkins)
admin.site.register(Billing)