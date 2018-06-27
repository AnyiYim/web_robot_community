from flask import jsonify, Flask

# from app import app
import config
from views import admin, user
from flask_cors import *

app = Flask(__name__)
app.config.from_object(config)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello World!'

#
# @app.route('/haha')
# def aahello_world():
#     return jsonify(code=0, msg='hello_world')


app.register_blueprint(admin.bp, url_prefix='/admin/')
app.register_blueprint(user.bp, url_prefix='/user/')

