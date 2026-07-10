import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "mindmate_secret_key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///mindmate.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False