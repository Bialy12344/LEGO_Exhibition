from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_user", views.add_user, name="add_user"),
    path("users", views.users, name="users"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("user_page", views.user_page, name="user_page"),
]
