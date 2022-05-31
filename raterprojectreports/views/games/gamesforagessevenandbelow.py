"""Module for generating games suitable for ages 7 and below report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterprojectreports.views.helpers import dict_fetch_all


class GamesForAgesSevenAndBelowList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get games suitable for ages 7 and below
            db_cursor.execute("""
                SELECT  g.description AS Desc,
                        g.age_rec AS Age,
                        g.id AS GameID,
                        g.title AS Title
                FROM raterprojectapi_game AS g
                WHERE g.age_rec < 8                     
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)
    
            games_with_ageseven = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the attributes from the row dictionary
                game = {
                    'id': row['GameID'],
                    'description': row['Desc'],
                    'title': row['Title'],
                    'age': row['Age']                   
                }
                
              
                
                game_dict = None
                if game_dict:
                    # If the game_dict is already in the games_by_rating list, append it to the list
                    game_dict['games'].append(game)
                else:
                    # If the game is not on the games_by_rating list, create and add the game to the list
                    games_with_ageseven.append({
                        'description': row['Desc'],
                        'title': row['Title'],
                        'age': row['Age']
                    })
        
        # The template string must match the file name of the html template
        template = 'games/games_for_ages_seven_and_below.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "agegame_list": games_with_ageseven
        }

        return render(request, template, context)
