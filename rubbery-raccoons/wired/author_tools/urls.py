from django.urls import path

from . import views as at_views

urlpatterns = [
    path("compose", at_views.compose, name="compose"),
    path("edit/<slug:slug>/", at_views.update, name="update"),
]
