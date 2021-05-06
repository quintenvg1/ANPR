import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "quinten",
    password = "quintenvg1",
    database = "anpr",
    auth_plugin = 'mysql_native_password', #for newer versions of mysql server (i just moved to desktop pc on april 4th 2021)
    )

class Database_handler:#all the functions the database will need
    #setup of nescesary variables
    global mydb

    
    def get_all_users(self, locatie):
        cursor = mydb.cursor()
        query = "select * from "+str(locatie)
        cursor.execute(query)
        a = ""
        for x in cursor:
            a += str(x)
        print(a)
    #end-get_all_users
    
    def add_user(locatie, naam, nummerplaat, startdatum, einddatum, pincode):
        actief = "0"
        cursor = mydb.cursor()
        #query = "insert into " + locatie + " (naam, pincode, nummerplaat, Startdatum, EindDatum, actief) VALUES ("+"'"+naam+"','"+str(pincode)+"','"+nummerplaat+"',"+"'"+startdatum+"',"+"'"+einddatum+"',"+ str(actief)+";"
        query = "insert into " + str(locatie) + " (naam, pincode, nummerplaat, Startdatum, EindDatum, actief) values (" + "'"+naam+"'," + "'"+str(pincode)+"',"+"'"+nummerplaat+"',"+"'"+startdatum+"',"+"'"+einddatum+"',"+"'"+actief+"');"
        cursor.execute(query)
        mydb.commit()
    #end-add_user
    
    def remove_user(locatie, naam = "", nummerplaat = ""): #remove by either plate or name
        cursor = mydb.cursor()
        query = ""
        if(naam != ""):
            query = "delete from " + locatie + " where naam = " + "'"+naam+"';"
        if(nummerplaat != ""):
            query = "delete from " + locatie + " where nummerplaat = " + "'"+nummerplaat+"';"
        cursor.execute(query)
        mydb.commit()
        print(query)
        
#end-class-Database_handler