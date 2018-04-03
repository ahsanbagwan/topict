from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def get_topics():
    print r.json()
    return render_template('qotd.html', quote=r.json())