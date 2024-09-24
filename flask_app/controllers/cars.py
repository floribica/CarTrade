from flask import jsonify, render_template, request, session

from flask_app import app

from flask_app.models.car import Car
from flask_app.models.car_image import Car_Image


@app.route('/show/cars', methods=['POST'])
def show_cars():
    # Retrieve form data and structure it into a dictionary
    data = {
        "year": request.form.get("year"),
        "brand": request.form.get("brand"),
        "style": "%" + request.form.get("style") + "%",
        "conditions": request.form.get("conditions"),
        "model": "%" + request.form.get("model") + "%",
        "rent_price": request.form.get("rent_price")
    }
    if data["year"] == "":
        data["year"] = "default"
    if data["model"] == "%%":
        data["model"] = "default"
    if data["style"] == "%%":
        data["style"] = "default"
    if data["rent_price"] == "":
        data["rent_price"] = "default"

    for key, value in data.items():
        if value == "default":
            data[key] = None

    if all(value is None for value in data.values()):
        search_results = None
    else:
        search_results = Car.get_selected_cars(data)

    if 'user' not in session:
        user = {
            "user_id": -1,
            "first_name": "user",
            "last_name": "user",
            "email": "user"
        }
    else:
        user = session['user']

    all_cars = Car.get_all_cars()
    brands = Car.get_all_cars_brand()
    
    return render_template(
        'index.html',
        cars=search_results,
        user=user,
        all_cars=all_cars,
        brands=brands
    )


@app.route("/display_car/<int:car_id>")
def display_car(car_id):
    data = {
        "car_id": car_id
    }
    car = Car.get_car_by_id(data)
    images = Car_Image.get_images_by_car_id(data)
    if 'user' not in session:
        user = {
            "user_id": -1,
            "first_name": "user",
            "last_name": "user",
            "email": "user"
        }
    else:
        user = session['user']
    return render_template(
        'car_display.html',
        user=user,
        car=car,
        images=images,
    )


@app.route('/get_car_details/<int:car_id>')
def get_car_details(car_id):
    car = Car.get_car_by_id({"car_id": car_id})
    car_data = {
        "id": car["car_id"],
        "brand": car["brand"],
        "model": car["model"],
        "year": car["year"],
        "price": car["price"],
        "km": car["km"],
        "description": car["DESCRIPTION"]
    }
    return jsonify(car_data)
