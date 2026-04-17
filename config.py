# Configuration settings for Flask app

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FACE_RECOGNITION_CONFIDENCE_THRESHOLD = 0.6
    FACE_RECOGNITION_MODEL = 'model.h5'
