from datetime import datetime
import os
import smtplib

from dotenv import load_dotenv

from flask_app.helpers.calculator import calculate_price
from flask_app.models.car import Car
from flask_app.models.client import Client
from flask_app.models.payment import Payment
from flask_app.models.rent import Rent

load_dotenv()
ADMINEMAIL = os.getenv("ADMINEMAIL")
PASSWORD = os.getenv("PASSWORD")
COMPANY_NAME = os.getenv("COMPANY_NAME")


def send_email(to_addr, subject, html_content):
    sender = f"{COMPANY_NAME} <{ADMINEMAIL}>"
    msg = f"From: {sender}\r\nTo: {to_addr}\r\nSubject: {
        subject}\r\nContent-Type: text/html\r\n\r\n{html_content}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(ADMINEMAIL, PASSWORD)
    server.sendmail(sender, to_addr, msg)
    server.quit()


def user_email_confirm(data):
    car = Car.get_car_by_id(data)
    amount = calculate_price(data)
    days = (datetime.strptime(data["dropoff_date"], "%Y-%m-%d") -
            datetime.strptime(data["pickup_date"], "%Y-%m-%d")).days
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CarTrade Invoice</title>
    </head>
    <body style="font-family: Arial, sans-serif; color: #322d28; background-color: #f4f4f4; margin: 0; padding: 0;">

    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f4f4f4; padding: 20px;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border: 1px solid #dddddd; padding: 20px;">
                    <tr>
                        <td align="center" style="padding: 10px 0 20px 0;">
                            <img src="http://www.travelerie.com/wp-content/uploads/2014/04/PlaceholderLogoBlue.jpg" alt="CarTrade" style="display: block; width: 200px;"/>
                        </td>
                    </tr>
                    <tr>
                        <td align="left" style="font-size: 16px; padding: 20px;">
                            <h2 style="color: #1779ba; font-size: 24px;">Invoice</h2>
                            <p>Hello, {data["first_name"]} {data["last_name"]},</p>
                            <p>Thank you for your order!</p>
                        </td>
                    </tr>
                    <tr>
                        <td align="left">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
                                <thead>
                                    <tr>
                                        <th align="left" style="border-bottom: 1px solid #dddddd; padding: 8px;">Item Description</th>
                                        <th align="center" style="border-bottom: 1px solid #dddddd; padding: 8px;">Item ID</th>
                                        <th align="center" style="border-bottom: 1px solid #dddddd; padding: 8px;">Days</th>
                                        <th align="right" style="border-bottom: 1px solid #dddddd; padding: 8px;">Amount</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td style="padding: 8px; border-bottom: 1px solid #dddddd;">{car["brand"]} {car["model"]} {car["year"]}</td>
                                        <td align="center" style="padding: 8px; border-bottom: 1px solid #dddddd;">{data["car_id"]}</td>
                                        <td align="center" style="padding: 8px; border-bottom: 1px solid #dddddd;">{days}</td>
                                        <td align="right" style="padding: 8px; border-bottom: 1px solid #dddddd;">${amount["total_amount"]}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" style="padding: 20px;">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                    <td align="left" style="padding: 8px;">Subtotal</td>
                                    <td align="right" style="padding: 8px;">${amount["subtotal"]}</td>
                                </tr>
                                <tr>
                                    <td align="left" style="padding: 8px;">Shipping & Handling</td>
                                    <td align="right" style="padding: 8px;">${amount["shipping"]}</td>
                                </tr>
                                <tr>
                                    <td align="left" style="padding: 8px;">Tax (20%)</td>
                                    <td align="right" style="padding: 8px;">${amount["tax"]}</td>
                                </tr>
                                <tr>
                                    <td align="left" style="padding: 8px;"><strong>Total</strong></td>
                                    <td align="right" style="padding: 8px;"><strong>${amount["total_amount"]}</strong></td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 20px;">
                            <a href="http://localhost:5050/confirm_rent/{data["client_id"]}/{data['car_id']}" style="background-color: #28a745; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Confirm Rent</a>
                        </td>

                    </tr>
                </table>
            </td>
        </tr>
    </table>

    </body>
    </html>
    """


def client_email_confirm(data):
    car = Car.get_car_by_id(data)
    amount = calculate_price(data)
    days = (datetime.strptime(data["dropoff_date"], "%Y-%m-%d") -
            datetime.strptime(data["pickup_date"], "%Y-%m-%d")).days
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CarTrade Invoice</title>
    </head>
    <body style="font-family: Arial, sans-serif; color: #322d28; background-color: #f4f4f4; margin: 0; padding: 0;">

    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f4f4f4; padding: 20px;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border: 1px solid #dddddd; padding: 20px;">
                    <tr>
                        <td align="center" style="padding: 10px 0 20px 0;">
                            <img src="http://www.travelerie.com/wp-content/uploads/2014/04/PlaceholderLogoBlue.jpg" alt="CarTrade" style="display: block; width: 200px;"/>
                        </td>
                    </tr>
                    <tr>
                        <td align="left" style="font-size: 16px; padding: 20px;">
                            <h2 style="color: #1779ba; font-size: 24px;">Reservation Confirmation</h2>
                            <p>Hello, {data["first_name"]} {data["last_name"]},</p>
                            <p>Thank you for your order! We are currently awaiting your confirmation.</p>
                            <p>If you have any questions or need assistance, please contact our support team at <strong>+355 685741795</strong>.</p>
                        </td>
                    </tr>
                    <tr>
                        <td align="left">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
                                <thead>
                                    <tr>
                                        <th align="left" style="border-bottom: 1px solid #dddddd; padding: 8px;">Item Description</th>
                                        <th align="center" style="border-bottom: 1px solid #dddddd; padding: 8px;">Item ID</th>
                                        <th align="center" style="border-bottom: 1px solid #dddddd; padding: 8px;">Days</th>
                                        <th align="right" style="border-bottom: 1px solid #dddddd; padding: 8px;">Amount</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td style="padding: 8px; border-bottom: 1px solid #dddddd;">{car["brand"]} {car["model"]} {car["year"]}</td>
                                        <td align="center" style="padding: 8px; border-bottom: 1px solid #dddddd;">{data["car_id"]}</td>
                                        <td align="center" style="padding: 8px; border-bottom: 1px solid #dddddd;">{days}</td>
                                        <td align="right" style="padding: 8px; border-bottom: 1px solid #dddddd;">${amount["total_amount"]}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" style="padding: 20px;">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                    <td align="left" style="padding: 8px;">Subtotal</td>
                                    <td align="right" style="padding: 8px;">${amount["subtotal"]}</td>
                                </tr>
                                <tr>
                                    <td align="left" style="padding: 8px;">Shipping & Handling</td>
                                    <td align="right" style="padding: 8px;">${amount["shipping"]}</td>
                                </tr>
                                <tr>
                                    <td align="left" style="padding: 8px;">Tax (20%)</td>
                                    <td align="right" style="padding: 8px;">${amount["tax"]}</td>
                                </tr>
                                <tr>
                                    <td align="left" style="padding: 8px;"><strong>Total</strong></td>
                                    <td align="right" style="padding: 8px;"><strong>${amount["total_amount"]}</strong></td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 20px;">
                            <p>If you have any concerns or need help, don't hesitate to contact our support at <strong><a href="tel:+355685741795">0685741795</a></strong>.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>

    </body>
    </html>
    """


def confirmation_email(data):
    payment = Payment.get_payment_by_id(data)
    car = Car.get_car_by_id({"car_id": payment["car_id"]})
    rent = Rent.get_rent_by_id({"car_id": payment["car_id"]})
    client = Client.get_client_by_id({"client_id": payment["client_id"]})
    days = (rent["dropoff_date"] - rent["pickup_date"]).days
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CarTrade Payment Confirmation</title>
    </head>
    <body style="font-family: Arial, sans-serif; color: #322d28; background-color: #f4f4f4; margin: 0; padding: 0;">

    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f4f4f4; padding: 20px;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border: 1px solid #dddddd; padding: 20px;">
                    <tr>
                        <td align="center" style="padding: 10px 0 20px 0;">
                            <img src="http://www.travelerie.com/wp-content/uploads/2014/04/PlaceholderLogoBlue.jpg" alt="CarTrade" style="display: block; width: 200px;"/>
                        </td>
                    </tr>
                    <tr>
                        <td align="left" style="font-size: 16px; padding: 20px;">
                            <h2 style="color: #1779ba; font-size: 24px;">Payment Confirmation</h2>
                            <p>Hello, {client["first_name"]} {client["last_name"]},</p>
                            <p>Thank you for your payment! Your reservation has been confirmed.</p>
                        </td>
                    </tr>
                    <tr>
                        <td align="left">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
                                <thead>
                                    <tr>
                                        <th align="left" style="border-bottom: 1px solid #dddddd; padding: 8px;">Item Description</th>
                                        <th align="center" style="border-bottom: 1px solid #dddddd; padding: 8px;">Item ID</th>
                                        <th align="center" style="border-bottom: 1px solid #dddddd; padding: 8px;">Days</th>
                                        <th align="right" style="border-bottom: 1px solid #dddddd; padding: 8px;">Amount</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td style="padding: 8px; border-bottom: 1px solid #dddddd;">{car["brand"]} {car["model"]} {car["year"]}</td>
                                        <td align="center" style="padding: 8px; border-bottom: 1px solid #dddddd;">{car["car_id"]}</td>
                                        <td align="center" style="padding: 8px; border-bottom: 1px solid #dddddd;">{days}</td>
                                        <td align="right" style="padding: 8px; border-bottom: 1px solid #dddddd;">${payment["amount"]}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 20px;">
                            <p>If you have any questions or need assistance, please contact our support team at <strong>+355 685741795</strong>.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>

    </body>
    </html>
    """


def cancellation_email(data):
    payment = Payment.get_payment_by_id(data)
    car = Car.get_car_by_id({"car_id": payment["car_id"]})
    rent = Rent.get_rent_by_id({"car_id": payment["car_id"]})
    client = Client.get_client_by_id({"client_id": payment["client_id"]})
    days = (rent["dropoff_date"] - rent["pickup_date"]).days

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CarTrade Reservation Cancellation</title>
    </head>
    <body style="font-family: Arial, sans-serif; color: #322d28; background-color: #f4f4f4; margin: 0; padding: 0;">

    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f4f4f4; padding: 20px;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border: 1px solid #dddddd; padding: 20px;">
                    <tr>
                        <td align="center" style="padding: 10px 0 20px 0;">
                            <img src="http://www.travelerie.com/wp-content/uploads/2014/04/PlaceholderLogoBlue.jpg" alt="CarTrade" style="display: block; width: 200px;"/>
                        </td>
                    </tr>
                    <tr>
                        <td align="left" style="font-size: 16px; padding: 20px;">
                            <h2 style="color: #e74c3c; font-size: 24px;">Reservation Cancellation</h2>
                            <p>Hello, {client["first_name"]} {client["last_name"]},</p>
                            <p>We regret to inform you that your reservation for the following vehicle has been canceled.</p>
                        </td>
                    </tr>
                    <tr>
                        <td align="left">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
                                <thead>
                                    <tr>
                                        <th align="left" style="border-bottom: 1px solid #dddddd; padding: 8px;">Item Description</th>
                                        <th align="center" style="border-bottom: 1px solid #dddddd; padding: 8px;">Item ID</th>
                                        <th align="center" style="border-bottom: 1px solid #dddddd; padding: 8px;">Days</th>
                                        <th align="right" style="border-bottom: 1px solid #dddddd; padding: 8px;">Amount</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td style="padding: 8px; border-bottom: 1px solid #dddddd;">{car["brand"]} {car["model"]} {car["year"]}</td>
                                        <td align="center" style="padding: 8px; border-bottom: 1px solid #dddddd;">{car["car_id"]}</td>
                                        <td align="center" style="padding: 8px; border-bottom: 1px solid #dddddd;">{days}</td>
                                        <td align="right" style="padding: 8px; border-bottom: 1px solid #dddddd;">${payment["amount"]}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 20px;">
                            <p>If you have any questions or need further assistance, please contact our support team at <strong>+355 685741795</strong>.</p>
                            <p>We hope to assist you again in the future.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>

    </body>
    </html>
    """


def suggest_email(data):
    payment = Payment.get_payment_by_id(data)
    car = Car.get_car_by_id({"car_id": payment["car_id"]})
    client = Client.get_client_by_id({"client_id": payment["client_id"]})
    data = {
        "car_id": car["car_id"],
        "user_id": car["user_id"],
    }
    # Try to get a similar car (if available)
    suggested_car = Car.get_similar_price_car(car["rent_price"],data)
    if len(suggested_car) > 0:
        # If a similar car is found
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>CarTrade Reservation Update</title>
        </head>
        <body style="font-family: Arial, sans-serif; color: #322d28; background-color: #f4f4f4; margin: 0; padding: 0;">

        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f4f4f4; padding: 20px;">
            <tr>
                <td align="center">
                    <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border: 1px solid #dddddd; padding: 20px;">
                        <tr>
                            <td align="center" style="padding: 10px 0 20px 0;">
                                <img src="http://www.travelerie.com/wp-content/uploads/2014/04/PlaceholderLogoBlue.jpg" alt="CarTrade" style="display: block; width: 200px;"/>
                            </td>
                        </tr>
                        <tr>
                            <td align="left" style="font-size: 16px; padding: 20px;">
                                <h2 style="color: #e67e22; font-size: 24px;">Car Unavailability Notice</h2>
                                <p>Hello, {client["first_name"]} {client["last_name"]},</p>
                                <p>We regret to inform you that the car you wanted to book, <strong>{car["brand"]} {car["model"]} {car["year"]}</strong>, is currently unavailable.</p>
                                <p>However, we are pleased to offer you a similar vehicle: <strong>{suggested_car["brand"]} {suggested_car["model"]} {suggested_car["year"]}</strong>, which is available at a comparable price.</p>
                            </td>
                        </tr>
                        <tr>
                            <td align="left">
                                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
                                    <thead>
                                        <tr>
                                            <th align="left" style="border-bottom: 1px solid #dddddd; padding: 8px;">Suggested Car</th>
                                            <th align="center" style="border-bottom: 1px solid #dddddd; padding: 8px;">Car ID</th>
                                            <th align="right" style="border-bottom: 1px solid #dddddd; padding: 8px;">Price per day</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td style="padding: 8px; border-bottom: 1px solid #dddddd;">{suggested_car["brand"]} {suggested_car["model"]} {suggested_car["year"]}</td>
                                            <td align="center" style="padding: 8px; border-bottom: 1px solid #dddddd;">{suggested_car["car_id"]}</td>
                                            <td align="right" style="padding: 8px; border-bottom: 1px solid #dddddd;">${suggested_car["rent_price"]}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td align="center" style="padding: 20px;">
                                <p>If this alternative suits your needs, please contact our support team to proceed with the reservation.</p>
                                <p>You can reach us at <strong>+355 685741795</strong>.</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>

        </body>
        </html>
        """
    else:
        # If no similar car is found
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>CarTrade Reservation Update</title>
        </head>
        <body style="font-family: Arial, sans-serif; color: #322d28; background-color: #f4f4f4; margin: 0; padding: 0;">

        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f4f4f4; padding: 20px;">
            <tr>
                <td align="center">
                    <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border: 1px solid #dddddd; padding: 20px;">
                        <tr>
                            <td align="center" style="padding: 10px 0 20px 0;">
                                <img src="http://www.travelerie.com/wp-content/uploads/2014/04/PlaceholderLogoBlue.jpg" alt="CarTrade" style="display: block; width: 200px;"/>
                            </td>
                        </tr>
                        <tr>
                            <td align="left" style="font-size: 16px; padding: 20px;">
                                <h2 style="color: #e67e22; font-size: 24px;">Car Unavailability Notice</h2>
                                <p>Hello, {client["first_name"]} {client["last_name"]},</p>
                                <p>We regret to inform you that the car you wanted to book, <strong>{car["brand"]} {car["model"]} {car["year"]}</strong>, is currently unavailable.</p>
                                <p>At the moment, we don’t have a similar vehicle to offer. However, we encourage you to explore other available cars on our platform. We are confident you will find the perfect option for your needs.</p>
                            </td>
                        </tr>
                        <tr>
                            <td align="center" style="padding: 20px;">
                                <p>If you need assistance or would like to browse our available vehicles, please visit our website or contact our support team at <strong>+355 685741795</strong>.</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>

        </body>
        </html>
        """


def password_email(email, password):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CarTrade Account Created</title>
    </head>
    <body style="font-family: Arial, sans-serif; color: #322d28; background-color: #f4f4f4; margin: 0; padding: 0;">

    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f4f4f4; padding: 20px;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border: 1px solid #dddddd; padding: 20px;">
                    <tr>
                        <td align="center" style="padding: 10px 0 20px 0;">
                            <img src="http://www.travelerie.com/wp-content/uploads/2014/04/PlaceholderLogoBlue.jpg" alt="CarTrade" style="display: block; width: 200px;"/>
                        </td>
                    </tr>
                    <tr>
                        <td align="left" style="font-size: 16px; padding: 20px;">
                            <h2 style="color: #1779ba; font-size: 24px;">Account Creation Confirmation</h2>
                            <p>Hello,</p>
                            <p>We are pleased to inform you that your account on CarTrade has been successfully created.</p>
                            <p>Your login credentials are as follows:</p>
                            <ul>
                                <li><strong>Email:</strong> {email}</li>
                                <li><strong>Password:</strong> {password}</li>
                            </ul>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 20px;">
                            <p>If you have any questions or need assistance, please contact our support team at <strong>+355 685741795</strong>.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>

    </body>
    </html>
    """
