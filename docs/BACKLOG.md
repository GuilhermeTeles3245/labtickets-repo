# BACKLOG — LabTickets

Histórico completo do Product Backlog e do Board Scrum por Sprint.

> **Legenda de Status:**
> - `✅ Concluído`   — entregue e validado
> - `🔵 Em andamento` — em progresso na Sprint atual
> - `⬜ Backlog`      — previsto para sprints futuras

---

## Product Backlog Priorizado (RICE)

| ID     | User Story                                                                                              | Prioridade RICE | Sprint   | Status        |
|--------|---------------------------------------------------------------------------------------------------------|-----------------|----------|---------------|
| US-01  | Como solicitante, quero fazer login com usuário e senha para acessar meus chamados.                     | Alta            | Sprint 2 | ✅ Concluído  |
| US-02  | Como visitante, quero criar minha própria conta de Solicitante para não depender do admin.              | Alta            | Sprint 2 | ✅ Concluído  |
| US-03  | Como solicitante, quero criar um chamado informando laboratório, categoria, prioridade e descrição.     | Alta            | Sprint 3 | ✅ Concluído  |
| US-04  | Como solicitante, quero visualizar o status dos meus chamados em um dashboard.                          | Alta            | Sprint 3 | ✅ Concluído  |
| US-05  | Como técnico, quero ver a fila de todos os chamados abertos, ordenada por prioridade.                   | Alta            | Sprint 3 | ✅ Concluído  |
| US-06  | Como técnico, quero assumir um chamado com um clique para indicar que estou resolvendo.                 | Alta            | Sprint 3 | ✅ Concluído  |
| US-07  | Como técnico, quero alterar o status de um chamado (Novo → Andamento → Concluído).                     | Alta            | Sprint 4 | ✅ Concluído  |
| US-08  | Como técnico, quero registrar a solução aplicada ao concluir um chamado.                                | Média           | Sprint 4 | ✅ Concluído  |
| US-09  | Como qualquer usuário, quero adicionar comentários dentro de um chamado para comunicação.               | Média           | Sprint 4 | ✅ Concluído  |
| US-10  | Como coordenador, quero visualizar relatórios com chamados por laboratório, categoria e prioridade.     | Média           | Sprint 4 | ✅ Concluído  |
| US-11  | Como coordenador, quero atribuir um técnico específico a um chamado.                                   | Média           | Sprint 4 | ✅ Concluído  |
| US-12  | Como coordenador, quero criar, ativar/desativar e deletar contas de usuários.                          | Alta            | Sprint 2 | ✅ Concluído  |
| US-13  | Como coordenador, quero deletar comentários inadequados de um chamado.                                  | Baixa           | Sprint 4 | ✅ Concluído  |
| US-14  | Como coordenador, quero deletar um chamado indevidamente aberto.                                        | Baixa           | Sprint 4 | ✅ Concluído  |
| US-15  | Como qualquer usuário, quero filtrar e buscar chamados por status, laboratório e título.                | Média           | Sprint 4 | ✅ Concluído  |

---

## Histórico por Sprint

### Sprint 1 — Planejamento e Arquitetura
**Sprint Goal:** Estruturar o projeto, definir tecnologias e preparar ambiente.

| Item                                                                          | Tipo          | Status |
|-------------------------------------------------------------------------------|---------------|--------|
| Discovery com professores e coordenadores                                     | Pesquisa      | ✅     |
| Redigir ADR-001 (Stack), ADR-002 (BD), ADR-003 (Auth), ADR-004 (Deploy)       | Documentação  | ✅     |
| Criar estrutura de pastas do repositório                                      | Setup         | ✅     |
| Redigir Dossiê do Projeto (12 user stories, stakeholders, jornada)            | Documentação  | ✅     |
| Configurar repositório Git                                                    | Setup         | ✅     |

---

### Sprint 2 — Autenticação e Usuários
**Sprint Goal:** Sistema de login funcionando com os 3 perfis de usuário.

| Item                                                       | User Story | Status |
|------------------------------------------------------------|------------|--------|
| Modelos do banco de dados (Usuario, Chamado, Comentario)   | —          | ✅     |
| Rota de login com validação de hash                        | US-01      | ✅     |
| Rota de logout com destruição de sessão                    | US-01      | ✅     |
| Página de cadastro público (perfil fixo: Solicitante)      | US-02      | ✅     |
| Painel de gerenciamento de usuários (Coordenador)          | US-12      | ✅     |
| Criar / ativar / desativar / deletar contas                | US-12      | ✅     |
| Controle de acesso por rotas (decorators)                  | —          | ✅     |

---

### Sprint 3 — Abertura e Fila de Chamados
**Sprint Goal:** Professores podem abrir chamados e técnicos veem a fila.

| Item                                                                   | User Story | Status |
|------------------------------------------------------------------------|------------|--------|
| Formulário de abertura de chamado (lab, categoria, prioridade)         | US-03      | ✅     |
| Dashboard do Solicitante (somente os próprios chamados)                | US-04      | ✅     |
| Dashboard do Técnico (fila completa, ordenada por prioridade)          | US-05      | ✅     |
| Dashboard do Coordenador (todos os chamados)                           | US-05      | ✅     |
| Filtros por status, laboratório e busca por título                     | US-15      | ✅     |
| Assumir chamado com 1 clique (técnico)                                 | US-06      | ✅     |

---

### Sprint 4 — Resolução, Relatórios e Refinamento
**Sprint Goal:** Fluxo completo até a conclusão do chamado + relatórios para coordenador.

| Item                                                         | User Story | Status |
|--------------------------------------------------------------|------------|--------|
| Página de detalhes do chamado                                | US-07      | ✅     |
| Campo de solução ao concluir chamado                         | US-08      | ✅     |
| Sistema de comentários por chamado                           | US-09      | ✅     |
| Deletar comentário (coordenador)                             | US-13      | ✅     |
| Deletar chamado (coordenador)                                | US-14      | ✅     |
| Atribuir técnico (coordenador)                               | US-11      | ✅     |
| Página de Métricas (por lab, categoria, prioridade)          | US-10      | ✅     |
| Exportação automática de usuários (usuarios_exportados.txt)  | —          | ✅     |
| Refinamento da UI (sidebar, Bootstrap Icons, cards)          | —          | ✅     |

---

## Itens fora do MVP (Backlog futuro)

| ID    | Descrição                                              | Motivo do corte                                  |
|-------|--------------------------------------------------------|--------------------------------------------------|
| F-01  | Notificação por e-mail ao abrir/atualizar chamado      | Fora do prazo de 4 Sprints                       |
| F-02  | Upload de foto/print de erro no chamado                | Complexidade de armazenamento                    |
| F-03  | App Mobile (React Native / Flutter)                    | Stack fora do escopo do MVP                      |
| F-04  | SLA com alertas de prazo estourado                     | Requer lógica de agendamento (Celery)            |
| F-05  | Integração com SSO institucional (Google/Microsoft)    | Dependência de TI da faculdade                   |
