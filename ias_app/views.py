from rest_framework.viewsets import ModelViewSet

from .models import IaFunction
from .serializers import IaFunctionSerializer

from .models import IntArt
from .serializers import IntArtSerializer

from .models import Comment
from .serializers import CommentSerializer

from .models import Curso
from .serializers import CursoSerializer 

from .models import Alumno
from .serializers import AlumnoSerializer

class IaFunctionViewSet(ModelViewSet):
   queryset = IaFunction.objects.all()
   serializer_class = IaFunctionSerializer

class IntArtViewSet(ModelViewSet):
   queryset = IntArt.objects.all()
   serializer_class = IntArtSerializer

class CommentViewSet(ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer

class CursoViewSet(ModelViewSet):
   queryset = Curso.objects.all()
   serializer_class = CursoSerializer

class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    