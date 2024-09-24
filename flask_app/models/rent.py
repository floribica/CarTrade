from datetime import datetime
from flask_app.config.load_db import load_db
from flask_app.config.mysqlconnection import connectToMySQL

DB_NAME = load_db()


class Rent:
    def __init__(self, data):
        
        self.rent_id = data['rent_id']
        self.pickup_location = data['pickup_location']
        self.pickup_date = data['pickup_date']
        self.pickuo_time = data['pickup_time']
        self.dropoff_location = data['dropoff_location']
        self.dropoff_date = data['dropoff_date']
        self.dropoff_time = data['dropoff_time']
        self.car_id = data['car_id']
        self.client_id = data['client_id']
        
    
    @classmethod
    def add_rent(cls, data):
        query = "INSERT INTO rents (pickup_location, pickup_date, pickup_time, dropoff_location, dropoff_date, dropoff_time, car_id, client_id) VALUES (%(pickup_location)s, %(pickup_date)s, %(pickup_time)s, %(dropoff_location)s, %(dropoff_date)s, %(dropoff_time)s, %(car_id)s, %(client_id)s);"
        return connectToMySQL(DB_NAME).query_db(query, data)
    
    
    @classmethod
    def is_car_available(cls, data):
        query = """
            SELECT * FROM rents
            WHERE car_id = %(car_id)s
            AND (
                (pickup_date < %(dropoff_date)s OR (pickup_date = %(dropoff_date)s AND pickup_time < %(dropoff_time)s))
                AND
                (dropoff_date > %(pickup_date)s OR (dropoff_date = %(pickup_date)s AND dropoff_time > %(pickup_time)s))
            );
            """
        results = connectToMySQL(DB_NAME).query_db(query, data)
        if results:
            return True
        return False
    
    
    @classmethod
    def get_rent_by_id(cls, data):
        query = "SELECT * FROM rents WHERE car_id = %(car_id)s;"
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]
        return None
    
    
    @staticmethod
    def validate_rent(data):
        
        pickup_date = datetime.strptime(data['pickup_date'], "%Y-%m-%d").date()
        dropoff_date = datetime.strptime(data['dropoff_date'], "%Y-%m-%d").date()
        pickup_time = datetime.strptime(data['pickup_time'], "%H:%M").time()
        dropoff_time = datetime.strptime(data['dropoff_time'], "%H:%M").time()
        date_now = datetime.now().date()
        time_now = datetime.now().time()
        
        is_valid = True
        if len(data['pickup_location']) < 3 or len(data['dropoff_location']) < 3:
            is_valid = False
        if pickup_date >= dropoff_date:
            is_valid = False
        if Rent.is_car_available(data):
            is_valid = False
        if pickup_date < date_now:
            is_valid = False
        if dropoff_date < date_now:
            is_valid = False
        if pickup_date == date_now and pickup_time < time_now:
            is_valid = False
        return is_valid
