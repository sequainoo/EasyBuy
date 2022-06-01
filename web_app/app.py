#!/usr/bin/python3
"""flask application entry point"""

from flask import Flask
from flask_cors import CORS

from .views import app_views
from .admin_views import admin_views


app = Flask(__name__)
app.register_blueprint(app_views)
app.register_blueprint(admin_views)
app.secret_key = b'easybuy'

cors = CORS(app, resources={r'/*': {'origins': '*', 'methods': '*', 'headers': ['Content-Type']}})
if __name__ == '__main__':
    app.run()
