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

from badmin import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login/', TemplateView.as_view(template_name="badmin_templates/admin_login.html"), name="admin_login"),
    path('check_admin/',views.chech_admin,name="check_admin"),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('pending_reg/',views.pending_reg,name='pending_reg'),
    path('approve_reg/',views.approve_reg,name='approve_reg'),
    path('approve_page/',views.approve_page,name='approve_page'),
    path('decline reg/',views.decline_reg,name='decline_reg'),
    path('decline_page/',views.decline_page,name='decline_page'),
    path('admin_contact/',views.admin_contact,name='admin_contact'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
]
