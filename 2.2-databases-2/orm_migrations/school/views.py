from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {'object_list': Student.objects.all().prefetch_related('teacher')}
    ordering = 'group'

    return render(request, template, context)
