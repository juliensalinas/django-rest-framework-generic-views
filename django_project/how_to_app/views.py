from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductsSerializer
from .model import Product


class GetProducts(generics.ListAPIView):
    """Return all products."""
    serializer_class = ProductsSerializer


class GetActiveProducts(generics.ListAPIView):
    """Return all active products."""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductsSerializer

    def get_queryset(self):
        """Filter active products."""
        return Product.objects.filter(active=True)


class DeleteProduct(generics.DestroyAPIView):
    """Remove product"""
    permission_classes = (permissions.IsAuthenticated,
                          )  # Limit to authenticated users only


class DisableProduct(generics.DestroyAPIView):
    """Remove product"""
    permission_classes = (permissions.IsAuthenticated,)

    def destroy(self, request, pk):
        """
        By default, DestroyAPIView deletes the product from db.
        Here we only want to flag it as inactive.
        """
        product = get_object_or_404(self.get_queryset(), pk=pk)
        product.active = False
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
