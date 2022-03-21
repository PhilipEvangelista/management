from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list-client/", views.list_client, name='list-client'),
    path("profile/<str:pk>/", views.profile, name="profile"),
    path("status/", views.status, name='status'),
    path("secure/", views.secure, name='secure'),
    path("secure/owner/", views.owner, name='owner'),
    path("edit/<str:pk>/", views.edit, name='edit-item'),
    path("update/<str:pk>?", views.update, name="update-item"),
    path("delete/<str:pk>?", views.delete, name="delete-item"),
    path("create-account/", views.create, name="create-account")
]