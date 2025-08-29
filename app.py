from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

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
            print(f"Nome: {nome}, Email: {email}, Senha: {senha}")
            return "Cadastro recebido com sucesso!"

    return render_template('cadastro.html', erro=erro)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        print(f"Login com Email: {email}, Senha: {senha}")
        return "Login recebido!"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
