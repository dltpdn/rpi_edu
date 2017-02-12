from flask import Flask, redirect, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def main():
    return redirect('/static/websocket.html')

@socketio.on('message')
def handle_message(msg):
    print 'recv:', msg
    send(msg, broadcast=True)
    
@app.route('/notify', methods=['GET'])
def msg():
    param = request.values['param']
    socketio.send("nofity : " + param)
    return 'ok'
    
    
if __name__ == '__main__':
   # app.run(host="0.0.0.0")
    socketio.run(app, host='0.0.0.0')
