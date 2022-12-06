from app import app
from flask import render_template

user_data = { # Mock User table
    'dylans': {
        'user_id': 1,
        'email': 'dylans@gmail.com',
        'name': 'Dylan Smith',
        'favorite_color': 'Purple',
        'is_active': True,
        'reviews': ['Dylan is a great dev!', 'He\'s the best']
    },
    'jdoe': {
        'user_id': 2,
        'email': 'johndoe@gmail.com',
        'name': 'John Doe',
        'favorite_color': 'Purple',
        'is_active': True,
        'reviews': ['John failed me', 'John is the best!']
    },
    'jenm': {
        'user_id': 3,
        'email': 'jenm@yahoo.com',
        'name': 'Jen Max',
        'favorite_color': 'Blue',
        'is_active': False,
        'reviews': ['Jen did the job well.']
    }
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<username>')
def display_profile(username):
    return render_template('profile.html.j2', **user_data[username])
    
# Functions/Endpoints:
# Get all users and their data
# Get all user emails
# Get a user by their username
# Get a user by their email
# Find all users with a specified favorite color

@app.route('/api/users')
def get_users():
    return user_data

@app.route('/api/users/emails')
def get_user_emails():
    emails = []

    for user in user_data.values():
        emails.append(user['email'])

    return emails

# Write an endpoint, similar to the previous one
# that returns a list of active user's names.

@app.route('/api/user/<username>')
def get_user_by_username(username):
    if username in user_data:
        return user_data[username]

    return f'User with username {username} not found'

@app.route('/api/user/email/<email>')
def get_user_by_email(email):
    for user in user_data.values():
        if user['email'] == email:
            return user

    return f'User with email {email} not found.'

@app.route('/api/users/color/<favorite_color>')
def get_users_by_color(favorite_color):
    users = []

    for user in user_data.values():
        if user['favorite_color'].lower() == favorite_color.lower():
            users.append(user)

    return users

@app.route('/api/users/<username>/reviews/<review_idx>')
def get_user_review(username, review_idx):
    return user_data[username]['reviews'][int(review_idx)]

car_data = {
    0: {
        "name": "Maruti Swift Dzire VDI",
        "year": 2014,
        "selling_price": 450000
    },
    1: {
        "name": "Skoda Rapid 1.5 TDI Ambition",
        "year": 2014,
        "selling_price": 370000
    },
    2: {
        "name": "Honda City 2017-2020 EXi",
        "year": 2006,
        "selling_price": 158000
    }
}

# Create 2 routes/templates:
# - Display all cars using a for loop and their information (not dynamic)
# - Display a specific car and it's information (Will be dynamic, you can use the car's ID in the car_data dict)

# Get all cars
@app.route('/api/cars')
def get_cars():
    return car_data


# Get cars in a dictionary separated by year, for example:
car_year_result = {
    2014: ["Maruti Swift Dzire VDI","Skoda Rapid 1.5 TDI Ambition"],
    2006: ["Honda City 2017-2020 EXi"]
}

@app.route('/api/cars/years')
def get_car_by_years():
    result = {}

    for car in car_data.values():
        if car['year'] in result:
            result[car['year']].append(car['name'])

        else:
            result[car['year']] = [car['name']]

    return result

# Get a car by it's ID (it's ID is just the key in the car data dictionary)
@app.route('/api/car/<id>')
def get_car(id): # /api/car/1 => '1'
    id = int(id)
    if id in car_data:
        return car_data[id]

    return f'Car with id {id} does not exist.'

# Get all cars below a given price point, so if the user enters 380000, you'd show the second and third cars
@app.route('/api/car/price/<price>')
def get_cars_below_price(price):
    result = []

    price = int(price)

    for car in car_data.values():
        if car['selling_price'] < price:
            result.append(car)

    return result
