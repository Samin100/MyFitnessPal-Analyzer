from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
from myfitnesspal import Client
import os
from datetime import date, timedelta
import Nutrition
from pprint import pprint

# config stuff
app = Flask(__name__)
app.secret_key = os.urandom(24)
client = MongoClient()
db = client.GainStats.users


@app.route('/')
def index():
    if 'username' in session:
        print('Active session')
        return redirect('/app')
    else:
        return render_template('index.html')


@app.route('/app')
def load_app():
    if 'username' in session:
        # smart_load()
        return render_template('app.html')

    else:
        return redirect('/')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    Route for the login page. Will validate credentials on POST, and redirect to / on GET. If credentials are valid
    user will get redirected to /app and if invalid redirected to /.
    :return: A redirect to / or app
    """

    if request.method == 'GET':  # if they navigate to /login they get redirected to /
        return redirect('/')
    else:
        print(request.form)
        inputted_username = request.form['username']
        inputted_password = request.form['password']

        try:  # validate login - look for a better way to test if login is valid
            mfp_client = Client(username=inputted_username, password=inputted_password)

        except ValueError:  # invalid login
            print('invalid login')
            return redirect('/')

        print('valid login')
        existing_user = db.find_one({'username': inputted_username})

        if existing_user is None:  # initializes user - full user initialization will take place in this block
            db.insert({"username": inputted_username, 'password': inputted_password, 'valid_value': 1000})
            print('Created the user: ' + db.find_one({'username': inputted_username}))
        else:
            print(inputted_username + ' already exists in the database.')

            if existing_user['password'] != inputted_password:  # updating their password if it's changed
                db.update_one({'username': inputted_username},
                              {'$set': {'password': inputted_password}})

        session['username'] = inputted_username  #adding their username to the session
        print(session)
        return redirect('/app')


@app.route('/logout')
def logout():
    """
    Logs out a user.
    :return: Redirect to /
    """
    if 'username' in session:
        session.pop('username')

    return redirect('/')


def initial_load():
    """
    Loads the past 61 days of data into the user's database document. If a day already exists then it will be overwritten.
    This should only be ran on creation of the user's database object (their initial login).
    :return: None
    """

    db_user = db.find_one({'username': session['username']})  # pulls session user from the database
    print(db_user)

    mfp_client = Client(username=session['username'], password=db_user['password'])  # creates a MFP client from the database credentials
    nutrition_user = Nutrition.User(mfp_client)  # creates a Nutrition User with the MFP client

    today = date.today()
    end = date.today() - timedelta(days=61)  # remember to change this to 61 after testing

    while today >= end:
        db.update_one({'username': session.get('username')}, {'$set': {('data.' + str(end)): nutrition_user.get_day(end)}})
        print('Added ' + str(end) + ' to ' + db_user['username'] + ' meal database.')
        end += timedelta(days=1)


def smart_load():
    """
    Loops through the past 61 days in the user's database, and if a day is missing then it will get added, otherwise no
    action will be taken. This should be run on every login to ensure the most recent data is loaded.
    :return: None
    """

    today = date.today()
    end = date.today() - timedelta(days=1)  # remember to change this to 61 after development
    db_user = db.find_one({'username': session['username']})  # links to the current user's database
    mfp_client = Client(username=session['username'], password=db_user['password'])  # creates a MFP client from the database credentials
    nutrition_user = Nutrition.User(mfp_client)  # creates a Nutrition User with the MFP client

    while today >= end:

        try: # see if a day exists in the database
            day = db_user['data'][str(end)]
            print(str(end) + ' is loaded.')

        except KeyError:  # if the day has not been loaded
            print(str(end) + ' is missing - updating now...')
            db.update_one({'username': session.get('username')},
                          {'$set': {('data.' + str(end)): nutrition_user.get_day(end)}})

        end += timedelta(days=1)  # increment the day


@app.route('/vdv', methods=['POST', 'GET'])
def set_valid_value():
    print('VDV')
    if request.method == 'GET':
        return redirect('/')
    else:
        print(request.form)
        return redirect('/app')
        db.update_one({'username': session['username']},
                      {'$set': {'valid_value': int(request.form['valid_value'])}})


@app.route('/database')
def database():
    """
    Renders database.html with a list of users in the database. Used as a templating test.
    :return: renders database.html
    """

    cursor = db.find()
    db_users = []

    for document in cursor:
        db_users.append(document['username'])

    return render_template('database.html', users=db_users)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

