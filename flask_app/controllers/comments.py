from flask import redirect, request, session

from flask_app import app

from flask_app.models.comment import Comment


@app.route("/add/comment", methods=["POST"])
def add_comment():
    if 'user' not in session:
        return redirect("/")
    else:
        data = {
            "content": request.form["content"],
            "user_id": session['user']['user_id']
        }
        if data['content'] == "":
            return redirect("/")
        Comment.add_comment(data)
        return redirect("/")
