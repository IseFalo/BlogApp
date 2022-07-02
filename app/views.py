from cgitb import text
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from.forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('app:login_page')
    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password Incorrect')
            
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def index(request):
    post = Post.objects.all()
    post_image = request.GET.get('post_image')
    context = {'post':post,'post_image':post_image}
    return render(request, 'index.html', context)



def detailPost(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
           instance=c_form.save(commit=False)
           instance.post = post
           instance.save()
           return redirect('app:detailView', pk=post.id)
    else:
        c_form = CommentForm()
    
    context = {'post':post, 'c_form':c_form}
    return render(request, 'post_detail.html',context)

@login_required
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'post_create.html', context)

@login_required
def updatePost(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    if request.user!=post.author:
        return HttpResponse('You are not allowed here')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'post_create.html', context)


def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    context = {'post':post}
    return render(request, 'post_delete.html', context)


