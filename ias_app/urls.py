from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IaFunctionViewSet
from .views import IaViewSet
from .views import CommentViewSet
from .views import CursoViewSet
from .views import AlumnoViewSet
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(r'iaFunction', IaFunctionViewSet, basename='iaFunction')
router.register(r'iasList', IaViewSet, basename='iasList')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'curso', CursoViewSet, basename='curso')
router.register(r'alumno', AlumnoViewSet, basename='alumno')
router.register(r'login', UsuarioViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]