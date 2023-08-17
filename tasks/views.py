from django.shortcuts import render,redirect
from tasks.forms import TaskForm
from tasks.models import TaskModel
# Create your views here.
def home(request):
    return render(request,"view_task.html")
def add_task(request):
    task = TaskForm(request.POST)
    if task.is_valid():
        task.save()
        print(task.cleaned_data)
        return redirect('view_task')
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
            return redirect('view_task')
    return render(request,'add_task.html',{'form':form})

def view_task(request):
    task = TaskModel.objects.all()
    return render(request,"view_task.html",{"tasks":task})
def completed_task(request):
    task = TaskModel.objects.all()
    return render(request,"complete_task.html",{"tasks":task})