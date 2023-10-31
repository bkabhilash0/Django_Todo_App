from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib import messages
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request: HttpRequest):
    # blogs = range(13)
    blogs = Blog.objects.filter(status="A")
    return render(request, "blog/blog.index.html", {'blogs': blogs})


@login_required
def createBlog(request: HttpRequest):
    if request.method == "GET":
        form = BlogForm()
        return render(request, "blog/blog.add.html", {"form": form})
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            messages.success(request, "Blog Added Successfully!")
            return redirect("blog:blog.index")
        else:
            return render(request, "blog/blog.add.html", {"form": form})


@login_required
def updateBlog(request: HttpRequest, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if not blog.user.id == request.user.id:
        return redirect("blog:blog.index")
    if request.method == 'GET':
        form = BlogForm(instance=blog)
        return render(request, "blog/blog.update.html", {"form": form})
    if request.method == 'POST':
        clear_image = request.POST.get('image-clear')
        # if clear_image:
        #     blog.image = None
        form = BlogForm(request.POST, request.FILES, instance=blog)
        print(form.errors)
        # if clear_image:
        #     form = form.save(commit=False)
        #     form['image'] = None
        if form.is_valid():
            form.save()
            messages.success(request, "Blog Updated Successfully!")
            return redirect("blog:blog.index")
        else:
            return render(request, "blog/blog.update.html", {"form": form})


@login_required
def deleteBlog(request: HttpRequest, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if not blog.user.id == request.user.id:
        return redirect("blog:blog.index")
    try:
        blog.delete()
        messages.success(request, "Blog Deleted Successfully!")
        return redirect("blog:blog.index")
    except:
        messages.error(request, "Error Deleting Blog!")
        return redirect("blog:blog.index")


def viewBlog(request: HttpRequest, pk):
    blog = get_object_or_404(Blog, pk=pk, status="A")
    return render(request, "blog/blog.show.html", {"blog": blog})


@login_required
def likeBlog(request: HttpRequest, pk):
    user = request.user
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "GET":
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        return render(request, "blog/blog.show.html", {"blog": post})
