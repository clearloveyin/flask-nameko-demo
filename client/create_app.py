
from client import app, rpc
from client.router import api


def create_app():

    app.config.update(dict(
        NAMEKO_AMQP_URI='amqp://localhost'
    ))

    rpc.init_app(app)
    app.register_blueprint(api)
    return app

