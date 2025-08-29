from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']

        if senha != confirmar_senha:
            return "Senha ioncorreta"
        
        print(f"Nome: {nome}, Email: {email}, Senha: {senha}")
        return "Cadastro recebido com sucesso!"

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)