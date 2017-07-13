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

import datetime
from itertools import chain

from .models import AprioriReview

from .serializers import AprioriReviewSerializer

# Create your views here.


class IndexView(View):
    def get(self, request):
        template_name = 'apriori_review/index.html'
        return render(request, template_name)

class ContentView(APIView):

    def get(self, request):
        day_list = [2, 4, 7, 15, 30, 60]

        content = AprioriReview.objects.filter(
            create_date = datetime.date.today() -
            datetime.timedelta(days=1))

        for day in day_list:
            content = chain(content ,AprioriReview.objects.filter(
                create_date = (datetime.datetime.now() -
                datetime.timedelta(days=day))))

        serializer = AprioriReviewSerializer(content, many=True)

        return Response(serializer.data)
#        print(content)
#        return Response(content)

    def post(self, request):
        print('###############################')
        new_content = request.POST.get('content')
        new_review = AprioriReview(content=new_content)
        if new_content is None:
            return HttpResponse("0")
        new_review.save()

        return HttpResponse("1")


