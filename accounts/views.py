from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView
from accounts.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

# Create your views here.
'''class CustomUserLogin(LoginView):
    template_name = 'registration/login.html'
    next_page = 'profile'
    authentication_form = AuthenticationForm
    success_url = reverse_lazy('profile')'''

class CustomUserRegistration(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm


class CustomUserUpdateView(UpdateView, LoginRequiredMixin):
    model = CustomUser
    template_name_suffix = '_update_form'
    fields = ['email', 'first_name', 'last_name', 'date_of_birth']

class Profile(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'user'
    login_url = 'accounts/login/'


@login_required
def account_redirect(request):
    return redirect('accounts:profile', pk=request.user.pk,)


class UserSettingsView(TemplateView, LoginRequiredMixin):
    login_url = 'accounts:login'
    template_name = 'accounts/user-settings.html'
    context_object_name = 'user'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        request = self.request
        #context['post_list'] = Post.objects.filter(
        #    username=user.username)
        #work on sorting post by current user
        #import note models to here
        return context

@login_required
def profile_update_redirect(request):
    return redirect('accounts:profile-update', pk=request.user.pk)