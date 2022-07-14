"""Module for generating the player with the most games in the collection report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterprojectreports.views.helpers import dict_fetch_all


class PlayerWithMostGamesList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # Query to get the player with the most games in the collection
            db_cursor.execute("""
                SELECT  gr.handle AS Gamer,
                        COUNT(g.id) AS NbrGames,
                        g.id AS GameID
                FROM raterprojectapi_game AS g
                JOIN raterprojectapi_gamer AS gr
                ON g.gamer_id = gr.id
                GROUP BY gr.handle                      
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)
    
            games_by_count = []

            for row in dataset:
                # Create a dictionary called "game" that includes 
                # the attributes from the "row" dictionary
                game = {
                    'id': row['GameID'],
                    'handle': row['Gamer'],
                    'NbrGames': row['NbrGames']               
                }
                
              
                
                game_dict = None
                if game_dict:
                    # If the "game_dict" is already in the "games_by_rating" list, append it to the list
                    game_dict['games'].append(game)
                else:
                    # If the game is not on the "games_by_rating" list, create and add the game to the list
                    games_by_count.append({
                        'handle': row['Gamer'],
                        'NbrGames': row['NbrGames']
                    })
        
        # The template string must match the file name of the html template
        template = 'games/player_with_most_games.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "countgame_list": games_by_count
        }

        return render(request, template, context)
