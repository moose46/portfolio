from django.shortcuts import render

from projects.models import Project


# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    print(f"======= {pk} ==========")
    project = Project.objects.get(pk=pk)
    print(f"======= {project} {pk} ==========")
    context = {
        "project": project
    }
    print(f"======= context={context} pk={pk} ==========")
    request(request, "project_detail.html", context)
