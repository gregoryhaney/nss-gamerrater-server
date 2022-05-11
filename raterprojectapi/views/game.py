"""View module to handle request about games"""

from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game, Gamer, Category


class GameView(ViewSet):
    """ViewSet for GameView - get the collection of games from DB
        Returns:
            Response -- JSON serialized list of all games    
    """
    def list(self, request):
        games = Game.objects.all()          # ORM method "all"
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
   
    def retrieve(self, request, pk):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)      
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """ Handle POST operations
                        returns:
                            Response -- JSON serialized game instance
        """ 
        # category = Category.objects.get(pk=request.data["category.id"])
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.create(
            title=request.data["title"],
            designer=request.data["designer"],
            release_year=request.data["release_year"],
            number_of_players=request.data["number_of_players"],
            time_to_play=request.data["time_to_play"],
            age_rec=request.data["age_rec"],
            description=request.data["description"],
            gamer=gamer
        #    category=category
        )  
        
        serializer = CreateGameSerializer(game)
        return Response(serializer.data)


    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
       
        game = Game.objects.get(pk=pk)
        serializer = CreateGameSerializer(game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)   
    

    
class GameSerializer(serializers.ModelSerializer):
    """  JSON serializer for game
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'designer', 'release_year', 
                  'description', 'number_of_players', 
                  'time_to_play', 'age_rec', 'gamer', 'description')
        depth: 2  
        
       
class CreateGameSerializer(serializers.ModelSerializer):
     # the Serializer class determines how the Python data should be serialized
        # to be sent back to the client.
    # This is a new Serializer class that is being used to do input validation
    # It includes ONLY the fields expected from the client.
        
    """JSON serializer for game to validate/save the new game in the Create method
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'designer', 'number_of_players',
                  'release_year', 'time_to_play', 'age_rec', 
                  'gamer', 'description')    
      