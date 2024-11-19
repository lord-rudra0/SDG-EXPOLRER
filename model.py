from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
# Compare this snippet from test.py:
from app import app
import unittest
import tempfile
import os
  
class TestApp(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'No entries here so far' in rv.data

    def test_login(self):
        rv = self.app.post('/login', data=dict(
            email='admin',
            password='admin'

        ))
        assert b'Login successful' in rv.data
  
    def test_signup(self):
        rv = self.app.post('/signup', data=dict(
            username='admin',
            email='admin',
            password='admin',
            phone='1234567890'
        ))
        assert b'Signup successful' in rv.data

    def test_logout(self):
        rv = self.app.get('/logout')
        assert b'Logout successful' in rv.data
if __name__ == '__main__':
    unittest.main(debug=True)