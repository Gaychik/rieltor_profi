from app import *
from flask_migrate import Migrate



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app,db)
    for bp in [bp_main,bp_client,bp_rieltor,bp_login]:
        app.register_blueprint(bp)
    
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
    return app