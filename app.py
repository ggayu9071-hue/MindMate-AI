from flask import Flask, render_template
from flask_login import LoginManager
from routes.chat import chat
from config import Config
from database.models import db, User
from routes.mood import mood
from routes.journal import journal

# Import Blueprints
from routes.auth import auth
from routes.dashboard import dashboard

app = Flask(__name__)

# -------------------------
# Load Configuration
# -------------------------
app.config.from_object(Config)

# -------------------------
# Initialize Database
# -------------------------
db.init_app(app)

# -------------------------
# Flask-Login Setup
# -------------------------
login_manager = LoginManager()
login_manager.init_app(app)

# Redirect users to login if not authenticated
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -------------------------
# Create Database Tables
# -------------------------
with app.app_context():
    db.create_all()

# -------------------------
# Register Blueprints
# -------------------------
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(chat)
app.register_blueprint(mood)
app.register_blueprint(journal)
# -------------------------
# Home Route
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# Run Application
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)