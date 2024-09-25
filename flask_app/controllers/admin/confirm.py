from flask import redirect, render_template, session

from flask_app import app
from flask_app.helpers.send_email import cancellation_email, confirmation_email, send_email, suggest_email
from flask_app.models.client import Client
from flask_app.models.payment import Payment
from flask_app.models.user import User


@app.route('/admin/confirm')
def admin_confirm():
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "admin":
        return redirect('/')
    users_id = User.get_all_user_id()
    all_payments = []
    for user_id in users_id:
        payment = Payment.get_all_payments({"user_id": user_id["user_id"]})
        if payment:
            all_payments.append(payment)
    user = session['user']
    user = session['user']
    return render_template(
        'admin/confirm.html',
        all_payments=all_payments,
        user=user
    )


@app.route('/admin/confirm_payment/<int:payment_id>')
def admin_confirm_payment(payment_id):
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "admin":
        return redirect('/')
    message = confirmation_email({"payment_id": payment_id})
    payment = Payment.get_payment_by_id({"payment_id": payment_id})
    client = Client.get_client_by_id({"client_id": payment["client_id"]})
    send_email(client["email"], "Confirm the Rental Car", message)
    Payment.confirm_payment({"payment_id": payment_id})
    return redirect('/admin/confirm')


@app.route('/admin/cancel_payment/<int:payment_id>')
def admin_cancel_payment(payment_id):
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "admin":
        return redirect('/')
    message = cancellation_email({"payment_id": payment_id})
    payment = Payment.get_payment_by_id({"payment_id": payment_id})
    client = Client.get_client_by_id({"client_id": payment["client_id"]})
    send_email(client["email"], "Cancel the Rental Car", message)
    Payment.cance_payment({"payment_id": payment_id})
    return redirect('/admin/confirm')


@app.route("/admin/suggest/<int:payment_id>")
def admin_suggest(payment_id):
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "admin":
        return redirect('/')
    payment = Payment.get_payment_by_id({"payment_id": payment_id})
    client = Client.get_client_by_id({"client_id": payment["client_id"]})
    message = suggest_email({"payment_id": payment_id})
    send_email(client["email"], "Suggest the Rental Car", message)
    return redirect('/admin/confirm')
