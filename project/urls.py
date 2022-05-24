from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import viewsets

router = routers.SimpleRouter()
router.register(r"films", viewsets.FilmViewset)
router.register(r"genres", viewsets.GenreViewset)


urlpatterns = [
    path('', include('films.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
