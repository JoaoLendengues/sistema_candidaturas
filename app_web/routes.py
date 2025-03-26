import os
from flask import Blueprint, render_template, request, redirect, url_for

from app_web.config import UPLOAD_FOLDER
from db.modelos import salvar_candidato

bp = Blueprint('main', __name__)

# Defina o diretório de uploads
UPLOAD_FOLDER = 'uploads'

# Verifique se o diretório de uploads existe, se não, crie-o
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/Candidatar', methods=['POST'])
def candidatar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        curriculum = request.files['curriculum']
        filename = os.path.join('uploads', curriculum.filename)

    # Validar e salvar os dados
    if curriculum and allowed_file(curriculum.filename):
        filename = os.path.join(UPLOAD_FOLDER, curriculum.filename)
        curriculum.save(filename)

        # Salvar os dados no banco de dados
        try:
            salvar_candidato(nome, email, telefone, filename)
            return redirect(url_for('main.index')) # Redireciona de volta para a página principal
        except Exception as e:
            return f"Erro ao salvar candidato: {e}"
    else:
        return "Arquivo inválido", 400

# Função para validar os tipos de arquivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}

@bp.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')