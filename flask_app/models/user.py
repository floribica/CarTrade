import os
import re
from flask_bcrypt import Bcrypt

from dotenv import load_dotenv
from flask import flash
from flask_app import app

from flask_app.config.mysqlconnection import connectToMySQL

bcrypt = Bcrypt(app)
load_dotenv()
DB_NAME = os.getenv("DB_NAME")

class User:
    def __init__(self, data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        
        
    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB_NAME).query_db(query, data)
        if results:
            return results[0]
        return False
    
    
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DB_NAME).query_db(query, data)
    
    
    @staticmethod
    def validate_login(data):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, data['email']):
            flash("Invalid email address", "login")
            return False
        user = User.get_user_by_email(data)
        if not user:
            flash("Invalid email", "login")
            return False
        if not bcrypt.check_password_hash(user['password'], data['password']):
            flash("Invalid password", "login")
            return False
        return True
    
    
    @staticmethod
    def validate_registration(data):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, data['email']):
            flash("Invalid email address", "register")
            return False
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters", "register")
            return False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters", "register")
            return False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters", "register")
            return False
        if data['password'] != data['confirm_password']:
            flash("Passwords do not match", "register")
            return False
        if User.get_user_by_email(data):
            flash("Email already in use", "register")
            return False
        return True
    