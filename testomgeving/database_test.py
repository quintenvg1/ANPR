import mysql.connector
import _thread

class Databasecontroller:
  mydb = mysql.connector.connect(
    host="localhost",
    user="quinten", #blur out when pushing on github
    password = "quintenvg1", # blur out when pushing to github
    database="ANPR"
  )
  gebruikersnaam = ""
  paswoord = ""
  nummerplaat = "'1-123-ABC'"
  cursor = mydb.cursor()
  query = "select * from user where nummerplaat = "
  query = query + nummerplaat
  cursor.execute(query)
  for x in cursor:
      print(x)
  #endfor
  query = "insert into user (naam, paswoord, nummerplaat) values ('John Cena', 'WrathOfTheCenation', '1-121-ABB')"
  cursor.execute(query)
  mydb.commit()
  # backend works
controller Databasecontroller()
