#workings of the maintnance script
#1 get current date, 2 update set active where startdatum = current date, 3 delete from location where einddatum = currentdate
#warning this script is supposed to run continiously or the system might keep outdated entries which will have to be removed manually later
import mysql.connector
import datetime
import time
locations = ("gratiekapel", "middelheim", "agora")

def maintnance():
    currentdate = datetime.datetime.now()
    day = str(currentdate)
    print(day[0:10])
    currentdate = day[0:10]
    mydb = mysql.connector.connect(
        user = "quinten",
        password = "quintenvg1",
        port=3306,
        database="ANPR",
        host="localhost"
        )

    cursor = mydb.cursor()
    for location in locations:
        query = ("update "+str(location)+" set actief 1 where startDatum = "+"'"+str(currentdate)+"';") #activeer entries
        print(query)
    for location in locations:
        query = ("delete from "+str(location)+ " where EindDatum = "+"'"+str(currentdate)+"';") # delete gedeactiveerde accounts
        print(query)
    print("performed maintnance")
#endmaintnance

while True:
    maintnance()
    time.sleep(30) #wait 5 minutes
#endwhile
