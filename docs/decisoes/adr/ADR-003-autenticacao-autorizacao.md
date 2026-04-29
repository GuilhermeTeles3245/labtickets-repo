# ADR-003 — Autenticação e Autorização

• **Status:** Aceito
• **Data:** 18/10/2026
• **Decisores:** Equipe de Desenvolvimento

**Contexto**
O sistema exige que existam os perfis: Solicitante, Técnico e Coordenador, cada um com permissões diferentes para ver e editar os chamados.

**Decisão**
Foi escolhido utilizar autenticação baseada em sessão gerada pelo próprio Flask (`flask-login` ou controle de sessão manual) e senhas hasheadas com `werkzeug.security`.

**Alternativas consideradas**
• Opção A: Sessão nativa do Flask
• Opção B: JWT (JSON Web Tokens)
• Opção C: Integração com SSO da faculdade (Google/Microsoft)

**Justificativa**
Implementar JWT exige mais complexidade no Frontend e Backend. O SSO da faculdade demandaria permissões que não temos no momento. A sessão local resolve o requisito com mínimo esforço.

**Consequências**
• Positivas: Simples de implementar e testar.
• Negativas: Não é uma API "stateless" verdadeira se formos fazer um App Mobile depois.
• Riscos e mitigação: Roubo de cookies de sessão. Mitigação: Configurar `HttpOnly` nos cookies.
