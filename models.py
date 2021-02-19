from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    todos = db.relationship('ToDO', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}'.format(self.username)


class ToDO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(150))
    due_date = db.Column(db.Date, index=True)
    is_complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<ToDO {}>'.format(self.title)
