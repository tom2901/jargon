from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.index, name='register'),
    url(r'^main/$', views.index, name='main'),
    url(r'^train/$', views.index, name='train'),
]
