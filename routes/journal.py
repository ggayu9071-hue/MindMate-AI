from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user

from database.models import db, Journal

journal = Blueprint("journal", __name__)


@journal.route("/journal", methods=["GET", "POST"])
@login_required
def journal_page():

    if request.method == "POST":

        content = request.form["content"]

        entry = Journal(
            content=content,
            user_id=current_user.id
        )

        db.session.add(entry)
        db.session.commit()

        return redirect("/journal")

    journals = Journal.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Journal.created_at.desc()
    ).all()

    return render_template(
        "journal/journal.html",
        journals=journals
    )