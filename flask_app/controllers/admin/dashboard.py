from flask import render_template, session, redirect

from flask_app import app
from flask_app.models.payment import Payment
from flask_app.models.user import User


@app.route("/admin")
def admin():
    if 'user' not in session:
        return redirect("/")
    if session['user']['role'] != 'admin':
        return redirect("/")
    total_payment = Payment.get_total_payment_this_month()
    total_confirm_payment = Payment.count_total_confirm_this_month()
    total_unconfirm_payment = Payment.count_total_unconfirm_this_month()
    total_cash_confirm = Payment.count_total_cash_confirm_this_month()
    users_id = User.get_all_user_id()
    confirm_payments_last_previous = []
    for user_id in users_id:
        confirm_payment = Payment.get_all_confirm_payment_previous_month({"user_id": user_id["user_id"]})
        if not confirm_payment:
            continue
        confirm_payments_last_previous.append(confirm_payment)
    confirm_payments_this_previous = []
    for user_id in users_id:
        confirm_payment = Payment.get_all_confirm_payment_this_month({"user_id": user_id["user_id"]})
        if not confirm_payment:
            continue
        confirm_payments_this_previous.append(confirm_payment)
    user = session['user']
    return render_template(
        "admin/index.html",
        user=user,
        total_payment=total_payment,
        total_confirm_payment=total_confirm_payment,
        total_unconfirm_payment=total_unconfirm_payment,
        total_cash_confirm=total_cash_confirm,
        confirm_payments=confirm_payments_last_previous,
        confirm_payments_this_month=confirm_payments_this_previous
    )