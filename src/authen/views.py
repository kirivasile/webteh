from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import *

# Create your views here.
def sign_up(request):
	if (request.method == 'POST'):
		form = UserForm(request.POST)
		if form.is_valid():
			myUser = MyUser.objects.generateByForm(form)
			if myUser == None:
				return redirect('index')
			myUser.save();
			myUser = authenticate(username=form.cleaned_data['login'], 
				password=form.cleaned_data['password'])
			login(request, myUser)
		return redirect('index')
	else:
		template = loader.get_template('registration/sign_up.html')
		form = UserForm()
		context = RequestContext(request, {
				"form": form,
			})
		return HttpResponse(template.render(context))
