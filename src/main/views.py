from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def question(request):
	template = loader.get_template('question.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def add_question(request):
	if (request.user.is_authenticated()):
		template = loader.get_template('add_question.html')
		context = RequestContext(request, {})
		return HttpResponse(template.render(context))
	else:
		return redirect("/login/")

def login(request):
	if (request.user.is_authenticated()):
		return redirect("/")
	else:	
		template = loader.get_template('login.html')
		context = RequestContext(request, {})
		return HttpResponse(template.render(context))

def sign_up(request):
	if (request.user.is_authenticated()):
		return redirect("/")
	else:	
		template = loader.get_template('sign_up.html')
		context = RequestContext(request, {})
		return HttpResponse(template.render(context))