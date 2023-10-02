from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@143.110.147.30/hooplogic'
db = SQLAlchemy(app)
