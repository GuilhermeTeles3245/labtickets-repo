# ADR-004 — Deploy e Observabilidade

• **Status:** Aceito
• **Data:** 18/10/2026
• **Decisores:** Equipe de Desenvolvimento

**Contexto**
Precisamos de um deploy rápido, grátis, e métricas simples.

**Decisão**
O deploy será feito rodando o Flask com Gunicorn em uma VPS Linux usando Docker, ou diretamente via script. Para o MVP local, usaremos apenas a execução direta (`python app.py`). Os logs serão mantidos em arquivos simples.

**Alternativas consideradas**
• Opção A: Gunicorn local / Docker
• Opção B: Heroku / PythonAnywhere
• Opção C: AWS EC2

**Justificativa**
PythonAnywhere ou AWS podem ter custos ocultos ou limitação de uso grátis que atrapalhariam a avaliação no fim do semestre. O deploy local/Docker numa VPS garante total controle.

**Consequências**
• Positivas: Controle absoluto do ambiente.
• Negativas: Precisaremos configurar o servidor Linux (Nginx/Gunicorn) manualmente se formos para produção real.
