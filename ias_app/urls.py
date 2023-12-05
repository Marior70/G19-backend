from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IaFunctionViewSet
from .views import IntArtViewSet
from .views import CommentViewSet
from .views import CursoViewSet
from .views import AlumnoViewSet

router = DefaultRouter()
router.register(r'api/iaFunction', IaFunctionViewSet, basename='iaFunction')
router.register(r'api/intArt', IntArtViewSet, basename='intArt')
router.register(r'api/comment', CommentViewSet, basename='comment')
router.register(r'api/curso', CursoViewSet, basename='curso')
router.register(r'api/alumno', AlumnoViewSet, basename='alumno')

urlpatterns = [
    path('', include(router.urls)),
]