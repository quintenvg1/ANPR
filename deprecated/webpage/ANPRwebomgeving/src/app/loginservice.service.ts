import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginserviceService{

  loggedin:Boolean = false;
  nummerplaat_allcaps:String = "";
  
  login = (username:string, password:string) =>{
    //check database for existing credentials
  }

  submitplate = (nummerplaat:string) =>{
    this.nummerplaat_allcaps = nummerplaat.toLocaleUpperCase();
    console.log(this.nummerplaat_allcaps);
    //set the input in allcaps
  }


  constructor() { }
}
