from . import *
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app,db)
    for bp in [bp_rieltor,bp_client,bp_main,bp_login]:  #регистрация марушрутной области
        app.register_blueprint(bp)
    login_manager.init_app(app)
    with app.app_context():
           db.create_all()
    return app 