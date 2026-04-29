# C4 Model - Nível de Containers

![C4 Containers](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/C4_model_Container_diagram_example.svg/1200px-C4_model_Container_diagram_example.svg.png)
*(Imagem ilustrativa)*

## Explicação

**Containers Principais:**
1. **Web App (Frontend):** 
   - HTML, CSS (Bootstrap).
   - Roda no navegador do usuário.
   - Fornece a interface visual responsiva.
2. **Web Application (Backend):** 
   - Python / Flask.
   - Responsável pela regra de negócios, autenticação, controle de fila e roteamento.
3. **Database:** 
   - SQLite.
   - Armazena as tabelas (Users, Tickets, Comments). Fica no mesmo disco da Web Application.
