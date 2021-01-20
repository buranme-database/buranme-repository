import os
import sys
import json
import psycopg2 as dbapi2


url  = "user='postgres' dbname='jobApplicationDatabase' host='localhost' password='4041'"


def student_signup(password,username,name):
    flag=False
    id=0
    connection = dbapi2.connect(url)
    cursor = connection.cursor()
    statement = """INSERT INTO public."Student"(
	"Password", "Username", "Name")
	VALUES ('{}', '{}', '{}') RETURNING "ID";""".format(password,username,name)
    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        connection.commit()
        id = int(id[0])
        flag=True
    except Exception as err:
        if (err.pgcode == "23505"):
            print("this email is already in use")
            id=-1
            flag=False
    finally:
        cursor.close()
        connection.close()
    return (flag,id)

def company_signup(password,username,name):
    flag=False
    id=0
    connection = dbapi2.connect(url)
    cursor = connection.cursor()
    statement = """INSERT INTO public."Company"(
	"Password", "Username", "Name")
	VALUES ('{}', '{}', '{}') RETURNING "ID";""".format(password,username,name)
    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        connection.commit()
        id = int(id[0])
        flag=True
    except Exception as err:
        if (err.pgcode == "23505"):
            print("this email is already in use")
            id=-1
            flag=False
    finally:
        cursor.close()
        connection.close()
    return (flag,id)

def student_login(username,password):
    connection = dbapi2.connect(url)
    cursor = connection.cursor()
    statement = """SELECT "ID" FROM public."Student" where "Username" = '{}' and "Password"='{}';""".format(username,password)

    cursor.execute(statement)
    result = cursor.fetchone()
    if result:
        return (True,int(result[0]))
    
    statement = """SELECT "ID" FROM public."Student" where "Username" = '{}' ;""".format(username)
    if result:
        print('wrong password')
        return (False,int(result[0]))
    print("user doesn't exist")
    return(False,-1)

def company_login(username,password):
    connection = dbapi2.connect(url)
    cursor = connection.cursor()
    statement = """SELECT "ID" FROM public."Company" where "Username" = '{}' and "Password"='{}';""".format(username,password)
    cursor.execute(statement)
    result = cursor.fetchone()
    if result:
        return (True,int(result[0]))
    statement = """SELECT "ID" FROM public."Company" where "Username" = '{}' ;""".format(username)
    if result:
        print('wrong password')
        return (False,int(result[0]))
    print("Company doesn't exist")
    return(False,-1)

def add_advert(company_id, name):
    connection = dbapi2.connect(url)
    cursor = connection.cursor()
    statement = """INSERT INTO public."Advert" ("Company ID","Name")
    VALUES ( '{}','{}') RETURNING "ID";""".format(company_id, name)
    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        id = id[0]
        connection.commit()
        flag=True
        cursor.close()
        connection.close()
        return (flag,id)
    except Exception as err:
        print_psycopg2_exception(err)
        flag=False
        cursor.close()
        connection.close()
        return (flag,-1)
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
