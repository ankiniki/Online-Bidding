"""BIDDING_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buyer_seller/', TemplateView.as_view(template_name='user/login_user.html'), name='login_user'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('user_reg/',views.user_reg,name='user_reg'),
    path('user_home/',views.user_home,name='user_home'),
    path('bid_product/',views.bid_product,name='bid_product'),
    path('sell_product/',views.sell_product,name='sell_product'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('save_product/',views.save_product,name='save_product'),
]
