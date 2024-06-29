from django.urls import path

from service.apps import ServiceConfig
from service.views import ApppointmentCreateView, ApppointmentDetailView, ApppointmentUpdateView, \
    ApppointmentConfirmDeleteView, ApppointmentDeleteView, ApppointmentListAdminView, IndexView, ServicesCreateView, \
    ServicesListView, ServicesUpdateView, ServicesDetailView, ServicesDeleteView, ServicesConfirmDeleteView, \
    ApppointmentFormSuccessView

app_name = ServiceConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('app/add/<int:service_id>/', ApppointmentCreateView.as_view(), name='app_form'),
    path('app/add/', ApppointmentCreateView.as_view(), name='app_form_empty'),
    path('app/success/', ApppointmentFormSuccessView.as_view(), name='apppointment_form_success'),
    path('app/detail/<int:pk>/', ApppointmentDetailView.as_view(), name='app_detail'),
    path('app/edit/<int:pk>/', ApppointmentUpdateView.as_view(), name='app_update'),
    path('app/delete/confirm/<int:pk>/', ApppointmentConfirmDeleteView.as_view(), name='app_confirm_delete'),
    path('app/delete/<int:pk>/', ApppointmentDeleteView.as_view(), name='app_delete'),
    path('app/list/', ApppointmentListAdminView.as_view(), name='app_list'),

    path('services/add/', ServicesCreateView.as_view(), name='services_form'),
    path('services/list/', ServicesListView.as_view(), name='services_list'),
    path('services/update/<int:pk>/', ServicesUpdateView.as_view(), name='update_form'),
    path('services/detail/<int:pk>/', ServicesDetailView.as_view(), name='services_detail'),
    path('services/delete/<int:pk>/', ServicesDeleteView.as_view(), name='services_delete'),
    path('services/confirm_delete/<int:pk>/', ServicesConfirmDeleteView.as_view(), name='services_confirm_delete'),
]
