"""
exportar_usuarios.py
--------------------
Execute com: python src/exportar_usuarios.py
Gera o arquivo 'usuarios_exportados.txt' com todos os usuarios cadastrados no banco.

NOTA IMPORTANTE SOBRE SENHAS:
  As senhas sao armazenadas como HASH (criptografadas) no banco, por segurança.
  Nao e possivel reverter o hash para a senha original.
  Este arquivo exibe apenas os dados visiveis: nome, usuario, perfil e status.
  Guarde as senhas dos usuarios em local seguro no momento do cadastro.
"""

import sqlite3
import os
from datetime import datetime

# Caminho do banco de dados (mesmo que o usado pelo app.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'labtickets.db')
OUTPUT_FILE = os.path.join(BASE_DIR, '..', 'usuarios_exportados.txt')

def exportar():
    if not os.path.exists(DB_PATH):
        print(f"[ERRO] Banco nao encontrado em: {DB_PATH}")
        print("       Certifique-se de ter rodado o app.py pelo menos uma vez.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, username, perfil, ativo, criado_em
        FROM usuario
        ORDER BY perfil, nome
    """)
    rows = cursor.fetchall()
    conn.close()

    agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    linhas = []
    linhas.append("=" * 60)
    linhas.append("  RELATORIO DE USUARIOS - LabTickets")
    linhas.append(f"  Gerado em: {agora}")
    linhas.append("=" * 60)
    linhas.append(f"  Total de contas: {len(rows)}")
    linhas.append("")

    perfis = {
        'coordenador': 'COORDENADORES',
        'tecnico':     'TECNICOS',
        'solicitante': 'SOLICITANTES'
    }

    for chave, titulo in perfis.items():
        grupo = [r for r in rows if r[2] == chave]
        if not grupo:
            continue
        linhas.append(f"--- {titulo} ({len(grupo)}) ---")
        for nome, username, perfil, ativo, criado_em in grupo:
            status = "Ativo" if ativo else "INATIVO"
            criado = criado_em[:10] if criado_em else "?"
            linhas.append(f"  Nome    : {nome}")
            linhas.append(f"  Usuario : {username}")
            linhas.append(f"  Status  : {status}  |  Criado em: {criado}")
            linhas.append(f"  Senha   : [apenas o usuario sabe - armazenada como hash]")
            linhas.append("")

    linhas.append("=" * 60)
    linhas.append("  SENHAS DOS USUARIOS DE TESTE INICIAIS (padrao do sistema):")
    linhas.append("    admin     -> admin")
    linhas.append("    tecnico1  -> 123")
    linhas.append("    professor -> 123")
    linhas.append("  Para contas criadas pelos proprios usuarios, a senha")
    linhas.append("  nao pode ser recuperada. Redefina pelo admin se necessario.")
    linhas.append("=" * 60)

    conteudo = "\n".join(linhas)

    output_path = os.path.abspath(OUTPUT_FILE)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    print(f"[OK] Relatorio gerado com sucesso!")
    print(f"     Arquivo: {output_path}")
    print(f"     Total de usuarios exportados: {len(rows)}")

if __name__ == '__main__':
    exportar()
