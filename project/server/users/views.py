from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

user_index_blueprint = Blueprint('user', __name__)

class UserIndexAPI(MethodView):
    """
    User Registration Resource
    """
    def get(self):
        users_table = User.query.order_by(User.id).all()
        print(users_table)
        list = []
        for user in users_table:
            user_info = []
            user_info.append("User id: " + str(user.id))
            if user.email: 
                user_info.append("email: " + str(user.email))
            user_info.append("registered on: " + str(user.registered_on))
            user_info.append("admin status: " + str(user.admin))
            list.append(user_info)
        return make_response(jsonify(list)), 201

# define the API resources
user_index_view = UserIndexAPI.as_view('user_index_api')

# add Rules for API Endpoints
user_index_blueprint.add_url_rule(
    '/user/index',
    view_func=user_index_view,
    methods=['GET']
)