from app import *
from datetime import datetime

class Message(db.Model):
        __tablename__ ='messages'
        id = db.Column(db.Integer, primary_key=True)
        text=db.Column(db.String)
        date=db.Column(db.DateTime,default=datetime.now())
        client_id=db.relationship('Client',backref='messages')
        rieltor_id=db.relationship('Rieltor',backref='messages') 