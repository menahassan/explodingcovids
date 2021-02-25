from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls', namespace='board')),
    path('', include("loading.urls"))
]
