"""View module for handling requests about routines"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curlpowerapi.models import Routine

class RoutineView(ViewSet):
    """Curl Power Routine View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single routine

        Returns:
            Response -- JSON serialized routine
        """
        routine = Routine.objects.get(pk=pk)
        serializer = RoutineSerializer(routine)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all routines

        Returns:
            Response -- JSON serialized list of routines
        """
        routines = Routine.objects.all()
        serializer = RoutineSerializer(routines, many=True)
        return Response(serializer.data)

class RoutineSerializer(serializers.ModelSerializer):
    """JSON serializer for routines
    """
    class Meta:
        model = Routine
        fields = ('id', 'title', 'description', 'hair_type', 'date', 'user')
