import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "quinten",
    password = "quintenvg1",
    database = "ANPR"
    )

class Database_handler:#all the functions the database will need
    #setup of nescesary variables
    global mydb
    
    def get_all_users(self):
        cursor = mydb.cursor()
        query = "select * from gratiekapel"
        cursor.execute(query)
        a = ""
        for x in cursor:
            a += str(x)
        print(a)
            
    
    def add_user(locatie, naam, nummerplaat, startdatum, einddatum, pincode):
        cursor = mydb.cursor()
        query = "insert into " + locatie + " (naam, pincode, nummerplaat, Startdatum, EindDatum, actief) VALUES ("+"'"+naam+"',"+pincode+",'"+nummerplaat+"',"+"'"+StartDatum+"',"+"'"+EindDatum+"',"+ actief+";"
    #end-add_user
#end-class-Database_handler