from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from questions.models import *
from django.utils.http import *
from .forms import QuestionForm

# Create your views here.

def index(request):
	template = loader.get_template('index.html')
	try:
		tag_name = request.GET.get('tag', None)
		if (tag_name == None):
			question_data = Question.objects.sortedByDate()
			context = RequestContext(request, {
					"question_data" : question_data,
					"header_value" : "New questions",
					"another_header_value" : "Hot questions",
					"another_header_link": "index_hot",
					"tag_data" : Tag.objects.sortedByPopularity(),
				})
			return HttpResponse(template.render(context))
		else:
			tag = Tag.objects.get(name=tag_name)
			question_data = Question.objects.getByTag(tag)
			context = RequestContext(request, {
					"question_data" : question_data,
					"header_value" : "Tag: " + tag_name,
					"another_header_value" : "New questions",
					"another_header_link" : "index",
					"tag_data" : Tag.objects.sortedByPopularity(),
				})
			return HttpResponse(template.render(context))
	except Tag.DoesNotExist:
		return redirect("index")

def index_hot(request):
	template = loader.get_template('index.html')
	question_data = Question.objects.sortedByNumAnswers()
	context = RequestContext(request, {
			"question_data" : question_data,
			"header_value" : "Hot questions",
			"another_header_value" : "New questions",
			"another_header_link": 'index',
			"tag_data" : Tag.objects.sortedByPopularity(),
		})
	return HttpResponse(template.render(context))

def question(request):
	template = loader.get_template('question.html')
	question = Question.objects.get(id=request.GET.get('id', None))
	context = RequestContext(request, {
			"question" : question,
			"tag_data" : Tag.objects.sortedByPopularity(),
		})
	return HttpResponse(template.render(context))

def add_question(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			questionId = Question.objects.generateByForm(form, request.user)
			question = Question.objects.get(id=questionId)
			template = loader.get_template('question.html')
			context = RequestContext(request, {
					"question" : question,
					"tag_data" : Tag.objects.sortedByPopularity(),
				})
			return HttpResponse(template.render(context))
		else:
			return redirect("index")
	else:
		if (request.user.is_authenticated()):
			template = loader.get_template('add_question.html')
			form = QuestionForm()
			context = RequestContext(request, {
					"form": form,
					"tag_data" : Tag.objects.sortedByPopularity(),
				})
			return HttpResponse(template.render(context))
		else:
			response = redirect('my_login')
			response['Location'] += '?next=' + request.path
			return response

