from django.urls import path

from service.apps import ServiceConfig
from service.views import ApppointmentCreateView, ApppointmentDetailView, ApppointmentUpdateView, \
    ApppointmentConfirmDeleteView, ApppointmentDeleteView, ApppointmentListAdminView, IndexView

app_name = ServiceConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('app_add/', ApppointmentCreateView.as_view(), name='app_form'),
    path('app/detail/<int:pk>/', ApppointmentDetailView.as_view(), name='app_detail'),
    path('app/edit/<int:pk>/', ApppointmentUpdateView.as_view(), name='app_update'),
    path('app/delete/confirm/<int:pk>/', ApppointmentConfirmDeleteView.as_view(), name='app_confirm_delete'),
    path('app/delete/<int:pk>/', ApppointmentDeleteView.as_view(), name='app_delete'),
    path('app/list/', ApppointmentListAdminView.as_view(), name='app_list'),

]
