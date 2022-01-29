from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectForm

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    
    return render(request, 'projects/single-project.html', {'project': projectObj})

@login_required(login_url='login')
def createProject(request):
    projectForm = ProjectForm()

    #getting and validating sent data
    if request.method == 'POST':
        projectForm = ProjectForm(request.POST, request.FILES)
        if projectForm.is_valid():
            projectForm.save()
            return redirect('projects')


    context = {'form': projectForm}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    projectForm = ProjectForm(instance=project)

    #getting and validating sent data
    if request.method == 'POST':
        projectForm = ProjectForm(request.POST, request.FILES, instance=project)
        if projectForm.is_valid():
            projectForm.save()
            return redirect('projects')


    context = {'form': projectForm}
    return render(request, 'projects/project_form.html', context) 

@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)