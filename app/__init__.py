from flask import render_template,redirect,flash,url_for,Flask,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_,and_
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,login_user,logout_user,login_required,UserMixin,current_user
from app.config import Config


db = SQLAlchemy()
from app.models.Client import Client
from app.models.Rieltor import Rieltor
from app.models.Chat import Chat
from app.models.Message import Message 
from app.models.Client_Rieltor_Association import client_rieltor_table
login_manager = LoginManager()
login_manager.login_view='auth.login'
from app.main import *
from app.rieltor import *
from app.client import *
from app.reg_auth import *
from .app import create_app
from dotenv import load_dotenv



