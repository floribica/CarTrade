import os

from dotenv import load_dotenv

from flask_app.config.mysqlconnection import connectToMySQL

load_dotenv()
DB_NAME = os.getenv("DB_NAME")


class Car:
    def __init__(self, data):

        self.car_id = data['car_id']
        self.year = data['year']
        self.brand = data['brand']
        self.model = data['model']
        self.style = data['style']
        self.condition = data['condition']
        self.price = data['price']
        self.km = data['km']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_cars(cls):
        query = "SELECT * FROM cars;"
        results = connectToMySQL(DB_NAME).query_db(query)
        cars = []
        for car in results:
            cars.append(car)
        return cars

    
    @classmethod
    def get_selected_cars(cls, data):
        
        query = "SELECT * FROM cars WHERE 1=1"
        if data['year']:
            query += " AND year = %(year)s"
        if data['brand']:
            query += " AND brand = %(brand)s"
        if data['style']:
            query += " AND style = %(style)s"
        if data['condition']:
            query += " AND condition = %(condition)s"
        if data['model']:
            query += " AND model = %(model)s"
        if data['price']:
            query += " AND price >= %(price)s"
        else:
            query += ";"
        results = connectToMySQL(DB_NAME).query_db(query, data)

        cars = []
        if results:
            for car in results:
                cars.append(car)
            return cars
        return None
    
    
    @classmethod
    def count_cars_by_price(cls, price):
        query = "SELECT COUNT(*) FROM cars WHERE price >= %(price)s;"
        data = {
            "price": price
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        return result[0]['COUNT(*)']
    
    
    @classmethod
    def count_cars_by_year(cls, year):
        query = "SELECT COUNT(*) FROM cars WHERE year = %(year)s;"
        data = {
            "year": year
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        return result[0]['COUNT(*)']
    
    
    @classmethod
    def count_cars_by_brand(cls, brand):
        query = "SELECT COUNT(*) FROM cars WHERE brand = %(brand)s;"
        data = {
            "brand": brand
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        return result[0]['COUNT(*)']
    
    
    @classmethod
    def count_cars_by_style(cls, style):
        query = "SELECT COUNT(*) FROM cars WHERE style = %(style)s;"
        data = {
            "style": style
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        return result[0]['COUNT(*)']
    
    
    @classmethod
    def count_cars_by_condition(cls, condition):
        query = "SELECT COUNT(*) FROM cars WHERE condition = %(condition)s;"
        data = {
            "condition": condition
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        return result[0]['COUNT(*)']
    
    
    @classmethod
    def count_cars_by_model(cls, model):
        query = "SELECT COUNT(*) FROM cars WHERE model = %(model)s;"
        data = {
            "model": model
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        return result[0]['COUNT(*)']
    
    
    @classmethod
    def count_cars_by_km(cls, km):
        query = "SELECT COUNT(*) FROM cars WHERE km = %(km)s;"
        data = {
            "km": km
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        return result[0]['COUNT(*)']
    
    
    @classmethod
    def count_cars_by_description(cls, description):
        query = "SELECT COUNT(*) FROM cars WHERE description = %(description)s;"
        data = {
            "description": description
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        return result[0]['COUNT(*)']


    @classmethod
    def add_car(cls, data):
        query = "INSERT INTO cars (`year`, `brand`, `model`, `style`, `condition`, `price`, `km`, `image`, `DESCRIPTION`) VALUES (%(year)s, %(brand)s, %(model)s, %(style)s, %(condition)s, %(price)s, %(km)s, %(image)s, %(description)s);"
        return connectToMySQL(DB_NAME).query_db(query, data)
    
    
    @classmethod
    def get_car_by_id(cls, data):
        query = "SELECT * FROM cars WHERE car_id = %(car_id)s;"
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]
        return None