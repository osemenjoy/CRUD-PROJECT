from django.urls import path
from .views import StudentListView, StudentUpdateView

urlpatterns = [
    path("",StudentListView.as_view(), name = "student-list" ),
    path("edit/<int:pk>", StudentUpdateView.as_view(), name = "student-update"),
]