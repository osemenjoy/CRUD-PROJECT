from django.urls import path
from .views import StudentListView, StudentUpdateView

urlpatterns = [
    path("",StudentListView.as_view(), name = "student-list" ),
 
]