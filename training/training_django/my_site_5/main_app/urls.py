from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("", views.index, name="index"),
    path("articles", views.articles, name="articles"),
    path("form", views.form, name="form"),
]