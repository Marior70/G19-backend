from rest_framework.serializers import ModelSerializer
from .models import IaFunction
from .models import IntArt
from .models import Comment
from .models import Curso
from .models import Alumno
from .models import Usuario
	
class IaFunctionSerializer(ModelSerializer):
   class Meta:
      model = IaFunction
      fields = "__all__"

class IntArtSerializer(ModelSerializer):
   class Meta:
      model = IntArt
      fields = "__all__"

class CommentSerializer(ModelSerializer):
   class Meta:
      model = Comment
      fields = "__all__"

class CursoSerializer(ModelSerializer):
   class Meta:
      model = Curso
      fields = "__all__"

class AlumnoSerializer(ModelSerializer):
   class Meta:
      model = Alumno
      fields = "__all__"

class UsuarioSerializer(ModelSerializer):
   class Meta:
      model = Usuario
      fields = "__all__"