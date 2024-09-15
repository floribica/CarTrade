from datetime import datetime
import os
from dotenv import load_dotenv
from flask import flash, jsonify, redirect, render_template, request, session

from flask_app import app
from werkzeug.utils import secure_filename

from flask_app.models.car import Car
from flask_app.models.car_image import Car_Image


load_dotenv()
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")


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


@app.route('/add/car', methods=['POST', 'GET'])
def add_new_car():
    if request.method == 'GET':
        if 'user' not in session:
            return redirect('/')
        if session['user']['user_id'] != 1:
            return redirect('/')
        return render_template('admin/add_car.html')
    if 'user' not in session:
        return redirect('/')
    if session['user']['user_id'] != 1:
        return redirect('/')
    data = {
        "year": request.form.get("year"),
        "brand": request.form.get("brand"),
        "style": request.form.get("style"),
        "conditions": request.form.get("conditions"),
        "model": request.form.get("model"),
        "price": request.form.get("price"),
        "km": request.form.get("km"),
        "description": request.form.get("description")
    }
    if 'image' in request.files:
        image = request.files['image']

        if image.filename != '':

            # check if the file is allowed by ALLOWED_EXTENSIONS
            if (image and '.' in image.filename
                    and image.filename.rsplit('.', 1)[1].lower()
                    in ALLOWED_EXTENSIONS):
                # add current timi in the file name
                filename = secure_filename(image.filename)
                filename = str(datetime.now().timestamp()) + filename
                image.save(os.path.join(UPLOAD_FOLDER, filename))
                data['image'] = filename
            else:
                flash("File not allowed", "image")
                return redirect(request.referrer)
    Car.add_car(data)
    return render_template('admin/add_car.html')


@app.route("/car/add_image/<int:car_id>", methods=['POST', 'GET'])
def add_car_image(car_id):
    if 'user' not in session:
        return redirect('/')
    if session['user']['user_id'] != 1:
        return redirect('/')

    if request.method == 'GET':
        return render_template('admin/add_image.html', car_id=car_id)

    if 'images' in request.files:
        images = request.files.getlist('images')  # Get list of images

        for image in images:
            if image.filename != '':
                # Check if the file is allowed by ALLOWED_EXTENSIONS
                if (image and '.' in image.filename
                        and image.filename.rsplit('.', 1)[1].lower()
                        in ALLOWED_EXTENSIONS):
                    # Add current time in the file name
                    filename = secure_filename(image.filename)
                    filename = str(datetime.now().timestamp()) + filename
                    image.save(os.path.join(UPLOAD_FOLDER, filename))
                    data = {
                        "car_id": car_id,
                        "image_url": filename
                    }
                    Car_Image.add_images(data)  # Save each image
                else:
                    flash("File not allowed", "image")
                    return redirect(request.referrer)

    return redirect(request.referrer)


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
