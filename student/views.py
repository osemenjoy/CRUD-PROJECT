from django.views.generic import ListView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy


class StudentListView(ListView):
    model = Student
    template_name = "student-list.html"


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student-update.html"

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student-delete.html"
    success_url = reverse_lazy("student-list")