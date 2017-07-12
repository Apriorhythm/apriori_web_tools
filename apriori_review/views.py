# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic import View

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

#  from .serializers import AprioriUserSerializer


# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'apriori_review/index.html')

