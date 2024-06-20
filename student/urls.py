from django.urls import path
from .views import StudentListView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path("",StudentListView.as_view(), name = "student-list" ),
    path("edit/<int:pk>", StudentUpdateView.as_view(), name = "student-update"),
    path("delete/<int:pk>", StudentDeleteView.as_view(), name = "student-delete"),
]