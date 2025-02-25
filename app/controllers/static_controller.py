from flask import send_from_directory

def carregar_arquivo(caminho):
    return send_from_directory("static", caminho)
