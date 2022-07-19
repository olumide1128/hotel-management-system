import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Employee, Room

# Create your views here.

@login_required(login_url='/login')
def home(request):

	user_name = request.user.username

	if user_name == "admin":
		return render(request, 'admin_home.html', {})
	else:
		return render(request, 'home.html', {})


def user_login(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		if username != "" and password != "":
			user = authenticate(username=username, password=password) #authenticate details

			if user is not None:
				login(request, user) #Login user

				return redirect('/')
			else:
				messages.error(request, 'Invalid Username and/or Password!')
				return redirect('/login')
		else:		
			messages.error(request, 'Username and Password Required!')
			return redirect('/login')
		
	else:
		return render(request, 'login.html', {})


@login_required(login_url='/login')
def manage_staff_view(request):

	employees = Employee.objects.all().order_by('id')

	context = {'employees':employees}

	return render(request, 'staff_mgt/manage_staff.html', context)



@login_required(login_url='/login')
def update_staff_view(request, id):

	if request.method == 'POST':
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		address = request.POST.get('address')
		dob = request.POST.get('dob')
		dept = request.POST.get('department')

		old = Employee.objects.get(id=id)
		old.first_name = firstname
		old.last_name = lastname
		old.email = email
		old.Address = address
		old.dob = dob
		old.department = dept

		old.save()

		return redirect('/staff_mgt')

	employee = Employee.objects.get(id=id)
	emp_birth_date = str(employee.dob)

	context = {'employee':employee, 'emp_birth_date':emp_birth_date}

	return render(request, 'staff_mgt/update_staff.html', context)


@login_required(login_url='/login')
def delete_staff_view(request, id):
	employee = Employee.objects.get(id=id)
	employee.delete()

	return redirect('/staff_mgt')


@login_required(login_url='/login')
def add_staff_view(request):
	if request.method == 'POST':

		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		address = request.POST.get('address')
		dob = request.POST.get('dob')
		dept = request.POST.get('department')

		new_employee = Employee.objects.create(first_name=firstname, last_name=lastname, email=email, Address=address, dob=dob, department=dept)
		new_employee.save()

		return redirect('/staff_mgt')


@login_required(login_url='/login')
def access_mgt_view(request):

	front_emp = Employee.objects.filter(department='Front-Office').order_by('id')
	context = {"front_emp": front_emp}

	return render(request, "access_mgt/access_mgt_page.html", context)


def grant_access_view(request, id):
	old = Employee.objects.get(id=id)
	
	#Change granted access status
	old.access_granted = True
	old.save()

	firstname = old.first_name
	lastname = old.last_name
	email = old.email
	username = firstname[0].upper()+lastname.lower()
	password = generate_pass()

	print(username, " : ", password)

	#store to txt file
	with open('details.txt', 'a') as f:
		f.write(username+":"+password+"\n")

	#Create User account for this Employee
	User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
	return redirect('/access_mgt')


#Generate Password Method
def generate_pass():
      
    # Takes random choices from
    # ascii_letters and digits
    access_pass = ''.join([random.choice(
                        string.ascii_letters + string.digits)
                        for n in range(6)])
                          
    return access_pass
  

def revoke_access_view(request, id):
	emp = Employee.objects.get(id=id)
	
	#Change granted access status
	emp.access_granted = False
	emp.save()

	#Find and Delete User instance
	user = User.objects.filter(first_name=emp.first_name, last_name=emp.last_name)
	user.delete()

	return redirect('/access_mgt')



@login_required(login_url='/login')
def manage_room_view(request):
    	
	if request.method == 'GET' and 'q' in request.GET:
		q = request.GET['q']
		if q is not None and q != '':
			rooms = Room.objects.filter(room_num=q)
			if not rooms:	
				messages.warning(request, "Room not found!")
	else:
		rooms = Room.objects.all().order_by('room_num')


	context = {'rooms':rooms}
	return render(request, 'room_mgt/manage_room.html', context)



@login_required(login_url='/login')
def delete_room_view(request, id):
	room = Room.objects.get(room_num=id)
	room.delete()

	return redirect('/room_mgt')



@login_required(login_url='/login')
def update_room_view(request, id):

	if request.method == 'POST':
		roomNum = int(request.POST.get('roomNum'))
		roomPrice = float(request.POST.get('roomPrice'))
		roomType = request.POST.get('roomType')

		old = Room.objects.get(room_num=id)
		old.room_num = roomNum
		old.room_price = roomPrice
		old.room_type = roomType

		old.save()
		return redirect('/room_mgt')

	room = Room.objects.get(room_num=id)

	context = {'room':room}

	return render(request, 'room_mgt/update_room.html', context)


@login_required(login_url='/login')
def add_room_view(request):
	if request.method == 'POST':
		roomNum = int(request.POST.get('roomNum'))
		roomPrice = float(request.POST.get('roomPrice'))
		roomType = request.POST.get('roomType')

		new_room = Room.objects.create(room_num=roomNum, room_price=roomPrice, room_type=roomType, room_status='Available')
		new_room.save()

		return redirect('/room_mgt')


@login_required(login_url='/login')
def available_rooms_view(request):
		
	if request.method == 'GET' and 'q' in request.GET:
		q = request.GET['q']
		if q is not None and q != '':
			rooms = Room.objects.filter(room_num=q, room_status='Available')
			if not rooms:	
				messages.warning(request, "Room not found!")	
	else:
		rooms = Room.objects.filter(room_status='Available').order_by('room_num')
		if not rooms:	
			messages.warning(request, "No Available Room!")
	
	context = {'rooms':rooms}
	return render(request, 'regular_staff_templates/available_rooms.html', context)


@login_required(login_url='/login')
def dirty_rooms_view(request):
		
	if request.method == 'GET' and 'q' in request.GET:
		q = request.GET['q']
		if q is not None and q != '':
			rooms = Room.objects.filter(room_num=q, room_status='Dirty')
			if not rooms:	
				messages.warning(request, "Room not found!")	
	else:
		rooms = Room.objects.filter(room_status='Dirty').order_by('room_num')
		if not rooms:	
			messages.warning(request, "No Dirty Room!")
	
	context = {'rooms':rooms}
	return render(request, 'regular_staff_templates/dirty_rooms.html', context)