# ADR-002 — Banco de Dados

• **Status:** Aceito
• **Data:** 18/10/2026
• **Decisores:** Equipe de Desenvolvimento

**Contexto**
O sistema precisa armazenar usuários, chamados e comentários. Temos uma restrição de R$ 0 de orçamento e uma VPS simples, então precisamos de algo leve e sem custo.

**Decisão**
Foi escolhido utilizar o SQLite.

**Alternativas consideradas**
• Opção A: SQLite
• Opção B: PostgreSQL
• Opção C: MySQL

**Justificativa**
O SQLite salva todos os dados em um único arquivo local. Para um MVP com uso restrito ao campus, o tráfego não será alto o suficiente para justificar a instalação e manutenção de um banco de dados em servidor dedicado como o PostgreSQL, que consumiria muita RAM da nossa VPS básica.

**Consequências**
• Positivas: Zero configuração. Backup fácil (só copiar o arquivo `.db`).
• Negativas: Não suporta alta concorrência de escrita.
• Riscos e mitigação: Risco de corromper o banco se muitas pessoas acessarem juntas. Mitigação: O volume de chamados de laboratório é pequeno, não haverá milhares de requisições por segundo.
