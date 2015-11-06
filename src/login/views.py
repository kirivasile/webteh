from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def my_login(request):
	#first_user = User.objects.create_user('Kirill', '', '123')
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect("/")
		else:
			template = loader.get_template('login_error.html')
			context = RequestContext(request, {
					'error_message': "Account has been disabled"
			})
	else:
		template = loader.get_template('login_error.html')
		context = RequestContext(request, {
				'error_message': "Incorrect username or password"
		})
	return HttpResponse(template.render(context))

def my_logout(request):
	logout(request)
	return redirect("/")


