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
		try:
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username,password=password)
			if user is not None:
				state = "Welcome"
				auth.login(request,user)
				return HttpResponseRedirect('profile',{'state':state}) 	
			else:
				state = "Your are not registered.please register below"
		except Exception as formexe:
			
			state = str(formexe)
	return render_to_response('auth.html',{'state':state}, context_instance=RequestContext(request)) 		

def register_user(request):
	state = "You are not a registered user. Please register below"
	
	if request.method == 'POST':
		print "passed"
		form = RegForm(request.POST)
		try:
			username = request.POST['username']
			password = request.POST['password']
			email =request.POST['email']
			isA = request.POST['IsInterestedA']
			isB = request.POST['IsInterestedB']
			isC = request.POST['IsInterestedC']
			isD = request.POST['IsInterestedD']
			isE = request.POST['IsInterestedE']
			isF = request.POST['IsInterestedF']
			isG = request.POST['IsInterestedG']
			isH = request.POST['IsInterestedH']
			isI = request.POST['IsInterestedI']
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
				
				state = str(inst)
		except Exception as formexce:
				state = str(formexce)
	return render_to_response('auth.html',{'state':state}, context_instance=RequestContext(request))	

def forget_password(request):
	
	status = ""
	if request.method == 'POST':
		form = forgetpassword(form.cleaned_data)
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

def printmyinterests(request):
	if request.method == "GET":
		interested = []
		User.objects.filter(pub_date__year=2006)
def selectinterest(request,Skill):
	if request.method == "GET":
		specialinterest = User.objects.filter(Skill = True)
	return render_to_response('selectinterest.html',{'specialinterest':specialinterest}, context_instance=RequestContext(request))
	
def profile(request):
	

	specialinterest = ["Python","Software","Hacking","Linux","Holaa","kakaa","papaa"]
	for x in User.objects.all():
		try:
			if  not (isinstance(int(x),int) and not x  == "0"):
				print x
				specialinterest.append(x)
		except:
			pass
	return render_to_response('profile.html',{'username':"Rakesh",'interest':specialinterest}, context_instance=RequestContext(request))		
de(request):
	interestedusers = User.objects.get(city = User.city)
	return render_to_response('checkround.html',{'city':city , 'neighbourhood':neighbourhood},context_instance=RequestContext(request))
def checkedin(request):
	form = RegForm(request.GET)
	city = request.POST['city']
	neighbourhood = request.POST['neighbourhood']
	return render_to_response('profile.html',{'state':"Your Location has been shared and Your are now able to interact and make use of your time with the proffesional around you..and help others also."},context_instance=RequestContext(request,{}))