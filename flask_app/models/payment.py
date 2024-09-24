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
    
    
    @classmethod
    def add_payment(cls, data):
        query = "INSERT INTO payments (status, amount, user_id, car_id, client_id) VALUES (%(status)s, %(amount)s, %(user_id)s, %(car_id)s, %(client_id)s);"
        return connectToMySQL(DB_NAME).query_db(query, data)

    
    @classmethod
    def confirm_payment(cls, data):
        query = "UPDATE payments SET confirmation = 1 WHERE payment_id = %(payment_id)s;"
        return connectToMySQL(DB_NAME).query_db(query, data)
    
    
    @classmethod
    def cance_payment(cls, data):
        query = "UPDATE payments SET confirmation = 0 WHERE payment_id = %(payment_id)s;"
        return connectToMySQL(DB_NAME).query_db(query, data)
    
    
    @classmethod
    def get_all_payments(cls, data):
        query = "SELECT * FROM payments JOIN clients ON payments.client_id = clients.client_id JOIN cars ON payments.car_id = cars.car_id WHERE payments.user_id = %(user_id)s;"
        results = connectToMySQL(DB_NAME).query_db(query, data)
        payments = []
        for payment in results:
            payments.append(payment)
        return payments


    @classmethod
    def count_total_confirm_by_month(cls):
        query = "SELECT COUNT(payment_id) AS total_confirm, MONTHNAME(created_at) AS month FROM payments WHERE YEAR(created_at) = YEAR(CURDATE()) AND confirmation = 1 GROUP BY month;"
        result = connectToMySQL(DB_NAME).query_db(query)
        if result:
            return result
        return None


    @classmethod
    def count_total_unconfirm_by_month(cls):
        query = "SELECT COUNT(payment_id) AS total_unconfirm, MONTHNAME(created_at) AS month FROM payments WHERE YEAR(created_at) = YEAR(CURDATE()) AND confirmation = 0 GROUP BY month;"
        result = connectToMySQL(DB_NAME).query_db(query)
        if result:
            return result
        return None


    @classmethod
    def get_payment_by_id(cls, data):
        query = "SELECT * FROM payments WHERE payment_id = %(payment_id)s;"
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]
        return None
