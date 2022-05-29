from turtle import title
from unicodedata import category
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q

#my modules
from .models import Post
from .forms import PostForm
from .filters import PostFilter

def homepage(request):
    post_list = Post.objects.all()

    # query = request.GET
    # if query:
    #     post_list = post_list.filter(
    #         Q(title__icontains=query)|
    #         Q(content__icontains=query)|
    #         Q(author__firstname__icontains=query)|
    #         Q(author__lastname__icontains=query)|
    #         Q(category__icontains=query)|
    #         Q(tags__icontains=query)
    #     ).distinct()

    post_filter = PostFilter(request.GET,queryset=post_list)
    post_list = post_filter.qs

    paginator = Paginator(post_list,5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"posts": posts}
    return render(request, 'base/index.html',context)


def createpage(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post = form.save()
        return redirect("post:home_url")
    context = {"form": form}
    return render(request, 'base/crudpages/post_create.html',context)


def updatepage(request,pk_slug_update):
    post = Post.objects.get(slug=pk_slug_update)
    form = PostForm(request.POST or None,request.FILES or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect("post:home_url")
    context = {"form": form}
    return render(request, 'base/crudpages/post_update.html',context)


def deletepage(request,pk_slugt_delete):
    post = Post.objects.get(slug=pk_slugt_delete)
    if request.method == 'POST':
        post.delete()
        return redirect("post:home_url")
    context = {}
    return render(request, 'base/crudpages/post_delete.html',context)


def detailpage(request,pk_slug_detail):
    post = get_object_or_404(Post,slug = pk_slug_detail)
    context = {"post": post}
    return render(request, 'base/leftside/postdetail.html',context)