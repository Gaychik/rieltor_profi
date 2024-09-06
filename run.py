from app import *
from app.chat import create_web_socketio,emit
load_dotenv()
    
app=create_app()
ws = create_web_socketio(app)

clients={}
@ws.on('connect')
def handle_connect():
     if current_user.is_authenticated :
        clients[current_user.phone]=request.sid
        print(clients)
        
     

@ws.on('send_msg')
def handle_msg(data):
    print(data)
    target_sid=clients[data['phone']]
    print(target_sid)    
    emit('recv_msg',{'message':data['message']},to=target_sid)


if __name__=='__main__':    
     ws.run(app)
 