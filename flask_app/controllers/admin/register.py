import random
from flask_bcrypt import Bcrypt
from flask import render_template, request, redirect, session

from flask_app import app

from flask_app.helpers.send_email import password_email, send_email
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route("/admin/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "role": request.form["role"],
            "nr_tel": request.form["nr_tel"]
        }
        if not User.validate_registration(data):
            redirect(request.referrer)
        # generate a random 10 character string for the password
        pass_char = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#^?"
        password = "".join(random.sample(pass_char, 10))
        message = password_email(data["email"], password)
        send_email(data["email"],"New Account", message)
        data["password"] = bcrypt.generate_password_hash(password)
        User.add_user(data)
        return redirect(request.referrer)
    return render_template(
        "admin/register.html",
        user=session["user"]
    )
