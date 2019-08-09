from rest_framework import serializers

from .models import Product


class ProductsSerializer(serializers.ModelSerializer):
    """Serialize products."""

    class Meta:
        model = Product
        fields = ("__all__")
