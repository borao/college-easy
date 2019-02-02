import os
from flask import Flask, request, redirect, render_template
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


@app.route('/add_college', methods=['GET', 'POST'])
def add_college():
    if request.method == "POST":
        name = request.form.get('name')
        app_deadline = request.form.get('app_deadline')
        rec_deadline = request.form.get('rec_deadline')
        num_essays = request.form.get('num_essays')
        midyear_report = request.form.get('midyear_report')
        acceptance_rate = request.form.get('acceptance_rate')
        platform = request.form.get('platform')
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
            return redirect('/')
        except Exception as e:
            return str(e)
    else:
        return render_template("college.html")


@app.route('/edit_college', methods=['GET', 'POST'])
def edit_college():
    college = College.query.filter_by(name=request.args.get('name')).one()
    if request.method == "POST":
        college.name = request.form.get('name')
        college.app_deadline = request.form.get('app_deadline')
        college.rec_deadline = request.form.get('rec_deadline')
        college.num_essays = request.form.get('num_essay')
        college.midyear_report = request.form.get('midyear_report')
        college.acceptance_rate = request.form.get('acceptance_rate')
        college.platform = request.form.get('platform')
        College.commit()
        return redirect('/')
    else:
        try:
            is_editing = True
            return render_template("college.html", college=college, is_editing=is_editing)
        except Exception as e:
            return str(e)


if __name__ == '__main__':
    app.run()
