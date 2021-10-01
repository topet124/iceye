from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import *

from .forms import *
# Create your views here.

def home(request):
    Lists = List_name.objects.all()
    entries = Entry.objects.all()
    

    form = TaskForm()


    context= {
    'entries': entries,
    'Lists'  : Lists,
    'form' : form,
    }
    
    return render(request, 'index.html',  context)


@require_POST
def addTodo(request):
    form = TaskForm(request.POST)
    #print(request.POST['text'])

    if form.is_valid():
       new_todo = List_name(name=request.POST['text'])
       new_todo.save()

    return redirect('/')
    


def deleteTask(request, pk):
    item = List_name.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)




 
