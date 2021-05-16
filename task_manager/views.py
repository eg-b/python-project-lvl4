from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Привет от Хекслета!')


class HomePage(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['welcome'] = _('Hello from Hexlet!')
        return context


class UserList(ListView):

    template_name = "user_list.html"
    model = User


class CreateUser(CreateView):

    template_name = "user_create.html"
    model = User
    fields = ['username', 'first_name', 'last_name', 'password', 'email']

    def get_absolute_url(self):
        return "/"

    def get_success_url(self):
        return "/"


class UpdateUser(UpdateView):

    template_name = "user_update.html"
    model = User
    fields = ['username', 'first_name', 'last_name', 'password', 'email']