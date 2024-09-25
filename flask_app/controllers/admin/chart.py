from flask import redirect, render_template, session

from flask_app import app
from flask_app.models.car import Car
from flask_app.models.payment import Payment
from flask_app.models.client import Client


@app.route('/admin/chart')
def admin_chart():
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "admin":
        return redirect('/')
    total_client = Client.count_total_client_by_month()
    total_car = Car.count_total_car_by_month()
    total_confirm_payment = Payment.count_total_confirm_by_month()
    total_unconfirm_payment = Payment.count_total_unconfirm_by_month()
    user = session['user']

    return render_template(
        'admin/chart.html',
        total_client=total_client,
        total_car=total_car,
        total_confirm_payment=total_confirm_payment,
        total_unconfirm_payment=total_unconfirm_payment,
        user=user
    )
