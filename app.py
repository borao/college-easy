import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import College


@app.route('/')
def index():
    try:
        colleges = College.query.all()
        return render_template("index.html", colleges=colleges)
    except Exception as e:
        return str(e)


@app.route('/add_college')
def add_college():
    name = request.args.get('name')
    app_deadline = request.args.get('app_deadline')
    rec_deadline = request.args.get('rec_deadline')
    num_essays = request.args.get('num_essays')
    midyear_report = request.args.get('midyear_report')
    acceptance_rate = request.args.get('acceptance_rate')
    platform = request.args.get('platform')
    try:
        college = College(
            name=name,
            app_deadline=app_deadline,
            rec_deadline=rec_deadline,
            num_essays=num_essays,
            midyear_report=midyear_report,
            acceptance_rate=acceptance_rate,
            platform=platform,
        )
        db.session.add(college)
        db.session.commit()
        return "College added. college id={}".format(college.id)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
