from flask import Flask

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_SALT = 'your_salt'
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_PASSWORD_RESET_URL = '/reset-password'