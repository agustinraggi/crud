import mysql.connector

bd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='universidad',
    charset='latin1'
)

micursor = bd.cursor()
micursor.execute("SELECT * FROM curso")
miresultado = micursor.fetchall()

for x in miresultado:
    print(x)
