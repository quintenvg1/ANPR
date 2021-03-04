import { Injectable } from '@angular/core';
import "reflect-metadata";
import {Connection, createConnection} from "typeorm";
import {User} from "../entity/User"; //the entity we will be using to compare database entries with

@Injectable({
  providedIn: 'root'
})
export class DbserviceService {

  //add a user method
  adduser = () =>{

  }
  /*
  createConnection().then(async connection => {

    console.log("Inserting a new user into the database...");
    const user = new User();
    user.naam = "Peter Parkeer";
    user.paswoord = "paswoord123";
    user.nummerplaat = "1-123-ABC";
    await connection.manager.save(user);
    console.log("Saved a new user with id: " + user.id);

    console.log("Loading users from the database...");
    const users = await connection.manager.find(User);
    console.log("Loaded users: ", users);

    console.log("Here you can setup and run express/koa/any other framework.");

}).catch(error => console.log(error));
*/


  constructor() { }
}
