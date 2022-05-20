from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404

from .models import Post

def homepage(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'base/index.html',context)

def createpage(request):
    context = {}
    return HttpResponse("Create Page")

def updatepage(request):
    context = {}
    return HttpResponse("Create Page")

def deletepage(request):
    context = {}
    return HttpResponse("Create Page")

# def detailpage(request,pk_post):
#     post = get_list_or_404(Post,id = pk_post)
#     context = {"post": post}
#     print(post.title)
#     return render(request, 'base/leftside/postdetail.html',context)

def detailpage(request,pk_post):
    
    post = get_object_or_404(Post,id = pk_post)

    context = {"post": post}
    
    return render(request, 'base/leftside/postdetail.html',context)