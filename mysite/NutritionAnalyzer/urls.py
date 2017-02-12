from django.conf.urls import url
from . import views  # imports the local views.py file

urlpatterns = [
    url(r'^$', views.index, name='index')]  # if the url remains ^$ then we're going to return the views.index
