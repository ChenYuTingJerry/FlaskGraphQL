from flask import Flask
from flask_graphql import GraphQLView

from app.apiv2 import blueprint as b1
from app.schema import schema


def register_blueprints(app):
    app.register_blueprint(b1)


def add_graphql(app):
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )


def create_app(config_name):
    """

      :param config_name:
      :return:
      """
    app = Flask(__name__)
    app.config.from_object(config_name)

    # bind db
    with app.app_context():
        from app import logger
        logger.init(app)

        from app import db
        mongo_db = db.mongodb
        mongo_db.init(app)
        db.init_db()

        register_blueprints(app)
        
        add_graphql(app)

    return app
