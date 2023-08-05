from django.shortcuts import render
from .models import Movie
from rest_framework import status
from .paginator import CustomPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieRatingSerializer
from .utils import _movies_search

class MovieViewset(ModelViewSet):
    serializer_class = MovieRatingSerializer
    queryset = Movie.objects.all()
    pagination_class = [CustomPagination,]

    @action(detail=False, methods=['get'], url_path='movie-search')
    def movies_search(self, request, *args, **kwargs):
        query_params = request.query_params
        title = query_params.get('title', '')
        year = query_params.get('year', '')
        release_date = query_params.get('release_date', '')

        # Create a dictionary to hold the query parameters you want to send to the API
        api_query_params = {
            'query': title,
            'year': year,
            'release_date': release_date,
            # Add any other query parameters you want to include
        }
        movies = _movies_search(api_query_params)
        return Response(data={'message': 'success', 'data':movies, 'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'], url_path='add-movie-rating')
    def add_movie_rating(self, request, *args, **kwargs):
        title = request.data.get('title')
        rating = request.data.get('rating')
        
        if not title or rating is None:
            return Response({'error': 'Title and rating are required.'}, status=400)
        
        if rating < 0 or rating > 5:
            return Response({'error': 'Rating must be between 0 and 5.'}, status=400)
        
        movie, created = Movie.objects.get_or_create(title=title)
        movie.rating = rating
        movie.save()
        movie_serialier = MovieRatingSerializer(movie)
        return Response({'message': 'Movie rated successfully.', 'data': movie_serialier.data, 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)