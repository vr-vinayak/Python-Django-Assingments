from django.urls import path, include
from rest_framework import routers
from .views import MovieViewset

router = routers.DefaultRouter()
router.register('movies', MovieViewset, basename='movie-rating')

app_name = 'movie'

urlpatterns = [
    path('', include(router.urls)),
]
