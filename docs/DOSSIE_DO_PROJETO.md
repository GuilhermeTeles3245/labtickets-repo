# Dossiê do Projeto

**1. Resumo executivo**
O sistema LabTickets é uma aplicação web focada na abertura, acompanhamento e resolução de chamados de suporte técnico para os laboratórios de TI. O MVP permite que professores e alunos abram tickets de forma organizada, enquanto técnicos e coordenadores visualizam a fila de prioridades, resolvem os problemas e extraem métricas. Isso elimina o caos de solicitações "de boca" ou WhatsApp e traz previsibilidade às manutenções.

**2. Problema e objetivos**
- **Problema:** A Coordenação de Laboratórios não tem controle, fila ou métricas para chamados de manutenção, resultando em retrabalho, perda de histórico e indisponibilidade para aulas.
- **Objetivos:** Centralizar 100% dos chamados em uma única plataforma, fornecendo status visível para quem abriu o ticket e relatórios simples para a coordenação.
- **Métrica de sucesso:** Redução de 50% nos chamados "verbais" e resolução de 80% dos tickets da fila prioritária em menos de 24 horas.

**3. Stakeholders e perfis de usuário**
- **Stakeholders:** Diretor do Campus, Professores, Alunos e Equipe de Manutenção.
- **Perfis de Usuário:**
  1. *Solicitante* (Professores/Alunos): Pode abrir chamados e visualizar o status.
  2. *Técnico*: Pode pegar chamados da fila e mudar o status para Em Andamento ou Concluído.
  3. *Coordenador*: Pode visualizar relatórios e todos os chamados.

**4. Jornada AS-IS e TO-BE**
- **AS-IS (Como é):** Professor nota defeito -> Procura técnico no corredor ou manda WhatsApp -> Técnico esquece ou anota no papel -> Professor fica sem retorno -> Aula é prejudicada. *Dores:* Falta de feedback, esquecimento.
- **TO-BE (Como será):** Professor acessa o app -> Abre chamado rápido (com foto, se precisar) -> Recebe notificação visual de status na dashboard -> Técnico vê na fila por prioridade -> Resolve e fecha o ticket. *Ganhos:* Transparência, fila organizada.

**5. Requisitos funcionais (12 User Stories)**
1. Como solicitante, quero fazer login com e-mail e senha para acessar meus chamados.
2. Como solicitante, quero criar um novo chamado informando o laboratório e a descrição.
3. Como solicitante, quero classificar o chamado (rede, hardware, software) para direcionar melhor o atendimento.
4. Como solicitante, quero ver o status do meu chamado (Novo, Andamento, Concluído).
5. Como técnico, quero ver uma fila de chamados abertos ordenada por prioridade.
6. Como técnico, quero atribuir um chamado a mim mesmo para começar a trabalhar nele.
7. Como técnico, quero adicionar um comentário no chamado para relatar a solução aplicada.
8. Como técnico, quero alterar o status do chamado para Concluído.
9. Como coordenador, quero ver quantos chamados foram abertos no mês.
10. Como coordenador, quero visualizar os chamados filtrados por laboratório.
11. Como usuário, quero poder redefinir minha senha se esquecê-la.
12. Como usuário, quero um design responsivo para usar a plataforma do meu celular.

**6. Requisitos não-funcionais**
- **Segurança:** As senhas devem ser criptografadas (hash) no banco de dados. Controle de acesso rigoroso por rotas de perfil.
- **Desempenho:** A página de fila de chamados deve carregar em menos de 2 segundos.
- **Disponibilidade:** O sistema deve ter uptime de 99% em horário comercial.

**7. Priorização do backlog (RICE)**
- *Login e Criação de Chamados:* Reach (Alto), Impact (Alto), Confidence (Alto), Effort (Médio). Prioridade: 1
- *Fila para Técnicos:* Reach (Médio), Impact (Alto), Confidence (Alto), Effort (Médio). Prioridade: 2
- *Dashboard de Relatórios:* Reach (Baixo), Impact (Médio), Confidence (Alto), Effort (Alto). Prioridade: 3

**8. Matriz de decisão tecnológica**
*Veja o arquivo `/docs/decisoes/MATRIZ_DECISAO_TECNOLOGICA.md`*

**9. Decisões registradas em ADR**
*Veja os arquivos na pasta `/docs/decisoes/adr/`*

**10. Arquitetura em C4**
*Veja os arquivos na pasta `/docs/arquitetura/`*

**11. Checklist de segurança mínima**
*Veja o arquivo `/docs/seguranca/ASVS_CHECKLIST_MINIMO.md`*
