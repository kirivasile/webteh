from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', name='my_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='my_logout'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
]