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
    """
    Workflow: A user selects a college from the 'edit college' dropdown and encounters the else case of this
    method because there is no post request yet. Then, once they edit the information, they submit the form
    with a post request which enters the if condition of the function.
    :return: if the user successfully edits, the '/' url
    """
    college = College.query.filter_by(name=request.args.get('name')).first()
    # Run this once the user makes some edits and submits the form with a post request
    if request.method == "POST":
        college.name = request.form.get('name')
        college.app_deadline = request.form.get('app_deadline')
        college.rec_deadline = request.form.get('rec_deadline')
        college.num_essays = request.form.get('num_essay')
        college.midyear_report = request.form.get('midyear_report')
        college.acceptance_rate = request.form.get('acceptance_rate')
        college.platform = request.form.get('platform')
        db.session.commit()
        return redirect('/')
    # Run this if the user is visiting the edit page for the first time (no edits yet)
    else:
        try:
            is_editing = True
            if request.args.get('name') is None:
                raise ValueError('There is no college specified for editing.')
            return render_template("college.html", college=college, is_editing=is_editing)
        except Exception as e:
            return str(e)


@app.route('/delete_college', methods=['GET', 'POST'])
def delete_college():
    college_to_delete = College.query.filter_by(name=request.args.get('name')).first()
    db.session.delete(college_to_delete)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run()
