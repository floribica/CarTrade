from flask import redirect, render_template, session

from flask_app import app
from flask_app.models.car import Car


@app.route('/admin/tables')
def admin_tables():
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "admin":
        return redirect('/')
    all_cars = Car.get_all_cars()
    user = session['user']
    return render_template(
        'admin/tables.html',
        all_cars=all_cars,
        user=user
    )


@app.route("/admin/delete/car/<int:car_id>")
def delete_car_admin(car_id):
    if 'user' not in session:
        return redirect('/')
    if session['user']['role'] != "admin":
        return redirect('/')
    Car.delete_car({"car_id": car_id})
    return redirect('/admin/tables')