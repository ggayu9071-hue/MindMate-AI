from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from services.ai_service import get_ai_response

chat = Blueprint("chat", __name__)


@chat.route("/chat")
@login_required
def chat_page():
    return render_template("chat/chat.html")


@chat.route("/ask", methods=["POST"])
@login_required
def ask_ai():

    data = request.get_json()

    user_message = data.get("message")

    ai_reply = get_ai_response(user_message)

    return jsonify({
        "reply": ai_reply
    })