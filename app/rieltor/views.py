from . import bp_rieltor
from app import render_template,login_required,current_user,Message,and_

@bp_rieltor.route('/profile')
def profile():
    return  render_template('.rieltor.html',rieltor=current_user)

@bp_rieltor.route('/chat/<int:client_id>')
@login_required
def show_chat(client_id):
    messages = Message.query.filter(and_(Message.client_id==client_id,Message.rieltor_id==current_user.id)).all()
    return render_template('rieltor.chat.html',messages=messages)

