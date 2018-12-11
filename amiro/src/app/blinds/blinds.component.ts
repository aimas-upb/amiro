import { Component, OnInit } from '@angular/core';
import { NONE_TYPE } from '@angular/compiler/src/output/output_ast';
import { AppComponent } from '../app.component';

declare var ros: any;

@Component({
  selector: 'app-blinds',
  templateUrl: './blinds.component.html',
  styleUrls: ['./blinds.component.css']
})
export class BlindsComponent implements OnInit {
  sideBlinds = {name : 'Side', enabled: true};
  frontBlinds = {name : 'Front', enabled: true};
  rosnode = null;

  stop(blinds)
  {
    if('topic' in blinds)
    {
      console.log("Stopped ");
      blinds.topic.publish({data: 0});
    }
  }
  
  raise(blinds)
  {
    console.log("Raised " + blinds);
    blinds.topic.publish({data: 1});
  }

  lower(blinds)
  {
    console.log("Lowered " + blinds);
    blinds.topic.publish({data: -1});
  }

  constructor() { 
    try{
      this.sideBlinds['topic'] = AppComponent.get_topic({
        ros : AppComponent.ros,
        name : '/blinds_1',
        messageType : 'std_msgs/Int32'
      });
      this.frontBlinds['topic'] = AppComponent.get_topic({
        ros : AppComponent.ros,
        name : '/blinds_2',
        messageType : 'std_msgs/Int32'
      });
    }
    catch(err)
    {
    }
  }

  ngOnInit() {
  }

}
