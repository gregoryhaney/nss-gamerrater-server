"""View module to handle requests about Reviews"""

from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game, Gamer, Category, Review, review


class GameReviewView(ViewSet):
    """ViewSet for GameReviewView - get the collection of games from DB
        Returns:
            Response -- JSON serialized list of all games    
    """
    def list(self, request):
        review = Review.objects.all()          # ORM method "all"
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
    
   
    def retrieve(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)      
        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """ Handle POST operations
                        returns:
                            Response -- JSON serialized game instance
        """ 
        game = Game.objects.get(pk=request.data["game"])
        gamer = Gamer.objects.get(user=request.auth.user)
        review = Review.objects.create(
            review_body=request.data["review_body"],
            game=game,
            gamer=gamer
        #    category=category
        )  
        
        serializer = CreateReviewSerializer(review)
        return Response(serializer.data)
    
class ReviewSerializer(serializers.ModelSerializer):
    """  JSON serializer for review
    """
    class Meta:
        model = Review
        fields = ('id', 'review_body', 'game', 'gamer')
        depth: 2  
        
       
class CreateReviewSerializer(serializers.ModelSerializer):
     # the Serializer class determines how the Python data should be serialized
        # to be sent back to the client.
    # This is a new Serializer class that is being used to do input validation
    # It includes ONLY the fields expected from the client.
        
    """JSON serializer for review to validate/save the new review in the Create method
    """
    class Meta:
        model = Review
        fields = ('id', 'review_body', 'game', 'gamer')    
      