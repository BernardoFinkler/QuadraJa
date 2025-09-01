QuadraJá

Aplicação web em Flask para gerenciamento de login, cadastro de usuários e navegação básica por páginas. O projeto é totalmente pessoal.

---

Pré-requisitos

- Python 3.10+ instalado
- pip atualizado
- Git instalado (caso vá clonar o repositório)

---

Configuração do ambiente

1. Clonar o repositório
   Se ainda não tiver o projeto, rode no terminal:

   git clone https://github.com/BernardoFinkler/QuadraJa.git
   cd QuadraJa

2. Criar e ativar ambiente virtual

   Windows:
   python -m venv venv
   venv\Scripts\activate

   Linux/Mac:
   python3 -m venv venv
   source venv/bin/activate

3. Instalar dependências
   Com o ambiente virtual ativo, rode:

   pip install -r requirements.txt

---

Arquivos principais

requirements.txt
Lista de dependências do projeto:

flask
flask-sqlalchemy
flask-login
flask-wtf

Estrutura de pastas

```text
/QuadraJa
├── app.py # Arquivo principal do Flask
├── requirements.txt # Dependências do projeto
├── README.md # Documentação do projeto
├── templates/ # Templates HTML
│ ├── menu.html
│ ├── cadastro.html
│ └── login.html
└── static/ # Arquivos estáticos
├── estilos/
│ └── style.css
└── imagens/
└── Logo_QuadraJá.png
```

---

Executar a aplicação

Com o ambiente virtual ativo, rode:

python app.py

Depois abra no navegador: http://127.0.0.1:5000/
