from flask_app.config.load_db import load_db
from flask_app.config.mysqlconnection import connectToMySQL

DB_NAME = load_db()


class Payment:
    def __init__(self, data):
        
        self.payment_id = data['payment_id']
        self.type = data['type']
        self.status = data['status']
        self.amount = data['amount']
        self.user_id = data['user_id']
        self.car_id = data['car_id']
        self.client_id = data['client_id']
        