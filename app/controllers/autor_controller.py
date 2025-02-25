from flask import render_template

def mostrar_autor():
    autor = {
        "nome": "Eliane Lucas",
        "formacoes": [
            {"curso": "Ténica em Informática", "instituicao": "IFCE", "ano": 2024}
        ],
        "experiencias": [
            {"funcao": "Desenvolvedor", "empresa": "Empresa Y", "ano": 2021}
        ]
    }
    return render_template("autor.html", autor=autor)
