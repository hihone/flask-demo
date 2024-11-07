from flask import Flask



if __name__ == '__main__':
    app = Flask(__name__)
    app.debug = True

    from bule_demo.rest_api.blueprint_api import mod
    app.register_blueprint(mod)

    app.run(port=5001)