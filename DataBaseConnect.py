import mysql.connector
import PasswdEncrypterAndValidation
import re

def checkEmail(entry_var2):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, entry_var2):
        print("Valid Email")
        return True

    else:
        print("Invalid Email")
        return False

def checkUserName(entry_var3):
    if len(entry_var3) <5:
        return False, "Nick jest za krótki"
    elif any(char ==' ' for char in entry_var3):
        return False, "Nick nie może zawierać spacji"
    elif len(entry_var3)>20:
        return False, "Nick nie może być dłuższy niż 20 znaków"
    else:
        return True, "Nick jest poprawny"


def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gra3"
        )
        return mydb
    except mysql.connector.Error as err:
        print("Error connecting to DB " + err.msg)
        return


def addUser(nick: str, email: str, passwd: str):
    global message
    if not checkEmail(email):
        print("Invalid Email")
        message = "Niepoprawny Email"
        return False, message

    isPasswordStrongOrNotStrongThatIsTheQuestion, message2 = PasswdEncrypterAndValidation.validation_password(passwd)
    if not isPasswordStrongOrNotStrongThatIsTheQuestion:
        print("Invalid Password")
        return False, message2

    isNickOkOrNotOkThatIsTheQuestion, message3 = checkUserName(nick)
    if not isNickOkOrNotOkThatIsTheQuestion:
        print("Invalid Password")
        return False, message3

    mydb = connect_to_db()
    mycursor = mydb.cursor()

    try:
        sql = "INSERT INTO usermain (UserNickName, UserEmail, UserPassword) VALUES (%s, %s, %s)"
        print("Parametry" + email + PasswdEncrypterAndValidation.encrypt_password(passwd))
        mycursor.execute(sql, (nick, email, PasswdEncrypterAndValidation.encrypt_password(passwd)))
        mydb.commit()
    except mysql.connector.Error as err:
        if err.msg.__contains__("UserNickName"):
            print("Użytkownik o podanym nicku już istnieje")
            message = "This nickname already exist"
            return False, message
        elif err.msg.__contains__("UserEmail"):
            print("UserEmail already exist")
            message = "Podany email już istnieje w bazie"
            return False, message
        else:
            print(err)
            message = "Something went wrong"
            return False, message

    mydb.commit()
    sql3 = "INSERT INTO userinventory (UserID) VALUES (LAST_INSERT_ID())"
    mycursor.execute(sql3)
    mydb.commit()
    mycursor.close()
    message = "Everything went well"
    return True, message


def loginUser(email: str, passwd: str):
    global message
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT count(*) as records FROM usermain WHERE UserEmail=%s AND UserPassword=%s"
    mycursor.execute(sql, (email, PasswdEncrypterAndValidation.encrypt_password(passwd)))
    myresult = mycursor.fetchone()[0]
    if myresult == 0:
        sql = "Select count(*) from usermain WHERE UserEmail=%s"
        mycursor.execute(sql, (email,))
        if mycursor.fetchone()[0] == 0:
            print("Nie ma takiego użytkownika!")
            message = "Nie ma takiego użytkownika!"
            return False, message
        else:
            print("Niepoprawne Hasło!")
            message = "Niepoprawne Hasło!"
            return False, message
    else:
        print("Logged in")
        message = "Logged in"
        return True, message


def shopList():
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT ProductName, MoneyPrice, WoodPrice, StonePrice, IronPrice, DiamondsPrice  FROM `store` "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mycursor.close()
    return myresult
