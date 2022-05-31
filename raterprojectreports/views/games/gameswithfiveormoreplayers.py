"""Module for generating games for 5+ players report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterprojectreports.views.helpers import dict_fetch_all


class GamesWithFiveOrMorePlayersList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get games for 5+ players
            db_cursor.execute("""
                SELECT  g.description AS Desc,
                        g.title AS Title, 
                        g.number_of_players AS Players,
                        g.id AS GameID
                FROM raterprojectapi_game AS g
                WHERE g.number_of_players > 5                        
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)
    
            games_with_fiveplus = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the attributes from the row dictionary
                game = {
                    'id': row['GameID'],
                    'description': row['Desc'],
                    'title': row['Title'],
                    'number_of_players': row['Players']                   
                }
                
              
                
                game_dict = None
                if game_dict:
                    # If the game_dict is already in the games_by_rating list, append it to the list
                    game_dict['games'].append(game)
                else:
                    # If the game is not on the games_by_rating list, create and add the game to the list
                    games_with_fiveplus.append({
                        'description': row['Desc'],
                        'title': row['Title'],
                        'number_of_players': row['Players']
                    })
        
        # The template string must match the file name of the html template
        template = 'games/games_with_five_or_more_players.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "fiveplusgame_list": games_with_fiveplus
        }

        return render(request, template, context)
