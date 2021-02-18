import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="quinten", #blur out when pushing on github
  password = "quintenvg1", # blur out when pushing to github
  database="ANPR"
)
nummerplaat = "'1-123-ABC'"
cursor = mydb.cursor()
query = "select * from user where nummerplaat = "
query = query + nummerplaat
cursor.execute(query)
for x in cursor:
    print(x)
#endfor