from . import bp_client
from app import db,render_template,login_required,current_user,Message,and_,client_rieltor_table

@bp_client.route('/profile')
def profile():
    return  render_template('.client.html',client=current_user)

@bp_client.route('/chat/<int:rieltor_id>')
@login_required
def show_chat(rieltor_id):

    select_query=client_rieltor_table.select().where(
        client_rieltor_table.c.rieltor_id==rieltor_id,
        client_rieltor_table.c.client_id==current_user.id,
        )
    result =  db.session.execute(select_query).first()
    messages=[]
    if result is None:
        insert_query=client_rieltor_table.insert().values((current_user.id,rieltor_id))
        db.session.execute(insert_query)
        db.session.commit()
    else:
        messages = Message.query.filter(and_(Message.client_id==current_user.id,Message.rieltor_id==rieltor_id)).all()

    return render_template('chat.html',messages=messages,rieltors=current_user.rieltors)
