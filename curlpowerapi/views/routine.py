"""View module for handling requests about routines"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curlpowerapi.models import Routine, User

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

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        user = User.objects.get(pk=request.data["user_id"])

        routine = Routine.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            hair_type=request.data["hair_type"],
            date=request.data["date"],
            user=user
        )
        serializer = RoutineSerializer(routine)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a routine

        Returns:
            Response -- Empty body with 204 status code
        """
        routine=Routine.objects.get(pk=pk)
        routine.title=request.data["title"]
        routine.description=request.data["description"]
        routine.hair_type=request.data["hair_type"]
        routine.date=request.data["date"]
        routine.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class RoutineSerializer(serializers.ModelSerializer):
    """JSON serializer for routines
    """
    class Meta:
        model = Routine
        fields = ('id', 'title', 'description', 'hair_type', 'date', 'user')
