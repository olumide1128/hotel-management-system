from django.db import models

# Create your models here.

class Employee(models.Model):

	DEPT_CHOICES = [
		('Front-Office','Front-Office'),
		('Housekeeping','Housekeeping'),
		('Accounts','Accounts'),
		('Maintenance','Maintenance'),
	]


	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	Address = models.CharField(max_length=150)
	dob = models.DateField()
	department = models.CharField(max_length=15, choices=DEPT_CHOICES)
	access_granted = models.BooleanField(default=False)


	def __str__(self):
		return self.first_name +' '+self.last_name+' - '+self.department


class Room(models.Model):
    
	ROOM_TYPES = [
		('Single','Single'),
		('Double','Double'),
		('Deluxe','Deluxe'),
		('Twin','Twin'),
		('Executive','Executive'),
	]

	ROOM_STATUS = [
		('Available','Available'),
		('Occupied','Occupied'),
		('Dirty','Dirty'),
		('Booked','Booked'),
	]


	room_num = models.IntegerField(primary_key=True)
	room_type = models.CharField(max_length=15, choices=ROOM_TYPES)
	room_price = models.FloatField()
	room_status = models.CharField(max_length=15, choices=ROOM_STATUS)


	def __str__(self):
		return "Room "+str(self.room_num)


class Guest(models.Model):
	guest_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	Address = models.CharField(max_length=150)
	card_num = models.CharField(max_length=50)
	card_cvv = models.CharField(max_length=10)
	card_expiry = models.CharField(max_length=20)


	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
	reserve_id= models.AutoField(primary_key=True)
	guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	checkin_date = models.DateField()
	checkout_date = models.DateField()
	Num_of_persons = models.IntegerField()


	def __str__(self):
		return f"Reserve Id: {self.reserve_id}, Reservation for Room {self.room.room_num}"