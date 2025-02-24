from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from .forms import UserForm 


# Create your views here.


class EnterRestricMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('tasks')


class CusomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = 'True'
    

    def get_success_url(self):
        return reverse_lazy('tasks')
    

class RegisterPage(EnterRestricMixin,FormView):
    template_name = "base/register.html"
    form_class = UserForm
    redirect_authenticated_user = 'True'
    success_url = reverse_lazy('tasks')

    def get_success_url(self):
        return reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:    
            login(self.request, user)
        return super(RegisterPage,self).form_valid(form)
    
  


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        result = self.request.GET.get('search-area')
        if self.request.GET.get('search-area'):
            return Task.objects.filter(user = self.request.user).filter(title__icontains= result)
        return Task.objects.filter(user = self.request.user)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['count'] = context['tasks'].filter(complete = False).count()
        return context

     


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_form.html'

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = "task"    
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['obj'] = self.object
        return context

