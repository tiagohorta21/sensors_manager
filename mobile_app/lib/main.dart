import 'package:flutter/material.dart';
import 'package:mobile_app/sensorsList.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sensors Manager',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: SensorsList(),
    );
  }
}
