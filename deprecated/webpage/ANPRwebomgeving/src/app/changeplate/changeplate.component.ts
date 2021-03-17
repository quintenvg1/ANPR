import { Component, OnInit } from '@angular/core';
import { LoginserviceService } from '../loginservice.service';

@Component({
  selector: 'app-changeplate',
  templateUrl: './changeplate.component.html',
  styleUrls: ['./changeplate.component.css']
})
export class ChangeplateComponent implements OnInit {

  constructor(private service:LoginserviceService) { }

  oldplate:string = "";
  newplate:string = "";

  changeplate = () =>{
    if(this.service.loggedin == true){

    }else{
      alert("je bent niet ingelogd");
    }
  }

  ngOnInit(): void {
  }

}
