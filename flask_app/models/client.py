from flask_app.config.load_db import load_db
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.helpers.email_check import check_email

DB_NAME = load_db()


class Client:
    def __init__(self, data):

        self.client_id = data['client_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.nr_tel = data['nr_tel']
        self.car_id = data['car_id']


    @classmethod
    def add_client(cls, data):
        query = """
            INSERT INTO clients
                (first_name, last_name, email, nr_tel, car_id)
            VALUES
                (%(first_name)s, %(last_name)s, %(email)s, %(nr_tel)s, %(car_id)s);
            """
        return connectToMySQL(DB_NAME).query_db(query, data)


    @classmethod
    def get_client_id(cls, data):
        # Get the client ID of the last client that was just added
        query = """
            SELECT
                client_id 
            FROM clients
            WHERE first_name = %(first_name)s 
            AND last_name = %(last_name)s 
            AND email = %(email)s 
            AND nr_tel = %(nr_tel)s
            AND car_id = %(car_id)s
            ORDER BY client_id
            DESC
            LIMIT 1;
        """
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['client_id']
        return None
    
    
    @classmethod
    def get_client_by_id(cls, data):
        query = "SELECT * FROM clients WHERE client_id = %(client_id)s;"
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]
        return None
    
    
    @classmethod
    def count_total_client_by_month(cls):
        query = """
            SELECT
                COUNT(client_id) AS total_client,
                MONTHNAME(created_at) AS month
            FROM clients
            WHERE YEAR(created_at) = YEAR(CURDATE())
            GROUP BY month;
        """
        result = connectToMySQL(DB_NAME).query_db(query)
        if result:
            return result
        return None


    @staticmethod
    def validate_client(data):
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
        if len(data['last_name']) < 2:
            is_valid = False
        if not check_email(data['email']):
            is_valid = False
        if len(data['nr_tel']) < 2:
            is_valid = False
        if len(data['car_id']) < 1:
            is_valid = False
        return is_valid
