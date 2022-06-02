from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()
router.register(r"films", viewsets.FilmViewset)
router.register(r"genres", viewsets.GenreViewset)


urlpatterns = [
    path('', include('films.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
