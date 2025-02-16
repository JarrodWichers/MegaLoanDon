# backend/routes/loan.py
from flask import Blueprint, request, jsonify
from services.loan_service import create_loan_request
from models import db, Loan, Payment, User

bp = Blueprint('loan', __name__)

@bp.route('/api/loan-request', methods=['POST'])
def create_loan_request_route():
    data = request.json
    return create_loan_request(data)


@bp.route('/api/investor-loans', methods=['GET'])
def get_investor_loans():
    user_id = request.args.get('user_id')  # Assuming you pass the user ID as a query parameter
    loans = Loan.query.all()  # Fetch all loans
    investments = Payment.query.filter_by(user_id=user_id).all()  # Fetch investments for the investor

    loan_data = []
    for loan in loans:
        loan_info = {
            'id': loan.id,
            'amount': loan.amount,
            'interest_rate': loan.interest_rate,
            'duration_months': loan.duration_months,
            'status': loan.status,
            'invested_amount': sum(payment.amount for payment in investments if payment.loan_id == loan.id)
        }
        loan_data.append(loan_info)

    return jsonify(loan_data), 200

@bp.route('/api/user-loan-requests', methods=['GET'])
def get_user_loan_requests():
    user_id = request.args.get('user_id')  # Assuming you pass the user ID as a query parameter
    loan_requests = Loan.query.filter_by(user_id=user_id).all()  # Fetch loans for the user

    loan_data = []
    for loan in loan_requests:
        loan_info = {
            'id': loan.id,
            'amount': loan.amount,
            'interest_rate': loan.interest_rate,
            'duration_months': loan.duration_months,
            'status': loan.status,
        }
        loan_data.append(loan_info)

    return jsonify(loan_data), 200

@bp.route('/api/loan-request/<int:loan_id>', methods=['PUT'])
def edit_loan_request(loan_id):
    data = request.json
    loan_request = Loan.query.get(loan_id)

    if not loan_request:
        return jsonify({"message": "Loan request not found!"}), 404

    # Update the loan request fields
    loan_request.amount = data.get('amount', loan_request.amount)
    loan_request.interest_rate = data.get('interest_rate', loan_request.interest_rate)
    loan_request.duration_months = data.get('duration_months', loan_request.duration_months)
    loan_request.status = data.get('status', loan_request.status)

    db.session.commit()
    return jsonify({"message": "Loan request updated successfully!"}), 200

@bp.route('/api/user-loan-request/<int:loan_id>', methods=['GET'])
def get_user_loan_request(loan_id):
    
    loan_request = Loan.query.filter_by(id=loan_id).first()  # Fetch the loan for the user

    if not loan_request:
        return jsonify({"message": "Loan request not found!"}), 404

    loan_info = {
        'id': loan_request.id,
        'amount': loan_request.amount,
        'interest_rate': loan_request.interest_rate,
        'duration_months': loan_request.duration_months,
        'status': loan_request.status,
    }

    return jsonify(loan_info), 200