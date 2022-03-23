from flask import render_template, redirect, request, session, flash
from app.models.user import User
from app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#index
@app.route('/')
def index():
    return render_template('index.html')