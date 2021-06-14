from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
import logging
# class LoginView(View):
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)

#                 return HttpResponseRedirect('/form')
#             else:
#                 return HttpResponse("Inactive user.")
#         else:
#             return HttpResponseRedirect(settings.LOGIN_URL)

#         return render(request, "index.html")


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Привет от Хекслета!')


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


class UpdateUser(UpdateView):

    template_name = "user_update.html"
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

    def get_success_url(self):
        return "/"

    # нужно как-то обработать ввод неправильного пароля при апдейте


class DeleteUser(DeleteView):

    template_name = "user_delete.html"
    model = User

    def get_success_url(self):
        return "/users"


class Login(LoginView):

    template_name = 'registration/login.html'
    redirect_field_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


