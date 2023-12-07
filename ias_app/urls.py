from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IaFunctionViewSet
from .views import IntArtViewSet
from .views import CommentViewSet
from .views import CursoViewSet
from .views import AlumnoViewSet

router = DefaultRouter()
router.register(r'/iaFunction', IaFunctionViewSet, basename='iaFunction')
router.register(r'/intArt', IntArtViewSet, basename='intArt')
router.register(r'/comment', CommentViewSet, basename='comment')
router.register(r'/curso', CursoViewSet, basename='curso')
router.register(r'/alumno', AlumnoViewSet, basename='alumno')

urlpatterns = [
    path('', include(router.urls)),
]