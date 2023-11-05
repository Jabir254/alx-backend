#!/usr/bin/env python3
'''render templates'''

from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def index():
    '''render index.html from templates folder'''
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)