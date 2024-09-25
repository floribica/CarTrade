from flask import redirect, render_template, session

from flask_app import app
from flask_app.helpers.send_email import cancellation_email, confirmation_email, send_email, suggest_email
from flask_app.models.client import Client
from flask_app.models.payment import Payment


@app.route('/seller/confirm')
def seller_confirm():
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "seller":
        return redirect('/')
    payments = Payment.get_all_payments({"user_id": session['user']['user_id']})
    user = session['user']
    return render_template(
        'seller/confirm.html',
        payments=payments,
        user=user
    )


@app.route('/seller/confirm_payment/<int:payment_id>')
def seller_confirm_payment(payment_id):
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "seller":
        return redirect('/')
    message = confirmation_email({"payment_id": payment_id})
    payment = Payment.get_payment_by_id({"payment_id": payment_id})
    client = Client.get_client_by_id({"client_id": payment["client_id"]})
    send_email(client["email"], "Confirm the Rental Car", message)
    Payment.confirm_payment({"payment_id": payment_id})
    return redirect('/seller/confirm')


@app.route("/seller/suggest/<int:payment_id>")
def seller_suggest(payment_id):
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "seller":
        return redirect('/')
    payment = Payment.get_payment_by_id({"payment_id": payment_id})
    client = Client.get_client_by_id({"client_id": payment["client_id"]})
    message = suggest_email({"payment_id": payment_id})
    send_email(client["email"], "Suggest the Rental Car", message)
    return redirect('/seller/confirm')
