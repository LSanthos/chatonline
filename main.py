# site com os scripts: https://cdnjs.com/
# pip install flask flask-socketio python-socketio simple-websocket
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar a 1ª guia = 1ª rota
@app.route("/")
def homepage():
    return render_template("index.html")

# roda o aplicativo
if __name__ == "__main__":
    socketio.run(app, host="192.168.1.36", debug=True)

