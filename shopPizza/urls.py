"""shopPizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from django.contrib.auth import views as auth_views

from pizzashopapp import views

#Для медиа файлов
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pizzashop/sign-in/', auth_views.login, 
    {'template_name':'pizzashop/sign_in.html'}, name='pizzashop-sign-in'),
    path('pizzashop/sign-out/', auth_views.logout, 
    {'next_page':'/'}, name='pizzashop-sign-out'),
    path('pizzashop/', views.pizzashop_home, name='pizzashop-home'),
    path('pizzashop/sign-up/', views.pizzashop_sign_up, name='pizzashop-sign-up'),

    path('pizzashop/account/', views.pizzashop_account, name='pizzashop-account'),
    path('pizzashop/pizza/', views.pizzashop_pizza, name='pizzashop-pizza'),
    path('pizzashop/pizza/add/', views.pizzashop_add_pizza, name='pizzashop-add-pizza'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
