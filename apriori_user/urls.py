from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'apriori_user'

urlpatterns = [
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', login_required(views.LogoutView.as_view()), name='logout'),
]
