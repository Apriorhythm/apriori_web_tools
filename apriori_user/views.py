# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import View
from .forms import LoginForm
from django import forms

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from apriori_user.models import AprioriUser
from .serializers import AprioriUserSerializer


# Create your views here.


class LoginView(View):
    form_class = LoginForm
    template_name = 'apriori_user/login.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        login_errors = "Sorry, username or password doesn't match"

        # cleaned (normalized) data
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # returns User object if credentials are correct
        if password is not none:
            return render(request, self.template_name,{'form':form,
            'login_errors':login_errors})

        # returns User object if credentials are correct
        user = authenticate(username=username)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')

        return render(request, self.template_name,{'form':form,
        'login_errors':login_errors})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

