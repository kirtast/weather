from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import app_test
import db_push_data_test

app = Flask(__name__)
# app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///DB_weather.sqlite'
# db = SQLAlchemy(app)


@app.route("/")
def main_page():

    conn=sqlite3.connect('DB_weather.sqlite')
    cur=conn.cursor()
    cur.execute('SELECT * FROM Daily')
    daily = cur.fetchall()
    cur.execute('SELECT * FROM Hour_Data')
    hours = cur.fetchall()
    cur.close()
    return render_template('home.html', daily = daily, hours = hours)
