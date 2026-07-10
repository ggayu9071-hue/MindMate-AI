from flask import Blueprint, render_template, request, redirect
from database.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

auth = Blueprint("auth", __name__)

# -------------------------
# LOGIN
# -------------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    print("========== LOGIN ==========")
    print("Request Method:", request.method)

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        print("Email Entered:", email)
        print("Password Entered:", password)

        user = User.query.filter_by(email=email).first()

        if user:
            print("✅ User Found")
            print("Stored Hash:", user.password)

            if check_password_hash(user.password, password):
                print("✅ Password Correct")
                login_user(user)
                print("✅ Logged In Successfully")
                return redirect("/dashboard")
            else:
                print("❌ Wrong Password")

        else:
            print("❌ User Not Found")

        return "Invalid email or password"

    return render_template("auth/login.html")


# -------------------------
# REGISTER
# -------------------------
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email already registered"

        password = generate_password_hash(request.form["password"])

        user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("auth/register.html")


# -------------------------
# LOGOUT
# -------------------------
@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/")