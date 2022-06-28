from flask import Blueprint
from client import rpc

api = Blueprint('api', __name__, url_prefix="")


@api.route('/create/order', methods=['POST'])
def CreateOrder():
    result = rpc.order_service.create_order('100005768799')
    return result


@api.route('/login', methods=['POST'])
def Login():
    result = rpc.user_service.login('15515807597')
    return result

