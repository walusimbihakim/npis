"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from  app.views import views

urlpatterns = [
    path('', views.index_page_view, name='home'),
    path('admin/', admin.site.urls),
    path('login', views.login,name="login"),
    path('logout', views.logout,name="logout"),
    # path('', views.IndexView.as_view(), name='home'),
    path('manage_company/', views.manage_company, name='register_company'),
    path('manage_sample/', views.manage_sample, name='request_sample'),
    path('index_page/', views.index_page, name='index_page'),
    path('delete_company_view/<int:id>/', views.delete_company_view, name='delete_company_view'),
    path('edit_company_view/<int:id>/', views.edit_company_view, name='edit_company_view'),
]
