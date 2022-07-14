"""Module for generating games lacking images report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterprojectreports.views.helpers import dict_fetch_all


class GamesWithoutPicsList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # Query to get Games without Images
            db_cursor.execute("""
                SELECT  g.id AS GameID,
                        g.title AS Title,
                        g.description AS Desc
                FROM raterprojectapi_game AS g
                LEFT JOIN raterprojectapi_image AS i
                    ON g.id = i.game_id        
                WHERE i.url is NULL                         
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)
    
            games_without_pics = []

            for row in dataset:
                # Create a dictionary called 'game' that includes 
                # the attributes from the 'row' dictionary
                game = {
                    'id': row['GameID'],
                    'description': row['Desc'],
                    'title': row['Title']                   
                }
                
              
                
                game_dict = None
                if game_dict:
                    # If the 'game_dict' is already in the 'games_by_rating' list, append it to the list
                    game_dict['games'].append(game)
                else:
                    # If the game is not on the 'games_by_rating list', create and add the game to the list
                    games_without_pics.append({
                        'description': row['Desc'],
                        'title': row['Title']
                    })
        
        # The template string must match the file name of the html template
        template = 'games/games_without_pics.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "piclessgames_list": games_without_pics
        }

        return render(request, template, context)
