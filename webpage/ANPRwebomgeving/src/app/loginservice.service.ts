import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginserviceService{

  loggedin:Boolean = false;
  nummerplaat_allcaps:string = "";
  
  login1 = (username:string, password:string) =>{
    //check database for existing credentials
  }

  submitplate = (nummerplaat:string) =>{
    this.nummerplaat_allcaps = nummerplaat.toLocaleUpperCase();
    console.log(this.nummerplaat_allcaps);
    //set the input in allcaps
  }

  constructor() { }
}
