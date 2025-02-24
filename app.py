from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal com formulário
@app.route("/index")
def index():
    return render_template("index.html")

# Página que processa os dados
@app.route("/resultado", methods=["POST"])
def resultado():
    nome = request.form["nome"]
    idade = request.form["idade"]
    profissao = request.form["profissao"]
    return f"<h1>Nome: {nome}</h1><h2>Idade: {idade}</h2><h3>Profissão: {profissao}</h3>"

# Página do autor
@app.route("/autor")
def autor():
    return """
    <h1>Autor: Eliane Lucas de Sousa </h1>
    <h2>Formação:</h2>
    <p>Técnica em TI- IFCE - 2024</p>
    <h2>Experiência:</h2>
    <p>Desenvolvedor - Empresa Y - 2024</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
