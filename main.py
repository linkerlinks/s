import json

from flask import Flask
from flask import request

app = Flask(__name__)

from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
