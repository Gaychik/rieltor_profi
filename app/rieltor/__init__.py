from flask import Blueprint
bp_rieltor=Blueprint('rieltor',__name__,template_folder='templates',static_folder='static',url_prefix='/rieltor')
from .views import profile,show_chat
