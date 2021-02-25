from django.urls import path
from . import views
from board.views import CreateGameView
app_name = 'board'
urlpatterns = [
    path("", CreateGameView.as_view(), name = "index")
]
