import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BlindsComponent } from './blinds/blinds.component';
import { SensehatComponent } from './sensehat/sensehat.component';

@NgModule({
  declarations: [
    AppComponent,
    BlindsComponent,
    SensehatComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
