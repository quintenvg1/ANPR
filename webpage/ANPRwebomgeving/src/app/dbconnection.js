var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "quintenvg1",
  database: "ANPR"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});