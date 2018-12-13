import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';

@Component({
  selector: 'app-pepper',
  templateUrl: './pepper.component.html',
  styleUrls: ['./pepper.component.css']
})
export class PepperComponent implements OnInit {
  public avaliableLanguages = ['ro-RO', 'en-EN'];
  public currentTextCommand = "";
  public pepper = {enabled: true, selectedLanguage:'ro-RO'};


  sendTextCommand(pepper){
    if('topic' in pepper)
    {
      var stringPayload = JSON.stringify(
      {
        'text': this.currentTextCommand,
        'error': "",
        'language': pepper.selectedLanguage
      });
      console.log(stringPayload);

      var payload = {data: stringPayload};
      pepper.topic.publish(payload);
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
