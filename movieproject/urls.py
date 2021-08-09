from django.urls import path
from . import views

app_name = "movie_project"

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<str:movie_id>", views.detail, name="detail"),
]
