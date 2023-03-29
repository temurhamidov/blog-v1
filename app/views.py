from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.text import slugify

from .forms import BlogAddForms, BlogUpdateForms, CommentForm
from .models import Blog, Category, Tag


# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2)

    current_page = request.GET.get('page')
    obj = paginator.get_page(current_page)
    context = {
        'blogs' : obj,
    }

    return render(request, 'app/home.html', context)


def blog_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = Blog.objects.filter(category=category)

    context = {
        'category' : category,
        'blogs': blogs,
    }
    return render(request, 'app/home.html', context)


def category(request):
    categories = Category.objects.all()

    context = {
        'categories' : categories,
    }

    return render(request, 'app/category.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect('app:blog_detail', blog.slug)
    else:
        form = CommentForm()
    blog.view += 1
    blog.save()
    context = {
        'blog': blog,
        'form': form,
    }
    return render(request, 'app/blog_detail.html', context)

def add_blog(request):
    user = request.user
    if request.method == 'POST':
        form = BlogAddForms(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = user
            blog.save()
            tags = form.cleaned_data.get('tags').split()
            for tag in tags:
                t, created = Tag.objects.get_or_create(name=tag)
                blog.tags.add(t)
            return redirect('app:home')
        else:
            messages.error(request, 'Blog yaratilmadi! ')
    else:
        form = BlogAddForms()
        context = {
            'form' : form,
        }
    return render(request, 'app/add_blog.html', context)


def blog_update(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = BlogUpdateForms(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.info(request, 'Blog yangilandi! ')
            return redirect('app:blog_detail', blog.slug)
    else:
        form = BlogUpdateForms(instance=blog)
    context = {
        'form' : form,
        'blog' : blog,
    }
    return render(request, 'app/blog_update.html', context)



def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog' : blog
    }

    if request.method == 'POST':
        blog.delete()
        messages.info(request, 'Succesfully update')
        return redirect('app:home')
    return render(request, 'app/blog_delete.html', context)


def user_list(request):
    search = request.GET.get('search')
    users = User.objects.all()
    if search:
        users = users.filter(Q(username__icontains=search) | Q(first_name__icontains=search))
    context = {
        'users' : users,
    }
    return render(request, 'app/user_list.html', context)


def my_blog(request):
    user = request.user
    blogs = Blog.objects.filter(author=user)

    context = {
        'blogs': blogs,
    }
    return render(request, 'app/my_blog.html', context)


def blog_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    blogs = Blog.objects.filter(tags=tag)
    paginator = Paginator(blogs, 2)
    current_page = request.GET.get('page')
    obj = paginator.get_page(current_page)
    context = {
        'blogs': obj,
    }
    return render(request, 'app/home.html', context)






