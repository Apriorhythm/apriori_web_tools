from django.conf.urls import url
from . import views

from django.contrib.auth.decorators import login_required

# My Urls

urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
    url(r'^index$', login_required(views.index), name='index'),

]

