import "reflect-metadata";
import {createConnection} from "typeorm";
import {user} from "./entity/User";

createConnection().then(async connection => {
/*
    console.log("Inserting a new user into the database...");
    const _user = new user();
    _user.naam = "john appleseed";
    _user.paswoord = "paswoord123";
    _user.nummerplaat = "1-123-ABC";
    await connection.manager.save(user);
    console.log("Saved a new user with id: " + _user.ID);

    console.log("Loading users from the database...");*/
    const users = await connection.manager.find(user);
    console.log("Loaded users: ", users);

    console.log("Here you can setup and run express/koa/any other framework.");

}).catch(error => console.log(error));
