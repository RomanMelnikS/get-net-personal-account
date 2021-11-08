from flask import Blueprint, Flask, Response, request
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    current_user,
    jwt_required
)
from flask_mail import Mail, Message
from flask_rest_paginate import Pagination
from flask_restful import Api, Resource, fields, marshal

from config import Config

from .database import db
from .models import Calls, Lines, PaymentAccount, Profile

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
jwt = JWTManager(app)
mail = Mail(app)
pagination = Pagination(app, db)
response = Response


app.register_blueprint(api_bp, url_prefix='/api')


@jwt.user_identity_loader
def user_identity_lookup(profile):
    return profile.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return Profile.query.filter_by(id=identity).one_or_none()


@api.resource('/login/')
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        profile = Profile.query.filter_by(
            username=data['username']
            ).one_or_none()
        if profile and profile.check_password(data['password']):
            access_token = create_access_token(
                identity=profile
            )
            result = {'token': access_token}
            return result
        return {'error': 'Invalid username and password'}


@api.resource('/profile/me/')
class ProfileView(Resource):

    profile_fields = {
        'name': fields.String,
        'email': fields.String,
        'balance': fields.Integer,
        'created_on': fields.DateTime
    }

    @jwt_required()
    def get(self):
        profile_obj = Profile.query.get_or_404(current_user.id)
        profile = marshal(profile_obj, self.profile_fields)
        return profile


@api.resource('/profile/')
class ProfilesView(Resource):
    def post(self):
        if request.is_json:
            data = request.get_json()
            new_profile = Profile(
                name=data['name'],
                balance=data['balance'],
                email=data['email'],
                username=data['username'],
                password=data['password']
            )
            new_profile.set_password(data['password'])
            db.session.add(new_profile)
            db.session.commit()
            return {'message': 'Profile succesfull created'}
        return {'error': 'The request payload is not in JSON format'}


@api.resource('/lines/')
class LinesView(Resource):

    line_fields = {
        'type_of_line': fields.Integer,
        'cli': fields.Integer,
        'city': fields.String,
        'tariff': fields.String
    }

    @jwt_required()
    def get(self):
        lines_objs = Lines.query.filter_by(
            profile_id=current_user.id
        ).all()
        lines = pagination.paginate(
            lines_objs,
            self.line_fields
        )
        return lines

    @jwt_required()
    def post(self):
        if request.is_json:
            data = request.get_json()
            new_line = Lines(
                profile_id=current_user.id,
                type_of_line=data['type_of_line'],
                cli=data['cli'],
                city=data['city'],
                tariff=data['tariff']
            )
            line = marshal(new_line, self.line_fields)
            db.session.add(new_line)
            db.session.commit()
            return line
        return {'error': 'The request payload is not in JSON format'}


@api.resource('/calls/')
class CallsView(Resource):

    call_fields = {
        'direction': fields.String,
        'date': fields.DateTime,
        'duration': fields.Integer,
        'cost': fields.Integer
    }

    @jwt_required()
    def get(self):
        calls_objs = Calls.query.filter_by(
            profile_id=current_user.id
        ).all()
        calls = pagination.paginate(
            calls_objs,
            self.call_fields
        )
        return calls

    @jwt_required()
    def post(self):
        if request.is_json:
            data = request.get_json()
            new_call = Calls(
                profile_id=current_user.id,
                line_id=data['line_id'],
                direction=data['direction'],
                duration=data['duration'],
                cost=data['cost']
            )
            call = marshal(new_call, self.call_fields)
            cost_call = new_call.cost * new_call.duration
            balance_upd = current_user.balance - cost_call
            current_user.balance = balance_upd
            db.session.add(new_call)
            db.session.commit()
            return call
        return {'error': 'The request payload is not in JSON format'}


@api.resource('/payment_accounts/')
class PaymentAccountView(Resource):

    pay_account_fields = {
        'account_number': fields.Integer,
        'service_name': fields.String,
        'date': fields.DateTime,
        'adress': fields.String,
        'amount': fields.Integer,
        'status': fields.Boolean
    }

    @jwt_required()
    def get(self):
        pay_accounts_obj = PaymentAccount.query.filter_by(
            profile_id=current_user.id
        ).all()
        pay_accounts = pagination.paginate(
            pay_accounts_obj, self.pay_account_fields
        )
        return pay_accounts

    @jwt_required()
    def post(self):
        if request.is_json:
            data = request.get_json()
            new_pay_account = PaymentAccount(
                profile_id=current_user.id,
                account_number=data['account_number'],
                service_name=data['service_name'],
                adress=data['adress'],
                amount=data['amount'],
                status=data['status']
            )
            pay_account = marshal(new_pay_account, self.pay_account_fields)
            if new_pay_account.status:
                balance_upd = current_user.balance - new_pay_account.amount
                current_user.balance = balance_upd
            db.session.add(new_pay_account)
            db.session.commit()
            return pay_account
        return {'error': 'The request payload is not in JSON format'}


@api.resource('/send_detail_for_current_account/')
class Mailer(Resource):
    @jwt_required()
    def get(self):
        email = current_user.email
        msg = Message('Get-Net-Personal-Account', recipients=[email])
        msg.html = '<h2>Детализация вашего счета:</h2> \
            \n<p>Заплатите всё или конец!</p>'
        mail.send(msg)
        return {'message': 'OK'}
