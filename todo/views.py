from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Todo


# Create your views here.


def index(request: HttpRequest):
    # return HttpResponse("Hello World")
    return render(request, "todo/home.html", )


@login_required
def getAllTodos(request: HttpRequest):
    user = User.objects.get(pk=request.user.pk)
    todos = user.todo_set.all()
    # todos = Todo.objects.all()

    return render(request, 'todo/todos.html', {"todos": todos})


@login_required
def createTodo(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'todo/todo.add.html')
    if request.method == 'POST':
        try:
            todo = request.POST['todo']
            Todo.objects.create(todo=todo, user=User.objects.get(pk=request.user.pk)).save()
            messages.add_message(request, messages.SUCCESS, "Todo Added Successfully!")
            return HttpResponseRedirect(reverse("todos:todos.index"))
        except Exception as e:
            messages.add_message(request, messages.ERROR, "Something Went Wrong!")
            print("Sample")
            return render(request, 'todo/todo.add.html')


@login_required
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


@login_required
def updateTodo(request: HttpRequest, todo):
    todo = get_object_or_404(Todo, pk=todo)
    if request.method == "GET":
        return render(request, 'todo/todo.add.html', {'todo': todo})
    if request.method == "POST":
        try:
            updated_todo = request.POST['todo']
            todo.todo = updated_todo
            todo.save()
            messages.success(request, "Todo Updated Successfully!")
            return HttpResponseRedirect(reverse("todos:todos.index"))
        except Exception as e:
            messages.error(request, "Error Updating Todo")
            return render(request, "todo/todo.add.html", {'todo': todo})


@login_required
def deleteTodo(request, todo):
    todo = get_object_or_404(Todo, pk=todo)
    try:
        todo.delete()
        messages.add_message(request, messages.SUCCESS, "Todo Deleted Successfully!")
        return HttpResponseRedirect(reverse("todos:todos.index"))
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something Went Wrong!")
        return render(request, 'todo/todos.html')
