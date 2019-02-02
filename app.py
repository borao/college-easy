import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import College

@app.route('/')
def hello_world():
    try:
        colleges = College.query.all()
        return render_template("index.html", colleges=colleges)
    except Exception as e:
        return (str(e))


if __name__ == '__main__':
    app.run()
