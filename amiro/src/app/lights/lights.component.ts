import { Component, OnInit } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-lights',
  templateUrl: './lights.component.html',
  styleUrls: ['./lights.component.css']
})
export class LightsComponent implements OnInit {
  light_url = 'https://192.168.0.160/api/1RwesaHuMDdr7DSsr9Z29UxOVAt-w697ioR9ipsD/lights';
  light = {state : false, 
          brightness: 0,
          hue: 0,
          saturation: 0};
  get_light_state()
  {
    return this.http.get(this.light_url);
  }

  constructor(private http: HttpClient) { 
    var light1 = this.get_light_state();
    console.log(light1);
    this.light = {
      state : light1['state']['on'].toBool(),
      brightness: light1['state']['bri'].toInt(),
      hue: 0,
      saturation: 0
    };
  }

  ngOnInit() {
  }

}
