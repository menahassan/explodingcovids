from django.urls import path
from . import views
from board.views import CreateGameView

urlpatterns = [
    path("", CreateGameView.as_view(), name = "index")
]
