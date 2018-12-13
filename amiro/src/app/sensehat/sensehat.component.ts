import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sensehat',
  templateUrl: './sensehat.component.html',
  styleUrls: ['./sensehat.component.css']
})
export class SensehatComponent implements OnInit {
  temperature = {'unit' : 'C', 'value' : 23, 'valid': true};
  humidity = {'unit' : '%%rH', 'value' : 65, 'valid': true};
  pressure =  {'unit' : 'mmHg', 'value' : 760, 'valid': true};
  topic = '';

  constructor() { 
    this.topic = 'environment';
  }

  on_message_received(ros_msg)
  {
    this.on_temperature_message(ros_msg['temperature']);
    this.on_humidity_message(ros_msg['humidity']);
    this.on_pressure_message(ros_msg['pressure']);
  }

  on_temperature_message(temp_msg)
  {
    this.temperature = temp_msg;
    this.temperature.valid = true;
  }

  on_humidity_message(humidity_msg)
  {
    this.humidity = humidity_msg;
    this.humidity.valid = true;
  }

  on_pressure_message(pressure_msg)
  {
    this.pressure = pressure_msg;
    this.pressure.valid = true;
  }

  ngOnInit() {
  }

}
