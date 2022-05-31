from django.urls import path
from .views import TopGamesByRatingList
from .views import BottomGamesByRatingList
from .views import GamesWithFiveOrMorePlayersList
from .views import MostReviewedGameList
from .views import PlayerWithMostGamesList
from .views import GamesForAgesSevenAndBelowList
from .views import GamesWithoutPicsList
from .views import TopGameReviewersList
from .views import GamesPerCategoryList


urlpatterns = [
    path('reports/topgamesbyrating', TopGamesByRatingList.as_view()),
    path('reports/bottomgamesbyrating', BottomGamesByRatingList.as_view()),
    path('reports/gameswithfiveormoreplayers', GamesWithFiveOrMorePlayersList.as_view()),
    path('reports/mostreviewedgame', MostReviewedGameList.as_view()),
    path('reports/playerwithmostgames', PlayerWithMostGamesList.as_view()),
    path('reports/gamesforagessevenandbelow', GamesForAgesSevenAndBelowList.as_view()),
    path('reports/gameswithoutpics', GamesWithoutPicsList.as_view()),
    path('reports/topgamereviewers', TopGameReviewersList.as_view()),
    path('reports/gamespercategory', GamesPerCategoryList.as_view()),
]
