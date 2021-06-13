import 'package:flutter/material.dart';

class SensorsForm extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Sensors Manager'),
      ),
      body: Container(
        child: Center(
          child: Text('Sensors Form',
              style: TextStyle(fontSize: 30.0, fontWeight: FontWeight.bold)),
        ),
      ),
    );
  }
}
