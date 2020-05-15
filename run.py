from flaskblog import create_app
from flask_socketio import SocketIO, send, emit

app = create_app()
socketio = SocketIO(app, cors_allowed_origins="*")

#@socketio.on('message')
#def handleMessage(msg):
#    print('Message: ' + msg)
#    send(msg, broadcast=True)

def messageReceived():
  print( 'message was received!!!' )


@socketio.on('sendMessage')
def send_the_message(json):
    print('Bericht:' + str(json))
    socketio.emit('response', json, callback=messageReceived)



if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=4000, debug=True)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)