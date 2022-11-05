

from django.shortcuts import render,redirect
from . models import Post
from . forms import MakePost
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def index(request):
    post = {
        'post':Post.objects.all()
    }
    return render(request,'index.html',post)
def post(request, id):
    post = {
        'post':Post.objects.get(id=id)
    }
    return render(request, 'post.html',post)
@login_required
def make(request):
    if request.method == 'POST':  
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'make.html',{'form':MakePost()})
def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request, 'update.html',{'form':MakePost(instance=post)})

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return index(request)
def register(request):
    form=UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,'register.html',{'form':form})
def login(request):
    form=UserCreationForm()
    return render(request,'login.html',{'form':form})