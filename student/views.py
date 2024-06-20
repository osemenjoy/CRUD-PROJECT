from django.views.generic import ListView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy


class StudentListView(ListView):
    model = Student
    template_name = "student-list.html"
    context_object_name = "students"


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student-update.html"
    fields = ["first", "last", "email", "phone", "location", "hobby", "course"]

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student-delete.html"
    success_url = reverse_lazy("student_list")