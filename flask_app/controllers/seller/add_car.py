from datetime import datetime
import os
from dotenv import load_dotenv
from flask import flash, redirect, render_template, request, session

from flask_app import app
from werkzeug.utils import secure_filename

from flask_app.models.car import Car
from flask_app.models.car_image import Car_Image


load_dotenv()
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")


@app.route('/add/car', methods=['POST', 'GET'])
def add_new_car():
    if request.method == 'GET':
        if 'user' not in session:
            return redirect('/')
        if session['user']['user_id'] != 1:
            return redirect('/')
        user = session['user']
        return render_template('seller/add_car.html', user=user)
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
        "rent_price": request.form.get("rent_price"),
        "km": request.form.get("km"),
        "description": request.form.get("description"),
        "conditions": request.form.get("conditions"),
    }
    data['user_id'] = session['user']['user_id']
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
    else:
        return redirect(request.referrer)
    Car.add_car(data)
    return render_template('seller/add_car.html')


@app.route("/car/add_image/<int:car_id>", methods=['POST', 'GET'])
def add_car_image(car_id):
    if 'user' not in session:
        return redirect('/')
    if session['user']['user_id'] != 1:
        return redirect('/')

    if request.method == 'GET':
        return render_template('seller/add_image.html', car_id=car_id)

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

