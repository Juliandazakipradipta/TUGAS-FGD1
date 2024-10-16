from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=3000, debug=True)
