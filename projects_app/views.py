from django.shortcuts import render
from projects_app.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, proj_id):
    project = Project.objects.get(pk=proj_id)
    context = {
        'project': project 
    }
    return render(request, 'project_detail.html', context)