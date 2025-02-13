# backend/services/user_service.py
from flask_security import user_datastore
from models import db, User

def register_user(email, password, name):
    if user_datastore.get_user(email):
        return {"message": "User already exists!"}, 400

    user = user_datastore.create_user(email=email, password=password, name=name)
    db.session.commit()
    return {"message": "User registered successfully!"}, 201

def login_user(email, password):
    user = user_datastore.get_user(email)
    if user and user.verify_password(password):
        return {"message": "Login successful!"}, 200
    return {"message": "Invalid credentials!"}, 401

def reset_password(email):
    user = user_datastore.get_user(email)
    if user:
        send_reset_password_email(user)
        return {"message": "Password reset email sent!"}, 200
    return {"message": "User not found!"}, 404