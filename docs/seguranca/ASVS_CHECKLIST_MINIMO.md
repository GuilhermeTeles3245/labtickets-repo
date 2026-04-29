# Checklist de Segurança Mínima (Baseado no OWASP ASVS)

Aplicamos os seguintes controles de segurança mínimos para o MVP:

1. **[X] Autenticação (V2):** 
   - O sistema exige login para visualizar ou abrir chamados.
   - As senhas não são armazenadas em texto puro (usando hashing SHA256 / pbkdf2 no banco).
   - Há opção de Logout que destrói a sessão.

2. **[X] Controle de Acesso (V4):**
   - Um Solicitante comum não consegue acessar o dashboard gerencial do Coordenador.
   - Apenas o Técnico ou Coordenador podem alterar o status de um chamado para "Concluído".

3. **[X] Validação de Entrada (V5):**
   - Formulários com proteção contra injeção direta de scripts básicos (HTML escaping automático nos templates do Jinja2/Flask).

4. **[X] Proteção de Dados (V9):**
   - Dados sensíveis como senhas não transitam na URL (sempre via POST method).
