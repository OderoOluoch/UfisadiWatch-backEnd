from rest_framework import serializers

from .models import Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['tender_no', 'description', 'entity_name', 'procurement_method', 'procurement_category',
                        'created_at', 'closing_date', 'is_active']

