from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)


@app.route('/sensors/create-sensor', methods=['GET', 'POST'])
def createSensor():
    # Open database connection
    connection = sqlite3.connect("../TP2.db")
    cursor = connection.cursor()

    # Access received data

    # name = request.form['name']
    # location = request.form['location']
    # unit = request.form['unit']
    sensor = "sensor1"
    # Adds a new sensor
    cursor.execute("INSERT INTO Unit (description) VALUES (?,?)", (None, sensor))

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return 'Hello, World'
