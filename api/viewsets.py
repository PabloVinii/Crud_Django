from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import FilmSerializer, GenreSerializer
from films.models import Film, Genre


class FilmViewset(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    permission_classes = [IsAuthenticated]


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    permission_classes = [IsAuthenticated]
    # falta o pop-up pra se autenticar
    # e adicionar token no admin
