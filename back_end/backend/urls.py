from django.contrib import admin
from django.urls import path
from api import views  # Importe suas views do app correto

urlpatterns = [
    path('admin/', admin.site.urls), #URL para acesso ao painel administrativo do Django
    path('media/<int:aluno_id>/<str:disciplina>/', views.media_aluno_disciplina, name='media_aluno_disciplina'), # URL para exibir a média do aluno em uma disciplina específica
    path('calendario/', views.calendario_academico, name='calendario_academico'), # URL para exibir o calendário acadêmico com os eventos
]