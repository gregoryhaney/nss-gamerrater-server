"""Module for generating bottom five rated games report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterprojectreports.views.helpers import dict_fetch_all


class BottomGamesByRatingList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # Query to get Bottom five games by rating
            db_cursor.execute("""
                SELECT  r.rating AS Rating, 
                        g.description AS Desc,
                        g.title AS Title,
                        g.id AS GameID
                FROM raterprojectapi_rating AS r
                JOIN raterprojectapi_game AS g
                    ON r.game_id = g.id
                ORDER BY r.rating DESC
                LIMIT 5                        
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)
    
            games_by_rating = []

            for row in dataset:
                # Create a dictionary called "game" that includes 
                # the attributes from the row dictionary.
                game = {
                    'id': row['GameID'],
                    'description': row['Desc'],
                    'title': row['Title'],
                    'rating': row['Rating']                   
                }
                
              
                
                game_dict = None
                if game_dict:
                    # If the game_dict is already in the "games_by_rating" list, append it to the list
                    game_dict['games'].append(game)
                else:
                    # If the game is not on the "games_by_rating" list, create and add the game to the list
                    games_by_rating.append({
                        'description': row['Desc'],
                        'title': row['Title'],
                        'rating': row['Rating']
                    })
        
        # The template string must match the file name of the html template
        template = 'games/top_games_by_rating.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "ratinggame_list": games_by_rating
        }

        return render(request, template, context)
