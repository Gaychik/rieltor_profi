from app import *
from datetime import datetime
class Message(db.Model):
    __tablename__='messages'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String) 
    date = db.Column(db.DateTime,default=datetime.now())
    to_id = db.Column(db.Integer,db.ForeignKey('clients.id',name='fk_client_msg'),nullable=False)
    from_id = db.Column(db.Integer,db.ForeignKey('rieltors.id',name='fk_rieltor_msg'),nullable=False)
    chat_id=db.Column(db.Integer,db.ForeignKey('chats.id',name='fk_chat_msg'),nullable=False)
    client = db.relationship('Client', backref='messages')
    rieltor = db.relationship('Rieltor',backref='messages') 