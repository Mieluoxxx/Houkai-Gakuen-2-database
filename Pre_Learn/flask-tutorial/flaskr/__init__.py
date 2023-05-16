import os

from flask import Flask
from . import db, auth, blog, medicine, customer, orderlist

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = '111'
    app.config.from_mapping(
        SCRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    app.register_blueprint(auth.bp)

    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    
    app.register_blueprint(medicine.bp)
    app.add_url_rule('/', endpoint='medicine')

    app.register_blueprint(customer.bp)
    app.add_url_rule('/', endpoint='customer')

    app.register_blueprint(orderlist.bp)
    app.add_url_rule('/', endpoint='orderlist')
    return app
