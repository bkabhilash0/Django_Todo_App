from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Todo


# Create your views here.


def index(request: HttpRequest):
    # return HttpResponse("Hello World")
    return render(request, "todo/home.html", )


def getAllTodos(request: HttpRequest):
    res = range(1, 15)
    todos = Todo.objects.all()

    return render(request, 'todo/todos.html', {"todos": todos})


def createTodo(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'todo/todo.add.html')
    if request.method == 'POST':
        try:
            todo = request.POST['todo']
            Todo.objects.create(todo=todo).save()
            messages.add_message(request, messages.SUCCESS, "Todo Added Successfully!")
            return HttpResponseRedirect(reverse("todos:todos.index"))
        except Exception as e:
            messages.add_message(request, messages.ERROR, "Something Went Wrong!")
            print("Sample")
            return render(request, 'todo/todo.add.html')


def toggleTodoState(request: HttpRequest, id):
    todo = get_object_or_404(Todo, pk=id)
    try:
        if todo.completed:
            todo.completed = False
        else:
            todo.completed = True
        todo.save()
        messages.add_message(request, messages.SUCCESS, "Todo Updated Successfully!")
        return HttpResponseRedirect(reverse("todos:todos.index"))
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something Went Wrong!")
        return render(request, 'todo/todos.html')


def deleteTodo(request, todo):
    todo = get_object_or_404(Todo, pk=todo)
    try:
        todo.delete()
        messages.add_message(request, messages.SUCCESS, "Todo Deleted Successfully!")
        return HttpResponseRedirect(reverse("todos:todos.index"))
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something Went Wrong!")
        return render(request, 'todo/todos.html')
