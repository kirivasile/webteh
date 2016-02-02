from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hot/', views.index_hot, name='index_hot'),
    url(r'^question/', views.question, name='question'),
    url(r'^add_question/', views.add_question, name='add_question'),
]