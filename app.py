from flask import Flask
from app.controllers import problema_controller, autor_controller

app = Flask(__name__)

# Rota inicial
app.add_url_rule("/index", "index", problema_controller.mostrar_formulario)

# Rota do problema
app.add_url_rule("/problema", "problema", problema_controller.processar_problema, methods=["POST"])

# Rota do autor
app.add_url_rule("/autor", "autor", autor_controller.mostrar_autor)

if __name__ == "__main__":
    app.run(debug=True)
