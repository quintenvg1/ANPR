import { Component, OnInit } from '@angular/core';
import { DatabaseserviceService } from '../databaseservice.service';

@Component({
  selector: 'app-createaccount',
  templateUrl: './createaccount.component.html',
  styleUrls: ['./createaccount.component.css']
})
export class CreateaccountComponent implements OnInit {

  constructor(private dbservice:DatabaseserviceService) { }
  naam:String = "";
  password:String = "";
  nummerplaat:String = "";


  createaccount = () =>{
    this.dbservice.createuser(this.naam, this.password, this.nummerplaat);
  }

  ngOnInit(): void {
  }

}
