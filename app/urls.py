from django.contrib import admin
from django.urls import path

from  app.views import sample_views as sample_views
from  app.views import dashboard_views as dashboard_views
from  app.views import company_views as company_views

dashboard_urls = [
    path('', dashboard_views.login,name="login"),
    path('logout', dashboard_views.logout,name="logout"),
    path('login', dashboard_views.login,name="login"),
    path('index_page/', dashboard_views.index_page, name='index_page'),
]

company_urls = [
    path('manage_company/', company_views.manage_company, name='register_company'),
    path('delete_company_view/<int:id>/', company_views.delete_company_view, name='delete_company_view'),
    path('edit_company_view/<int:id>/', company_views.edit_company_view, name='edit_company_view'),
]

sample_urls = [
    path('manage_sample_requests/', sample_views.manage_sample_requests, name='request_sample'),
    
    path('manage_samples/<int:sample_request_id>/',
         sample_views.manage_samples, name='manage_sample'),
    path('view_request_details/<int:sample_request_id>/',
         sample_views.request_details_view, name='view_request_details'),
    
]

urlpatterns = [
] + dashboard_urls + company_urls + sample_urls
