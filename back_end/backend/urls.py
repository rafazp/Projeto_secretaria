from django.contrib import admin
from django.urls import path, include
from api import views  # Importe suas views do app correto
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('admin/', admin.site.urls), #URL para acesso ao painel administrativo do Django
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('media/<int:aluno_id>/<str:disciplina>/', views.media_aluno_disciplina, name='media_aluno_disciplina'), # URL para exibir a média do aluno em uma disciplina específica
    path('calendario/', views.calendario_academico, name='calendario_academico'), # URL para exibir o calendário acadêmico com os eventos
    path('api/', include('api.urls')),
]