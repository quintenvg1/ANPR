import { Injectable } from '@angular/core';
import {HttpClient, HttpClientModule} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class DatabaseserviceService {
  url:String = "localhost:8080/";
  user:any;

  constructor(private client: HttpClient) { 
    
  }

  getuser = (naam:string, paswoord:string) =>{
    //code to list users from the database
    this.user = this.client.request("GET", + this.url + "/user/" + naam); //attempt to get a user by name
    return(this.user);
  }

  createuser = (naam:String, paswoord:String, nummerplaat:String) =>{
    //code to create a user
  }

  deleteuser = (naam:String, paswoord:String) =>{
    //code to delete user in the database
  }

  edituser = (naam:String, paswoord:String, nieuwe_naam:String, nieuw_paswoord:String, nieuwe_nummerplaat:String) =>{
    //code to change a user in the database
  }
}
