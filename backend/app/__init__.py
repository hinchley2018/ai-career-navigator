from flask import Flask
from app.config import Config
from app.extensions import init_extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    init_extensions(app)

    # Register Blueprints (e.g., API routes)
    from app.api.routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
