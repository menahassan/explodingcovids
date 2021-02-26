from django.urls import path
from . import views
from loading.views import LoadGameView

app_name = 'loading'
urlpatterns = [
    path("", LoadGameView.as_view(), name = "index"),
    path("start", LoadGameView.as_view(), name = "start")
]