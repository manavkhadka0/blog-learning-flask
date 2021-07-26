
from dotenv import dotenv_values

class Config:
    config = dotenv_values(".env")
    SQLALCHEMY_DATABASE_URI = config['DB_URI']
    MAIL_USERNAME = config['EMAIL']
    MAIL_PASSWORD = config['PASS']    
    SECRET_KEY = config['SEC']
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True       