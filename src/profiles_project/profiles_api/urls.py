from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from profiles_api import views


urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
]
