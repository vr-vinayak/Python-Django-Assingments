from importlib.metadata import requires
from rest_framework import serializers
from .models import Movie

class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    title = serializers.CharField(required=True)
    rating = serializers.DecimalField(required=True, max_digits=5, decimal_places=1)