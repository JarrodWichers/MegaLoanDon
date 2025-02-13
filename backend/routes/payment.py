# backend/routes/payment.py
from flask import Blueprint, request, jsonify
from services.payment_service import create_payment

bp = Blueprint('payment', __name__)

@bp.route('/api/payment', methods=['POST'])
def create_payment_route():
    data = request.json
    return create_payment(data['amount'], data['payment_method_id'])