from rest_framework import serializers

from .models import Item 

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item 
        fields = ['tender_no', 'description', 'entity_name', 'procurement_method', 'procurement_category',
                        'created_at', 'closing_date', 'is_active']

