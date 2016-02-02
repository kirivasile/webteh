from django.db import models
from authen.models import MyUser
from django.utils import timezone
from django.db.models import Count
from .forms import QuestionForm
from django.contrib.auth.models import User
from authen.models import MyUser

class TagManager(models.Manager):
	def sortedByPopularity(self):
		return Tag.objects.annotate(question_count=Count('question')).order_by('-question_count')

class Tag(models.Model):
	name = models.CharField(max_length=20)
	objects = TagManager()

class QuestionManager(models.Manager):
	def sortedByDate(self):
		return Question.objects.all().order_by('-timestamp')

	def sortedByNumAnswers(self):
		return Question.objects.annotate(answer_count=Count('answers')).order_by('-answer_count')

	def getByTag(self, tag):
		return Question.objects.filter(tags__in =[tag])

	def generateByForm(self, form, user):
		result = Question()
		result.header = form.cleaned_data['title']
		result.value = form.cleaned_data['text']
		result.save()
		tagList = form.cleaned_data['tags'].split()
		for tag in tagList:
			try:
				tagObject = Tag.objects.get(name = tag)
			except Tag.DoesNotExist:
				tagObject = Tag.objects.create(name = tag)
			result.tags.add(tagObject)
		user = User.objects.get(username=user.username)
		result.author = MyUser.objects.get(user=user)
		result.save()
		return result.id


class Question(models.Model):
	header = models.CharField(max_length=100)
	value = models.CharField(max_length=500)
	timestamp = models.DateTimeField(default=timezone.now())
	author = models.ForeignKey(MyUser, related_name='questions',null=True)
	tags = models.ManyToManyField(Tag)
	likes = models.ManyToManyField(MyUser, through='Like')
	objects = QuestionManager()

class Answer(models.Model):
	value = models.CharField(max_length=500)
	author = models.ForeignKey(MyUser, related_name='answers', null=True)
	question = models.ForeignKey(Question, related_name='answers')

class Like(models.Model):
	value = models.IntegerField()
	author = models.ForeignKey(MyUser)
	question = models.ForeignKey(Question)