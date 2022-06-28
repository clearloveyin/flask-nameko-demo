from flask import Flask
from flask_nameko import FlaskPooledClusterRpcProxy

rpc = FlaskPooledClusterRpcProxy()
app = Flask(__name__)
