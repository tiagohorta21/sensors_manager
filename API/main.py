from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def homeScreen():
    sensorsList = listSensor()
    return render_template('home.html', sensors=sensorsList)


@app.route('/sensors/create-sensor', methods=['GET', 'POST'])
def createSensor():
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    cursor = connection.cursor()

    # Access received data from the url
    name = request.args.get('name')
    unit = request.args.get('unit')

    # Adds a new sensor
    cursor.execute('INSERT INTO Sensor (idSensor, idLocation, name, unit) VALUES (?,?,?,?)',
                   (None, None, name, unit))

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return 'Sensor created successfully'


@app.route('/sensors', methods=['GET'])
def listSensor():
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    cursor = connection.cursor()

    # List sensors
    cursor.execute('SELECT * FROM Sensor')
    sensorsList = cursor.fetchall()

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return sensorsList


@app.route('/delete/<id>')
def deleteSensor(id):
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    cursor = connection.cursor()

    # Deletes a sensor by id
    cursor.execute("PRAGMA FOREIGN_KEYS = ON")
    cursor.execute('DELETE FROM Sensor WHERE idSensor=?', id)

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return 'Sensor deleted successfully'


if __name__ == '__main__':
    app.run(debug=True)
