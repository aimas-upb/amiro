import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';

@Component({
  selector: 'app-pepper',
  templateUrl: './pepper.component.html',
  styleUrls: ['./pepper.component.css']
})
export class PepperComponent implements OnInit {
  public currentTextCommand = "";
  public pepper = {enabled: true};

  sendTextCommand(pepper){
    if('topic' in pepper)
    {
      console.log("Sending " + this.currentTextCommand);
      pepper.topic.publish(this.currentTextCommand);
      this.currentTextCommand = "";
    }
  }

  constructor() { 
    this.pepper['topic'] = AppComponent.get_topic({
      ros : AppComponent.ros,
      name : '/commands_text',
      messageType : 'std_msgs/String'
    });
  }

  ngOnInit() {
  }

}
