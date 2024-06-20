from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'legeand'

urlpatterns = [
    path('', views.index, name='index'),
    path('contect/', views.contect, name='contect'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='cos/login.html', authentication_form=LoginForm), name='login'),
]
