import mysql.connector


def connect_to_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gra"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM usermain"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def addUser(nick: str, email: str, passwd: str):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gra3"
    )
    if mydb.is_connected():
        print("Connection")
    else:
        print(" NO Connection")
        return

    mycursor = mydb.cursor()

    try:
        sql = "INSERT INTO usermain (UserNickName, UserEmail, UserPassword) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (nick, email, passwd))
        mydb.commit()
    except mysql.connector.Error as err:
        print(err)
        return False

    # sql2 = "INSERT INTO userlogindata (UserID, UserEmail, UserPassword) VALUES (LAST_INSERT_ID(), %s, %s)"
    # mycursor.execute(sql2, (email, passwd))
    mydb.commit()
    sql3 = "INSERT INTO userinventory (UserID) VALUES (LAST_INSERT_ID())"
    mycursor.execute(sql3)
    mydb.commit()
    mycursor.close()
    return True


def loginUser(email: str, passwd: str):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gra3"
    )
    if mydb.is_connected():
        print("Connection")
    else:
        print(" NO Connection")
        return

    mycursor = mydb.cursor()
    sql = "SELECT count(*) as records FROM usermain WHERE UserEmail=%s AND UserPassword=%s"
    mycursor.execute(sql, (email, passwd))
    myresult = mycursor.fetchone()[0]
    if myresult == 0:
        print("No such user")
        return False
    else:
        print("Logged in")
        return True


def shopList():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gra3"
    )
    if mydb.is_connected():
        print("Connection")
    else:
        print(" NO Connection")
        return

    mycursor = mydb.cursor()
    sql = "SELECT ProductName, MoneyPrice, WoodPrice, StonePrice, IronPrice, DiamondsPrice  FROM `store` "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mycursor.close()
    return myresult
