import os

from dotenv import load_dotenv

from flask_app import app
from flask_app.controllers import (
    dashboard,
    cars,
    clients,
    payments
)
from flask_app.controllers.seller import chart, confirm, tables, dashboard, add_car
from flask_app.controllers.admin import dashboard, chart,confirm, tables, register

load_dotenv()
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
