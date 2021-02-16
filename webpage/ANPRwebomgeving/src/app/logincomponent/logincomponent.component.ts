import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-logincomponent',
  templateUrl: './logincomponent.component.html',
  styleUrls: ['./logincomponent.component.css']
})
export class LogincomponentComponent implements OnInit {

  constructor() { }
  agreed:boolean = false;
  loggedin:boolean = false;
  username:string = "";
  password:string = "";
  licenseplate:string = "";
  //ngmodel binds up here

  flipag = () =>{
    this.agreed = !this.agreed;
  }

  login = () =>{
    this.loggedin = !this.loggedin;
  }

  ngOnInit(): void {
  }

}
