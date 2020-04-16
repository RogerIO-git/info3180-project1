from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost/info3180_project_1"
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://odmeryjflnxmph:a78e3ed20280cc577698344a03a36c62a362c3bcc7a5c14d25b54ddd6d3fe76f@ec2-18-210-51-239.compute-1.amazonaws.com:5432/d41e4kl2ts2u0i'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://kzutmuyqzhdynb:7e6221982457a002b10d5dec7515d795bccb5002b038184476495ee3b373fe58@ec2-3-211-48-92.compute-1.amazonaws.com:5432/drevtm32oh602'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
