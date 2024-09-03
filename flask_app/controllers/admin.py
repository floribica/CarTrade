from flask import redirect, render_template, request, session

from flask_app import app
from flask_app.models.car import Car


@app.route('/admin/chart')
def admin_chart():
    if 'user' not in session:
        return redirect('/')
    if session['user']['user_id'] != 1:
        return redirect('/')
    return render_template('admin/chart.html')


@app.route('/admin/tables')
def admin_tables():
    if 'user' not in session:
        return redirect('/')
    if session['user']['user_id'] != 1:
        return redirect('/')
    all_cars = Car.get_all_cars()
    return render_template(
        'admin/tables.html',
        all_cars=all_cars
    )
