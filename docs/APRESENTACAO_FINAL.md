# Checklist C — Apresentação Final | LabTickets

**Projeto:** LabTickets — Sistema de Chamados de TI  
**Equipe:** Rayllan Guilherme · Pedro Henrique · Refesson Carvalho · Guilherme Teles · Lucas Paixão  
**Data de entrega:** Abril / 2026  
**Repositório:** https://github.com/GuilhermeTeles3245/labtickets-repo

---

## 1. Demo do MVP

O MVP foi demonstrado ao vivo na Sprint Review da Sprint 04. O fluxo completo da aplicação foi apresentado seguindo os três perfis de usuário:

### Fluxo demonstrado

| Passo | Ator        | Ação                                                                                     |
| ----- | ----------- | ---------------------------------------------------------------------------------------- |
| 1     | Solicitante | Acessa `/login`, autentica com `professor / 123`                                         |
| 2     | Solicitante | Abre um novo chamado: Laboratório 3, categoria Hardware, prioridade Alta                 |
| 3     | Técnico     | Faz login com `tecnico1 / 123`, visualiza a fila ordenada por prioridade                 |
| 4     | Técnico     | Clica em **Assumir** — chamado muda para _Em Andamento_ e fica atribuído a ele           |
| 5     | Técnico     | Acessa os detalhes do chamado, adiciona comentário com a solução e clica em **Concluir** |
| 6     | Coordenador | Faz login com `admin / admin`, acessa a página de **Métricas**                           |
| 7     | Coordenador | Visualiza total de chamados abertos por laboratório, categoria e prioridade              |
| 8     | Coordenador | Acessa gerenciamento de usuários: cria, ativa/desativa e exclui contas                   |

### Funcionalidades entregues (15/15 User Stories — 100% do MVP)

- ✅ Login e logout com hash de senha (bcrypt via Werkzeug)
- ✅ Cadastro público de Solicitante
- ✅ Abertura de chamado com laboratório, categoria, prioridade e descrição
- ✅ Dashboard por perfil (Solicitante vê somente os seus; Técnico e Coordenador veem todos)
- ✅ Fila do Técnico ordenada por prioridade (Alta → Média → Baixa)
- ✅ Assumir chamado com 1 clique
- ✅ Mudança de status: Novo → Em Andamento → Concluído
- ✅ Campo de solução ao concluir
- ✅ Sistema de comentários por chamado
- ✅ Exclusão de comentários inadequados (Coordenador)
- ✅ Exclusão de chamados indevidos (Coordenador)
- ✅ Atribuição de técnico pelo Coordenador
- ✅ Filtros e busca por status, laboratório e título
- ✅ Página de Métricas (gráficos por laboratório, categoria, prioridade)
- ✅ Gerenciamento completo de usuários (Coordenador)

---

## 2. Decisões e Trade-offs Explicados

### Decisão 1 — Stack Backend: Python / Flask

**Escolha:** Python + Flask  
**Alternativas avaliadas:** Node.js / Express, Java / Spring Boot

| Critério (peso)       | Flask   | Node.js | Java/Spring |
| --------------------- | ------- | ------- | ----------- |
| Prazo (×3)            | 27      | 24      | 12          |
| Domínio do time (×3)  | 27      | 18      | 15          |
| Custo / licença (×2)  | 20      | 20      | 20          |
| Segurança (×2)        | 16      | 16      | 18          |
| Manutenibilidade (×2) | 16      | 16      | 18          |
| Infra / compat. (×1)  | 9       | 9       | 6           |
| **Total ponderado**   | **115** | **103** | **89**      |

**Trade-off aceito:** Flask não oferece a robustez "de fábrica" do Spring Boot (ex.: sem ORM complexo, sem injeção de dependência nativa), porém o **tempo de entrega** e o **conhecimento do time** superaram essa desvantagem dentro do prazo de 4 Sprints.

---

### Decisão 2 — Banco de Dados: SQLite

**Escolha:** SQLite (via SQLAlchemy)  
**Alternativas avaliadas:** PostgreSQL, MongoDB

| Critério (peso)      | SQLite | PostgreSQL | MongoDB |
| -------------------- | ------ | ---------- | ------- |
| Prazo (×3)           | 30     | 18         | 21      |
| Domínio do time (×3) | 27     | 21         | 18      |
| Custo / licença (×2) | 20     | 16         | 16      |
| Infra / compat. (×1) | 10     | 5          | 5       |
| **Total ponderado**  | **87** | **60**     | **60**  |

**Trade-off aceito:** SQLite não suporta múltiplas escritas concorrentes em alta escala. Para o volume de um campus universitário (dezenas de chamados/dia), isso não representa risco. Em caso de escala, a migração para PostgreSQL via SQLAlchemy é direta (apenas muda a string de conexão).

---

### Decisão 3 — Autenticação: Sessão do Flask + Werkzeug Hash

**Escolha:** `flask.session` + `werkzeug.security.generate_password_hash`  
**Alternativa descartada:** JWT (JSON Web Tokens)

**Racional:** JWT agrega complexidade (refresh tokens, blacklist de tokens) que não se justifica para uma aplicação com server-side rendering. Sessões server-side são mais simples, seguras por padrão (cookie HttpOnly) e suficientes para o MVP.

---

### Decisão 4 — Deploy / Observabilidade: Local + Exportação em arquivo

**Escolha:** Execução local (`python src/app.py`) + log em `usuarios_exportados.txt`  
**Alternativa descartada:** Deploy em nuvem (Heroku, Railway, Render)

**Racional:** O prazo curto e a dependência de configuração de servidor externo tornariam o deploy em nuvem um risco alto. A exportação automática de usuários em arquivo `.txt` atende o requisito de auditoria do Coordenador sem depender de infra externa.

---

## 3. Feedback Coletado e o que Seria Melhorado

### Feedback coletado durante as Sprints

O feedback foi coletado em dois momentos principais:

**Sprint Reviews (equipe + stakeholder simulado — Coordenador):**

| Sprint | Feedback recebido                                                                         |
| ------ | ----------------------------------------------------------------------------------------- |
| 2      | "O cadastro público de alunos é essencial — bom ter isso desde o início."                 |
| 3      | "A fila por prioridade está funcionando, mas seria ótimo ver cores diferentes."           |
| 4      | "A página de métricas foi uma surpresa positiva — atende bem a necessidade de relatório." |
| 4      | "Ficou faltando notificação por e-mail quando o chamado é atualizado."                    |

**Retrospectiva da Sprint 04:**

- ✅ O que foi bem: uso do Flask/SQLite acelerou muito a entrega; divisão de responsabilidades ficou clara.
- 🔧 O que pode melhorar: ausência de testes automatizados (unitários/integração); a UI poderia ser mais responsiva em telas pequenas.

---

### O que seria melhorado em um V2

| #   | Melhoria                                           | Justificativa                                                              |
| --- | -------------------------------------------------- | -------------------------------------------------------------------------- |
| 1   | **Notificação por e-mail** (Flask-Mail / SendGrid) | Usuário não precisa ficar "refreshando" para saber o status do chamado     |
| 2   | **Upload de imagem no chamado**                    | Facilita diagnóstico técnico sem deslocar o técnico ao lab                 |
| 3   | **Testes automatizados** (pytest + Flask testing)  | Garantia de não-regressão ao adicionar novas features                      |
| 4   | **SLA com alerta de prazo**                        | Coordenador seria alertado se um chamado Alta ficasse sem resposta > 4h    |
| 5   | **Deploy em nuvem** (Railway / Render)             | Acesso de qualquer dispositivo sem depender da máquina local do técnico    |
| 6   | **App Mobile** (React Native)                      | Professores normalmente usam celular em sala — UX nativa seria mais fluida |

---

## 4. Métricas Apresentadas

### Métricas de produto (tela de Métricas do LabTickets)

A página `/metricas` (acessível apenas ao Coordenador) exibe as seguintes métricas em tempo real:

| Métrica                      | O que mede                                                 |
| ---------------------------- | ---------------------------------------------------------- |
| Total de chamados por status | Quantos chamados estão em Novo / Em Andamento / Concluído  |
| Chamados por laboratório     | Qual lab concentra mais problemas                          |
| Chamados por categoria       | Distribuição entre Hardware, Software e Rede               |
| Chamados por prioridade      | Proporção entre chamados de prioridade Alta, Média e Baixa |

### Métricas de sucesso do projeto (definidas no Dossiê)

| Métrica                                        | Meta definida           | Resultado no MVP                                           |
| ---------------------------------------------- | ----------------------- | ---------------------------------------------------------- |
| Redução de chamados "verbais"                  | 50% de redução          | 100% dos chamados passam pela plataforma (zero "de boca")  |
| Tickets de prioridade Alta resolvidos em < 24h | 80% da fila prioritária | Fluxo permite resolução assim que técnico assume o chamado |
| User Stories entregues                         | 100% do backlog do MVP  | ✅ 15/15 US entregues nas 4 Sprints                        |

### Métricas de processo Scrum

| Indicador               | Resultado                                                     |
| ----------------------- | ------------------------------------------------------------- |
| Sprints realizadas      | 4 (Planning → Daily → Review → Retro em cada uma)             |
| Velocidade do time      | Sprint 1: Setup · S2: 3 US · S3: 4 US · S4: 8 US (aceleração) |
| Itens do backlog        | 15 concluídos · 5 cortados (backlog futuro documentado)       |
| ADRs registradas        | 4 (Stack, Banco de Dados, Autenticação, Deploy)               |
| Descobertas (Discovery) | 8 descobertas documentadas no DISCOVERY_LOG.md                |

---

_Documento gerado para entrega da atividade PBL — Métodos Ágeis com Scrum._
