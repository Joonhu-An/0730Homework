from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone


def main(request):
    post = Post.objects
    return render(request, "main.html", {"post": post})


def new(request):
    return render(request, "new.html")


def create(request):
    post = Post()
    post.title = request.GET["title"]
    post.body = request.GET["body"]
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect("/detail/" + str(post.id))


def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, "detail.html", {"post": post})


def update(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    post.title = request.GET["title"]
    post.body = request.GET["body"]

    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect("/detail/" + str(post.id))


def delete(request, blog_id):
    post_d = get_object_or_404(Post, pk=blog_id)
    post_d.delete()
    return redirect("/")


def renew(request, blog_id):
    post_r = get_object_or_404(Post, pk=blog_id)
    return render(request, "renew.html", {"post": post_r})


# Create your views here.
