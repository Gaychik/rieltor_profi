from . import bp_client
from app import render_template,login_required,current_user,Message,and_

@bp_client.route('/profile')
def profile():
    return  render_template('.client.html',client=current_user)

@bp_client.route('/chat/<int:rieltor_id>')
@login_required
def show_chat(rieltor_id):
    messages = Message.query.filter(and_(Message.client_id==current_user.id,Message.rieltor_id==rieltor_id)).all()
    return render_template('.chat.html',messages=messages)
