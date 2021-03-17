import { Component, OnInit } from '@angular/core';
import { LoginserviceService } from '../loginservice.service';

@Component({
  selector: 'app-remove-acc',
  templateUrl: './remove-acc.component.html',
  styleUrls: ['./remove-acc.component.css']
})
export class RemoveAccComponent implements OnInit {
  username:string = "";
  password:string = "";

  constructor(private service:LoginserviceService) {

   }

  remove = () =>{
    if(this.service.loggedin == true){

    }else{
      alert("u bent niet ingelogd");
    }
  }
  ngOnInit(): void {
  }

}
