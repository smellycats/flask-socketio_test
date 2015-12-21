#codeing=utf-8
from flask import Flask, render_template
from flask.ext.socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('message',namespace='/msg')
def on_connect(message):
    emit('my response', {'data': 'Connected'+message})

if __name__ == '__main__':
    socketio.run(app)
