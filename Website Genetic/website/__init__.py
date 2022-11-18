from flask import Flask

def create_app():
    app =  Flask(__name__)
    app.config['SECRET_KEY'] = 'flask'
    from .views import views
    from .actions import actions,zuruck
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(actions, url_prefix='/')
    app.register_blueprint(zuruck, url_prefix = '/')
    return app
