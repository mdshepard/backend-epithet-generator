def configure_app():
    import os
    import dotenv
    import flask

    PROJECT_ROOT = os.path.dirname(__file__)
    ENV_PATH = os.path.join(PROJECT_ROOT, '.env')
    dotenv.load_dotenv(ENV_PATH)
    app = flask.Flask(__name__)
    return app


app = configure_app()
