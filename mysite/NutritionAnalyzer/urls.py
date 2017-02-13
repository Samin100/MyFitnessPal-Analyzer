from django.conf.urls import url, include
from . import views  # imports the local views.py file

urlpatterns = [
    url(r'^$', views.index, name='index'),
    ]  # if the url is regex ^$ then we're going to return the views.index
