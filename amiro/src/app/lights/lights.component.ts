import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';

@Component({
  selector: 'app-lights',
  templateUrl: './lights.component.html',
  styleUrls: ['./lights.component.css']
})
export class LightsComponent implements OnInit {
  public light = {type:'phillips_hue', enabled: true};

  public colors = [{value:'Red', selected: false},
                    {value:'Blue', selected: false},
                    {value:'Green', selected: false},
                    {value:'Orange', selected: false},
                    {value:'White', selected: false},
                    {value:'Purple', selected: false},
                    {value:'Pink', selected: false},
                    {value:'Cyan', selected: false}];
  public selectedColor = this.colors[0];
                    
  get_light_state()
  {
    
  }

  oncolorchanged(color)
  {
    console.log(color);
    this.selectedColor = color;
  }

  set_brightness(val, light)
  {
    var payload = {data: JSON.stringify({'brightness': val})};
    light.topic.publish(payload);
  }

  set_color(val, light)
  {
    console.log(val);
    console.log(this.selectedColor);
    var payload = {data: JSON.stringify({'color': val.value.toLowerCase()})};
    light.topic.publish(payload);
  }

  set_power(on, light)
  {
    if('topic' in light)
    {
      var payload = {data : ""};
      if(on)
      {
        payload = {data: JSON.stringify({'power': "on"})};
      }
      else{
        payload = {data: JSON.stringify({'power': 'off'})};
      }
      light.topic.publish(payload);
      
    }
  }

  constructor() { 
    this.light['topic'] = AppComponent.get_topic({
      ros : AppComponent.ros,
      name : '/lights_1',
      messageType : 'std_msgs/String'
    });
  }

  ngOnInit() {
  }

}
