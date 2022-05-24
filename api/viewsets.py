from rest_framework import viewsets
from api.serializers import FilmSerializer, GenreSerializer
from films.models import Film, Genre

class FilmViewset(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
