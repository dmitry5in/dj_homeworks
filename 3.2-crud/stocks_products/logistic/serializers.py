from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description', 'stocks']


class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for el in positions:
            StockProduct.objects.create(
                stock=stock,
                product=el.get('product'),
                quantity=el.get('quantity'),
                price=el.get('price'),
            )
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for el in positions:
            StockProduct.objects.update_or_create(
                product=el.get('product'),
                stock=stock,
                defaults={
                    'quantity': el.get('quantity'),
                    'price': el.get('price'),
                }
            )
        return stock
