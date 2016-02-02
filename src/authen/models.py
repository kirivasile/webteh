from django.db import models
from django.contrib.auth.models import User
from questions.models import *

class MyUserManager(models.Manager):
	def generateByForm(self, form):
		try:
			user = User.objects.get(username=form.cleaned_data['login'])
			return None
		except User.DoesNotExist:
			user = User(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
			user.save()
			return MyUser(user=user, nick=form.cleaned_data['nick'])

class MyUser(models.Model):
	user = models.OneToOneField(User)
	nick = models.CharField(max_length=20)
	objects = MyUserManager()


