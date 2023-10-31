from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="blog.index"),
    path("create", views.createBlog, name="blog.create"),
    path("<int:pk>", views.viewBlog, name="blog.show"),
    path("edit/<int:pk>", views.updateBlog, name="blog.edit"),
    path("delete/<int:pk>", views.deleteBlog, name="blog.delete"),
    path("like/<int:pk>", views.likeBlog, name="blog.like"),
]
