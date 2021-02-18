import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginserviceService{

  loggedin:Boolean = false;
  
  login(username:string, password:string){

  }

  constructor() { }
}
