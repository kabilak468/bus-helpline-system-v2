from flask import Flask
from dotenv import load_dotenv
import os

from app.api.bus_routes import bus_routes
from app.api.telephony_routes import telephony_routes

load_dotenv()

app = Flask(__name__)

app.register_blueprint(
    bus_routes,
    url_prefix="/api"
)

app.register_blueprint(
    telephony_routes,
    url_prefix="/api"
)


@app.route("/")
def home():
    return "Smart Bus Tracking IVR V2 Backend is running!"


@app.route("/health")
def health():
    return {
        "status": "success",
        "message": "Backend is healthy"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )