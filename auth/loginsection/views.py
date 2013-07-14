import base64
import hashlib
import random
import sys
import traceback
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from loginsection.forms import *
from django.core.mail import send_mail
from loginsection.models import Userprofile
from django.template import RequestContext 
#from django.contrib.auth.views import *
here = "nowhere"
def login_user(request):
	state = "please login into to your account"
	if request.method == 'POST' :
		form = LoginForm(request.POST)
		if form.is_valid() :
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = auth.authenticate(username=username,password=password)
			if user is not None:
				state = "Welcome"
				auth.login(request,user)
				return render_to_response('userprof.html',{'state':state}, context_instance=RequestContext(request)) 	
			else:
				state = "Your are not registered.please register below"
		else:
			
			state = "Your entered invalid details."
	return render_to_response('auth.html',{'state':state}, context_instance=RequestContext(request)) 		

def register_user(request):
	state = "You are not a registered user. Please register below"
	
	if request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid() :
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			
			try:
				user= User.objects.create_user(username=username,password=password,email=email)
				
				user.save()
				user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
				
				if user is not None:
				
					# send_mail(
						# 'Welcome to CrowdBeans',
						# 'Welcome to CrowdBeans.com! Your username is %s and your app key is:\n %s' % (user.username, auth_key),
						# 'rakeshnitcalicut@gmail.com',
						# [user.email])
					
					auth.login(request,user)
					state = "Thank you for registiring.Welcome"
				else:
					state = "The Details you provided are wrong. Please Enter your Details correctly"
			except Exception as inst:
				
				state = "Username/Email already exists. Please select another username"
	return render_to_response('auth.html',{'state':state}, context_instance=RequestContext(request))	

def forget_password(request):
	
	status = ""
	if request.method == 'POST':
		form = forgetpassword(request.POST)
		if form.is_valid() :
			email = form.cleaned_data['email']
			try:
				user = User.objects.get(email = email)
				message1 = "please go to the following link to reset your password %s" %('http://127.0.0.1:8000/resetpassword')
				if user is not None:
					send_mail(
									'Request for change/forget password',
							
									message1,
									'rakeshnitcalicut@gmail.com',
									[user.email])
					status = "Link to change your password has been sent to your mail"
				else:
					status = "Your are not a registered user.please Register first"
			except:
				status = "Your are not a registered user.please Register first"
	return render_to_response('forgetpassword.html',{'status':status}, context_instance=RequestContext(request))

