import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BlindsComponent } from './blinds/blinds.component';
import { SensehatComponent } from './sensehat/sensehat.component';
import { LightsComponent } from './lights/lights.component';

@NgModule({
  declarations: [
    AppComponent,
    BlindsComponent,
    SensehatComponent,
    LightsComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
