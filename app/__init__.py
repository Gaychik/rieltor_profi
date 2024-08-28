from flask import render_template,flash,redirect,url_for,Flask,request,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_,and_
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,login_user,logout_user,login_required,UserMixin,current_user
from app.config import Config



db=SQLAlchemy()
from app.models.Client import Client
from app.models.Rieltor import Rieltor
from app.models.Message import Message
login_manager=LoginManager()
login_manager.login_view='auth.login'
from app.main import *
from app.rieltor import *
from app.client import *
from app.reg_auth import *
