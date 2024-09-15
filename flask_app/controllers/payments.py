from flask import flash, redirect, render_template, request, session

from flask_app import app


@app.route("/back/car_details/<int:car_id>")
def car_details(car_id):
    session.clear()
    return redirect(f'/display_car/{car_id}')


@app.route("/payment/cash")
def cash():
    pass


@app.route("/payment/card")
def card():
    pass


@app.route("/payment/paypal")
def paypal():
    pass
