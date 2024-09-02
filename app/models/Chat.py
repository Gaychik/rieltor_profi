from app import *
class Chat(db.Model):
    __tablename__='chats'
    id = db.Column(db.Integer, primary_key=True)
    last_msg=db.Column(db.String)
    client_id = db.Column(db.Integer,db.ForeignKey('clients.id',name='fk_client_msg'),nullable=False)
    rieltor_id = db.Column(db.Integer,db.ForeignKey('rieltors.id',name='fk_rieltor_msg'),nullable=False)
    client = db.relationship('Client', backref='chats')
    rieltor = db.relationship('Rieltor',backref='chats') 
    messages=db.relationship('Message',backref='chat')