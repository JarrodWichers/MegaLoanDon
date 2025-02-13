# backend/routes/auth.py
from flask import Blueprint, request, jsonify
from services.user_service import register_user, login_user, reset_password

bp = Blueprint('auth', __name__)

@bp.route('/api/register', methods=['POST'])
def register():
    data = request.json
    return register_user(data.get('email'), data.get('password'), data.get('name'))

@bp.route('/api/login', methods=['POST'])
def login():
    data = request.json
    return login_user(data.get('email'), data.get('password'))

@bp.route('/api/reset-password', methods=['POST'])
def reset_password_route():
    data = request.json
    return reset_password(data.get('email'))