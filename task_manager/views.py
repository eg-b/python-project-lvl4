import logging

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(_('Привет от Хекслета!'))


class HomePage(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserList(ListView):

    template_name = "user_list.html"
    model = User


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Login(LoginView):

    template_name = 'registration/login.html'
    redirect_field_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    template_name = "user_update.html"
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    
    @property
    def obj(self):
        return self.get_object()

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )
    
    def get_success_url(self):
        msg = _('was updated succesfully')
        messages.success(self.request, f'{self.obj.username} {msg}')
        return "/users"

    def test_func(self):
        return str(self.request.user) in [self.obj.username, 'admin']

    def handle_no_permission(self):
        msg = _("You have no permission to do this")
        messages.error(self.request, f'{msg}')
        return redirect("/users")
        

    # нужно как-то обработать ввод неправильного пароля при апдейте


class DeleteUser(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):

    template_name = "user_delete.html"
    model = User
    permission_required = "auth.delete_user"

    def get_success_url(self):
        return "/users"

    def test_func(self):
        obj = self.get_object()
        return str(self.request.user) in [obj.username, 'admin']

    def handle_no_permission(self):
        messages.error(self.request, f'{_("You have no permission to do this")}')
        return redirect("/users")
