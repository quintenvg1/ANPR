import { Component, OnInit } from '@angular/core';
import { LoginserviceService } from '../loginservice.service';

@Component({
  selector: 'app-removeplate',
  templateUrl: './removeplate.component.html',
  styleUrls: ['./removeplate.component.css']
})
export class RemoveplateComponent implements OnInit {

  constructor(private service:LoginserviceService) { }

  remove = (nummerplaat:string = "") =>{
    if(this.service.loggedin == true){
      //search database for the numberplate, then delete the plate
    }else{
      alert("u bent niet ingelogd");
    }
  }

  ngOnInit(): void {
  }

}
