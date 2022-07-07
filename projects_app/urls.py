from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:proj_id>/", views.project_detail, name="project_detail"),
]