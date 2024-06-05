from tkinter import *
import DataBaseConnect
import MainMenu
import time

def registerMenu():
    def registerMenuFunction(nick: str, email: str, password: str):
        print("JD", nick, email, password)
        if DataBaseConnect.addUser(nick, email, password):
            successLabel = Label(root, text="Użytkownik dodany!")
            successLabel.pack()
            time.sleep(2)
            root.destroy()
        else:
            notsuccessLabel = Label(root, text="Użytkownik o podanym nicku lub emailu już istnieje!")
            notsuccessLabel.pack()
            return



    root = Tk()
    root.title("Register")
    root.geometry('600x800')
    nameLabel = Label(root, text="Podaj Nazwę")
    nameLabel.pack()
    nickEntry = Entry(root, font="Ariel", bg="#666")
    nickEntry.pack()
    emailLabel = Label(root, text="Podaj email")
    emailLabel.pack()
    emailEntry = Entry(root, font="Ariel", bg="#666")
    emailEntry.pack()
    passwordLabel = Label(root, text="Podaj hasło")
    passwordLabel.pack()
    passwordEntry = Entry(root, font="Ariel", bg="#666")
    passwordEntry.pack()
    button = Button(root, text="Register", command=lambda: registerMenuFunction(nickEntry.get(), emailEntry.get(), passwordEntry.get()))
    button.pack()



