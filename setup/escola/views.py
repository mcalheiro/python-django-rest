from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibicao de todos os alunos
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibicao de todos os cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    """
    Lista de todas as matriculas
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """
    Lista de matriculas de um aluno
    """

    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatricula(generics.ListAPIView):
    """
    Lista de matriculas de um aluno
    """

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])
    
    serializer_class = ListaAlunosMatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
