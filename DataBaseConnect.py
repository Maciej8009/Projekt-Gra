import mysql.connector
import PasswdEncrypterAndValidation
import re
import tkinter

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
            host="db",
            user="root",
            password="password",
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
            mycursor.close()
            mydb.close()
            return False, message, None, None
        else:
            print("Niepoprawne Hasło!")
            message = "Niepoprawne Hasło!"
            mycursor.close()
            mydb.close()
            return False, message, None, None
    else:
        print("Logged in")
        message = "Logged in"
        sql = "Select userID, userNickName from usermain WHERE UserEmail=%s"
        mycursor.execute(sql, (email, ))
        myresult = mycursor.fetchone()
        userID = myresult[0]
        userNickName = myresult[1]
        mycursor.close()
        mydb.close()
        return True, message, userID, userNickName


def shopList():
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT ProductName, MoneyPrice, WoodPrice, StonePrice, IronPrice, DiamondsPrice, ProductID  FROM `store` "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    print(myresult)
    return myresult


def buy(id: int, userID: int):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT MoneyPrice, WoodPrice, StonePrice, IronPrice, DiamondsPrice, ProductName FROM store WHERE ProductID=%s"
    mycursor.execute(sql, (id, ))
    myresult = mycursor.fetchone()
    print(myresult)
    MoneyPrice = myresult[0]
    WoodPrice = myresult[1]
    StonePrice = myresult[2]
    IronPrice = myresult[3]
    DiamondsPrice = myresult[4]
    ProductName = myresult[5]
    sql2 = "SELECT Money, Wood, Stone, Iron, Diamonds FROM userinventory WHERE UserID=%s"
    mycursor.execute(sql2, (userID, ))
    myresult2 = mycursor.fetchone()
    print(myresult2)
    UserMoney = myresult2[0]
    UserWood = myresult2[1]
    UserStone = myresult2[2]
    UserIron = myresult2[3]
    UserDiamonds = myresult2[4]
    if (MoneyPrice > UserMoney) or (WoodPrice > UserWood) or (StonePrice > UserStone) or (IronPrice > UserIron) or (DiamondsPrice > UserDiamonds):
        print("Warunek spełniony")
        return False

    UserMoney = UserMoney - MoneyPrice
    UserWood = UserWood - WoodPrice
    UserStone = UserStone - StonePrice
    UserIron = UserIron - IronPrice
    UserDiamonds = UserDiamonds - DiamondsPrice
    if ProductName == 'Axe':
        sql3 = "UPDATE userinventory set Money=%s, Wood=%s, Stone=%s, Iron=%s, Diamonds=%s, Axe=1 WHERE UserID = %s"
    elif ProductName == 'Pickaxe':
        sql3 = "UPDATE userinventory set Money=%s, Wood=%s, Stone=%s, Iron=%s, Diamonds=%s, Pickaxe=1 WHERE UserID = %s"
    elif ProductName == 'Better Pickaxe':
        sql3 = "UPDATE userinventory set Money=%s, Wood=%s, Stone=%s, Iron=%s, Diamonds=%s, `Better Pickaxe`=1 WHERE UserID = %s"
    elif ProductName == 'Drill':
        sql3 = "UPDATE userinventory set Money=%s, Wood=%s, Stone=%s, Iron=%s, Diamonds=%s, Drill=1 WHERE UserID = %s"
    else:
        return False
    mycursor.execute(sql3, (UserMoney, UserWood, UserStone, UserIron, UserDiamonds, userID))
    mydb.commit()
    mycursor.close()
    mydb.close()
    return True

def alreadyBought(ProductID, userID):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    if ProductID == 0:
        sql = "SELECT Axe FROM userinventory WHERE UserID = %s"
    elif ProductID == 1:
        sql = "SELECT Pickaxe FROM userinventory WHERE UserID = %s"
    elif ProductID == 2:
        sql = "SELECT `Better Pickaxe` FROM userinventory WHERE UserID = %s"
    elif ProductID == 3:
        sql = "SELECT Drill FROM userinventory WHERE UserID = %s"
    else:
        return False, "error"

    mycursor.execute(sql, (userID, ))
    myresult = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    if myresult[0] == 1:
        return False, "Już posiadasz ten item!"
    else:
        return True, ""


def getUserScores():
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT userNickName, UserScore FROM usermain ORDER BY UserScore DESC LIMIT 5"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return myresult


def getUserEQ(userID):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT Money, Wood, Stone, Iron, Diamonds FROM userinventory WHERE UserID = %s"
    mycursor.execute(sql, (userID, ))
    myresult = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return myresult


def updateUserScore(userID, score):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT UserScore FROM usermain WHERE UserID = %s"
    mycursor.execute(sql, (userID, ))
    myresult = mycursor.fetchone()
    newscore = myresult[0] + score
    print(newscore)
    sql = "UPDATE usermain SET UserScore = %s WHERE UserID = %s"
    try:
        mycursor.execute(sql, (newscore, userID))
        mydb.commit()
    except mydb.IntegrityError:
        print("Error updating")
    mycursor.close()
    mydb.close()


def updateMoney(userID, value):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT Money FROM userinventory WHERE UserID = %s"
    mycursor.execute(sql, (userID, ))
    myresult = mycursor.fetchone()
    newValue = myresult[0] + value
    print(newValue)
    sql = "UPDATE userinventory SET Money = %s WHERE UserID = %s"
    try:
        mycursor.execute(sql, (newValue, userID))
        mydb.commit()
    except mydb.IntegrityError:
        print("Error updating")
    mydb.commit()
    mycursor.close()
    mydb.close()

def updateWood(userID, value):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT Wood FROM userinventory WHERE UserID = %s"
    mycursor.execute(sql, (userID, ))
    myresult = mycursor.fetchone()
    newValue = myresult[0] + value
    print(newValue)
    sql = "UPDATE userinventory SET Wood = %s WHERE UserID = %s"
    try:
        mycursor.execute(sql, (newValue, userID))
        mydb.commit()
    except mydb.IntegrityError:
        print("Error updating")
    mycursor.close()
    mydb.close()


def updateStone(userID, value):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT Stone FROM userinventory WHERE UserID = %s"
    mycursor.execute(sql, (userID, ))
    myresult = mycursor.fetchone()
    newValue = myresult[0] + value
    print(newValue)
    sql = "UPDATE userinventory SET Stone = %s WHERE UserID = %s"
    try:
        mycursor.execute(sql, (newValue, userID))
        mydb.commit()
    except mydb.IntegrityError:
        print("Error updating")
    mycursor.close()
    mydb.close()


def updateIron(userID, value):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT Iron FROM userinventory WHERE UserID = %s"
    mycursor.execute(sql, (userID, ))
    myresult = mycursor.fetchone()
    newValue = myresult[0] + value
    print(newValue)
    sql = "UPDATE userinventory SET Iron = %s WHERE UserID = %s"
    try:
        mycursor.execute(sql, (newValue, userID))
        mydb.commit()
    except mydb.IntegrityError:
        print("Error updating")
    mycursor.close()
    mydb.close()


def updateDiamonds(userID, value):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT Diamonds FROM userinventory WHERE UserID = %s"
    mycursor.execute(sql, (userID, ))
    myresult = mycursor.fetchone()
    newValue = myresult[0] + value
    print(newValue)
    sql = "UPDATE userinventory SET Diamonds = %s WHERE UserID = %s"
    try:
        mycursor.execute(sql, (newValue, userID))
        mydb.commit()
    except mydb.IntegrityError:
        print("Error updating")
    mycursor.close()
    mydb.close()


def checkIfUserHaveAxe(userID):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT Axe FROM userinventory WHERE UserID = %s"
    mycursor.execute(sql, (userID, ))
    myresult = mycursor.fetchone()
    newValue = myresult[0]
    if newValue == 0:
        mycursor.close()
        mydb.close()
        return False
    else:
        mycursor.close()
        mydb.close()
        return True

