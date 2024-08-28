from flask import Blueprint
bp_client=Blueprint('client',__name__,template_folder='templates',static_folder='static')
from .views import profile,show_chat
