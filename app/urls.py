from django.contrib import admin
from django.urls import path

from  app.views import sample_views as sample_views
from  app.views import dashboard_views as dashboard_views
from  app.views import company_views as company_views
from app.views import enforcement_views as enforcement_views
from app.views import inspection_views as inspection_views



dashboard_urls = [
    path('', dashboard_views.login,name="login"),
    path('logout', dashboard_views.logout,name="logout"),
    path('login', dashboard_views.login,name="login"),
    path('index_page/', dashboard_views.index_page, name='index_page'),
]

print_sample_urls = [
    path('sample_print/<int:sample_request_id>',sample_views.generate_pdf, name='sample_print'),
]

enforcement_urls = [
    path('manage_enforceement/', enforcement_views.manage_enforcement_field, name='register_enforcement'),    
    path('edit_field_view/<int:field_id>/',enforcement_views.edit_field_view, name='edit_field_view'),
    path('Detail_field/<int:field_id>/',
         enforcement_views.request_details_field_view, name='Detail_field'),
    
    path('field_print/<int:field_id>',
         enforcement_views.print_enforcement_field, name='field_print_enf'),
]

inspection_urls = [
    path('company_inspection/<int:company_id>/', inspection_views.manage_company_inspection,
         name='company_inspection'),
     path('inspection_checklist/<int:inspection_id>/', inspection_views.manage_inspection_checklist,
         name='inspection_checklist'),
]

company_urls = [
    path('company_detail/<int:company_id>/',
         company_views.company_detail_view, name='company_detail'),
    path('product_detail/<int:company_id>/',
         company_views.manage_product, name='manage_company_product'),
    path('branch_detail/<int:company_id>/',
         company_views.manage_branch, name='manage_company_branch'),
    path('permit_detail/<int:company_id>/',
         company_views.manage_permit, name='manage_company_permit'),
    path('employee_detail/<int:company_id>/',
         company_views.manage_employee, name='manage_company_employee'),
    path('supplier_detail/<int:company_id>/',
         company_views.manage_supplier, name='manage_company_supplier'),
    path('gas_detail/<int:company_id>/',
         company_views.manage_gas, name='manage_company_gas'),
    path('manage_company/', company_views.manage_company, name='register_company'),
    path('manage_product/', company_views.manage_product, name='register_product'),
    path('delete_company_view/<int:company_id>/',
         company_views.delete_company_view, name='delete_company_view'),
    path('edit_company_view/<int:company_id>/',
         company_views.edit_company_view, name='edit_company_view'),
]

sample_urls = [
    path('manage_sample_requests/', sample_views.manage_sample_requests, name='request_sample'),
    
    path('manage_samples/<int:sample_request_id>/',
         sample_views.manage_samples, name='manage_sample'),
    path('view_request_details/<int:sample_request_id>/',
         sample_views.request_details_view, name='view_request_details'),
    
]

urlpatterns = [
] + dashboard_urls + company_urls + sample_urls+print_sample_urls+enforcement_urls + inspection_urls
