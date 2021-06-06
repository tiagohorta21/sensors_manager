from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def homeScreen():
    sensorsList = [list(sensor) for sensor in listSensor()]
    for sensor in sensorsList:
        location = getLocation(sensor[1])
        sensor[1] = location[1]
    return render_template('home.html', sensors=sensorsList)


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


@app.route('/sensors/<id>', methods=['GET'])
def getSensor(id):
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    cursor = connection.cursor()

    # List sensors
    cursor.execute('SELECT * FROM Sensor WHERE idSensor=?', (id,))
    sensor = cursor.fetchone()

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return sensor


@app.route('/sensors/create-sensor', methods=['GET', 'POST'])
def createSensor():
    if request.method == 'POST' and request.form['submit_button'] == 'Submit':
        # Open database connection
        connection = sqlite3.connect("TP2.db")
        cursor = connection.cursor()

        # Access received data from the form
        name = request.form.get('name')
        unit = request.form.get('unit')
        unit_description = request.form.get('unit_description')
        location = request.form.get('location')
        location_description = request.form.get('location_description')

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

        # Access received data from the form
        name = request.form.get('name')
        unit = request.form.get('unit')
        unit_description = request.form.get('unit_description')
        location = request.form.get('location')
        location_description = request.form.get('location_description')

        # Get sensor data to get the current sensor unit
        sensor = getSensor(id)

        # Update unit by unit
        cursor.execute('UPDATE Unit SET unit=?, description=? WHERE unit=?',
                       (unit, unit_description, sensor[3]))

        # Update location by id
        cursor.execute('UPDATE Location SET name=?, description=? WHERE idLocation=?',
                       (location, location_description, sensor[1]))

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
        sensor = getSensor(id)
        unit = getUnit(sensor[3])
        location = getLocation(sensor[1])

        return render_template('sensor.html', sensorName=sensor[2], sensorUnit=sensor[3], sensorUnitDescription=unit[1],
                               sensorLocation=location[1], sensorLocationDescription=location[2])


@app.route('/unit/<unit>', methods=['GET'])
def getUnit(unit):
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    cursor = connection.cursor()

    # Get a specific unit by unit
    cursor.execute('SELECT * FROM Unit WHERE unit=?', (unit,))
    unit = cursor.fetchone()

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return unit


@app.route('/location/<id>', methods=['GET'])
def getLocation(id):
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    cursor = connection.cursor()

    # Get a specific location by id
    cursor.execute('SELECT * FROM Location WHERE idLocation=?', (id,))
    location = cursor.fetchone()

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return location


if __name__ == '__main__':
    app.run(debug=True)
