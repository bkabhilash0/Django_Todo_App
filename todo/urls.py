from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path('', views.index, name="index"),
    path('todos', views.getAllTodos, name="todos.index"),
    path('todos/create', views.createTodo, name="todos.create"),
    path('todo/toggle/<int:id>', views.toggleTodoState, name="todos.toggle"),
    path('todo/delete/<int:todo>', views.deleteTodo, name="todos.delete"),
    path('todo/update/<int:todo>', views.updateTodo, name="todos.update")
]
