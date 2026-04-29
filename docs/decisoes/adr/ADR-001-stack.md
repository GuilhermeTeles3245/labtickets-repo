# ADR-001 — Stack Tecnológica Principal

• **Status:** Aceito
• **Data:** 18/10/2026
• **Decisores:** Equipe de Desenvolvimento

**Contexto**
Precisamos de uma stack para entregar o MVP em 4 Sprints, com custo zero e hospedagem em VPS simples.

**Decisão**
Foi escolhido utilizar Python com o microframework Flask para o backend, e HTML/CSS puro com Bootstrap para o frontend.

**Alternativas consideradas**
• Opção A: Python/Flask + Bootstrap
• Opção B: Node.js/Express + React
• Opção C: Java/Spring + Angular

**Justificativa (por que essa opção?)**
O time tem mais fluência em Python. Além disso, o Flask permite criar rotas rapidamente sem muito código ("boilerplate"). O uso de Bootstrap acelera o design responsivo sem precisar configurar o React.

**Consequências (impactos)**
• Positivas: Desenvolvimento muito rápido, fácil de rodar localmente.
• Negativas: Para sistemas gigantes, o Flask pode ficar bagunçado (precisa de boa arquitetura).
• Riscos e mitigação: Risco de código não estruturado. Mitigação: Uso de Blueprints do Flask caso cresça, mas para MVP 1 arquivo `app.py` bem organizado serve.

**Referências**
- Documentação do Flask: https://flask.palletsprojects.com/
