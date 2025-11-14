from django.shortcuts import render,redirect,get_object_or_404
from.forms import Todoform,Userform
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView,DetailView
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class Register_view(View):
    def get(self,request,*args, **kwargs):
        form=Userform()
        return render(request,'registerform.html',{'form':form})

    def post(self,request,*args, **kwargs):
        form=Userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

def login_view(request):
    if request.method == "POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,'loginform.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

class foryou_view(ListView):
    model = Todo
    template_name = 'foryou.html'
    context_object_name = 'Todo'

class detail_view(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'Todo'
    
@login_required(login_url='login')
def createtodo_view(request):
    if request.method == "POST":
        form=Todoform(request.POST,request.FILES)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.user=request.user
            todo.save()
            return redirect('profile')
    else:
        form=Todoform()
    return render(request,'createtodo.html',{'form':form})

@login_required(login_url='login')
def edit_view(request,required_id):
    data=get_object_or_404(Todo,user=request.user,id=required_id)
    if request.method == "POST":
        form=Todoform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.user=request.user
            todo.save()
            return redirect('profile')
    else:
        form=Todoform(instance=data)
    return render(request,'createtodo.html',{'form':form})

@login_required(login_url='login')
def delete_view(request,required_id):
    if request.method == "POST":
        todo=Todo.objects.filter(id=required_id,user=request.user)
        todo.delete()
        return redirect('profile')
    return render(request,'delete.html')

class myprofile_view(LoginRequiredMixin,ListView):
    model = Todo
    template_name = 'myprofile.html'
    context_object_name = 'data'    

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
