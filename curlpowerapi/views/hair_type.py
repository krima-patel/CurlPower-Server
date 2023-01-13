"""View module for handling requests about routines"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curlpowerapi.models import HairType

class HairTypeView(ViewSet):
    """Curl Power Hair Type View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single hair type

        Returns:
            Response -- JSON serialized hair type
        """
        hair_type = HairType.objects.get(pk=pk)
        serializer = HairTypeSerializer(hair_type)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all hair types

        Returns:
            Response -- JSON serialized list of hair types
        """
        hair_types = HairType.objects.all()
        serializer = HairTypeSerializer(hair_types, many=True)
        return Response(serializer.data)

class HairTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for hair type
    """
    class Meta:
        model = HairType
        fields = ('id', 'hair_type')
