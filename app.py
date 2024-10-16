from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('mongodb+srv://test:sparta1@project0.wvnom.mongodb.net/')
db = client.zaki

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    pesan_receive = request.form['pesan_give']
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    doc = {
        'name': name,
        'email': email,
        'message': message,
        'pesan' : pesan_receive
    }
    db.pesan.insert_one(doc) 
    return jsonify({'msg': 'Saran & Kritik anda sudah masuk ke database saya!'})
if __name__ == '__main__':
    app.run('0.0.0.0', port=3000, debug=True)
