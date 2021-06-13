import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

Future<void> createSensor(data) async {
  print(data);

  final response = await http.post(
    Uri.parse('http://192.168.1.201:5000/sensors/create-sensor'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    // Fix Sensor data
    body: jsonEncode(SensorData.fromJson(data)),
  );

  if (response.statusCode == 200) {
    // Navigate to list
    return null;
  } else {
    throw Exception('Failed to create a sensor');
  }
}

class SensorData {
  final String name;
  final String unit;
  final String unitDescription;
  final String location;
  final String locationDescription;

  SensorData({
    required this.name,
    required this.unit,
    required this.unitDescription,
    required this.location,
    required this.locationDescription,
  });

  factory SensorData.fromJson(dynamic data) {
    return SensorData(
      name: data['name'],
      unit: data['unit'],
      unitDescription: data['unitDescription'],
      location: data['location'],
      locationDescription: data['locationDescription'],
    );
  }
}

class SensorsForm extends StatefulWidget {
  const SensorsForm({Key? key}) : super(key: key);

  @override
  SensorsFormState createState() => SensorsFormState();
}

class SensorsFormState extends State<SensorsForm> {
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    final sensorNameController = TextEditingController();
    final sensorUnitController = TextEditingController();
    final sensorUnitDescriptionController = TextEditingController();
    final sensorLocationController = TextEditingController();
    final sensorLocationDescriptionController = TextEditingController();

    return Scaffold(
        appBar: AppBar(
          title: const Text('Sensors Manager'),
        ),
        body: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: TextFormField(
                    controller: sensorNameController,
                    decoration: const InputDecoration(
                      labelText: 'Sensor Name',
                    ),
                  )),
              Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: TextFormField(
                    controller: sensorUnitController,
                    decoration: const InputDecoration(
                      labelText: 'Sensor Unit',
                    ),
                  )),
              Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: TextFormField(
                    controller: sensorUnitDescriptionController,
                    decoration: const InputDecoration(
                      labelText: 'Sensor Unit Description',
                    ),
                  )),
              Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: TextFormField(
                    controller: sensorLocationController,
                    decoration: const InputDecoration(
                      labelText: 'Sensor Location',
                    ),
                  )),
              Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: TextFormField(
                    controller: sensorLocationDescriptionController,
                    decoration: const InputDecoration(
                      labelText: 'Sensor Location Description',
                    ),
                  )),
              Padding(
                padding: const EdgeInsets.all(20.0),
                child: ElevatedButton(
                  onPressed: () {
                    createSensor({
                      sensorNameController.text,
                      sensorUnitController.text,
                      sensorUnitDescriptionController.text,
                      sensorLocationController.text,
                      sensorLocationDescriptionController.text
                    });
                  },
                  child: const Text('Submit'),
                ),
              ),
            ],
          ),
        ));
  }
}
