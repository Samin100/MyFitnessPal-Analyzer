from flask import Flask, render_template, redirect, request, session, abort, flash, jsonify, sessions, redirect
import os
import Nutrition
import myfitnesspal
from datetime import date, timedelta
import time

app = Flask(__name__)


# home page
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('home.html')
    else:
        return login


# login information
@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        start = time.time()
        print('login attempt')

        try:
            nutrient = request.form['nutrient']
            client = myfitnesspal.Client(username=request.form['username'], password=request.form['password'])
            user = Nutrition.User(client)
            session['logged_in'] = True

            context_dict = {'nutrient': nutrient,
                            'days': request.form['days'],
                            'value': user.calculate_average_daily(request.form['nutrient'],date.today(), date.today()-timedelta(days=int(request.form['days']))),
                            'meals': user.get_meals(date.today()),
                            }

            end = time.time()
            load_time = round(end-start, 3)
            context_dict['load_time'] = load_time
            return render_template('home.html', context=context_dict)  # pass the context as a dict

        except ValueError:
            print('Login failed.')

        return home()

    return home()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


@app.route('/favicon.ico')
def favicon():
    return 'static/img/favicon.ico'

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='127.0.0.1', port=8000, debug=True)
