import { Component, OnInit } from '@angular/core';
import { NONE_TYPE } from '@angular/compiler/src/output/output_ast';
@Component({
  selector: 'app-blinds',
  templateUrl: './blinds.component.html',
  styleUrls: ['./blinds.component.css']
})
export class BlindsComponent implements OnInit {
  sideBlinds = {name : 'Side', enabled: true};
  frontBlinds = {name : 'Front', enabled: true};
  rosnode = null;

  stop(idx)
  {
    console.log("Stopped " + idx);
  }
  
  raise(idx)
  {
    console.log("Raised " + idx);
  }

  lower(idx)
  {
    console.log("Lowered " + idx);
  }

  constructor() { 
    try{
      
      //this.rosnode.initNode('/blinds_node');
    }
    catch(err)
    {
      console.log(err);
    }
  }

  ngOnInit() {
  }

}
