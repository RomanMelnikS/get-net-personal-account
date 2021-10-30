from flask_restful import Api, Resource, fields, marshal
from flask import request, Blueprint, Flask
from .database import db
from .models import Profile, Lines, Calls, CurrentAccount


app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

app.register_blueprint(api_bp, url_prefix='/api')

PROFILE_FIELDS = {
    'name': fields.String,
    'balance': fields.Integer,
    'created_on': fields.DateTime
}

LINE_FIELDS = {
    'type_of_line': fields.Integer,
    'cli': fields.Integer,
    'city': fields.String,
    'tariff': fields.String
}

CALL_FIELDS = {
    'direction': fields.String,
    'date': fields.DateTime,
    'duration': fields.Integer,
    'cost': fields.Integer
}

CURRENT_ACCOUNT_FIELDS = {
    'account_number': fields.Integer,
    'service_name': fields.String,
    'date': fields.DateTime,
    'adress': fields.String,
    'amount': fields.Integer,
    'status': fields.Boolean
}


@api.resource('/profile/<int:profile_id>/')
class ProfileView(Resource):
    def get(self, profile_id):
        profile = Profile.query.get_or_404(profile_id)
        values = marshal(profile, PROFILE_FIELDS)
        return values


@api.resource('/profiles/')
class ProfilesView(Resource):
    def get(self):
        profiles = Profile.query.all()
# paginate_profiles = Profile.query.paginate(page, per_page, error_out=False)
        values = marshal(profiles, PROFILE_FIELDS)
        return values

    def post(self):
        if request.is_json:
            data = request.get_json()
            new_profile = Profile(name=data['name'], balance=data['balance'])
            values = marshal(new_profile, PROFILE_FIELDS)
            db.session.add(new_profile)
            db.session.commit()
            return values
        return {'error': 'The request payload is not in JSON format'}


@api.resource('/lines/')
class LinesView(Resource):
    def get(self):
        query = Lines.query.all()
        lines = marshal(query, LINE_FIELDS)
        return lines

    def post(self):
        if request.is_json:
            data = request.get_json()
            new_query = Lines(
                profile_id=data['profile_id'],
                type_of_line=data['type_of_line'],
                cli=data['cli'],
                city=data['city'],
                tariff=data['tariff']
            )
            line = marshal(new_query, LINE_FIELDS)
            db.session.add(new_query)
            db.session.commit()
            return line
        return {'error': 'The request payload is not in JSON format'}


@api.resource('/calls/')
class CallsView(Resource):
    def get(self):
        query = Calls.query.all()
        calls = marshal(query, CALL_FIELDS)
        return calls

    def post(self):
        if request.is_json:
            data = request.get_json()
            new_query = Calls(
                profile_id=data['profile_id'],
                line_id=data['line_id'],
                direction=data['direction'],
                duration=data['duration'],
                cost=data['cost']
            )
            call = marshal(new_query, CALL_FIELDS)
            db.session.add(new_query)
            db.session.commit()
            return call
        return {'error': 'The request payload is not in JSON format'}


@api.resource('/current_accounts/')
class CurrentAccountView(Resource):
    def get(self):
        query = CurrentAccount.query.all()
        current_accounts = marshal(query, CURRENT_ACCOUNT_FIELDS)
        return current_accounts

    def post(self):
        if request.is_json:
            data = request.get_json()
            new_query = CurrentAccount(
                profile_id=data['profile_id'],
                account_number=data['account_number'],
                service_name=data['service_name'],
                adress=data['adress'],
                amount=data['amount'],
                status=data['status']
            )
            current_account = marshal(new_query, CURRENT_ACCOUNT_FIELDS)
            db.session.add(new_query)
            db.session.commit()
            return current_account
        return {'error': 'The request payload is not in JSON format'}
