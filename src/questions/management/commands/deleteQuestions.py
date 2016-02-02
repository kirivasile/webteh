from django.core.management import BaseCommand
from questions.models import *
from authen.models import *
from django.contrib.auth.models import User
import random

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
	def handle(self, *args, **options):
		for i in range(0,20):
			q = Question.objects.get(header=("Template question#" + str(i)))
			q.delete()