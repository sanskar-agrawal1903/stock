from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    price=serializers.IntegerField()

    def create(self,validated_data):
        return Stock.objects.create(validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.price=validated_data.get('price',instance.price)
        instance.save()
        return instance

