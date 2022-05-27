#
# If you need any resources created 
# before a test is run, do it in setUp(). 
# Below, set up FN does three things:
#
#  1. Registers a Gamer in the testing database.
#  2. Captures the authentication Token from the response.
#  3. Seeds the testing database with a GameType.
#
#  All FNs dealing with integration testing must start with " test_  "
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from raterprojectapi.models import Game, Gamer
from raterprojectapi.views.game import GameSerializer, CreateGameSerializer

class GameTests(APITestCase):
    # start with adding fixtures needed to run to build out the test DB
    fixtures = ['users', 'tokens', 'gamers', 'categories', 'games',
                'images', 'ratings', 'reviews']
    
    def setUp(self):
        # Get the 1st Gamer object from DB and add their token to headers
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        
    
    def test_create_game(self):
        """ Test for creating a game"""
        url = "/games"
        
        # define the game properties
        # keys should match what the CREATE method is expecting
        game = {
            "description": "Sunday Rodeo",
            "designer": "The Fun Room Club2",
            "number_of_players": 14,
            "time_to_play": 2,
            "age_rec": 21,
            "title": "Vroooooom2",
            "release_year": 2011,
            "gamer_id": 1         
        }
        
        response = self.client.post(url, game, format='json')
        
        # The _expected_ output should come first when using an assertion with 2 arguments
        # The _actual_ output will be the second argument
        # We _expect_ the status to be status.HTTP_201_CREATED and it _actually_ was response.status_code
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        # Get the last game added to the database, it should be the one just created
        new_game = Game.objects.last()
        
        # Since the create method should return the serialized version of the newly created game,
        # Use the serializer you're using in the create method to serialize the "new_game"
        # Depending on your code this might be different
        expected = CreateGameSerializer(new_game)   

        # Now we can test that the expected output matches what was actually returned
       
        self.assertEqual(expected.data, response.data)
        
        
        
        
        
             
    def test_get_game(self):
        """Get Game Test
        """
        # Grab a game object from the database
        game = Game.objects.first()

        url = f'/games/{game.id}'

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        # Like before, run the game through the serializer that's being used in view
        expected = GameSerializer(game)

        # Assert that the response matches the expected return data
        self.assertEqual(expected.data, response.data)
        
        
        
    def test_list_games(self):
        """Test list games"""
        url = '/games'

        response = self.client.get(url)
        
        # Get all the games in the database and serialize them to get the expected output
        all_games = Game.objects.all()
        expected = GameSerializer(all_games, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(expected.data, response.data)
        
        
        
    def test_change_game(self):
        """test update game"""
        # Grab the first game in the database
        game = Game.objects.first()

        url = f'/games/{game.id}'

        updated_game = {
            "description": f'{game.description} updated',
            "designer": game.designer,
            "number_of_players": game.number_of_players,
            "time_to_play": game.time_to_play,
            "age_rec": game.age_rec,
            "title": game.title,
            "release_year": game.release_year,
            "gamer": game.gamer_id
        }

        response = self.client.put(url, updated_game, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        # Refresh the game object to reflect any changes in the database
        game.refresh_from_db()

        # assert that the updated value matches
        self.assertEqual(updated_game['description'], game.description)
        
      