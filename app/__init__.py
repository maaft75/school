from flask import Flask
import os

from app.admin.views import admin_blueprint

app = Flask(__name__)
app.secret_key = "ayodejiadedeji"

#REGISTERING BLUEPRINT
app.register_blueprint(admin_blueprint, url_prefix='/admin')
