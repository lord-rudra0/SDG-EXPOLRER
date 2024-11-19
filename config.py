import os

class Config:
  SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db' 
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    
   
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False  
    
    
CACHE_TYPE = 'simple'
CACHE_DEFAULT_TIMEOUT = 300  
