-Projeto Secretaria Web (Python + Django)

Esse projeto foi baseado em como seria um sistema de gerenciamento de uma secretaria escolar, usando Django.

-Implementações
Separei tudo em modelos diferentes (aluno, professor, nota, etc.) porque acho que assim fica mais organizado e fácil de mexer depois. Tentei deixar o admin bem intuitivo, com buscas e filtros. Usei ForeignKey para conectar aluno com responsável e com suas notas, refletindo como isso acontece na realidade. Para evitar erros de digitação, defini opções fixas (choices) nos campos de turma e disciplina. Também incluí validações para CPF e telefone, garantindo que os dados estejam corretos. 

-O que dá pra fazer
É possível cadastrar e gerenciar alunos, professores e responsáveis numa boa. Também dá pra lançar e ver notas por disciplina e bimestre. Coloquei controle de advertências, suspensões e pagamentos pendentes. Tem uma agenda com eventos, provas e feriados, então dá pra se organizar fácil. E no admin dá pra buscar e filtrar tudo rapidinho, sem dor de cabeça.

-Teste
Testei manualmente os principais modelos: cadastro de aluno, lançamento de nota, advertências, suspensões, pagamentos e agenda.
O admin.py foi ajustado para facilitar a compreensão de algumas funções. Todos os nomes do admin foram adaptados. 

-Dificuldades
Minha principal dificuldade foi implementar a funcionalidade de contratos e a conversão para PDF, que acabei não conseguindo concluir. Tentei de várias formas, pesquisei bastante, mas todas as soluções que testei acabaram dando erro. Fora isso, achei o restante bem tranquilo, já que eu já tinha um certo conhecimento sobre a maioria dos comandos.