from database import db
from flask import Flask
from routes.skins import skins_bp

app = Flask(__name__)

app.register_blueprint(skins_bp)

if __name__ == "__main__":
    app.run(debug=True)
