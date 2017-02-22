from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
import flask_login
from myfitnesspal import Client
import os
from datetime import date, timedelta

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
        return render_template('app.html')
    else:
        return redirect('/')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':  # if they navigate to /login they get redirected to /
        return redirect('/')
    else:
        print(request.form)
        inputted_username = request.form['username']
        inputted_password = request.form['password']

        try:  # valid login
            MFP_client = Client(username=inputted_username, password=inputted_password)

        except ValueError:  # invalid login
            print('invalid login')
            return redirect('/')

        print('valid login')
        existing_user = db.find_one({'username': inputted_username})

        if existing_user is None:  # if user is not in database
            db.insert({"username": inputted_username, 'password': inputted_password})
            print('Created the user: ' + db.find_one({'username': inputted_username}))
        else:
            print(inputted_username + ' already exists in the database.')

        session['username'] = inputted_username
        print(session)
        return redirect('/app')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')


def load_2_months():
    '''
    Loads the past 61 days of data into the user's database. If a day already exists then it will be overwritten.
    :return: None
    '''

    today = date.today()
    end = date.today() - timedelta(days=3)

    while today > end:
        db.update_one({'username': session['username']}, {'$set':{('data.' + end)}})
        end += timedelta(days=1)


def verify_2_months():
    '''
    Checks whether the past 61 days of data have been loaded into the database
    :return: Boolean
    '''


if __name__ == '__main__':
    app.run(debug=True)

