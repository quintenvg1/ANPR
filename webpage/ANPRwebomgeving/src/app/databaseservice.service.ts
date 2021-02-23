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
    this.user = this.client.request("GET", + this.url + "/user/" + naam); //attempt to get a user by name
    return(this.user);
  }
}
