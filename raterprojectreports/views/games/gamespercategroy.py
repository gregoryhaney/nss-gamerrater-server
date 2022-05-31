"""Module for generating games per category report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterprojectreports.views.helpers import dict_fetch_all


class GamesPerCategoryList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get games per category
            db_cursor.execute("""
                SELECT  c.cat_name AS Category, 
                        g.description AS Desc,
                        g.id AS GameID,
                        COUNT(g.id) AS NbrGames
                FROM raterprojectapi_game AS g
                JOIN raterprojectapi_category AS c
                    ON c.id = g.id
                GROUP BY Category
                       
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)
    
            games_by_category = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the attributes from the row dictionary
                game = {
                    'id': row['GameID'],
                    'category': row['Category'],
                    'description': row['Desc'],
                    'NbrGames': row['NbrGames']                   
                }
                
              
                
                game_dict = None
                if game_dict:
                    # If the game_dict is already in the games_by_rating list, append it to the list
                    game_dict['games'].append(game)
                else:
                    # If the game is not on the games_by_rating list, create and add the game to the list
                    games_by_category.append({
                        'category': row['Category'],
                        'description': row['Desc'],
                        'NbrGames': row['NbrGames']
                    })
        
        # The template string must match the file name of the html template
        template = 'games/games_by_category.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "categorygames_list": games_by_category
        }

        return render(request, template, context)
