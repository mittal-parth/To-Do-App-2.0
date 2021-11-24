from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# Just to redirect from one page to another
from django.urls import reverse_lazy 

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# To enable a user to directly login after registration
from django.contrib.auth import login
from .models import Task
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True # A user which is already authenticated cant access this page now

    def get_success_url(self): # We are now defining a function for our success_url
        return reverse_lazy('tasks')

class SignUpPage(FormView):
    template_name = 'base/signup.html'
    form_class = UserCreationForm
    # redirect_authenticated_user = True # This doesnt work for UserCreationForm
    success_url = reverse_lazy('tasks')

    #A function to handle data from the SignUp page
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user) # Automatically login
        return super(SignUpPage, self).form_valid(form) # Otherwise, do what you were doing
    
    # We write a custom method to not allow a user to access the register page if logged in
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(SignUpPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin ,ListView):
    model = Task
    # This is the name of the list that is passed onto the template
    # Its by default called object_list
    context_object_name = 'tasks' 

    # Only gives data pertaining to that user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtering it out for that user
        context["tasks"] = context["tasks"].filter(user = self.request.user) 

        # Number of tasks that are undone
        # Here we can pass more data than defined in model
        context["count"] = context["tasks"].filter(complete = False).count() 

        # Note that each time we are changing the context, 
        # we are doing the over the already changed value
        # Get what was typed in 'search_area', or by defualt keep it empty
        search_input = self.request.GET.get('search_area') or ''
        if search_input:
            # icontains is Django thing and is self explanatory
            context["tasks"] = context["tasks"].filter(title__icontains = search_input) 
        
        # Pass that back to the template
        context["search_input"] = search_input 
        return context
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    # default is task_detail
    template_name = 'base/task.html' 

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    # Creates a model form by defualt. Only selected fields are passed
    fields = ['title', 'description', 'complete', 'duedate'] 
    
    # If everything goes correctly, redirect the user to tasks
    success_url = reverse_lazy('tasks') 

    # For adding tasks specific to that user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title', 'description', 'complete', 'duedate']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')