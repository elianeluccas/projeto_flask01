from flask import render_template, request
from app.models.problema import Problema


def mostrar_formulario():
    return render_template("index.html")

def processar_problema():
    nome = request.form.get("nome", "Nome não informado")
    idade = request.form.get("idade", "Idade não informada")
    profissao = request.form.get("profissao", "Profissão não informada")
    
    problema = Problema(nome, idade, profissao)
    
    return render_template("problema.html", problema=problema)
