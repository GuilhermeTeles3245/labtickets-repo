# LabTickets - Sistema de Chamados de TI

Este repositório contém o código do MVP e toda a documentação da atividade PBL de Métodos Ágeis com Scrum.
O objetivo do projeto é resolver o problema da Coordenação de Laboratórios de TI, que recebia chamados por WhatsApp e "de boca", sem histórico ou fila organizada.

## Equipe

| #   | Nome                            | Papel               | Responsabilidade                       |
| --- | ------------------------------- | ------------------- | -------------------------------------- |
| 1   | Rayllan Guilherme Brito Ribeiro | Facilitador / Líder | Garante os ritos do Scrum              |
| 2   | Pedro Henrique Gomes Dutra      | Pesquisador         | Coleta dados com alunos e stakeholders |
| 3   | Refesson da Silva Carvalho      | Analista            | Traduz necessidades em tarefas         |
| 4   | Guilherme Teles Pacheco         | Tech Lead           | Guia o desenvolvimento técnico         |
| 5   | Lucas Paixão Cardoso Luis       | Editor / QA         | Revisa o código e a documentação       |

## Como rodar o projeto localmente

### 1. Pré-requisitos

- Python 3.8 ou superior instalado.

### 2. Instalação das dependências

```bash
pip install flask flask-sqlalchemy werkzeug
```

### 3. Execução

Na pasta raiz do projeto, execute:

```bash
python src/app.py
```

O banco de dados (`labtickets.db`) é criado automaticamente na primeira execução.

### 4. Acesso

Acesse no navegador: `http://localhost:5000`

### 5. Perfis de Acesso (criados automaticamente)

| Usuário     | Senha   | Perfil      |
| ----------- | ------- | ----------- |
| `admin`     | `admin` | Coordenador |
| `tecnico1`  | `123`   | Técnico     |
| `professor` | `123`   | Solicitante |

> Novos Solicitantes podem criar conta diretamente pelo link "Criar conta" na tela de login.

### 6. Ver lista de usuários cadastrados

```bash
python src/exportar_usuarios.py
```

Gera o arquivo `usuarios_exportados.txt` com todos os usuários. Este arquivo também é atualizado automaticamente a cada novo cadastro ou deleção.

---

## Documentação

Toda a documentação exigida encontra-se na pasta [`/docs`](/docs):

| Arquivo                                                                               | Descrição                                                         |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [DOSSIE_DO_PROJETO.md](docs/DOSSIE_DO_PROJETO.md)                                     | Dossiê completo (user stories, stakeholders, jornada, requisitos) |
| [BACKLOG.md](docs/BACKLOG.md)                                                         | **Histórico do Board/Backlog por Sprint**                         |
| [discovery/DISCOVERY_LOG.md](docs/discovery/DISCOVERY_LOG.md)                         | Log de Discovery (8 descobertas)                                  |
| [discovery/EVIDENCIAS.md](docs/discovery/EVIDENCIAS.md)                               | Evidências coletadas                                              |
| [decisoes/MATRIZ_DECISAO_TECNOLOGICA.md](docs/decisoes/MATRIZ_DECISAO_TECNOLOGICA.md) | Matriz de decisão tecnológica                                     |
| [decisoes/adr/](docs/decisoes/adr/)                                                   | 4 ADRs (Stack, BD, Auth, Deploy)                                  |
| [arquitetura/C4-CONTEXTO.md](docs/arquitetura/C4-CONTEXTO.md)                         | Diagrama C4 — Contexto                                            |
| [arquitetura/C4-CONTAINERS.md](docs/arquitetura/C4-CONTAINERS.md)                     | Diagrama C4 — Containers                                          |
| [seguranca/ASVS_CHECKLIST_MINIMO.md](docs/seguranca/ASVS_CHECKLIST_MINIMO.md)         | Checklist OWASP ASVS                                              |
| [sprints/](docs/sprints/)                                                             | SPRINT-01 a SPRINT-04 (Planning, Daily, Review, Retro)            |
