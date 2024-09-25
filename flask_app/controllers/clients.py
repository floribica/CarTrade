from flask import flash, redirect, render_template, request, session

from flask_app import app
from flask_app.helpers.send_email import client_email_confirm, send_email, user_email_confirm
from flask_app.helpers.calculator import calculate_price
from flask_app.models.car import Car
from flask_app.models.client import Client
from flask_app.models.payment import Payment
from flask_app.models.rent import Rent
from flask_app.models.user import User


@app.route('/client/register', methods=['POST'])
def register_client():
    # Extract client data from the modal form
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "nr_tel": request.form['nr_tel'],
        "car_id": request.form['car_id'],  # Car ID from the rental form
        "pickup_location": request.form.get('pickup_location'),
        "dropoff_location": request.form.get('dropoff_location'),
        "pickup_date": request.form.get('pickup_date'),
        "dropoff_date": request.form.get('dropoff_date'),
        "pickup_time": request.form.get('pickup_time'),
        "dropoff_time": request.form.get('dropoff_time')
    }
    
    # Validate and register the client
    if not Client.validate_client(data):
        flash("Invalid client data", "client_error")
        return redirect(request.referrer)
    if not Rent.validate_rent(data):
        flash("Invalid rent data", "rent_error")
        return redirect(request.referrer)

    Client.add_client(data)
    #id off the client that was just added
    client_id = Client.get_client_id(data)
    if not client_id:
        return redirect(request.referrer)
    data['client_id'] = client_id
    car = Car.get_car_by_id(data)
    user_email = User.get_user_email({"user_id": car["user_id"]})
    paymrnt_data = {
        "client_id": client_id,
        "car_id": data["car_id"],
        "user_id": car["user_id"],
        "amount": calculate_price(data)["total_amount"],
        "status": "pending"
    }
    Rent.add_rent(data) 
    Payment.add_payment(paymrnt_data)
    
    message_user = user_email_confirm(data)
    message_clent = client_email_confirm(data)
    send_email(user_email["email"], "Confirm the Rental Car", message_user)
    send_email(data["email"], "Rental Car Confirmation", message_clent)
    return redirect("/")


@app.route("/confirm_rent/<int:client_id>/<int:car_id>", methods=['POST', 'GET'])
def confirm_rent(client_id, car_id):
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'GET':
        data = {
            "car_id": car_id,
            "user_id": session['user']['user_id']
        }
        return redirect("/seller/confirm")

    data = {
        "car_id": car_id,
        "client_id": client_id
    }
    Payment.confirm_payment(data)
    return redirect("/seller/confirm")
