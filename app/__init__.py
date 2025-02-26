from .app import app
from .routes import pig_bp
app.register_blueprint(pig_bp, url_prefix='/PigAPI')
