# Matriz de Decisão Tecnológica

## Linguagem/Framework Backend
| Critério (peso) | Opção A (Python/Flask) | Opção B (Node.js/Express) | Opção C (Java/Spring) | Evidência/observação |
|---|---|---|---|---|
| Prazo (3) | 9 (27) | 8 (24) | 4 (12) | Flask é microframework rápido |
| Domínio do time (3) | 9 (27) | 6 (18) | 5 (15) | Time conhece mais Python |
| Custo/licença (2) | 10 (20) | 10 (20) | 10 (20) | Todos open source |
| Segurança (2) | 8 (16) | 8 (16) | 9 (18) | Spring é robusto, mas Flask atende o mínimo |
| Manutenibilidade (2) | 8 (16) | 8 (16) | 9 (18) | Código menor no Flask |
| Infra/compatibilidade (1) | 9 (9) | 9 (9) | 6 (6) | Java exige mais memória |
| **Total ponderado** | **115** | **103** | **89** | Vencedor: Python/Flask |

## Banco de Dados
| Critério (peso) | Opção A (SQLite) | Opção B (PostgreSQL) | Opção C (MongoDB) | Evidência/observação |
|---|---|---|---|---|
| Prazo (3) | 10 (30) | 6 (18) | 7 (21) | SQLite não precisa instalar BD |
| Domínio do time (3) | 9 (27) | 7 (21) | 6 (18) | SQL é bem conhecido |
| Custo/licença (2) | 10 (20) | 8 (16) | 8 (16) | SQLite roda local sem VPS extra |
| Infra/compatibilidade (1) | 10 (10) | 5 (5) | 5 (5) | Zero configuração no SQLite |
| **Total ponderado** | **87** | **60** | **60** | Vencedor: SQLite |
