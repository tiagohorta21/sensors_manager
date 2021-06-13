import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:mobile_app/sensorsForm.dart';
import 'package:http/http.dart' as http;

Future<List<Sensor>> fetchSensors() async {
  final response =
      await http.get(Uri.parse('http://192.168.1.201:5000/sensors'));

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    List data = json.decode(response.body);
    return data.map((sensor) => Sensor.fromJson(sensor)).toList();
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load sensors');
  }
}

class Sensor {
  final int id;
  final String location;
  final String name;
  final String unit;

  Sensor({
    required this.id,
    required this.location,
    required this.name,
    required this.unit,
  });

  factory Sensor.fromJson(dynamic json) {
    return Sensor(
      id: json['idSensor'],
      location: json['location'],
      name: json['name'],
      unit: json['unit'],
    );
  }
}

class SensorsList extends StatefulWidget {
  const SensorsList({Key? key}) : super(key: key);

  @override
  _SensorsListState createState() => _SensorsListState();
}

class _SensorsListState extends State<SensorsList> {
  late Future<List<Sensor>> sensor;

  @override
  void initState() {
    super.initState();
    sensor = fetchSensors();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Sensors Manager'),
        ),
        body: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            Padding(
                padding: const EdgeInsets.all(20.0),
                child: ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => const SensorsForm()));
                  },
                  child: const Text('Create Sensor'),
                )),
            Expanded(
              child: FutureBuilder<List<Sensor>>(
                future: sensor,
                builder: (context, snapshot) {
                  if (snapshot.hasData) {
                    return DataTable(
                        columns: [
                          const DataColumn(label: Text('Name')),
                          const DataColumn(label: Text('Unit')),
                          const DataColumn(label: Text('Location'))
                        ],
                        rows: snapshot.data!
                            .map((sensor) => DataRow(cells: [
                                  DataCell(Text(sensor.name)),
                                  DataCell(Text(sensor.unit)),
                                  DataCell(Text(sensor.location)),
                                ]))
                            .toList());
                  } else if (snapshot.hasError) {
                    return Text("${snapshot.error}");
                  }
                  // By default, show a loading spinner.
                  return const CircularProgressIndicator();
                },
              ),
            ),
          ],
        ));
  }
}
