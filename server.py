import os

from dotenv import load_dotenv

from flask_app import app
from flask_app.controllers import (
    dashboard,
    admin,
    cars,
    clients,
    payments
)

load_dotenv()
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
