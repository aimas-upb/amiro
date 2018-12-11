import { Component } from '@angular/core';

declare var ROSLIB: any;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'AMIRO';
  public static ros_lib = ROSLIB;
  public static ros = new ROSLIB.Ros({
    url : 'ws://192.168.0.158:9090'
  });
  public static ros_connected = false;


  constructor() { 
    this.initROS();
  }

  public static get_topic(topic_info)
  {
    return new ROSLIB.Topic(topic_info);
  }

  public static get_message(message_info)
  {
    return new ROSLIB.Message(message_info);
  }

  initROS()
  {
     // Connecting to ROS
    // -----------------
    AppComponent.ros.on('connection', function() {
      console.log('Connected to websocket server.');
      AppComponent.ros_connected = true;
    });
  
    AppComponent.ros.on('error', function(error) {
      console.log('Error connecting to websocket server: ', error);
      AppComponent.ros_connected = false;
    });
  
    AppComponent.ros.on('close', function() {
      console.log('ROS Unavaliable');
      AppComponent.ros_connected = false;
    });
  }
}
