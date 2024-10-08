from flask_app.config.load_db import load_db
from flask_app.config.mysqlconnection import connectToMySQL

DB_NAME = load_db()


class Car:
    def __init__(self, data):

        self.car_id = data['car_id']
        self.year = data['year']
        self.brand = data['brand']
        self.model = data['model']
        self.style = data['style']
        self.conditions = data['conditions']
        self.km = data['km']
        self.description = data['description']
        self.image = data['image']
        self.rent_price = data['rent_price']
        self.user_id = data['user_id']
        self.display = data['display']


    @classmethod
    def get_all_cars(cls):
        query = "SELECT * FROM cars;"
        results = connectToMySQL(DB_NAME).query_db(query)
        cars = []
        if results:
            for car in results:
                cars.append(car)
        return cars
    
    
    @classmethod
    def delete_car(cls, data):
        query = "UPDATE cars SET display = 0 WHERE car_id = %(car_id)s;"
        return connectToMySQL(DB_NAME).query_db(query, data)


    @classmethod
    def get_selected_cars(cls, data):

        query = "SELECT * FROM cars WHERE display = 1 AND 1=1"
        if data['year']:
            query += " AND year = %(year)s"
        if data['brand']:
            query += " AND brand = %(brand)s"
        if data['style']:
            query += " AND style LIKE %(style)s"
        if data['conditions']:
            query += " AND conditions = %(conditions)s"
        if data['model']:
            query += " AND model LIKE %(model)s"
        if data['rent_price']:
            query += " AND rent_price = %(rent_price)s"
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
    def count_total_car_by_month(cls):
        query = "SELECT COUNT(car_id) as total_car, MONTHNAME(created_at) as month FROM cars WHERE display = 1 AND YEAR(created_at) = YEAR(CURDATE()) GROUP BY month;"
        result = connectToMySQL(DB_NAME).query_db(query)
        if result:
            return result
        return None
    
    
    @classmethod
    def get_similar_price_car(cls, rent_price,data):
        min_price = rent_price - 10
        max_price = rent_price + 10
        query = f"""
            SELECT
                *
            FROM cars
            WHERE display = 1
            AND rent_price BETWEEN {min_price} AND {max_price}
            AND car_id != %(car_id)s
            AND user_id = %(user_id)s
            ORDER BY rent_price
            LIMIT 1;
        """
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]
        return None


    @classmethod
    def count_cars_by_price(cls, price):
        query = "SELECT COUNT(*) FROM cars WHERE display = 1 AND price >= %(price)s;"
        data = {
            "price": price
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['COUNT(*)']
        return 0


    @classmethod
    def count_cars_by_year(cls, year):
        query = "SELECT COUNT(*) FROM cars WHERE display = 1 AND year = %(year)s;"
        data = {
            "year": year
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['COUNT(*)']
        return 0


    @classmethod
    def count_cars_by_brand(cls, brand):
        query = "SELECT COUNT(*) FROM cars WHERE display = 1 AND brand = %(brand)s;"
        data = {
            "brand": brand
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['COUNT(*)']
        return 0


    @classmethod
    def count_cars_by_style(cls, style):
        query = "SELECT COUNT(*) FROM cars WHERE display = 1 AND style = %(style)s;"
        data = {
            "style": style
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['COUNT(*)']
        return 0


    @classmethod
    def count_cars_by_conditions(cls, conditions):
        query = "SELECT COUNT(*) FROM cars WHERE display = 1 AND conditions = %(conditions)s;"
        data = {
            "conditions": conditions
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['COUNT(*)']
        return 0


    @classmethod
    def count_cars_by_model(cls, model):
        query = "SELECT COUNT(*) FROM cars WHERE display = 1 AND model = %(model)s;"
        data = {
            "model": model
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['COUNT(*)']


    @classmethod
    def count_cars_by_km(cls, km):
        query = "SELECT COUNT(*) FROM cars WHERE display = 1 AND km = %(km)s;"
        data = {
            "km": km
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['COUNT(*)']
        return 0


    @classmethod
    def count_cars_by_description(cls, description):
        query = "SELECT COUNT(*) FROM cars WHERE display = 1 AND description = %(description)s;"
        data = {
            "description": description
        }
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['COUNT(*)']
        return 0


    @classmethod
    def add_car(cls, data):
        query = """
            INSERT INTO cars
                (`year`, `brand`, `model`, `style`, `conditions`, `rent_price`, `km`, `image`, `description`, `user_id`)
            VALUES
                (%(year)s, %(brand)s, %(model)s, %(style)s, %(conditions)s, %(rent_price)s, %(km)s, %(image)s, %(description)s, %(user_id)s);
            """
        return connectToMySQL(DB_NAME).query_db(query, data)


    @classmethod
    def get_car_by_id(cls, data):
        query = "SELECT * FROM cars WHERE display = 1 AND car_id = %(car_id)s;"
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]
        return None

    @classmethod
    def get_all_cars_brand(cls):
        query = "SELECT brand FROM cars WHERE display = 1 GROUP BY brand;"
        results = connectToMySQL(DB_NAME).query_db(query)
        brands = []
        if results:
            for brand in results:
                brands.append(brand)
        return brands


    @classmethod
    def get_car_price(cls, data):
        query = "SELECT rent_price FROM cars WHERE display = 1 AND car_id = %(car_id)s;"
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return result[0]['rent_price']
        return None
