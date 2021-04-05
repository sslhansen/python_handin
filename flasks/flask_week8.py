#!flask/bin/python
from flask import Flask, jsonify, abort, request
import mysql.connector as mysql
app = Flask(__name__)

db = mysql.connect(
    host = "db",
    user = "root",
    passwd = "root",
    db = "db"
)
cur = db.cursor()
@app.route('/api/laptops/all', methods=['GET'])
def get_laptops():
    query = 'select * from week8'
    cur.execute(query)
    myresult = cur.fetchall()
    return jsonify(myresult)

@app.route('/api/laptops', methods=['POST'])
def add_laptop():
    if not request.json or not 'name' in request.json or not 'price' in request.json:
            abort(400)
    laptop = {
        'name': request.json['name'],
        'price': request.json['price']
    }
    query = 'INSERT INTO week8 (name, price) VALUES(%s, %s);'
    cur.execute(query, (laptop.name, request.json['price'],))
    db.commit()
    return jsonify(laptop), 201