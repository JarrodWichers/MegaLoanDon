# backend/routes/loan.py
from flask import Blueprint, request, jsonify
from services.loan_service import create_loan_request

bp = Blueprint('loan', __name__)

@bp.route('/api/loan-request', methods=['POST'])
def create_loan_request_route():
    data = request.json
    return create_loan_request(data)