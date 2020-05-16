from flaskblog import create_app
from flask_socketio import SocketIO, send, emit

app = create_app()
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handleMessage(msg):
   print('Message: ' + msg)
   send(msg, broadcast=True)

def messageReceived():
  print( 'message was received!!!' )


@socketio.on('sendMessage')
def send_the_message(json):
    print('Bericht:' + str(json))
    socketio.emit('response', json, callback=messageReceived)


# @socketio.on('message', namespace='/chat')
# def chat_message(message):
#     emit('message', {'data': message['data']}, broadcast = True)
 
@socketio.on('connect')
def connect():
    msg = "Hi there "
    socketio.emit('response_conn', msg)



if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=4000, debug=True)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)