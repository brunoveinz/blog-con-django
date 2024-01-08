from django.shortcuts import render
# httpresonse para devolver string
from django.http import HttpResponse, JsonResponse  # json para devolver json
from .models import Project, Taks  # import models
from django.shortcuts import render, redirect  # para renderizar html
from django.shortcuts import get_object_or_404  # manejar 404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def hello(request, username):
    # asi se concatena en django
    return HttpResponse("<h1>hello %s</h1>" % username)


def about(request):
    username = 'bruno'
    return render(request, 'about.html', {'username': username})


def index(request):
    title = "Welcome to Django app"
    return render(request, 'index.html', {'title': title})


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task= (get_object_or_404(Taks, id=id ) )
    tareas = Taks.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tareas': tareas
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Taks.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        print(request.POST)
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    #esta es la manera de buscar algo y ya manejando el error 404
    project = get_object_or_404(Project, id=id)
    tasks = Taks.objects.filter(project_id=id)
    print(project)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })