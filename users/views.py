from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy

from .forms import UserCreationForm

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('tasks:tasks-list')


class UserRegisterPage(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks:tasks-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks-list')
        return super(UserRegisterPage, self).get(*args, **kwargs)