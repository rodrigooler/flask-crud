# coding:utf-8
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
mongoClient = MongoClient('mongodb://localhost:27017')
database = mongoClient['flask']


@app.route("/")
def main():
    return {
        "firstName": "Rodrigo",
        "lastName": "Oler",
        "email": "roodrigoprogrammer@gmail.com",
        "github": "@rodrigooler",
    }


if __name__ == '__main__':
    app.run()
