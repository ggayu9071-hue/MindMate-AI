from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from database.models import db, Mood

mood = Blueprint("mood", __name__)


@mood.route("/mood")
@login_required
def mood_page():
    return render_template("mood/mood.html")


@mood.route("/save_mood", methods=["POST"])
@login_required
def save_mood():

    selected_mood = request.form["mood"]

    new_mood = Mood(
        mood=selected_mood,
        user_id=current_user.id
    )

    db.session.add(new_mood)
    db.session.commit()

    return redirect("/dashboard")