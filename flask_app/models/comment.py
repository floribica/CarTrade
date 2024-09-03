import os

from dotenv import load_dotenv
from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL

load_dotenv()
DB_NAME = os.getenv("DB_NAME")

class Comment:
    def __init__(self, data):
        self.comment_id = data['comment_id']
        self.content = data['content']
        self.user_id = data['user_id']

    @classmethod
    def add_comment(cls, data):
        query = "INSERT INTO comments (content, user_id) VALUES (%(content)s, %(user_id)s);"
        return connectToMySQL(DB_NAME).query_db(query, data)
    
    @classmethod
    def get_comments(cls):
        query = "SELECT * FROM comments JOIN users ON comments.user_id = users.user_id;"
        results = connectToMySQL(DB_NAME).query_db(query)
        comments = []
        for comment in results:
            comments.append(comment)
        return comments
    
    
    @classmethod
    def get_comments_by_car_id(cls, data):
        query = "SELECT * FROM comments JOIN users ON comments.user_id = users.user_id WHERE car_id = %(car_id)s;"
        results = connectToMySQL(DB_NAME).query_db(query, data)
        comments = []
        if results:
            for comment in results:
                comments.append(comment)
        return comments
