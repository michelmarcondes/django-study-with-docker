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
    profile = request.user.profile
    projectForm = ProjectForm()

    #getting and validating sent data
    if request.method == 'POST':
        projectForm = ProjectForm(request.POST, request.FILES)
        if projectForm.is_valid():
            project = projectForm.save(commit=False)
            project.owner = profile #set logged user as project owner
            project.save()
            return redirect('account')


    context = {'form': projectForm}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    # project = Project.objects.get(id=pk)
    project = profile.project_set.get(id=pk) #ensure just owner can update his project
    projectForm = ProjectForm(instance=project)

    #getting and validating sent data
    if request.method == 'POST':
        projectForm = ProjectForm(request.POST, request.FILES, instance=project)
        if projectForm.is_valid():
            projectForm.save()
            return redirect('account')


    context = {'form': projectForm}
    return render(request, 'projects/project_form.html', context) 

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk) # ensure just owner can delete his project

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'delete_template.html', context)