"""View module for handling requests about routines"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curlpowerapi.models import Product, Routine, User, ProductHairType, HairType
from .product_hair_type import ProductHairTypeSerializer
from rest_framework.decorators import action
from rest_framework import generics

class ProductView(ViewSet):
    """Curl Power Product View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single product

        Returns:
            Response -- JSON serialized product
        """
        product = Product.objects.get(pk=pk)
        types = ProductHairType.objects.filter(product=pk)
        types_serialized = ProductHairTypeSerializer(types, many=True)
        product.types = types_serialized.data
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all products

        Returns:
            Response -- JSON serialized list of products
        """
        routine = request.query_params.get('routine', None)
        if routine is not None:
            products=products.filter(routine_id=routine)
        serializer = ProductSerializer(products, many=True)

        # products = Product.objects.all()
        # for product in products:
        #     types = ProductHairType.objects.filter(product=product.id)
        #     types_serialized = ProductHairTypeSerializer(types, many=True)
        #     product.types = types_serialized.data
        #     serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized product instance
        """
        hair_types=request.data["types"]
        user = User.objects.get(pk=request.data["user_id"])

        product = Product.objects.create(
            routine=Routine.objects.get(pk=request.data["routine_id"]),
            name=request.data["name"],
            product_type=request.data["product_type"],
            purpose=request.data["purpose"],
            price_range=request.data["price_range"],
            image_url=request.data["image_url"],
            date=request.data["date"],
            user=user
          )
        for hair in hair_types:
            print(hair)
            ProductHairType.objects.create(product=product, hair_type=HairType.objects.get(pk=hair))
            serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a product

        Returns:
            Response -- Empty body with 204 status code
        """
        product = Product.objects.get(pk=pk)
        product.name=request.data["name"]
        product.product_type=request.data["product_type"]
        product.purpose=request.data["purpose"]
        product.price_range=request.data["price_range"]
        product.image_url=request.data["image_url"]
        product.date=request.data["date"]

        routine = Routine.objects.get(pk=request.data["routine_id"])
        product.routine = routine
        product.save()

        types = request.data["types"]
        existing_types = ProductHairType.objects.filter(product=product)

        if existing_types is not None:
            for taco in existing_types:
                taco.delete()

        if types is not None:
            for taco in types:
                ProductHairType.objects.create(product=product, hair_type=HairType.objects.get(pk=taco))

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE request for a productcap"""
        product=Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for product
    """
    class Meta:
        model = Product
        fields = ('id', 'routine', 'name',
                  'product_type','purpose', 'price_range','image_url', 'date', 'user', 'types')
        depth = 1

class RoutineProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        routine_id = self.kwargs['routine_id']
        return Product.objects.filter(routine__id=routine_id)
