from . import bp_client
from app import  db,render_template,login_required,current_user,Message,and_,client_rieltor_table,Chat,redirect,url_for

@bp_client.route('/profile')
@login_required 
def profile():    
    chats=Chat.query.filter_by(client_id=current_user.id).all()
    return render_template('client.html',chats=chats)


@bp_client.route('/contact/<int:rieltor_id>')
@login_required 
def connect(rieltor_id):
    select_query=client_rieltor_table.select().where(
        client_rieltor_table.c.rieltor_id==rieltor_id,
        client_rieltor_table.c.client_id==current_user.id)
    result=db.session.execute(select_query).first()
    if result is None:
        insert_query=client_rieltor_table.insert().values((current_user.id,rieltor_id))
        db.session.execute(insert_query)
        db.session.add(Chat(rieltor_id=rieltor_id,client_id=current_user.id))
        db.session.commit()
    return  redirect(url_for('.show_chat',rieltor_id=rieltor_id))

    

@bp_client.route('/chat/<int:rieltor_id>')
@login_required
def show_chat(rieltor_id):
    chats=Chat.query.filter(and_(Chat.client_id==current_user.id,Chat.rieltor_id==rieltor_id) ).all()
    current_chat= Chat.query.filter_by(rieltor_id=rieltor_id).first()
    return render_template('chat.html',chats=chats,current_chat=current_chat)