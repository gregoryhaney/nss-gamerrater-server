"""View module to handle request about categories"""

from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Category



class CategoryView(ViewSet):
    """ViewSet for CategoryView - get the collection of categories from DB
        Returns:
            Response -- JSON serialized list of all categories    
    """
    def list(self, request):
        category = Category.objects.all()          # ORM method "all"
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    
   
    def retrieve(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)      
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)



class CategorySerializer(serializers.ModelSerializer):
        
    """JSON serializer for category
    """
    class Meta:
        model = Category
        fields = ('id', 'cat_name')
        