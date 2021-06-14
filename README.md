# Sensors Manager

### 1. Implement a RESTful web service

Build an API/RESTful web service, where each entity can be CREATED, READ, UPDATED, and/or DELETED with standard HTTP verbs (POST, GET, PUT/PATCH, and DELETE). 
The database can enhanced with other tables. Furthermore, at your choice, you can use MongoDB instead of a relational database.  
To referred implementation should be made in [Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing).

### 2. Web Application
Build a small and simple website to show the acquired data about sensors, their location, etc. Besides showing data, some statistical features about data should be presented (think on using Pandas to achieve it). Use some map API to show your sensors location over time.  
The referred implementation should be made in [Flask Jinja](https://flask.palletsprojects.com/en/2.0.x/tutorial/templates/).

### 3. Mobile Application

Implement a mobile app which will send to your web service data from at least one your mobile’s sensors.  
To achieve this you can use [Flutter](https://flutter.dev/).

# Running the application

In the API folder:
```
set FLASK_APP=main.py
```

```
set FLASK_ENV=development
```

```
flask run
```

```
flask run --host=0.0.0.0
```
