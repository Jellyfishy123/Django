import os

class Config:
    SECRET_KEY = '8e46490514eda3aeb0dfcf68d6a7d738'  
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tiendat311003@gmail.com'
    MAIL_PASSWORD = 'daeecwqsigrxnocx'