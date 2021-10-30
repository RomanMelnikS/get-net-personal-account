import datetime

from .database import db


class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(80)
    )
    balance = db.Column(
        db.Integer()
    )
    lines = db.relationship(
        'Lines',
        backref='profile',
        lazy='dynamic'
    )
    calls = db.relationship(
        'Calls',
        backref='profile',
        lazy='dynamic'
    )
    current_accounts = db.relationship(
        'CurrentAccount',
        backref='profile',
        lazy='dynamic'
    )
    created_on = db.Column(
        db.DateTime(),
        default=datetime.datetime.now
    )


class Lines(db.Model):
    __tablename__ = 'lines'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    profile_id = db.Column(
        db.Integer,
        db.ForeignKey('profiles.id')
    )
    type_of_line = db.Column(
        db.Integer()
    )
    cli = db.Column(
        db.Integer()
    )
    city = db.Column(
        db.String(80)
    )
    tariff = db.Column(
        db.String(80)
    )


class Calls(db.Model):
    __tablename__ = 'calls'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    profile_id = db.Column(
        db.Integer,
        db.ForeignKey('profiles.id')
    )
    line_id = db.Column(
        db.Integer,
        db.ForeignKey('lines.id')
    )
    direction = db.Column(
        db.String(80)
    )
    date = db.Column(
        db.DateTime(),
        default=datetime.datetime.now
    )
    duration = db.Column(
        db.Integer()
    )
    cost = db.Column(
        db.Integer()
    )


class CurrentAccount(db.Model):
    __tablename__ = 'current_accounts'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    profile_id = db.Column(
        db.Integer,
        db.ForeignKey('profiles.id')
    )
    account_number = db.Column(
        db.Integer()
    )
    service_name = db.Column(
        db.String(80)
    )
    date = db.Column(
        db.DateTime(),
        default=datetime.datetime.now
    )
    adress = db.Column(
        db.Text()
    )
    amount = db.Column(
        db.Integer()
    )
    status = db.Column(
        db.Boolean()
    )
