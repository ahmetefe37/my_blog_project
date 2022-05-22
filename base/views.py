from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory

#my modules
from .models import Post
from .forms import PostForm


def homepage(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'base/index.html',context)


def createpage(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("post:home_url")
    context = {"form": form}
    return render(request, 'base/crudpages/post_create.html',context)


def updatepage(request,pk_post_update):
    post = Post.objects.get(id=pk_post_update)
    form = PostForm(request.POST or None,request.FILES or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect("post:home_url")
    context = {"form": form}
    return render(request, 'base/crudpages/post_update.html',context)


def deletepage(request,pk_post_delete):
    post = Post.objects.get(id=pk_post_delete)
    if request.method == 'POST':
        post.delete()
        return redirect("post:home_url")
    context = {}
    return render(request, 'base/crudpages/post_delete.html',context)


def detailpage(request,pk_post_detail):
    post = get_object_or_404(Post,id = pk_post_detail)
    context = {"post": post}
    return render(request, 'base/leftside/postdetail.html',context)