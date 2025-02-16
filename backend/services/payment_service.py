import stripe
from models import db, Payment

stripe.api_key = ""

def create_payment(amount, payment_method_id):
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            payment_method=payment_method_id,
            confirmation_method='manual',
            confirm=True,
        )
        payment = Payment(amount=amount, payment_method_id=payment_method_id)
        db.session.add(payment)
        db.session.commit()
        return intent, 200
    except Exception as e:
        return {"error": str(e)}, 403
    
def update_payment(payment_id, amount, payment_date):
    payment = Payment.query.get(payment_id)
    if not payment:
        return {"message": "Payment not found!"}, 404

    payment.amount = amount
    payment.payment_date = payment_date
    db.session.commit()
    return {"message": "Payment updated successfully!"}, 200

def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return {"message": "Payment not found!"}, 404

    db.session.delete(payment)
    db.session.commit()
    return {"message": "Payment deleted successfully!"}, 200