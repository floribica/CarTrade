from flask_app.config.load_db import load_db
from flask_app.config.mysqlconnection import connectToMySQL

DB_NAME = load_db()


class Car_Image:
    def __init__(self, data):

        self.image_id = data['image_id']
        self.car_id = data['car_id']
        self.image_url = data['image_url']

    @classmethod
    def add_images(cls, data):
        query = "INSERT INTO car_images (car_id, image_url) VALUES (%(car_id)s, %(image_url)s);"
        return connectToMySQL(DB_NAME).query_db(query, data)

    @classmethod
    def get_images_by_car_id(cls, data):
        query = "SELECT * FROM car_images WHERE car_id = %(car_id)s;"
        results = connectToMySQL(DB_NAME).query_db(query, data)
        images = []
        if results:
            for image in results:
                images.append(image)
        return images
