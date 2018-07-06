#coding:utf-8
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
mongoClient = MongoClient('mongodb://localhost:27017')
database = mongoClient['flask']

@app.route("/")
def nain():
    return "<p>Hello World</p>"

if __name__ == '__main__':
    app.run()