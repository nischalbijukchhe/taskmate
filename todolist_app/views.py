from django.shortcuts import render, redirect
from django.http import HttpResponse #import http response
from todolist_app.models import TaskList
from todolist_app.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def todolist(request): #take parameter called request so if we need any information form browser or anything else it would carry along with this request
    if request.method =="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()

        messages.success(request,("New task added!"))
        return redirect('todolist')

    else:
         all_tasks= TaskList.objects.filter(manage=request.user)
         paginator = Paginator(all_tasks, 5)
         page = request.GET.get('pg')
         all_tasks = paginator.get_page(page)

         return render(request, 'todolist.html', {'all_tasks' : all_tasks}) #instead of dictionary we can pass context only

def index(request): #take parameter called request so if we need any information form browser or anything else it would carry along with this request
    context = {   #dictionary submit everythhing in this all the elemenet we want to pass
        'index_text' :"Welcome Index Page."
    }
    return render(request, 'index.html', context)

@login_required
def delete_task(request, task_id):
    task= TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
         task.delete()
    else:
        messages.error(request,("Access Restricted, You Are Not Allowed.")) 

    return redirect('todolist')

@login_required
def complete_task(request, task_id):
    task= TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,("Access Restricted, You Are Not Allowed."))    
    task.done = True
    task.save()
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task= TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')    

@login_required
def edit_task(request, task_id):
    if request.method =="POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
          form.save()

        messages.success(request,("Task Edited!"))
        return redirect('todolist')

    else:
         task_obj= TaskList.objects.get(pk=task_id)
         return render(request, 'edit.html', {'task_obj' : task_obj})    


def contact(request): #take parameter called request so if we need any information form browser or anything else it would carry along with this request
    context = {   #dictionary submit everythhing in this all the elemenet we want to pass
        'contact_text' :"Welcome contact us page."
    }
    return render(request, 'contact.html', context)

def about(request): #take parameter called request so if we need any information form browser or anything else it would carry along with this request
    context = {   #dictionary submit everythhing in this all the elemenet we want to pass
        'about_text' :"Welcome From about us page."
    }
    return render(request, 'about.html', context)