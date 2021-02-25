from django.urls import path
from . import views
from loading.views import LoadGameView

urlpatterns = [
    path("", LoadGameView.as_view(), name = "index")
]