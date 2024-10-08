from flask_bcrypt import Bcrypt
from flask import render_template, request, session, redirect

from flask_app import app
from flask_socketio import SocketIO, send

from flask_app.helpers.chatboot import process_message
from flask_app.models.car import Car
from flask_app.models.user import User

bcrypt = Bcrypt(app)
socketio = SocketIO(app)


@app.route("/")
def check():
    
    if 'user' not in session:
        return redirect("/dashboard")
    if session['user']["role"] == "seller":
        return redirect("/seller")
    if session['user']["role"] == "admin":
        return redirect("/admin")


@app.route("/dashboard")
def index():
    if 'user' not in session:
        user = {
            "user_id": -1,
            "first_name": "user",
            "last_name": "user",
            "email": "user",
            "role": "user"
        }
    else:
        user = session['user']
    all_cars = Car.get_all_cars()
    brands = Car.get_all_cars_brand()
    return render_template(
        'index.html',
        user=user,
        all_cars=all_cars,
        brands=brands
    )


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = {
            "email": request.form["email"],
            "password": request.form["password"]
        }
        if User.validate_login(data):
            user = User.get_user_by_email(data)
            session['user'] = {
                "user_id": user["user_id"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "email": user["email"],
                "role": user["role"]
            }
            return redirect("/")
    if 'user' in session:
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@socketio.on('message')
def handlemessage(msg):
    response = process_message(msg)
    send(response, broadcast=True)
