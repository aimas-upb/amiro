import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BlindsComponent } from './blinds/blinds.component';
import { SensehatComponent } from './sensehat/sensehat.component';
import { LightsComponent } from './lights/lights.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { PepperComponent } from './pepper/pepper.component';

@NgModule({
  declarations: [
    AppComponent,
    BlindsComponent,
    SensehatComponent,
    LightsComponent,
    PepperComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    AppRoutingModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
