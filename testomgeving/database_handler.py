#!/ust/bin/python3
import mysql.connector # connect to database
import time # delay bruteforce attacks
import _thread as thread

mydb1 = mysql.connector.connect(
    host="localhost",
    user="quinten", #blur out when pushing on github
    password = "quintenvg1", # blur out when pushing to github
    database="ANPR"
    )

def remove_default_accounts(): # thread 2
    global mydb1 # create a second connection
    cursor = mydb1.cursor()
    query = "delete from user where user.naam = 'nieuwe naam'"
    cursor.execute(query)
    mydb1.commit()
    time.sleep(10) # every 10 seconds default users are removed
    print("removed accidentally created accounts accounts")
#end-remove_default_accounts

def Thread2():
    while True:
        remove_default_accounts
    #endwhile
#end-Thread2

thread.start_new_thread( Thread2, ( ) ) # run the background process

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
            a += x
            print(x)
        return (a)
        #endfor
    #end-getuserfroplate
    
    def getuserfromcredentials(naam, paswoord):
        result = ""
        cursor = mydb.cursor()
        query = "select * from user where naam = "+"'" + naam +"'"+"and paswoord ="+"'" + paswoord + "';"
        cursor.execute(query)
        for x in cursor:
            result += str(x)
        return (result) #return all the stuff
    #end-getuserfromcredentials
    
    def createuser(naam, paswoord, plaat):
        cursor = mydb.cursor()
        if(naam != "" and paswoord != "" and plaat != ""): #check if there are values in the function call
            query = "insert into user (naam, paswoord, nummerplaat) values(" +"'"+ naam +"'" + "," +"'"+ paswoord +"'"+","+"'" + plaat +"'"+ ")"
            print(query)
            #query = "insert into user (naam, paswoord, nummerplaat) values ('John Cena', 'WrathOfTheCenation', '1-121-ABB')"
            cursor.execute(query)
            mydb.commit()
            # backend works
    #end-createuser
    
    def deleteuser(naam, paswoord):
        query = "delete from user where user.naam = " +"'" +naam +"'" +" AND user.paswoord = "+"'"+paswoord+"';"
        cursor = mydb.cursor()
        print(query)
        cursor.execute(query)
        mydb.commit()
    #end-deleteuser
    
    def updateuser(naam, paswoord, nieuwenaam ,nieuwpaswoord, nieuweplaat): #momentarily untested
        #update user set naam = "nieuwenaam", paswoord = "nieuwpaswoord", nummerplaat = "nieuweplaat" where naam = "naam" and paswoord = "paswoord"
        cursor = mydb.cursor()
        query = "update user set naam = "+"'"+nieuwenaam+"',"+" paswoord = "+"'"+nieuwpaswoord+"',"+"nummerplaat = "+"'"+nieuweplaat+"'" + "where naam = " + "'"+naam+"' and paswoord = "+"'"+paswoord+"'"
        print(query)
        cursor.execute(query)
        mydb.commit()
    #end-updateuser
    
    def getUserFromPlate(plaat):
        result = ""
        cursor = mydb.cursor()
        query = "select naam from user where nummerplaat = "+"'"+plaat+"'"
        cursor.execute(query)
        for x in cursor:
            result += str(x)
        return (result)
    #end-getuserfromplate