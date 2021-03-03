import mysql.connector
import _thread

class Databasecontroller:
    global mydb
    mydb = mysql.connector.connect(
    host="localhost",
    user="quinten", #blur out when pushing on github
    password = "quintenvg1", # blur out when pushing to github
    database="ANPR"
    )
    gebruikersnaam = ""
    paswoord = ""
    nummerplaat = ""
    #cursor = mydb.cursor()
    def getuserfromplate(plaat):
        cursor = mydb.cursor()
        query = "select * from user where nummerplaat = "
        query = query + "'"+plaat+"'"
        print(query)
        cursor.execute(query)
        for x in cursor:
            print(x)
        #endfor
    #end-getuserfroplate
    
    def createuser(naam, paswoord, plaat):
        cursor = mydb.cursor()
        if(naam != ""):
            query = "insert into user (naam, paswoord, nummerplaat) values(" +"'"+ naam +"'" + "," +"'"+ paswoord +"'"+","+"'" + plaat +"'"+ ")"
            print(query)
            #query = "insert into user (naam, paswoord, nummerplaat) values ('John Cena', 'WrathOfTheCenation', '1-121-ABB')"
            cursor.execute(query)
            mydb.commit()
            # backend works

