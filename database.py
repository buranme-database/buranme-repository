import psycopg2 as db

url  = "dbname='jobApplicationDatabase' user='postgres' host='localhost' password='4041'"

def create_tables():
    with open("db.sql","r") as sql:
        temp = sql.readlines()
    tmp = ""
    for i in temp:
        statement += i +" "
    print(tmp)
    
    connection = db.connect(url)
    cursor = connection.cursor()
    cursor.execute(tmp)
    connection.commit()
    cursor.close()
    connection.close()