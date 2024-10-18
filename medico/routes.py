from medico import app
from flask import render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
from .mailkey import mailkey, secretkey

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
