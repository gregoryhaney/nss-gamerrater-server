"""Module for generating top game reviewers report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterprojectreports.views.helpers import dict_fetch_all


class TopGameReviewersList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get Top game reviewers
            db_cursor.execute("""
                    SELECT  gr.handle AS Handle,
                            COUNT(r.id) AS NbrReviews,
                            r.id AS ReviewID
                    FROM raterprojectapi_review AS r
                    JOIN raterprojectapi_gamer AS gr
                    ON r.gamer_id = gr.id
                    GROUP BY gr.handle
                    ORDER BY r.id DESC                       
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)
    
            games_by_NbrReviews = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the attributes from the row dictionary
                game = {
                    'id': row['ReviewID'],
                    'handle': row['Handle'],
                    'NbrReviews': row['NbrReviews']           
                }
                
              
                
                game_dict = None
                if game_dict:
                    # If the game_dict is already in the games_by_rating list, append it to the list
                    game_dict['games'].append(game)
                else:
                    # If the game is not on the games_by_rating list, create and add the game to the list
                    games_by_NbrReviews.append({
                        'handle': row['Handle'],
                        'NbrReviews': row['NbrReviews']
                    })
        
        # The template string must match the file name of the html template
        template = 'games/top_game_reviewers.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "reviewers_list": games_by_NbrReviews
        }

        return render(request, template, context)
