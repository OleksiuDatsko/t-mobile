from flask import Flask
from controllers.subscriber_controller import subscriber_bp
from controllers.tariff_controller import tariff_bp

app = Flask(__name__)
app.secret_key = "super-secret"
app.register_blueprint(subscriber_bp, url_prefix="/")
app.register_blueprint(tariff_bp, url_prefix="/tariffs")

if __name__ == "__main__":
    app.run(debug=True)
