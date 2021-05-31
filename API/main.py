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
    if request.method == 'POST' and request.form['submit_button'] == 'Submit':
        # Open database connection
        connection = sqlite3.connect("TP2.db")
        cursor = connection.cursor()

        # Access received data from the url
        name = request.form.get('name')
        unit = request.form.get('unit')

        # Adds a new sensor
        cursor.execute('INSERT INTO Sensor (idSensor, idLocation, name, unit) VALUES (?,?,?,?)',
                       (None, None, name, unit))

        # Save (commit) the changes
        connection.commit()
        # We can also close the connection if we are done with it
        # Just be sure any changes have been committed or they will be lost.
        connection.close()

        return 'Sensor created successfully'
    elif request.method == 'GET':
        return render_template('sensor.html')


@app.route('/sensors', methods=['GET'])
def listSensor():
    # Open database connection
    connection = sqlite3.connect("TP2.db")
    cursor = connection.cursor()

    # list sensors
    cursor.execute('SELECT * FROM Sensor')
    sensorsList = cursor.fetchall()

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

    return sensorsList


if __name__ == '__main__':
    app.run(debug=True)
