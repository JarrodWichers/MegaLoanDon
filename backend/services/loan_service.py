# backend/services/loan_service.py
from models import db, LoanRequest  # Assuming you have a LoanRequest model

def create_loan_request(data):
    loan_request = LoanRequest(**data)  # Assuming data contains the necessary fields
    db.session.add(loan_request)
    db.session.commit()
    return {"message": "Loan request created!"}, 201