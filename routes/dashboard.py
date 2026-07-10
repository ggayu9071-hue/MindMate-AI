from flask import Blueprint, render_template
from flask_login import login_required, current_user
from database.models import Mood

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
@login_required
def dashboard_page():

    latest_mood = Mood.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Mood.created_at.desc()
    ).first()

    return render_template(
        "dashboard/dashboard.html",
        user=current_user,
        latest_mood=latest_mood
    )