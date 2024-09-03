import re
from flask_app.models.car import Car

def process_message(msg):
    msg = msg.lower()

    # Dictionary of common phrases and responses
    responses = {
        'hello': '[Pafi 🐣]=> Hello! How can I help you today?',
        'goodbye': '[Pafi 🐣]=> Goodbye! Have a great day!',
        'search': '[Pafi 🐣]=> What would you like to search for?',
        'hi': '[Pafi 🐣]=> Hi! How can I help you today?',
        'price': '[Pafi 🐣]=> What is your budget?',
        'year': '[Pafi 🐣]=> What year are you looking for?',
        'brand': '[Pafi 🐣]=> What brand are you looking for?',
        'style': '[Pafi 🐣]=> What style are you looking for?',
        'condition': '[Pafi 🐣]=> What condition are you looking for?',
        'model': '[Pafi 🐣]=> What model are you looking for?',
        'km': '[Pafi 🐣]=> How many kilometers are you looking for?',
        'thanks': '[Pafi 🐣]=> You are welcome! Is there anything else for today?',
        'help': '[Pafi 🐣]=> I can help you find cars based on price, year, brand, style, condition, model, km, and description. What would you like to search for?',
        'please': '[Pafi 🐣]=> Please provide more details.',
        'pleasure': '[Pafi 🐣]=> The pleasure is mine! How can I help you today?',
        'name': '[Pafi 🐣]=> My name is Pafi. How can I help you today?',
        'car': '[Pafi   🐣]=> What car would you like to search for?',
        'test drive': '[Pafi 🐣]=> Ready for a test drive? I can help schedule it at a time that works for you.',
        'new or used': '[Pafi 🐣]=> Are you looking for a new or used car?',

        
    }

    # Check for price-related queries
    price_match = re.search(r'\bprice\s+(\d+)\b', msg)
    if price_match:
        price = int(price_match.group(1))
        count = Car.count_cars_by_price(price)
        return f'[Pafi 🐣]=> We have {count} car(s) available over ${price}.'

    # Check for year-related queries
    year_match = re.search(r'\byear\s+(\d{4})\b', msg)
    if year_match:
        year = int(year_match.group(1))
        count = Car.count_cars_by_year(year)
        return f'[Pafi 🐣]=> We have {count} car(s) from the year {year}.'

    # Check for brand-related queries
    brand_match = re.search(r'\bbrand\s+(\w+)\b', msg)
    if brand_match:
        brand = brand_match.group(1).capitalize()
        count = Car.count_cars_by_brand(brand)
        return f'[Pafi 🐣]=> We have {count} car(s) of the brand {brand}.'

    # Check for style-related queries
    style_match = re.search(r'\bstyle\s+(\w+)\b', msg)
    if style_match:
        style = style_match.group(1).capitalize()
        count = Car.count_cars_by_style(style)
        return f'[Pafi 🐣]=> We have {count} car(s) of the style {style}.'

    # Check for condition-related queries
    condition_match = re.search(r'\bcondition\s+(\w+)\b', msg)
    if condition_match:
        condition = condition_match.group(1).capitalize()
        count = Car.count_cars_by_condition(condition)
        return f'[Pafi 🐣]=> We have {count} car(s) in {condition} condition.'

    # Check for model-related queries
    model_match = re.search(r'\bmodel\s+(\w+)\b', msg)
    if model_match:
        model = model_match.group(1).capitalize()
        count = Car.count_cars_by_model(model)
        return f'[Pafi 🐣]=> We have {count} car(s) of the model {model}.'

    # Check for km-related queries
    km_match = re.search(r'\bkm\s+(\d+)\b', msg)
    if km_match:
        km = int(km_match.group(1))
        count = Car.count_cars_by_km(km)
        return f'[Pafi 🐣]=> We have {count} car(s) with approximately {km} km.'

    # Check for description-related queries
    description_match = re.search(r'\bdescription\s+(.+)\b', msg)
    if description_match:
        description = description_match.group(1)
        count = Car.count_cars_by_description(description)
        return f'[Pafi 🐣]=> We have {count} car(s) matching the description: {description}.'

    # Check for other responses
    for key, response in responses.items():
        if key in msg:
            return response

    # Default response if no match found
    return "[Pafi 🐣]=> I'm not sure how to respond to that. Can you please provide more details?"
