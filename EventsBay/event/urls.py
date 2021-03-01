from django.urls import path
from . import views

app_name = "event"
urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
    path("login/", views.logIn, name="login"),
    path("logout/", views.logOut, name="logout"),
    path("create/", views.createEvent, name="createEvent"),
    path("liked/", views.likedEvents, name="likedEvents"),
    path('like/', views.like, name="like")
]

