from flask_socketio import SocketIO,emit


def create_web_socketio(app):
      return  SocketIO(app)


