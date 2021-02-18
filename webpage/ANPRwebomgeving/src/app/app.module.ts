import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LogincomponentComponent } from './logincomponent/logincomponent.component';
import {FormsModule}   from '@angular/forms';
import { RemoveplateComponent } from './removeplate/removeplate.component';

@NgModule({
  declarations: [
    AppComponent,
    LogincomponentComponent,
    RemoveplateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
