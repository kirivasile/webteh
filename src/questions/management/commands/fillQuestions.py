from django.core.management import BaseCommand
from questions.models import *
from authen.models import *
from django.contrib.auth.models import User
import random

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
	def handle(self, *args, **options):
		user2 = User.objects.get(username='Artyom')
		myuser = MyUser.objects.get(user=user2)
		listTags = ["Java", "C++", "C#"]
		for i in range (0,20):
			q = Question(header=("Template question#" + str(i)), value="Hi, it is a template question #" + str(i))
			user = User.objects.get(username='Kirill')
			myuser = MyUser.objects.get(user=user)
			q.author = myuser
			q.save()
			count = random.randint(1,5)
			for j in range(count):	
				a = Answer(value="Template answer#" + str(j), author=myuser, question=q)
				a.save()
			firstTag = i % 3;
			secondTag = (i + 1) % 3
			q.tags.add(Tag.objects.get(name=listTags[firstTag]))
			q.tags.add(Tag.objects.get(name=listTags[secondTag]))
			q.save()