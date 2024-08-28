from . import bp_main
from app import render_template,Rieltor,current_user

@bp_main.route('/',methods=['GET'])
@bp_main.route('/index')
def index():
    rieltors=Rieltor.query.all()
    return  render_template('index.html',rieltors=rieltors,current_user=current_user)


