from flask import render_template, session, redirect

from flask_app import app


@app.route("/seller")
def seller():
    if 'user' not in session:
        return redirect("/")
    if session['user']['role'] != 'seller':
        return redirect("/")
    user = session['user']
    return render_template(
        "seller/index.html",
        user=user
    )