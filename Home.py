from flask import Flask, render_template, redirect, request, session, abort, flash
import os
import Nutrition
import myfitnesspal
from datetime import date, timedelta


app = Flask(__name__)


# home page
@app.route('/')
def home():
    print('home')
    if not session.get('logged_in'):
        return render_template('home.html')
    else:
        return 'Logged in'


# login information
@app.route('/login', methods=['POST'])
def login():
    print('login attempt')

    try:
        print(request.form)
        nutrient = request.form['nutrient']
        print('trying to log in with MFP data')
        client = myfitnesspal.Client(username=request.form['username'], password=request.form['password'])
        user = Nutrition.User(client)
        return str('Your ' + nutrient + ' total: ' + str(user.calculate_average_daily(request.form['nutrient'], date.today(), date.today())))


    except ValueError:
        print('error')

    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/favicon.ico')
def favicon():
    return 'static/img/favicon.ico'

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='127.0.0.1', port=8000, debug=True)
