import 'package:flutter/material.dart';

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
                  onPressed: () {},
                  child: const Text('Submit'),
                ),
              ),
            ],
          ),
        ));
  }
}
