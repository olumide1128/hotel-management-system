from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

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



