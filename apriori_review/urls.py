from django.conf.urls import url

from django.contrib.auth.decorators import login_required
from . import views

app_name = 'apriori_review'

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^index$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^content$', login_required(views.ContentView.as_view()), name='content'),
]
