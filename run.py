from app import *
from app.chat import create_web_socketio,emit
from flask_login import current_user
from flask import request
load_dotenv()
    
app=create_app()
ws = create_web_socketio(app)

clients={}
@ws.on('connect')
def handle_connect():
     if current_user.is_authenticated:
        clients[current_user.id]=request.sid
        
     

@ws.on('send_msg')
def handle_msg(data):
    target_sid=clients[data['id']]
    db.session.add(Message(text=data['message'], to_id=data['id'],from_id=current_user.id, chat_id=data['chat_id']))
    db.session.commit()
    emit('recv_msg',{'message':data['message']},to=target_sid)


if __name__=='__main__':    
     ws.run(app)
 