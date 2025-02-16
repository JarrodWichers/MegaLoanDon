# backend/routes/payment.py
from flask import Blueprint, request, jsonify
from services.payment_service import create_payment, update_payment, delete_payment
from models import db, Payment

bp = Blueprint('payment', __name__)

@bp.route('/api/payment', methods=['POST'])
def create_payment_route():
    data = request.json
    return create_payment(data['amount'], data['payment_method_id'])

# Get a payment by ID
@bp.route('/api/payment/<int:payment_id>', methods=['GET'])
def get_payment_by_id(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({"message": "Payment not found!"}), 404

    payment_info = {
        'id': payment.id,
        'loan_id': payment.loan_id,
        'amount': payment.amount,
        'payment_date': payment.payment_date.isoformat(),  # Convert to ISO format for JSON
    }
    return jsonify(payment_info), 200

# Get all payments by loan ID
@bp.route('/api/payments/loan/<int:loan_id>', methods=['GET'])
def get_payments_by_loan_id(loan_id):
    payments = Payment.query.filter_by(loan_id=loan_id).all()
    payment_data = []
    for payment in payments:
        payment_info = {
            'id': payment.id,
            'amount': payment.amount,
            'payment_date': payment.payment_date.isoformat(),
        }
        payment_data.append(payment_info)

    return jsonify(payment_data), 200

# Update a payment by ID
@bp.route('/api/payment/<int:payment_id>', methods=['PUT'])
def update_payment_route(payment_id):
    data = request.json
    payment = Payment.query.get(payment_id)

    if not payment:
        return jsonify({"message": "Payment not found!"}), 404

    payment.amount = data.get('amount', payment.amount)
    payment.payment_date = data.get('payment_date', payment.payment_date)

    db.session.commit()
    return jsonify({"message": "Payment updated successfully!"}), 200

# Delete a payment by ID
@bp.route('/api/payment/<int:payment_id>', methods=['DELETE'])
def delete_payment_route(payment_id):
    payment = Payment.query.get(payment_id)

    if not payment:
        return jsonify({"message": "Payment not found!"}), 404

    db.session.delete(payment)
    db.session.commit()
    return jsonify({"message": "Payment deleted successfully!"}), 200