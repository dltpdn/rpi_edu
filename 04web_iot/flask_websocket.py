from flask import *
from flask_socketio import *

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def main():
    return app.send_static_file("websocket.html")


@socketio.on('connect')
def on_connect():
    print("client connected")

@socketio.on('echo')
def handle_message(msg):
    print('recv:', msg)
    emit('echo', msg)
    
if __name__ == '__main__':
  #  app.run()
    socketio.run(app, host="0.0.0.0", port=8080, debug=True)