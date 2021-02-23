import { Component, OnInit } from '@angular/core';
import { DatabaseserviceService } from '../databaseservice.service';
import { LoginserviceService } from '../loginservice.service';

@Component({
  selector: 'app-logincomponent',
  templateUrl: './logincomponent.component.html',
  styleUrls: ['./logincomponent.component.css']
})
export class LogincomponentComponent implements OnInit {

  constructor(private dbservice:DatabaseserviceService,private logservice:LoginserviceService) {
    this.loggedin = this.logservice.loggedin;
    console.log(this.loggedin);
  }
  agreed:Boolean = false;
  loggedin:Boolean = false;
  username:String = "";
  password:String = "";
  licenseplate:String = "";
  //ngmodel binds up here

  flipag = () =>{
    this.agreed = !this.agreed;
  }

  login = () =>{
    //this.logservice.loggedin = !this.logservice.loggedin;
    this.logservice.loggedin = true;
    this.loggedin = this.logservice.loggedin;
    console.log(this.loggedin);
  }

  logout = () =>{
    this.logservice.loggedin = false;
    this.loggedin = this.logservice.loggedin;
  }

  ngOnInit(): void {
  }

}
