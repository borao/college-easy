from app import db


class College(db.Model):
    __tablename__ = 'college'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    app_deadline = db.Column(db.String())
    rec_deadline = db.Column(db.String())
    num_essays = db.Column(db.String())
    midyear_report = db.Column(db.String())
    acceptance_rate = db.Column(db.String())
    platform = db.Column(db.String())

    def __init__(self, name, app_deadline, rec_deadline, num_essays, midyear_report, acceptance_rate, platform):
        self.name = name
        self.app_deadline = app_deadline
        self.rec_deadline = rec_deadline
        self.num_essays = num_essays
        self.midyear_report = midyear_report
        self.acceptance_rate = acceptance_rate
        self.platform = platform

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
        }