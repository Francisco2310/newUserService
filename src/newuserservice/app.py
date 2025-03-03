from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from extensions import db  
from config import Config, BASE_DIR
from pathlib import Path
import sys
from routes.usuario_route import usuarios_bp

sys.path.append(str(BASE_DIR))
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(usuarios_bp)

with app.app_context():
    from models.usuario import usuario


if __name__ == "__main__":
    app.run(debug=True)

