"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import path, include

from core.forms import LoginForm
from core.views import HomeView

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html', form_class=LoginForm
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path('home/', login_required(HomeView.as_view()), name='home'),

    # app urls
    path(
        'expenses/', include('expenses.urls', namespace='expenses')
    ),
    path(
        'envelopes/', include('envelopes.urls', namespace='envelopes')
    ),

    # admin and translation
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]
