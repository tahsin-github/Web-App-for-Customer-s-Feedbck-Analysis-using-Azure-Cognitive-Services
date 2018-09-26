from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyodbc

from azuretext.database_setting import params

app = Flask(__name__)


app.config.update(dict(
    SECRET_KEY='16a69fbd6d591c61299a0ac9ff52bc8c',
    WTF_CSRF_SECRET_KEY='a69fbd6d591c61299a0ac9ff52bc8c',
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params,
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
))

db = SQLAlchemy(app)

from azuretext import routes