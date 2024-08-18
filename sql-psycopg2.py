import psycopg2
#connect to chinook database
connection = psycopg2.connect(database="chinook")
#built a cursor object of the database
cursor = connection.cursor()
#Query 1 - select all records from the ¨Artist¨table
cursor.execute('SELECT * FROM ¨Artist¨')
#Query 2 - select only the ¨name¨column from the ¨artist¨table
cursor.execute('SELECT ¨Name¨FROM ¨Artist¨table' )
#Query 3 - select only Queen from the artist table
cursor.execute('SELECT*FROM ¨Artist¨WHERE ¨name¨=%s'[Queen] )
#fetch the result (multiple)
results = cursor.fetchall()
#fetch the result (single)
result=cursor.fetchOne()
#close the connection
connection.close()
#print result
for result in results:
    print (result)