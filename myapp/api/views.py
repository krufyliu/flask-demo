from flask import jsonify, make_response
from flask_restful import Resource, Api, reqparse
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_httpauth import HTTPTokenAuth
from myapp.api import api

_api = Api(api)
seirializer = Serializer('123456', expires_in=1800)

auth = HTTPTokenAuth()

@auth.verify_token
def verify_token(token):
  try:
    seirializer.loads(token)
    return True
  except:
    return False

@auth.error_handler
def error_handler():
  return make_response('{"error": "Unauthorized"}', 401)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

@api.route('/token')
def token():
  args = parser.parse_args()
  username = args['name']
  print username
  token = seirializer.dumps({'username': username})
  return jsonify({'token': token})


class User(Resource):
  decorators = [auth.login_required]
  user = {'name': 'liujun'}
  def get(self, user_id):
    return self.user

  def put(self, user_id):
    return self.user

_api.add_resource(User, '/user/<user_id>')


