from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient()
db = client.GainStatsPulledData


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/app')
def load_app():
    return render_template('app.html')







if __name__ == '__main__':
    app.run(debug=True)