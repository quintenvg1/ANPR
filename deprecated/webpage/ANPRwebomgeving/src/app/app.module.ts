import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LogincomponentComponent } from './logincomponent/logincomponent.component';
import {FormsModule}   from '@angular/forms';
import { RemoveplateComponent } from './removeplate/removeplate.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ChangeplateComponent } from './changeplate/changeplate.component';
import { CreateaccountComponent } from './createaccount/createaccount.component';
import { RemoveAccComponent } from './remove-acc/remove-acc.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginserviceService } from './loginservice.service';
import { DatabaseserviceService } from './databaseservice.service';

@NgModule({
  declarations: [
    AppComponent,
    LogincomponentComponent,
    RemoveplateComponent,
    NavbarComponent,
    ChangeplateComponent,
    CreateaccountComponent,
    RemoveAccComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
