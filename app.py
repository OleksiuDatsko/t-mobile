from flask import Flask
from controllers.subscriber_controller import subscriber_bp

app = Flask(__name__)
app.secret_key = "super-secret"
app.register_blueprint(subscriber_bp, url_prefix="/subscribers")

if __name__ == "__main__":
    app.run(debug=True)
