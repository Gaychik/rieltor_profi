from . import bp_rieltor
from app import  db,render_template,login_required,Message,and_,client_rieltor_table,Chat,redirect,url_for
from flask_login import current_user

@bp_rieltor.route('/profile')
@login_required 
def profile():    
    chats=Chat.query.filter_by(rieltor_id=current_user.id).all()
    return render_template('rieltor.html',chats=chats)



@bp_rieltor.route('/chat/<client_id>')
@login_required
def show_chat(client_id):
    chats=Chat.query.filter(and_(Chat.rieltor_id==current_user.id,Chat.client_id==client_id) ).all()
    current_chat= Chat.query.filter_by(client_id=client_id).first()
    return render_template('rieltor_chat.html',chats=chats,current_chat=current_chat)