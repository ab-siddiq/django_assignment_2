from django.shortcuts import render,redirect
from tasks.forms import TaskForm
from tasks.models import TaskModel
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    task = TaskModel.objects.all()
    return render(request,"show_tasks.html",{"tasks":task})

def add_task(request):
    task = TaskForm(request.POST)
    if task.is_valid():
        task.save()
        print(task.cleaned_data)
        return redirect('show_tasks')
    else:
        task =  TaskForm()
        return render(request,"add_task.html",{"form":task})

def edit_task(request,id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request,'add_task.html',{'form':form})

def delete_task(request,id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('show_tasks')

def show_tasks(request):
    task = TaskModel.objects.all()
    return render(request,"show_tasks.html",{"tasks":task})

def completed_task(request):
    task = TaskModel.objects.all()
    return render(request,"complete_task.html",{"tasks":task})

def complete_task(request, id):
    task  = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('completed_task')

def repriotise_task(request, id):
    task  = TaskModel.objects.get(pk=id)
    task.is_completed = False
    task.save()
    return redirect('show_tasks')