from django.shortcuts import render
from.models import Project


def list_projects(request):
    projects = Project.objects.all
    # filter(owner=request.user)
    context = {
        "list_projects": projects,
    }
    return render(request, "projects/list.html", context)
