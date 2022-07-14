"""Module for generating most-reviewed game report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterprojectreports.views.helpers import dict_fetch_all


class MostReviewedGameList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # Query to get the most-reviewed game
            db_cursor.execute("""
                SELECT  g.description AS Desc,
                        g.title AS Title, 
                        COUNT(r.id) AS NbrReviews,
                        g.id AS GameID
                FROM raterprojectapi_review AS r
                JOIN raterprojectapi_game AS g
                ON r.game_id = g.id
                GROUP BY r.id                    
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)
    
            games_reviews = []

            for row in dataset:
                # Create a dictionary called "game" that includes 
                # the attributes from the "row" dictionary
                game = {
                    'id': row['GameID'],
                    'description': row['Desc'],
                    'title': row['Title'],
                    'NbrReviews': row['NbrReviews']                   
                }
                
              
                
                game_dict = None
                if game_dict:
                    # If the "game_dict" is already in the "games_by_rating" list, append it to the list
                    game_dict['games'].append(game)
                else:
                    # If the game is not on the "games_by_rating" list, create and add the game to the list
                    games_reviews.append({
                        'description': row['Desc'],
                        'title': row['Title'],
                        'NbrReviews': row['NbrReviews']
                    })
        
        # The template string must match the file name of the html template
        template = 'games/most_reviewed_game.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "reviews_list": games_reviews
        }

        return render(request, template, context)
