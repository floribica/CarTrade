from flask import render_template, session, redirect

from flask_app import app
from flask_app.helpers.calculator import calculate_totals
from flask_app.models.payment import Payment


@app.route("/seller")
def seller():
    if 'user' not in session:
        return redirect("/")
    if session['user']['role'] != 'seller':
        return redirect("/")
    total_payment = Payment.get_total_payment_this_month()
    total_confirm_payment = Payment.count_total_confirm_this_month()
    total_unconfirm_payment = Payment.count_total_unconfirm_this_month()
    total_cash_confirm = Payment.count_total_cash_confirm_this_month()
    confirm_payment = Payment.get_all_confirm_payment_previous_month(
        {"user_id": session['user']['user_id']}
    )
    confirm_payment_this_month = Payment.get_all_confirm_payment_this_month(
        {"user_id": session['user']['user_id']}
    )
    total_amount, total_commission = calculate_totals(confirm_payment)
    user = session['user']
    return render_template(
        "seller/index.html",
        user=user,
        total_payment=total_payment,
        total_confirm_payment=total_confirm_payment,
        total_unconfirm_payment=total_unconfirm_payment,
        total_cash_confirm=total_cash_confirm,
        confirm_payment=confirm_payment,
        total_amount=total_amount,
        total_commission=total_commission,
        confirm_payment_this_month=confirm_payment_this_month
    )
