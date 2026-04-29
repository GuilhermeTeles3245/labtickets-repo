from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps
import os

# Caminho absoluto para o banco — resolve o bug de "run de qualquer pasta"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'labtickets.db')

app = Flask(__name__)
app.secret_key = "chave_super_secreta_pbl_2026"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

OUTPUT_TXT = os.path.join(BASE_DIR, '..', 'usuarios_exportados.txt')

def exportar_usuarios_txt():
    """Regera o arquivo usuarios_exportados.txt automaticamente."""
    try:
        from datetime import datetime as dt
        usuarios = Usuario.query.order_by(Usuario.perfil, Usuario.nome).all()
        agora = dt.now().strftime('%d/%m/%Y %H:%M:%S')
        linhas = []
        linhas.append("=" * 60)
        linhas.append("  RELATORIO DE USUARIOS - LabTickets")
        linhas.append(f"  Gerado em: {agora}")
        linhas.append("=" * 60)
        linhas.append(f"  Total de contas: {len(usuarios)}")
        linhas.append("")
        grupos = {
            'coordenador': 'COORDENADORES',
            'tecnico':     'TECNICOS',
            'solicitante': 'SOLICITANTES'
        }
        for chave, titulo in grupos.items():
            grupo = [u for u in usuarios if u.perfil == chave]
            if not grupo:
                continue
            linhas.append(f"--- {titulo} ({len(grupo)}) ---")
            for u in grupo:
                status = "Ativo" if u.ativo else "INATIVO"
                criado = u.criado_em.strftime('%d/%m/%Y') if u.criado_em else "?"
                linhas.append(f"  Nome    : {u.nome}")
                linhas.append(f"  Usuario : {u.username}")
                linhas.append(f"  Status  : {status}  |  Criado em: {criado}")
                linhas.append(f"  Senha   : [armazenada como hash - nao recuperavel]")
                linhas.append("")
        linhas.append("=" * 60)
        linhas.append("  SENHAS PADRAO DAS CONTAS DE TESTE INICIAIS:")
        linhas.append("    admin     -> admin")
        linhas.append("    tecnico1  -> 123")
        linhas.append("    professor -> 123")
        linhas.append("  Contas criadas pelos proprios usuarios: senha nao recuperavel.")
        linhas.append("=" * 60)
        path = os.path.abspath(OUTPUT_TXT)
        with open(path, 'w', encoding='utf-8') as f:
            f.write("\n".join(linhas))
    except Exception as e:
        print(f"[AVISO] Nao foi possivel atualizar usuarios_exportados.txt: {e}")


db = SQLAlchemy(app)

# ================= MODELOS =================

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    perfil = db.Column(db.String(20), nullable=False)  # solicitante, tecnico, coordenador
    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

class Chamado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    laboratorio = db.Column(db.String(50), nullable=False)
    prioridade = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='Novo')
    solucao = db.Column(db.Text, nullable=True)
    data_abertura = db.Column(db.DateTime, default=datetime.utcnow)
    data_conclusao = db.Column(db.DateTime, nullable=True)
    solicitante_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    tecnico_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    solicitante = db.relationship('Usuario', foreign_keys=[solicitante_id])
    tecnico = db.relationship('Usuario', foreign_keys=[tecnico_id])

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    chamado_id = db.Column(db.Integer, db.ForeignKey('chamado.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario')
    chamado = db.relationship('Chamado', backref=db.backref('comentarios', lazy=True, order_by='Comentario.data'))

# ================= DECORATORS =================

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('Faça login para continuar.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def perfil_required(*perfis):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if session.get('perfil') not in perfis:
                flash('Acesso não permitido.', 'danger')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated
    return decorator

# ================= ROTAS DE AUTH =================

@app.route('/')
def index():
    return redirect(url_for('dashboard') if 'user_id' in session else url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        user = Usuario.query.filter_by(username=request.form['username'].strip()).first()
        if user and user.ativo and check_password_hash(user.senha_hash, request.form['senha']):
            session['user_id'] = user.id
            session['perfil'] = user.perfil
            session['nome'] = user.nome
            return redirect(url_for('dashboard'))
        flash('Usuário ou senha inválidos!', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        username = request.form.get('username', '').strip()
        senha = request.form.get('senha', '')
        confirma = request.form.get('confirma', '')

        if not nome or not username or not senha:
            flash('Preencha todos os campos.', 'danger')
        elif len(senha) < 4:
            flash('A senha deve ter pelo menos 4 caracteres.', 'danger')
        elif senha != confirma:
            flash('As senhas nao coincidem.', 'danger')
        elif Usuario.query.filter_by(username=username).first():
            flash('Este nome de usuario ja esta em uso.', 'danger')
        else:
            novo = Usuario(
                nome=nome,
                username=username,
                senha_hash=generate_password_hash(senha),
                perfil='solicitante'  # visitantes sempre entram como solicitante
            )
            db.session.add(novo)
            db.session.commit()
            exportar_usuarios_txt()
            flash(f'Conta criada com sucesso! Faca login com "{username}".', 'success')
            return redirect(url_for('login'))
    return render_template('cadastro.html')

# ================= DASHBOARD =================

@app.route('/dashboard')
@login_required
def dashboard():
    perfil = session['perfil']
    user_id = session['user_id']

    status_filter = request.args.get('status', '')
    lab_filter = request.args.get('lab', '')
    busca = request.args.get('busca', '')

    query = Chamado.query
    if perfil == 'solicitante':
        query = query.filter_by(solicitante_id=user_id)

    if status_filter:
        query = query.filter_by(status=status_filter)
    if lab_filter:
        query = query.filter_by(laboratorio=lab_filter)
    if busca:
        query = query.filter(Chamado.titulo.ilike(f'%{busca}%'))

    if perfil == 'tecnico':
        # Prioridade: Alta > Média > Baixa, depois por data
        prioridade_order = db.case({'Alta': 1, 'Média': 2, 'Baixa': 3}, value=Chamado.prioridade)
        chamados = query.order_by(prioridade_order, Chamado.data_abertura.asc()).all()
    else:
        chamados = query.order_by(Chamado.data_abertura.desc()).all()

    labs = ['Lab 1', 'Lab 2', 'Lab 3', 'Redes']
    return render_template('dashboard.html', chamados=chamados, perfil=perfil,
                           labs=labs, status_filter=status_filter,
                           lab_filter=lab_filter, busca=busca)

# ================= CHAMADOS =================

@app.route('/chamado/novo', methods=['GET', 'POST'])
@login_required
@perfil_required('solicitante')
def novo_chamado():
    if request.method == 'POST':
        novo = Chamado(
            titulo=request.form['titulo'].strip(),
            descricao=request.form['descricao'].strip(),
            categoria=request.form['categoria'],
            laboratorio=request.form['laboratorio'],
            prioridade=request.form['prioridade'],
            solicitante_id=session['user_id']
        )
        db.session.add(novo)
        db.session.commit()
        flash(f'Chamado #{novo.id} aberto com sucesso!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('novo_chamado.html')

@app.route('/chamado/<int:id>', methods=['GET', 'POST'])
@login_required
def ver_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    perfil = session['perfil']

    if request.method == 'POST':
        acao = request.form.get('acao')

        if acao == 'comentar':
            texto = request.form.get('comentario', '').strip()
            if texto:
                c = Comentario(texto=texto, chamado_id=id, usuario_id=session['user_id'])
                db.session.add(c)
                db.session.commit()
                flash('Comentário adicionado!', 'success')

        elif acao == 'status' and perfil in ['tecnico', 'coordenador']:
            novo_status = request.form.get('novo_status')
            chamado.status = novo_status
            if novo_status == 'Andamento' and not chamado.tecnico_id:
                chamado.tecnico_id = session['user_id']
            if novo_status == 'Concluído':
                chamado.data_conclusao = datetime.utcnow()
                chamado.solucao = request.form.get('solucao', '').strip()
            db.session.commit()
            flash('Status atualizado!', 'success')

        elif acao == 'assumir' and perfil == 'tecnico':
            chamado.tecnico_id = session['user_id']
            chamado.status = 'Andamento'
            db.session.commit()
            flash('Chamado assumido por você!', 'success')

        return redirect(url_for('ver_chamado', id=id))

    tecnicos = Usuario.query.filter_by(perfil='tecnico', ativo=True).all()
    return render_template('chamado.html', chamado=chamado, perfil=perfil, tecnicos=tecnicos)

@app.route('/chamado/<int:id>/deletar', methods=['POST'])
@login_required
@perfil_required('coordenador')
def deletar_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    # Apagar comentários vinculados primeiro
    Comentario.query.filter_by(chamado_id=id).delete()
    db.session.delete(chamado)
    db.session.commit()
    flash(f'Chamado #{id} removido com sucesso.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/comentario/<int:id>/deletar', methods=['POST'])
@login_required
@perfil_required('coordenador')
def deletar_comentario(id):
    comentario = Comentario.query.get_or_404(id)
    chamado_id = comentario.chamado_id
    db.session.delete(comentario)
    db.session.commit()
    flash('Comentário removido.', 'success')
    return redirect(url_for('ver_chamado', id=chamado_id))

@app.route('/chamado/<int:id>/atribuir', methods=['POST'])
@login_required
@perfil_required('coordenador')
def atribuir_tecnico(id):
    chamado = Chamado.query.get_or_404(id)
    tecnico_id = request.form.get('tecnico_id')
    chamado.tecnico_id = int(tecnico_id) if tecnico_id else None
    db.session.commit()
    flash('Técnico atribuído com sucesso!', 'success')
    return redirect(url_for('ver_chamado', id=id))

# ================= MÉTRICAS (COORDENADOR) =================

@app.route('/metricas')
@login_required
@perfil_required('coordenador')
def metricas():
    total = Chamado.query.count()
    novos = Chamado.query.filter_by(status='Novo').count()
    andamento = Chamado.query.filter_by(status='Andamento').count()
    concluidos = Chamado.query.filter_by(status='Concluído').count()
    cancelados = Chamado.query.filter_by(status='Cancelado').count()

    por_lab = db.session.query(Chamado.laboratorio, db.func.count(Chamado.id))\
        .group_by(Chamado.laboratorio).all()
    por_categoria = db.session.query(Chamado.categoria, db.func.count(Chamado.id))\
        .group_by(Chamado.categoria).all()
    por_prioridade = db.session.query(Chamado.prioridade, db.func.count(Chamado.id))\
        .group_by(Chamado.prioridade).all()

    return render_template('metricas.html',
        total=total, novos=novos, andamento=andamento,
        concluidos=concluidos, cancelados=cancelados,
        por_lab=por_lab, por_categoria=por_categoria, por_prioridade=por_prioridade)

# ================= GERENCIAR USUÁRIOS (COORDENADOR) =================

@app.route('/usuarios')
@login_required
@perfil_required('coordenador')
def usuarios():
    lista = Usuario.query.order_by(Usuario.criado_em.desc()).all()
    return render_template('usuarios.html', usuarios=lista)

@app.route('/usuarios/novo', methods=['GET', 'POST'])
@login_required
@perfil_required('coordenador')
def novo_usuario():
    if request.method == 'POST':
        username = request.form['username'].strip()
        if Usuario.query.filter_by(username=username).first():
            flash('Usuário já existe!', 'danger')
        else:
            u = Usuario(
                nome=request.form['nome'].strip(),
                username=username,
                senha_hash=generate_password_hash(request.form['senha']),
                perfil=request.form['perfil']
            )
            db.session.add(u)
            db.session.commit()
            exportar_usuarios_txt()
            flash(f'Usuário "{u.nome}" criado com sucesso!', 'success')
            return redirect(url_for('usuarios'))
    return render_template('novo_usuario.html')

@app.route('/usuarios/<int:id>/toggle', methods=['POST'])
@login_required
@perfil_required('coordenador')
def toggle_usuario(id):
    u = Usuario.query.get_or_404(id)
    if u.id == session['user_id']:
        flash('Você não pode desativar a si mesmo.', 'danger')
    else:
        u.ativo = not u.ativo
        db.session.commit()
        flash(f'Usuário {"ativado" if u.ativo else "desativado"}.', 'success')
    return redirect(url_for('usuarios'))

@app.route('/usuarios/<int:id>/deletar', methods=['POST'])
@login_required
@perfil_required('coordenador')
def deletar_usuario(id):
    u = Usuario.query.get_or_404(id)
    if u.id == session['user_id']:
        flash('Voce nao pode deletar a sua propria conta.', 'danger')
        return redirect(url_for('usuarios'))
    # Desvincula chamados abertos pelo usuario (mantém histórico, mas sem FK quebrada)
    Chamado.query.filter_by(solicitante_id=id).update({'solicitante_id': None})
    Chamado.query.filter_by(tecnico_id=id).update({'tecnico_id': None})
    Comentario.query.filter_by(usuario_id=id).delete()
    db.session.delete(u)
    db.session.commit()
    exportar_usuarios_txt()
    flash(f'Conta de "{u.nome}" deletada permanentemente.', 'success')
    return redirect(url_for('usuarios'))



def inicializar_banco():
    with app.app_context():
        db.create_all()
        if not Usuario.query.first():
            users = [
                Usuario(nome='Admin Coordenador', username='admin',
                        senha_hash=generate_password_hash('admin'), perfil='coordenador'),
                Usuario(nome='Técnico João', username='tecnico1',
                        senha_hash=generate_password_hash('123'), perfil='tecnico'),
                Usuario(nome='Prof. Maria', username='professor',
                        senha_hash=generate_password_hash('123'), perfil='solicitante'),
            ]
            for u in users:
                db.session.add(u)
            db.session.commit()
            print("[OK] Banco criado com usuarios de teste!")
        else:
            print("[OK] Banco ja existente, continuando...")

if __name__ == '__main__':
    inicializar_banco()
    print("[SERVER] Rodando em http://127.0.0.1:5000")
    app.run(debug=True)
