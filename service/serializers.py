from .models import Equipment
from rest_framework import serializers

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        field = ['id','provider_id','equipment_type','service_type','price_per_gecktar','is_available','created_at','updated_at',]