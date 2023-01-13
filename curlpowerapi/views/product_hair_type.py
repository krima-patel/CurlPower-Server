"""View module for handling requests about routines"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curlpowerapi.models import ProductHairType

class ProductHairTypeView(ViewSet):
    """Curl Power Product Hair Type View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single product hair type

        Returns:
            Response -- JSON serialized product hair type
        """
        product_hair_type = ProductHairType.objects.get(pk=pk)
        serializer = ProductHairTypeSerializer(product_hair_type)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all product hair types

        Returns:
            Response -- JSON serialized list of product hair types
        """
        product_hair_types = ProductHairType.objects.all()
        serializer = ProductHairTypeSerializer(product_hair_types, many=True)
        return Response(serializer.data)

class ProductHairTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for product hair type
    """
    class Meta:
        model = ProductHairType
        fields = ('id', 'product', 'hair_type', 'user')
