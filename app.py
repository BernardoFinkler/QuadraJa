from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

# Menu inicial
@app.route('/')
def menu():
    return render_template('menu.html')

# Cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    erro = None
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']

        if senha != confirmar_senha:
            erro = "As senhas não coincidem"
        else:
            usuario_existente = Usuario.query.filter_by(email=email).first()
            if usuario_existente:
                erro = "Este e-mail já esta cadastrado."
            else:
                novo_usuario = Usuario(nome=nome, email=email, senha=senha)
                db.session.add(novo_usuario)
                db.session.commit()
                return redirect(url_for('login'))

    return render_template('cadastro.html', erro=erro)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    erro =  None
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.query.filter_by(email=email, senha=senha).first()
        if usuario:
            return f"Bem-vindo, {usuario.nome}!"
        else:
            erro = "E-mail ou senha incorretos!"

    return render_template('login.html', erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
