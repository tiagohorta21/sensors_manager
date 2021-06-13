from flask import Flask, render_template, request
import sqlite3
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def homeScreen():
    sensorsList = json.loads(listSensor())
    return render_template('home.html', sensors=sensorsList)


@app.route('/sensors', methods=['GET'])
def listSensor():
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # List sensors
    cursor.execute('SELECT Sensor.idSensor, Sensor.unit, Sensor.name, Location.name AS location FROM Sensor,'
                   'Location WHERE Sensor.idLocation=Location.idLocation')
    sensorsList = [dict(row) for row in cursor.fetchall()]

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return json.dumps(sensorsList)


@app.route('/sensors/<id>', methods=['GET'])
def getSensor(id):
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # List sensors
    cursor.execute('SELECT Sensor.idSensor, Sensor.unit, Sensor.name, Location.name AS location, Location.description '
                   'AS locationDescription, Unit.description AS unitDescription FROM Sensor, '
                   'Location, Unit WHERE '
                   'idSensor=? AND Sensor.idLocation=Location.idLocation AND Sensor.unit=Unit.unit', (id,))
    sensor = dict(cursor.fetchone())

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return json.dumps(sensor)


@app.route('/sensors/create-sensor', methods=['GET', 'POST'])
def createSensor():
    if request.method == 'POST':
        # Open database connection
        connection = sqlite3.connect("TP2.db")
        cursor = connection.cursor()

        # Json payload from the POST request
        payload = request.get_json()

        # Access received data from the form
        name = request.form.get('name') or payload['name']
        unit = request.form.get('unit') or payload['unit']
        unit_description = request.form.get('unit_description') or payload['unitDescription']
        location = request.form.get('location') or payload['location']
        location_description = request.form.get('location_description') or payload['locationDescription']

        # Adds unit and unit description to the Unit table
        cursor.execute('INSERT INTO Unit (unit, description) VALUES (?,?)',
                       (unit, unit_description))

        # Adds location and location description to the Location table
        cursor.execute('INSERT INTO Location (idLocation, name, description) VALUES (?,?,?)',
                       (None, location, location_description))
        locationId = cursor.lastrowid

        # Adds a new sensor to the sensor table
        cursor.execute('INSERT INTO Sensor (idSensor, idLocation, name, unit) VALUES (?,?,?,?)',
                       (None, locationId, name, unit))

        # Save (commit) the changes
        connection.commit()
        # We can also close the connection if we are done with it
        # Just be sure any changes have been committed or they will be lost.
        connection.close()

        return homeScreen()
    elif request.method == 'GET':
        return render_template('sensor.html')


@app.route('/sensors/<id>/delete', methods=['GET', 'DELETE'])
def deleteSensor(id):
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    cursor = connection.cursor()

    # Deletes a sensor by id
    cursor.execute("PRAGMA FOREIGN_KEYS = ON")
    cursor.execute('DELETE FROM Sensor WHERE idSensor=?', (id,))

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return homeScreen()


@app.route('/sensors/<id>/update', methods=['GET', 'PUT', 'POST'])
def updateSensor(id):
    if request.method == 'POST' or request.method == 'PUT' and request.form['submit_button'] == 'Submit':
        # Open database connection
        connection = sqlite3.connect("TP2.db")
        cursor = connection.cursor()

        # Json payload from the POST request
        payload = request.get_json()

        # Access received data from the form
        name = request.form.get('name') or payload['name']
        unit = request.form.get('unit') or payload['unit']
        unit_description = request.form.get('unit_description') or payload['unit_description']
        location = request.form.get('location') or payload['location']
        location_description = request.form.get('location_description') or payload['location_description']

        # Get sensor data to get the current sensor unit
        sensor = json.loads(getSensor(id))

        # Update unit by unit
        cursor.execute('UPDATE Unit SET unit=?, description=? WHERE unit=?',
                       (unit, unit_description, sensor['unit']))

        # Update location by id
        cursor.execute('UPDATE Location SET name=?, description=? WHERE idLocation=?',
                       (location, location_description, sensor['location']))

        # Update sensor by id
        cursor.execute('UPDATE Sensor SET name=?, unit=? WHERE idSensor=?',
                       (name, unit, id))

        # Save (commit) the changes
        connection.commit()
        # We can also close the connection if we are done with it
        # Just be sure any changes have been committed or they will be lost.
        connection.close()

        return homeScreen()
    elif request.method == 'GET':
        # Get needed data to fill the form
        sensor = json.loads(getSensor(id))
        return render_template('sensor.html', sensor=sensor)


if __name__ == '__main__':
    app.run(debug=True)
