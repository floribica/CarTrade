from flask import flash, redirect, render_template, request, session

from flask_app import app
from flask_app.helpers.calculator import calculate_price
from flask_app.models.car import Car
from flask_app.models.client import Client
from flask_app.models.rent import Rent


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
    Rent.add_rent(data) 
    amount = calculate_price(data)
    session['total_amount'] = amount["total_amount"]
    session['rent_info'] = data
    car = Car.get_car_by_id(data)
    client = Client.get_client_by_id({"client_id": client_id})
    
    return render_template(
        "ticket.html",
        amount=amount,
        rent_info=data,
        car=car,
        client=client
    )
    