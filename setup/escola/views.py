from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibicao de todos os alunos
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibicao de todos os cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """
    Lista de todas as matriculas
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """
    Lista de matriculas de um aluno
    """

    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    
    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatricula(generics.ListAPIView):
    """
    Lista de matriculas de um aluno
    """

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])
    
    serializer_class = ListaAlunosMatriculaSerializer
