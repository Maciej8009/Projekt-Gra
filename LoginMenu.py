import os
from tkinter import *


import DataBaseConnect
import MainMenu
import RegisterMenu


def floginMenu():
    def login(email: str, passwd: str):
        print("Kupa" + email + passwd)
        logInOrNotLogInThatIsTheQuestion, message, userID, userNickName = DataBaseConnect.loginUser(email, passwd)
        if logInOrNotLogInThatIsTheQuestion:
            print("Logged in")
            MenuK.destroy()
            MainMenu.MainMenu(UserID=userID, UserName=userNickName).MenuPage()
        else:
            print("Wrong username or password")
            labelWrongData = Label(text=message, fg="red", font="Ariel")
            labelWrongData.pack()

    def register():
        RegisterMenu.registerMenu()

    MenuK = Tk()
    MenuK.title("Gra - ProjektGra - LoginMenu")
    MenuK.geometry('600x800')
    label = Label(MenuK, text="Podaj email", font="Ariel", fg="black")
    label.pack()
    emailLabel = Entry(MenuK, font="Ariel", bg="#666", fg="white", width=20)
    emailLabel.pack()
    passwordLabel = Entry(MenuK, font="Ariel", bg="#666", show="*")
    passwordLabel.pack()
    buttonLogin = Button(MenuK, text="Login", width=10, height=2, command=lambda: login(emailLabel.get(), passwordLabel.get()))
    buttonLogin.pack()
    buttonRegister = Button(MenuK, text="Register", width=10, height=2, command=register)
    buttonRegister.pack()
    MenuK.mainloop()


