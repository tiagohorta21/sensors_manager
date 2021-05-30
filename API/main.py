from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
