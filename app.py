from flask import Flask
from route import api

def create_app():
    """Initialize and configure the Flask application."""
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(api, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
