import stripe

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
        return intent, 200
    except Exception as e:
        return {"error": str(e)}, 403