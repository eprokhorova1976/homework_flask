import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash


db=SQLAlchemy()


class User(db.Mode):
    id=db.Column(db.Integr, primary_key=True)
    username=db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


def set_password(self,password):
    self.password=generate_password_hash(password)

def __repr__(self):
    return f'User ({self.username}, {self.surname}, {self.email})'
