from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from .models import Responsavel, Aluno, Professor, Bimestre, Nota, AtividadePendente, EventoExtracurricular, PagamentoPendente, Advertencia, Suspensao, EventoCalendario, EmprestimoLivro, Livro
from .serializers import ResponsavelSerializer, AlunoSerializer, ProfessorSerializer, BimestreSerializer, NotaSerializer, AtividadePendenteSerializer, EventoExtracurricularSerializer, PagamentoPendenteSerializer, AdvertenciaSerializer, SuspensaoSerializer, EventoCalendarioSerializer, EmprestimoLivroSerializer, LivroSerializer
from .permissions import IsSecretaria, IsProfessor, IsResponsavel, IsAluno
from rest_framework.decorators import action

# Funções de views HTML
def calendario_academico(request):
    eventos = EventoCalendario.objects.order_by('data')
    return render(request, 'calendario.html', {'eventos': eventos})

def media_aluno_disciplina(request, aluno_id, disciplina):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    media = aluno.media_por_disciplina(disciplina)
    return render(request, 'media_aluno.html', {
        'aluno': aluno,
        'disciplina': disciplina,
        'media': media,
    })


# ViewSets de CRUD Total (Apenas para a Secretaria)
# As permissões para Aluno, Professor e Responsavel são de nivel de objeto,
# entao vamos lidar com elas com get_queryset.
class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
    permission_classes = [IsSecretaria]

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsSecretaria]

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsSecretaria]

# ViewSets com Permissões Múltiplas e Filtros de Objeto
class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    def get_queryset(self):
        user = self.request.user
        if IsSecretaria().has_permission(self.request, self) or IsProfessor().has_permission(self.request, self):
            return Nota.objects.all()
        elif IsResponsavel().has_permission(self.request, self):
            return Nota.objects.filter(aluno__Responsavel__user=user)
        elif IsAluno().has_permission(self.request, self):
            return Nota.objects.filter(aluno__user=user)
        
        return Nota.objects.none() # Retorna um queryset vazio se não houver permissão

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSecretaria | IsProfessor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class AtividadePendenteViewSet(viewsets.ModelViewSet):
    queryset = AtividadePendente.objects.all()
    serializer_class = AtividadePendenteSerializer

    def get_queryset(self):
        user = self.request.user
        if IsSecretaria().has_permission(self.request, self) or IsProfessor().has_permission(self.request, self):
            return AtividadePendente.objects.all()
        elif IsResponsavel().has_permission(self.request, self):
            return AtividadePendente.objects.filter(aluno__Responsavel__user=user)
        elif IsAluno().has_permission(self.request, self):
            return AtividadePendente.objects.filter(aluno__user=user)
        
        return AtividadePendente.objects.none()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSecretaria | IsProfessor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class PagamentoPendenteViewSet(viewsets.ModelViewSet):
    queryset = PagamentoPendente.objects.all()
    serializer_class = PagamentoPendenteSerializer

    def get_queryset(self):
        user = self.request.user
        if IsSecretaria().has_permission(self.request, self):
            return PagamentoPendente.objects.all()
        elif IsResponsavel().has_permission(self.request, self):
            return PagamentoPendente.objects.filter(aluno__Responsavel__user=user)
        
        return PagamentoPendente.objects.none()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSecretaria]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class AdvertenciaViewSet(viewsets.ModelViewSet):
    queryset = Advertencia.objects.all()
    serializer_class = AdvertenciaSerializer

    def get_queryset(self):
        user = self.request.user
        if IsSecretaria().has_permission(self.request, self):
            return Advertencia.objects.all()
        elif IsResponsavel().has_permission(self.request, self):
            return Advertencia.objects.filter(aluno__Responsavel__user=user)
        elif IsAluno().has_permission(self.request, self):
            return Advertencia.objects.filter(aluno__user=user)
        
        return Advertencia.objects.none()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSecretaria]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class SuspensaoViewSet(viewsets.ModelViewSet):
    queryset = Suspensao.objects.all()
    serializer_class = SuspensaoSerializer
    
    # Lógica de get_queryset é a mesma do AdvertenciaViewSet
    def get_queryset(self):
        user = self.request.user
        if IsSecretaria().has_permission(self.request, self):
            return Suspensao.objects.all()
        elif IsResponsavel().has_permission(self.request, self):
            return Suspensao.objects.filter(aluno__Responsavel__user=user)
        elif IsAluno().has_permission(self.request, self):
            return Suspensao.objects.filter(aluno__user=user)
        
        return Suspensao.objects.none()
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSecretaria]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


# ViewSets de Visualização para todos os autenticados (ReadOnly)
class EventoExtracurricularViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventoExtracurricular.objects.all()
    serializer_class = EventoExtracurricularSerializer
    permission_classes = [IsAuthenticated]

class EventoCalendarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventoCalendario.objects.all()
    serializer_class = EventoCalendarioSerializer
    permission_classes = [IsAuthenticated]

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    # Permissões: Secretaria total, outros apenas view
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSecretaria]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class EmprestimoLivroViewSet(viewsets.ModelViewSet):
    queryset = EmprestimoLivro.objects.all()
    serializer_class = EmprestimoLivroSerializer
    # Permissões: Secretaria total, outros apenas view
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSecretaria]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class BimestreViewSet(viewsets.ModelViewSet):
    queryset = Bimestre.objects.all()
    serializer_class = BimestreSerializer
    # Permissões: Secretaria total, outros apenas view
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSecretaria]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()