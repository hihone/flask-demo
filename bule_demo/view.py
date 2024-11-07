from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = '2345676543'
    app.config.from_object('config.default')
    app.config.from_envvar('FLASK_DEMO_CONFIG_FILE')
    app.config.update(SQLALCHEMY_POOL_SIZE=1)

    from models.model import db

    db.init_app(app)

    from bule_demo.views.demo import bp
    from bule_demo.views.demo1 import bp as demo1
    from bule_demo.views.login import bp as login_bp
    app.register_blueprint(bp)
    app.register_blueprint(demo1)
    app.register_blueprint(login_bp)

    app.run(port=5002)