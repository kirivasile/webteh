from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/', views.question, name='question'),
    url(r'^add_question/', views.add_question, name='add_question'),
    url(r'^login/', views.login, name='login'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
]