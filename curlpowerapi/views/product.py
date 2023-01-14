"""View module for handling requests about routines"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curlpowerapi.models import Product, User, Routine

class ProductView(ViewSet):
    """Curl Power Product View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single product

        Returns:
            Response -- JSON serialized product
        """
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all products

        Returns:
            Response -- JSON serialized list of products
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized product instance
        """
        user = User.objects.get(pk=request.data["user_id"])

        product = Product.objects.create(
            routine=Routine.objects.get(pk=request.data["routine_id"]),
            hair_type=request.data["hair_type"],
            name=request.data["name"],
            product_type=request.data["product_type"],
            purpose=request.data["purpose"],
            price_range=request.data["price_range"],
            image_url=request.data["image_url"],
            date=request.data["date"],
            user=user
          )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for product
    """
    class Meta:
        model = Product
        fields = ('id', 'routine', 'hair_type', 'name',
                  'product_type','purpose', 'price_range','image_url', 'date', 'user')
