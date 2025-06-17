from django.shortcuts import render, get_object_or_404
from .models import Aluno, Nota, EventoCalendario

# Função que exibe o calendário acadêmico
def calendario_academico(request):
    eventos = EventoCalendario.objects.order_by('data')
    return render(request, 'calendario.html', {'eventos': eventos})

# Função que calcula e exbe a média de um aluno em uma disciplina especifica
def media_aluno_disciplina(request, aluno_id, disciplina):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    media = aluno.media_por_disciplina(disciplina)
    return render(request, 'media_aluno.html', {
        'aluno': aluno,
        'disciplina': disciplina,
        'media': media,
    })

