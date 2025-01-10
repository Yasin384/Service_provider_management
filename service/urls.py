from django.urls import path 
from django.urls import path
from .views import EquipmentListCreateView, EquipmentDetailView

urlpatterns = [
    # List and Create Equipment
    path('equipment/', EquipmentListCreateView.as_view(), name='equipment-list-create'),

    # Retrieve, Update, and Delete specific Equipment
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
]
