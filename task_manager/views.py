from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Привет от Хекслета!')