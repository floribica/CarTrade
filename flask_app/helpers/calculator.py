from datetime import datetime
from flask_app.models.car import Car


def calculate_price(data):
    # Extract the car's price per day from the database
    car_price = Car.get_car_price(data)
    if not car_price:
        return None
    # Calculate the number of days between the pickup and dropoff dates
    pickup_date = datetime.strptime(data['pickup_date'], "%Y-%m-%d")
    dropoff_date = datetime.strptime(data['dropoff_date'], "%Y-%m-%d")
    days = (dropoff_date - pickup_date).days
    # Calculate the total price
    total_price = days * car_price
    tax = total_price * 0.2
    subtotal = total_price - tax
    tax = round(tax, 2)
    subtotal = round(subtotal, 2)
    total_price = round(total_price, 2)
    shipping = 00.00
    amount = {
        "total_amount": total_price,
        "days": days,
        "tax": tax,
        "subtotal": subtotal,
        "shipping": shipping
    }
    return amount